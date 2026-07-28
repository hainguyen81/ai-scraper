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

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
# models list
SYSTEM_PROMPT_TEMPLATE      = resolve_absolute_path("sources/agents/business-analysis/agent_ba.prompt.system.md")
USER_PROMPT_TEMPLATE        = resolve_absolute_path("sources/agents/business-analysis/agent_ba.prompt.user.md")
ABS_IDEAS_STORAGE_PATH      = "sources/storage/ideas"
IDEAS_STORAGE_PATH          = resolve_absolute_path(ABS_IDEAS_STORAGE_PATH)
ABS_SRS_STORAGE_PATH        = "sources/storage/business-analysis"
SRS_STORAGE_PATH            = resolve_absolute_path(ABS_SRS_STORAGE_PATH)
BA_OUTPUT_PATH              = resolve_absolute_path("sources/output/business-analysis")
SRS_STORAGE_FILE            = "requirements.md"
SRS_INFO_FILE               = "project-info.json"
SRSS_SUMMARY_FILE           = os.path.join(SRS_STORAGE_PATH, "projects-summary.json")
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
        self.srss_summary = self.load_srss_summary()
    
    def load_srss_summary(self):
        return read_json_file(SRSS_SUMMARY_FILE)

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
        abs_idea_file = os.path.join(ABS_IDEAS_STORAGE_PATH, f"{self.idea_id}.md")
        idea_file = resolve_absolute_path(abs_idea_file)
        if not os.path.exists(idea_file):
            print(f"[ 💀 {self.agent_id} Agent | CRITICAL ERROR ] Not found IDEA file { idea_file }")
            sys.exit(1)
        
        # read idea file to build user prompt
        _, idea_content = read_file_raw(file_path=idea_file)
        
        # return merged new values
        return {
            **kwargs,
            "language": self.language,
            "idea_file": abs_idea_file,
            "raw_idea_content": idea_content
        }
    
    # @override
    def clean_response(self, raw_response, **kwargs):
        srs_info = json.loads(raw_response.strip()) if raw_response else None
        
        # check srss summary
        srss_summary = []
        if self.srss_summary and isinstance(self.srss_summary, tuple):
            srss_summary = list(self.srss_summary[1]) if len(self.srss_summary) > 1 and isinstance(self.srss_summary[1], list) else list(self.srss_summary)
            
        elif self.srss_summary:
            srss_summary = list(self.srss_summary)
        srss_summary = [ i for i in srss_summary if isinstance(i, dict) ]
        
        # parse technical project name as folder name
        datetimeStr = datetime.now().strftime("%Y%m%d%H%M%S")
        defaultPrjName = f"project-{datetimeStr}"
        project_info = srs_info.get("project_names") or {}
        project_name = project_info.get("technical_codename") or defaultPrjName
        project_storage_path = os.path.join(ABS_SRS_STORAGE_PATH, project_name)
        
        # initial project info
        abs_requirements_file = os.path.join(project_storage_path, SRS_STORAGE_FILE)
        project_info = {
            **project_info,
            "idea": self.idea_id,
            "location": project_storage_path,
            "requirements": abs_requirements_file
        }
        srss_summary.append(project_info)
        self.srss_summary = srss_summary
        
        # return cleaned/prepared data
        return {
            **srs_info,
            "requirements": resolve_absolute_path(abs_requirements_file),
            "project_info": { **project_info }
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("- Invalid AI raw response. Not a valid JSON format data.")
        
        # export requirements
        requirements_file = response_data.get("requirements")
        requirements_content = response_data.get("srs_content_markdown")
        write_file(file=requirements_file, data=requirements_content)
        
        # export project info
        project_info = response_data.get("project_info")
        project_info_file = resolve_absolute_path(os.path.join(project_info.get("location"), SRS_INFO_FILE))
        write_json_file(file=project_info_file, json_data=project_info)
        
        # export projects summary
        write_json_file(file=SRSS_SUMMARY_FILE, json_data=self.srss_summary)
        
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
