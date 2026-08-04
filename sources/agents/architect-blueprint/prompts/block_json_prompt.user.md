Analyze the attached Phase {{ phase_idx }} Context Markdown content. 
{% if is_chunked %}
Extract and parse ALL daily steps, checklists, and agent tasks starting from Day {{ current_start_day }} up to Day {{ current_end_day }} (inclusive). Localize the human-readable text strictly within the JSON string values according to your System Prompt Override rule.
{% else %}
Extract and parse ALL daily steps, checklists, and agent tasks from the entire document. Localize the human-readable text strictly within the JSON string values according to your System Prompt Override rule.
{% endif %}

# 🔒 AGENT ATOMICITY, TASK ID FORMAT & FILE-LEVEL COMPONENT MANDATES (ABSOLUTE):
- **STRICT TASK ID ALIGNMENT BLUEPRINT:** You MUST strictly generate the "id" field string for every single sub-task using the exact sequential formatting blueprint: `D<day_num>_ST<task_index>` (e.g., `D1_ST1`, `D1_ST2`, `D2_ST1`).
- **STRICT AGENT ROLE LITERAL VALUES:** The "agent" field inside the JSON sub-task object MUST strictly enforce a capitalized first letter and lowercase subsequent letters pattern matching the exact tokens: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'Gcp' | 'Gke'. Any other values or lowercase blocks (e.g., NO "coder") are strictly banned.
- **🚨 NO FOLDER OR PACKAGE PATHS ALLOWED IN COMPONENTS (ABSOLUTE HARD LIMIT):** You are STRINCENTLY BANNED from generating any sub-task object where the 'components' array field contains a raw folder directory name or stops at a Java package structural layer. 
  * 🚨 **THE STRICT TERMINAL EXPLICIT SUFFIX LAW (UNIVERSAL FILE-EXTENSION GATING)**: You MUST systematically cross-examine every predicted path string within the 'components' array. Every single output path string **MUST STRICTLY END** with one of the following explicit physical file format extensions: `.java`, `.tf`, `.sql`, `.yml`, `.yaml`, `.xml`, `.json`, `.properties`, `.md`, or the literal word `Dockerfile`. 
  * If a path ends with a raw directory folder name or a package boundary node (meaning the last characters of the string do NOT form a valid code file dot-extension, regardless of any dot operators present at the beginning like `./sources/`), you are CRITICALLY FORBIDDEN from carrying it over blindly into the payload. 
  * You MUST immediately intercept that truncated path container, think step-by-step like a Senior Solution Architect, evaluate the sub-task 'desc' context, and dynamically expand that plain folder path into an array of explicit physical file targets ending with proper code format suffixes (e.g., if the task 'desc' specifies implementing PostgreSQL and Firebase config inside a lazy `.../config` package boundary, you MUST programmatically refactor it into an array of individual explicit files: `.../config/DatabaseConfig.java`, `.../config/FirebaseAuthConfig.java`, and `.../config/SecurityConfig.java`). Every single array node element string must satisfy this explicit terminal file extension filter to pass backend runtime validation.
- **FALLBACK COMPONENT RULE:** If a day has technical descriptions but lacks physical file paths, assign the task to "Doc" agent and populate 'components' with exactly the value of: "{{ project_phase_context_file }}".
- **STRICT AGENT ROLE SEGREGATION (ANTI-AGGREGATION):** If a workflow file involves multiple actions by different personas on the same calendar day, you MUST split this workflow into completely separate, sequential task objects inside the 'sub_tasks' array.
- **HIGH-DENSITY TECHNICAL SPECIFICATION:** The 'task' field MUST contain an exhaustive, granular engineering instruction. If the sub-task involves an API route, integration endpoint, database query, or message block, you MUST explicitly inline the complete technical contract (e.g., Request/Response Payload Schemas, Data Types, Error Status Codes, or Queue names) directly inside this string value. Vague high-level bullet summaries are forbidden.
- **WORKSPACE PREFIX RULE & MULTI-LANGUAGE TEST EXCEPTION:** Every path in 'components' array MUST strictly begin with `./sources/`. 
  * *CRITICAL EXCEPTION:* If the first parameter before the semi-colon character in a tester task is the literal string token `INTEGRATION_SCOPE`, you MUST leave that token completely unmodified. Do NOT append any path prefix to it (e.g., `"components": ["INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts"]`).

# 🛠️ MANDATORY TOP-LEVEL FIELD VALUES INJECTION & ANCHOR PARSING (STRICT FIDELITY):
You MUST dynamically populate the top-level keys of the JSON object using EXACT raw variable values without any modifications, or parse them directly from the primary Markdown header HTML comments:
- **`phase_id`**: {{ phase_idx }}
- **`phase_name`**: [Locate the primary Markdown title header line, extract the clean technical string text located exactly between the hidden HTML delimiters `<!--PHASE_NAME_START-->` and `<!--PHASE_NAME_END-->` without any alterations or translations]
- **`phase_description`**: [Locate the primary Markdown title header line, extract the exact contextually translated phase description text that follows after the literal marker `| Description:` or its translated equivalent]
- **`project_name`**: "{{ project_name }}"
- **`global_context_file`**: "{{ global_context_file }}"
- **`source_target_dir`**: "{{ source_target_dir }}"

## 7. Context Fields Integration Mandate
- For each day object inside the array, set 'day' to its calculated integer value, set 'context_file' to exact string "{{ project_phase_context_file }}", and set 'context_section' to the exact string value of the entire primary Day Header extracted from the source Markdown context text (render this value contextually translated into the target language context) (e.g., `"context_section": "DAY 1: Multi-Tenant Inception Schema & Flyway Migration Setup"`).
- **`context_section`**: You MUST locate the exact day header line inside the source Markdown context and scan exclusively between the technical delimiters `<!--DAY_HEADER_START-->` and `<!--DAY_HEADER_END-->`. You MUST extract the ENTIRE clean human-readable title phrase enclosed within these markers. You are CRITICALLY BANNED from truncating, shortcutting, or slicing the string to just "DAY 1" or "DAY 2". You MUST capture the full, complete objective text after the day marker and render this value contextually translated into the target language context (e.g., if the localized text inside the anchors is in Vietnamese, extract and output it exactly, such as: `"context_section": "NGÀY 1: Thiết lập cấu hình cơ sở dữ liệu và hạ tầng"`).

## 8. CHRONOLOGICAL TIMELINE SEQUENCING MANDATE (ABSOLUTE):
{% if is_chunked %}
# SYSTEM CRITICAL BOUNDARY: CHUNKED CONFIGURATION IS ACTIVE (is_chunked is TRUE)
- You MUST PRESERVE the exact absolute chronological day index requested from the template parameters.
- The first parsed day object inside the 'days' array MUST match the exact integer value of {{ current_start_day }}, and progress incrementally up to {{ current_end_day }}.
- You are STRICTLY BANNED from resetting the day value to 1. Map the absolute day index directly to the "day" field, set 'context_file' to "{{ project_phase_context_file }}", and set 'context_section' to the localized primary day header line corresponding to that absolute day index from the source markdown.
{% else %}
# SYSTEM CRITICAL BOUNDARY: FLAT CONFIGURATION IS ACTIVE (is_chunked is FALSE)
- Regardless of the actual day numbers documented in the source Markdown content (e.g., even if the text states "DAY 4", "DAY 5"), you MUST completely reset the timeline sequence internally so that the first operational day inside this Phase always starts from integer 1. Progression follows sequentially as 2, 3, 4, etc.
- Map the first targeted day to `"day": 1`, set 'context_file' to "{{ project_phase_context_file }}", and strictly set 'context_section' to the localized primary header line of the first day parsed from the text. Incremental days follow this relative baseline.
{% endif %}

# 🛑 MANDATORY STRUCTURE ENFORCEMENT FOR TRACEABILITY TAGS VIA HTML ANCHORS (CRITICAL):
- For each sub-task block, locate the hidden technical container bounds delimited strictly between `<!--START_TAGS-->` and `<!--END_TAGS-->`. Extract all individual inherited Tag IDs from inside that container, completely purge all markdown backticks (`` ` ``) and padding spaces, and populate them as clean separate string elements inside the "targeted_tags" array field (e.g., `"targeted_tags": ["[REQ-001]", "[DAT-005]"]`).
- You are STRICTLY BANNED from leaving the "targeted_tags" array empty `[]` or null. Every single tag token must be its own separated array element string.

You must conform strictly and output exactly ONE (1) single, standalone, unified JSON block containing all target fields including `objectives`, `phase_idx`, and `phase_context_file` from the very start. 

🚨 **CRITICAL PIPELINE FREEZE MANDATE**: You are ABSOLUTELY FORBIDDEN from outputting conversational filler text, dashes, symbols, separators (NO `----------------------------------`), post-generation text remarks, or secondary blocks. Open exactly with a single line of triple backticks + json, render the unified schema, close with a closing brace, close with triple backticks, and STOP GENERATING INSTANTLY. Any token after the first valid closing fence crashes the enterprise runtime.

Required JSON Schema layout design structure: {{ phase_steps_json_schema }}

--- PHASE {{ phase_idx }} CONTEXT MARKDOWN ---
{{ phase_markdown_content }}
------------------------------------------
