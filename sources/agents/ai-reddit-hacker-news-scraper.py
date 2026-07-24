import os
import sys
import json
import logging
import re
import argparse
import urllib.request
from typing import List, Dict, Any, Optional

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import resolve_absolute_path, json_raw_content, exception_stacktrace

# logger
logger = logging.getLogger("CommunityForumScraper")

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
output_scraper_data_file        = resolve_absolute_path("sources/output/discovered-community-endpoints.json")
agent_working_history_file      = resolve_absolute_path("sources/output/discovered-community-endpoints.md")

HN_ITEM_URL                     = "https://hacker-news.firebaseio.com/v0/item/"
HN_STORIES_JSON_URL             = "https://hacker-news.firebaseio.com/v0/showstories.json" 

class HackerNewsTechScraper:
    """Real-time community monitor tracking new text threads to catch newly released free AI models instantly."""
    
    def __init__(self) -> None:
        # Escaped internal Hacker News REST endpoints to maintain layout stability
        self._base_item_url = HN_ITEM_URL
        self._show_stories_url = HN_STORIES_JSON_URL
    
    def write_log(self, raw_content):
        pattern = r"\{.*\}|\[.*\]"
        raw_content = json_raw_content(raw_content)
        is_json = bool(re.search(pattern, raw_content, re.DOTALL))
        log_content = (
            f"# Source:\n\n{self._show_stories_url}\n\n"
            f"# Raw Response / Exception:\n\n```json\n{raw_content}\n```\n\n" if is_json else f"# Raw Response / Exception:\n\n```text\n{raw_content}\n```\n\n"
        )
        os.makedirs(os.path.dirname(agent_working_history_file), exist_ok=True)
        with open(agent_working_history_file, "a", encoding="utf-8") as file:
            file.write(log_content)
    
    def fetch_latest_ai_threads(self, scan_limit: int = 40) -> List[Dict[str, Any]]:
        """Scan latest 'Show HN' launch threads for keyword matches relating to free LLM endpoints."""
        logger.info("Scanning community pipeline for open-source and free tech releases...")
        log_data = {'story_ids': [], 'threads': []}
        resolved_list_url = self._show_stories_url
        
        try:
            # Step 1: Fetch the list of newest show/launch story item IDs
            req = urllib.request.Request(resolved_list_url, headers={"User-Agent": "EnterpriseMonitor/1.0"})
            with urllib.request.urlopen(req) as resp:
                raw_data = resp.read().decode("utf-8")
                json_story_ids = json.loads(raw_data)
                log_data['story_ids'] = json_story_ids if json_story_ids else raw_data
                story_ids: List[int] = json_story_ids[:scan_limit]
                
            matching_threads = []
            keywords = ["free", "api", "llm", "endpoint", "model", "provider"]
            
            # Step 2: Iterate through thread items and pull detailed text data blocks
            for item_id in story_ids:
                try:
                    resolved_item_url = f"{self._base_item_url}{item_id}.json".replace(".", ".")
                    item_req = urllib.request.Request(resolved_item_url, headers={"User-Agent": "EnterpriseMonitor/1.0"})
                    
                    with urllib.request.urlopen(item_req) as item_resp:
                        raw_item_data = item_resp.read().decode("utf-8")
                        item_data = json.loads(raw_item_data)
                        if not item_data:
                            log_data['threads'].append({ "id": item_id, "raw_data": raw_item_data })
                            continue
                        
                        log_data['threads'].append(item_data)
                        title = item_data.get("title", "").lower()
                        text_content = item_data.get("text", "").lower()
                        
                        # Filter elements containing high-relevancy operational keywords
                        if any(kw in title for kw in keywords) or any(kw in text_content for kw in keywords):
                            matching_threads.append({
                                "id": item_id,
                                "title": item_data.get("title"),
                                "url": item_data.get("url", f"https://ycombinator.com{item_id}"),
                                "description_snippet": item_data.get("text", "")[:1000]
                            })
                except Exception as item_err:
                    print(f"Error while fetching {item_id}: {item_err}")
                    log_data['threads'].append({ "id": item_id, "error": item_err })
                    continue
            
            # write log
            logger.info(f"Raw log data: {str(log_data)}")
            self.write_log(log_data)
                        
            logger.info(f"Community scanning pipeline complete. Found {len(matching_threads)} relevant API topics.")
            return matching_threads
            
        except Exception as network_err:
            logger.error(f"Critical interface crash monitoring community pipeline: {exception_stacktrace(network_err)}")
            self.write_log(exception_stacktrace(network_err))
            return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-limit", required=True)
    args = parser.parse_args()
    
    scan_limit = args.scan_limit
    try:
        scan_limit = int(scan_limit)
    except ValueError:
        scan_limit = 50 # Reliable fallback value configuration
    
    forum_scraper = HackerNewsTechScraper()
    discovered_threads = forum_scraper.fetch_latest_ai_threads(scan_limit=scan_limit)
    # Save the output arrays locally if threads are successfully captured
    if discovered_threads:
        print('🎉 Pipeline parsing complete. Successfully extracted', len(discovered_threads), 'highly-relevant technical threads.')
        with open(output_scraper_data_file, "w", encoding="utf-8") as out:
            json.dump(discovered_threads, out, indent=4, ensure_ascii=False)
    else:
        print('⚠️ Operational Warning: Zero matching threads found in the current community buffer.')

