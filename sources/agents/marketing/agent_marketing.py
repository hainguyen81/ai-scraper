import sys

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    extract_data_part,
    read_file_raw,
    render_prompt
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
PLANNER_RAW_FILE                = "marketing-planner.md"
ASSETS_RAW_FILE                 = "marketing-assets.md"
CORP_COMPLIANCE_RULES_FILE      = "corporate.compliance.rules.md"

MASTER_RULE_PROMPT_TEMPLATE = "marketing.rule.enterprise.governance.guardrails.md"


class AbstractMarketingAgent(AbstractSubAgent):
    def __init__(self, agent_id, **kwargs):
        super().__init__(agent_id=agent_id, **kwargs)
    
    def __marketing_planner_file__(self) -> str:
        project_name = self.__current_project_name__()
        return self.__storage_path__(storage_name="storage_marketing", file=f"{project_name}/{PLANNER_RAW_FILE}") if project_name else None
    
    def __marketing_assets_file__(self) -> str:
        project_name = self.__current_project_name__()
        return self.__storage_path__(storage_name="storage_marketing", file=f"{project_name}/{ASSETS_RAW_FILE}") if project_name else None
    
    def __corporate_compliance_file__(self) -> str:
        project_name = self.__current_project_name__()
        return self.__agents_path__(storage_name="storage_config", file=CORP_COMPLIANCE_RULES_FILE) if project_name else None
    
    def __read_marketing_planner__(self) -> str:
        planner_file = self.__marketing_planner_file__()
        _, raw_planner_content = read_file_raw(file_path=planner_file)
        return raw_planner_content
    
    def __read_marketing_assets__(self) -> str:
        assets_file = self.__marketing_assets_file__()
        _, raw_assets_content = read_file_raw(file_path=assets_file)
        return raw_assets_content
    
    def __read_corporate_compliance__(self) -> str:
        compliance_file = self.__corporate_compliance_file__()
        _, raw_compliance_content = read_file_raw(file_path=compliance_file)
        return raw_compliance_content
    
    def master_prompt_file(self) -> str:
        return MASTER_RULE_PROMPT_TEMPLATE
    
    def build_master_prompt(self, **kwargs) -> str:
        prompt_context = self.build_master_prompt_context(**kwargs) or {}
        super_master_prompt = render_prompt(super().master_prompt_template(), prompt_context)
        master_prompt = render_prompt(self.master_prompt_template(), prompt_context)
        return f"{super_master_prompt}\n\n{master_prompt}"
    
    # @override
    def __pre_execute__(self, **kwargs):
        # read idea
        idea_same_project, raw_idea_content = self.__read_idea_or_requirements__(ignore_not_found=True)
        self.idea_is_project = idea_same_project
        
        # no idea also no requirements
        if not raw_idea_content:
            self.logger.critical(f"💀 Not found IDEA / Requirements file to process")
            sys.exit(1)
        
        # read ba/SRS
        raw_srs_content = self.__read_srs__(ignore_not_found=False)
        
        # read sa/blueprint
        raw_blueprint_content = self.__read_blueprint__(ignore_not_found=False)
        
        # return merged new values
        return {
            **kwargs,
            "raw_idea_content": raw_idea_content,
            "raw_srs_content": raw_srs_content,
            "raw_blueprint_content": raw_blueprint_content
        }
    
    def __extract_response_part__(self, response_data: str, start_delimiter: str, end_delimiter: str) -> str:
        return extract_data_part(data=response_data, start_delimiter=start_delimiter, end_delimiter=end_delimiter)  

