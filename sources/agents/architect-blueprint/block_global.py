# BLOCK 1: GENERATES GLOBAL CONTEXT

import os

# GEMINI
# from google import genai
# from google.genai import types

# OpenAI
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    write_blueprint_log,
    write_file,
    render_prompt,
    parseAIResponseData,
    exception_stacktrace,
    get_logger,
    storage_info,
    datetime_for_agent,
    merge_master_prompt
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
def generate_global_context(client: OpenAI, model_name: str, master_rules: str, project_name: str, requirements: str, num_phases: int, max_days_per_phase: int, language: str, out_dir: str) -> str:
    """
    BLOCK 1: Transforms raw text requirements into the supreme global project blueprint.
    Operates inside an isolated transactional API request to maximize logic token efficiency.
    """
    logger.info(f"🏗️  [ BLOCK 1 ] Extracting Raw Requirements into Global Context MD...")
    
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    log_prompt = ""
    log_system_prompt = ""
    model_name_safe = model_name if model_name else "gpt-4o"
    try:
        datetime_prompt, datetime_docid = datetime_for_agent()
        
        # parse system prompt from template
        prompt_context = {
            "project_name": project_name,
            "project_requirements": requirements,
            "doc_id": datetime_docid,
            "current_timestamp": datetime_prompt,
            "language": language or DEFAULT_BLUEPRINT_LANGUAGE,
            "num_phases": num_phases,
            "max_days_per_phase": max_days_per_phase
        }
        # parse system prompt from template
        system_prompt = render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, prompt_context)
        log_system_prompt = system_prompt
        system_prompt = merge_master_prompt(master_rules, system_prompt)
        logger.trace("=============================================================================")
        logger.trace("🤖 Combine MASTER + SYSTEM PROMPTS:")
        logger.trace(system_prompt)
        logger.trace("=============================================================================")
        
        # parse user prompt from template
        user_prompt = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, prompt_context)
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

def generate_global_context_by_chunk(client: OpenAI, model_name: str, master_rules: str, project_name: str, requirements: str, num_phases: int, max_days_per_phase: int, language: str, out_dir: str, force_full_export: bool = False) -> str:
    # full export
    if force_full_export:
        return generate_global_context(
            client=client,
            model_name=model_name,
            master_rules=master_rules,
            project_name=project_name,
            requirements=requirements,
            num_phases=num_phases,
            max_days_per_phase=max_days_per_phase,
            language=language,
            out_dir=out_dir
        )
    
    # BLOCK 1: Transforms raw text requirements into the supreme global project blueprint.
    # Splits the generation pipeline into 3 discrete, non-truncating sequential steps.
    logger.info(f"🏗️ [ BLOCK 1 ] Initiating Multi-Part Progressive Extraction Pipeline...")
    
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    model_name_safe = model_name if model_name else "gpt-4o"
    safe_name = project_name.replace(' ', '-').lower()
    blueprint_file = f"{safe_name}.global.blueprint.md"
    
    # result chunks
    accumulated_blueprint_chunks = []
    
    try:
        datetime_prompt, datetime_docid = datetime_for_agent()
        
        # prompt context
        base_prompt_context = {
            "project_name": project_name,
            "project_requirements": requirements,
            "doc_id": datetime_docid,
            "current_timestamp": datetime_prompt,
            "language": language or DEFAULT_BLUEPRINT_LANGUAGE,
            "num_phases": num_phases,
            "max_days_per_phase": max_days_per_phase,
            "force_full_export": False
        }

        # ==============================================================================
        # CHUNK 1: from Section 1 to the end of Section 4
        # ==============================================================================
        logger.info(f"    |__ [ PART 1/3 ] Generating System Matrix and Master Product Backlog...")
        ctx_part1 = base_prompt_context.copy()
        ctx_part1["target_segment"] = "PART_1_INITIAL"
        
        sys_prompt_p1 = merge_master_prompt(master_rules, render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, ctx_part1))
        usr_prompt_p1 = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, ctx_part1)
        
        res_p1 = client.chat.completions.create(
            model=model_name_safe,
            messages=[{"role": "system", "content": sys_prompt_p1}, {"role": "user", "content": usr_prompt_p1}],
            temperature=0.2
        )
        chunk_1 = parseAIResponseData(res_p1)
        accumulated_blueprint_chunks.append(chunk_1)
        
        # ==============================================================================
        # CHUNK 2: LOOP PHASE IN SECTION 5
        # ==============================================================================
        logger.info(f"    |__ [ PART 2/3 ] Extracting Granular Daylog for {num_phases} phases...")
        accumulated_phase_logs = []
        for phase_idx in range(1, num_phases + 1):
            logger.info(f"             |__ Extracting Granular Daylog for Phase {phase_idx} out of {num_phases}...")
            ctx_part2 = base_prompt_context.copy()
            ctx_part2["target_segment"] = "PART_2_PHASE_LOOP"
            ctx_part2["target_phase_index"] = phase_idx
            # provide backlog table from chunk 1
            ctx_part2["master_backlog_context"] = chunk_1
            
            sys_prompt_p2 = merge_master_prompt(master_rules, render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, ctx_part2))
            usr_prompt_p2 = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, ctx_part2)
            
            res_p2 = client.chat.completions.create(
                model=model_name_safe,
                messages=[{"role": "system", "content": sys_prompt_p2}, {"role": "user", "content": usr_prompt_p2}],
                temperature=0.2
            )
            phase_chunk = parseAIResponseData(res_p2)
            accumulated_phase_logs.append(phase_chunk)
            accumulated_blueprint_chunks.append(phase_chunk)

        # ==============================================================================
        # CHUNK 3: from Section 6 to the end
        # ==============================================================================
        logger.info(f"    |__ [ PART 3/3 ] Generating Universal Security Codes & Git Branch Flow...")
        ctx_part3 = base_prompt_context.copy()
        ctx_part3["target_segment"] = "PART_3_FINAL"
        # provide phase detail logs
        ctx_part3["generated_phases_context"] = "\n\n".join(accumulated_phase_logs)
        
        sys_prompt_p3 = merge_master_prompt(master_rules, render_prompt(GLOBAL_SYSTEM_PROMPT_TEMPLATE_PATH, ctx_part3))
        usr_prompt_p3 = render_prompt(GLOBAL_USER_PROMPT_TEMPLATE_PATH, ctx_part3)
        
        res_p3 = client.chat.completions.create(
            model=model_name_safe,
            messages=[{"role": "system", "content": sys_prompt_p3}, {"role": "user", "content": usr_prompt_p3}],
            temperature=0.2
        )
        chunk_3 = parseAIResponseData(res_p3)
        accumulated_blueprint_chunks.append(chunk_3)

        # ==============================================================================
        # COMBINE ALL CHUNKS
        # ==============================================================================
        raw_data = "\n\n".join(accumulated_blueprint_chunks)
        
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
        write_blueprint_log(0, sys_prompt_p1, usr_prompt_p1.replace('#', '##'), raw_data.replace('#', '##') if raw_data else "-", False, model_name_safe, out_dir)
        
        logger.info(f"✅ [BLOCK 1 SUCCESS] Saved Global Blueprint: {out_path}")
        return raw_data

    except Exception as e:
        logger.error(f"❌ Failed to initiate chat/generate Global Blueprint: {exception_stacktrace(e)}")
        write_blueprint_log(0, "SYSTEM_ERROR", "PIPELINE_CRASH", exception_stacktrace(e), False, model_name_safe, out_dir)
        return None
