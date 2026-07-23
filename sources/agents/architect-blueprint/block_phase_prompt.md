Project Name: {{ project_name }}
You are tasked to detail **PHASE {{ phase_idx }} OUT OF {{ num_phases }}**.
You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

--- GLOBAL CONTEXT REFERENCE ---
{{ global_markdown_context }}

--- RAW REQUIREMENTS REFERENCE ---
{{ project_requirements }}
----------------------------------

# CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to {{ max_days_per_phase }} days maximum (Absolute Hard Limit: Maximum {{ max_days_per_phase }} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day {{ max_days_per_phase }}.
## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

# EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE {{ phase_idx }} into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY {{ max_days_per_phase }}**.
2. **Strict Grouping Hierarchy:** 
   - **DAY LEVEL:** Group all activities belonging to that specific calendar day.
   - **AGENT SUB-TASK LEVEL:** Inside each Day, split work strictly by Sub-Tasks. **Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent: 'Coder' OR 'Tester' OR 'Reviewer' OR 'Docker' OR 'GCP' OR 'GKE'** who owns that specific execution context.
   - **TARGET COMPONENT LEVEL:** Inside each Agent's Sub-Task, list **ALL Target Paths (Components)** that the designated Agent is responsible for creating, modifying, or testing on that day.
3. **STRICT TARGET PATH SYNTAX RULES FOR AGENTS:**
   - **For CODER / REVIEWER / DOCKER / GCP / GKE Agents:** Each component MUST be listed as a single relative file path string.
     *Example:* `**Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name }}/service/OrderService.java`
   - **For TESTER Agent (JUnit / PyTest / Playwright Testing Context):** Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`.
     *   **Rule for Unit Tests:** Match the exact physical path of the component class/file being tested.
         *Example:* `**Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name }}/service/OrderService.java;./sources/backend/src/test/java/org/nlh4j/saas/{{ project_name }}/service/OrderServiceTest.java`
     *   **Rule for Integration / E2E / UI Tests (No single source file isolated):** You MUST use the literal string token `INTEGRATION_SCOPE` as the first parameter to signal that this test verifies multi-component workflows, cross-platform behaviors, or API network loops.
         *Example:* `**Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts`
4. **WORKSPACE PATH BOUNDARY & MULTI-REPO CONSTRAINTS:**
   - **Absolute Root Directory Rule:** The true workspace root is permanently fixed at the project root `./`. You MUST never use relative paths that assume a sub-module or microservice directory is the root. Generating file paths directly under the repository root (e.g., `./Dockerfile` or `./ci.yml`) is strictly BANNED.
   - **Strict Sub-folder Prefixing:** Every single `Target Path` generated MUST strictly start with either:
     *   `./sources/backend/...` (For all backend service logics, database schemas, framework configs, and tests)
     *   `./sources/frontend/...` (For all frontend UI views, web dashboards, state management packages, and client-side tests)
   - **Multi-Stack Inclusion Rule:** For each Phase, you MUST evaluate both the Backend and Frontend requirements. Do NOT completely omit Frontend components if the raw requirements imply UI modifications or multi-tenant layouts for that phase.
   - **Java Package Enforcement:** If the project uses Java for the backend stack, every single Java source or test file path under `./sources/backend/` MUST strictly match and contain the enterprise package layout directory segment: `/org/nlh4j/saas/{{ project_name }}/`.

# COMPLIANCE MANDATES AND CRITICAL CONSTRAINTS (ABSOLUTE)
1. **Strict Content Purity:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought markdown segments, reasoning explanations, or notes like "Here is a thinking process", "Analyze User Input", or "Based on requirements...". 
2. **Direct Output Mandate:** Start the output response IMMEDIATELY with the primary title text `# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}`. Do NOT wrap the entire response inside any markdown codeblocks (no ` ```markdown ` wrapping). Any conversational filler text, greetings, or reasoning logs before or after this markdown structure will result in an immediate application pipeline failure.

Your output MUST follow this exact Markdown abstract layout structure for Phase {{ phase_idx }}:

# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}

## 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement]

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase]

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE)
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase]

## 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully]

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY [X]: [CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]
[Dynamically evaluate the current target phase requirements. If the day targets backend development, generate sub-tasks utilizing 'Coder', 'Tester', or 'Reviewer' with components prefixed with './sources/backend/'. If the day targets frontend UI/App development, generate sub-tasks utilizing 'Coder' or 'Tester' with components prefixed with './sources/frontend/'. If the day targets containerization or infrastructure provisioning, invoke 'Docker', 'GCP', or 'GKE' agents accordingly. Do not invent fake service names; bind to the real repository domain.]

#### SUB-TASK [X.1]: [Clear, engineering description of the specific sub-task goal]
##### Assigned Sub-Agent: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Docker | GCP | GKE]
##### Targeted Components & Technical Requirements:
*   **Target Path:** [Insert explicit physical file path starting with ./sources/backend/ or ./sources/frontend/ matching the assigned agent syntax rules]
    *   **Architectural Requirements:**
        *   [Explicit technical design rule or instruction 1]
        *   [Explicit technical design rule or instruction 2]

#### SUB-TASK [X.2]: [Next sequential sub-task for a different Agent or Component on the same Day, if applicable]
##### Assigned Sub-Agent: [Insert exactly ONE unique literal Agent token]
##### Targeted Components & Technical Requirements:
*   **Target Path:** [Insert explicit physical path adhering strictly to workspace prefix and tester syntax rules]
    *   **Architectural Requirements:**
        *   [Explicit technical design rule or verification instruction]
