import re
import hashlib

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    write_json_file,
    write_file,
    parse_args
)

# super agent
from sources.agents.subagent_super import AbstractSubAgent

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
SYSTEM_PROMPT_TEMPLATE      = "agent_idea_generator.prompt.system.md"
USER_PROMPT_TEMPLATE        = "agent_idea_generator.prompt.user.md"

IDEAS_OUTPUT_FILE           = "ideas.md"
IDEAS_LOG_FILE              = "ideas_log.md"

DEFAULT_IDEAS_DOMAIN        = "Any high-momentum, trending industry in 2026 (such as AI Agents, Automation Web-apps, Renewable Energy tech, Spatial Computing, Web3/Fintech, etc.) where a lightweight software solution or Micro-SaaS can be rapidly deployed to capture immediate market demand with an MVP built within 2-4 weeks"
DEFAULT_IDEAS_QUNATITY      = 3
DEFAULT_IDEAS_LANGUAGE      = "English"


class EnterpriseIdeaGeneratorAgent(AbstractSubAgent):
    def __init__(self, **kwargs):
        super().__init__(
            agent_id='EnterpriseIdeaGeneratorAgent',
            agent_name='💡 EnterpriseIdeaGeneratorAgent',
            **kwargs
        )
    
    # @override
    def initialize(self):
        super().initialize()
        
        # load generated ideas to avoid conflicts
        self.domain = self.get_kwargs("domain") or DEFAULT_IDEAS_DOMAIN
        self.quantity = self.get_kwargs("quantity") or DEFAULT_IDEAS_QUNATITY
        self.language = self.get_kwargs("language") or DEFAULT_IDEAS_LANGUAGE
        self.initialize_ideas()
    
    def initialize_ideas(self):
        self.history_ideas = self.__read_ideas_history__(ignore_not_found=True) or []
    
    # @override
    def initialize_projects(self):
        pass
    
    # @override
    def agent_log_file(self) -> str:
        return self.__output_storage_path__(storage_name="output_ideas", file=IDEAS_LOG_FILE)
    
    # @override
    def build_system_prompt_context(self, **kwargs):
        ideas_history = self.history_ideas if self.history_ideas else []
        ideas = [ idea["idea"] for idea in ideas_history if idea and isinstance(idea, dict) and "idea" in idea ]
        return {
            "ideas_history": ideas if ideas else None,
            "language": self.language
        }
    
    # @override
    def system_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_ideas_prompts", file=SYSTEM_PROMPT_TEMPLATE)
    
    # @override
    def build_user_prompt_context(self, **kwargs):
        ideas_history = self.history_ideas if self.history_ideas else []
        ideas = [ idea["idea"] for idea in ideas_history if idea and isinstance(idea, dict) and "idea" in idea ]
        return {
            "domain": self.domain,
            "quantity": self.quantity,
            "ideas_history": ideas if ideas else None,
            "language": self.language
        }
    
    # @override
    def user_prompt_template(self) -> str:
        return self.__agents_path__(storage_name="storage_ideas_prompts", file=USER_PROMPT_TEMPLATE)
    
    # @override
    def agent_temperature(self):
        return 0.8 # high ideas
    
    # @override
    def pre_execute(self, **kwargs):
        pass
    
    # @override
    def clean_response(self, raw_response, **kwargs):
        # extract idea blocks
        pattern_block = (
            r"####\s*\[IDEA_\d+\]\s*(.*?)\n(.*?)(?=####\s*\[IDEA_\d+\]|$)"
        )
        ideas_blocks = re.findall(pattern_block, raw_response, re.DOTALL)
        
        # check history ideas
        history_ideas = []
        if self.history_ideas and isinstance(self.history_ideas, tuple):
            history_ideas = list(self.history_ideas[1]) if len(self.history_ideas) > 1 and isinstance(self.history_ideas[1], list) else list(self.history_ideas)
            
        elif self.history_ideas:
            history_ideas = list(self.history_ideas)
        history_ideas = [ i for i in history_ideas if isinstance(i, dict) ]
        
        # find all idea names match prefix from AI response
        ideas = []
        for raw_name, raw_desc in ideas_blocks:
            clean_idea_name = raw_name.replace("**", "").strip()
            clean_idea_desc = raw_desc.strip()
            if not clean_idea_name:
                continue
            
            # idea unique identity
            unique_id = hashlib.md5(clean_idea_name.encode("utf-8")).hexdigest()[:12]
            idea_id = f"idea_{unique_id}"
            abs_idea_file = self.__storage_path__(storage_name="relative_ideas", file=f"{self.idea_id}.md")
            idea_file = self.__storage_path__(storage_name="storage_ideas", file=f"{self.idea_id}.md")
            idea_content = f"# {clean_idea_name}\n\n{clean_idea_desc}"
            idea_item = {
                "id": idea_id,
                "idea": clean_idea_name,
                "file": abs_idea_file
            }
            ideas.append({
                **idea_item,
                "physical_file": idea_file,
                "content": idea_content
            })
            history_ideas.append({ **idea_item })
        self.history_ideas = history_ideas
                
        self.logger.info(f"[ 🎯 INFO ] Found / Extracted: {len(ideas)} new ideas.")
        return ideas
    
    # @override
    def process_communication(self, **kwargs):
        response_data = self.get_kwargs_by_key(key="clean_response", **kwargs)
        if not response_data:
            raise RuntimeError("❌ Invalid AI raw response. Not a valid JSON format data.")
        
        # export new ideas as md files
        for idea in response_data:
            write_file(
                file=idea.get("physical_file"),
                data=idea.get("content")
            )
        
        # update ideas history
        write_json_file(
            file=self.__ideas_history_path__(),
            json_data=self.history_ideas
        )
        
        # export raw response if necessary as log tracing
        raw_response = self.get_kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=self.__output_storage_path__(storage_name="output_ideas", file=IDEAS_OUTPUT_FILE),
                data=raw_response
            )

if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--domain", type=str, help="Domain to find ideas")
        parser.add_argument("--quantity", type=int, help="The number of ideas")
        parser.add_argument("--language", type=str, help="Translate found ideas to language. Ex: Vietnamese, English, etc.")
    
    args, unknown_args = parse_args(
        description="💡 EnterpriseIdeaGeneratorAgent",
        parser_callback=add_known_arguments
    )
    EnterpriseIdeaGeneratorAgent(
        domain=args.domain,
        quantity=args.quantity,
        language=args.language,
        **unknown_args
    ).execute()
