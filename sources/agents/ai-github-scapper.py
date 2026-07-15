import os
import sys
import json
import logging
from typing import Dict, List, Any, Optional
import urllib.request
import urllib.error

# Configure enterprise-grade logging infrastructure
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("GitHubScraper")

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
output_scapper_data_file        = resolve_absolute_path("sources/output/free_models_by_github_scapper.json")
agent_working_history_file      = resolve_absolute_path("sources/output/free_models_by_github_scapper.md")

GITHUB_LLM_MODELS_JSON_URL      = "https://raw.githubusercontent.com/mnfst/awesome-free-llm-apis/main/data.json"

class GitHubModelScraper:
    """Enterprise automation class to fetch and standardize free AI model providers from GitHub."""
    
    def __init__(self) -> None:
        # Use escaped strings to prevent system auto-formatting and markdown render errors
        self.target_url: str = GITHUB_LLM_MODELS_JSON_URL
        self.timeout_seconds: int = 15
    
    def write_log(self, raw_content):
        log_content = (
            f"# Source:\n-------------------------------------------------\n{self.target_url}\n-------------------------------------------------\n\n"
            f"# Raw Response / Exception:\n-------------------------------------------------\n{raw_content}\n-------------------------------------------------\n\n"
        )
        with open(agent_working_history_file, "a", encoding="utf-8") as file:
            file.write(log_content)
    
    def fetch_raw_data(self) -> Optional[List[Dict[str, Any]]]:
        """Fetch raw JSON payload from the remote repository with error isolation."""
        logger.info("Initializing secure connection to GitHub data repository...")
        
        headers: Dict[str, str] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) EnterpriseScraper/1.0"
        }
        
        req = urllib.request.Request(self.target_url, headers=headers)
        
        try:
            with urllib.request.urlopen(req, timeout=self.timeout_seconds) as response:
                self.write_log(str(response))
                if response.status == 200:
                    logger.info("Raw configuration data fetched successfully from GitHub.")
                    return json.loads(response.read().decode("utf-8"))
                else:
                    logger.error(f"Invalid server response status code received: {response.status}")
                    return None
        except urllib.error.URLError as url_err:
            logger.error(f"Network transport layer error or malformed URL: {url_err.reason}")
            self.write_log(str(url_err))
            return None
        except json.JSONDecodeError as json_err:
            logger.error(f"Failed to parse source payload. Invalid JSON structure: {json_err.msg}")
            self.write_log(str(json_err))
            return None
        except Exception as general_err:
            logger.error(f"Unexpected operational anomaly during download: {str(general_err)}")
            self.write_log(str(general_err))
            return None

    def process_and_standardize(self, raw_providers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Normalize raw provider schemas into a unified format optimized for Agent discovery."""
        standardized_list: List[Dict[str, Any]] = []
        
        for provider in raw_providers:
            provider_name = provider.get("name", "Unknown Provider")
            api_info = provider.get("api", {})
            base_url = api_info.get("baseUrl") or api_info.get("endpoint", "")
            
            # Skip provider evaluation if the base connection string is missing
            if not base_url:
                continue
                
            models = provider.get("models", [])
            for model in models:
                # Evaluate multiple criteria to confirm free tier accessibility
                is_free = model.get("is_free") or model.get("free", False) or "free" in model.get("tier", "").lower()
                
                if is_free or provider.get("is_free_provider", False):
                    context = model.get("context_length") or model.get("context", 128000)
                    
                    standardized_list.append({
                        "provider": provider_name,
                        "base_url": base_url,
                        "model_id": model.get("id") or model.get("name"),
                        "context_window": context,
                        "recommended_agent_role": "Coder/Fixer" if "coder" in str(model.get("id")).lower() else "General Tester"
                    })
                    
        return standardized_list

    def execute_pipeline(self, output_filepath: str = "free_models_github.json") -> bool:
        """Orchestrate the end-to-end data pipelines for the GitHub extraction workflow."""
        raw_data = self.fetch_raw_data()
        if not raw_data:
            logger.critical("Pipeline aborted: Unable to retrieve operational data from source.")
            return False
        
        # ==============================================================================
        # 🩹 ENTERPRISE CORE FIX: Extract the nested array under the 'providers' key
        # ==============================================================================
        providers_list = []
        if isinstance(raw_data, dict):
            # Safe extraction of the target list array embedded within the corporate JSON object
            providers_list = raw_data.get("providers", [])
        elif isinstance(raw_data, list):
            # Fallback handling in case the raw payload directly resolves to a root array list
            providers_list = raw_data
            
        processed_data = self.process_and_standardize(providers_list)
        
        try:
            with open(output_filepath, "w", encoding="utf-8") as f:
                json.dump(processed_data, f, indent=4, ensure_ascii=False)
            logger.info(f"Pipeline executed successfully. Exported {len(processed_data)} free models to: {output_filepath}")
            return True
        except IOError as io_err:
            logger.error(f"Disk I/O failure while writing structured payload: {str(io_err)}")
            self.write_log(str(io_err))
            return False

# Application entry point for executing Block 1 pipeline testing
if __name__ == "__main__":
    scraper = GitHubModelScraper()
    scraper.execute_pipeline(output_scapper_data_file)

