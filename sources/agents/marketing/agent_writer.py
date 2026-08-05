# ==========================================
# FILE: ./marketing_pipeline/writer.py
# DESCRIPTION: Native OpenAI Implementation of ContentWriterAgent
# COMMENTS: Written in English as mandated
# ==========================================
import sys

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    read_file_raw,
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
SYSTEM_PROMPT_TEMPLATE          = "prompt.system.writer.md"
USER_PROMPT_TEMPLATE            = "prompt.user.writer.md"

CONTENT_WRITER_JSON_FILE        = "marketing-content-writer.json"
CONTENT_WRITER_RAW_FILE         = "marketing-content-writer.md"
CONTENT_WRITER_LOG_FILE         = "marketing-content-writer_log.md"

DELIMITER_CONTENT_WRITER_START  = "<!--START_GOVERNANCE_REPORT-->"
DELIMITER_CONTENT_WRITER_END    = "<!--END_GOVERNANCE_REPORT-->"
DELIMITER_RESPONDER_START       = "<!--START_RESPONDER_PAYLOAD-->"
DELIMITER_RESPONDER_END         = "<!--END_RESPONDER_PAYLOAD-->"

class EnterpriseContentWriterAgent(AbstractMarketingAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='EnterpriseContentWriterAgent',
            agent_name='💡✍️ EnterpriseContentWriterAgent',
            **kwargs
        )
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_marketing", file=CONTENT_WRITER_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def __pre_execute__(self, **kwargs):
        # read planner file
        planner_file = self.__marketing_planner_file__()
        _, raw_planner_content = read_file_raw(file_path=planner_file)
        
        # not anything to publish, exit
        if not raw_planner_content:
            self.logger.critical(f"💀 Not found MARKETING PLANNER file to process")
            sys.exit(1)
        
        # return merged new values
        return {
            **kwargs,
            "platform_target": self.get_kwargs_by_key(key="platform_target", **kwargs)
                or self.get_kwargs_by_key(key="platform", **kwargs) or "generic",
            "target_interval": self.get_kwargs_by_key(key="target_interval", **kwargs)
                or self.get_kwargs_by_key(key="interval", **kwargs) or "Week 1",
            "raw_planner_content": raw_planner_content
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("❌ Invalid AI raw response: No data to process")
        
        # -------------------------------------------------------------
        # ZONE 1 EXTRACTION FLOW: The C-Suite Governance Report
        # -------------------------------------------------------------
        raw_content_writer_report = self.__extract_response_part__(
            response_data, DELIMITER_CONTENT_WRITER_START, DELIMITER_CONTENT_WRITER_END
        ) or response_data
        
        # write storage content writer report
        write_file(
            file=self.__storage_path__(storage_name="storage_marketing", file=f"{self.project_name}/{CONTENT_WRITER_RAW_FILE}"),
            data=raw_content_writer_report
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
                    file=self.__storage_path__(storage_name="storage_marketing", file=f"{self.project_name}/{CONTENT_WRITER_JSON_FILE}"),
                    json_data=json_responder_payload
                )
            
            # write as raw file
            else:
                write_file(
                    file=self.__storage_path__(storage_name="storage_marketing", file=f"{self.project_name}/{CONTENT_WRITER_JSON_FILE}"),
                    data=raw_responder_payload
                )
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.__output_storage_path__(storage_name="output_marketing", file=CONTENT_WRITER_RAW_FILE),
                data=raw_response
            )


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    
    args, unknown_args = parse_args(
        description="✍️ EnterpriseContentWriterAgent",
        parser_callback=add_known_arguments
    )
    EnterpriseContentWriterAgent(
        idea=args.idea,
        project=args.idea,
        **unknown_args
    ).execute()
