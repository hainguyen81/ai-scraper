import os
import sys
import json
import re
import hashlib
import argparse
from datetime import datetime
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    resolve_absolute_path,
    read_json_file,
    write_json_file,
    write_file,
    read_file_raw,
    kwargs_by_key
)

# super agent
from sources.agents.agent_super import AbstractAgent

# models list
SYSTEM_PROMPT_TEMPLATE      = resolve_absolute_path("sources/agents/business-analysis/agent_ba.prompt.system.md")
USER_PROMPT_TEMPLATE        = resolve_absolute_path("sources/agents/business-analysis/agent_ba.prompt.user.md")
IDEAS_STORAGE_PATH          = resolve_absolute_path("sources/storage/ideas")
BA_OUTPUT_PATH              = resolve_absolute_path("sources/output/business-analysis")
SRS_STORAGE_PATH            = resolve_absolute_path("sources/requirements")
SRS_STORAGE_FILE            = "requirements.md"
SRS_INFO_FILE               = "project-info.json"
BA_RAW_FILE                 = os.path.join(BA_OUTPUT_PATH, "ba.md")
BA_LOG_FILE                 = os.path.join(BA_OUTPUT_PATH, "ba_log.md")
DEFAULT_SRS_LANGUAGE        = "English"

class PrincipalBusinessAnalysisAgent(AbstractAgent):
    def __init__(self, **kwargs):
        super().__init__(agent_id='BusinessAnalysis', **kwargs)
    
    def initialize(self):
        # require idea identity to analyze
        self.idea_id = self.get_kwargs("idea") or self.get_kwargs("idea_id")
        if not self.idea_id:
            raise RuntimeError("- Invalid idea identity to analyze!")
        
        # start initialization
        super().initialize()
        self.language = self.get_kwargs("language") or DEFAULT_IDEAS_LANGUAGE

    def read_idea_from_file(self, file: str) -> str:
        """read idea from file (Txt, MD, v.v.)."""
        if not os.path.exists(file):
            raise FileNotFoundError(f"Not found idea file: {file}")
        _, idea_content = read_file_raw(file_path=file)
        return idea_content
    
    # @override
    def agent_secrets_key(self) -> str:
        pass
    
    # @override
    def agent_log_file(self) -> str:
        return BA_LOG_FILE
    
    # @override
    def system_prompt_template(self) -> str:
        return SYSTEM_PROMPT_TEMPLATE
    
    # @override
    def user_prompt_template(self) -> str:
        return USER_PROMPT_TEMPLATE
    
    # @override
    def agent_temperature(self):
        return 0.8 # high ides
    
    # @override
    def pre_execute(self, **kwargs):
        idea_file = os.path.join(IDEAS_STORAGE_PATH, f"{self.idea_id}.md")
        if not os.path.exists(idea_file):
            print(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] Not found IDEA file { idea_file }")
            sys.exit(1)
        
        # read idea file to build user prompt
        idea_file, idea_content = read_file_raw(file_path=idea_file)
        
        # return merged new values
        return {
            **kwargs,
            "language": self.language,
            "idea_file": idea_file,
            "raw_idea_content": idea_content
        }
    
    # @override
    def clean_response(self, raw_response, **kwargs):
        return json.loads(raw_response.strip()) if raw_response else None
    
    # @override
    def process_chat(self, response_data, **kwargs):
        if not response_data:
            raise RuntimeError("- Invalid AI raw response. Not a valid JSON format data.")
        
        # parse technical project name as folder name
        datetimeStr = datetime.now().strftime("%Y%m%d%H%M%S")
        defaultPrjName = f"project-{datetimeStr}"
        project_info = response_data.get("project_names") or {}
        project_name = project_info.get("technical_codename") or defaultPrjName
        project_storage_path = os.path.join(SRS_STORAGE_PATH, project_name)
        
        # export requirements
        requirements_file = os.path.join(project_storage_path, SRS_STORAGE_FILE)
        requirements_content = response_data.get("srs_content_markdown")
        write_file(file=requirements_file, data=requirements_content)
        
        # export project info
        project_info = {
            **project_info,
            "requirements": requirements_file
        }
        project_info_file = os.path.join(project_storage_path, SRS_INFO_FILE)
        write_json_file(file=project_info_file, json_data=project_info)
        
        # export raw response if necessary as log tracing
        raw_response = kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=BA_RAW_FILE,
                data=raw_response
            )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--idea", type=str, help="Idea Identity for searching")
    parser.add_argument("--language", type=str, help="Translate SRS to language. Ex: Vietnamese, English, etc.")
    args = parser.parse_args()
    PrincipalBusinessAnalysisAgent(
        idea=args.idea,
        language=args.language
    ).execute()
