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
    write_json_file,
    write_file
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
# models list
SYSTEM_PROMPT_TEMPLATE      = "agent_ba.prompt.system.md"
USER_PROMPT_TEMPLATE        = "agent_ba.prompt.user.md"

SRS_FILE                    = "requirements.md"
PROJECT_INFO_FILE           = "project-info.json"
BA_RAW_FILE                 = "ba.md"
BA_LOG_FILE                 = "ba_log.md"

DEFAULT_SRS_LANGUAGE        = "English"


class PrincipalBusinessAnalysisAgent(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(agent_id='BusinessAnalysis', **kwargs)
    
    # @override
    def initialize(self):
        # start initialization
        super().initialize()
        self.language = self.get_kwargs("language") or DEFAULT_IDEAS_LANGUAGE
    
    def ba_output_raw_file(self):
        return self.__output_storage_path__(storage_name="storage_ba", file=BA_RAW_FILE)
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="storage_ba", file=BA_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__storage_path__(storage_name="storage_ba", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__storage_path__(storage_name="storage_ba", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def agent_temperature(self):
        return 0.8 # high ideas
    
    # @override
    def pre_execute(self, **kwargs):
        # read idea
        idea_same_project, file_content = self.__read_idea_or_requirements__(ignore_not_found=True)
        self.idea_is_project = idea_same_project
        
        # no idea also no requirements
        if not file_content:
            self.logger.critical(f"[ 💀 CRITICAL ] Not found IDEA / Requirements file to process")
            sys.exit(1)
        
        # return merged new values
        _, idea_file = self.__idea_files__()
        return {
            **kwargs,
            "language": self.language,
            "idea_file": idea_file,
            "raw_idea_content": file_content
        }
    
    # @override
    def clean_response(self, raw_response, **kwargs):
        srs_info = json.loads(raw_response.strip()) if raw_response else None
        
        # check srss summary
        projects = []
        if self.projects_summary and isinstance(self.projects_summary, tuple):
            projects = list(self.projects_summary[1]) if len(self.projects_summary) > 1 and isinstance(self.projects_summary[1], list) else list(self.projects_summary)
            
        elif self.projects_summary:
            projects = list(self.projects_summary)
        projects = [ i for i in projects if isinstance(i, dict) ]
        
        # parse technical project name as folder name
        datetimeStr = datetime.now().strftime("%Y%m%d%H%M%S")
        defaultPrjName = f"project-{datetimeStr}"
        project_info = srs_info.get("project_names") or {}
        project_name = project_info.get("technical_codename") or defaultPrjName
        
        # initial project info
        idea_id = self.idea_id
        if self.idea_is_project:
            unique_id = hashlib.md5(idea_id.encode("utf-8")).hexdigest()[:12]
            idea_id = f"idea_{unique_id}"
        project_info = {
            **project_info,
            "idea": idea_id,
            "location": self.__storage_path__(storage_name="relative_ba", file=project_name),
            "requirements": self.__storage_path__(storage_name="relative_ba", file=f"{project_name}/{SRS_FILE}")
        }
        projects.append(project_info)
        self.projects_summary = projects
        
        # return cleaned/prepared data
        return {
            **srs_info,
            "requirements_file": self.__storage_path__(storage_name="storage_ba", file=f"{project_name}/{SRS_FILE}"),
            "project_info_file": self.__storage_path__(storage_name="storage_ba", file=f"{project_name}/{PROJECT_INFO_FILE}"),
            "project_info": { **project_info }
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("- Invalid AI raw response. Not a valid JSON format data.")
        
        # export requirements
        requirements_file = response_data.get("requirements_file")
        requirements_content = response_data.get("srs_content_markdown")
        write_file(file=requirements_file, data=requirements_content)
        
        # export project info
        project_info = response_data.get("project_info")
        write_json_file(file=response_data.get("project_info_file"), json_data=project_info)
        
        # export projects summary
        write_json_file(file=self.__projects_summary_path__(), json_data=self.projects_summary)
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.ba_output_raw_file(),
                data=raw_response
            )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    parser.add_argument("--language", type=str, help="Translate SRS to language. Ex: Vietnamese, English, etc.")
    args = parser.parse_args()
    PrincipalBusinessAnalysisAgent(
        idea=args.idea,
        project=args.idea,
        language=args.language
    ).execute()
