import os
import json
import logging
import urllib.request
from typing import List, Dict, Any, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger("CommunityForumScraper")

# ==============================================================================
# 🏢 ENTERPRISE INTER-PACKAGE ROUTING LAYER
# ==============================================================================
# Programmatically appends the parent directory (.ai/.agents/) into Python's runtime
# search path array. This completely unlocks importing 'agent_helper.py'.
# ==============================================================================
CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # .ai/.agents/.sub-agents/
PARENT_AGENTS_DIR  = os.path.abspath(os.path.join(CURRENT_SCRIPT_DIR, "../")) # .ai/.agents/

# jump to `agent_helper.py` folder path
if PARENT_AGENTS_DIR not in sys.path:
    sys.path.insert(0, PARENT_AGENTS_DIR)

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from agent_helper import resolve_absolute_path

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
output_scapper_data_file  = resolve_absolute_path("sources/output/discovered-community-endpoints.json")

class HackerNewsTechScraper:
    """Real-time community monitor tracking new text threads to catch newly released free AI models instantly."""
    
    def __init__(self) -> None:
        # Escaped internal Hacker News REST endpoints to maintain layout stability
        self._base_item_url = "https://hacker-news.firebaseio.com/v0/item/"
        self._show_stories_url = "https://hacker-news.firebaseio.com/v0/showstories.json"

    def fetch_latest_ai_threads(self, scan_limit: int = 40) -> List[Dict[str, Any]]:
        """Scan latest 'Show HN' launch threads for keyword matches relating to free LLM endpoints."""
        logger.info("Scanning community pipeline for open-source and free tech releases...")
        resolved_list_url = self._show_stories_url
        
        try:
            # Step 1: Fetch the list of newest show/launch story item IDs
            req = urllib.request.Request(resolved_list_url, headers={"User-Agent": "EnterpriseMonitor/1.0"})
            with urllib.request.urlopen(req) as resp:
                story_ids: List[int] = json.loads(resp.read().decode("utf-8"))[:scan_limit]
                
            matching_threads = []
            keywords = ["free", "api", "llm", "endpoint", "model", "provider"]
            
            # Step 2: Iterate through thread items and pull detailed text data blocks
            for item_id in story_ids:
                resolved_item_url = f"{self._base_item_url}{item_id}.json".replace(".", ".")
                item_req = urllib.request.Request(resolved_item_url, headers={"User-Agent": "EnterpriseMonitor/1.0"})
                
                with urllib.request.urlopen(item_req) as item_resp:
                    item_data = json.loads(item_resp.read().decode("utf-8"))
                    if not item_data:
                        continue
                        
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
                        
            logger.info(f"Community scanning pipeline complete. Found {len(matching_threads)} relevant API topics.")
            return matching_threads
            
        except Exception as network_err:
            logger.error(f"Critical interface crash monitoring community pipeline: {str(network_err)}")
            return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan-limit", required=True)
    args = parser.parse_args()
    
    forum_scraper = HackerNewsTechScraper()
    scanLimit = args['scan-limit'] if args else None
    discovered_threads = forum_scraper.fetch_latest_ai_threads(scan_limit=scanLimit)
    # Save the output arrays locally if threads are successfully captured
    if discovered_threads:
        print('🎉 Pipeline parsing complete. Successfully extracted', len(discovered_threads), 'highly-relevant technical threads.')
        with open(output_scapper_data_file, "w", encoding="utf-8") as out:
            json.dump(discovered_threads, out, indent=4, ensure_ascii=False)
    else:
        print('⚠️ Operational Warning: Zero matching threads found in the current community buffer.')

