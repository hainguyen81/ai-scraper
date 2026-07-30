# CONTEXT INHERITANCE PIPELINE
Project Name: {{ project_name }}
You are tasked to detail **PHASE {{ phase_idx }} OUT OF {{ num_phases }}**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
{{ global_markdown_context }}

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---
# Use this state to track exactly what has already been built across preceding phases. Do not reinvent or override these existing file layouts.
{{ previous_phase_context }}

--- RAW REQUIREMENTS REFERENCE ---
{{ project_requirements }}
----------------------------------

# 🛑 CORE DATABASE SCHEMA INHERITANCE MANDATE
# Explicit instruction to prevent broken relational foreign key mappings across decoupled development phases.
- **Relational Integrity Bound:** When designing a localized data dictionary table for this current Phase, you MUST strictly inherit and reference the exact primary keys (PK), column names, and data types established in preceding modules or global baseline. Do NOT alter inherited schema definitions. Every foreign key (FK) mapping must be fully trace-compatible with its parent entity state.

# 🛑 ANTI-CREATIVE TAGGING & INHERITANCE MANDATE (CRITICAL):
1. You are STRICTLY BANNED from inventing, generating, or guessing any new Tag IDs.
2. Every Tag ID you reference (`[REQ-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) MUST be a 100% exact string match to the tags found inside the `--- RAW REQUIREMENTS REFERENCE ---` or `--- GLOBAL CONTEXT REFERENCE ---` sections.
3. If a tag is not present in the input documentation, it DOES NOT EXIST. Do not create placeholder tags or secondary sequence systems.

# CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT:
Each individual Phase MUST be strictly bounded between 1 to {{ max_days_per_phase }} days maximum (Absolute Hard Limit: Maximum {{ max_days_per_phase }} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs or design multi-phase overviews beyond Day {{ max_days_per_phase }} for this phase.

## 2. PROGRESSION STOPPING CRITERION (ZERO FILLER DAYS):
Stop generating daily logs immediately once the core technical objectives allocated for this current Phase are satisfied. Do NOT duplicate, loop, or inject placeholder tasks (such as generic reviews, documentation padding, or empty syncs) just to inflate the calendar. If the technical work is logically complete on Day 1, freeze the output and exit immediately.

# EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE {{ phase_idx }} into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY {{ max_days_per_phase }}**.
2. **Strict Grouping Hierarchy:**
   - **DAY LEVEL:** Group all activities belonging to that specific calendar day.
   - **AGENT SUB-TASK LEVEL:** Inside each Day, split work strictly by Sub-Tasks. **Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'coder' OR 'tester' OR 'reviewer' OR 'doc' OR 'docker' OR 'GCP' OR 'GKE'**. You are ABSOLUTELY BANNED from inventing external agent personas (e.g., 'Manager' or 'DevOps' are permanently banned).
   - **TARGET COMPONENT LEVEL:** Inside each Day, list **ALL Target Paths (Components)** that the designated Agent is responsible for creating, modifying, testing, or documenting on that day.

3. **STRICT TARGET PATH SYNTAX RULES FOR AGENTS:**
   - **For coder / doc / docker / GCP / GKE Agents:** Each component MUST be listed as a single relative file path string starting strictly with `./sources/`.
     * *CRITICAL DOC AGENT RULE:* If the assigned agent is 'doc', the target path must represent an explicit documentation asset, business specification, flow architecture file, or diagram asset placed inside the dedicated documentation or module folders under `./sources/`.
     * *DEVOPS AND INFRASTRUCTURE BOUNDS:* If the assigned agent is docker, GCP, or GKE, the target path must be encapsulated cleanly within the dedicated infrastructure paths (e.g., `./sources/infra/docker/Dockerfile` or `./sources/infra/gke/deployment.yaml`). Generating configuration assets in the root workspace boundary is permanently banned.
   - **For reviewer Agent (Strict File Bound Rule):** The component MUST be a single, explicit physical code file path (e.g., ending with `.java`, `.go`, `.py`, `.ts`). You are STRICTLY BANNED from targeting a directory or parent folder path. The task must exclusively execute automated static code analysis, security linting, or compiler error fixes on that individual file.
   - **For tester Agent (Multi-Language Testing Context):** Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST be absolute to the workspace and begin with `./sources/`.
     * **Rule for Unit Tests:** Match the exact physical path of the component class/file being tested with its corresponding test suite file under `./sources/`. Example: `./sources/backend/src/main/java/org/nlh4j/saas/ecommerceapp/service/OrderService.java;./sources/backend/src/test/java/org/nlh4j/saas/ecommerceapp/service/OrderServiceTest.java`
     * **Rule for Integration / E2E / UI Tests (No single source file isolated):** You MUST use the literal string token `INTEGRATION_SCOPE` as the first parameter to signal that this test verifies multi-component workflows, cross-platform behaviors, or API network loops. Example: `INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts`

4. **WORKSPACE PATH BOUNDARY & MULTI-REPO CONSTRAINTS:**
   - **Absolute Root Directory Rule:** The true workspace root is permanently fixed at the project root `./`. You MUST never use relative paths that assume a sub-module or microservice directory is the root. Generating file paths directly under the repository root (e.g., `./Dockerfile` or `./ci.yml`) is strictly BANNED. Every path MUST start with `./sources/`.
   - **Strict Sub-folder Prefixing (Topology-Aware):** Every single `Target Path` generated MUST strictly start with either `./sources/backend/...`, `./sources/frontend/...`, or `./sources/infra/...` based exclusively on the active topology and assigned agent. If the project is Backend-Only, you are STRICTLY BANNED from generating frontend paths.

# [CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule
# This rule applies ONLY if a file path targets a Java source or test component (.java).
# For all non-Java projects, this specific block MUST be skipped entirely.
- **Calculated Lowercase Token Rule:** To compute the package layouts, you MUST strictly apply a deterministic regex execution pattern: Remove all non-alphanumeric characters, strip out whitespaces, underscores, hyphens, and force-convert the remaining string token entirely into 100% pure lowercase alphanumeric characters.
- The path under `./sources/backend/` MUST strictly contain the directory segment: `/org/nlh4j/saas/<calculated_lowercase_token>/`.

- **Deterministic Security Embedding:** Every engineering task for coder and reviewer agents must explicitly inject OWASP compliance parameters (multi-tenancy `tenant_id` scopes, AES-256 application-layer PII encryption, or parameterized queries) directly into the task's technical design instruction if that component handles data, authentication, or query compilation.

# COMPLIANCE MANDATES AND CRITICAL CONSTRAINTS (ABSOLUTE)
1. **Strict Content Purity:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought markdown segments, reasoning explanations, or notes.
2. **Direct Output Mandate:** Start the output response IMMEDIATELY with the primary title text `# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}`. Do NOT wrap the entire response inside any markdown codeblocks (no ` ```markdown ` wrapping). Any conversational filler text, greetings, or reasoning logs before or after this markdown structure will result in an immediate application pipeline failure.

Your output MUST follow this exact Markdown layout structure:

# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}

## 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase {{ phase_idx }}]

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and project stack. Every directory matrix path must be bounded under `./sources/`]

## 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, incorporating the specialized 'doc' agent role for full technical documentation compilation, and 'reviewer' for single file static/compiler analysis inside `./sources/`. You are absolutely banned from referencing un-authorized agents like 'Manager']

## 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards and complete functional test coverage for the allocated requirements]

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY [X]: [CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]
[INSTRUCTION: Evaluate the current target phase requirements. Stop generating daily logs immediately when objectives are met; do not pad days. Generate sub-tasks dynamically using ONLY the minimum required authorized agent tokens ('coder' | 'tester' | 'reviewer' | 'doc' | 'docker' | 'GCP' | 'GKE') to fulfill that day's objective. If a day requires only N sub-tasks, generate exactly N sub-task blocks. You are STRICTLY BANNED from generating placeholder, duplicate, or empty tasks. Follow the structural syntax for Sub-Tasks below iteratively for each valid sub-task on this day:]

#### SUB-TASK [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
##### Assigned Sub-Agent: [Insert exactly ONE unique literal Agent token: coder | tester | reviewer | doc | docker | GCP | GKE]
##### Targeted Components & Technical Requirements:
* **Target Path:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax adhering strictly to the constraints. If 'reviewer', path must target a single code file, never a folder.]
* **Architectural Requirements:**
  * [Explicit technical design rule, framework-specific convention, or implementation instruction]
  * [Explicit security enforcement parameter, e.g., OWASP A01/A02 implementation rule if handling data entry or state changes]
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [You MUST explicitly list the exact inherited BA Tag IDs that this specific sub-task implements or verifies. Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`. You are STRICTLY BANNED from leaving this field blank, using placeholder text like "N/A"/"None", using ranges like `[REQ-001...005]`, or inventing new tags not found in the raw requirements reference.]
