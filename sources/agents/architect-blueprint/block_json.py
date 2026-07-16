# BLOCK 3: CONVERTS PHASE MARKDOWN TO STEPS JSON

import os
import sys
import json
from pydantic import BaseModel, Field
from typing import List

# GEMINI
#from google import genai
#from google.genai import types

# OpenAI
from openai import OpenAI

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from helper import write_log
from helper import parseOpenAIResponseJsonData

# --- Validated Schemas for Structured JSON Output ---
class SubAgentTask(BaseModel):
    agent_role: str = Field(description="Target sub-agent role executing the task.")
    task_description: str = Field(description="Literal, low-level technical step assigned to the agent.")

class DailyStep(BaseModel):
    day: int = Field(description="Timeline iteration day inside this isolated phase.")
    focus: str = Field(description="The functional epic targeted for closure on this day.")
    sub_agent_tasks: List[SubAgentTask] = Field(description="Array of isolated micro-tasks assigned to sub-agents.")

class PhaseStepsPlan(BaseModel):
    phase_id: int = Field(description="Target phase tracker index.")
    phase_title: str = Field(description="Descriptive roadmap title matching the source Markdown.")
    steps: List[DailyStep] = Field(description="Day-by-day engineering tracking steps.")

# GEMINI
# def convert_phases_to_json(client: genai.Client, project_name: str, num_phases: int, out_dir: str):

# OpenAI
def convert_phases_to_json(client: OpenAI, model_name: str, project_name: str, num_phases: int, out_dir: str):
    """
    BLOCK 3: Consumes the physical localized markdown outputs and structuralized them into strictly-typed JSON.
    Guarantees no invalid text pollution using Pydantic typing patterns.
    """
    print(f"⚙️  [BLOCK 3] Translating Phase Markdown files into Structured Daily Steps JSON trackers...")
    
    log_phase_idx = 0
    log_prompt = ""
    instruction = "You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas."
    try:
        for phase_idx in range(1, num_phases + 1):
            log_phase_idx = phase_idx
            phase_context_dir = os.path.join(out_dir, "plan", "context")
            md_path = os.path.join(phase_context_dir, f"phase-{phase_idx}.context.blueprint.md")
            
            if not os.path.exists(md_path):
                print(f" │   └── ❌ Skipped Phase {phase_idx}: Source Markdown file not found.")
                continue
                
            with open(md_path, "r", encoding="utf-8") as f:
                phase_markdown_content = f.read()
                
            print(f" │   ├── 🔀 Parsing Phase {phase_idx} MD -> Compiling phase-{phase_idx}.steps.json...")
            
            prompt = f"""
            Analyze the attached Phase {phase_idx} Context Markdown content. 
            Translate every directive, objective, and daily task mentioned inside it into a structured day-by-day JSON map.
            
            --- PHASE {phase_idx} CONTEXT MARKDOWN ---
            {phase_markdown_content}
            ------------------------------------------

            Map your response strictly to the requested PhaseStepsPlan JSON structure.
            """
            log_prompt = prompt
            
            # GEMINI
            # response = client.models.generate_content(
            #     model='gemini-2.5-pro',
            #     contents=prompt,
            #     config=types.GenerateContentConfig(
            #         system_instruction=instruction,
            #         temperature=0.1,
            #         response_mime_type="application/json",
            #         response_schema=PhaseStepsPlan
            #     )
            # )
            # raw_data = response.text
            # json_data = json.loads(raw_data)
            
            # OpenAI
            response = client.beta.chat.completions.parse(
                model=model_name if model_name else "gpt-4o",  # Standard heavy reasoning model for structured enterprise operations
                messages=[
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                # response_format=PhaseStepsPlan, # Injects the pydantic model schema ruleset natively
            )
            raw_data, json_data = parseOpenAIResponseJsonData(response)
            
            # write blueprint
            try:
                # 2. Parse and validate the string payload locally with Pydantic core engine
                validated_pydantic_object = PhaseStepsPlan.model_validate_json(json_data)
                
                out_path = os.path.join(out_dir, f"phase-{phase_idx}.steps.json")
                with open(out_path, "w", encoding="utf-8") as f:
                    json.dump(validated_pydantic_object.model_dump(), f, ensure_ascii=False, indent=4)
                    
                print(f" │   └── 🎉 Saved Phase {phase_idx} Standardized JSON Tracker: {out_path}")
                
            except Exception as pydantic_error:
                print(f" │   └── ❌ Local Validation Failed for Phase {phase_idx}: {pydantic_error}")
                
                # Save the raw unparsed text payload directly to file for manual logging evaluation
                fallback_path = os.path.join(out_dir, f"phase-{phase_idx}.steps.error.txt")
                with open(fallback_path, "w", encoding="utf-8") as f:
                    f.write(raw_data)
                print(f" │   └── ⚠️ Raw dump saved to diagnostic log file: {fallback_path}")
            
            # write log
            write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), raw_data, True)
            
            print(f" │   └── 🎉 Saved Phase {phase_idx} JSON Tracker: {out_path}")
    except Exception as e:
        print(f"❌ Failed to initiate chat/generate Phase {log_phase_idx} Steps JSON: {e}")
        write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), str(e), True)
        sys.exit(1) # break pipeline
