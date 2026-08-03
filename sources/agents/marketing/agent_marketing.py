import os
import sys

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    datetime_for_agent
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

MASTER_RULE_PROMPT_TEMPLATE = "marketing.rule.enterprise.governance.guardrails.md"


class AbstractMarketingAgent(AbstractSubAgent):
    def __init__(self, agent_id, **kwargs):
        super().__init__(agent_id=agent_id, **kwargs)
    
    def __common_prompt_context__(self):
        datetime_prompt, datetime_docid = datetime_for_agent()
        return {
            "idea_id": self.idea_id,
            "language": self.language,
            "project_name": self.__current_project_name__() or "-",
            "project_description": self.__current_project_description__() or "-",
            "current_timestamp": datetime_prompt,
            "doc_id": datetime_docid
        }
    
    def __pre_initialize__(self):
        # require idea identity to analyze
        if not self.project_info:
            self.logger.critical(f"💀 (1) Invalid idea identity / project name to analyze!")
            sys.exit(1)
        
        # check idea file
        abs_idea_file, phys_idea_file = self.__idea_files__()
        if not os.path.exists(phys_idea_file):
            self.logger.critical(f"💀 (4) Not found IDEA file {abs_idea_file}")
            sys.exit(1)
        else:
            self.idea_file = abs_idea_file
        
        # check requirments file
        self.ba_file = self.__ba_file__()
        if not os.path.exists(self.ba_file):
            self.logger.critical(f"💀 (5) Not found BA file by idea identity / project name '{self.idea_id}'")
            sys.exit(1)
        
        # check blueprint file
        self.blueprint_file = self.__sa_file__()
        if not os.path.exists(self.blueprint_file):
            self.logger.critical(f"💀 (6) Not found BLUEPRINT file by idea identity / project name '{self.idea_id}")
            sys.exit(1)
    
    # @override
    def initialize(self):
        # pre-initialize
        self.__pre_initialize__()
        
        # initialize super
        super().initialize()
    
    def master_prompt_file(self) -> str:
        return MASTER_RULE_PROMPT_TEMPLATE
    
    # @override
    def pre_execute(self, **kwargs):
        # read idea file
        _, raw_idea_content = self.__read_idea_or_requirements__(ignore_not_found=True)
        
        # no idea also no requirements
        if not raw_idea_content:
            self.logger.critical(f"💀 Not found IDEA / Requirements file to process")
            sys.exit(1)
        
        # read BA file
        raw_ba_content = self.__read_srs__(ignore_not_found=False)
        
        # read BluePrint file
        raw_blueprint_content = self.__read_blueprint__(ignore_not_found=False)
        
        # return merged new values
        return {
            **kwargs,
            **self.__common_prompt_context__(),
            "raw_idea_content": raw_idea_content,
            "raw_srs_content": raw_ba_content,
            "raw_blueprint_content": raw_blueprint_content
        }
