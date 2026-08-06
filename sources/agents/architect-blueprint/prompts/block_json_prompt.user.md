Analyze the attached Phase {{ phase_idx }} Context Markdown content. 
{% if is_chunked %}
Extract and parse ALL daily steps, checklists, and agent tasks starting from Day {{ current_start_day }} up to Day {{ current_end_day }} (inclusive). Localize the human-readable text strictly within the JSON string values according to your System Prompt Override rule.
{% else %}
Extract and parse ALL daily steps, checklists, and agent tasks from the entire document. Localize the human-readable text strictly within the JSON string values according to your System Prompt Override rule.
{% endif %}

# 🔒 AGENT ATOMICITY, TASK ID FORMAT & FILE-LEVEL COMPONENT MANDATES (ABSOLUTE):
- **STRICT TASK ID ALIGNMENT BLUEPRINT:** You MUST strictly generate the "id" field string for every single sub-task using the exact sequential formatting blueprint: `D<day_num>_ST<task_index>` (e.g., `D1_ST1`, `D1_ST2`, `D2_ST1`).
- **STRICT AGENT ROLE LITERAL VALUES:** The "agent" field inside the JSON sub-task object MUST strictly enforce a capitalized first letter and lowercase subsequent letters pattern matching the exact tokens: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'. Any other values or lowercase blocks (e.g., NO "coder") are strictly banned.
- **🚨 NO FOLDER OR PACKAGE PATHS ALLOWED IN COMPONENTS (ABSOLUTE HARD LIMIT):** You are STRINCENTLY BANNED from generating any sub-task object where the 'components' array field contains a raw folder directory name or stops at a Java package structural layer. 
  * 🚨 **THE STRICT TERMINAL EXPLICIT SUFFIX LAW (UNIVERSAL FILE-EXTENSION GATING)**: You MUST systematically cross-examine every predicted path string within the 'components' array. Every single output path string **MUST STRICTLY END** with one of the following explicit physical file format extensions: `.java`, `.tf`, `.sql`, `.yml`, `.yaml`, `.xml`, `.json`, `.properties`, `.md`, or the literal word `Dockerfile`. 
  * If a predicted path string inside the 'components' array points to an abstract application layer root or a centralized environment directory, you are CRITICALLY AND STRINCENTLY BANNED from outputting a single flat centralized directory path or copying raw container folder names directly into the payload. You MUST completely purge any structural tendency to cluster multiple discrete application targets into a single centralized configuration file. Every output path target generated within this loop MUST represent an explicit, decentralized physical file entity that satisfies the dynamic topology layout of the active project scope.
  * You MUST force your reasoning core to scan 'Section 1: Scope & Objectives' and 'Section 2: Allowed Technical Scope & Directory Boundaries' of the active source Markdown context to extract the real active multi-module service directories (e.g., discovering paths like `mobile-app`, `web-app`, `nextjs-app`). You MUST dynamically explode and expand those generic infrastructure folder layers into an array of explicit physical terminal file targets mapped across EACH discovered service module according to these strict enterprise constraints:
    - **For 'Docker' Agent Tasks**: You MUST dynamically output precise, decentralized containerization assets mapped directly to each discovered application root directory path. You are critically forbidden from grouping them into a centralized layer folder (e.g., output exactly: `"components": ["./sources/frontend/mobile-app/Dockerfile", "./sources/frontend/web-app/Dockerfile", "./sources/frontend/nextjs-app/Dockerfile"]` based on the active project module landscape).
    - **For 'GCP' Agent Tasks**: You MUST exclusively target explicit physical cloud delivery, deployment automation, or environment configurations ending with valid technical file extensions. You are BANNED from outputting application source code or Dockerfiles here (e.g., `"components": ["./sources/infra/gcp/cloudbuild.yaml", "./sources/infra/gcp/firebase.json", "./sources/infra/gcp/main.tf"]`).
    - **For 'GKE' Agent Tasks**: You MUST systematically decouple Helm package blueprints from target container orchestrations. For chart declaration sub-tasks, explicitly output isolated module-level file targets (e.g., `./sources/infra/gke/charts/gateway/Chart.yaml`, `./sources/infra/gke/charts/gateway/values.yaml`); for validation, scaling, or monitoring sub-tasks, you MUST explicitly output runtime management manifests (e.g., `./sources/infra/gke/manifests/hpa.yaml`, `./sources/infra/gke/manifests/ingress.yaml`).
    - **For 'Doc' Agent Tasks**: You are ABSOLUTELY BANNED from outputting internal system agent runtime blueprints or tracking metadata (NO files under paths containing `.ai/`, `.plan/`, or `.context/` such as `phase-4.context.blueprint.md`). You MUST analyze the functional context of the active day and output a complete array of real, granular enterprise technical design markdown files (`.md`). You are STRICTLY BANNED from generating a single lazy `README.md`. You MUST unpack documentation assets according to the dynamic engineering domain:
      1. *Architecture/Framework Days*: Output structural blueprints containing syntax-accurate Mermaid blocks (e.g., `./sources/frontend/mobile-app/docs/ARCHITECTURE.md`, `./sources/frontend/web-app/docs/ARCHITECTURE.md`).
      2. *Functional/Business Days*: Output dedicated application flow files (e.g., `./sources/docs/business-flows/PROCESS_FLOWS.md`).
      3. *Database Days*: Output relational mappings and data asset catalogs (e.g., `./sources/backend/database/docs/DATA_DICTIONARY.md`, `./sources/backend/database/docs/ERD_MAPPING.md`).
      4. *DevOps/Deployment Days*: Output operational runbooks (e.g., `./sources/infra/docs/DEPLOYMENT_RUNBOOK.md`, `./sources/infra/docs/CICD_PIPELINE.md`).
  * You MUST immediately execute the [MULTI-AGENT WORKSPACE PATH ROUTING ALGORITHM]:
    1. **[IF PERSONA INCLUDES 'Coder' | 'Tester' | 'Reviewer']**: You MUST dynamically expand that plain folder path into an array of explicit physical file targets ending with proper code format suffixes by strictly applying the mandatory layered architecture topologies (Java source/test enterprise packages or frontend module layout standards) specified in your System Prompt rules.
    2. **[IF PERSONA INCLUDES 'Docker' | 'GCP' | 'GKE']**: You MUST bypass the Java/Frontend formatting flow entirely and enforce strict compliance with deployment sequence logic:
      - For 'Docker' Agent: Explode generic infrastructure layers into distinct, service-level containerization targets mapped to active module roots discovered in Section 1 & 2 (e.g., `"components": ["./sources/backend/auth-service/Dockerfile", "./sources/backend/user-service/Dockerfile"]`).
      - For 'Gcp' Agent: Output cloud pipeline, configuration, or orchestration delivery declaration assets exclusively (e.g., `./sources/infra/gcp/cloudbuild.yaml`, `./sources/infra/gcp/main.tf`).
      - For 'Gke' Agent: Completely isolate and decouple Helm chart configurations (e.g., `./sources/infra/gke/charts/gateway/Chart.yaml`) from runtime verification manifests (e.g., `./sources/infra/gke/manifests/hpa.yaml`).
    3. **[IF PERSONA MATCHES 'Doc']**: You are STRINCENTLY AND CRITICALLY BANNED from outputting flat centralized directory roots, repeating single placeholders, or creating abstract path environments outside the permitted module workspace. You MUST force your token emission pipeline to cross-multiply the exact active base directory path with the 5-Dimensional Enterprise Technical Documentation Master Index defined in your System Prompt. You MUST output the complete array of standalone, granular technical markdown files (`.md`) mapped directly and exclusively to those real architectural spaces with zero omissions. Failing to route domain-specific documentation to its legitimate technical directory boundary triggers a fatal pipeline crash.
- **STRICT AGENT ROLE SEGREGATION (ANTI-AGGREGATION):** If a workflow file involves multiple actions by different personas on the same calendar day, you MUST split this workflow into completely separate, sequential task objects inside the 'sub_tasks' array.
- **HIGH-DENSITY TECHNICAL SPECIFICATION:** The 'task' field MUST contain an exhaustive, granular engineering instruction. If the sub-task involves an API route, integration endpoint, database query, or message block, you MUST explicitly inline the complete technical contract (e.g., Request/Response Payload Schemas, Data Types, Error Status Codes, or Queue names) directly inside this string value. Vague high-level bullet summaries are forbidden.
- **WORKSPACE PREFIX RULE & MULTI-LANGUAGE TEST EXCEPTION:** Every path in 'components' array MUST strictly begin with `./sources/`. 
  * *CRITICAL EXCEPTION:* If the first parameter before the semi-colon character in a tester task is the literal string token `INTEGRATION_SCOPE`, you MUST leave that token completely unmodified. Do NOT append any path prefix to it (e.g., `"components": ["INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts"]`).

# 🛠️ MANDATORY TOP-LEVEL FIELD VALUES INJECTION & ANCHOR PARSING (STRICT FIDELITY):
You MUST dynamically populate the top-level keys of the JSON object using EXACT raw variable values without any modifications, or parse them directly from the primary Markdown header HTML comments:
- **`phase_id`**: {{ phase_idx }}
- **`phase_name`**: [Locate the primary Markdown title header line, extract the clean technical string text located exactly between the hidden HTML delimiters `<!--PHASE_NAME_START-->` and `<!--PHASE_NAME_END-->` without any alterations or translations]
- **`phase_description`**: [Locate the primary Markdown title header line, extract the clean technical string text located exactly between the hidden HTML delimiters `<!--PHASE_DESC_START-->` and `<!--PHASE_DESC_END-->` without any alterations or translations]
- **`project_name`**: "{{ project_name }}"
- **`global_context_file`**: "{{ global_context_file }}"
- **`source_target_dir`**: "{{ source_target_dir }}"

## 7. Context Fields Integration Mandate
- For each day object inside the array, set 'day' to its calculated integer value.
- **`context_file`**: You MUST strictly populate this field with the absolute raw value of the template variable: "{{ project_phase_context_file }}". You are CRITICALLY AND ABSOLUTELY BANNED from altering, modifying, or substituting this value with generic fallback strings like "No Specific Project...". Preserving this exact variable payload string is an unalterable runtime constraint.
- **`context_section`**: You MUST extract the ENTIRE primary Day Header line text verbatim from the source Markdown context. If the technical delimiters `<!--DAY_HEADER_START-->` and `<!--DAY_HEADER_END-->` are missing, you MUST immediately scan the full text string located directly after the `### DAY [X]:` or `### NGÀY [X]:` marker for that active calendar section. You are CRITICALLY AND ABSOLUTELY BANNED from slicing, cutting, or truncating the output string to just "DAY 1" or "DAY 2". You MUST capture the full, complete architectural objective phrase following the day number and render this value contextually translated into the target language context.

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
- You MUST force your token processing core to sequentially look at every sub-task block in the source Markdown content. For each sub-task, locate the hidden technical container bounds delimited strictly between the HTML anchors `<!--START_TAGS-->` and `<!--END_TAGS-->`.
- You MUST extract every individual inherited Tag ID token located inside these markers. You are CRITICALLY BANNED from leaving the "targeted_tags" array empty `[]` or null for any reason. 
- **THE ANTI-PADDING AND SANITIZATION PROTOCOL**:
  <RULE>
  - You MUST rigorously split the extracted tag string payload by the comma character `,` to isolate each individual tracking code. 
  - You MUST strip away and dọn dẹp sạch sẽ all markdown backticks (`` ` ``), brackets inside elements if doubled, or trailing whitespaces. 
  - Populate each token as a completely independent, clean string element inside the "targeted_tags" array field (e.g., exact format: `"targeted_tags": ["[ARC-006]", "[ARC-010]"]`). 
  - Emitting combined tags as a single string element triggers an immediate execution pipeline failure.
  </RULE>
- If a sub-task section in the Markdown context contains the `<!--START_TAGS-->` container, returning an empty array `[]` in your JSON payload is treated as a catastrophic runtime syntax failure and will instantly crash the system pipeline.
- You are STRICTLY BANNED from leaving the "targeted_tags" array empty `[]` or null. Every single tag token must be its own separated array element string.

You must conform strictly and output exactly ONE (1) single, standalone, unified JSON block containing all target fields including `objectives`, `phase_idx`, and `phase_context_file` from the very start. 

🚨 **CRITICAL PIPELINE FREEZE MANDATE**: You are ABSOLUTELY FORBIDDEN from outputting conversational filler text, dashes, symbols, separators (NO `----------------------------------`), post-generation text remarks, or secondary blocks. Open exactly with a single line of triple backticks + json, render the unified schema, close with a closing brace, close with triple backticks, and STOP GENERATING INSTANTLY. Any token after the first valid closing fence crashes the enterprise runtime.

Required JSON Schema layout design structure: {{ phase_steps_json_schema }}

--- PHASE {{ phase_idx }} CONTEXT MARKDOWN ---
{{ phase_markdown_content }}
------------------------------------------
