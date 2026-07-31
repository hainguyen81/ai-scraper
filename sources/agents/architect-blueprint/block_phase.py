# BLOCK 2: GENERATES PHASE MARKDOWN

import os
import time

# GEMINI
# from google import genai
# from google.genai import types

# OpenAI
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    resolve_absolute_path,
    exception_stacktrace,
    write_blueprint_log,
    write_file,
    render_prompt,
    parseAIResponseData,
    get_logger,
    storage_info,
    datetime_for_agent
)

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
STORAGE                             = storage_info.get("storage") or {}
STORAGE_AGENTS                      = storage_info.get("agents") or {}
STORAGE_OUTPUT                      = storage_info.get("output") or {}

STORAGE_BLUEPRINT                   = STORAGE.get("storage_blueprint") or {}
STORAGE_AGENT_BLUEPRINT_PROMPTS     = STORAGE_AGENTS.get("storage_blueprint_prompts") or {}

PHASE_SYSTEM_PROMPT_TEMPLATE_PATH   = os.path.join(STORAGE_AGENT_BLUEPRINT_PROMPTS, "block_phase_prompt.system.md")
PHASE_USER_PROMPT_TEMPLATE_PATH     = os.path.join(STORAGE_AGENT_BLUEPRINT_PROMPTS, "block_phase_prompt.user.md")

DEFAULT_BLUEPRINT_LANGUAGE          = "English"

logger = get_logger("🏗️ EnterpriseSystemArchitecturePhaseAgent")

# GEMINI
# def generate_phase_contexts(client: genai.Client, project_name: str, requirements: str, global_context: str, num_phases: int, out_dir: str):

# OpenAI
def generate_phase_contexts(client: OpenAI, model_name: str, project_name: str, requirements: str, global_context: str, num_phases: int, max_days_per_phase: int, language: str, out_dir: str, delay: int):
    """
    BLOCK 2: Decomposes requirements into segmented, sandbox-ready development boundaries.
    Executes raw isolated stateless calls per loop item to bypass sequence length degradation.
    """
    logger.info(f"🔄 [BLOCK 2] Decomposing requirements into {num_phases} isolated Phase Markdowns...")
    
    delay = delay if delay else 3
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    log_phase_idx = 0
    log_prompt = ""
    log_system_prompt = ""
    model_name_safe = model_name if model_name else "gpt-4o"
    try:
        datetime_prompt, datetime_docid = datetime_for_agent()
        previous_phase_context = ""
        for phase_idx in range(1, num_phases + 1):
            log_phase_idx = phase_idx
            logger.info(f" │   ├── 📝 Compiling Context Markdown for Phase {phase_idx} of {num_phases}...")
            
            # parse system prompt from template
            prompt_context = {
                "project_name": project_name,
                "project_requirements": requirements,
                "doc_id": datetime_docid,
                "current_timestamp": datetime_prompt,
                "language": language or DEFAULT_BLUEPRINT_LANGUAGE,
                "num_phases": num_phases,
                "max_days_per_phase": max_days_per_phase,
                "global_markdown_context": global_context,
                "previous_phase_context": previous_phase_context
            }
            system_prompt = render_prompt(PHASE_SYSTEM_PROMPT_TEMPLATE_PATH, prompt_context)
            log_system_prompt = system_prompt
            
            # parse user prompt from template
            user_prompt = render_prompt(PHASE_USER_PROMPT_TEMPLATE_PATH, prompt_context)
            log_prompt = user_prompt
            
            # GEMINI
            # response = client.models.generate_content(
            #     model='gemini-2.5-pro',
            #     contents=prompt,
            #     config=types.GenerateContentConfig(system_instruction=system_prompt, temperature=0.2)
            # )
            # raw_data = response.text
            
            # OpenAI
            response = client.chat.completions.create(
                model=model_name_safe,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2
            )
            raw_data = parseAIResponseData(response)
            previous_phase_context = raw_data

            # convert project name
            safe_name = project_name.replace(' ', '-').lower()
            phase_blueprint_file = f"phase-{phase_idx}.context.blueprint.md"
            
            # export to storage
            out_path = write_file(
                dir=os.path.join(STORAGE_BLUEPRINT, safe_name, "plan", "context"),
                file=phase_blueprint_file,
                data=raw_data
            )
            
            # export output context
            out_path = write_file(
                dir=os.path.join(out_dir, "plan", "context"),
                file=phase_blueprint_file,
                data=raw_data
            )
        
            # write log
            write_blueprint_log(log_phase_idx, system_prompt, log_prompt.replace('#', '##'), raw_data.replace('#', '##') if raw_data else "-", False, model_name_safe, out_dir)
            
            logger.info(f" │   ├── ✅ Saved Phase {phase_idx} MD: {out_path}")
            
            # sleep to avoid 429 Too Many Requests
            if phase_idx < num_phases + 1:
                logger.debug(f"⏳ Rate limit guard active... holding pipeline for { delay } seconds to clear AI TPM window...")
                time.sleep(delay)
            
        result = True if num_phases > 0 else False
        return result # success or empty phases
    except Exception as e:
        logger.error(f"❌ Failed to initiate chat/generate Phase {log_phase_idx} Blueprint: {exception_stacktrace(e)}")
        write_blueprint_log(log_phase_idx, log_system_prompt, log_prompt.replace('#', '##'), exception_stacktrace(e), False, model_name_safe, out_dir)
        return False

