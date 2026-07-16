# BLOCK 2: GENERATES PHASE MARKDOWN

import os

# GEMINI
# from google import genai
# from google.genai import types

# OpenAI
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from helper import write_log
from helper import parseOpenAIResponseData

# GEMINI
# def generate_phase_contexts(client: genai.Client, project_name: str, requirements: str, global_context: str, num_phases: int, out_dir: str):

# OpenAI
def generate_phase_contexts(client: OpenAI, project_name: str, requirements: str, global_context: str, num_phases: int, out_dir: str):
    """
    BLOCK 2: Decomposes requirements into segmented, sandbox-ready development boundaries.
    Executes raw isolated stateless calls per loop item to bypass sequence length degradation.
    """
    print(f"🔄 [BLOCK 2] Decomposing requirements into {num_phases} isolated Phase Markdowns...")
    
    log_phase_idx = 0
    log_prompt = ""
    try:
        instruction = "You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap."
        
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
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2
            )
            raw_data = parseOpenAIResponseData(response)
            
            context_dir = os.path.join(out_dir, "plan", "context")
            os.makedirs(context_dir, exist_ok=True)
            out_path = os.path.join(context_dir, f"phase-{phase_idx}.context.blueprint.md")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(raw_data)
        
            # write log
            write_log(log_phase_idx, log_prompt.replace('#', '##'), raw_data.replace('#', '##') if raw_data else "-", False)
            
            print(f" │   ├── ✅ Saved Phase {phase_idx} MD: {out_path}")
    except Exception as e:
        print(f"❌ Failed to initiate chat/generate Phase {log_phase_idx} Blueprint: {e}")
        write_log(log_phase_idx, log_prompt.replace('#', '##'), str(e), False)
        sys.exit(1) # break pipeline

