Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project '{{ project_name }}'.

--- RAW REQUIREMENTS ---
{{ project_requirements }}
--- END REQUIREMENTS ---

# CRITICAL ENTERPRISE STRUCTURAL CONSTRAINTS (ABSOLUTE HARD LIMIT):
## 1. EXACT PHASE COUNT MANDATE: You MUST segment the entire project architecture and development plan into EXACTLY {{ num_phases }} sequential phases. 
## 2. NO MORE, NO LESS: Generating fewer than {{ num_phases }} phases or exceeding {{ num_phases }} phases is a critical engine failure. Under no circumstances are you allowed to create a Phase {{ num_phases + 1 }}.
## 3. SCOPE COMPRESSION: If the project requirements are small, you MUST distribute and stretch the tasks to fit exactly {{ num_phases }} phases. If the requirements are massive, you MUST compress, aggregate, and streamline the architectural components so they fit strictly within the {{ num_phases }} phases boundary.
## 4. CHRONOLOGICAL PACKING: Every single requirement item specified in the documentation must be fully covered and packed cleanly across these {{ num_phases }} phases. Do not leave any loose ends or plan for post-phase execution.

# CRITICAL TIMELINE BOUNDARY CONSTRAINTS:
## 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to {{ max_days_per_phase }} days maximum (Absolute Hard Limit: Maximum {{ max_days_per_phase }} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs beyond Day {{ max_days_per_phase }}.
## 2. PROGRESSION STOPPING CRITERION: Stop generating immediately once the core technical objectives of the current Phase are satisfied. Do NOT duplicate or loop previous task structures just to inflate the timeline. If the work is complete on Day 1, freeze the output and exit.

# STRICT CONTENT PURITY & DIRECT OUTPUT MANDATE (NO SYSTEM FILLER):
## 1. BANNED ELEMENTS: You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks, conversational filler texts, introductions (e.g., "Here is the blueprint..."), analysis logs, or notes like "Here is a thinking process", "Analyze User Input", or "Based on requirements...".
## 2. EXPLICIT START MANDATE: Start the output response IMMEDIATELY with the primary title header text `# GLOBAL PROJECT CONTEXT: {{ project_name }}`. Do NOT wrap the entire output inside any markdown codeblocks (no ` ```markdown ` wrapping). Any text, comment, or reasoning log before or after this exact markdown structure will cause an immediate execution pipeline crash.

Your output MUST follow this exact Markdown layout structure:

# GLOBAL PROJECT CONTEXT: {{ project_name }}

## 1. Executive Summary & Tech Stack Blueprint
[Provide a comprehensive enterprise tech stack blueprint and systemic baseline based on the provided requirements]

## 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. AI agents are strictly forbidden from emitting relative paths that assume a sub-module directory is the root.
- **Mandatory Path Prefixing:** Every single directory path generated across all phases must strictly adhere to the following multi-module workspace boundaries:
  * All Java/Spring/Quarkus/Database logic, properties, and configurations must be prefixed with: `./sources/backend/`
  * All TypeScript/Tailwind/UI views, packages, and assets must be prefixed with: `./sources/frontend/`
- **Java Enterprise Package Standard:** All Java backend source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.{{ project_name }}`.
- **Strict Package-to-Path Mapping:** This package structure dictates that all physical Java files under `./sources/backend/src/main/java/` or `./sources/backend/src/test/java/` MUST follow the exact subdirectory layout matching the package tokens.
  * *Example Correct Path:* `./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name }}/service/ReconciliationService.java`
- **Strict Tester Target Path Syntax (JUnit & Integration):** Any component targeted by a Tester Sub-Agent must be structured as a semi-colon separated pair `<source_component>;<test_suite>`.
  * *For Unit Testing:* Match the exact physical class path with its unit test path (e.g., `./sources/backend/src/main/java/.../Service.java;./sources/backend/src/test/java/.../ServiceTest.java`).
  * *For Integration/E2E Testing:* If no single source file is isolated, you MUST use the literal placeholder token `INTEGRATION_SCOPE` as the first parameter (e.g., `INTEGRATION_SCOPE;./sources/backend/src/test/java/.../IntegTest.java`).
- **Memory & Loop Constraints:** All generated code structures must strictly avoid runtime in-memory large dataset loops (for-loops over large collections). Complex multi-dataset processing must be delegated to native, indexed database relational operations (JOINs). Standard heavy DOM-mapping file-parsing tools are banned; event-driven line-by-line streaming (SAX/EasyExcel) must be mandated.

## 3. Standardized Sub-Agent Persona Definitions
- **Manager Agent:** Responsible for cross-phase orchestration, task timeline validation, and checking that the total phase count is exactly {{ num_phases }}.
- **Coder Agent:** Owns the implementation of core features located strictly within `./sources/backend/src/main/` and `./sources/frontend/src/`. Never writes test frameworks.
- **Tester Agent:** Owns code verification. Responsible for emitting the dual-path semi-colon format (`<source>;<test>`) for units, or prefixing with `INTEGRATION_SCOPE` for system integration suites under `./sources/backend/src/test/`.
- **Reviewer Agent (Compiler Fixer):** Performs static analysis, validates compliance against database-native calculation rules, and acts as the automated compiler fixer/patcher to repair compilation logs.
- **Docker Agent:** Responsible ONLY for writing multi-stage, secure container configurations (e.g., Dockerfile) localized exactly inside their workspace subdirectories.
- **GCP Agent:** Responsible for Google Cloud Platform identity access management (IAM), cloud storage, and resource provisioning setups.
- **GKE Agent:** Responsible for Kubernetes orchestrations, writing deployment manifests, services, ingress configurations, and pipeline workflows under the enterprise layout.

## 4. Multi-Phase Segmentation Strategy Overview (Plan exactly {{ num_phases }} phases)
- You MUST outline a structural synopsis for exactly {{ num_phases }} phases.
- Each phase synopsis must preview the core architectural components that will be touched within `./sources/backend/` and `./sources/frontend/` respectively.
- Explicitly declare that no scheduling log within any subsequent phase generation is allowed to exceed Day {{ max_days_per_phase }}.
