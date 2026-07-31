Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project '{{ project_name }}'.

--- RAW REQUIREMENTS ---
{{ project_requirements }}
--- END REQUIREMENTS ---

# 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

#### 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `..sources.backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `..sources.backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `..sources.frontend.` (or `..sources.frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `..sources.infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `..sources.`.

#### 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of {{ num_phases }} phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of {{ max_days_per_phase }} days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('coder' | 'tester' | 'reviewer' | 'doc' | 'docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

#### 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
Every header and table parameter below MUST be translated and naturally rendered into "{{ language }}", except for the explicit Technical English core tokens protected by system mandates. You MUST include every single section below without exception to satisfy enterprise compliance requirements:

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

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `..`. All paths generated MUST begin with `..sources.`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "{{ project_name }}" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `..sources.`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
# Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. (Maximum allowed limit ceiling: {{ num_phases }} phases). Each row MUST specify a calendar duration strictly bounded between 1 to {{ max_days_per_phase }} days maximum. Do NOT generate empty rows or placeholder steps if the BA scope has been fully covered.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
# You MUST exhaustively detail EVERY single active phase generated in Section 4. 
# For EACH active phase, you MUST provide deep, production-ready implementation specifications matching the full granularity of the raw requirements, broken down into single isolated days from DAY 1 up to the dynamic freeze day (Maximum ceiling limit: {{ max_days_per_phase }} days per phase). No day ranges or empty padding allowed.

### 🔹 Phase [X] Detailed Architectural Specification
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `..sources.` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system fallback logic states handled under this phase.
- **Enterprise Business Core Code Sample:** Provide high-fidelity, non-blocking asynchronous domain source code snippets using standard enterprise idioms matching the detected stack framework to guide the implementation layer.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Maximum ceiling limit: {{ max_days_per_phase }} Days per phase)
# Enforce the 'Longitructural Day Partitioning' and 'Anti-Padding Mandate' rules. Output each active day as an isolated standalone single integer subsection header. Freeze and terminate immediately once all BA tracking codes mapped to this phase are fully covered.

#### 🗓️ DAY [Y]: [CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]
- **Sub-Agent Workflow Specialization:**
  * **[Assigned Sub-Agent literal token: coder | tester | reviewer | doc | docker | GCP | GKE]:**
    - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `..sources.` or Tester pair syntax. Append its corresponding Tag IDs inline here, e.g., `..sources.backend.... [REQ-001], [DAT-002]`]
    - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters mapping 1:1 to the requirements and attaching Tag IDs]
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
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-day-X`.
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE
Immediately at the absolute end of the document text, you MUST print a strict mathematical traceability verification text block by parsing and counting every unique tag string present in your output:
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`
