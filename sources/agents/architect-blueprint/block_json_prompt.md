Analyze the attached Phase {{ phase_idx }} Context Markdown content.
{% if is_chunked %}
Extract and translate ALL daily steps, checklists, and agent tasks starting from Day {{ current_start_day }} up to Day {{ current_end_day }} (inclusive).
{% else %}
Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.
{% endif %}

# ⏳ CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT: Individual Phase MUST be bounded between 1 to {{ max_days_per_phase }} days maximum. Never generate scheduling logs beyond Day {{ max_days_per_phase }}.
## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core objectives are satisfied. Do NOT duplicate or loop previous task structures. Freeze output and exit.

# 🔒 AGENT ATOMICITY & COMPONENT MANDATES (ABSOLUTE):
- **ATOMIC AGENT ASSIGNMENT:** Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
- **NO ZERO-COMPONENT TASKS (ABSOLUTE HARD LIMIT):** You are STRICTLY BANNED from generating any sub-task object where the 'components' array is empty `[]`, null, or missing. If an Agent does not have any physical files or target paths to create, modify, test, or document on that specific day, you MUST NOT generate that sub-task object at all. No components means NO task. Every file path inside 'components' must be prefixed with `./sources/`.
- **FALLBACK COMPONENT RULE:** If a day has technical descriptions but lacks physical file paths, assign the task to "doc" agent and populate 'components' with exactly: `["./sources/{{ project_phase_context_file }}"]`.
- **STRICT AGENT ROLE SEGREGATION (ANTI-AGGREGATION):** If a workflow file involves multiple actions by different personas on the same calendar day (e.g., coder implements code, tester verifies, reviewer patches security), you MUST split this workflow into completely separate, sequential task objects inside the 'sub_tasks' array. Under no circumstances are you allowed to merge coder, reviewer, or tester actions on the same component into a single object node.
- **COMPONENT SEGREGATION:** Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, modify, or document for that exact step.

# 🔒 CRITICAL PRODUCTION STABILITY & PURITY MANDATES:
{% if is_chunked %}
- Target Focus: Parse sections strictly between Day {{ current_start_day }} and Day {{ current_end_day }} (inclusive). Generate a day object node inside 'days' array for EVERY day within range.
{% else %}
- Target Focus: Extract every scheduled day found in text. Generate a day object node inside 'days' array for EVERY documented day.
{% endif %}
- **NO ESCAPE HATCH:** Do NOT return empty array for 'days' if markdown text is present. Parse descriptions into sub-tasks utilizing Fallback Rule if paths are missing.
- **COMPONENT COMPLETENESS:** Every 'Target Path' listed in source Markdown must have a 1:1 mapping into 'components' array. Do not aggregate, abbreviate, or omit files.
- **STRICT CONTENT PURITY:** Output ONLY the pure raw executable JSON string matching schema. Response must start with `{` and end exactly with `}`. Banned from including thinking processes, chain-of-thought, conversational texts, introductions, wrapping inside markdown codeblocks (no ` ```json ` wrapping), or post-generation notes.
- **STRICT LITERAL FIELD VALUES:** Populate exact string "./sources/{{ global_context_file }}" into 'global_context_file'. Populate exact empty string "" into 'source_target_dir' field. (Enforcing an empty string ensures that all paths inside the 'components' array must maintain their full, explicit absolute repository reference starting with `./sources/` from the workspace root directory).
- **TASK DETAILS:** 'task' field must contain sequential description text preserving all embedded OWASP security tags (A01, A02, etc.) and requirement tracking tokens. Do not truncate or abstract them away.
- **AGENT FIELD VALUES:** 'agent' field MUST contain exactly one literal string token matching the authorized schema: 'coder', 'tester', 'reviewer', 'doc', 'docker', 'GCP', 'GKE'. Any other values (such as 'Manager' or 'DevOps') are strictly banned and will break the execution engine.
- **WORKSPACE PREFIX RULE:** Every path in 'components' array MUST strictly begin with `./sources/`. Generating files directly under repository root (e.g., `./Dockerfile`) is permanently BANNED.
- **FOR 'coder' TASKS:** 'components' array must contain relative file paths starting with `./sources/backend/` or `./sources/frontend/` using lowercase alphanumeric structures matching the project layout.
- **FOR 'reviewer' TASKS (Strict Single File Mandate):** The 'components' array MUST exclusively contain targeted individual code file paths requiring compilation fix, security hardening, or auto-patching (e.g., `"components": ["./sources/backend/src/main/java/.../AttendanceService.java"]`). You are ABSOLUTELY BANNED from parsing directory paths or parent folder paths into a reviewer task component array. It must resolve to an individual physical code file asset.
- **FOR 'doc' TASKS:** 'components' array must contain technical documents, process diagrams, workflow logs, metadata files, or structural layouts under `./sources/`. (e.g., `"components": ["./sources/docs/architecture_blueprint.md"]` or workflow files).
- **FOR 'tester' TASKS:** You MUST strictly preserve the semi-colon separated string format exactly as documented in source Markdown. Every single file path component on BOTH sides of the semi-colon character inside the string element MUST be strictly prefixed with `./sources/`.
     *   Do NOT split a `<source>;<test>` pair into two separate array elements. It MUST be emitted as a single string element inside the 'components' array.
     *   Example correct JSON entry: `"components": ["./sources/backend/src/main/java/.../Service.java;./sources/backend/src/test/java/.../ServiceTest.java"]`
     *   Example for Integration Tests: `"components": ["INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts"]`
- **JAVA PACKAGE ENFORCEMENT:** ONLY if the file path extension targets a Java component (`.java`), you MUST verify that the path contains the package layout directory segment derived from a pure alphanumeric lowercase format of the project name: `/org/nlh4j/saas/<stripped_lowercase_project_name>/`. For all non-Java files, this package segment is STRICTLY BANNED from being injected.
- **FOR docker TASKS:** The 'components' array MUST only contain Dockerfile configurations localized exactly inside their workspace subdirectories under `./sources/`. (e.g., `"components": ["./sources/backend/Dockerfile"]`).
- **FOR GCP AND GKE TASKS:** All architecture, orchestration manifests, IAM configurations, or deployment workflows must reside within their respective module enterprise folders starting with `./sources/`.

## 7. Context Fields: For each day object, set 'day' to its calculated integer value, set 'context_file' to './sources/{{ project_phase_context_file }}', and set 'context_section' to 'DAY ' followed by the calculated day number.

## 8. CHRONOLOGICAL TIMELINE SEQUENCING MANDATE (ABSOLUTE):
Evaluate the context tracking mechanics based strictly on the chunk configuration:
   - **Case A: If is_chunked is FALSE:** Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7"), you MUST reset the timeline sequence internally so that the first operational day inside this Phase always starts from integer 1. Progression follows sequentially as 2, 3, 4, etc. Map "Day 4" to "day": 1, and 'context_section' to "DAY 1".
   - **Case B: If is_chunked is TRUE:** You MUST PRESERVE the exact absolute chronological day index requested. The first parsed day object must match the integer value of {{ current_start_day }}, and progress incrementally up to {{ current_end_day }}. Under Case B, you are STRICTLY BANNED from resetting the day value to 1. Map "Day 4" to "day": 4, and its 'context_section' to "DAY 4".

You MUST conform strictly to your required JSON Schema layout design structure:
{{ phase_steps_json_schema }}

--- PHASE {{ phase_idx }} CONTEXT MARKDOWN ---
{{ phase_markdown_content }}
------------------------------------------
