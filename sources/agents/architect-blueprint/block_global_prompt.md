Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project '{{ project_name }}'.

--- RAW REQUIREMENTS ---
{{ project_requirements }}
--- END REQUIREMENTS ---

# 🛑 CRITICAL ENTERPRISE STRUCTURAL CONSTRAINTS (ABSOLUTE HARD LIMIT):
## 1. EXACT PHASE COUNT MANDATE: You MUST segment the entire project architecture and development plan into EXACTLY {{ num_phases }} sequential phases. 
## 2. NO MORE, NO LESS: Generating fewer than {{ num_phases }} phases or exceeding {{ num_phases }} phases is a critical engine failure. Under no circumstances are you allowed to create an extra phase beyond the designated count.
## 3. POLYMORPHIC TECHSTACK & SCOPE ADAPTABILITY:
   - Dynamic Topology Mapping: Automatically detect the project architecture (Monolith, Microservices, Serverless, Data Pipeline, Embedded, Backend-only, Frontend-only, or Multi-platform) and the complete techstack (Node.js, Python, Go, Java, .NET, Rust, C++, etc.) from the raw requirements.
   - Conditional Component Enforcement: If a layer, component, or specific service type is absent from the requirements, you are STRICTLY BANNED from inventing dummy paths, placeholder modules, or fake architectural goals for that layer.
   - Granular Scope Distribution: Expand or compress technical tasks dynamically so they map logically and fit strictly within the {{ num_phases }} phases boundary without losing low-level structural details.
## 4. CHRONOLOGICAL PACKING & ZERO REQUIREMENT OMISSION: Every single requirement item specified in the raw documentation must be explicitly mapped, covered, and packed cleanly across these {{ num_phases }} phases. No features or functions can be left unassigned or planned for post-phase execution. The final phase MUST represent a 100% feature-complete, production-ready, and security-hardened state.

# ⏳ CRITICAL TIMELINE BOUNDARY CONSTRAINTS (MANDATORY PHASE CALENDAR):
## 1. STRICT PHASE DURATION LIMIT: Each individual Phase MUST be strictly bounded between 1 to {{ max_days_per_phase }} days maximum (Absolute Hard Limit: Maximum {{ max_days_per_phase }} days per phase). Under no circumstances are you allowed to invent, extrapolate, or generate scheduling logs or design multi-phase overviews beyond Day {{ max_days_per_phase }} for any single phase.
## 2. EFFICIENCY & ANTI-PADDING RULE (ZERO FILLER DAYS): Determine the realistic timeline based strictly on the technical complexity of the tasks. If a phase's core objectives are logically fulfilled in fewer than {{ max_days_per_phase }} days (e.g., 2 or 3 days), freeze the timeline for that phase immediately and move to the next phase. You are STRICTLY BANNED from generating repetitive logs, filler reviews, placeholder refactoring, "document maintenance", or artificial tasks to inflate the calendar. Every day allocated must yield raw code or test assets.

# 🔒 UNIVERSAL ENTERPRISE SECURITY & OWASP HARDENING RULES:
Translate and enforce these security mandates natively into the detected project techstack and programming language conventions:
- **A01:2021-Broken Access Control (Strict Multi-Tenancy Data Isolation):** Every database schema modification, native query, API route, or repository layer task MUST bake in implicit tenant filtering based on a discriminator column `tenant_id` (or equivalent multi-tenancy isolation model specified in requirements). Context must be derived securely from cryptographically verified auth claims at the API gateway or entry boundary. Cross-tenant data leakage is a catastrophic system failure.
- **A02:2021-Cryptographic Failures (PII Data Protection):** All highly sensitive Personal Identifiable Information (PII), specifically Citizen IDs, Phone Numbers, and financial transaction metadata, MUST be systematically encrypted at the application layer using enterprise-grade symmetric encryption (e.g., AES-256-GCM or equivalent native secure algorithm) before crossing the database persistence boundary. Raw PII must never be stored in plain text. Account passwords must be hashed using argon2id, bcrypt, or crypto-safe native equivalents.
- **A03:2021-Injection (Universal Injection Defense):** Standard string concatenation for dynamic query compilation, OS command execution, or script evaluation is strictly BANNED. Every system/database interaction must exclusively utilize parameter binding, named parameters, safe ORM queries, or prepared typed criteria builders.
- **A07:2021-Identification and Authentication Failures:** Multi-source authentication tokens (Internal JWT, Firebase, Google, Facebook OAuth2, API Keys) must undergo strict cryptographic signature and lease verification checks on every inbound API call. Expose token revocation and strict session expiration controls.

# 🔒 STRICT CONTENT PURITY & DIRECT OUTPUT MANDATE (NO SYSTEM FILLER):
## 1. BANNED ELEMENTS: You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks, conversational filler texts, introductions (e.g., "Here is the blueprint..."), analysis logs, or notes like "Here is a thinking process", "Analyze User Input", or "Based on requirements...".
## 2. EXPLICIT START MANDATE: Start the output response IMMEDIATELY with the primary title header text `# GLOBAL PROJECT CONTEXT: {{ project_name }}`. Do NOT wrap the entire output inside any markdown codeblocks (no ` ```markdown ` wrapping). Any text, comment, or reasoning log before or after this exact markdown structure will cause an immediate execution pipeline crash.

Your output MUST follow this exact Markdown layout structure:

# GLOBAL PROJECT CONTEXT: {{ project_name }}

## 1. Executive Summary & Tech Stack Blueprint
[Provide a comprehensive enterprise tech stack blueprint and systemic baseline based on the provided raw requirements, explicitly defining the detected architecture topology and exact language/framework ecosystem choices]

## 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. AI agents are strictly forbidden from emitting relative paths that assume a sub-module directory is the root.
- **Mandatory Path Subdirectory Rule (Absolute Hard Constraint):** Every single file path, configuration, script, or test asset generated across all prompts MUST be strictly placed inside the `./sources/` directory. Generating files directly under the repository root (e.g., `./Dockerfile`) is permanently BANNED.
- **Conditional Path Prefixing (Apply ONLY where applicable to the project topology):** 
  * All Backend service logics, microservices, configurations, database schemas, and backend tests must be prefixed with: `./sources/backend/` (If Microservices topology is detected, you MUST strictly use the alphanumeric lower-case service name from requirements as the sub-folder path, e.g., `./sources/backend/<service-name>/`).
  * All Frontend user interfaces, responsive views, mobile apps, state management packages, and client-side tests must be prefixed with: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple apps exist. Skip entirely if project is Backend-only).
  * For other project topologies (AI/Data, IoT, Embedded), paths must strictly map to logical root subdirectories matching the service domain under `./sources/`.
- **Java Enterprise Package Standard (Conditional - Apply ONLY if Techstack contains Java/Quarkus/Spring):** All source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.{{ project_name }}`.
- **Strict Package-to-Path Mapping (Conditional - Apply ONLY if Techstack contains Java/Quarkus/Spring):** This package structure dictates that all physical Java files under `./sources/backend/src/main/java/` or `./sources/backend/src/test/java/` MUST follow the exact subdirectory layout matching the package tokens.
  * *Example Correct Path:* `./sources/backend/src/main/java/org/nlh4j/saas/{{ project_name }}/service/ReconciliationService.java`
- **Strict Tester Target Path Syntax (Polyglot Test Suites):** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`.
  * *For Unit Testing:* Match the exact physical class/component file path with its corresponding unit test path (e.g., `./sources/backend/src/main/...;./sources/backend/src/test/...`).
  * *For Integration / E2E / UI Testing:* If no single source file is isolated (e.g., cross-component workflows, Kafka pipelines, API network loops, or UI flows), you MUST use the literal placeholder token `INTEGRATION_SCOPE` as the first parameter (e.g., `INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts`).
- **Memory, Ingestion, & Loop Constraints:** All generated code structures must strictly avoid runtime in-memory large dataset loops (for-loops over massive collections). Complex multi-dataset processing or multi-ledger matching must be delegated directly to native, indexed database relational operations (JOINs) or optimized stream-based bulk processes. Standard heavy DOM-mapping file-parsing tools are banned; event-driven stream-based parsing configurations (such as SAX/StAX model or stream-oriented high-throughput parsers native to the techstack) must be strictly implemented for high-throughput ingestion pipelines.

# 👥 STANDARDIZED SUB-AGENT PERSONA DEFINITIONS
Every task within the phases must be explicitly assigned to one of the following specialized sub-agents:
- **Manager Agent:** Oversees cross-phase orchestration, task timeline validation, architectural alignment, and signs off on the Definition of Done (DoD). Targets exclusively orchestration logs, markdown blue prints, or metadata definitions inside `./sources/`.
- **Coder Agent:** Owns the implementation of core features located strictly within the identified project architecture paths under `./sources/`. Never writes test frameworks.
- **Tester Agent:** Owns code verification. Responsible for emitting the dual-path semi-colon format (`<source>;<test>`) for units, or prefixing with `INTEGRATION_SCOPE` for system integration and automated UI/E2E test suites under the proper subdirectory under `./sources/`.
- **Reviewer Agent (Compiler Fixer):** Performs strict static analysis, validates compliance against security/multi-tenancy boundaries and database-native/language-native optimization rules, and acts as the automated compiler fixer to repair compilation logs (Auto-patching files directly under `./sources/`).
- **Docker Agent:** Responsible ONLY for writing multi-stage, secure container configurations (e.g., Dockerfile) localized exactly inside their workspace subdirectories under `./sources/`. Root-level Dockerfiles are strictly banned.
- **GCP Agent:** Responsible for Google Cloud Platform identity access management (IAM), cloud storage, and automated cloud resource provisioning setups under `./sources/`.
- **GKE Agent:** Responsible for Kubernetes orchestrations, writing deployment manifests, services, ingress configurations, and automated pipeline workflows under the enterprise layout inside `./sources/`.

# 📈 MULTI-PHASE SEGMENTATION STRATEGY OVERVIEW (Plan exactly {{ num_phases }} phases)
- You MUST divide and allocate 100% of the raw project requirements into exactly {{ num_phases }} sequential phases.
- **STRICT PHASE CALENDAR MANDATE (CRITICAL):** Each phase outlined in this overview MUST be planned to be completed within a duration strictly bounded between 1 to {{ max_days_per_phase }} days max. You are ABSOLUTELY FORBIDDEN from assigning a duration greater than {{ max_days_per_phase }} days to any phase.
- You MUST provide an architectural synopsis grid mapping which component features go into which phase. 
- **The Phase Breakdown Strategy MUST follow this sequential complete packing alignment:**
  * **Incremental Feature Distribution:** Distribute and fully implement 100% of the core business logic, database schemas, state engines, microservices layouts, and application-layer code across the early and middle phases, ensuring total functional completeness prior to the final phase.
  * **The Final Phase:** The final phase under the exact total count of {{ num_phases }} is reserved strictly and exclusively for cross-system integration, performance profiling, automated multi-tenant leak validation, enterprise OWASP security verification, and complete production containerized/cloud deployment infrastructure configurations (Docker/GCP/GKE manifests inside `./sources/`). At the end of this phase, zero requirement items from the input documentation must remain unexecuted or unbuilt.

## 3. High-Level Multi-Phase Architectural Synopsis Grid
[Provide a markdown table mapping the exact distribution of components and requirements across the {{ num_phases }} phases, showing planned phase duration days and targeted sub-agents. Ensure tasks strictly match the detected project architecture layout and language stack. No placeholder, dummy, or empty tasks are allowed. Every task row must explicitly link back to its corresponding Raw Requirement item to guarantee 100% complete coverage at the completion of the final phase]
