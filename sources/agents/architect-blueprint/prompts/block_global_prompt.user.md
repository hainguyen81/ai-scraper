Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project '{{ project_name }}'.

--- RAW REQUIREMENTS ---
{{ project_requirements }}
--- END REQUIREMENTS ---

# 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

#### 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "{{ project_name }}" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= {{ num_phases }}) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of {{ max_days_per_phase }} days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than {{ num_phases }} phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
# STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= {{ num_phases }}). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of {{ max_days_per_phase }} days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to {{ max_days_per_phase }} is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}.
<!--END_DELIMITTER-->

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`#`, `##`, `###`, `####`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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
