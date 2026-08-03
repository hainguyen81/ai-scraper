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
    def __pre_execute__(self, **kwargs):
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
            # Example (approved_content_vault_json):
            # {
            #     "audit_metadata": {
            #         "reviewer_agent": "ComplianceReviewer",
            #         "audit_status": "APPROVED_VAULT",
            #         "approval_timestamp": "2026-08-03 15:25:00",
            #         "compliance_rule_version": "v2.1-corporate"
            #     },
            #     "project_identity": {
            #         "project_name": "Membership-Hub",
            #         "campaign_interval": "Week 1"
            #     },
            #     "approved_distribution_assets": [
            #         {
            #         "platform": "LinkedIn",
            #         "content_body": "Cắt giảm 40% chi phí in ấn thẻ nhựa vật lý và tối ưu hóa 35% tốc độ phục vụ tại quầy cho chuỗi bán lẻ bằng giải pháp số hóa hội viên trên nền tảng Cloud-Native EDA vững chắc. Tìm hiểu thêm tại chiến dịch của chúng tôi: __HTTPS__://membership-hub__DOT__com__SLASH__roi-calculator",
            #         "tags": ["#EnterpriseTech", "#RetailAutomation", "#CloudNative"]
            #         },
            #         {
            #         "platform": "X",
            #         "content_body": "Giải mã cấu trúc hạ tầng Redis Cluster giúp hệ thống Membership-Hub xử lý mượt mà 10,000 lượt quét mã QR bảo mật mỗi giây mà không nghẽn hạ tầng. Toàn văn báo cáo SA: __HTTPS__://membership-hub__DOT__com__SLASH__architecture-deepdive",
            #         "tags": ["#EDA", "#GKE", "#RedisCluster"]
            #         }
            #     ]
            # }
            "approved_content_vault_json": social_approval_json_vault,
            # Example (social_credentials_json):
            # {
            #     "target_routing_environment": "PRODUCTION",
            #     "platforms_auth_matrix": {
            #         "X": {
            #         "api_endpoint": "__HTTPS__://api__DOT__x__SLASH__2__SLASH__tweets",
            #         "oauth_client_id": "X_CLIENT_ENT_90128",
            #         "bearer_token_vault_reference": "ENV_VAULT_X_AUTH_BEARER",
            #         "target_account_handle": "@MembershipHubEnt"
            #         },
            #         "LinkedIn": {
            #         "api_endpoint": "__HTTPS__://api__DOT__linkedin__DOT__com__SLASH__v2__SLASH__ugcPosts",
            #         "author_organization_urn": "urn:li:organization:8912743",
            #         "access_token_vault_reference": "ENV_VAULT_LINKEDIN_ACCESS_TOKEN",
            #         "target_page_name": "Membership-Hub Enterprise Solutions"
            #         }
            #     }
            # }
            "social_credentials_meta": self.secrets
        }
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("❌ Invalid AI raw response: No data to process")
        
        # Example (response_data):
        # {
        #     "status": "SUCCESS",
        #     "project_name": "Membership-Hub",
        #     "execution_timestamp": "2026-08-03 15:30:00",
        #     "dispatched_accounts": {
        #         "linkedin_enterprise_id": "urn:li:organization:8912743",
        #         "x_corporate_handle": "@MembershipHubEnt"
        #     },
        #     "platform_post_ids": {
        #         "LinkedIn": "activity:7129847192847192384",
        #         "X": "tweet_1819283719238127361"
        #     },
        #     "diagnostic_meta": {
        #         "http_status_code": 201,
        #         "api_response_message": "All payloads successfully committed to external webhooks.",
        #         "rate_limit_remaining": 498
        #     }
        # }
        
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
