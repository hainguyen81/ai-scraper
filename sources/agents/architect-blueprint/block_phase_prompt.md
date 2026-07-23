Project Name: {{ project_name }}
You are tasked to detail **PHASE {{ phase_idx }} OUT OF {{ num_phases }}**.
You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

--- GLOBAL CONTEXT REFERENCE ---
{{ global_markdown_context }}

--- RAW REQUIREMENTS REFERENCE ---
{{ project_requirements }}
----------------------------------

# CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to {{ max_days_per_phase }} days maximum (Absolute Hard Limit: Maximum {{ max_days_per_phase }} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs or design multi-phase overviews beyond Day {{ max_days_per_phase }} for this phase.
## 2. PROGRESSION STOPPING CRITERION (ZERO FILLER DAYS): Stop generating daily logs immediately once the core technical objectives allocated for this current Phase are satisfied. Do NOT duplicate, loop, or inject placeholder tasks (such as generic reviews, documentation padding, or empty syncs) just to inflate the calendar. If the technical work is logically complete on Day 1, freeze the output and exit immediately.

# EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE {{ phase_idx }} into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY {{ max_days_per_phase }}**.
2. **Strict Grouping Hierarchy:** 
   - **DAY LEVEL:** Group all activities belonging to that specific calendar day.
   - **AGENT SUB-TASK LEVEL:** Inside each Day, split work strictly by Sub-Tasks. **Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent: 'Coder' OR 'Tester' OR 'Reviewer' OR 'Docker' OR 'GCP' OR 'GKE' OR 'Manager'** who owns that specific execution context.
   - **TARGET COMPONENT LEVEL:** Inside each Agent's Sub-Task, list **ALL Target Paths (Components)** that the designated Agent is responsible for creating, modifying, or testing on that day.
3. **STRICT TARGET PATH SYNTAX RULES FOR AGENTS:**
   - **For CODER / REVIEWER / DOCKER / GCP / GKE / MANAGER Agents:** Each component MUST be listed as a single relative file path string.
     *Example:* `**Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name }}/service/OrderService.java`
   - **For TESTER Agent (Multi-Language Testing Context):** Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`.
     *   **Rule for Unit Tests:** Match the exact physical path of the component class/file being tested with its corresponding test suite file under `./sources/`.
         *Example:* `**Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name }}/service/OrderService.java;./sources/backend/src/test/java/org/nlh4j/saas/{{ project_name }}/service/OrderServiceTest.java`
     *   **Rule for Integration / E2E / UI Tests (No single source file isolated):** You MUST use the literal string token `INTEGRATION_SCOPE` as the first parameter to signal that this test verifies multi-component workflows, cross-platform behaviors, or API network loops.
         *Example:* `**Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts`
4. **WORKSPACE PATH BOUNDARY & MULTI-REPO CONSTRAINTS:**
   - **Absolute Root Directory Rule:** The true workspace root is permanently fixed at the project root `./`. You MUST never use relative paths that assume a sub-module or microservice directory is the root. Generating file paths directly under the repository root (e.g., `./Dockerfile` or `./ci.yml`) is strictly BANNED. Every path MUST start with `./sources/`.
   - **Strict Sub-folder Prefixing (Topology-Aware):** Every single `Target Path` generated MUST strictly start with either `./sources/backend/...` or `./sources/frontend/...` based exclusively on the active topology defined in the Global Context. If the project is Backend-Only, you are STRICTLY BANNED from generating frontend paths. If it is Microservices, paths must strictly maintain sub-folder references under the precise lower-case alphanumeric service token inside `./sources/backend/`.
   - **Java Package Enforcement:** If the backend infrastructure utilizes Java/Quarkus/Spring, every single Java source or test file path under `./sources/backend/` MUST strictly match and contain the enterprise package layout directory segment: `/org/nlh4j/saas/{{ project_name }}/`.
   - **Deterministic Security Embedding:** Every engineering task for Coder and Reviewer agents must explicitly inject OWASP compliance parameters (multi-tenancy `tenant_id` scopes, AES-256 application-layer PII encryption, or parameterized queries) directly into the task's technical design instruction if that component handles data, authentication, or query compilation.

# COMPLIANCE MANDATES AND CRITICAL CONSTRAINTS (ABSOLUTE)
1. **Strict Content Purity:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought markdown segments, reasoning explanations, or notes like "Here is a thinking process", "Analyze User Input", or "Based on requirements...". 
2. **Direct Output Mandate:** Start the output response IMMEDIATELY with the primary title text `# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}`. Do NOT wrap the entire response inside any markdown codeblocks (no ` ```markdown ` wrapping). Any conversational filler text, greetings, or reasoning logs before or after this markdown structure will result in an immediate application pipeline failure.
Your output MUST follow this exact Markdown abstract layout structure for Phase {{ phase_idx }}:

# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}

## 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase {{ phase_idx }}]

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and project stack. Every directory matrix path must be bounded under `./sources/`]

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE, Manager)
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, incorporating the specialized 'Manager' agent role for high-level system orchestration and fallback validations inside `./sources/`]

## 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards and complete functional test coverage for the allocated requirements]

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY [X]: [CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]
[INSTRUCTION: Evaluate the current target phase requirements. Stop generating daily logs immediately when objectives are met; do not pad days. Generate sub-tasks dynamically using ONLY the minimum required agent tokens to fulfill that day's objective. If a day requires only N sub-tasks, generate exactly N sub-task blocks. You are STRICTLY BANNED from generating placeholder, duplicate, or empty tasks. Follow the structural syntax for Sub-Tasks below iteratively for each valid sub-task on this day:]

#### SUB-TASK [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules and tracing numbers from the raw documentation]
##### Assigned Sub-Agent: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Docker | GCP | GKE | Manager]
##### Targeted Components & Technical Requirements:
*   **Target Path:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax adhering strictly to the constraints]
    *   **Architectural Requirements:**
        *   [Explicit technical design rule, framework-specific convention, or implementation instruction]
        *   [Explicit security enforcement parameter, e.g., OWASP A01/A02 implementation rule if handling data entry or state changes]
