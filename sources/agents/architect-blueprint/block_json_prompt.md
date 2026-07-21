Analyze the attached Phase {{ phase_idx }} Context Markdown content.
{# 🎯 CHECK LOGIC ĐIỀU KIỆN CHUNK TẠI ĐÂY #}
{% if is_chunked %}
Extract and translate ALL daily steps, checklists, and agent tasks starting from Day {{ current_start_day }} up to Day {{ current_end_day }} (inclusive).
{% else %}
Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.
{% endif %}

# CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to {max_days_per_phase} days maximum (Absolute Hard Limit: Maximum {max_days_per_phase} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day {max_days_per_phase}.
## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

# AGENT ATOMICITY CONSTRAINTS (CRITICAL FOR PRODUCTION):
## 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
## 2. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array:
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
## 3. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

# CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY:
{# 🎯 TIẾP TỤC DÙNG IF ELSE CHO PHẦN ĐỊNH HƯỚNG RANGE FOCUS #}
{% if is_chunked %}
## 1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day {{ current_start_day }} and Day {{ current_end_day }} (inclusive).
## 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [{{ current_start_day }} to {{ current_end_day }}].
{% else %}
## 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
## 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.
{% endif %}
## 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day.
## 4. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "{global_context_file}" into the 'global_context_file' field.
   - Populate the exact string "sources/" into the 'source_target_dir' field.
## 5. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field.
   - Provide the assigned role (e.g., 'Coder', 'Tester', 'Reviewer', 'DevOps') into the 'agent', 'subAgent', 'assignee' or 'subAgent' field.
## 6. Context Fields: For each day object, set 'day' as the integer value of that day, set 'context_file' to '{project_phase_context_file}', and set 'context_section' to 'DAY ' followed by the day number.

You MUST conform strictly to your required JSON Schema layout design structure:
{{ phase_steps_json_schema }}

--- PHASE {{ phase_idx }} CONTEXT MARKDOWN ---
{{ phase_markdown_content }}
------------------------------------------