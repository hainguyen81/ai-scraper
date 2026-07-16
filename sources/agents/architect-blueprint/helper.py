import os
import sys

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
from ..agent_helper import resolve_absolute_path

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
agent_working_history_file      = resolve_absolute_path("sources/output/architecture-blueprint.md")

def write_log(phase_idx, prompt, raw_content, is_step):
    pattern = r"\{.*\}|\[.*\]"
    raw_content = json_raw_content(raw_content)
    is_json = bool(re.search(pattern, raw_content, re.DOTALL))
    log_content = (
        f"# Global Prompt:\n\n{prompt}\n\n" if phase_idx <= 0 else (f"# Phase {phase_idx} - Prompt:\n\n{prompt}\n\n" if not is_step else f"# Phase {phase_idx} STEPS - Prompt:\n\n{prompt}\n\n")
        f"# Raw Response / Exception:\n\n```json\n{raw_content}\n```\n\n" if is_json else f"# Raw Response / Exception:\n\n```text\n{raw_content}\n```\n\n"
    )
    os.makedirs(os.path.dirname(agent_working_history_file), exist_ok=True)
    with open(agent_working_history_file, "a", encoding="utf-8") as file:
        file.write(log_content)

