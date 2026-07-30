# AI Model: llama-3.3-70b-versatile - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
None
--- END REQUIREMENTS ---

## 🛑 CRITICAL ENTERPRISE STRUCTURAL CONSTRAINTS (ABSOLUTE HARD LIMIT):
#### 1. EXACT PHASE COUNT MANDATE: You MUST segment the entire project architecture and development plan into EXACTLY 5 sequential phases. 
#### 2. NO MORE, NO LESS: Generating fewer than 5 phases or exceeding 5 phases is a critical engine failure. Under no circumstances are you allowed to create an extra phase beyond the designated count.
#### 3. POLYMORPHIC TECHSTACK & SCOPE ADAPTABILITY:
   - Dynamic Topology Mapping: Automatically detect the project architecture (Monolith, Microservices, Serverless, Data Pipeline, Embedded, Backend-only, Frontend-only, or Multi-platform) and the complete techstack (Node.js, Python, Go, Java, .NET, Rust, C++, etc.) from the raw requirements.
   - Conditional Component Enforcement: If a layer, component, or specific service type is absent from the requirements, you are STRICTLY BANNED from inventing dummy paths, placeholder modules, or fake architectural goals for that layer.
   - Granular Scope Distribution: Expand or compress technical tasks dynamically so they map logically and fit strictly within the 5 phases boundary without losing low-level structural details.
#### 4. CHRONOLOGICAL PACKING & ZERO REQUIREMENT OMISSION (STRICT TAG MAPPING): Every single requirement item and Tag ID (`[REQ-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`) specified in the raw documentation must be explicitly mapped, covered, and packed cleanly across these 5 phases. Every architectural task, database schema design, and interface implementation item generated within the phases MUST explicitly append the corresponding Tag ID in square brackets. No features, functions, or quality tags can be left unassigned or planned for post-phase execution. The final phase MUST represent a 100% feature-complete, production-ready, and security-hardened state.

## ⏳ CRITICAL TIMELINE BOUNDARY CONSTRAINTS (MANDATORY PHASE CALENDAR):
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs or design multi-phase overviews beyond Day 7 for any single phase.
#### 2. EFFICIENCY & ANTI-PADDING RULE (ZERO FILLER DAYS): Determine the realistic timeline based strictly on the technical complexity of the tasks. If a phase's core objectives are logically fulfilled in fewer than 7 days (e.g., 2 or 3 days), freeze the timeline for that phase immediately and move to the next phase. You are STRICTLY BANNED from generating repetitive logs, filler reviews, placeholder refactoring, "empty synchronization meetings", or artificial tasks to inflate the calendar. Every day allocated must yield raw code, test assets, deployment manifests, or structural documentation.

## 🔒 UNIVERSAL ENTERPRISE SECURITY & OWASP HARDENING RULES:
Translate and enforce these security mandates natively into the detected project techstack and programming language conventions:
- **A01:2021-Broken Access Control (Strict Multi-Tenancy Data Isolation):** Every database schema modification, native query, API route, or repository layer task MUST bake in implicit tenant filtering based on a discriminator column `tenant_id` (or equivalent multi-tenancy isolation model specified in requirements). Context must be derived securely from cryptographically verified auth claims at the API gateway or entry boundary. Cross-tenant data leakage is a catastrophic system failure.
- **A02:2021-Cryptographic Failures (PII Data Protection):** All highly sensitive Personal Identifiable Information (PII), specifically Citizen IDs, Phone Numbers, and financial transaction metadata, MUST be systematically encrypted at the application layer using enterprise-grade symmetric encryption (e.g., AES-256-GCM or equivalent native secure algorithm) before crossing the database persistence boundary. Raw PII must never be stored in plain text. Account passwords must be hashed using argon2id, bcrypt, or crypto-safe native equivalents.
- **A03:2021-Injection (Universal Injection Defense):** Standard string concatenation for dynamic query compilation, OS command execution, or script evaluation is strictly BANNED. Every system/database interaction must exclusively utilize parameter binding, named parameters, safe ORM queries, or prepared typed criteria builders.
- **A07:2021-Identification and Authentication Failures:** Multi-source authentication tokens (Internal JWT, Firebase, Google, Facebook OAuth2, API Keys) must undergo strict cryptographic signature and lease verification checks on every inbound API call. Expose token revocation and strict session expiration controls.

## 🔒 STRICT CONTENT PURITY & DIRECT OUTPUT MANDATE (NO SYSTEM FILLER):
#### 1. BANNED ELEMENTS: You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks, conversational filler texts, introductions (e.g., "Here is the blueprint..."), analysis logs, or notes like "Here is a thinking process", "Analyze User Input", or "Based on requirements...".
#### 2. EXPLICIT START MANDATE: Start the output response IMMEDIATELY with the primary title header text `## GLOBAL PROJECT CONTEXT: membership-hub`. Do NOT wrap the entire output inside any markdown codeblocks (no ` ```markdown ` wrapping). Any text, comment, or reasoning log before or after this exact markdown structure will cause an immediate execution pipeline crash.

Your output MUST follow this exact Markdown layout structure:

## GLOBAL PROJECT CONTEXT: membership-hub

#### 1. Executive Summary & Tech Stack Blueprint
[Provide a comprehensive enterprise tech stack blueprint and systemic baseline based on the provided raw requirements, explicitly defining the detected architecture topology and exact language/framework ecosystem choices]

#### 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. AI agents are strictly forbidden from emitting relative paths that assume a sub-module directory is the root.
- **Mandatory Path Subdirectory Rule (Absolute Hard Constraint):** Every single file path, configuration, script, diagram, or test asset generated across all prompts MUST be strictly placed inside the `./sources/` directory. Generating files directly under the repository root (e.g., `./Dockerfile`) is permanently BANNED.
- **Conditional Path Prefixing (Apply ONLY where applicable to the project topology):** 
  * All Backend service logics, microservices, configurations, database schemas, and backend tests must be prefixed with: `./sources/backend/` (If Microservices topology is detected, you MUST strictly use the alphanumeric lower-case service name from requirements as the sub-folder path, e.g., `./sources/backend/<service-name>/`).
  * All Frontend user interfaces, responsive views, mobile apps, state management packages, and client-side tests must be prefixed with: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple apps exist. Skip entirely if project is Backend-only).
  * For other project topologies (AI/Data, IoT, Embedded), paths must strictly map to logical root subdirectories matching the service domain under `./sources/`.
- **Java Enterprise Package Standard (Conditional - Apply ONLY to files with '.java' extension):** If the techstack utilizes Java/Quarkus/Spring, Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" by stripping out all whitespaces, hyphens, underscores, and special characters, transforming it into a strict pure alphanumeric lowercase token. This rule is STRICTLY BANNED from applying to non-Java languages.
- **Strict Package-to-Path Mapping (Conditional - Apply ONLY to files with '.java' extension):** All physical Java files under `./sources/backend/src/main/java/` or `./sources/backend/src/test/java/` MUST follow the exact subdirectory layout matching the calculated lowercase token.
  * *Example Correct Path (if project name is "E-Commerce-App"):* `./sources/backend/src/main/java/org/nlh4j/saas/ecommerceapp/service/ReconciliationService.java`

- **Strict Tester Target Path Syntax (Polyglot Test Suites):** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST be absolute to the workspace and begin with `./sources/`.
  * *For Unit Testing:* Match the exact physical class/component file path with its corresponding unit test path (e.g., `./sources/backend/src/main/...;./sources/backend/src/test/...`).
  * *For Integration / E2E / UI Testing:* If no single source file is isolated, you MUST use the literal placeholder token `INTEGRATION_SCOPE` as the first parameter (e.g., `INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts`).
- **Memory, Ingestion, & Loop Constraints:** All generated code structures must strictly avoid runtime in-memory large dataset loops (for-loops over massive collections). Complex multi-dataset processing or multi-ledger matching must be delegated directly to native, indexed database relational operations (JOINs) or optimized stream-based bulk processes. Standard heavy DOM-mapping file-parsing tools are banned; event-driven stream-based parsing configurations (such as SAX/StAX model or stream-oriented high-throughput parsers native to the techstack) must be strictly implemented for high-throughput ingestion pipelines.

## 👥 STANDARDIZED SUB-AGENT PERSONA DEFINITIONS
You are STRICTLY FORBIDDEN from creating, inventing, or referencing any agent roles other than the 7 authorized tokens specified below. Multi-agent merging or external persona injection is a critical pipeline failure.
- **coder:** Owns the implementation of core functional features, business logic, framework initializations, components, and user interfaces localized strictly inside their multi-module subdirectories under `./sources/`. Never writes test frameworks or technical documents.
- **tester:** Owns full verification scope. Responsible for writing unit test code, automated suite structures, integration frameworks, running automated pipelines, and fixing tests if execution failures occur. Emits dual-path semi-colon syntax for units under `./sources/`.
- **reviewer:** Performs strict static code analysis, validates multi-tenancy context isolation, reviews security compliance (OWASP metrics), checks for compiler diagnostics/errors, and auto-patches/fixes source or test code files directly under `./sources/`.
- **doc:** Responsible exclusively for generating, formatting, or updating technical document files, architectural artifacts, business workflows, system workflows, database diagrams, and product specification layouts. All generated document files must strictly reside in enterprise paths under `./sources/`.
- **docker:** Responsible exclusively for writing multi-stage, secure container configurations (e.g., Dockerfile), managing multi-stage compilation within containers, building optimized docker images, and configuring workflows to push artifacts to Docker Hub. Banned from writing application logic.
- **GCP:** Responsible for managing Google Cloud Platform resource layouts, identity access structures (IAM roles), cloud storage buckets, container registry connections, and automated cloud infrastructure provisioning pipelines under `./sources/`.
- **GKE:** Responsible for Kubernetes cluster orchestrations, writing deployment manifests, defining service routings, configuring cluster ingress parameters, and automating operational workloads inside GKE layouts.

## 📈 MULTI-PHASE SEGMENTATION STRATEGY OVERVIEW (Plan exactly 5 phases)
- You MUST divide and allocate 100% of the raw project requirements into exactly 5 sequential phases.
- **STRICT PHASE CALENDAR MANDATE (CRITICAL):** Each phase outlined in this overview MUST be planned to be completed within a duration strictly bounded between 1 to 7 days max. You are ABSOLUTELY FORBIDDEN from assigning a duration greater than 7 days to any phase.
- You MUST provide an architectural synopsis grid mapping which component features go into which phase. 

#### 3. High-Level Multi-Phase Architectural Synopsis Grid
You MUST generate a strict, highly detailed Markdown Table mapping the exact distribution of components and requirements across the 5 phases. 

###### 🛑 STRICT FORMATTING RULES FOR TAG IDS (ZERO TOLERANCE):
1. **NO TAG BUNDLING/RANGES:** You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`, NO `[REQ-001...005]`, NO `[REQ-All]`). Every single tag must be written out individually and separated by commas (e.g., `[REQ-001], [REQ-002], [REQ-003]`).
2. **NO INVENTED TAGS:** Every Tag ID listed in the table MUST exist in the "RAW REQUIREMENTS" input. Inventing fake IDs will crash the pipeline.
3. **MANDATORY FOR EVERY ROW:** Every single row inside the table MUST have at least one Tag ID. Leaving the "Targeted Tag IDs" column empty or putting placeholders like "N/A" or "None" is strictly prohibited.

| Phase | Day Range | Architectural Component / Module Path | Technical Task Details | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Phase 1` | `Day 1 - Day X` | `./sources/backend/...` | [Describe low-level engineering task, e.g., Initialize database context with multi-tenancy tenant_id schema] | `coder`, `doc` | `[REQ-001]`, `[ARC-001]` |
| `Phase 1` | `Day 1 - Day X` | `./sources/backend/...;./sources/backend/...` | [Write unit tests for tenant-isolation database validation queries] | `tester` | `[ARC-001]`, `[NFR-002]` |
| ... | ... | ... | ... | ... | ... |
| `Phase 5` | `Day Y - Day Z` | `./sources/` | [Execute complete multi-tenant leak audit and OWASP A02 PII application-layer encryption validation] | `reviewer` | `[NFR-002]`, `[EXC-003]` |
| `Phase 5` | `Day Y - Day Z` | INTEGRATION_SCOPE;./sources/infra/gke/ | [Deploy multi-stage Docker configurations to GKE cluster and map ingress routing rules] | `docker`, `GKE` | `[NFR-003]`, `[ARC-005]` |

###### 🛑 MATRIX COVERAGE CHECK MANDATE
Immediately following the table above, you MUST print a strict traceability verification text block. You must physically parse the requirements and count them accurately:
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]` 
(Replace X, Y, Z, W with the exact actual count of unique tags detected from the input documentation).

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```json
'NoneType' object has no attribute 'chat': ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 64, in generate_global_context
    response = client.chat.completions.create(
               ^^^^^^^^^^^
', "AttributeError: 'NoneType' object has no attribute 'chat'
"]
```

# AI Model: llama-3.3-70b-versatile - Phase 1 - Prompt:

Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**.
You must align perfectly with the established Global Context and satisfy a subset of the Raw Requirements.

--- GLOBAL CONTEXT REFERENCE ---

[ 🤖💬 WARN ] No need project global context, due to building plan spec!

--- RAW REQUIREMENTS REFERENCE ---
None
----------------------------------

## 🛑 ANTI-CREATIVE TAGGING & INHERITANCE MANDATE (CRITICAL):
1. You are STRICTLY BANNED from inventing, generating, or guessing any new Tag IDs. 
2. Every Tag ID you reference (`[REQ-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`) MUST be a 100% exact string match to the tags found inside the `--- RAW REQUIREMENTS REFERENCE ---` or `--- GLOBAL CONTEXT REFERENCE ---` sections. 
3. If a tag is not present in the input documentation, it DOES NOT EXIST. Do not create placeholder tags or secondary sequence systems.

## CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
#### 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to 7 days maximum (Absolute Hard Limit: Maximum 7 days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs or design multi-phase overviews beyond Day 7 for this phase.
#### 2. PROGRESSION STOPPING CRITERION (ZERO FILLER DAYS): Stop generating daily logs immediately once the core technical objectives allocated for this current Phase are satisfied. Do NOT duplicate, loop, or inject placeholder tasks (such as generic reviews, documentation padding, or empty syncs) just to inflate the calendar. If the technical work is logically complete on Day 1, freeze the output and exit immediately.

## EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE 1 into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY 7**.
2. **Strict Grouping Hierarchy:** 
   - **DAY LEVEL:** Group all activities belonging to that specific calendar day.
   - **AGENT SUB-TASK LEVEL:** Inside each Day, split work strictly by Sub-Tasks. **Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'coder' OR 'tester' OR 'reviewer' OR 'doc' OR 'docker' OR 'GCP' OR 'GKE'**. You are ABSOLUTELY BANNED from inventing external agent personas (e.g., 'Manager' or 'DevOps' are permanently banned).
   - **TARGET COMPONENT LEVEL:** Inside each Agent's Sub-Task, list **ALL Target Paths (Components)** that the designated Agent is responsible for creating, modifying, testing, or documenting on that day.

3. **STRICT TARGET PATH SYNTAX RULES FOR AGENTS:**
   - **For coder / doc / docker / GCP / GKE Agents:** Each component MUST be listed as a single relative file path string starting strictly with `./sources/`.
     *   *CRITICAL DOC AGENT RULE:* If the assigned agent is 'doc', the target path must represent an explicit documentation asset, business specification, flow architecture file, or diagram asset (e.g., `.md`, `.json`, `.puml`, `.drawio`) placed inside the dedicated documentation or module folders under `./sources/`.
   - **For reviewer Agent (Strict File Bound Rule):** The component MUST be a single, explicit physical code file path (e.g., ending with `.java`, `.go`, `.py`, `.ts`). You are STRICTLY BANNED from targeting a directory or parent folder path. The task must exclusively execute automated static code analysis, security linting, or compiler error fixes on that individual file.
   - **For tester Agent (Multi-Language Testing Context):** Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST be absolute to the workspace and begin with `./sources/`.
     *   **Rule for Unit Tests:** Match the exact physical path of the component class/file being tested with its corresponding test suite file under `./sources/`.
         *Example:* `**Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/ecommerceapp/service/OrderService.java;./sources/backend/src/test/java/org/nlh4j/saas/ecommerceapp/service/OrderServiceTest.java`
     *   **Rule for Integration / E2E / UI Tests (No single source file isolated):** You MUST use the literal string token `INTEGRATION_SCOPE` as the first parameter to signal that this test verifies multi-component workflows, cross-platform behaviors, or API network loops.
         *Example:* `**Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts`
4. **WORKSPACE PATH BOUNDARY & MULTI-REPO CONSTRAINTS:**
   - **Absolute Root Directory Rule:** The true workspace root is permanently fixed at the project root `./`. You MUST never use relative paths that assume a sub-module or microservice directory is the root. Generating file paths directly under the repository root (e.g., `./Dockerfile` or `./ci.yml`) is strictly BANNED. Every path MUST start with `./sources/`.
   - **Strict Sub-folder Prefixing (Topology-Aware):** Every single `Target Path` generated MUST strictly start with either `./sources/backend/...` or `./sources/frontend/...` based exclusively on the active topology defined in the Global Context. If the project is Backend-Only, you are STRICTLY BANNED from generating frontend paths. If it is Microservices, paths must strictly maintain sub-folder references under the precise lower-case alphanumeric service token inside `./sources/backend/`.
   - **Java Package Enforcement Rule (ONLY for '.java' files):** If and only if a file path targets a Java source or test component, you MUST calculate a pure lowercase alphanumeric representation of "membership-hub" (stripping spaces, dashes, special characters). The path under `./sources/backend/` MUST strictly contain the directory segment: `/org/nlh4j/saas/<calculated_lowercase_token>/`. Non-Java files (Go, Python, etc.) must NEVER contain this Java segment.
   - **Deterministic Security Embedding:** Every engineering task for coder and reviewer agents must explicitly inject OWASP compliance parameters (multi-tenancy `tenant_id` scopes, AES-256 application-layer PII encryption, or parameterized queries) directly into the task's technical design instruction if that component handles data, authentication, or query compilation.

## COMPLIANCE MANDATES AND CRITICAL CONSTRAINTS (ABSOLUTE)
1. **Strict Content Purity:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought markdown segments, reasoning explanations, or notes like "Here is a thinking process", "Analyze User Input", or "Based on requirements...". 
2. **Direct Output Mandate:** Start the output response IMMEDIATELY with the primary title text `## PHASE 1 CONTEXT BLUEPRINT: membership-hub`. Do NOT wrap the entire response inside any markdown codeblocks (no ` ```markdown ` wrapping). Any conversational filler text, greetings, or reasoning logs before or after this markdown structure will result in an immediate application pipeline failure.

Your output MUST follow this exact Markdown layout structure:

## PHASE 1 CONTEXT BLUEPRINT: membership-hub

#### 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase 1]

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and project stack. Every directory matrix path must be bounded under `./sources/`]

#### 3. Dedicated Sub-Agent Functional Directives (Specific tasks for coder, tester, reviewer, doc, docker, GCP, GKE)
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, incorporating the specialized 'doc' agent role for full technical documentation compilation, and 'reviewer' for single file static/compiler analysis inside `./sources/`. You are absolutely banned from referencing un-authorized agents like 'Manager']

#### 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards and complete functional test coverage for the allocated requirements]

#### 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

###### DAY [X]: [CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]
[INSTRUCTION: Evaluate the current target phase requirements. Stop generating daily logs immediately when objectives are met; do not pad days. Generate sub-tasks dynamically using ONLY the minimum required authorized agent tokens ('coder' | 'tester' | 'reviewer' | 'doc' | 'docker' | 'GCP' | 'GKE') to fulfill that day's objective. If a day requires only N sub-tasks, generate exactly N sub-task blocks. You are STRICTLY BANNED from generating placeholder, duplicate, or empty tasks. Follow the structural syntax for Sub-Tasks below iteratively for each valid sub-task on this day:]

######## SUB-TASK [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
########## Assigned Sub-Agent: [Insert exactly ONE unique literal Agent token: coder | tester | reviewer | doc | docker | GCP | GKE]
########## Targeted Components & Technical Requirements:
*   **Target Path:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax adhering strictly to the constraints. If 'reviewer', path must target a single code file, never a folder.]
    *   **Architectural Requirements:**
        *   [Explicit technical design rule, framework-specific convention, or implementation instruction]
        *   [Explicit security enforcement parameter, e.g., OWASP A01/A02 implementation rule if handling data entry or state changes]
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [You MUST explicitly list the exact inherited BA Tag IDs that this specific sub-task implements or verifies. Write each tag out individually separated by commas, e.g., `[REQ-001], [ARC-002]`. You are STRICTLY BANNED from leaving this field blank, using placeholder text like "N/A"/"None", using ranges like `[REQ-001...005]`, or inventing new tags not found in the raw requirements reference.]

# System Instruction

You are an Elite Solution Architect. Isolate development boundaries so sub-agents never overlap.

# Raw Response / Exception:

```json
'NoneType' object has no attribute 'chat': ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_phase.py", line 73, in generate_phase_contexts
    response = client.chat.completions.create(
               ^^^^^^^^^^^
', "AttributeError: 'NoneType' object has no attribute 'chat'
"]
```

