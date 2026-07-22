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
from sources.agents.agent_helper import resolve_absolute_path
from helper import write_log
from helper import write_json_file
from helper import render_prompt
from helper import parseOpenAIResponseJsonData

# ==============================================================================
# GLOBAL CONFIGURATION PATHS - CONFIG HERE TO CUSTOMIZE DIRECTORY STRUCTURE
# ==============================================================================
PROMPT_TEMPLATE_PATH = resolve_absolute_path("sources/agents/architect-blueprint/block_json_prompt.md")

# --- Validated Schemas for Structured JSON Output ---
class SubAgentTask(BaseModel):
    id: str = Field(description="Sub-Task identity of Task that sub-agent role executing.")
    agent: str = Field(description="Target sub-agent role executing the task.")
    desc: str = Field(description="Literal, low-level technical step assigned to the agent.")
    
    # 🎯 FLAT STRING ARRAY - DEFAULTS TO EMPTY []
    # list of source file paths that sub-agent should do
    components: List[str] = Field(
        default_factory=list,  # or default=[]
        description="Flat array of physical localized file paths or scripts modified or targeted by this single task. Return an empty array [] if no files are involved."
    )

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
        # custom field mapping
        # print(f" │   └── ⚠️ The mapping JSON template: {template_content}")
        # print(f" │         { template_content }")
        json_data['project_name'] = project_name.lower()
        json_data['global_context_file'] = project_context_file(project_name)
        json_data['phase_idx'] = phase_idx
        json_data['phase_context_file'] = phase_context_file(phase_idx)
        
        # 1. read mapping configuration
        with open(template_file_path, "r", encoding="utf-8") as f:
            template_content = f.read()
        
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
    
    json_days = json_data.get("days", json_data.get("steps", json_data.get("dailyTasks", json_data.get("dayByDayPlan", []))))
    for item in json_days:
        day_val = item.get("day", 1)
        
        step_node = {
            "day": day_val,
            "context_section": f"DAY {day_val}",
            "context_file": phase_context_file(phase_idx),
            "sub_tasks": []
        }
        
        json_tasks = item.get("sub_tasks", item.get("sub_agent_tasks", item.get("tasks", [])))
        t_idx = 1
        for t in json_tasks:
            if isinstance(t, str):
                role = item.get("agent", item.get("subAgent", item.get("assignee", "Coder")))
                desc = f"{ role } Agent: { t }"
            else:
                role = t.get("agent", t.get("agent_role", t.get("assignee", "Coder")))
                desc = t.get("task_description", t.get("task", "No description provided"))
                desc = f"{ role } Agent: { desc }"
            
            step_node["sub_tasks"].append({
                "id": f"D{day_val}_ST{t_idx}",
                "agent": role,
                "desc": desc,
                "components": t.get("components", t.get("files", t.get("targets", [])))
            })
            t_idx = t_idx + 1
        transform_json_data["days"].append(step_node)
    
    # manual transform JSON data
    return transform_json_data

# GEMINI
# def convert_phases_to_json(client: genai.Client, project_name: str, num_phases: int, out_dir: str):

# OpenAI
def convert_phases_to_json(client: OpenAI, model_name: str, project_name: str, num_phases: int, max_days_per_phase: int, json_mapping: str, out_dir: str, delay: int, daysPerChunk: int):
    """
    BLOCK 3: Consumes the physical localized markdown outputs and structuralized them into strictly-typed JSON.
    Guarantees no invalid text pollution using Pydantic typing patterns.
    """
    print(f"⚙️  [BLOCK 3] Translating Phase Markdown files into Structured Daily Steps JSON trackers...")
    
    steps_context_dir = os.path.join(out_dir, "plan", "steps")
    os.makedirs(steps_context_dir, exist_ok=True)
    
    delay = delay if delay else 3
    max_days_per_phase = max_days_per_phase if max_days_per_phase > 0 else 7
    log_phase_idx = 0
    log_prompt = ""
    instruction = "You are a rigid technical translator. Map high-level Markdown workflows into precise, executable JSON schemas."
    
    # 🎯 CONFIG: Define safe day span bounds per API transaction window
    DAYS_PER_CHUNK = daysPerChunk if daysPerChunk and daysPerChunk > 0 else 0
    
    # 🎯 SCHEMA INJECTION: Dump expected structure configuration for the prompt injector
    json_schema_dump = json.dumps(PhaseStepsPlan.model_json_schema(), indent=2)
    global_context_file = project_context_file(project_name)
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
            
            # 🎯 CHUNKING MEMORY STORAGE: Initialize temporary dictionary repository to hold aggregated elements
            project_phase_context_file = phase_context_file(phase_idx)
            master_phase_plan = {
                "phase_id": phase_idx,
                "phase_name": f"Phase {phase_idx}",
                "project_name": project_name.lower(),
                "global_context_file": global_context_file,
                "source_target_dir": "sources/",
                "objectives": [],
                "days": [] # Matches your dynamic transform's expected source property fields
            }
            
            current_start_day = 1
            has_more_days = True
            chunk_counter = 1
            
            # # Combined text accumulators for the ultimate logging layers
            # accumulated_raw_data = ""
            # accumulated_json_text = ""
            
            # 🎯 CORE SLIDING TIMELINE SCROLL LOOP
            while has_more_days:
                current_end_day = current_start_day + DAYS_PER_CHUNK - 1
                if DAYS_PER_CHUNK > 0:
                    print(f" │       ├── 📦 Chunk {chunk_counter}: Extracting Days {current_start_day} to {current_end_day}...")
                else:
                    print(f" │       ├── 📦 Chunk {chunk_counter}: Extracting All Days...")
                
                # parse prompt from template
                is_chunked_mode = True if DAYS_PER_CHUNK > 0 else False
                prompt_context = {
                    "is_chunked": is_chunked_mode,
                    "project_name": project_name,
                    "phase_idx": phase_idx,
                    "current_start_day": current_start_day,
                    "current_end_day": current_end_day,
                    "max_days_per_phase": max_days_per_phase,
                    "phase_steps_json_schema": json_schema_dump,
                    "phase_markdown_content": phase_markdown_content,
                    "global_context_file": global_context_file,
                    "project_phase_context_file": project_phase_context_file
                }
                prompt = render_prompt(PROMPT_TEMPLATE_PATH, prompt_context)
                log_prompt = prompt  # Stores the latest prompt state for error block fallback capture
                
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
                    max_completion_tokens=4096,
                    # # 💡 Turn OFF thinking feature of Qwen on Groq
                    # extra_body={
                    #     "reasoning_format": "hidden"
                    # },
                )
                
                # if response is ok, parse json
                raw_data, json_data = parseOpenAIResponseJsonData(response)
                # dump_json_data = json.dumps(json_data, indent=4, ensure_ascii=False) if json_data else "Invalid JSON Data"
                # print(f" │   └── 🎉 Response Phase {phase_idx} Standardized JSON:")
                # print(f" │         { dump_json_data }")
                
                # write log
                write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), raw_data, True)
                
                # # Accumulate stream markers for audit logging preservation
                # accumulated_raw_data += f"\n--- CHUNK {chunk_counter} RAW ---\n" + (raw_data if raw_data else "")
                # if json_data:
                #     accumulated_json_text += f"\n--- CHUNK {chunk_counter} JSON ---\n" + json.dumps(json_data, indent=2)
                # print(f" │       └── ⚠️ Chunk {chunk_counter}:")
                # print(f" │             {accumulated_raw_data}")
                # print(f" │             {accumulated_json_text}")
                
                # Guard against corrupted extractions
                if not json_data or not isinstance(json_data, dict):
                    print(f" │       └── ⚠️ Chunk {chunk_counter} failed to yield clean data object. Halting scroll vector.")
                    has_more_days = False
                    break
                
                # Extract target task collections using flexible property matching vectors
                chunk_steps_array = json_data.get("days", json_data.get("steps", json_data.get("dailyTasks", json_data.get("dayByDayPlan", []))))
                
                # Termination trigger: If array is missing or empty, the entire markdown blueprint context has been fully scanned
                if not chunk_steps_array:
                    print(f" │       └── 🏁 Reached timeline boundary. No data mapped for Day {current_start_day}+.")
                    has_more_days = False
                    break
                
                # ✅ MASTER MERGE: Merge chunk results into Python's memory repository tracker
                new_days_added_in_this_chunk = 0
                for day_node in chunk_steps_array:
                    day_num = day_node.get("day", 0)
                    if DAYS_PER_CHUNK == 0 or current_start_day <= day_num <= current_end_day:
                        # Auto-inject string metadata if AI fills them with blank placeholders during chunking
                        if not day_node.get("context_file"):
                            day_node["context_file"] = f"{project_phase_context_file}"
                        if not day_node.get("context_section"):
                            day_node["context_section"] = f"## Day {day_num}"
                        master_phase_plan["days"].append(day_node)
                        new_days_added_in_this_chunk += 1
                
                # Incremental shift parameters mapping to the next chronological segment index
                if DAYS_PER_CHUNK == 0:
                    print(f" │       └── 🎉 Monolithic processing complete. Total days extracted: {new_days_added_in_this_chunk}. Halting.")
                    has_more_days = False
                    break
                else:
                    # not found any days
                    if new_days_added_in_this_chunk == 0:
                        print(f" │       └── 🏁 No new valid days matched the current span [{current_start_day}-{current_end_day}]. Ending scroll vector.")
                        break
                    
                    # loop chunk
                    current_start_day += DAYS_PER_CHUNK
                    chunk_counter += 1
                    
                    # Short internal sleep interval protecting free engine limits from burst failures
                    time.sleep(1)
            
            # --- END OF CHUNK SCROLL LOOP ---
            # dump_json_data = json.dumps(master_phase_plan, indent=4, ensure_ascii=False)
            # print(f" │   └── 🎉 Master Phase Plan:")
            # print(f"           { dump_json_data }")
                
            # write blueprint
            fallback_path = os.path.join(steps_context_dir, f"phase-{phase_idx}.steps.error.md")
            transform_log_path = os.path.join(steps_context_dir, f"phase-{phase_idx}.steps.transformer.md")
            try:
                # transform mapping
                transform_json_data = dynamic_transform(master_phase_plan, project_name, phase_idx, json_mapping, transform_log_path)
                # dump_json_data = json.dumps(transform_json_data, indent=4, ensure_ascii=False) if transform_json_data else "Invalid JSON Data"
                # print(f" │   └── 🎉 Transform Phase {phase_idx} Standardized JSON:")
                # print(f" │         { dump_json_data }")
                
                # 2. Parse and validate the string payload locally with Pydantic core engine
                print(f" │   └── 🎉 Validate Phase {phase_idx} Standardized JSON...")
                validated_pydantic_object = PhaseStepsPlan.model_validate(transform_json_data)
                model_dump = validated_pydantic_object.model_dump()
                # dump_json_data = json.dumps(model_dump, indent=4, ensure_ascii=False)
                # rint(f" │         { dump_json_data }")
                
            
                # write steps
                out_path = write_json_file(
                    dir=steps_context_dir,
                    file_name=f"phase-{phase_idx}.steps.json",
                    json_data=model_dump
                )
                    
                print(f" │   └── 🎉 Saved Phase {phase_idx} Standardized JSON Tracker: {out_path}")
                
            except Exception as pydantic_error:
                print(f" │   └── ❌ Local Validation Failed for Phase {phase_idx}: {pydantic_error}")
                
                # Save the raw unparsed text payload directly to file for manual logging evaluation
                with open(fallback_path, "w", encoding="utf-8") as f:
                    f.write(raw_data)
                    f.write("\n-------------------------------------------------\n")
                    f.write(json.dumps(master_phase_plan, indent=4, ensure_ascii=False))
                    f.write("\n-------------------------------------------------\n")
                print(f" │   └── ⚠️ Raw dump saved to diagnostic log file: {fallback_path}")
            
            # sleep to avoid 429 Too Many Requests
            if phase_idx < num_phases + 1:
                print(f"⏳ Rate limit guard active... holding pipeline for { delay } seconds to clear AI TPM window...")
                time.sleep(delay)
                
        result = True if num_phases > 0 else False
        return result # success or empty phases
    except Exception as e:
        print(f"❌ Failed to initiate chat/generate Phase {log_phase_idx} Steps JSON: {str(e)}")
        write_log(log_phase_idx, instruction, log_prompt.replace('#', '##'), str(e), True)
        return False
