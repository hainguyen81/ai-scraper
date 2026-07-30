# BLOCK 1: GENERATES GLOBAL CONTEXT

import os

# GEMINI
# from google import genai
# from google.genai import types

# OpenAI
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    resolve_absolute_path,
    write_blueprint_log,
    write_file,
    render_prompt,
    parseAIResponseData,
    exception_stacktrace,
    get_logger,
    storage_info,
    datetime_for_agent
)

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
STORAGE                                 = storage_info.get("storage") or {}
STORAGE_AGENTS                          = storage_info.get("agents") or {}
STORAGE_OUTPUT                          = storage_info.get("output") or {}

STORAGE_BLUEPRINT                       = STORAGE.get("storage_blueprint") or {}
STORAGE_AGENT_BLUEPRINT_PROMPTS         = STORAGE_AGENTS.get("storage_blueprint_prompts") or {}

GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH      = os.path.join(STORAGE_AGENT_BLUEPRINT_PROMPTS, "block_global_prompt.system.md")
GLOBAL_USER_PROMPT_TEMPLATE_PATH        = os.path.join(STORAGE_AGENT_BLUEPRINT_PROMPTS, "block_global_prompt.user.md")

DEFAULT_BLUEPRINT_LANGUAGE              = "English"

logger = get_logger("🏗️ EnterpriseSystemArchitectureGlobalAgent")

# GEMINI
# def generate_global_context(client: genai.Client, project_name: str, requirements: str, num_phases: int, out_dir: str) -> str:

# OpenAI
def generate_global_context(client: OpenAI, model_name: str, project_name: str, requirements: str, num_phases: int, max_days_per_phase: int, language: str, out_dir: str) -> str:
    """
    BLOCK 1: Transforms raw text requirements into the supreme global project blueprint.
    Operates inside an isolated transactional API request to maximize logic token efficiency.
    """
    logger.info(f"🏗️  [BLOCK 1] Extracting Raw Requirements into Global Context MD...")
    
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    log_prompt = ""
    log_system_prompt = ""
    model_name_safe = model_name if model_name else "gpt-4o"
    try:
        datetime_prompt, datetime_docid = datetime_for_agent()
        
        # parse system prompt from template
        system_prompt_context = {
            "project_name": project_name,
            "num_phases": num_phases,
            "max_days_per_phase": max_days_per_phase,
            "language": language or DEFAULT_BLUEPRINT_LANGUAGE
        }
        system_prompt = render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, system_prompt_context)
        log_system_prompt = system_prompt
        
        # parse user prompt from template
        user_prompt_context = {
            "project_name": project_name,
            "project_requirements": requirements,
            "num_phases": num_phases,
            "max_days_per_phase": max_days_per_phase,
            "doc_id": datetime_docid,
            "current_timestamp": datetime_prompt
        }
        user_prompt = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, user_prompt_context)
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
        
        # convert project name
        safe_name = project_name.replace(' ', '-').lower()
        blueprint_file = f"{safe_name}.global.blueprint.md"
        
        # export to storage
        out_path = write_file(
            dir=os.path.join(STORAGE_BLUEPRINT, safe_name, "context"),
            file=blueprint_file,
            data=raw_data
        )
        
        # export to output path
        out_path = write_file(
            dir=os.path.join(out_dir, "context"),
            file=blueprint_file,
            data=raw_data
        )
        
        # write log
        write_blueprint_log(0, system_prompt, log_prompt.replace('#', '##'), raw_data.replace('#', '##') if raw_data else "-", False, model_name_safe, out_dir)
        
        logger.info(f"✅ [BLOCK 1 SUCCESS] Saved Global Blueprint: {out_path}")
        return raw_data
    except Exception as e:
        logger.error(f"❌ Failed to initiate chat/generate Global Blueprint: {exception_stacktrace(e)}")
        write_blueprint_log(0, log_system_prompt, log_prompt.replace('#', '##'), exception_stacktrace(e), False, model_name_safe, out_dir)
        return None

