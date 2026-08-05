# ==========================================
# FILE: ./marketing_pipeline/planner.py
# DESCRIPTION: Native OpenAI Implementation of MarketingPlannerAgent
# COMMENTS: Written in English as mandated
# ==========================================
# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    write_file,
    parse_args,
    json_loads,
    write_json_file
)

# super agent
from sources.agents.marketing.agent_marketing import AbstractMarketingAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
# models list
SYSTEM_PROMPT_TEMPLATE      = "prompt.system.planner.md"
USER_PROMPT_TEMPLATE        = "prompt.user.planner.md"

PLANNER_RAW_FILE            = "marketing-planner.md"
RESPONDER_REF_JSON_FILE     = "marketing-planner-for-responder.json"
PLANNER_LOG_FILE            = "marketing-planner_log.md"

DELIMITER_PLANNER_START     = "<!--START_GOVERNANCE_REPORT-->"
DELIMITER_PLANNER_END       = "<!--END_GOVERNANCE_REPORT-->"
DELIMITER_RESPONDER_START   = "<!--START_RESPONDER_PAYLOAD-->"
DELIMITER_RESPONDER_END     = "<!--END_RESPONDER_PAYLOAD-->"

class EnterpriseMarketingPlannerAgent(AbstractMarketingAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='EnterpriseMarketingPlannerAgent',
            agent_name='💡🎯 EnterpriseMarketingPlannerAgent',
            **kwargs
        )
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_marketing", file=PLANNER_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("❌ Invalid AI raw response: No data to process")
        
        # -------------------------------------------------------------
        # ZONE 1 EXTRACTION FLOW: The C-Suite Governance Report
        # -------------------------------------------------------------
        raw_planner_report = self.__extract_response_part__(
            response_data, DELIMITER_PLANNER_START, DELIMITER_PLANNER_END
        ) or response_data

        # write storage planner report
        write_file(
            file=self.__storage_path__(storage_name="storage_marketing", file=f"{self.project_name}/{PLANNER_RAW_FILE}"),
            data=raw_planner_report
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
            json_responder_payload = json_loads(data=raw_responder_payload, silent=True)
            # write as JSON file
            if json_responder_payload:
                write_json_file(
                    file=self.__storage_path__(storage_name="storage_marketing", file=f"{self.project_name}/{RESPONDER_REF_JSON_FILE}"),
                    json_data=json_responder_payload
                )
            
            # write as raw file
            else:
                write_file(
                    file=self.__storage_path__(storage_name="storage_marketing", file=f"{self.project_name}/{RESPONDER_REF_JSON_FILE}"),
                    data=raw_responder_payload
                )
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.__output_storage_path__(storage_name="output_marketing", file=PLANNER_RAW_FILE),
                data=raw_response
            )


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    
    args, unknown_args = parse_args(
        description="🎯 EnterpriseMarketingPlannerAgent",
        parser_callback=add_known_arguments
    )
    EnterpriseMarketingPlannerAgent(
        idea=args.idea,
        project=args.idea,
        **unknown_args
    ).execute()
