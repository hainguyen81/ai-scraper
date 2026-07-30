Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project '{{ project_name }}'.

--- RAW REQUIREMENTS ---
{{ project_requirements }}
--- END REQUIREMENTS ---

# 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

#### 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

#### 🗄️ PROTOCOL 2: Granular Low-Level Deliverables Per Phase
- For EACH individual phase from 1 to {{ num_phases }}, you MUST supply concrete technical layout specifications. This includes: physical directory database DDL SQL tables mapping to specific fields, explicit REST/Event API Payload Contracts, and concrete state-machine lifecycle matrices. Every phase must explicitly state exactly which requirements it fulfills.

#### 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

---

### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
Every header and table parameter below MUST be translated and naturally rendered into "{{ language }}", except for the explicit Technical English core tokens protected by system mandates:

# GLOBAL PROJECT CONTEXT: {{ project_name }}

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-{{ doc_id }} |
| **Project Name** | {{ project_name }} |
| **Version** | 1.0 (Baseline) |
| **Date/Time** | {{ current_timestamp }} |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. Architectural Alignment Summary & Tech Stack Baseline
- **Detected Technology Stack:** [List the exact languages, frameworks, and databases extracted from the requirements]
- **Architecture Pattern:** Distributed Event-Driven Architecture / Decoupled Hub Topology matching the requirements specifications.

## 📁 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All paths generated MUST begin with `./sources/`.
- **[CONDITION: JAVA_STACK_ONLY] Java Enterprise Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "{{ project_name }}" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 📈 3. High-Level Multi-Phase Architectural Synopsis Grid
# Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the {{ num_phases }} phases. Do NOT put long code snippets inside this table to prevent token compression.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 4. Granular Low-Level Phase Specializations & Technical Deliverables
# To completely eliminate AI laziness and truncation, you MUST exhaustively detail EVERY single one of the {{ num_phases }} phases discovered in Section 3 under this longitudinal text section. 
# For EACH phase, you MUST provide deep, production-ready implementation specifications matching the full granularity of the raw requirements:

### 🔹 Phase [X] Detailed Architectural Specification
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals]
- **Target Physical Directory Matrix:** List all specific file paths underneath `./sources/` initialized or modified in this phase, complying fully with the dynamic topology path prefixing rules. Every single line path generated MUST be appended with its tracking Tag IDs inline.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic and partitioning configurations).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system fallback logic states handled under this phase.

## 5. Global Non-Functional Requirements & Security Hardening [NFR-XXX]
- **Multi-Tenancy Isolation Strategy:** Concrete architectural mapping of how data isolation is enforced at runtime (e.g., `tenant_id` discriminator column routing or container namespace boundaries).
- **OWASP Hardening Protocols:** Specific configurations for SQLi parameter bindings, application-layer PII encryption, and secure asymmetric cryptographic token controls.

### 🛑 MATRIX COVERAGE CHECK MANDATE
Immediately at the absolute end of the document text, you MUST print a strict mathematical traceability verification text block by parsing and counting every unique tag string present in your output:
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`
