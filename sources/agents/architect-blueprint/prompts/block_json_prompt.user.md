Analyze the attached Phase {{ phase_idx }} Context Markdown content.
{% if is_chunked %}
Extract and translate ALL daily steps, checklists, and agent tasks starting from Day {{ current_start_day }} up to Day {{ current_end_day }} (inclusive).
{% else %}
Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.
{% endif %}

# 🔒 AGENT ATOMICITY, TASK ID FORMAT & COMPONENT MANDATES (ABSOLUTE):
- **STRICT TASK ID ALIGNMENT BLUEPRINT:** You MUST strictly generate the "id" field string for every single sub-task using the exact sequential formatting blueprint: `D<day_num>_ST<task_index>` (e.g., `D1_ST1`, `D1_ST2`, `D2_ST1`).
- **STRICT AGENT ROLE LITERAL VALUES:** The "agent" field inside the JSON sub-task object MUST strictly enforce a capitalized first letter and lowercase subsequent letters pattern matching the exact tokens: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'Gcp' | 'Gke'. Any other values or lowercase blocks (e.g., NO "coder") are strictly banned.
- **NO ZERO-COMPONENT TASKS (ABSOLUTE HARD LIMIT):** You are STRICTLY BANNED from generating any sub-task object where the 'components' array is empty `[]`, null, or missing. If an Agent does not have any physical file paths to create, modify, or document, you MUST NOT generate that sub-task object node.
- **FALLBACK COMPONENT RULE:** If a day has technical descriptions but lacks physical file paths, assign the task to "Doc" agent and populate 'components' with exactly the value of: "{{ project_phase_context_file }}".
- **STRICT AGENT ROLE SEGREGATION (ANTI-AGGREGATION):** If a workflow file involves multiple actions by different personas on the same calendar day, you MUST split this workflow into completely separate, sequential task objects inside the 'sub_tasks' array.
- **HIGH-DENSITY TECHNICAL SPECIFICATION:** The 'task' field MUST contain an exhaustive, granular engineering instruction. If the sub-task involves an API route, integration endpoint, database query, or message block, you MUST explicitly inline the complete technical contract (e.g., Request/Response Payload Schemas, Data Types, Error Status Codes, or Queue names) directly inside this string. Vague high-level bullet summaries are forbidden.
- **WORKSPACE PREFIX RULE & MULTI-LANGUAGE TEST EXCEPTION:** Every path in 'components' array MUST strictly begin with `./sources/`. 
  * *CRITICAL EXCEPTION:* If the first parameter before the semi-colon character in a tester task is the literal string token `INTEGRATION_SCOPE`, you MUST leave that token completely unmodified. Do NOT append any path prefix to it (e.g., `"components": ["INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts"]`).

# 🛠️ MANDATORY TOP-LEVEL FIELD VALUES INJECTION (STRICT FIDELITY):
You MUST dynamically populate the top-level keys of the JSON object using EXACT raw variable values without any folder modifications, structural padding, or text injections:
- **`phase_id`**: {{ phase_idx }}
- **`phase_name`**: [Extract the exact phase name string from the source Markdown context header text]
- **`project_name`**: "{{ project_name }}"
- **`global_context_file`**: "{{ global_context_file }}"
- **`source_target_dir`**: "{{ source_target_dir }}"

## 7. Context Fields Integration Mandate
- For each day object inside the array, set 'day' to its calculated integer value, set 'context_file' to exact string "{{ project_phase_context_file }}", and **set 'context_section' to the exact raw string value of the entire primary Day Header extracted from the source Markdown context text** (e.g., `"context_section": "DAY 1: Multi-Tenant Inception Schema & Flyway Migration Setup"`).

## 8. CHRONOLOGICAL TIMELINE SEQUENCING MANDATE (ABSOLUTE):
{% if is_chunked %}
# SYSTEM CRITICAL BOUNDARY: CHUNKED CONFIGURATION IS ACTIVE (is_chunked is TRUE)
- You MUST PRESERVE the exact absolute chronological day index requested from the template parameters. 
- The first parsed day object inside the 'days' array MUST match the exact integer value of {{ current_start_day }}, and progress incrementally up to {{ current_end_day }}. 
- You are STRICTLY BANNED from resetting the day value to 1. Map the absolute day index directly to the "day" field, set 'context_file' to "{{ project_phase_context_file }}", and set 'context_section' to the exact raw primary day header line corresponding to that absolute day index from the source markdown.
{% else %}
# SYSTEM CRITICAL BOUNDARY: FLAT CONFIGURATION IS ACTIVE (is_chunked is FALSE)
- Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "DAY 4", "DAY 5"), you MUST completely reset the timeline sequence internally so that the first operational day inside this Phase always starts from integer 1. Progression follows sequentially as 2, 3, 4, etc. 
- Map the first targeted day to `"day": 1`, set 'context_file' to "{{ project_phase_context_file }}", and strictly set 'context_section' to the exact raw primary header line of the first day parsed from the text. Incremental days follow this relative baseline.
{% endif %}

# 🛑 MANDATORY STRUCTURE ENFORCEMENT FOR TRACEABILITY TAGS (CRITICAL):
- Scan the source Markdown text, extract all corresponding inline Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, etc.) for each sub-task, and populate them as clean individual string elements inside the "targeted_tags" array field (e.g., `"targeted_tags": ["[REQ-001]", "[DAT-005]"]`).
- You are STRICTLY BANNED from leaving the "targeted_tags" array empty `[]` or bundling tags into a single string. Every tag must be its own array element.

You must conform strictly to your required JSON Schema layout design structure:
{{ phase_steps_json_schema }}

--- PHASE {{ phase_idx }} CONTEXT MARKDOWN ---
{{ phase_markdown_content }}
------------------------------------------
