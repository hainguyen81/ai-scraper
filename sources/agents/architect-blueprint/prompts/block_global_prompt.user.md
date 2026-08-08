Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project '{{ project_name }}'.

--- RAW REQUIREMENTS ---
{{ project_requirements }}
--- END REQUIREMENTS ---

# 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

#### 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

#### 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of {{ num_phases }} phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of {{ max_days_per_phase }} days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

#### 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

#### 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

#### 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "{{ num_phases }}".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "{{ num_phases }}" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "{{ num_phases }}" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "{{ max_days_per_phase }}".
  * The actual number of days per phase can be LESS than or EQUAL to "{{ max_days_per_phase }}" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

#### 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}". Everything MUST be translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

#### 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`#`, `##`, `###`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `## 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `## 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %} while completely freezing all technical paths, tags, and block codes.
</RULE>

# GLOBAL PROJECT CONTEXT: {{ project_name }}

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-{{ doc_id }} |
| **Project Name** | {{ project_name }} |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | {{ current_timestamp }} |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "{{ project_name }}" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= {{ num_phases }}) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of {{ max_days_per_phase }} days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than {{ num_phases }} phases, terminate the matrix setup immediately at phase N.
- **LOCAL DAY RANGE BOUNDARY**: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: `Day 1 - 2`, Phase 2: `Day 1 - 2`). Compounding or running a linear progressive day count across phase boundaries (e.g., `Day 3 - 4` for Phase 2) is strictly prohibited.
- **🚨 DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic)**: Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. 
- If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2). If a phase contains high-density heavy tasks (e.g., combining Mobile UI, Chatbot AI, and DevOps simultaneously), you MUST expand its duration proportionally to smooth out the sub-task distribution, but under any circumstance, the calculated upper boundary MUST NOT exceed the absolute parameter ceiling of {{ max_days_per_phase }} days. Generating phantom filler days or trailing padding tasks is a fatal compliance breach.
- **🚨 IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE**: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens `<!--START_PHASE_SYNOPSIS_GRID-->` and `<!--END_PHASE_SYNOPSIS_GRID-->`.
- **🚨 DYNAMIC DAY TITLE ENFORCEMENT**: Inside Section 5, for every chronological day element (e.g., `- **Day [Y]**:`), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- **MANDATORY MULTI-AGENT SYNOPIS DISTRIBUTION LAW:** When generating rows for the summary matrix table, you ARE CRITICALLY FORBIDDEN from assigning only a single agent (like `Coder`) to any software delivery block. If the phase handles functional implementation paths (under `./sources/backend/` or `./sources/frontend/`), you MUST explicitly bundle `Tester`, `Doc`, and `Reviewer` alongside `Coder` inside the "Assigned Sub-Agent" column as a comma-separated list: `Coder, Tester, Doc, Reviewer`.
- **MANDATORY LIFECYCLE AGENT RESOURCE ALLOCATION LAW (ANTI-LAZINESS):** Inside Section 5 daily logs, you ARE CRITICALLY BANNED from leaving `[Coder]` as the solitary operating agent during development timelines. However, you MUST dynamically execute parallel or sequential resource distribution based strictly on the core technical nature of the targeted component to ensure compliance with the dynamic density ceiling. 
- **STRICT COMPONENT-BASED DISTRIBUTION PATTERNS:**
  1. *For Application Logic Layers (Backend/Frontend):* You MUST bundle `[Tester]`, `[Doc]`, and `[Reviewer]` alongside `[Coder]` within the daily sequence to enforce verification metrics, API contract formulation, and compilation verification gates.
  2. *For Infrastructure Layers (Docker/GCP/GKE Deployment):* If the target component belongs to infrastructure provisioning or containerization, you MUST immediately swap out application personas and exclusively allocate `[Docker]`, `[GCP]`, or `[GKE]` sub-agents within those specific daily segments. The corresponding descriptive instructions MUST explicitly mandate Dockerfile optimization, Terraform infrastructure scripts, or Kubernetes orchestration manifests.
- **STRICT PARALLEL LOG SCHEMAS:**
  1. *For Coder:* Deliver core engineering logic, entity models, and endpoint routing.
  2. *For Tester:* Force immediate initialization of validation assets. You MUST explicitly order the production of JUnit suites, Integration test matrices, and automated E2E test scripts on that exact same operational calendar day matching the coder architecture scope.
  3. *For Doc:* Force execution of document blueprints, technical manuals, and API specifications.
  4. *For Reviewer:* Operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections.
- **STRICT SEMI-COLON PAIR SYNTAX FOR TESTER:** Within the `target_component` field for any task block allocated to `Tester`, you MUST dynamically bifurcate the string format into exactly two structural validation use-cases using a raw semicolon delimiter:
  1. *Case 1 (Unit / JUnit Test Automation):* You MUST strict-couple the source file and the test file in the exact position: `<source_component_file_path>;<test_suite_file_path>`. The source file path MUST precede the semicolon. Both paths MUST start with `./sources/`.
  2. *Case 2 (Integration / End-to-End Automation):* If the test validation operates over an entire multi-module or system-wide layout where no single source file is isolated, you MUST strictly utilize the unaccented literal token `INTEGRATION_SCOPE` as the first parameter before the semicolon: `INTEGRATION_SCOPE;<target_test_suite_file_path>`. You are critically banned from prefixing or altering the `INTEGRATION_SCOPE` token.
- **SUPREME MULTI-AGENT COMPLIANCE & DISTRIBUTION LAW (9-CORE MANDATES):** You MUST execute 100% rigid adherence to the following lifecycle engineering distribution gates without any omission, padding, or contextual degradation:
  1. *Universal Adaptive Scope:* This orchestration engine MUST adapt natively to any tech stack or business requirements supplied via `{{ project_requirements }}`. Hardcoding specific domain logic is critically banned.
  2. *Strict Phase Partitioning:* The output lifecycle MUST be partitioned into exactly `{{ num_phases }}` distinct phases. No more, no less.
  3. *Hard Daily Ceilings:* The calendar allocation for any individual phase MUST NOT exceed `{{ max_days_per_phase }}` days.
  4. *Zero Filler Data / Ghost Logs:* You are strictly forbidden from inventing duplicate tasks, ghost metrics, filler actions, or extending day blocks artificially to pad the timeline. If the requirements are met, the index stops immediately.
  5. *Mandatory 7-Agent Allocation Matrix:* Every single phase workflow generated MUST distribute functional low-level tasks across all 7 operational personas: `[Coder]`, `[Tester]`, `[Reviewer]`, `[Doc]`, `[Docker]`, `[GCP]`, and `[GKE]`. Leaving any persona with zero tasks inside a phase is a critical compliance break.
  6. *Anti-Consolidation & Balanced Pacing:* Tasks MUST NOT be bulk-consolidated into a single day or single agent node. You MUST orchestrate the daily sequence linearly: App-development tasks (`[Coder]` and `[Doc]` initializing architecture, immediately reviewed by `[Reviewer]` for compilers, validated by `[Tester]` for JUnit/E2E) MUST run first, followed sequentially by infrastructure deployment logs (`[Docker]` containerizing components, `[GCP]` provisioning via Terraform scripts, `[GKE]` deploying cluster resource manifests) on the concluding days of the lifecycle.
  7. *Strict Tester Target Contract:* 100% of tasks allocated to `[Tester]` MUST follow Case 1 or Case 2 semi-colon string formatting precisely.
  8. *Enterprise-Grade Documentation Master:* The `[Doc]` agent MUST be explicitly assigned separate daily tasks to write comprehensive system blueprints, data structures, deployment protocols, and production-ready API specifications in clean localized markdown under `./sources/docs/`.
  9. *100% Tracing Matrix Coverage:* Every dynamic log and task row generated MUST map 100% of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- **STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW:** You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. *For [Coder] and [Reviewer]:* The `target_component` MUST strictly point to a physical executable source file ending with valid production extensions (e.g., `.java`, `.ts`, `.sql`).
  2. *For [Tester]:* The `target_component` MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., `.java`, `.ts`, `.spec.ts`) matching Case 1 or Case 2 patterns.
  3. *For [Doc]:* The `target_component` MUST permanently target granular, individual documentation files ending strictly with the `.md` extension, located inside `./sources/docs/`.
  4. *Markdown Render Integrity:* You ARE ABSOLUTELY BANNED from outputting naked triple backticks (` ``` `) for inner specifications (such as ` ```sql:matrix ` or ` ```json `) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (` ```` `) or five backticks (` ````` `) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- **ABSOLUTE DISCRETE DAY-LOG SEPARATION MANDATE:** You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Even if components intersect, you MUST output them as separate, independent, standalone list items inside that day's timeline to prevent downstream parser panics.
- **CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE:** The `[Reviewer]` MUST operate strictly in a sequential multi-step gating paradigm immediately following the `[Coder]` execution block. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- **GRANULAR DELIVERABLE CHECKLIST MANDATE:** You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. *For Tester:* Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. *For Doc:* Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
</RULE>

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

<!--START_PHASE_SYNOPSIS_GRID-->
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
# STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= {{ num_phases }}). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of {{ max_days_per_phase }} days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to {{ max_days_per_phase }} is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}.
</PHASE_TEMPLATE_LOOP>

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
    * **Sub-Agent Workflow Specialization:** <RULE>You MUST analyze the required daily task domain and output EXACTLY one single literal token code inside brackets representing the allocated persona: `[Coder]`, `[Tester]`, `[Reviewer]`, `[Doc]`, `[Docker]`, `[GCP]`, or `[GKE]`. You are CRITICALLY BANNED from outputting any English instructional placeholders or text descriptions like "Assigned Sub-Agent" or "literal token". Emitting anything other than the naked bracketed sub-agent code triggers an immediate failure.</RULE>
    * **Targeted Tag IDs:** <RULE>Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.</RULE>
    * **Target Component file path (`target_component`):** <RULE>Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`</RULE>
    * **Low-Level Technical Task Instruction:** <RULE>Output exhaustive, high-density engineering instructions, validation schemas, or API contract parameters fully translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}, attaching explicit Tag IDs.</RULE>
    
    # DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):  
    * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
      - You MUST actively check the active Sub-Agent for this DAY. If and ONLY IF the task involves database migrations, SQL, scripts, or persistence engines, you MUST dynamically generate the complete SQL blocks extracted STRICTLY INSIDE THE BOUNDARY OF THE ACTIVE PHASE. If the task is FrontendUI/DevOps/Testing and has NO database work, you MUST completely delete and eliminate this entire bullet point from the output buffer.
      - **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
      - You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
    </RULE>
    * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** <RULE>You MUST actively check the active Sub-Agent for this DAY. If and ONLY IF the task involves backend service microservices, route contracts, or event brokers, you MUST dynamically generate the endpoint JSON/WebSocket schemas extracted STRICTLY INSIDE THE BOUNDARY OF THE ACTIVE PHASE. If the task involves ONLY frontend components, containerization, or infrastructure, you MUST completely delete and eliminate this entire bullet point from the output buffer.</RULE>
    * **Phase Localized Exception Handlers [EXC-XXX]:** <RULE>You MUST actively check the active Sub-Agent for this DAY. If and ONLY IF the task contains explicit business validation boundaries or system exceptions, generate the handlers extracted STRICTLY INSIDE THE BOUNDARY OF THE ACTIVE PHASE. Otherwise, completely delete and eliminate this entire bullet point from the output buffer.</RULE>

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= {{ num_phases }}; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`
