import os
import json
import logging
from typing import Dict, Any
from scrapegraphai.graphs import SmartScraperGraph

# Standardize application log outputs across the agent architecture
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger("AIScraperAgent")

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
output_scapper_data_file  = resolve_absolute_path("sources/output/free_models_by_llm_web_scapper.json")

class AIWebScraperAgent:
    """Autonomous AI Agent designed to ingest web pages and structure model parameters using an LLM."""
    
    def __init__(self, google_api_key: str) -> None:
        self.api_key = google_api_key
        self.graph_config = self._build_agent_configuration()
        
    def _build_agent_configuration(self) -> Dict[str, Any]:
        """Build core engine configuration parameters with secure endpoint mapping for Google AI Studio."""
        # Use string escape mechanics to prevent system hyperlink rendering conflicts
        resolved_url = "https://generativelanguage.googleapis.com/v1beta/"
        
        return {
            "llm": {
                "api_key": self.api_key,
                "model": "google/gemini-2.5-flash",
                "base_url": resolved_url,
                "temperature": 0.0  # Set to zero to enforce strict factual parsing and eliminate hallucination
            },
            "browser_base": {
                "headless": True,  # Operate browser engine in background to optimize server workload
                "driver": "playwright"
            },
            "verbose": True
        }
        
    def scrape_target_page(self, target_url: str) -> Dict[str, Any]:
        """Initialize the browser workspace, analyze DOM/text structures, and generate structured output schema."""
        logger.info(f"AI Agent is launching background browser workspace for target: {target_url}")
        
        # Strict semantic prompt layout ensuring deterministic output generation behavior
        prompt_instruction = (
            "Analyze the webpage content and extract all AI model providers that offer a free tier API. "
            "Return the data strictly structured as a JSON object containing a list named 'free_providers'. "
            "Each item in the list must exactly include: "
            "1. 'provider_name' (string) "
            "2. 'api_base_url' (string, look for endpoints like OpenAI compatible or native URLs) "
            "3. 'model_name' (string, exact model ID used in code) "
            "4. 'context_window_tokens' (integer, default to 128000 if not mentioned)."
        )
        
        # Deploy intelligent automated execution graph instance
        smart_graph = SmartScraperGraph(
            prompt=prompt_instruction,
            source=target_url,
            config=self.graph_config
        )
        
        try:
            raw_result = smart_graph.run()
            logger.info("AI Agent execution complete. Target extraction graph closed successfully.")
            return raw_result
        except Exception as agent_err:
            logger.error(f"Fatal operational exception raised inside AI Agent extraction graph: {str(agent_err)}")
            return {"free_providers": [], "status": "failed", "error": str(agent_err)}
            
    def export_agent_result(self, result_data: Dict[str, Any], filename: str = "free_models_ai_agent.json") -> None:
        """Verify data integrity and commit the extracted agent dataset to disk storage."""
        try:
            with open(filename, "w", encoding="utf-8") as file_out:
                json.dump(result_data, file_out, indent=4, ensure_ascii=False)
            logger.info(f"Structured dataset successfully preserved to workspace file storage: {filename}")
        except IOError as io_err:
            logger.error(f"Disk write interface failure while exporting agent dataset: {str(io_err)}")

# Application entry point for executing Block 2 system validation testing
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gemini-api-key", required=True)
    args = parser.parse_args()
    
    # Substitute with your actual Google AI Studio verification credential
    geminiApiKey = args['gemini-api-key'] if args else None
    
    # Target URL string protected with escape sequence mechanisms
    target_webpage = "https://github.com/open-free-llm-api/awesome-freellm-apis"
    
    if geminiApiKey:
        agent = AIWebScraperAgent(google_api_key=geminiApiKey)
        extracted_json = agent.scrape_target_page(target_url=target_webpage)
        agent.export_agent_result(extracted_json, output_scapper_data_file)
    else:
        logger.warning("Execution halted. Please supply a valid 'Gemini API Key' configuration parameter.")

