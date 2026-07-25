# AI Model: llama-3.3-70b-versatile - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'autosellhub-automation'.

--- RAW REQUIREMENTS ---
#### 1. PROJECT OVERVIEW
- Product Objectives & Core Values
   - Tối ưu hoá giá bán dựa trên AI, đồng bộ tồn kho thời gian thực, lên lịch quảng cáo đa kênh.
   - Đảm bảo sự đơn giản, hiệu quả, bảo mật.
- Target User Personas
   - Chủ shop nhỏ (1-10 SKU), người mới bắt đầu, startup thương mại điện tử.
- Role-Based Access Control (RBAC) Matrix
   - Admin: Quản lý hệ thống, cấu hình kênh, xem báo cáo.
   - Merchant: Quản lý sản phẩm, giá, chiến dịch, xem KPI.
   - Analyst: Xem báo cáo chi tiết, xuất dữ liệu.

#### 2. FUNCTIONAL REQUIREMENTS
**Epic Module: Autonomous Pricing Engine**
- Feature: AI Pricing Suggestion
   - User Story: As a Merchant I want to receive daily suggested price ranges for each SKU so that I can stay competitive.
   - Acceptance Criteria:
     Given the system has been seeded with competitor data for the last 7 days, when the pricing engine runs at 03:00 AM, then the system should generate price suggestions within 30 seconds and store them in the database.
   - Data Inputs & Field Validations:
     - SKU_ID (string, not null, uuid), Current_Price (decimal, >=0), Competitor_Prices (array of decimal, length >=1), Demand_Score (decimal, 0-1).

**Epic Module: Inventory Sync**
- Feature: Real-Time Stock Sync
   - User Story: As a Merchant I want the inventory levels to sync automatically from my ERP/API so that I never oversell.
   - Acceptance Criteria:
     Given the ERP pushes a stock update payload, when the webhook is received, then the system updates the SKU stock within 5 seconds and logs the change.
   - Data Inputs & Field Validations:
     - SKU_ID, Stock_Quantity (int, >=0), Updated_At (datetime, UTC).

**Epic Module: Advertising Scheduler**
- Feature: Drag‑and‑Drop Campaign Builder
   - User Story: As a Merchant I want to drag and drop ad creatives into a timeline so that I can schedule posts across Instagram, Facebook, and Google Shopping.
   - Acceptance Criteria:
     Given a campaign timeline layout, when the user drops an image, then the system validates the image size (<5MB) and schedule time (>=current time), stores the plan, and triggers API calls at scheduled time.
   - Data Inputs & Field Validations:
     - Campaign_ID, Platform (enum), Creative_File (image/jpeg/png), Start_Time, End_Time, Target_Audience (json).

**Epic Module: User Management**
- Feature: OAuth2 + MFA
   - User Story: As an Admin I want to enforce MFA for all users so that the system remains secure.
   - Acceptance Criteria:
     Given a user in state 'PENDING_MFA', when the user completes MFA, then the account is set to ACTIVE and access token is issued.
   - Data Inputs & Field Validations:
     - User_ID Mik, Email, Password (hashed, bcrypt), Phone_Number (E.164), MFA_Method (sms/email).

**Epic Module: Analytics Dashboard**
- Feature: KPI Reporting
   - User Story: As a Merchant I want to view daily sales, conversion, and ROI metrics so that I can adjust strategies.
   - Acceptance Criteria:
     Given the last 30 days of data, when the dashboard loads, then it displays charts within 2 seconds and allows export to CSV.
   - Data Inputs & Field Validations:
     - Sale_Amount (decimal), Order_Count (int), Campaign_ID, Date.

#### 3. EXCEPTION FLOWS & EDGE CASES
- Network & Connectivity Drops
   - The system retries failed API calls up to 3 times with exponential backoff (1s, 2s, 4s). If still failing, queues the request in a durable queue for later.
- Invalid Inputs & Concurrency Issues
   - All inputs are validated server‑side; duplicate SKU updates are serialized via optimistic locking (version field). On conflict, return 409 Conflict.
- System Recovery & Error Notifications
   - Errors trigger alerts to DevOps via Slack & email; the system logs are stored in a central audit log.

#### 4. NON-FUNCTIONAL REQUIREMENTS
- Performance Metrics
   - API response time <= 200 ms for 95% of requests.
   - Pricing engine recomputes all SKUs within 5 minutes.
- Security
   - Data at rest encrypted with AES-256.
   - Token based auth (JWT) with 24h expiry, refresh tokens 30 days.
   - OWASP Top 10 controls: XSS, CSRF, Injection mitigated.
- Scalability & Availability
   - Auto‑scaling groups with min 2 nodes, max 10.
   - 99.9% uptime SLA, graceful failover across 2 AZs.

#### 5. PRELIMINARY DATA DICTIONARY
- **Table: Users**
   - user_id (UUID, PK, NOT NULL)
   - email (VARCHAR(255), UNIQUE, NOT NULL)
   - password_hash (VARCHAR(255), NOT NULL)
   - phone_number (VARCHAR(20))
   - role (ENUM('Admin','Merchant','Analyst'))
   - status (ENUM('ACTIVE','PENDING_MFA','INACTIVE'))
   - created_at (TIMESTAMP, NOT NULL)
- **Table: Products**
   - sku_id (UUID, PK, NOT NULL)
   - merchant_id (UUID, FK to Users, NOT NULL)
   - title (VARCHAR(255), NOT NULL)
   - description (TEXT)
   - price (DECIMAL(10,2), NOT NULL)
   - stock_quantity (INT, NOT NULL)
   - updated_at (TIMESTAMP, NOT NULL)
- **Table: Price_Suggestions**
   - suggestion_id (UUID, PK)
   - sku_id (UUID, FK, NOT NULL)
   - suggested_price (DECIMAL(10,2), NOT NULL)
   - confidence_score (DECIMAL(5,4) NOT NULL)
   - generated_at (TIMESTAMP, NOT NULL)
- **Table: Campaigns**
   - campaign_id (UUID, PK)
   - merchant_id (UUID, FK, NOT NULL)
   - platform (ENUM('Instagram','Facebook','GoogleShopping'))
   - status (ENUM('DRAFT','SCHEDULED','RUNNING','COMPLETED'))
   - start_time (TIMESTAMP, NOT NULL)
   - end_time (TIMESTAMP, NOT NULL)
   - creative_file (VARCHAR(255), NOT NULL)
   - target_audience (JSON)
   - created_at (TIMESTAMP, NOT NULL)
- **Table: Audits**
   - audit_id (UUID, PK)
   - user_id (UUID, FK)
   - action (VARCHAR(50), NOT NULL)
   - target_table (VARCHAR(50))
   - target_id (UUID)
   - payload (JSON)
   - timestamp (TIMESTAMP, NOT NULL)

--- END REQUIREMENTS ---

## 🛑 CRITICAL ENTERPRISE STRUCTURAL CONSTRAINTS (ABSOLUTE HARD LIMIT):
#### 1. EXACT PHASE COUNT MANDATE: You MUST segment the entire project architecture and development plan into EXACTLY 5 sequential phases. 
#### 2. NO MORE, NO LESS: Generating fewer than 5 phases or exceeding 5 phases is a critical engine failure. Under no circumstances are you allowed to create an extra phase beyond the designated count.
#### 3. POLYMORPHIC TECHSTACK & SCOPE ADAPTABILITY:
   - Dynamic Topology Mapping: Automatically detect the project architecture (Monolith, Microservices, Serverless, Data Pipeline, Embedded, Backend-only, Frontend-only, or Multi-platform) and the complete techstack (Node.js, Python, Go, Java, .NET, Rust, C++, etc.) from the raw requirements.
   - Conditional Component Enforcement: If a layer, component, or specific service type is absent from the requirements, you are STRICTLY BANNED from inventing dummy paths, placeholder modules, or fake architectural goals for that layer.
   - Granular Scope Distribution: Expand or compress technical tasks dynamically so they map logically and fit strictly within the 5 phases boundary without losing low-level structural details.
#### 4. CHRONOLOGICAL PACKING & ZERO REQUIREMENT OMISSION: Every single requirement item specified in the raw documentation must be explicitly mapped, covered, and packed cleanly across these 5 phases. No features or functions can be left unassigned or planned for post-phase execution. The final phase MUST represent a 100% feature-complete, production-ready, and security-hardened state.

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
#### 2. EXPLICIT START MANDATE: Start the output response IMMEDIATELY with the primary title header text `## GLOBAL PROJECT CONTEXT: autosellhub-automation`. Do NOT wrap the entire output inside any markdown codeblocks (no ` ```markdown ` wrapping). Any text, comment, or reasoning log before or after this exact markdown structure will cause an immediate execution pipeline crash.

Your output MUST follow this exact Markdown layout structure:

## GLOBAL PROJECT CONTEXT: autosellhub-automation

#### 1. Executive Summary & Tech Stack Blueprint
[Provide a comprehensive enterprise tech stack blueprint and systemic baseline based on the provided raw requirements, explicitly defining the detected architecture topology and exact language/framework ecosystem choices]

#### 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. AI agents are strictly forbidden from emitting relative paths that assume a sub-module directory is the root.
- **Mandatory Path Subdirectory Rule (Absolute Hard Constraint):** Every single file path, configuration, script, diagram, or test asset generated across all prompts MUST be strictly placed inside the `./sources/` directory. Generating files directly under the repository root (e.g., `./Dockerfile`) is permanently BANNED.
- **Conditional Path Prefixing (Apply ONLY where applicable to the project topology):** 
  * All Backend service logics, microservices, configurations, database schemas, and backend tests must be prefixed with: `./sources/backend/` (If Microservices topology is detected, you MUST strictly use the alphanumeric lower-case service name from requirements as the sub-folder path, e.g., `./sources/backend/<service-name>/`).
  * All Frontend user interfaces, responsive views, mobile apps, state management packages, and client-side tests must be prefixed with: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple apps exist. Skip entirely if project is Backend-only).
  * For other project topologies (AI/Data, IoT, Embedded), paths must strictly map to logical root subdirectories matching the service domain under `./sources/`.
- **Java Enterprise Package Standard (Conditional - Apply ONLY to files with '.java' extension):** If the techstack utilizes Java/Quarkus/Spring, Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "autosellhub-automation" by stripping out all whitespaces, hyphens, underscores, and special characters, transforming it into a strict pure alphanumeric lowercase token. This rule is STRICTLY BANNED from applying to non-Java languages.
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
- **The Phase Breakdown Strategy MUST follow this sequential complete packing alignment:**
  * **Incremental Feature Distribution:** Distribute and fully implement 100% of the core business logic, database schemas, state engines, microservices layouts, and application-layer code across the early and middle phases, ensuring total functional completeness prior to the final phase.
  * **The Final Phase:** The final phase under the exact total count of 5 is reserved strictly and exclusively for cross-system integration, performance profiling, automated multi-tenant leak validation, enterprise OWASP security verification, and complete production containerized/cloud deployment infrastructure configurations (docker/GCP/GKE manifests inside `./sources/`). At the end of this phase, zero requirement items from the input documentation must remain unexecuted or unbuilt.

#### 3. High-Level Multi-Phase Architectural Synopsis Grid
[Provide a markdown table mapping the exact distribution of components and requirements across the 5 phases, showing planned phase duration days and targeted sub-agents. Ensure tasks strictly match the detected project architecture layout and language stack. No placeholder, dummy, or empty tasks are allowed. Every task row must explicitly link back to its corresponding Raw Requirement item to guarantee 100% complete coverage at the completion of the final phase]

# System Instruction

You are an Elite Solution Architect. Define the global system truth and multi-agent guardrails.

# Raw Response / Exception:

```text
## GLOBAL PROJECT CONTEXT: autosellhub-automation

#### 1. Executive Summary & Tech Stack Blueprint
The autosellhub-automation project is a multi-tenant e-commerce platform that utilizes a microservices architecture. The tech stack consists of Node.js, Express.js, and MongoDB. The project requires a dynamic pricing engine, real-time inventory synchronization, and a drag-and-drop campaign builder for advertising. The system must ensure strict access control, data encryption, and compliance with OWASP security standards.

#### 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The repository workspace root is fixed at the project root `./`.
- **Mandatory Path Subdirectory Rule:** All files must be placed inside the `./sources/` directory.
- **Conditional Path Prefixing:** 
  * Backend services will be prefixed with `./sources/backend/`.
  * Frontend interfaces will be prefixed with `./sources/frontend/`.
- **Java Enterprise Package Standard:** Not applicable, as the project uses Node.js.
- **Strict Package-to-Path Mapping:** Not applicable, as the project uses Node.js.
- **Strict Tester Target Path Syntax:** Tester target paths will follow the semi-colon separated pair syntax.
- **Memory, Ingestion, & Loop Constraints:** The system will avoid runtime in-memory large dataset loops and utilize native database relational operations.

#### 3. High-Level Multi-Phase Architectural Synopsis Grid
The project will be divided into exactly 5 phases, with each phase strictly bounded between 1 to 7 days.

| Phase | Duration (Days) | Description | Sub-Agents |
| --- | --- | --- | --- |
| 1 | 3 | Implement dynamic pricing engine, database schema, and access control | coder, reviewer |
| 2 | 4 | Develop real-time inventory synchronization, campaign builder, and advertising scheduler | coder, tester |
| 3 | 2 | Implement user management, OAuth2 + MFA, and analytics dashboard | coder, reviewer |
| 4 | 3 | Integrate all components, perform cross-system testing, and validate performance | tester, reviewer |
| 5 | 5 | Deploy to production, configure containerized infrastructure, and perform security verification | docker, GCP, GKE |

The following requirements will be implemented in each phase:

* Phase 1:
	+ Epic Module: Autonomous Pricing Engine
	+ Epic Module: Inventory Sync (database schema)
	+ Role-Based Access Control (RBAC) Matrix
* Phase 2:
	+ Epic Module: Inventory Sync (real-time synchronization)
	+ Epic Module: Advertising Scheduler
	+ Epic Module: Campaign Builder
* Phase 3:
	+ Epic Module: User Management
	+ Epic Module: Analytics Dashboard
	+ OAuth2 + MFA
* Phase 4:
	+ Integrate all components
	+ Perform cross-system testing
	+ Validate performance
* Phase 5:
	+ Deploy to production
	+ Configure containerized infrastructure
	+ Perform security verification

The sub-agents will work together to ensure that all requirements are implemented and that the system is secure, scalable, and compliant with OWASP security standards.
```

