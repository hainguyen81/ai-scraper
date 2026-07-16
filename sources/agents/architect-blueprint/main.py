# ENTERPRISE MAIN ORCHESTRATOR RUNNER

import os
import sys
import argparse
from datetime import datetime

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

def run_architect_agent(project_name: str, requirements_path: str, num_phases: int, output_dir: str, api_key: str):
    """
    Master pipeline orchestrator that runs individual functional blocks in sequence.
    Provides pristine separation of concerns and protects engine runtime stability.
    """
    
    # GEMINI
    # client = genai.Client(api_key=api_key)
    
    # OpenAI
    client = OpenAI(api_key=api_key)
    
    absolute_requirements_path = resolve_absolute_path(requirements_path)
    if not os.path.exists(absolute_requirements_path):
        print(f"❌ Target requirements file not found at: {absolute_requirements_path}")
        return
        
    with open(absolute_requirements_path, "r", encoding="utf-8") as f:
        project_requirements = f.read()
        
    absolute_out_dir = resolve_absolute_path(output_dir)
    os.makedirs(absolute_out_dir, exist_ok=True)
    
    # 1. Execute Block 1 Module
    global_context_text = generate_global_context(
        client=client, 
        project_name=project_name, 
        requirements=project_requirements, 
        num_phases=num_phases, 
        out_dir=absolute_out_dir
    )
    
    # 2. Execute Block 2 Module
    generate_phase_contexts(
        client=client,
        project_name=project_name,
        requirements=project_requirements,
        global_context=global_context_text,
        num_phases=num_phases,
        out_dir=absolute_out_dir
    )
    
    # 3. Execute Block 3 Module
    convert_phases_to_json(
        client=client,
        project_name=project_name,
        num_phases=num_phases,
        out_dir=absolute_out_dir
    )
    
    print("\n🎉 [PIPELINE SUCCESS] Modular Enterprise Architecture Pipeline Executed Perfectly!")

if __name__ == "__main__":
    # Configure CLI arguments parsing to allow dynamic inputs for requirements path, phase count, and output location.
    datetimeStr = datetime.now().strftime("%Y%m%d%H%M%S")
    defaultPrjName = f"project-architecture-{datetimeStr}"
    parser = argparse.ArgumentParser(description="AI Solution / Lead Architect Agent Configuration")
    parser.add_argument("--project-name", type=str, default=defaultPrjName, help="Project name")
    parser.add_argument("--req", type=str, default="sources/requirements/test-requirements.md", help="Path to the raw project requirements file")
    parser.add_argument("--phases", type=int, default=3, help="Total number of execution phases to segment")
    parser.add_argument("--out", type=str, default="sources/output/blueprint", help="Target output directory for the generated blueprint")
    parser.add_argument("--api-key", type=str, required=True, help="Gemini API Key is required")
    
    args = parser.parse_args()
    
    # Trigger the primary agent orchestration function.
    run_architect_agent(args.project_name, args.req, args.phases, args.out, args.api_key)
