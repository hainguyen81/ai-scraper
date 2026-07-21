# BLOCK 2: GENERATES PHASE MARKDOWN

import os
import sys
import time

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
# def generate_phase_contexts(client: genai.Client, project_name: str, requirements: str, global_context: str, num_phases: int, out_dir: str):

# OpenAI
def generate_phase_contexts(client: OpenAI, model_name: str, project_name: str, requirements: str, global_context: str, num_phases: int, max_days_per_phase: int, out_dir: str, delay: int):
    """
    BLOCK 2: Decomposes requirements into segmented, sandbox-ready development boundaries.
    Executes raw isolated stateless calls per loop item to bypass sequence length degradation.
    """
    print(f"🔄 [BLOCK 2] Decomposing requirements into {num_phases} isolated Phase Markdowns...")
    
    delay = delay if delay else 3
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    log_phase_idx = 0
    log_prompt = ""
    instruction = "You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap."
    try:
        for phase_idx in range(1, num_phases + 1):
            log_phase_idx = phase_idx
            print(f" │   ├── 📝 Compiling Context Markdown for Phase {phase_idx} of {num_phases}...")
            
            prompt = f"""
            Project Name: {project_name}
            You are tasked to detail **PHASE {phase_idx} OUT OF {num_phases}**.
            You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

            --- GLOBAL CONTEXT REFERENCE ---
            {global_context}
            
            --- RAW REQUIREMENTS REFERENCE ---
            {requirements}
            ----------------------------------
            
            # CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
            ## 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to {max_days_per_phase} days maximum (Absolute Hard Limit: Maximum {max_days_per_phase} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day {max_days_per_phase}.
            ## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

            Your output MUST follow this exact Markdown structure for Phase {phase_idx}:
            # PHASE {phase_idx} CONTEXT BLUEPRINT: {project_name}
            ## 1. Phase Operational Scope & Objectives
            ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
            ## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
            ## 4. Phase Definition of Done (DoD)
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
            write_file(
                dir=os.path.join(out_dir, "plan", "context"),
                file_name=f"phase-{phase_idx}.context.blueprint.md",
                data=raw_data
            )
        
            # write log
            write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), raw_data.replace('#', '##') if raw_data else "-", False)
            
            print(f" │   ├── ✅ Saved Phase {phase_idx} MD: {out_path}")
            
            # sleep to avoid 429 Too Many Requests
            if phase_idx < num_phases + 1:
                print(f"⏳ Rate limit guard active... holding pipeline for { delay } seconds to clear AI TPM window...")
                time.sleep(delay)
            
        result = True if num_phases > 0 else False
        return result # success or empty phases
    except Exception as e:
        print(f"❌ Failed to initiate chat/generate Phase {log_phase_idx} Blueprint: {e}")
        write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), str(e), False)
        return False

