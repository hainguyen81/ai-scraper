### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
# GLOBAL DYNAMIC TRANSLATION MANDATE:
- You MUST naturally translate and render every single section header (from Section 1 to Section 8), table parameters, column names, and descriptive text below into "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
- Do NOT leave any layout headers, item keys, or bullet descriptions in English if a different language is specified.
- The ONLY elements permanently protected from translation are the technical syntax tokens specified in System Mandate 6 (e.g., pure code blocks, JSON/YAML, exact relative paths starting with `./sources/`, and Tag IDs).

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
[Translate this section header and provide a comprehensive technical overview in {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %} mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Translate this section header and detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures in {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}]

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Translate this key and detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks in {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}]
- **Frontend & Cross-Platform UI Mobile Stack:** [Translate this key and detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present in {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}]

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** [Translate rule name] The true repository workspace root is permanently fixed at the project root `..`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** [Translate rule name] Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** [Translate rule name] If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "{{ project_name }}" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** [Translate rule name] Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
[Translate this section header and table column headers into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}. Content inside the "Technical Deliverables Summary" column MUST be fully translated.]

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
# STRICT 1:1 SYNOPSIS MIRROR & LANGUAGE MANDATE:
- Section 5 headers and sub-headers MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= {{ num_phases }}).
- You MUST translate the Phase title, core objectives, Day log titles, and the "Low-Level Technical Task Instruction" entirely into "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}". Do NOT leave explanations in English.

<!--START_DELIMITTER-->
### Phase [X] Detailed Architectural Specification
- **Phase Core Objective & Purpose:** [Detailed technical explanation translated into the specified language]
- **Target Physical Directory Matrix Map:** [List paths in Technical English, but translate the layout description]
- **Database Schema DDL SQL Specification [DAT-XXX]:** [Keep raw valid DDL SQL in Technical English]
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** [Keep structural paths/JSON schema in Technical English, translate functional definitions]
- **Phase Localized Exception Handlers [EXC-XXX]:** [Translate business validation rules and error descriptions]
<!--END_DELIMITTER-->

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`#`, `##`, `###`, `####`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: [TRANSLATED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` in Technical English with its Tag IDs inline]
      - **Low-Level Technical Task Instruction:** [Exhaustive engineering instruction translated completely into the specified language, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
[Translate this section header and all bullet descriptions below entirely into the specified language]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
[Translate this section header and all bullet descriptions below entirely into the specified language]
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
[Translate this section header and all bullet descriptions below entirely into the specified language]
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-day-X`.
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.
