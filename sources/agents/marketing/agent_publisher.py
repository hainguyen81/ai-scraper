# ==========================================
# FILE: ./marketing_pipeline/planner.py
# DESCRIPTION: Native OpenAI Implementation of MarketingPlannerAgent
# COMMENTS: Written in English as mandated
# ==========================================
import sys

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    write_file,
    parse_args,
    read_json_file,
)

# super agent
from sources.agents.marketing.agent_marketing import AbstractMarketingAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
# models list
SYSTEM_PROMPT_TEMPLATE          = "prompt.system.publisher.md"
USER_PROMPT_TEMPLATE            = "prompt.user.publisher.md"

PUBLISHER_SOCIAL_SECRETS_KEY    = "SOCIAL_SECRETS_KEY"

PUBLISHER_APPROVAL_JSON_FILE    = "marketing-publisher-approval.json"
PUBLISHER_JSON_FILE             = "marketing-publisher.json"
PUBLISHER_RAW_FILE              = "marketing-publisher.md"
PUBLISHER_LOG_FILE              = "marketing-publisher_log.md"

class EnterpriseSocialPublisherAgent(AbstractMarketingAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='EnterpriseSocialPublisherAgent',
            agent_name='💡🎨 EnterpriseSocialPublisherAgent',
            **kwargs
        )
    
    def __social_approval_file__(self) -> str:
        project_name = self.__current_project_name__()
        return self.__storage_path__(storage_name="storage_marketing", file=f"{project_name}/{PUBLISHER_APPROVAL_JSON_FILE}") if project_name else None
    
    # @override
    def agent_secrets_key(self) -> str:
        return PUBLISHER_SOCIAL_SECRETS_KEY
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_marketing", file=PUBLISHER_LOG_FILE)
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_marketing_prompts", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def pre_execute(self, **kwargs):
        # read social approval file
        social_approval_file = self.__social_approval_file__()
        _, social_approval_json_vault = read_json_file(file_path=social_approval_file)
        
        # not anything to publish, exit
        if not social_approval_json_vault:
            self.logger.critical(f"💀 Not found SOCIAL APPROVAL file to process")
            sys.exit(1)
        
        # return merged new values
        return {
            **kwargs,
            "approved_content_vault_json": social_approval_json_vault,
            "social_credentials_meta": self.secrets
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("❌ Invalid AI raw response: No data to process")
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.__output_storage_path__(storage_name="output_marketing", file=PUBLISHER_RAW_FILE),
                data=raw_response
            )


if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--idea", type=str, help="Idea Identity / Project Name for searching")
    
    args, unknown_args = parse_args(
        description="🎨 EnterpriseSocialPublisherAgent",
        parser_callback=add_known_arguments
    )
    EnterpriseSocialPublisherAgent(
        idea=args.idea,
        project=args.idea,
        **unknown_args
    ).execute()
