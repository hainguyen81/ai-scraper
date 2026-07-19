import os
import sys
import re
import json

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
        response_block = f"# Raw Response / Exception:\n\n```json\n{raw_content}\n```\n\n"
    else:
        response_block = f"# Raw Response / Exception:\n\n```text\n{raw_content}\n```\n\n"
    log_content = header_title + instruction_block + response_block
    os.makedirs(os.path.dirname(agent_working_history_file), exist_ok=True)
    with open(agent_working_history_file, "a", encoding="utf-8") as file:
        file.write(log_content)

def parseOpenAIResponseData(response):
    """
    Safely parses text responses from OpenAI completion models.
    Protects the runtime from attribute errors if content fields are blank or null.
    """
    if not response or not hasattr(response, 'choices') or not response.choices:
        return None
        
    choices_data = response.choices
    
    # Verify that choices structure matches standard list tracking behavior
    if isinstance(choices_data, list) and len(choices_data) > 0:
        first_choice = choices_data[0]
        
        # Guard against malformed message blocks or unexpected payload closures
        if hasattr(first_choice, 'message') and first_choice.message:
            message_obj = first_choice.message
            if hasattr(message_obj, 'content') and message_obj.content:
                return message_obj.content.strip()
                
        # Safe fallback if choice format changes or breaks unexpectedly
        return str(first_choice).strip()
        
    return None

def splitOpenAIResponseJsonData(raw_data):
    clean_json_str = raw_data.strip()
    
    # 💡 Cải tiến: Dùng find() cắt chuỗi block nhanh gọn, chấp mọi loại khoảng trắng/xuống dòng
    lower_raw = clean_json_str.lower()
    start_tag = "```json"
    end_tag = "```"
    
    if start_tag in lower_raw:
        start_idx = lower_raw.find(start_tag) + len(start_tag)
        end_idx = lower_raw.find(end_tag, start_idx)
        if end_idx != -1:
            clean_json_str = clean_json_str[start_idx:end_idx].strip()
    
    elif "```" in lower_raw:
        start_idx = lower_raw.find("```") + 3
        end_idx = lower_raw.find("```", start_idx)
        if end_idx != -1:
            clean_json_str = clean_json_str[start_idx:end_idx].strip()
    
    return clean_json_str

def parseOpenAIResponseJsonData(response):
    """
    Extracts and deserializes raw response texts into fully validated Python dict layouts.
    Leverages non-greedy structural indexing to filter out conversational agent summaries.
    """
    # Ingest text payload through the hardened safety parser above
    raw_data = parseOpenAIResponseData(response)
    
    if not raw_data:
        return (None, None)
        
    # Pattern 1: Targeted scan for standard markdown language JSON codeblocks
    json_match = re.search(r"```json\s*([\s\S]*?)\s*```", raw_data, re.DOTALL)
    if json_match:
        try:
            clean_json_str = json_match.group(1).strip()
            return (raw_data, json.loads(clean_json_str))
        except Exception:
            pass # Continue evaluating alternative pattern structures if parsing breaks
            
    # Pattern 2: Generic codeblock fallback without language tags
    json_match = re.search(r"```\s*([\s\S]*?)\s*```", raw_data, re.DOTALL)
    if json_match:
        try:
            clean_json_str = json_match.group(1).strip()
            return (raw_data, json.loads(clean_json_str))
        except Exception:
            pass

    # Pattern 3: Hardened bracket boundary locator leveraging non-greedy isolation
    # Fixes the broken greedy regex logic to ensure text outside the curly braces is safely ignored
    try:
        return (raw_data, json.loads(splitOpenAIResponseJsonData(raw_data)))
    except Exception as e:
        json_match = re.search(r"(\{[\s\S]*\})", raw_data, re.DOTALL)
        if json_match:
            try:
                clean_json_str = json_match.group(1).strip()
                return (raw_data, json.loads(clean_json_str))
            except Exception:
                pass
        
        else:
            pass
            
    # Final Fallback Layer: Treat the whole string as literal plain text payload
    try:
        return (raw_data, json.loads(raw_data.strip()))
    except Exception as final_error:
        print(f"⚠️  [PARSER WARNING] Local string-to-json mapping failed: {final_error}")
        return (raw_data, None)