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

# ⏳ EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE {{ phase_idx }} into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY {{ max_days_per_phase }}**.
2. **Strict Grouping Hierarchy:** 
   - **DAY LEVEL:** Group all activities belonging to that specific calendar day.
   - **AGENT SUB-TASK LEVEL:** Inside each Day, split work strictly by Sub-Tasks. **Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent** (e.g., Coder, Tester, Reviewer, DevOps) who owns that specific execution context.
   - **TARGET COMPONENT LEVEL:** Inside each Agent's Sub-Task, list **ALL Target Paths (Components)** that the designated Agent is responsible for creating, modifying, or testing on that day.
3. **STRICT TARGET PATH SYNTAX RULES FOR AGENTS:**
   - **For CODER / DEVOPS / REVIEWER Agents:** Each component MUST be listed as a single relative file path.
     *Example:* `Target Path: ./sources/backend/src/main/java/.../OrderService.java`
   - **For TESTER Agent (JUnit / Integration Testing Context):** Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by junit>;<source junit file to test>`.
     *   **Rule for Unit Tests:** Use the exact physical path of the class being tested.
         *Example:* `./sources/backend/src/main/java/.../OrderService.java;./sources/backend/src/test/java/.../OrderServiceTest.java`
     *   **Rule for Integration / E2E Tests (No single source file):** You MUST use the literal string `INTEGRATION_SCOPE` as the first parameter to signal that this test verifies multi-component behaviors or API endpoints.
         *Example:* `INTEGRATION_SCOPE;./sources/backend/src/test/java/.../ReconciliationIntegTest.java`

Your output MUST follow this exact Markdown structure for Phase {{ phase_idx }}:
# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}
## 1. Phase Operational Scope & Objectives
## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
## 4. Phase Definition of Done (DoD)
## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY [X]: [SHORT CAPITALIZED SPECIFIC OBJECTIVE NAME]

#### SUB-TASK [X.1]: [Short description of work for the Agent]
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `[Relative path to source file, e.g., ./src/main/java/.../ReconciliationService.java]`
    *   **Architectural Requirements:**
        *   [Rule 1: Detailed functional logic for this component]

#### SUB-TASK [X.2]: [Next sub-task for the Tester Agent - Unit Testing Scenario]
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/com/saas/recon/service/ReconciliationService.java;./sources/backend/src/test/java/com/saas/recon/service/ReconciliationServiceTest.java`
    *   **Architectural Requirements:**
        *   [Rule 1: Specify exact JUnit 5 / Mockito constraints to verify the paired source file]
        *   [Rule 2: Boundary test cases required (e.g., handling Empty Excel rows, Null values)]

#### SUB-TASK [X.3]: [Next sub-task for the Tester Agent - Integration Testing Scenario]
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `INTEGRATION_SCOPE;./sources/backend/src/test/java/com/saas/recon/integration/ReconciliationIntegTest.java`
    *   **Architectural Requirements:**
        *   [Rule 1: Setup full context integration test using SpringBootTest and Testcontainers]
        *   [Rule 2: Validate end-to-end HTTP Rest API endpoints and native database state transitions]

