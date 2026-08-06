# ENTERPRISE MAIN ORCHESTRATOR RUNNER

import os
import sys
import json
import time

# GEMINI
#from google import genai
#from google.genai import types

# OpenAI
from openai import OpenAI

# Import decoupled functional components cleanly
from block_global import generate_global_context, logger as global_logger
from block_phase import generate_phase_contexts, logger as phase_logger
from block_json import convert_phases_to_json, logger as steps_logger

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import (
    resolve_absolute_path,
    delete_log,
    read_json_file,
    write_json_file,
    count_files_by_pattern,
    read_file_raw,
    get_logger,
    json_loads,
    parse_args,
    storage_info,
    enabledLogDebug,
    render_prompt,
    exception_stacktrace
)

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
STORAGE                         = storage_info.get("storage") or {}
STORAGE_AGENTS                  = storage_info.get("agents") or {}
STORAGE_OUTPUT                  = storage_info.get("output") or {}

REL_STORAGE_BLUEPRINT           = STORAGE.get("relative_blueprint") or {}
STORAGE_MASTER_PROMPTS          = STORAGE_AGENTS.get("storage_master_prompts") or {}
STORAGE_BLUEPRINT               = resolve_absolute_path(REL_STORAGE_BLUEPRINT)

MASTER_PROMPT_TEMPLATE_PATH     = os.path.join(STORAGE_MASTER_PROMPTS, "prompt.rule.enterprise.governance.guardrails.md")

BA_STORAGE_PATH                 = STORAGE.get("storage_ba") or {}
PROJECTS_SUMMARY_FILE           = os.path.join(BA_STORAGE_PATH, "projects-summary.json")

REL_REQUIREMENTS_STORAGE_PATH   = STORAGE.get("relative_requirements") or {}
REQUIREMENTS_FILE               = "requirements.md"

MODELS_POOL_PATH                = resolve_absolute_path("sources/agents/models/models.json")
MODELS_SECRETS_ENV_KEY          = "AI_MODELS_KEYS_JSON"
PLAN_SPEC_FILE                  = "plan.spec.json"

DEFAULT_BLUEPRINT_LANGUAGE      = "English"

logger = get_logger("🏗️ EnterpriseSystemArchitectureAgent")

def load_models_pool():
    _, models_json = read_json_file(MODELS_POOL_PATH)
    return models_json

def load_models_keys():
    json_key_secrets = os.environ.get(MODELS_SECRETS_ENV_KEY)
    if not json_key_secrets:
        logger.warning(f"[ ⚠️ WARN ] The environment variable '{MODELS_SECRETS_ENV_KEY}' is completely absent.")
        return None
    
    return json_loads(json_key_secrets)
    
def __close_ai_client__(client, logger):
    if client:
        try:
            client.close()
        except Exception as e:
            logger.error(f"⚠️ Exception while closing AI client: {exception_stacktrace(e)}")

def rotate_matching_model(json_ai_models, json_ai_keys, model_idx):
    models_len = len(json_ai_models) if json_ai_models else 0
    
    while model_idx < models_len and json_ai_keys and isinstance(json_ai_keys, dict):
        config = json_ai_models[model_idx]
        target_model_name = config.get("model_name") if isinstance(config, dict) else None
        target_model_endpoint = config.get("api_endpoint") if isinstance(config, dict) else None
        
        logger.debug("==============================================")
        logger.debug("🔍 DEBUG: 'config':")
        try:
            logger.debug(json.dumps(config, indent=4, ensure_ascii=False))
        except Exception:
            logger.error(f"⚠️ Exception while dump 'config' json: {type(config)} - Config: {config}")
        logger.debug("==============================================")
        
        # If endpoint is missing, None, empty "", or just whitespaces "   ", skip it cleanly
        if not target_model_name or not target_model_endpoint or not str(target_model_endpoint).strip():
            logger.warning(f"⚠️ Ignore this config due to invalid 'model_name': {target_model_name} or 'model_endpoint': {target_model_endpoint}")
            model_idx += 1
            continue # 🔄 Immediately jumps to the next iteration of the while loop
        
        # Lookup the API Key inside the GitHub Secret JSON dictionary using the model_name from models.json
        api_key = json_ai_keys.get(target_model_endpoint)
        if api_key:
            logger.info(f"[ 💀 FAILOVER ENGAGED ] Found AI model: {target_model_name} | endpoint: {target_model_endpoint}")
            return (model_idx, config, api_key)
        else:
            logger.warning(f"[ ⚠️ WARNING ] API key missing inside GitHub JSON for model: {target_model_name} | endpoint: {target_model_endpoint}. Skipping tier.")
            model_idx += 1
    
    return (-1, None, None)

def find_project_requirements(project_name: str):
    if not project_name:
        logger.warning("[ ⚠️ WARNING ] Invalid project_name to search. Skipping tier.")
        return (None, None)
    
    # read projects summaize
    _, projects = read_json_file(file_path=PROJECTS_SUMMARY_FILE)
    if not projects:
        logger.warning(f"[ ⚠️ WARNING ] Not found %s to search. Skipping tier.", PROJECTS_SUMMARY_FILE)
        return (None, None)
    
    # filter to find project
    project_info = next((pi for pi in projects if isinstance(pi, dict) and project_name in [ pi.get("technical_codename"), pi.get("idea"), pi.get("brand_name") ]), None)
    if not project_info:
        logger.warning(f"[ ⚠️ WARNING ] Not found {project_name} from projects list of BA. Skipping tier.")
        return (None, None)
    
    return (project_info.get("technical_codename"), project_info.get("requirements"))

def run_architect_agent(
    project_name: str, requirements_path: str,
    num_phases: int, max_days_per_phase: int, output_dir: str,
    api_key: str, api_endpoint: str, api_model_global: str, api_model_phase: str, api_model_steps: str, api_model_steps_mapping: str,
    exec_mode: int, exec_delay: int, daysPerChunk: int, language: str,
    rotate_model: bool
):
    # check arguments
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    exec_mode = exec_mode if exec_mode >= 0 and exec_mode <= 4 else 0
    exec_delay = exec_delay if exec_delay else 3
    is_build_all = exec_mode == 0
    is_build_global = is_build_all or exec_mode in (0, 1)
    is_build_phase = is_build_all or exec_mode in (0, 2)
    is_build_steps = is_build_all or exec_mode in (0, 3)
    is_build_plan_spec = exec_mode not in (0, 1, 2, 3)
    
    # -------------------------------------------------
    # Should detect project first to request requirements from BA
    # -------------------------------------------------
    # not specify requirements file
    if not requirements_path:
        # detect requirements based on project name from BA storage
        detected_project_name, detected_requirements_file = find_project_requirements(project_name)
        # if found, should re-update inputted parameters
        if detected_project_name and detected_requirements_file:
            project_name = detected_project_name
            requirements_path = detected_requirements_file
        
    # not found requirements from BA storage, then detecting from requirements storage
    if not requirements_path:
        requirements_path = os.path.join(REL_REQUIREMENTS_STORAGE_PATH, project_name, REQUIREMENTS_FILE)
    
    # if need to build project context/steps, then checking the existing requirements file
    logger.info(f"\n🎉 Analyze project {project_name} with requirements {requirements_path}...")
    physical_requirements_path = resolve_absolute_path(requirements_path)
    if not is_build_plan_spec and not os.path.exists(physical_requirements_path):
        logger.critical(f"❌ [ CRITICAL ] Target requirements file not found at: {requirements_path}")
        sys.exit(1)
    
    # read requirements
    project_requirements = None
    if not is_build_plan_spec:
        _, project_requirements = read_file_raw(physical_requirements_path)
    
    # safely project name
    safe_name = project_name.replace(' ', '-')
    
    # make sure output directory existing
    relative_out_dir = os.path.join(output_dir, safe_name)
    absolute_out_dir = resolve_absolute_path(relative_out_dir)
    os.makedirs(absolute_out_dir, exist_ok=True)
    
    # remove previous log if necessary
    delete_log(absolute_out_dir)
    
    # resolve JSON mapping configuration file path
    absolute_api_model_steps_mapping = None
    if api_model_steps_mapping and os.path.exists(resolve_absolute_path(api_model_steps_mapping)):
        absolute_api_model_steps_mapping = resolve_absolute_path(api_model_steps_mapping)
    
    # parse master prompt rules from template
    master_rules = None
    if not is_build_plan_spec:
        logger.trace("=============================================================================")
        logger.trace(f"🤖 Master Rule File: {MASTER_PROMPT_TEMPLATE_PATH}")
        logger.trace("=============================================================================")
        master_rules = render_prompt(MASTER_PROMPT_TEMPLATE_PATH, {
            "language": language or DEFAULT_BLUEPRINT_LANGUAGE,
        })
        logger.trace(master_rules)
    
    # Master pipeline orchestrator that runs individual functional blocks in sequence.
    # Provides pristine separation of concerns and protects engine runtime stability.
    
    json_ai_models = None
    json_ai_keys = None
    # need to rotate, so loading models / api keys configuration
    if not is_build_plan_spec and rotate_model:
        json_ai_models = load_models_pool()
        json_ai_keys = load_models_keys()
    model_idx = -1
    models_len = len(json_ai_models) if json_ai_models else 0
    
    # whether should loop processes based on rotating AI models
    result_global = None
    result_phase = False if exec_mode in (0, 2) else True       # Phase should be ok if not running it
    result_steps = False if exec_mode in (0, 3) else True       # Steps should be ok if not running it
    everything_ok = False
    client = None
    while not everything_ok and model_idx < models_len:
        # rotate to find matching AI models
        if model_idx >= 0:
            # not found any registered matching AI model
            rotate_idx, config, rotate_api_key = rotate_matching_model(json_ai_models, json_ai_keys, model_idx)
            if rotate_idx < 0 or not config or not rotate_api_key:
                logger.critical("[ 💀 CRITICAL ] Not found any more registered AI models with valid keys.")
                break
            
            # found registered matching AI model, but information is invalid
            model_idx = rotate_idx
            api_model_global = config.get("model_name") if isinstance(config, dict) else None
            api_model_phase = api_model_global
            api_model_steps = api_model_global
            api_endpoint = config.get("api_endpoint") if isinstance(config, dict) else None
            api_key = rotate_api_key
            if not api_model_global or not api_endpoint or not api_key:
                logger.critical("[ 💀 CRITICAL ] Invalid registered AI models. Missing Endpoint, Model or API Key.")
                break
        
        # first time
        else:
            api_model_phase = api_model_phase if api_model_phase else api_model_global
            api_model_steps = api_model_steps if api_model_steps else api_model_phase
            api_model_steps = api_model_steps if api_model_steps else api_model_global
        
        # close old AI client if existing
        __close_ai_client__(client, logger)
        
        # GEMINI
        # client = genai.Client(api_key=api_key)
        
        # OpenAI
        if not is_build_plan_spec:
            client = OpenAI(
                base_url=api_endpoint,
                api_key=api_key,
                # 0 to turn off retries
                max_retries=3, 
                # timeout in seconds (600 seconds ~ 10 minutes)
                timeout=600.0
            )
        
        logger.info("=============================================================================")
        logger.info(f"🤖 AI: Endpoint {api_endpoint}. Mode '0' for all.")
        logger.info(f"    - Global Context:               {api_model_global}. Mode 1")
        logger.info(f"    - Phase Context:                {api_model_phase}.  Mode 2")
        logger.info(f"    - Phase JSON Steps:             {api_model_steps}.  Mode 3")
        logger.info(f"    - Phase JSON Steps Mapping:     {api_model_steps_mapping}")
        logger.info(f"    - Build Plan Spec:              {api_model_steps}.  Mode 4")
        logger.info(f"    - Execution Mode:               {exec_mode}")
        logger.info(f"    - Execution Delay:              {exec_delay}")
        logger.info(f"    - Language:                     {language}")
        logger.info(f"    - Max Phases:                   {num_phases}")
        logger.info(f"    - Max Days Per Phase:           {max_days_per_phase}")
        logger.info(f"    - Out Directory:                {relative_out_dir}")
        logger.info("=============================================================================")
        logger.info(f"    - ROTATE MODEL INTEGRATION:     {model_idx}")
        logger.info("=============================================================================")
        
        # -------------------------------------------------
        # 1. Execute Block 1 Module
        # -------------------------------------------------
        if is_build_global and not result_global:
            result_global = generate_global_context(
                client=client,
                model_name=api_model_global,
                master_rules=master_rules,
                project_name=project_name,
                requirements=project_requirements,
                num_phases=num_phases,
                max_days_per_phase=max_days_per_phase,
                language=language,
                out_dir=absolute_out_dir
            )
            
            # sleep to avoid 429 Too Many Requests
            if result_global:
                logger.debug(f"⏳ Rate limit guard active... holding pipeline for { exec_delay } seconds to clear AI TPM window...")
                time.sleep(exec_delay)
        
        # no need AI, just reading from existing context file
        elif not is_build_plan_spec and not result_global:
            context_dir = os.path.join(absolute_out_dir, "context")
            global_context_file = os.path.join(context_dir, f"{safe_name}.global.blueprint.md")
            if not os.path.exists(global_context_file):
                global_context_file = os.path.join(
                    STORAGE_BLUEPRINT, safe_name, "context", f"{safe_name}.global.blueprint.md")
            
            # read existing global context
            with open(global_context_file, "r", encoding="utf-8") as f:
                result_global = f.read()
        
        # if failed, check whether should rotate model
        if not is_build_plan_spec and not result_global:
            logger.warning(f"\n[ 🤖💬 WARN ] Modular Enterprise Architecture Pipeline Executed: Fail to generate project global context!")
            
            # should rotate to find other models
            if rotate_model:
                model_idx += 1
                continue
            
            # out of function if not rotating
            break
        
        # fake global context if building plan spec
        elif is_build_plan_spec:
            result_global = f"\n[ 🤖💬 WARN ] No need project global context, due to building plan spec!"
        
        # -------------------------------------------------
        # 2. Execute Block 2 Module
        # -------------------------------------------------
        if is_build_phase and not result_phase:
            global_context_text = result_global
            result_phase = generate_phase_contexts(
                client=client,
                model_name=api_model_phase,
                master_rules=master_rules,
                project_name=project_name,
                requirements=project_requirements,
                global_context=global_context_text,
                num_phases=num_phases,
                max_days_per_phase=max_days_per_phase,
                language=language,
                out_dir=absolute_out_dir,
                delay=exec_delay
            )
            
            # sleep to avoid 429 Too Many Requests
            if result_phase:
                logger.debug("⏳ Rate limit guard active... holding pipeline for 15 seconds to clear AI TPM window...")
                time.sleep(5)
            
            else:
                logger.warning("\n[ 🤖💬 WARN ] Modular Enterprise Architecture Pipeline Executed: Fail to generate project phase contexts!")
                
                # should rotate to find other models
                if rotate_model:
                    model_idx += 1
                    continue
                
                # out of function if not rotating
                break
        
        # fake phase result if building plan spec
        elif is_build_plan_spec:
            result_phase = True
        
        # -------------------------------------------------
        # 3. Execute Block 3 Module
        # -------------------------------------------------
        if is_build_steps and not result_steps:
            result_steps = convert_phases_to_json(
                client=client,
                model_name=api_model_steps,
                master_rules=master_rules,
                project_name=project_name,
                num_phases=num_phases,
                max_days_per_phase=max_days_per_phase,
                language=language,
                json_mapping=absolute_api_model_steps_mapping,
                out_dir=absolute_out_dir,
                delay=exec_delay,
                daysPerChunk=daysPerChunk
            )
            if not result_steps:
                logger.warning("\n[ 🤖💬 WARN ] Modular Enterprise Architecture Pipeline Executed: Fail to generate project phase JSON steps!")
                
                # should rotate to find other models
                if rotate_model:
                    model_idx += 1
                    continue
                
                # out of function if not rotating
                break
        
        # fake phase steps if building plan spec
        elif is_build_plan_spec:
            result_steps = True
        
        # check everything whether is ok
        everything_ok = result_global and result_phase and result_steps
        
        # -------------------------------------------------
        # 4. Re-build Plan Spec
        # -------------------------------------------------
        plan_context_dir = os.path.join(absolute_out_dir, "plan")
        if is_build_plan_spec:
            phase_file_pattern = "phase-*.context.blueprint.md"
            num_phases = count_files_by_pattern(os.path.join(plan_context_dir, "context"), phase_file_pattern) if everything_ok else 0
            # try to detect from storage blueprint
            if num_phases <= 0:
                num_phases = count_files_by_pattern(
                    os.path.join(STORAGE_BLUEPRINT, safe_name, "context"), phase_file_pattern) if everything_ok else 0
        plan_spec = {
            "project_name": project_name,
            "requirements": requirements_path,
            "num_phases": num_phases,
            "total_days": 0,
            "phases": []
        }
        # if everything is ok, should building plan spec
        if everything_ok:
            # build plan spec
            steps_context_dir = os.path.join(plan_context_dir, "steps")
            for phase_idx in range(1, num_phases + 1):
                phase_steps_file = os.path.join(steps_context_dir, f"phase-{phase_idx}.steps.json")
                _, steps_data = read_json_file(phase_steps_file)
                plan_spec["phases"].append({
                    "phase": phase_idx,
                    "days": len(steps_data.get("days", [])) if steps_data else 0
                })
        
        # sum total_days
        plan_spec["total_days"] += sum(item["days"] for item in plan_spec["phases"])
        
        # write to storage
        logger.info(f"\n🎉 [ INFO ] Modular Enterprise Architecture Plan Spec: {json.dumps(plan_spec, indent=4, ensure_ascii=False)}")
        write_json_file(dir=os.path.join(STORAGE_BLUEPRINT, safe_name, "plan"), file=PLAN_SPEC_FILE, json_data=plan_spec)
        
        # write output plan spec
        write_json_file(dir=plan_context_dir, file=PLAN_SPEC_FILE, json_data=plan_spec)
    
    # close AI client if existing
    __close_ai_client__(client, logger)
    
    # log for tracing
    if not everything_ok:
        logger.error(f"\n❌ [ FAILED ] Modular Enterprise Architecture Pipeline Executed Failed: Global?. { True if result_global else False } - Phase { result_phase } - Steps { result_steps }")
    
    # everything is ok
    else:
        logger.info("\n🎉 [ SUCCESS ] Modular Enterprise Architecture Pipeline Executed Perfectly!")
    
    # result should be good for all
    return everything_ok

def str2bool(v):
    return str(v).lower() in ("yes", "true", "t", "1")

if __name__ == "__main__":
    def add_known_arguments(parser):
        parser.add_argument("--project-name", type=str, required=True, help="Project Name / Idea Identity")
        parser.add_argument("--req", type=str, default="sources/requirements/test-requirements.md", help="Path to the raw project requirements file")
        parser.add_argument("--phases", type=int, default=3, help="Total number of execution phases to segment")
        parser.add_argument("--out", type=str, default="sources/output/blueprint", help="Target output directory for the generated blueprint")
        parser.add_argument("--api-key", type=str, required=True, help="AI API Key is required")
        parser.add_argument("--api-endpoint", type=str, required=True, help="AI API Endpoint is required")
        parser.add_argument("--api-model-global-context", type=str, default="gpt-4o", help="AI API Model to support global Markdown context")
        parser.add_argument("--api-model-phase-context", type=str, default="gpt-4o", help="AI API Model to support phase Markdown context")
        parser.add_argument("--api-model-phase-max-days", type=int, default=5, help="Maximum days per phase")
        parser.add_argument("--api-model-phase-steps-json", type=str, default="gpt-4o", help="AI API Model to support phase steps JSON context")
        parser.add_argument("--api-model-phase-steps-json-mapping", type=str, default="", help="AI phase steps JSON ampping configuration")
        parser.add_argument("--api-model-phase-steps-days-per-chunk", type=int, default=5, help="Execution Days per AI Request Chunk")
        parser.add_argument("--exec-mode", type=int, default=0, help="AI Execution Mode: Global / Phase Context / Steps. Acceptable values: 0, 1, 2, 3")
        parser.add_argument("--exec-delay", type=int, default=3, help="AI Execution Delay in seconds")
        parser.add_argument("--language", type=str, default=DEFAULT_BLUEPRINT_LANGUAGE, help="Output blueprint under specific language")
        # use method `str2bool` to parse argument
        parser.add_argument("--exec-rotate-model", type=str2bool, default=False,  help="Specify whether should rotate models if exceeding rate limit")
    
    args, unknown_args = parse_args(
        description="🏗️ EnterpriseSystemArchitectureAgent",
        parser_callback=add_known_arguments
    )
    verbose = unknown_args.get("verbose", None) if unknown_args else False
    if verbose:
        enabledLogDebug(logger)
        enabledLogDebug(global_logger)
        enabledLogDebug(phase_logger)
        enabledLogDebug(steps_logger)
    
    # Trigger the primary agent orchestration function.
    run_architect_agent(
        args.project_name, args.req, args.phases, args.api_model_phase_max_days, args.out,
        args.api_key, args.api_endpoint,
        args.api_model_global_context, args.api_model_phase_context, args.api_model_phase_steps_json,
        args.api_model_phase_steps_json_mapping, args.exec_mode, args.exec_delay,
        args.api_model_phase_steps_days_per_chunk, args.language,
        args.exec_rotate_model
    )

