import os
import sys
import json
import logging
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

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
output_scapper_data_file  = resolve_absolute_path("sources/output/web_search_corpus.json")

class SemanticSearchScraper:
    """Enterprise-grade semantic scraper using Exa AI to discover and scrape raw data from hundreds of tech sites simultaneously."""
    
    def __init__(self, exa_api_key: str) -> None:
        self.client = Exa(api_key=exa_api_key)
        
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
                use_autoprompt=True,
                num_results=15,
                text=True # Instruct Exa to extract clean text contents from all found pages
            )
            
            scraped_payload = []
            for result in response.results:
                scraped_payload.append({
                    "source_title": result.title,
                    "source_url": result.url,
                    "extracted_text": result.text[:8000] # Truncate text block size per page to optimize token space
                })
                
            logger.info(f"Successfully scraped and extracted text from {len(scraped_payload)} different web domains.")
            return scraped_payload
            
        except Exception as search_err:
            logger.error(f"Failed to execute semantic search pipeline: {str(search_err)}")
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
    parser.add_argument("--gemini-api-key", required=True)
    args = parser.parse_args()
    
    exaApiKey = args['exa-api-key'] if args else None
    
    if exaApiKey:
        scraper = SemanticSearchScraper(exa_api_key=exaApiKey)
        raw_corpus = scraper.discover_and_scrape_sources()
        scraper.save_raw_corpus(raw_corpus, output_scapper_data_file)

