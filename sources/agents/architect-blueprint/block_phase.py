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
from sources.agents.agent_helper import resolve_absolute_path, exceptionStackTrace
from helper import write_log, write_file, render_prompt, parseOpenAIResponseData

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
PROMPT_TEMPLATE_PATH = resolve_absolute_path("sources/agents/architect-blueprint/block_phase_prompt.md")

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
    model_name_safe = model_name if model_name else "gpt-4o"
    try:
        for phase_idx in range(1, num_phases + 1):
            log_phase_idx = phase_idx
            print(f" │   ├── 📝 Compiling Context Markdown for Phase {phase_idx} of {num_phases}...")
            
            # parse prompt from template
            prompt_context = {
                "project_name": project_name,
                "phase_idx": phase_idx,
                "num_phases": num_phases,
                "global_markdown_context": global_context,
                "project_requirements": requirements,
                "max_days_per_phase": max_days_per_phase
            }
            prompt = render_prompt(PROMPT_TEMPLATE_PATH, prompt_context)
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
                model=model_name_safe,
                messages=[
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2
            )
            raw_data = parseOpenAIResponseData(response)
            
            # write context
            out_path = write_file(
                dir=os.path.join(out_dir, "plan", "context"),
                file_name=f"phase-{phase_idx}.context.blueprint.md",
                data=raw_data
            )
        
            # write log
            write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), raw_data.replace('#', '##') if raw_data else "-", False, model_name_safe, out_dir)
            
            print(f" │   ├── ✅ Saved Phase {phase_idx} MD: {out_path}")
            
            # sleep to avoid 429 Too Many Requests
            if phase_idx < num_phases + 1:
                print(f"⏳ Rate limit guard active... holding pipeline for { delay } seconds to clear AI TPM window...")
                time.sleep(delay)
            
        result = True if num_phases > 0 else False
        return result # success or empty phases
    except Exception as e:
        print(f"❌ Failed to initiate chat/generate Phase {log_phase_idx} Blueprint: {exceptionStackTrace(e)}")
        write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), exceptionStackTrace(e), False, model_name_safe, out_dir)
        return False

