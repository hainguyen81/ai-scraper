Analyze the attached Phase {{ phase_idx }} Context Markdown content.
{% if is_chunked %}
Extract and translate ALL daily steps, checklists, and agent tasks starting from Day {{ current_start_day }} up to Day {{ current_end_day }} (inclusive).
{% else %}
Extract and translate ALL daily steps, checklists, and agent tasks from the entire document.
{% endif %}

# ⏳ CRITICAL CHUNK BOUNDARY ALIGNMENT RULE
# This rule applies ONLY if the chunk configuration is active (is_chunked is TRUE).
- **Boundary Execution Context:** When parsing tasks that span across boundary calendar days, you MUST exclusively extract and document the operational steps and sub-tasks that are actively executed within the requested window of Day {{ current_start_day }} to Day {{ current_end_day }}. Do not duplicate previous states or omit ongoing workflows.

# ⏳ CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT: Individual Phase MUST be bounded between 1 to {{ max_days_per_phase }} days maximum. Never generate scheduling logs beyond Day {{ max_days_per_phase }}.
## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core objectives are satisfied. Do NOT duplicate or loop previous task structures. Freeze output and exit.

# 🛑 ANTI-CREATIVE TAGGING & INHERITANCE MANDATE (CRITICAL):
1. You are STRICTLY BANNED from inventing, generating, omitting, or modifying any requirement Tag IDs (`[REQ-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`).
2. Every Tag ID present in the source Phase Markdown content MUST be perfectly preserved and mapped 1:1 into the corresponding task node inside the JSON output.
3. Under no circumstances should you strip out or abstract away these tracking codes.

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
- **STRICT LITERAL FIELD VALUES:** Populate exact string `./sources/{{ global_context_file }}` into 'global_context_file'. Populate exact empty string "" into 'source_target_dir' field. (All paths inside the 'components' array must maintain their full, explicit absolute repository reference starting with `./sources/` from the workspace root directory).

- **HIGH-DENSITY TECHNICAL SPECIFICATION:** The 'task' field MUST contain an exhaustive, granular engineering instruction. If the sub-task involves an API route, integration endpoint, database query, or message block, you MUST explicitly inline the complete technical contract (e.g., Request/Response Payload Schemas, Data Types, Error Status Codes, or Queue names) directly inside this string. Vague high-level bullet summaries are forbidden.
- **AGENT FIELD VALUES:** 'agent' field MUST contain exactly one literal string token matching the authorized schema: 'coder', 'tester', 'reviewer', 'doc', 'docker', 'GCP', 'GKE'. Any other values are strictly banned.
- **WORKSPACE PREFIX RULE:** Every path in 'components' array MUST strictly begin with `./sources/`. Generating files directly under repository root is permanently BANNED.
- **FOR 'coder' TASKS:** 'components' array must contain relative file paths starting with `./sources/backend/` or `./sources/frontend/` using lowercase alphanumeric structures matching the project layout.
- **FOR 'reviewer' TASKS (Strict Single File Mandate):** The 'components' array MUST exclusively contain targeted individual code file paths requiring compilation fix, security hardening, or auto-patching. You are ABSOLUTELY BANNED from parsing directory paths or parent folder paths into a reviewer task component array.
- **FOR 'doc' TASKS:** 'components' array must contain technical documents, process diagrams, workflow logs, metadata files, or structural layouts under `./sources/`.
- **FOR 'tester' TASKS:** You MUST strictly preserve the semi-colon separated string format `<source>;<test>` exactly as documented in source Markdown. 
  * **Workspace Prefix Rule with Token Exception:** Every single physical file path component on BOTH sides of the semi-colon character inside the string element MUST be strictly prefixed with `./sources/`. 
  * **CRITICAL EXCEPTION:** If the first parameter before the semi-colon character is the literal string token `INTEGRATION_SCOPE`, you MUST leave that token completely unmodified. Do NOT append any path prefix to it (e.g., `"components": ["INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts"]`). Appending `./sources/` to the database placeholder or literal integration token is strictly banned.
- **FOR docker / GCP / GKE TASKS:** The 'components' array MUST exclusively contain targeted DevOps manifests localized inside the dedicated infrastructure subdirectory layer (e.g., `"components": ["./sources/infra/gke/deployment.yaml"]`).

# [CONDITION: JAVA_STACK_ONLY] Java Directory Integrity Verification
# Explicit regex rule to ensure 100% path consistency across distinct sub-agent execution pipelines.
- **Calculated Lowercase Token Rule:** To compute the package layouts, you MUST strictly apply a deterministic regex execution pattern: Remove all non-alphanumeric characters, strip out whitespaces, underscores, hyphens, and force-convert the remaining string token entirely into 100% pure lowercase alphanumeric characters.
- Only if the file path extension targets a Java component (.java), you MUST verify that the path contains the calculated package segment: `/org/nlh4j/saas/<calculated_lowercase_token>/`. For all non-Java files, this package segment is STRICTLY BANNED.

## 7. Chronological Timeline and Section Sequencing Mandate
# Evaluate the context tracking mechanics based strictly on the chunk configuration to prevent logical conflicts.
# The 'day' integer and 'context_section' string MUST be resolved atomically within the specific cases below.
- **Case A: If is_chunked is FALSE:**
  * Regardless of the actual day numbers documented in the source Markdown content (e.g., even if text states "Days 4-7"), you MUST reset the timeline sequence internally so that the first operational day inside this Phase always starts from integer 1. Progression follows sequentially as 2, 3, 4, etc. 
  * Map the first targeted day to `"day": 1`, set 'context_file' to `"./sources/{{ project_phase_context_file }}"`, and strictly set 'context_section' to `"DAY 1"`. Incremental days follow this relative baseline.
- **Case B: If is_chunked is TRUE:**
  * You MUST PRESERVE the exact absolute chronological day index requested from the template parameters. The first parsed day object must match the integer value of {{ current_start_day }}, and progress incrementally up to {{ current_end_day }}. 
  * Under Case B, you are STRICTLY BANNED from resetting the day value to 1. Map the absolute day index to the `"day"` field, set 'context_file' to `"./sources/{{ project_phase_context_file }}"`, and set 'context_section' to `"DAY "` followed exactly by that calculated absolute day number (e.g., `"DAY 4"`).

# 🛑 MANDATORY STRUCTURE ENFORCEMENT FOR TRACEABILITY TAGS (CRITICAL):
When extracting sub-tasks, you MUST populate the exact inherited BA/SA Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) directly into the "targeted_tags" array field of EACH sub-task object node inside the JSON schema.
- Scan the source Markdown text, extract all corresponding Tag IDs for that sub-task, and populate them as clean individual string elements inside the "targeted_tags" array (e.g., `"targeted_tags": ["[REQ-001]", "[DAT-005]", "[EXC-002]"]`).
- You are STRICTLY BANNED from leaving the "targeted_tags" array empty `[]` or bundling tags into a single string (e.g., NO `["[REQ-001], [REQ-002]"]`). Every tag must be its own array element.

You must conform strictly to your required JSON Schema layout design structure:
{{ phase_steps_json_schema }}

--- PHASE {{ phase_idx }} CONTEXT MARKDOWN ---
{{ phase_markdown_content }}
------------------------------------------
