import os
import sys
import json
import logging
import re
from typing import Dict, List, Any, Optional
import urllib.request
import urllib.error

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from agent_helper import resolve_absolute_path, json_raw_content, exception_stacktrace

# logger
logger = logging.getLogger("GitHubScraper")

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
output_scraper_data_file        = resolve_absolute_path("sources/output/free_models_by_github_scraper.json")
agent_working_history_file      = resolve_absolute_path("sources/output/free_models_by_github_scraper.md")

GITHUB_LLM_MODELS_JSON_URL      = "https://raw.githubusercontent.com/mnfst/awesome-free-llm-apis/main/data.json"

class GitHubModelScraper:
    """Enterprise automation class to fetch and standardize free AI model providers from GitHub."""
    
    def __init__(self) -> None:
        # Use escaped strings to prevent system auto-formatting and markdown render errors
        self.target_url: str = GITHUB_LLM_MODELS_JSON_URL
        self.timeout_seconds: int = 15
    
    def write_log(self, raw_content):
        pattern = r"\{.*\}|\[.*\]"
        raw_content = json_raw_content(raw_content)
        is_json = bool(re.search(pattern, raw_content, re.DOTALL))
        log_content = (
            f"# Source:\n\n{self.target_url}\n\n"
            f"# Raw Response / Exception:\n\n```json\n{raw_content}\n```\n\n" if is_json else f"# Raw Response / Exception:\n\n```text\n{raw_content}\n```\n\n"
        )
        os.makedirs(os.path.dirname(agent_working_history_file), exist_ok=True)
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
                if response.status == 200:
                    logger.info("Raw configuration data fetched successfully from GitHub.")
                    return json.loads(response.read().decode("utf-8"))
                else:
                    logger.error(f"Invalid server response status code received: {response.status}")
                    return None
        except urllib.error.URLError as url_err:
            logger.error(f"Network transport layer error or malformed URL: {url_err.reason}")
            self.write_log(exception_stacktrace(url_err))
            return None
        except json.JSONDecodeError as json_err:
            logger.error(f"Failed to parse source payload. Invalid JSON structure: {json_err.msg}")
            self.write_log(exception_stacktrace(json_err))
            return None
        except Exception as general_err:
            logger.error(f"Unexpected operational anomaly during download: {str(general_err)}")
            self.write_log(exception_stacktrace(general_err))
            return None

    def process_and_standardize(self, raw_providers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Normalize raw provider schemas into a unified format optimized for Agent discovery."""
        standardized_list: List[Dict[str, Any]] = []
        
        for provider in raw_providers:
            if not isinstance(provider, dict):
                continue
            
            # ✅ ENTERPRISE CORE FIX: Detect free tier status via the parent's description text channel
            description = str(provider.get("description", "-"))
            description_text = description.lower()
            is_free_provider = "free" in description_text or provider.get("category") == "provider_api"
            
            # If the provider is verified as a free host node, process its embedded models
            if is_free_provider:
                provider_name = provider.get("name", "-")
                api_info = provider.get("api", {})
                base_url = api_info.get("baseUrl") or api_info.get("endpoint") or provider.get("baseUrl", "-")
                url = provider.get("url", "-")
                
                # Skip provider evaluation if the base connection string is missing
                if not base_url:
                    continue
                
                # parse models
                models = provider.get("models", [])
                if not isinstance(models, list):
                    continue
                
                for model in models:
                    model_id = model.get("id") or model.get("name", "unknown-model")
                    
                    # ✅ DYNAMIC TOKEN PARSING: Convert strings like "128K" or "32K" into clean operational integers
                    raw_context = str(model.get("context", "128K")).upper().strip()
                    try:
                        if "K" in raw_context:
                            context_tokens = int(float(raw_context.replace("K", "").strip()) * 1000)
                        elif "M" in raw_context:
                            context_tokens = int(float(raw_context.replace("M", "").strip()) * 1000000)
                        else:
                            context_tokens = int(raw_context)
                    except Exception:
                        context_tokens = 128000 # Stable engineering fallback value
                    
                    raw_context = str(model.get("maxOutput", "128K")).upper().strip()
                    try:
                        if "K" in raw_context:
                            output_tokens = int(float(raw_context.replace("K", "").strip()) * 1000)
                        elif "M" in raw_context:
                            output_tokens = int(float(raw_context.replace("M", "").strip()) * 1000000)
                        else:
                            output_tokens = int(raw_context)
                    except Exception:
                        output_tokens = 128000 # Stable engineering fallback value
                    
                    # collect model info
                    standardized_list.append({
                        "provider": provider_name,
                        "id": model_id,
                        "name": model.get("name", "-"),
                        "url": url,
                        "base_url": base_url,
                        "context_window": context_tokens,
                        "description": description,
                        "maxOutput": output_tokens,
                        "modality": model.get("modality", "-"),
                        "rateLimit": model.get("rateLimit", "-")
                    })
                    
        return standardized_list

    def execute_pipeline(self, output_filepath: str = "free_models_github.json") -> bool:
        """Orchestrate the end-to-end data pipelines for the GitHub extraction workflow."""
        raw_data = self.fetch_raw_data()
        if not raw_data:
            logger.critical("Pipeline aborted: Unable to retrieve operational data from source.")
            return False
        
        # write response
        self.write_log(raw_data)
        
        # ==============================================================================
        # 🩹 DEEP TYPE DE-SERIALIZATION: Force conversion if payload is a double-encoded string
        # ==============================================================================
        if isinstance(raw_data, str):
            try:
                logger.info("Payload isolated as raw string format. Executing second layer JSON deserialization...")
                raw_data = json.loads(raw_data)
            except Exception as parse_inner_err:
                logger.error(f"Failed to process internal character token blocks: {exception_stacktrace(parse_inner_err)}")
        
        # ==============================================================================
        # 🩹 ENTERPRISE CORE FIX: Extract the nested array under the 'providers' key
        # ==============================================================================
        providers_list = []
        if isinstance(raw_data, dict):
            # Safe extraction of the target list array embedded within the corporate JSON object
            providers_list = raw_data.get("providers", [])
            logger.info(f"Target key 'providers' discovered. Array volume captured: {len(providers_list)} blocks.")
        
        elif isinstance(raw_data, list):
            # Fallback handling in case the raw payload directly resolves to a root array list
            providers_list = raw_data
            logger.info(f"Root node resolved as flat array list. Volume captured: {len(providers_list)} blocks.")
        
        else:
            logger.error(f"Critical operational mismatch. Unrecognized data mapping signature: {type(raw_data)}")
            
        processed_data = self.process_and_standardize(providers_list)
        
        try:
            with open(output_filepath, "w", encoding="utf-8") as f:
                json.dump(processed_data, f, indent=4, ensure_ascii=False)
            logger.info(f"Pipeline executed successfully. Exported {len(processed_data)} free models to: {output_filepath}")
            return True
        except IOError as io_err:
            logger.error(f"Disk I/O failure while writing structured payload: {exception_stacktrace(io_err)}")
            self.write_log(exception_stacktrace(io_err))
            return False

# Application entry point for executing Block 1 pipeline testing
if __name__ == "__main__":
    scraper = GitHubModelScraper()
    scraper.execute_pipeline(output_scraper_data_file)

