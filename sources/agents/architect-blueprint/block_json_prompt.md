Analyze the attached Phase {{ phase_idx }} Context Markdown content.
{% if is_chunked %}
Extract/translate ALL daily steps, checklists, and agent tasks starting from Day {{ current_start_day }} up to Day {{ current_end_day }} (inclusive).
{% else %}
Extract/translate ALL daily steps, checklists, and agent tasks from the entire document.
{% endif %}

# ⏳ CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT: Individual Phase MUST be bounded between 1 to {{ max_days_per_phase }} days maximum. Never generate scheduling logs beyond Day {{ max_days_per_phase }}.
## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core objectives are satisfied. Do NOT duplicate or loop previous task structures. Freeze output and exit.

# 🔒 AGENT ATOMICITY & COMPONENT MANDATES (ABSOLUTE):
- **ATOMIC AGENT ASSIGNMENT:** Every object inside 'sub_tasks' MUST have exactly ONE sub-agent role string assigned to 'agent' field. Dual-agent assignments are strictly forbidden.
- **NO ZERO-COMPONENT TASKS:** STRICTLY BANNED from generating any task object where 'components' array is empty `[]` or null. No physical paths means NO task object allowed.
- **FALLBACK COMPONENT RULE:** If a day has technical descriptions but lacks physical file paths, assign the task to "Manager" agent and populate 'components' with exactly: `["./sources/{{ project_phase_context_file }}"]`.
- **ONE AGENT PER WORK-UNIT:** Separate collaborative actions into sequential distinct task objects inside 'sub_tasks' array (e.g., Coder implements, Tester verifies, Reviewer patches). Banned from merging Coder, Reviewer, or Tester actions on the same file into a single object node.
- **COMPONENT SEGREGATION:** The 'components' array MUST ONLY contain specific files that the assigned agent touches or modifies for that exact step.

# 🔒 CRITICAL PRODUCTION STABILITY & PURITY MANDATES:
{% if is_chunked %}
- Target Focus: Parse sections strictly between Day {{ current_start_day }} and Day {{ current_end_day }} (inclusive). Generate a day node inside 'days' array for EVERY day within range.
{% else %}
- Target Focus: Extract every scheduled day found in text. Generate a day node inside 'days' array for EVERY documented day.
{% endif %}
- **NO ESCAPE HATCH:** Do NOT return empty array for 'days' if markdown text is present. Parse descriptions into sub-tasks utilizing Fallback Rule if paths are missing.
- **COMPONENT COMPLETENESS:** Every 'Target Path' listed in source Markdown must have a 1:1 mapping into 'components' array. Do not aggregate, abbreviate, or omit files.
- **STRICT CONTENT PURITY:** Output ONLY the pure raw executable JSON string matching schema. Response must start with `{` and end exactly with `}`. Banned from including thinking processes, chain-of-thought, conversational texts, introductions, wrapping inside markdown codeblocks (no ` ```json ` wrapping), or post-generation notes.
- **STRICT LITERAL FIELD VALUES:** Populate exact string "./sources/{{ global_context_file }}" into 'global_context_file'. Populate exact empty string "" into 'source_target_dir' field.

- **TASK DETAILS:** 'task' field must contain sequential description text preserving all embedded OWASP security tags (A01, A02, etc.) and requirement tracking tokens. Do not truncate.
- **AGENT FIELD VALUES:** 'agent' field MUST contain exactly one literal string token: 'Coder', 'Tester', 'Reviewer', 'Docker', 'GCP', 'GKE', 'Manager'.
- **WORKSPACE PREFIX RULE:** Every path in 'components' array MUST strictly begin with `./sources/`. Generating files directly under repository root (e.g., `./Dockerfile`) is permanently BANNED.
- **FOR 'CODER' TASKS:** 'components' array must contain relative file paths starting with `./sources/backend/` or `./sources/frontend/`.
- **FOR 'TESTER' TASKS:** Strictly preserve semi-colon separated syntax format exactly as documented in source Markdown. Both paths inside the string pair MUST begin with `./sources/`.
  * *Correct JSON Entry:* `"components": ["./sources/backend/src/main/java/.../Service.java;./sources/backend/src/test/java/.../ServiceTest.java"]`
  * *Integration / E2E:* `"components": ["INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts"]`
- **FOR 'REVIEWER' TASKS:** 'components' array must contain relative file paths requiring compilation fix or security hardening starting strictly with `./sources/` (e.g., `"components": ["./sources/backend/src/main/java/.../AttendanceService.java"]`).
- **JAVA PACKAGE ENFORCEMENT:** If techstack uses Java, verify every `.java` file path in 'components' contains package segment derived from pure lowercase alphanumeric format of project name: `/org/nlh4j/saas/<stripped_lowercase_project_name>/.` Auto-expand prefix if omitted in source. Banned from injecting this segment into non-Java extensions.
- **FOR DOCKER / GCP / GKE TASKS:** Configurations, Dockerfiles, and manifests must reside in enterprise subdirectories starting strictly with `./sources/`.

- **CONTEXT FIELDS:** For each day object, set 'day' to its calculated integer value, set 'context_file' to './sources/{{ project_phase_context_file }}', and set 'context_section' to 'DAY ' followed by calculated day number.

- **CHRONOLOGICAL TIMELINE SEQUENCING MANDATE (ABSOLUTE):**
  * **Case A (is_chunked is FALSE):** Reset timeline sequence internally so first operational day always starts from integer 1. Progression follows 2, 3, 4, etc. Map "Day 4" to "day": 1, and 'context_section' to "DAY 1".
  * **Case B (is_chunked is TRUE):** PRESERVE exact absolute chronological day index requested. First parsed day object must match integer value of {{ current_start_day }}, progressing up to {{ current_end_day }}. Under Case B, you are STRICTLY BANNED from resetting the day value to 1. Map "Day 4" to "day": 4, and 'context_section' to "DAY 4".

You MUST conform strictly to your required JSON Schema layout design structure:
{{ phase_steps_json_schema }}

--- PHASE {{ phase_idx }} CONTEXT MARKDOWN ---
{{ phase_markdown_content }}
------------------------------------------
