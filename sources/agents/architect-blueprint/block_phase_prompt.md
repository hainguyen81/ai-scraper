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
   - **For CODER / REVIEWER / DOCKER / GCP / GKE Agents:** Each component MUST be listed as a single relative file path.
     *Example:* `**Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name_safe }}/service/OrderService.java`
   - **For TESTER Agent (JUnit / Integration Testing Context):** Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by junit>;<source junit file to test>`.
     *   **Rule for Unit Tests:** Use the exact physical path of the class being tested.
         *Example:* `**Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name_safe }}/service/OrderService.java;./sources/backend/src/test/java/org/nlh4j/saas/{{ project_name_safe }}/service/OrderServiceTest.java`
     *   **Rule for Integration / E2E Tests (No single source file):** You MUST use the literal string `INTEGRATION_SCOPE` as the first parameter to signal that this test verifies multi-component behaviors or API endpoints.
         *Example:* `**Target Path:** INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/{{ project_name_safe }}/integration/ReconciliationIntegTest.java`
4. **WORKSPACE PATH BOUNDARY & MULTI-REPO CONSTRAINTS:**
   - **Absolute Root Directory Rule:** The true workspace root is always the project root `./`. You MUST never use relative paths that assume the microservice directory is the root. Generating file paths directly under the repository root (e.g., `./Dockerfile`) is strictly BANNED.
   - **Strict Sub-folder Prefixing:** Every single `Target Path` generated MUST strictly start with either:
     *   `./sources/backend/...` (For all Java/Quarkus logic, source codes, pom.xml, configs, and tests)
     *   `./sources/frontend/...` (For all TypeScript/Tailwind/NextJS logic, package.json, and UI components)
   - **Multi-Stack Inclusion Rule:** For each Phase, you MUST evaluate both the Backend and Frontend requirements. Do NOT completely omit Frontend components if the raw requirements imply UI modifications or features for that phase.
   - **Java Package Enforcement:** Every single Java source or test file path under `./sources/backend/` MUST strictly match and contain the enterprise package layout directory segment: `/org/nlh4j/saas/{{ project_name_safe }}/`.

# COMPLIANCE MANDATES AND CRITICAL CONSTRAINTS (ABSOLUTE)
1. **Strict Content Purity:** You are ABSOLUTELY BANNED from including any internal thinking processes, markdown code blocks of thinking, chain-of-thought texts, or notes like "Here is a thinking process", "Analyze User Input", or "Based on requirements...". 
2. **Direct Output Mandate:** Start the output response IMMEDIATELY with the primary title text `# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}`. Do NOT wrap the entire output inside any markdown codeblocks (no ` ```markdown ` wrapping). Any conversational filler text, greetings, or reasoning logs before or after this markdown structure will result in an immediate pipeline failure.

Your output MUST follow this exact Markdown structure for Phase {{ phase_idx }}:
# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}
## 1. Phase Operational Scope & Objectives
## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE)
## 4. Phase Definition of Done (DoD)
## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY [X]: INITIAL ENVIRONMENT & PIPELINE SETUP

#### SUB-TASK [X.1]: Configure Enterprise Multi-Module Backend
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/pom.xml`
    *   **Architectural Requirements:**
        *   Define the core parent dependencies, Quarkus parent extensions, and Alibaba EasyExcel libraries.
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name_safe }}/rest/HealthResource.java`
    *   **Architectural Requirements:**
        *   Expose `/api/v1/health` endpoint returning server infrastructure multi-tenant state.

#### SUB-TASK [X.2]: Initialize Core Multi-Stage Container Setup
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/Dockerfile`
    *   **Architectural Requirements:**
        *   Build an optimized, multi-stage production container environment running Java 17 runtime layer.

#### SUB-TASK [X.3]: Execute Core Unit and Ingestion Suite
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name_safe }}/rest/HealthResource.java;./sources/backend/src/test/java/org/nlh4j/saas/{{ project_name_safe }}/rest/HealthResourceTest.java`
    *   **Architectural Requirements:**
        *   Assert response status `200` and verify the internal health checking state metrics.
