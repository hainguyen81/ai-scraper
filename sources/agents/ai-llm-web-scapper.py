import os
import sys
import json
import logging
import argparse
import urllib.request
from bs4 import BeautifulSoup
from typing import Dict, Any

# Standardize application log outputs across the agent architecture
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger("NativeAIScraper")

# ==============================================================================
# 🏢 ENTERPRISE INTER-PACKAGE ROUTING LAYER
# ==============================================================================
CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_AGENTS_DIR  = os.path.abspath(os.path.join(CURRENT_SCRIPT_DIR, "../"))

if PARENT_AGENTS_DIR not in sys.path:
    sys.path.insert(0, PARENT_AGENTS_DIR)

from agent_helper import resolve_absolute_path

output_scapper_data_file = resolve_absolute_path("sources/output/free_models_by_llm_web_scapper.json")

class NativeGeminiScraperAgent:
    """Enterprise fallback agent utilizing official Google GenAI SDK to eliminate buggy third-party abstractions."""
    
    def __init__(self, google_api_key: str) -> None:
        # Programmatically defer import to prevent environment setup issues when SDK is missing
        from google import genai
        from google.genai import types
        
        self.client = genai.Client(api_key=google_api_key)
        self.model_name = "gemini-2.5-flash"
        self.types = types
    
    def extract_web_content(self, url: str) -> str:
        """Fetch remote HTML content safely and strip heavy DOM elements to preserve token window space."""
        logger.info(f"Extracting DOM structures from remote target: {url}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "EnterpriseScraper/2.0"})
            with urllib.request.urlopen(req, timeout=15) as response:
                html_raw = response.read().decode("utf-8")
            
            # Parse and clean text payload utilizing BeautifulSoup layout matrices
            soup = BeautifulSoup(html_raw, "html.parser")
            for element in soup(["script", "style", "nav", "footer", "header"]):
                element.decompose()
            
            return soup.get_text(separator=" ", strip=True)
        except Exception as fetch_err:
            logger.error(f"Failed to ingest raw data structures from target URL: {str(fetch_err)}")
            return ""
    
    def process_and_structure_data(self, raw_text: str) -> Dict[str, Any]:
        """Execute semantic data structuring leveraging official Google structured output parameters."""
        logger.info("Deserializing semi-structured text matrix using official Gemini Client...")
        
        prompt_instruction = (
            "Analyze the text corpus provided and isolate all AI model providers offering a free tier API. "
            "Extract the provider name, api base URL, precise model ID, and context window tokens. "
            "Return the data strictly structured as a JSON object containing a list named 'free_providers'. "
            "Each item in the list must exactly include: "
            "1. 'provider_name' (string) "
            "2. 'api_base_url' (string) "
            "3. 'model_name' (string) "
            "4. 'context_window_tokens' (integer, default to 128000 if not mentioned)."
        )
        
        # ✅ ENTERPRISE BACKOFF: Implement robust retry mechanism to bypass temporary 429 Rate Limits
        import time
        max_retries = 3
        retry_delay_seconds = 30 # Sleep for 30 seconds if Google throttles the connection
        
        for attempt in range(max_retries):
            try:
                # Enforce deterministic JSON output matching your strict specification schema
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=[prompt_instruction, raw_text],
                    config=self.types.GenerateContentConfig(
                        response_mime_type="application/json",
                        temperature=0.0
                    ),
                )
                return json.loads(response.text)
            except Exception as llm_err:
                if "429" in str(llm_err) and attempt < max_retries - 1:
                    logger.warning(f"⚠️ Rate limit 429 detected. Backing off for {retry_delay_seconds}s (Attempt {attempt + 1}/{max_retries})...")
                    time.sleep(retry_delay_seconds)
                else:
                    logger.error(f"Structured inference schema parsing crashed: {str(llm_err)}")
                    return {"free_providers": [], "status": "failed"}
    
    def save_output(self, dataset: Dict[str, Any], filepath: str) -> None:
        """Ensure destination space existence and securely persist data objects on disk storage."""
        try:
            target_directory = os.path.dirname(filepath)
            if target_directory and not os.path.exists(target_directory):
                os.makedirs(target_directory, exist_ok=True)
            
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(dataset, f, indent=4, ensure_ascii=False)
            logger.info(f"Persistent payload successfully deployed to target: {filepath}")
        except IOError as io_err:
            logger.error(f"Disk storage access interface crashed: {str(io_err)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Native GenAI Ingestion Core Engine")
    parser.add_argument("--gemini-api-key", required=True)
    args = parser.parse_args()
    
    target_webpage = "https://github.com/open-free-llm-api/awesome-freellm-apis"
    
    agent = NativeGeminiScraperAgent(google_api_key=args.gemini_api_key)
    cleaned_corpus = agent.extract_web_content(target_webpage)
    
    if cleaned_corpus:
        structured_json = agent.process_and_structure_data(cleaned_corpus)
        agent.save_output(structured_json, output_scapper_data_file)
