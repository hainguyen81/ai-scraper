# BLOCK 1: GENERATES GLOBAL CONTEXT

import os
import sys

# GEMINI
# from google import genai
# from google.genai import types

# OpenAI
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import resolve_absolute_path
from helper import write_log
from helper import write_file
from helper import render_prompt
from helper import parseOpenAIResponseData

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
PROMPT_TEMPLATE_PATH = resolve_absolute_path("sources/agents/architect-blueprint/block_global_prompt.md")

# GEMINI
# def generate_global_context(client: genai.Client, project_name: str, requirements: str, num_phases: int, out_dir: str) -> str:

# OpenAI
def generate_global_context(client: OpenAI, model_name: str, project_name: str, requirements: str, num_phases: int, max_days_per_phase: int, out_dir: str) -> str:
    """
    BLOCK 1: Transforms raw text requirements into the supreme global project blueprint.
    Operates inside an isolated transactional API request to maximize logic token efficiency.
    """
    print(f"🏗️  [BLOCK 1] Extracting Raw Requirements into Global Context MD...")
    
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    log_prompt = ""
    instruction = "You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails."
    try:
        # parse prompt from template
        prompt_context = {
            "project_name": project_name,
            "project_requirements": requirements,
            "num_phases": num_phases,
            "max_days_per_phase": max_days_per_phase
        }
        prompt = render_prompt(PROMPT_TEMPLATE_PATH, prompt_context)
        log_prompt = prompt
        
        # GEMINI
        # response = client.models.generate_content(
        #     model='gemini-2.5-pro',
        #     contents=prompt,
        #     config=types.GenerateContentConfig(system_instruction=instruction, temperature=0.2)
        # )
        # raw_data = response.text
        
        # OpenAI
        response = client.chat.completions.create(
            model=model_name if model_name else "gpt-4o",
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        raw_data = parseOpenAIResponseData(response)
        
        # write context
        safe_name = project_name.replace(' ', '-')
        out_path = write_file(
            dir=os.path.join(out_dir, "context"),
            file_name=f"{safe_name}.global.blueprint.md",
            data=raw_data
        )
        
        # write log
        write_log(0, instruction, log_prompt.replace('#', '##'), raw_data.replace('#', '##') if raw_data else "-", False)
        
        print(f"✅ [BLOCK 1 SUCCESS] Saved Global Blueprint: {out_path}")
        return raw_data
    except Exception as e:
        print(f"❌ Failed to initiate chat/generate Global Blueprint: {e}")
        write_log(0, instruction, log_prompt.replace('#', '##'), str(e), False)
        return None

