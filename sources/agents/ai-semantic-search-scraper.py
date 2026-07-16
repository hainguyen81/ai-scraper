import os
import sys
import json
import logging
import re
import argparse
from typing import List, Dict, Any
from exa_py import Exa

# Setup system logging format
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger("MultiSourceSearchScraper")

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
from agent_helper import json_raw_content

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
output_scraper_data_file        = resolve_absolute_path("sources/output/web_search_corpus.json")
agent_working_history_file      = resolve_absolute_path("sources/output/web_search_corpus.md")

class SemanticSearchScraper:
    """Enterprise-grade semantic scraper using Exa AI to discover and scrape raw data from hundreds of tech sites simultaneously."""
    
    def __init__(self, exa_api_key: str) -> None:
        self.client = Exa(api_key=exa_api_key)
    
    def write_log(self, url, query, raw_content):
        pattern = r"\{.*\}|\[.*\]"
        if isinstance(raw_content, (list, dict)):
            json_string = json.dumps(raw_content, indent=4, ensure_ascii=False)
            is_json = True
        else:
            json_string = json_raw_content(raw_content)
            pattern = r"\{.*\}|\[.*\]"
            is_json = bool(re.search(pattern, json_string, re.DOTALL))
        log_content = (
            f"# Source:\n\n{url}\n\n"
            f"# Query:\n\n{query}\n\n"
            f"# Raw Response / Exception:\n\n```json\n{json_string}\n```\n\n" if is_json else f"# Raw Response / Exception:\n\n```text\n{json_string}\n```\n\n"
        )
        os.makedirs(os.path.dirname(agent_working_history_file), exist_ok=True)
        with open(agent_working_history_file, "a", encoding="utf-8") as file:
            file.write(log_content)
        
        # extract details as md
        if isinstance(raw_content, list) and len(raw_content) > 0:
            with open(agent_working_history_file, "a", encoding="utf-8") as file:
                for item in raw_content:
                    if not isinstance(item, dict):
                        continue
                    
                    title = item.get("source_title", "[ No title ]")
                    url = item.get("source_url", "<!-- URL -->")
                    text = item.get("extracted_text", "-").replace("#", "##")
                    markdown_block = f"---\n\n# Source: [{title}]({url})\n{text}\n\n"
                    file.write(markdown_block)
                
    
    def discover_and_scrape_sources(self) -> List[Dict[str, Any]]:
        """Search the entire web for free AI endpoints, extract their raw text, and compile source links."""
        logger.info("Initiating massive multi-source semantic web discovery...")
        
        # High-intent search prompt targeting free model endpoints and base URLs
        search_query = "List of free LLM API providers endpoints base_url openrouter alternatives 2026"
        
        try:
            # Perform semantic search, limit to top 15 authoritative domains, and grab full webpage text contents
            response = self.client.search_and_contents(
                query=search_query,
                type="neural",
                num_results=15,
                text=True # Instruct Exa to extract clean text contents from all found pages
            )
            
            scraped_payload = []
            for result in response.results:
                scraped_payload.append({
                    "source_title": result.title,
                    "source_url": result.url,
                    "extracted_text": result.text # Truncate text block size per page to optimize token space
                })
            
            urls = "\n".join([payload["source_url"] for payload in scraped_payload])
            self.write_log(urls, search_query, scraped_payload)
            
            logger.info(f"Successfully scraped and extracted text from {len(scraped_payload)} different web domains.")
            return scraped_payload
            
        except Exception as search_err:
            logger.error(f"Failed to execute semantic search pipeline: {str(search_err)}")
            self.write_log("!!! EXA URL !!!", search_query, str(search_err))
            return []

    def save_raw_corpus(self, data: List[Dict[str, Any]], filename: str = "web_search_corpus.json") -> None:
        """Save the scraped text dataset from all web sources onto the disk storage."""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            logger.info(f"Scraped knowledge corpus successfully dumped to: {filename}")
        except IOError as io_err:
            logger.error(f"File system I/O error writing corpus payload: {str(io_err)}")

if __name__ == "__main__":
    # Substitute with your actual Exa AI token key credentials
    parser = argparse.ArgumentParser()
    parser.add_argument("--exa-api-key", required=True)
    args = parser.parse_args()
    
    exaApiKey = args.exa_api_key if args else None
    
    if exaApiKey:
        scraper = SemanticSearchScraper(exa_api_key=exaApiKey)
        raw_corpus = scraper.discover_and_scrape_sources()
        scraper.save_raw_corpus(raw_corpus, output_scraper_data_file)

