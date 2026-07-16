import os
import sys
import re

# ==============================================================================
# 🏢 ENTERPRISE INTER-PACKAGE ROUTING LAYER
# ==============================================================================
# Programmatically appends the parent directory (.ai/.agents/) into Python's runtime
# search path array. This completely unlocks importing 'agent_helper.py'.
# ==============================================================================
CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # .ai/.agents/.sub-agents/
PARENT_AGENTS_DIR  = os.path.abspath(os.path.join(CURRENT_SCRIPT_DIR, "../")) # .ai/.agents/

# jump to `agent_helper.py` folder path
if PARENT_AGENTS_DIR not in sys.path:
    sys.path.insert(0, PARENT_AGENTS_DIR)

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import resolve_absolute_path
from sources.agents.agent_helper import json_raw_content

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
agent_working_history_file      = resolve_absolute_path("sources/output/architecture-blueprint.md")

def write_log(phase_idx, instruction, prompt, raw_content, is_step):
    pattern = r"\{.*\}|\[.*\]"
    raw_content = json_raw_content(raw_content)
    is_json = bool(re.search(pattern, raw_content, re.DOTALL))
    if phase_idx <= 0:
        header_title = f"# Global Prompt:\n\n{prompt}\n\n"
    elif not is_step:
        header_title = f"# Phase {phase_idx} - Prompt:\n\n{prompt}\n\n"
    else:
        header_title = f"# Phase {phase_idx} STEPS - Prompt:\n\n{prompt}\n\n"
    instruction_block = f"# System Instruction\n\n{instruction}\n\n"
    if is_json:
        response_block = f"# Raw Response / Exception:\n\n```json\n{cleaned_content}\n```\n\n"
    else:
        response_block = f"# Raw Response / Exception:\n\n```text\n{cleaned_content}\n```\n\n"
    log_content = header_title + instruction_block + response_block
    os.makedirs(os.path.dirname(agent_working_history_file), exist_ok=True)
    with open(agent_working_history_file, "a", encoding="utf-8") as file:
        file.write(log_content)

def parseOpenAIResponseData(response):
    choices_data = response.choices if response and response.choices else None
    raw_data = None
    if choices_data and isinstance(choices_data, list) and len(choices_data) > 0:
        first_choice = choices_data[0]
        raw_data = first_choice.message.content.strip() if hasattr(first_choice, 'message') else str(first_choice)
    
    else:
        # Standard OpenAI object layout behavior fallback
        raw_data = choices_data.message.content.strip() if choices_data and choices_data.message and choices_data.message.content else None
    
    return raw_data

def parseOpenAIResponseJsonData(response):
    raw_data = parseOpenAIResponseData(response)
    
    # ✅ ROBUST REGEX EXTRACTION: Isolate nested JSON bracket layouts to eliminate markdown wrapper block errors
    if raw_data:
        json_match = re.search(r'\{.*\}', raw_data, re.DOTALL)
        if json_match:
            clean_json_str = json_match.group(0)
            json_data = json.loads(clean_json_str)
        else:
            json_data = json.loads(raw_data)
        return (raw_data, json_data)
    return (raw_data, None)
