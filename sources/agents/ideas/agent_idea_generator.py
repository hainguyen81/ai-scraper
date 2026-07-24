import os
import sys
import json
import re
import argparse
from datetime import datetime
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import resolve_absolute_path, read_json_file

# super agent
from sources.agents.agent_super import AbstractAgent

# models list
IDEAS_USER_PROMPT_TEMPLATE  = resolve_absolute_path("sources/agents/ideas/agent_idea_generator.prompt.md")
IDEAS_HISTORY_FILE          = resolve_absolute_path("sources/storage/ideas/history_ideas.json")
IDEAS_FILE                  = "sources/output/ideas/ideas.md"
IDEAS_LOG_FILE              = resolve_absolute_path("sources/output/ideas/ideas_log.md")
DEFAULT_IDEAS_DOMAIN        = "Any high-value industry or sector (e.g., Logistics, Real Estate, Healthcare, Finance, etc.) where a lightweight software solution, Micro-SaaS, or AI tool can be rapidly deployed to solve a major pain point with high immediate ROI (MVP built within 2-4 weeks)"
DEFAULT_IDEAS_QUNATITY      = 3
DEFAULT_IDEAS_LANGUAGE      = "English"

class IdeaGeneratorAgent(AbstractAgent):
    def __init__(self, **kwargs):
        super().__init__(agent_id='Idea', **kwargs)
    
    def initialize(self):
        super().initialize()
        # load generated ideas to avoid conflicts
        self.history_ideas = self.load_history_ideas()
        self.domain = self.get_kwargs("domain") or DEFAULT_IDEAS_DOMAIN
        self.quantity = self.get_kwargs("quantity") or DEFAULT_IDEAS_QUNATITY
        self.language = self.get_kwargs("language") or DEFAULT_IDEAS_LANGUAGE
    
    def load_history_ideas(self):
        return read_json_file(IDEAS_HISTORY_FILE)
    
    # @override
    def agent_secrets_key(self) -> str:
        pass
    
    # @override
    def agent_log_file(self) -> str:
        return IDEAS_LOG_FILE
    
    # @override
    def system_prompt_template(self) -> str:
        pass
    
    # @override
    def build_system_prompt(self, **kwargs) -> str:
        return "You are a creative and strict Idea Generation Agent. Never replicate past ideas."
    
    # @override
    def build_user_prompt_context(self, **kwargs):
        return {
            "domain": self.domain,
            "quantity": self.quantity,
            "ideas_history": self.history_ideas,
            "language": self.language
        }
    
    # @override
    def user_prompt_template(self) -> str:
        return IDEAS_USER_PROMPT_TEMPLATE
    
    # @override
    def agent_temperature(self):
        return 0.8 # high ides
    
    # @override
    def pre_execute(self):
        pass
    
    # @override
    def clean_response(self, raw_response, **kwargs):
        # extract idea names
        pattern = r"\[IDEA_NAME\]:\s*(.*)"
        
        # find all idea names match prefix from AI response
        idea_names = re.findall(pattern, raw_response)
        ideas = []
        for idea_name in idea_names:
            clean_idea_name = name.strip()
            if clean_idea_name:
                ideas.append(clean_idea_name)
                self.history_ideas.add(clean_idea_name)
                
        print(f"🎯 Found / Extracted {len(ideas)} new ideas.")
        return ideas
    
    # @override
    def process_chat(self, response_data, **kwargs):
        # export new ideas
        write_file(
            file=resolve_absolute_path(IDEAS_FILE),
            data=response_data
        )
        
        # update ideas history
        write_json_file(
            file=IDEAS_HISTORY_FILE,
            data=self.history_ideas
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", type=str, help="Domain to find ideas")
    parser.add_argument("--quantity", type=int, help="The number of ideas")
    parser.add_argument("--language", type=str, help="Translate found ideas to language. Ex: Vietnamese, English, etc.")
    args = parser.parse_args()
    IdeaGeneratorAgent(
        domain=args.domain,
        quantity=args.quantity,
        language=args.language
    ).execute()
