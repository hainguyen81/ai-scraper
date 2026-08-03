# ==========================================
# FILE: ./marketing_pipeline/reviewer.py
# DESCRIPTION: Native OpenAI Implementation of ComplianceReviewerAgent
# COMMENTS: Written in English as mandated
# ==========================================
import sys

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    write_file,
    parse_args,
)

# super agent
from sources.agents.marketing.agent_marketing import AbstractMarketingAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
SYSTEM_PROMPT_TEMPLATE          = "prompt.system.reviewer.md"
USER_PROMPT_TEMPLATE            = "prompt.user.reviewer.md"

REVIEWER_JSON_FILE              = "marketing-reviewer.json"
REVIEWER_RAW_FILE               = "marketing-reviewer.md"
REVIEWER_LOG_FILE               = "marketing-reviewer_log.md"

DELIMITER_REVIEWER_START        = "<!--START_GOVERNANCE_REPORT-->"
DELIMITER_REVIEWER_END          = "<!--END_GOVERNANCE_REPORT-->"
DELIMITER_RESPONDER_START       = "<!--START_RESPONDER_PAYLOAD-->"
DELIMITER_RESPONDER_END         = "<!--END_RESPONDER_PAYLOAD-->"

class EnterpriseComplianceReviewerAgent(AbstractMarketingAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='EnterpriseComplianceReviewerAgent',
            agent_name='💡🛡️ EnterpriseComplianceReviewerAgent',
            **kwargs
        )

    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_marketing", file=REVIEWER_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def __pre_execute__(self, **kwargs):
        # read compliance policy file
        raw_compliance_content = self.__read_corporate_compliance__()
        if not raw_compliance_content:
            self.logger.critical(f"💀 Not found CORPORATE COMPLIANCE file to process")
            sys.exit(1)
        
        # read planner file
        raw_planner_content = self.__read_marketing_planner__()
        if not raw_planner_content:
            self.logger.critical(f"💀 Not found MARKETING PLANNER file to process")
            sys.exit(1)
        
        # read assets file
        raw_assets_content = self.__read_marketing_assets__()
        if not raw_assets_content:
            self.logger.critical(f"💀 Not found MARKETING ASSETS file to process")
            sys.exit(1)
        
        # return merged new values
        return {
            **kwargs,
            "raw_compliance_content": raw_compliance_content,
            "raw_planner_content": raw_planner_content,
            "raw_assets_content": raw_assets_content
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("❌ Invalid AI raw response: No data to process")
        
        # -------------------------------------------------------------
        # ZONE 1 EXTRACTION FLOW: The C-Suite Governance Report
        # -------------------------------------------------------------
        raw_reviewer_report = self.__extract_response_part__(
            response_data, DELIMITER_REVIEWER_START, DELIMITER_REVIEWER_END
        ) or response_data
        
        # write storage reviewer report
        write_file(
            file=self.__storage_path__(storage_name="storage_marketing", file=f"{self.project_name}/{REVIEWER_RAW_FILE}"),
            data=raw_reviewer_report
        )
        
        # -------------------------------------------------------------
        # ZONE 2 EXTRACTION FLOW: The Downstream Bot Knowledge Base
        # -------------------------------------------------------------
        raw_responder_payload = self.__extract_response_part__(
            response_data, DELIMITER_RESPONDER_START, DELIMITER_RESPONDER_END
        )

        # write storage responder payload for downstream bot knowledge base
        if not raw_responder_payload:
            self.logger.warning("⚠️ No valid responder payload found in the AI response")
        else:
            write_file(
                file=self.__storage_path__(storage_name="storage_marketing", file=f"{self.project_name}/{REVIEWER_JSON_FILE}"),
                data=raw_responder_payload
            )
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.__output_storage_path__(storage_name="output_marketing", file=REVIEWER_RAW_FILE),
                data=raw_response
            )


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    
    args, unknown_args = parse_args(
        description="🛡️ EnterpriseComplianceReviewerAgent",
        parser_callback=add_known_arguments
    )
    EnterpriseComplianceReviewerAgent(
        idea=args.idea,
        project=args.idea,
        **unknown_args
    ).execute()
