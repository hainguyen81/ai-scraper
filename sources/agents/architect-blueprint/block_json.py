# BLOCK 3: CONVERTS PHASE MARKDOWN TO STEPS JSON

import os
import sys
import json
import time
import re

from pydantic import BaseModel, Field
from typing import List

# GEMINI
#from google import genai
#from google.genai import types

# OpenAI
from openai import OpenAI

# mapping JSON
from jinja2 import Template

# Now Python can seamlessly see and import the centralized helper utility cleanly!
from helper import write_log
from helper import parseOpenAIResponseJsonData

# --- Validated Schemas for Structured JSON Output ---
class SubAgentTask(BaseModel):
    id: str = Field(description="Sub-Task identity of Task that sub-agent role executing.")
    agent: str = Field(description="Target sub-agent role executing the task.")
    desc: str = Field(description="Literal, low-level technical step assigned to the agent.")

class DailyStep(BaseModel):
    day: int = Field(description="Timeline iteration day inside this isolated phase.")
    context_file: str = Field(description="The phase context Markdown file for closure on this day.")
    context_section: str = Field(description="The day targeted for closure on this day.")
    sub_tasks: List[SubAgentTask] = Field(description="Array of isolated micro-tasks assigned to sub-agents.")

class PhaseStepsPlan(BaseModel):
    phase_id: int = Field(description="Target phase tracker index.")
    phase_name: str = Field(description="Target phase tracker name.")
    project_name: str = Field(description="Target project tracker name.")
    global_context_file: str = Field(description="Project global context Markdown file for closure.")
    source_target_dir: str = Field(description="Project sources folder path for closure.")
    days: List[DailyStep] = Field(description="Day-by-day engineering tracking steps.")

def project_context_file(project_name: str):
    return f".ai/.context/{ project_name.lower() }.global.blueprint.md"

def phase_context_file(phase_idx: int):
    return f".ai/.plan/.context/phase-{ phase_idx }.context.blueprint.md"

def dynamic_transform(json_data, project_name: str, phase_idx: int, template_file_path: str, log_file_path: str):
    # check json mapping whether existed
    if not template_file_path or not os.path.exists(template_file_path):
        print(f" │   └── ⚠️ The mapping JSON file not found: {template_file_path}. So using manual transform...")
        return manual_transform(json_data, project_name, phase_idx)
    
    try:
        # 1. read mapping configuration
        with open(template_file_path, "r", encoding="utf-8") as f:
            template_content = f.read()
        
        # custom field mapping
        # print(f" │   └── ⚠️ The mapping JSON template: {template_content}")
        # print(f" │         { template_content }")
        json_data['project_name'] = project_name.lower()
        json_data['global_context_file'] = project_context_file(project_name)
        json_data['phase_idx'] = phase_idx
        json_data['phase_context_file'] = phase_context_file(phase_idx)
        
        # 2. Render template using Jinja2 with AI json data
        # wrap AI json data to variable `ai` in mapping config file to use
        jinja_template = Template(template_content)
        rendered_str = jinja_template.render(ai=json_data)
        # print(f" │   └── ⚠️ The mapping JSON Rendered String:")
        # print(f" │         { rendered_str }")
        
        # write log for tracing
        # if os.path.exists(log_file_path):
        #     with open(log_file_path, "a", encoding="utf-8") as f:
        #         f.write(f"# Project Name: { project_name } | Phase: { phase_idx }\n\n")
        #         f.write(f"## JSON:\n\n```json{ json.dumps(json_data) }```\n\n")
        #         f.write(f"## Mapped JSON:\n\n```json{ rendered_str }```\n\n")
        
        # 3. Clean up redundant comma (,) by Jinja in JSON Array
        # Process cases: [..., {obj}, ] hoặc [ , {obj} ]
        cleaned_str = re.sub(r',\s*\]', ']', rendered_str)
        cleaned_str = re.sub(r'\[\s*,', '[', cleaned_str)
        cleaned_str = re.sub(r',\s*\}', '}', cleaned_str)
        # print(f" │   └── ⚠️ The mapping JSON Cleaned String:")
        # print(f" │         { cleaned_str }")
        
        # write log for tracing
        # if os.path.exists(log_file_path):
        #     with open(log_file_path, "a", encoding="utf-8") as f:
        #         f.write(f"## Cleaned JSON:\n\n```json{ cleaned_str }```\n\n")
        
        # 4. Parse result JSON after rendering by Jinja
        return json.loads(cleaned_str)
    except json.JSONDecodeError as e:
        print(f" │   └── ❌ Exception while mapping JSON: { str(e) }. So using manual transform...")
        return manual_transform(json_data, project_name, phase_idx)

def manual_transform(json_data, project_name: str, phase_idx: int):
    transform_json_data = {
        "phase_id": phase_idx,
        "phase_name": json_data.get("phase", f"Phase {phase_idx}"),
        "project_name": project_name.lower(),
        "global_context_file": project_context_file(project_name),
        "source_target_dir": "sources/",
        "days": []
    }
    
    json_days = json_data.get("steps", json_data.get("dailyTasks", json_data.get("dayByDayPlan", [])))
    for item in json_days:
        day_val = item.get("day", 1)
        
        step_node = {
            "day": day_val,
            "context_section": f"DAY {day_val}",
            "context_file": phase_context_file(phase_idx),
            "sub_tasks": []
        }
        
        json_tasks = item.get("sub_agent_tasks", item.get("tasks", []))
        t_idx = 1
        for t in json_tasks:
            if isinstance(t, str):
                role = item.get("subAgent", item.get("assignee", "Coder"))
                desc = f"{ role } Agent: { t }"
            else:
                role = t.get("agent_role", t.get("assignee", "Coder"))
                desc = t.get("task_description", t.get("task", "No description provided"))
                desc = f"{ role } Agent: { desc }"
            
            step_node["sub_tasks"].append({
                "id": f"D{day_val}_ST{t_idx}",
                "agent": role,
                "desc": desc
            })
            t_idx = t_idx + 1
        transform_json_data["days"].append(step_node)
    
    # manual transform JSON data
    return transform_json_data

# GEMINI
# def convert_phases_to_json(client: genai.Client, project_name: str, num_phases: int, out_dir: str):

# OpenAI
def convert_phases_to_json(client: OpenAI, model_name: str, project_name: str, num_phases: int, json_mapping: str, out_dir: str):
    """
    BLOCK 3: Consumes the physical localized markdown outputs and structuralized them into strictly-typed JSON.
    Guarantees no invalid text pollution using Pydantic typing patterns.
    """
    print(f"⚙️  [BLOCK 3] Translating Phase Markdown files into Structured Daily Steps JSON trackers...")
    
    steps_context_dir = os.path.join(out_dir, "plan", "steps")
    os.makedirs(steps_context_dir, exist_ok=True)
    
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
                # max_tokens=8192,
            )
            raw_data, json_data = parseOpenAIResponseJsonData(response)
            # dump_json_data = json.dumps(json_data, indent=4, ensure_ascii=False) if json_data else "Invalid JSON Data"
            # print(f" │   └── 🎉 Response Phase {phase_idx} Standardized JSON:")
            # print(f" │         { dump_json_data }")
            
            # write blueprint
            out_path = os.path.join(steps_context_dir, f"phase-{phase_idx}.steps.json")
            fallback_path = os.path.join(steps_context_dir, f"phase-{phase_idx}.steps.error.md")
            transform_log_path = os.path.join(steps_context_dir, f"phase-{phase_idx}.steps.transformer.md")
            try:
                # transform mapping
                transform_json_data = dynamic_transform(json_data, project_name, phase_idx, json_mapping, transform_log_path)
                # dump_json_data = json.dumps(transform_json_data, indent=4, ensure_ascii=False) if transform_json_data else "Invalid JSON Data"
                # print(f" │   └── 🎉 Transform Phase {phase_idx} Standardized JSON:")
                # print(f" │         { dump_json_data }")
                
                # 2. Parse and validate the string payload locally with Pydantic core engine
                print(f" │   └── 🎉 Validate Phase {phase_idx} Standardized JSON...")
                validated_pydantic_object = PhaseStepsPlan.model_validate(transform_json_data)
                
                with open(out_path, "w", encoding="utf-8") as f:
                    json.dump(validated_pydantic_object.model_dump(), f, ensure_ascii=False, indent=4)
                    
                print(f" │   └── 🎉 Saved Phase {phase_idx} Standardized JSON Tracker: {out_path}")
                
            except Exception as pydantic_error:
                print(f" │   └── ❌ Local Validation Failed for Phase {phase_idx}: {pydantic_error}")
                
                # Save the raw unparsed text payload directly to file for manual logging evaluation
                with open(fallback_path, "w", encoding="utf-8") as f:
                    f.write(raw_data)
                    f.write("\n-------------------------------------------------\n")
                    f.write(json_data)
                    f.write("\n-------------------------------------------------\n")
                print(f" │   └── ⚠️ Raw dump saved to diagnostic log file: {fallback_path}")
            
            # write log
            write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), json_data, True)
            
            print(f" │   └── 🎉 Saved Phase {phase_idx} JSON Tracker: {out_path}")
            
            # sleep to avoid 429 Too Many Requests
            if phase_idx < num_phases + 1:
                print("⏳ Rate limit guard active... holding pipeline for 15 seconds to clear AI TPM window...")
                time.sleep(15)
                
        result = True if num_phases > 0 else False
        return result # success or empty phases
    except Exception as e:
        print(f"❌ Failed to initiate chat/generate Phase {log_phase_idx} Steps JSON: {str(e)}")
        write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), str(e), True)
        return False
