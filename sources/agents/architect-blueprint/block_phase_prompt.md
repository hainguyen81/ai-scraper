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

Your output MUST follow this exact Markdown structure for Phase {{ phase_idx }}:
# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}
## 1. Phase Operational Scope & Objectives
## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
## 4. Phase Definition of Done (DoD)
## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY [X]: [SHORT CAPITALIZED SPECIFIC OBJECTIVE NAME]

#### SUB-TASK [X.1]: [Short description of work for the Agent]
##### Assigned Sub-Agent: [Insert exactly ONE Agent: Coder OR Tester OR DevOps OR Reviewer]
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `[Relative path to file/endpoint 1, e.g., ./src/.../OrderController.java]`
    *   **Architectural Requirements:**
        *   [Rule 1: Detailed functional logic for this component]
        *   [Rule 2: Expected input/output, validations, or constraints]
*   **Target Path 2:** `[Relative path to file/endpoint 2, e.g., ./src/.../OrderService.java]`
    *   **Architectural Requirements:**
        *   [Rule 1: Business logic mapping, database interaction rules]
        *   [Rule 2: Inter-dependency or sync logic linking with Target Path 1]

#### SUB-TASK [X.2]: [Next sub-task for a DIFFERENT Agent on the same day, if applicable]
##### Assigned Sub-Agent: [Insert exactly ONE Agent, e.g., Tester]
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `[Relative path to test file, e.g., ./src/test/.../OrderControllerTest.java]`
    *   **Architectural Requirements:**
        *   [Rule 1: Specific unit testing instructions, mock configurations]

