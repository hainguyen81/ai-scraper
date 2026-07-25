import os
import sys
import json
import re
import hashlib
import argparse
from datetime import datetime
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    resolve_absolute_path,
    read_json_file,
    write_json_file,
    write_file,
    kwargs_by_key
)

# super agent
from sources.agents.agent_super import AbstractAgent

# models list
USER_PROMPT_TEMPLATE  = resolve_absolute_path("sources/agents/ideas/agent_idea_generator.prompt.md")
IDEAS_STORAGE_PATH          = resolve_absolute_path("sources/storage/ideas")
IDEAS_OUTPUT_PATH           = resolve_absolute_path("sources/output/ideas")
IDEAS_HISTORY_FILE          = os.path.join(IDEAS_STORAGE_PATH, "history_ideas.json")
IDEAS_OUTPUT_FILE           = os.path.join(IDEAS_OUTPUT_PATH, "ideas.md")
IDEAS_LOG_FILE              = os.path.join(IDEAS_OUTPUT_PATH, "ideas_log.md")
DEFAULT_IDEAS_DOMAIN        = "Any high-momentum, trending industry in 2026 (such as AI Agents, Automation Web-apps, Renewable Energy tech, Spatial Computing, Web3/Fintech, etc.) where a lightweight software solution or Micro-SaaS can be rapidly deployed to capture immediate market demand with an MVP built within 2-4 weeks"
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
        return USER_PROMPT_TEMPLATE
    
    # @override
    def agent_temperature(self):
        return 0.8 # high ides
    
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
        history_ideas_len = len(history_ideas)
        
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
            idea_file = os.path.join(IDEAS_STORAGE_PATH, f"{idea_id}.md")
            idea_content = f"# {clean_idea_name}\n\n{clean_idea_desc}"
            idea_item = {
                "id": idea_id,
                "idea": clean_idea_name,
                "file": idea_file
            }
            ideas.append({
                **idea_item,
                "content": idea_content
            })
            history_ideas.append({ **idea_item })
        self.history_ideas = history_ideas
                
        print(f"[ 🎯 {self.agent_id} Agent ] Found / Extracted: {len(ideas)} new ideas.")
        return ideas
    
    # @override
    def process_chat(self, response_data, **kwargs):
        # export new ideas as md files
        for idea in response_data:
            write_file(
                file=idea.get("file"),
                data=idea.get("content")
            )
        
        # update ideas history
        write_json_file(
            file=IDEAS_HISTORY_FILE,
            json_data=self.history_ideas
        )
        
        # export raw response if necessary as log tracing
        raw_response = kwargs_by_key(key="raw_response", **kwargs)
        if raw_response:
            write_file(
                file=IDEAS_OUTPUT_FILE,
                data=raw_response
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
