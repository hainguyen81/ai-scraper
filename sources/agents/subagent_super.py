import os
import sys
import re
import json
import urllib.parse
import requests
import argparse
from datetime import datetime
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    read_json_file,
    read_file_raw,
    kwargs_by_key
)

# super agent
from sources.agents.agent_super import AbstractAgent


class AbstractSubAgent(AbstractAgent):
    def __init__(self, agent_id, **kwargs):
        super().__init__(agent_id=agent_id, **kwargs)
    
    # @override
    def initialize(self):
        # request parameters
        self.idea_id = self.get_kwargs("idea") or self.get_kwargs("idea") or None
        self.project_name = self.get_kwargs("project") or self.get_kwargs("project_name") or None
        
        # initialize projects information
        self.initialize_projects()
        
        # start initialization
        super().initialize()
    
    def initialize_projects(self):
        self.projects_summary = self.__read_projects_info__(ignore_not_found=True) or []
        self.project_info = self.__project_info__()
    
    def __storage_path__(self, storage_name, file) -> str:
        return os.path.join(self.storage.get(storage_name), file))
    
    def __output_storage_path__(self, storage_name, file) -> str:
        return os.path.join(self.storage_output.get(storage_name), file))
    
    def __agents_path__(self, storage_name, file) -> str:
        return os.path.join(self.storage_agents.get(storage_name), file))
    
    def __read_storage_file__(self, storage_name, file, ignore_not_found=False):
        storage_file = self.__storage_path__(storage_name=storage_name, file=file)
        if not ignore_not_found and not os.path.exists(storage_file):
            self.logger.critical(f"[ 💀 ERROR ] Not found storage '{storage_name}' file { file }")
            sys.exit(1)
        
        elif not os.path.exists(storage_file):
            self.logger.critical(f"[ 💀 WARN ] Not found storage '{storage_name}' file { file }")
            return None
        
        # read idea file to build user prompt
        _, storage_file_content = read_file_raw(file_path=storage_file)
        return storage_file_content
    
    def __read_storage_json__(self, storage_name, file, ignore_not_found=False):
        storage_file = self.__storage_path__(storage_name=storage_name, file=file)
        if not ignore_not_found and not os.path.exists(storage_file):
            self.logger.critical(f"[ 💀 ERROR ] Not found storage '{storage_name}' file { file }")
            sys.exit(1)
        
        elif not os.path.exists(storage_file):
            self.logger.critical(f"[ 💀 WARN ] Not found storage '{storage_name}' file { file }")
            return None
        
        # read idea file to build user prompt
        _, storage_json = read_json_file(file_path=storage_file)
        return storage_json
    
    def __project_info__(self):
        return next(
            (
                pi for pi in self.projects_summary
                if isinstance(pi, dict) and (
                    self.idea_id in [pi.get("technical_codename"), pi.get("idea"), pi.get("brand_name")]
                    or self.project_name in [pi.get("technical_codename"), pi.get("idea"), pi.get("brand_name")]
                )
            ),
            None
        )
    
    def __current_project_name__(self):
        return self.project_info.get("technical_codename", None)
    
    def __current_project_description__(self):
        return self.project_info.get("descriptive_name", None)
    
    def __idea_files__(self):
        absolute_file = self.__storage_path__(storage_name="absolute_ideas", file=f"{self.idea_id}.md")
        physical_file = self.__storage_path__(storage_name="storage_ideas", file=f"{self.idea_id}.md")
        if not os.path.exists(physical_file):
            absolute_file = self.__storage_path__(storage_name="absolute_requirements", file=f"{self.idea_id}/requirements.md")
            physical_file = self.__storage_path__(storage_name="storage_requirements", file=f"{self.idea_id}/requirements.md")
        if not os.path.exists(physical_file):
            absolute_file = self.__storage_path__(storage_name="absolute_requirements", file=f"{self.project_name}/requirements.md")
            physical_file = self.__storage_path__(storage_name="storage_requirements", file=f"{self.project_name}/requirements.md")
        return (None, None) if not os.path.exists(physical_file) else (absolute_file, physical_file)
    
    def __ba_file__(self):
        return self.project_info.get("requirements", None) if self.project_info else None
    
    def __sa_file__(self):
        project_name = self.__current_project_name__()
        return self.__storage_path__(storage_name="storage_sa", file=f"{project_name}/context/{project_name}.global.blueprint.md") if project_name else None
    
    def __projects_summary_path__(self):
        return self.__storage_path__(storage_name="storage_ba", file="projects-summary.json")
    
    def __ideas_history_path__(self):
        return self.__storage_path__(storage_name="storage_ideas", file="history_ideas.json")

    def __read_idea__(self, ignore_not_found=False): -> str:
        return self.__read_storage_file__(storage_name="storage_ideas", file=f"{self.idea_id}.md", ignore_not_found=ignore_not_found)

    def __read_requirements__(self, ignore_not_found=False): -> str:
        return self.__read_storage_file__(storage_name="storage_requirements", file=f"{self.project_name}/requirements.md", ignore_not_found=ignore_not_found)
    
    def __read_idea_or_requirements__(self, ignore_not_found=False):
        requirements = self.__read_idea__(ignore_not_found=ignore_not_found)
        idea_is_project = not requirements
        if not requirements:
            requirements = self.__read_requirements__(ignore_not_found=ignore_not_found)
        return (idea_is_project, requirements)

    def __read_srs__(self, ignore_not_found=False): -> str:
        project_name = self.__current_project_name__()
        project_name = project_name if project_name else self.project_name
        return self.__read_storage_file__(storage_name="storage_ba", file=f"{project_name}/requirements.md", ignore_not_found=ignore_not_found)

    def __read_blueprint__(self, ignore_not_found=False): -> str:
        project_name = self.__current_project_name__()
        project_name = project_name if project_name else self.project_name
        return self.__read_storage_file__(storage_name="storage_blueprint", file=f"{project_name}/context/{project_name}.global.blueprint.md", ignore_not_found=ignore_not_found)

    def __read_projects_info__(self, ignore_not_found=False): -> str:
        return self.__read_storage_json__(storage_name="storage_ba", file="projects-summary.json", ignore_not_found=ignore_not_found)

    def __read_ideas_history__(self, ignore_not_found=False): -> str:
        return self.__read_storage_json__(storage_name="storage_ideas", file="history_ideas.json", ignore_not_found=ignore_not_found)


