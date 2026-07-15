import os
import sys
import json
import logging
import argparse
import re
import urllib.request
from bs4 import BeautifulSoup
from typing import Dict, Any
from openai import OpenAI

# Standardize application log outputs across the agent architecture
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger("DynamicAIScraper")

# ==============================================================================
# 🏢 ENTERPRISE INTER-PACKAGE ROUTING LAYER
# ==============================================================================
CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_AGENTS_DIR  = os.path.abspath(os.path.join(CURRENT_SCRIPT_DIR, "../"))

if PARENT_AGENTS_DIR not in sys.path:
    sys.path.insert(0, PARENT_AGENTS_DIR)

from agent_helper import resolve_absolute_path

output_scapper_data_file        = resolve_absolute_path("sources/output/free_models_by_llm_web_scapper.json")
agent_working_history_file      = resolve_absolute_path("sources/output/free_models_by_llm_web_scapper.md")

# ==============================================================================
# 🎛️ CENTRALIZED AI ENDPOINT CONFIGURATION LAYER
# Swap providers instantly by changing these 2 variables. The API Key is passed via CLI.
# ==============================================================================
SOURCE_LLM_MODELS_FREE_URL = "https://github.com/open-free-llm-api/awesome-freellm-apis"

class DynamicScraperAgent:
    """Enterprise-grade dynamic agent designed to switch LLM providers effortlessly by modifying endpoint configurations."""
    
    def __init__(self, api_key: str, base_url: str, model_name: str) -> None:
        # Initialize standard OpenAI wrapper compatible with OpenRouter, Groq, and Gemini OpenAI-base endpoints
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )
        self.api_endpoint = base_url
        self.model_name = model_name

    def extract_web_content(self, url: str) -> str:
        """Fetch remote HTML content safely and strip heavy DOM elements to preserve token window space."""
        logger.info(f"Extracting DOM structures from remote target: {url}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "EnterpriseScraper/3.0"})
            with urllib.request.urlopen(req, timeout=15) as response:
                html_raw = response.read().decode("utf-8")
                
            soup = BeautifulSoup(html_raw, "html.parser")
            for element in soup(["script", "style", "nav", "footer", "header"]):
                element.decompose()
                
            return soup.get_text(separator=" ", strip=True)
        except Exception as fetch_err:
            logger.error(f"Failed to ingest raw data structures from target URL: {str(fetch_err)}")
            return ""
    
    def write_log(self, raw_content, prompt_instruction):
        pattern = r"^\s*(\{.*\}|\[.*\])\s*$"
        log_content = (
            f"# Prompt Instruction:\n\n{prompt_instruction}\n\n"
            f"# Raw Response:\n\n```json\n{raw_content}\n```\n\n" if re.match(pattern, raw_content, re.DOTALL) else f"# Raw Response:\n\n```text\n{raw_content}\n```\n\n"
        )
        with open(agent_working_history_file, "a", encoding="utf-8") as file:
            file.write(log_content)

    def process_and_structure_data(self, raw_text: str) -> Dict[str, Any]:
        """Execute semantic data structuring leveraging OpenAI compatible JSON structures globally."""
        logger.info(f"Deserializing text matrix using Provider Base URL: {self.api_endpoint} | Model: {self.model_name}")
        
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

        try:
            # Enforce strict deterministic JSON response schema via completion payloads
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a professional web data extractor. Always output clean raw JSON without markdown codeblocks."},
                    {"role": "user", "content": f"{prompt_instruction}\n\nWebpage content:\n{raw_text}"}
                ],
                temperature=0.0
            )
            
            # ✅ ENTERPRISE DYNAMIC PARSING: Safely handle polymorphic responses (List vs Object choices wrapper)
            choices_data = response.choices
            # write response to history log
            try:
                # Convert the entire response structure into a standardized dictionary and serialize to string
                raw_response_string = json.dumps(response, default=lambda o: getattr(o, '__dict__', str(o)), indent=2)
                self.write_log(raw_response_string, prompt_instruction)
                logger.info(f"💾 RAW RESPONSE MATRIX CAPTURED:\n{raw_response_string}")
            except Exception as log_err:
                # Fallback to standard string casting if complex nested serialization handshakes fail
                logger.info(f"💾 RAW RESPONSE STRING CASTING FALLBACK:\n{str(response)}")
                self.write_log(str(response), prompt_instruction)
            
            # parse response JSON
            raw_content = None
            if isinstance(choices_data, list):
                # If the provider wraps choices inside a native list structure
                if len(choices_data) > 0:
                    first_choice = choices_data[0]
                    raw_content = first_choice.message.content.strip() if hasattr(first_choice, 'message') else str(first_choice)
            else:
                # Standard OpenAI object layout behavior fallback
                raw_content = choices_data.message.content.strip()
            
            # could not parse
            if not raw_content:
                raise ValueError("Operational Critical: Extracted chat completion content stream is empty.")

            # ✅ ROBUST REGEX EXTRACTION: Isolate nested JSON bracket layouts to eliminate markdown wrapper block errors
            json_match = re.search(r'\{.*\}', raw_content, re.DOTALL)
            if json_match:
                clean_json_str = json_match.group(0)
                return json.loads(clean_json_str)
            
            return json.loads(response.choices.message.content)
        except Exception as llm_err:
            logger.error(f"Structured inference schema parsing crashed: {str(llm_err)}")
            return {"free_providers": [], "status": "failed", "error": f"Structured inference schema parsing crashed: {str(llm_err)}"}

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
    parser = argparse.ArgumentParser(description="Dynamic Multi-Provider AI Ingestion Core Engine")
    # Kept argument name '--api-key' to retain 100% backward compatibility with your GitHub Workflow files
    parser.add_argument("--api-key", required=True)
    parser.add_argument("--api-endpoint", required=True)
    parser.add_argument("--api-model", required=True)
    args = parser.parse_args()
    
    target_webpage = SOURCE_LLM_MODELS_FREE_URL
    
    # Instantiate the agent dynamically passing centralized provider attributes
    agent = DynamicScraperAgent(
        api_key=args.api_key,
        base_url=args.api_endpoint,
        model_name=args.api_model
    )
    cleaned_corpus = agent.extract_web_content(target_webpage)
    
    if cleaned_corpus:
        structured_json = agent.process_and_structure_data(cleaned_corpus)
        agent.save_output(structured_json, output_scapper_data_file)
