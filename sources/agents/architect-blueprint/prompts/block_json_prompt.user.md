Analyze the attached Phase {{ phase_idx }} Context Markdown content.
{% if is_chunked %}
Extract and translate ALL daily steps, checklists, and agent tasks starting from Day {{ current_start_day }} up to Day {{ current_end_day }} (inclusive).
{% else %}
Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.
{% endif %}

# ⏳ CRITICAL CHUNK BOUNDARY ALIGNMENT RULE
# This rule applies ONLY if the chunk configuration is active (is_chunked is TRUE).
- **Boundary Execution Context:** When parsing tasks that span across boundary calendar days, you MUST exclusively extract and document the operational steps and sub-tasks that are actively executed within the requested window of Day {{ current_start_day }} to Day {{ current_end_day }}. Do not duplicate previous states or omit ongoing workflows.

# 🔒 AGENT ATOMICITY & COMPONENT MANDATES (ABSOLUTE):
- **ATOMIC AGENT ASSIGNMENT:** Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field: 'coder' | 'tester' | 'reviewer' | 'doc' | 'docker' | 'GCP' | 'GKE'.
- **NO ZERO-COMPONENT TASKS (ABSOLUTE HARD LIMIT):** You are STRICTLY BANNED from generating any sub-task object where the 'components' array is empty `[]`, null, or missing. If an Agent does not have any physical files or target paths to create, modify, test, or document on that specific day, you MUST NOT generate that sub-task object at all. No components means NO task. Every file path inside 'components' must be prefixed with `./sources/`.
- **FALLBACK COMPONENT RULE:** If a day has technical descriptions but lacks physical file paths, assign the task to "doc" agent and populate 'components' with exactly: `["./sources/{{ project_phase_context_file }}"]`.
- **STRICT AGENT ROLE SEGREGATION (ANTI-AGGREGATION):** If a workflow file involves multiple actions by different personas on the same calendar day, you MUST split this workflow into completely separate, sequential task objects inside the 'sub_tasks' array.
- **HIGH-DENSITY TECHNICAL SPECIFICATION:** The 'task' field MUST contain an exhaustive, granular engineering instruction. If the sub-task involves an API route, integration endpoint, database query, or message block, you MUST explicitly inline the complete technical contract (e.g., Request/Response Payload Schemas, Data Types, Error Status Codes, or Queue names) directly inside this string. Vague high-level bullet summaries are forbidden.
- **WORKSPACE PREFIX RULE & MULTI-LANGUAGE TEST EXCEPTION:** Every path in 'components' array MUST strictly begin with `./sources/`. 
  * *CRITICAL EXCEPTION:* If the first parameter before the semi-colon character in a tester task is the literal string token `INTEGRATION_SCOPE`, you MUST leave that token completely unmodified. Do NOT append any path prefix to it (e.g., `"components": ["INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts"]`).
- **STRICT LITERAL FIELD VALUES:** Populate exact string `./sources/{{ global_context_file }}` into 'global_context_file'. Populate exact empty string "" into 'source_target_dir' field.

## 7. Context Fields: For each day object, set 'day' to its calculated integer value, set 'context_file' to './sources/.../{{ project_phase_context_file }}', and set 'context_section' to 'DAY ' followed by the calculated day number.

## 8. CHRONOLOGICAL TIMELINE SEQUENCING MANDATE (ABSOLUTE):
- **Case A: If is_chunked is FALSE:** Regardless of the actual day numbers documented in the source Markdown content, you MUST reset the timeline sequence internally so that the first operational day inside this Phase always starts from integer 1. Map the first targeted day to `"day": 1`, set 'context_file' to `"./sources/{{ project_phase_context_file }}"`, and strictly set 'context_section' to `"DAY 1"`.
- **Case B: If is_chunked is TRUE:** You MUST PRESERVE the exact absolute chronological day index requested from the template parameters. The first parsed day object must match the integer value of {{ current_start_day }}, and progress incrementally up to {{ current_end_day }}. Map the absolute day index to the `"day"` field, set 'context_file' to `"./sources/{{ project_phase_context_file }}"`, and set 'context_section' to `"DAY "` followed exactly by that calculated absolute day number.

# 🛑 MANDATORY STRUCTURE ENFORCEMENT FOR TRACEABILITY TAGS (CRITICAL):
- When extracting sub-tasks, you MUST populate the exact inherited BA/SA Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) directly into the "targeted_tags" array field of EACH sub-task object node inside the JSON schema.
- Scan the source Markdown text, extract all corresponding Tag IDs for that sub-task, and populate them as clean individual string elements inside the "targeted_tags" array (e.g., `"targeted_tags": ["[REQ-001]", "[DAT-005]", "[EXC-002]"]`).
- You are STRICTLY BANNED from leaving the "targeted_tags" array empty `[]` or bundling tags into a single string (e.g., NO `["[REQ-001], [REQ-002]"]`). Every tag must be its own array element. If a task maps to a requirement, its tracking code array MUST be populated.

You must conform strictly to your required JSON Schema layout design structure:
{{ phase_steps_json_schema }}

--- PHASE {{ phase_idx }} CONTEXT MARKDOWN ---
{{ phase_markdown_content }}
------------------------------------------
