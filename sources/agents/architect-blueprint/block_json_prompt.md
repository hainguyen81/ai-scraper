Analyze the attached Phase {{ phase_idx }} Context Markdown content.
{% if is_chunked %}
Extract and translate ALL daily steps, checklists, and agent tasks starting from Day {{ current_start_day }} up to Day {{ current_end_day }} (inclusive).
{% else %}
Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.
{% endif %}

# CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to {{ max_days_per_phase }} days maximum (Absolute Hard Limit: Maximum {{ max_days_per_phase }} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs or design multi-phase overviews beyond Day {{ max_days_per_phase }}.
## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

# AGENT ATOMICITY & COMPONENT MANDATES (CRITICAL FOR PRODUCTION):
## 1. ATOMIC AGENT ASSIGNMENT: Every single object inside the 'sub_tasks' array MUST have exactly ONE sub-agent role (string) assigned to the 'agent' field. Dual-agent or multi-agent assignments within a single task object are strictly forbidden.
## 2. NO ZERO-COMPONENT TASKS (ABSOLUTE HARD LIMIT): You are STRICTLY BANNED from generating any sub-task object where the 'components' array is empty `[]`, null, or missing. If an Agent does not have any physical files or target paths to create, modify, or test on that specific day, you MUST NOT generate that sub-task object at all. No components means NO task. Every file path inside 'components' must be prefixed with `./sources/`.
## 3. FALLBACK ADMINISTRATIVE COMPONENT RULE: If a specific day contains descriptive technical goals in the source text but lacks explicit physical file paths, you MUST NOT leave the 'components' array empty. Instead, assign the sub-task to the "Manager" agent and populate the 'components' array with exactly one element containing the localized context file string: "./sources/{{ project_phase_context_file }}".
## 4. ONE AGENT PER WORK-UNIT: If a workflow step requires collaborative action (e.g., a Coder writes code and a Tester verifies it), you MUST split this action into two distinct, sequential task objects inside the 'sub_tasks' array (Only if BOTH tasks have valid non-empty 'components'):
   - Task 1: Assigned to "Coder" with its respective files in 'components'.
   - Task 2: Assigned to "Tester" with its respective verification files in 'components'.
## 5. COMPONENT SEGREGATION: Ensure that the 'components' array inside each task object ONLY contains the specific files that the assigned agent will touch, create, or modify for that exact step.

# CRITICAL INSTRUCTIONS FOR PRODUCTION STABILITY & PURITY:
{% if is_chunked %}
## 1. Target Range Focus: Carefully locate all scheduling logs and task sections for any Day that falls strictly between Day {{ current_start_day }} and Day {{ current_end_day }} (inclusive).
## 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day within the requested range [{{ current_start_day }} to {{ current_end_day }}].
{% else %}
## 1. Target Range Focus: Extract every single scheduled day found in the provided markdown file.
## 2. Mandatory Data Extraction: You MUST parse and generate a day object node inside the 'days' array for EVERY single day documented in the text.
{% endif %}
## 3. NO ESCAPE HATCH: Do NOT return an empty array for 'days' under any circumstances if there is markdown text present. Even if tasks are not explicitly labeled, parse the paragraph descriptions into technical sub-tasks for that day utilizing the Fallback Rule if paths are missing.
## 3.1. COMPONENT COMPLETENESS MANDATE: Every single 'Target Path' listed under a sub-task in the source Markdown MUST have a 1:1 direct mapping into the 'components' array of that specific task object in the JSON output. Do NOT aggregate, abbreviate, or omit any file path.

## 4. STRICT CONTENT PURITY & NO FILLER MANDATE (CRITICAL):
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks, conversational texts, introductions (e.g., "Here is the JSON..."), analysis commentary, or post-generation notes.
- **Direct Output Mandate:** Output ONLY the pure raw executable JSON string matching the schema. Your response must begin immediately with the opening bracket `{` and end exactly with the closing bracket `}`. Any text, formatting, markdown codeblock wrapping (no ` ```json ` wrapping), or reasoning log outside the pure JSON structure will cause an immediate execution crash.

## 5. STRICT LITERAL FIELD VALUES (MANDATORY):
   - Populate the exact string "./sources/{{ global_context_file }}" into the 'global_context_file' field.
   - Populate the exact string "" into the 'source_target_dir' field. (Enforcing an empty string ensures that all paths inside the 'components' array must maintain their full, explicit absolute repository reference starting with `./sources/` from the workspace root directory).

## 6. Task Details: For every micro task item under a specific day:
   - Provide a sequential task description text into the 'task' field. **You MUST preserve all embedded OWASP security tags (e.g., A01, A02, etc.) and requirement tracking numbers from the source text; do not truncate or abstract them away.**
   - Provide the assigned role strictly matching the targeted persona matrix. **The 'agent' field MUST contain exactly one of the following literal string tokens: 'Coder', 'Tester', 'Reviewer', 'Docker', 'GCP', 'GKE', 'Manager'.**

## 6.1. STRICT COMPONENT SYNTAX & INFRASTRUCTURE GUARDRAILS FOR JSON ARRAY:
   - **Workspace Prefix Rule:** Generating file paths directly under the repository root (e.g., `./Dockerfile` or `./ci-cd.yml`) is strictly BANNED. Every single file path in the 'components' array MUST strictly begin with `./sources/`.
   - **For 'Coder' tasks:** The 'components' array MUST contain individual relative file path strings starting with `./sources/backend/` or `./sources/frontend/` using lowercase alphanumeric structures matching the project layout.
   - **For 'Tester' tasks:** You MUST strictly preserve the semi-colon separated string format exactly as documented in the source Markdown. Every component file path path pair inside the string MUST be strictly enclosed under `./sources/`.
     *   Do NOT split a `<source>;<test>` pair into two separate array elements. It MUST be emitted as a single string element inside the 'components' array.
     *   Example correct JSON entry: `"components": ["./sources/backend/src/main/java/.../Service.java;./sources/backend/src/test/java/.../ServiceTest.java"]`
     *   Example for Integration Tests: `"components": ["INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts"]`
   - **For 'Reviewer' tasks (Compiler Fixer Modality):** The 'components' array MUST contain the target file path requiring compilation fix, security hardening, or auto-patching. The path must be relative to the module inside sources (e.g., `"components": ["./sources/backend/src/main/java/.../AttendanceService.java"]`).
   - **Java Package Enforcement for Ingestion (Conditional):** ONLY if the backend technological stack uses Java, you MUST verify that every single Java source or test file path parsed into the 'components' array strictly contains the corporate package path segment: `/org/nlh4j/saas/{{ project_name }}/`.
         * If the source markdown omits this package prefix due to brevity, you MUST automatically inject and expand the path to include `/org/nlh4j/saas/{{ project_name }}/` based on Java package standards.
   - **For 'Docker' tasks:** The 'components' array MUST only contain Dockerfile configurations localized exactly inside their workspace subdirectories under `./sources/`.
         * *Correct Example:* `"components": ["./sources/backend/Dockerfile"]` or `"components": ["./sources/frontend/Dockerfile"]`
   - **For 'GCP' and 'GKE' tasks:** All architecture, orchestration manifests, IAM configurations, or deployment workflows must reside within their respective module enterprise folders starting with `./sources/`.

## 7. Context Fields: For each day object, set 'day' to its calculated integer value, set 'context_file' to './sources/{{ project_phase_context_file }}', and set 'context_section' to 'DAY ' followed by the calculated day number.

## 8. CHRONOLOGICAL TIMELINE SEQUENCING MANDATE (ABSOLUTE):
Evaluate the context tracking mechanics based strictly on the chunk configuration:
   - **Case A: If is_chunked is FALSE:** Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "Days 4-7"), you MUST reset the timeline sequence internally so that the first operational day inside this Phase always starts from integer 1. Progression follows sequentially as 2, 3, 4, etc. Map "Day 4" to "day": 1, and its 'context_section' to "DAY 1".
   - **Case B: If is_chunked is TRUE:** You MUST PRESERVE the exact absolute chronological day index requested. The first parsed day object must match the integer value of {{ current_start_day }}, and progress incrementally up to {{ current_end_day }}. Under Case B, you are STRICTLY BANNED from resetting the day value to 1. Map "Day 4" to "day": 4, and its 'context_section' to "DAY 4".

You MUST conform strictly to your required JSON Schema layout design structure:
{{ phase_steps_json_schema }}

--- PHASE {{ phase_idx }} CONTEXT MARKDOWN ---
{{ phase_markdown_content }}
------------------------------------------
