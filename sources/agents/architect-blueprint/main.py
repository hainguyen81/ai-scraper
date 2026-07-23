# ENTERPRISE MAIN ORCHESTRATOR RUNNER

import os
import sys
import json
import re
import argparse
from datetime import datetime
import time

# GEMINI
#from google import genai
#from google.genai import types

# OpenAI
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from sources.agents.agent_helper import resolve_absolute_path

# Import decoupled functional components cleanly
from block_global import generate_global_context
from block_phase import generate_phase_contexts
from block_json import convert_phases_to_json

# models list
MODELS_POOL_PATH = resolve_absolute_path("sources/agents/models/models.json")

def load_models_pool():
    # empty model
    if not os.path.exists(MODELS_POOL_PATH):
        return None
    
    # load models list from file
    with open(MODELS_POOL_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_models_keys():
    json_key_secrets = os.environ.get("AI_MODELS_KEYS_JSON")
    if not json_key_secrets:
        print("[ ⚠️ CRITICAL WARN ] The environment variable 'AI_MODELS_KEYS_JSON' is completely absent.")
        return None
    
    return json.loads(json_key_secrets)

def rotate_matching_model(json_ai_models, json_ai_keys, model_idx):
    models_len = len(json_ai_models) if json_ai_models else 0
    
    while model_idx < models_len and json_ai_keys and isinstance(json_ai_keys, dict):
        config = json_ai_models[model_idx]
        target_model_name = config.get("model_name") if isinstance(config, dict) else None
        target_model_endpoint = config.get("api_endpoint") if isinstance(config, dict) else None
        
        print("==============================================")
        print("🔍 DEBUG: 'config':")
        try:
            print(json.dumps(config, indent=4, ensure_ascii=False))
        except Exception:
            print(f"⚠️ Exception while dump 'config' json: {type(config)} - Config: {config}")
        print("==============================================")
        
        # If endpoint is missing, None, empty "", or just whitespaces "   ", skip it cleanly
        if not target_model_name or not target_model_endpoint or not str(target_model_endpoint).strip():
            print(f"⚠️ Ignore this config due to invalid 'model_name': {target_model_name} or 'model_endpoint': {target_model_endpoint}")
            model_idx += 1
            continue # 🔄 Immediately jumps to the next iteration of the while loop
        
        # Lookup the API Key inside the GitHub Secret JSON dictionary using the model_name from models.json
        api_key = json_ai_keys.get(target_model_endpoint)
        if api_key:
            print(f"[ 💀 FAILOVER ENGAGED ] Found AI model: {target_model_name} | endpoint: {target_model_endpoint}")
            return (model_idx, config, api_key)
        else:
            print(f"[ ⚠️ WARNING] API key missing inside GitHub JSON for model: {target_model_name} | endpoint: {target_model_endpoint}. Skipping tier.")
            model_idx += 1
    
    return (-1, None, None)

def run_architect_agent(
    project_name: str, requirements_path: str,
    num_phases: int, max_days_per_phase: int, output_dir: str,
    api_key: str, api_endpoint: str, api_model_global: str, api_model_phase: str, api_model_steps: str, api_model_steps_mapping: str,
    exec_mode: int, exec_delay: int, daysPerChunk: int,
    rotate_model: bool
):
    # check requirements
    absolute_requirements_path = resolve_absolute_path(requirements_path)
    if not os.path.exists(absolute_requirements_path):
        print(f"❌ Target requirements file not found at: {absolute_requirements_path}")
        return
    
    # read requirements
    with open(absolute_requirements_path, "r", encoding="utf-8") as f:
        project_requirements = f.read()
    
    # safely project name
    safe_name = project_name.replace(' ', '-')
    
    # make sure output directory existing
    absolute_out_dir = resolve_absolute_path(os.path.join(output_dir, safe_name))
    os.makedirs(absolute_out_dir, exist_ok=True)
    
    # resolve JSON mapping configuration file path
    absolute_api_model_steps_mapping = None
    if api_model_steps_mapping and os.path.exists(resolve_absolute_path(api_model_steps_mapping)):
        absolute_api_model_steps_mapping = resolve_absolute_path(api_model_steps_mapping)
    
    """
    Master pipeline orchestrator that runs individual functional blocks in sequence.
    Provides pristine separation of concerns and protects engine runtime stability.
    """
    
    json_ai_models = None
    json_ai_keys = None
    # need to rotate, so loading models / api keys configuration
    if rotate_model:
        json_ai_models = load_models_pool()
        json_ai_keys = load_models_keys()
    model_idx = -1
    models_len = len(json_ai_models) if json_ai_models else 0
    
    # whether should loop processes based on rotating AI models
    result_global = None
    result_phase = False if exec_mode in (0, 2) else True       # Phase should be ok if not running it
    result_steps = False if exec_mode in (0, 3) else True       # Steps should be ok if not running it
    everything_ok = False
    while not everything_ok and model_idx < models_len:
        # rotate to find matching AI models
        if model_idx >= 0:
            # not found any registered matching AI model
            rotate_idx, config, rotate_api_key = rotate_matching_model(json_ai_models, json_ai_keys, model_idx)
            if rotate_idx < 0 or not config or not rotate_api_key:
                print("[ 💀 CRITICAL SHUTDOWN ] Not found any more registered AI models with valid keys.")
                break
            
            # found registered matching AI model, but information is invalid
            model_idx = rotate_idx
            api_model_global = config.get("model_name") if isinstance(config, dict) else None
            api_model_phase = api_model_global
            api_model_steps = api_model_global
            api_endpoint = config.get("api_endpoint") if isinstance(config, dict) else None
            api_key = rotate_api_key
            if not api_model_global or not api_endpoint or not api_key:
                print("[ 💀 CRITICAL SHUTDOWN ] Invalid registered AI models. Missing Endpoint, Model or API Key.")
                break
        
        # first time
        else:
            api_model_phase = api_model_phase if api_model_phase else api_model_global
            api_model_steps = api_model_steps if api_model_steps else api_model_phase
            api_model_steps = api_model_steps if api_model_steps else api_model_global
        
        # GEMINI
        # client = genai.Client(api_key=api_key)
        
        # OpenAI
        client = OpenAI(
            base_url=api_endpoint,
            api_key=api_key,
            # 0 to turn off retries
            max_retries=3, 
            # timeout in seconds (600 seconds ~ 10 minutes)
            timeout=600.0
        )
        
        max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
        exec_mode = exec_mode if exec_mode >= 0 and exec_mode <= 3 else 0
        exec_delay = exec_delay if exec_delay else 3
        print("=============================================================================")
        print(f"🤖 AI: Endpoint {api_endpoint}. Mode '0' for all.")
        print(f"    - Global Context:               {api_model_global}. Mode 1")
        print(f"    - Phase Context:                {api_model_phase}.  Mode 2")
        print(f"    - Phase JSON Steps:             {api_model_steps}.  Mode 3")
        print(f"    - Phase JSON Steps Mapping:     {api_model_steps_mapping}")
        print(f"    - Execution Mode:               {exec_mode}")
        print(f"    - Execution Delay:              {exec_delay}")
        print("=============================================================================")
        print(f"    - ROTATE MODEL INTEGRATION:     {model_idx}")
        print("=============================================================================")
        
        # -------------------------------------------------
        # 1. Execute Block 1 Module
        # -------------------------------------------------
        if exec_mode in (0, 1) and not result_global:
            result_global = generate_global_context(
                client=client,
                model_name=api_model_global,
                project_name=project_name,
                requirements=project_requirements,
                num_phases=num_phases,
                max_days_per_phase=max_days_per_phase,
                out_dir=absolute_out_dir
            )
            
            # sleep to avoid 429 Too Many Requests
            if result_global:
                print(f"⏳ Rate limit guard active... holding pipeline for { exec_delay } seconds to clear AI TPM window...")
                time.sleep(exec_delay)
        
        # no need AI, just reading from existing context file
        elif not result_global:
            context_dir = os.path.join(absolute_out_dir, "context")
            global_context_file = os.path.join(context_dir, f"{safe_name}.global.blueprint.md")
            with open(global_context_file, "r", encoding="utf-8") as f:
                result_global = f.read()
        
        # if failed, check whether should rotate model
        if not result_global:
            print("\n[ 🤖💬 PIPELINE WARN ] Modular Enterprise Architecture Pipeline Executed: Fail to generate project global context!")
            
            # should rotate to find other models
            if rotate_model:
                model_idx += 1
                continue
            
            # out of function if not rotating
            break
        
        # -------------------------------------------------
        # 2. Execute Block 2 Module
        # -------------------------------------------------
        if exec_mode in (0, 2) and not result_phase:
            global_context_text = result_global
            result_phase = generate_phase_contexts(
                client=client,
                model_name=api_model_phase,
                project_name=project_name,
                requirements=project_requirements,
                global_context=global_context_text,
                num_phases=num_phases,
                max_days_per_phase=max_days_per_phase,
                out_dir=absolute_out_dir,
                delay=exec_delay
            )
            
            # sleep to avoid 429 Too Many Requests
            if result_phase:
                print("⏳ Rate limit guard active... holding pipeline for 15 seconds to clear AI TPM window...")
                time.sleep(5)
            
            else:
                print("\n[ 🤖💬 PIPELINE WARN ] Modular Enterprise Architecture Pipeline Executed: Fail to generate project phase contexts!")
                
                # should rotate to find other models
                if rotate_model:
                    model_idx += 1
                    continue
                
                # out of function if not rotating
                break
        
        # -------------------------------------------------
        # 3. Execute Block 3 Module
        # -------------------------------------------------
        if exec_mode in (0, 3) and not result_steps:
            result_steps = convert_phases_to_json(
                client=client,
                model_name=api_model_steps,
                project_name=project_name,
                num_phases=num_phases,
                max_days_per_phase=max_days_per_phase,
                json_mapping=absolute_api_model_steps_mapping,
                out_dir=absolute_out_dir,
                delay=exec_delay,
                daysPerChunk=daysPerChunk
            )
            if not result_steps:
                print("\n[ 🤖💬 PIPELINE WARN ] Modular Enterprise Architecture Pipeline Executed: Fail to generate project phase JSON steps!")
                
                # should rotate to find other models
                if rotate_model:
                    model_idx += 1
                    continue
                
                # out of function if not rotating
                break
        
        # check everything whether is ok
        everything_ok = result_global and result_phase and result_steps
    
    # log for tracing
    if not everything_ok:
        print(f"\n❌ [ PIPELINE FAILED ] Modular Enterprise Architecture Pipeline Executed Failed: Global?. { True if result_global else False } - Phase { result_phase } - Steps { result_steps }")
    
    # everything is ok
    else:
        print("\n🎉 [ PIPELINE SUCCESS ] Modular Enterprise Architecture Pipeline Executed Perfectly!")
    
    # result should be good for all
    return result_global and result_phase and result_steps

def str2bool(v):
    return str(v).lower() in ("yes", "true", "t", "1")

if __name__ == "__main__":
    # Configure CLI arguments parsing to allow dynamic inputs for requirements path, phase count, and output location.
    datetimeStr = datetime.now().strftime("%Y%m%d%H%M%S")
    defaultPrjName = f"project-architecture-{datetimeStr}"
    parser = argparse.ArgumentParser(description="AI Solution / Lead Architect Agent Configuration")
    parser.add_argument("--project-name", type=str, default=defaultPrjName, help="Project name")
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
    # use method `str2bool` to parse argument
    parser.add_argument("--exec-rotate-model", type=str2bool, default=False,  help="Specify whether should rotate models if exceeding rate limit")
    
    args = parser.parse_args()
    
    # Trigger the primary agent orchestration function.
    run_architect_agent(
        args.project_name, args.req, args.phases, args.api_model_phase_max_days, args.out,
        args.api_key, args.api_endpoint,
        args.api_model_global_context, args.api_model_phase_context, args.api_model_phase_steps_json,
        args.api_model_phase_steps_json_mapping, args.exec_mode, args.exec_delay,
        args.api_model_phase_steps_days_per_chunk,
        args.exec_rotate_model
    )

