# BLOCK 1: GENERATES GLOBAL CONTEXT

import os
import sys

# GEMINI
# from google import genai
# from google.genai import types

# OpenAI
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from helper import write_log
from helper import write_file
from helper import parseOpenAIResponseData

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
        prompt = f"""
        Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for '{project_name}'.
        
        --- RAW REQUIREMENTS ---
        {requirements}
        --- END REQUIREMENTS ---
            
        # CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
        ## 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to {max_days_per_phase} days maximum (Absolute Hard Limit: Maximum {max_days_per_phase} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day {max_days_per_phase}.
        ## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

        Your output MUST follow this exact structure:
        # GLOBAL PROJECT CONTEXT: {project_name}
        ## 1. Executive Summary & Tech Stack Blueprint
        ## 2. Global Guardrails & Enterprise Compliance Standards
        ## 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
        ## 4. Multi-Phase Segmentation Strategy Overview (Plan exactly {num_phases} phases)
        """
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
        write_file(
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

