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
)

# super agent
from sources.agents.marketing.agent_marketing import AbstractMarketingAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
# models list
SYSTEM_PROMPT_TEMPLATE          = "prompt.system.reviewer.md"
USER_PROMPT_TEMPLATE            = "prompt.user.reviewer.md"

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
            "platform_target": self.get_kwargs_by_key(key="platform_target", **kwargs) or "generic",
            "target_interval": self.get_kwargs_by_key(key="target_interval", **kwargs) or "Week 1",
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
        content_writer_start_idx = str(response_data).find(DELIMITER_CONTENT_WRITER_START)
        content_writer_end_idx = str(response_data).find(DELIMITER_CONTENT_WRITER_END)
        raw_content_writer_report = None

        if content_writer_start_idx != -1 and content_writer_end_idx != -1 and content_writer_start_idx < content_writer_end_idx:
            # Shift index forward to exclude the raw opening comment token itself
            actual_start = content_writer_start_idx + len(DELIMITER_CONTENT_WRITER_START)
            raw_content_writer_report = response_data[actual_start:content_writer_end_idx].strip()
        else:
            raw_content_writer_report = response_data  # Fallback to the entire response if delimiters are not found
        
        # write storage content writer report
        write_file(
            file=self.__storage_path__(storage_name="storage_marketing", file=f"{self.project_name}/{CONTENT_WRITER_RAW_FILE}"),
            data=raw_content_writer_report
        )
        
        # -------------------------------------------------------------
        # ZONE 2 EXTRACTION FLOW: The Downstream Bot Knowledge Base
        # -------------------------------------------------------------
        responder_start_idx = str(response_data).find(DELIMITER_RESPONDER_START)
        responder_end_idx = str(response_data).find(DELIMITER_RESPONDER_END)
        raw_responder_payload = None

        if responder_start_idx != -1 and responder_end_idx != -1 and responder_start_idx < responder_end_idx:
            # Shift index forward to exclude the raw opening comment token itself
            actual_start = responder_start_idx + len(DELIMITER_RESPONDER_START)
            raw_responder_payload = response_data[actual_start:responder_end_idx].strip()

            # write storage responder payload for downstream bot knowledge base
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
