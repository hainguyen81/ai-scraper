<think>
Here's a thinking process:

1.  **Analyze User Input:**
   - **Project Name:** `test-ai-architecture` (context title), `membership-hub` (raw requirements)
   - **Task:** Detail **PHASE 2 OUT OF 5**
   - **Global Context & Raw Requirements:** Provided in the prompt. Key features: Web admin + Mobile app, Quarkus/Kafka/Postgres backend, scalable, Docker/GCP/GKE, Auth (internal + Firebase/Google/FB), Multi-tenant, QR attendance (idempotent daily), validity countdown, Notifications (Zalo phone/group + mobile push), Next.js frontend (mobile/web), i18n, SEO, locale detection.
   - **Required Output Structure:**
     ```
     # PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
     ## 1. Phase Operational Scope & Objectives
     ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
     ## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
     ## 4. Phase Definition of Done (DoD)
     ```
   - **Constraint:** "Isolate development boundaries so sub-agents never overlap." This is critical. I need to define strict boundaries for Phase 2, ensuring clear separation of concerns and preventing agent overlap.

2.  **Determine Phase 2 Focus:**
   Looking at the 5-phase strategy I mentally outlined earlier:
   - Phase 1: Foundation & Core Architecture (DB, Auth, Multi-tenant, Base Infra, Next.js/Quarkus scaffolding)
   - **Phase 2: Attendance & Business Logic Core** (QR generation/validation, daily deduplication/idempotency, validity countdown, Kafka event streams for attendance, core API endpoints)
   - Phase 3: Multi-Channel Notifications & i18n/SEO
   - Phase 4: Testing, Security & Optimization
   - Phase 5: Production Deployment & Observability
   This aligns perfectly. Phase 2 will focus on the core business logic: Attendance processing, QR handling, validity tracking, and the Kafka event pipeline that will later feed notifications. I'll strictly bound it to avoid overlapping with Auth (Phase 1), Notifications (Phase 3), and Deployment/Testing (Phases 4/5).

3.  **Draft - Section by Section:**

   *## 1. Phase Operational Scope & Objectives*
   - Focus: Core attendance engine, QR lifecycle, daily idempotency logic, membership validity countdown, and Kafka event publishing.
   - Objectives:
     - Implement idempotent daily attendance tracking per tenant/student.
     - Build QR generation & validation service with cryptographic signing.
     - Develop validity countdown logic (days remaining calculation).
     - Establish Kafka event schema & producers for attendance events.
     - Ensure strict multi-tenant data isolation for attendance records.
     - Deliver REST/gRPC endpoints for frontend consumption.
   - Boundaries: Explicitly exclude Auth implementation, Notification delivery, i18n/SEO, and Infrastructure deployment. These are handled in other phases.

   *## 2. Allowed Technical Scope & Directory Boundaries*
   - Need strict file/path/endpoint boundaries to prevent overlap.
   - Backend (Quarkus):
     - `src/main/java/com/membershiphub/attendance/` (Domain, Application, Infrastructure layers)
     - `src/main/java/com/membershiphub/qr/` (QR generation/validation)
     - `src/main/java/com/membershiphub/events/` (Kafka producers, DTOs)
     - `src/main/resources/db/migration/V2__attendance_schema.sql`
     - Endpoints: `POST /api/v1/attendance/check-in`, `GET /api/v1/attendance/{studentId}/status`, `GET /api/v1/qr/generate`
   - Frontend (Next.js):
     - `src/app/(mobile)/attendance/` (Pages/components for QR scan & countdown display)
     - `src/app/(admin)/dashboard/attendance/` (Admin view)
     - `src/services/attendance.service.ts`
     - `src/components/qr-scanner/`
   - Kafka:
     - Topic: `membership.attendance.events`
     - Schema: `AttendanceEvent` (tenantId, studentId, timestamp, status, validityRemaining)
   - Explicit Exclusions: Auth routes, Notification services, i18n config, Dockerfiles, GKE manifests, Test suites (handled by other agents/phases).

   *## 3. Dedicated Sub-Agent Functional Directives*
   - Need specific tasks for Coder, Tester, Reviewer, DevOps (Docker/Deployer combined or split as requested? The prompt says "Coder, Tester, Reviewer, DevOps". I'll stick to that).
   - **Coder:**
     - Implement Quarkus attendance service with JPA/Hibernate, ensuring tenant isolation via `@TenantId` or row-level security.
     - Build idempotency key mechanism (composite key: tenantId + studentId + date).
     - Develop QR payload structure (JWT-like signed token with studentId, tenantId, expiry).
     - Create Kafka producer for `membership.attendance.events`.
     - Implement Next.js attendance UI components (QR scanner, countdown display, API integration).
     - Strictly adhere to Clean Architecture & DDD boundaries.
   - **Tester:**
     - Design unit tests for idempotency logic, validity calculation, QR validation.
     - Create integration tests for Kafka event publishing & DB persistence.
     - Validate multi-tenant isolation (cross-tenant data leakage tests).
     - Mock external dependencies (Kafka, DB) for isolated testing.
     - Output: Test suite structure, coverage targets (>85%), test execution scripts.
   - **Reviewer:**
     - Audit code for DDD compliance, transaction boundaries, and idempotency guarantees.
     - Verify Kafka schema versioning & backward compatibility.
     - Check for N+1 queries, connection pooling, and tenant filtering enforcement.
     - Ensure frontend components follow Next.js App Router standards & accessibility.
     - Output: Review checklist, architectural compliance report, refactoring directives.
   - **DevOps (Docker/Deployer focus for Phase 2):**
     - Containerize Quarkus service with multi-stage Dockerfile.
     - Define Kafka topic provisioning scripts (Ansible/Terraform or GCP PubSub/Kafka bridge config).
     - Set up local development environment (Docker Compose: Postgres, Kafka, Quarkus, Next.js).
     - Output: `docker-compose.phase2.yml`, Dockerfile, environment variable templates, local run instructions.

   *## 4. Phase Definition of Done (DoD)*
   - Need clear, measurable criteria.
   - Functional: QR check-in works, idempotency enforced, countdown accurate, Kafka events published.
   - Technical: Code passes review, tests pass, Docker images build successfully, local env runs.
   - Compliance: Multi-tenant isolation verified, no auth/notification/i18n code mixed in, strict directory boundaries respected.
   - Documentation: API specs (OpenAPI), Kafka schema docs, local setup guide.
   - Sign-off: All sub-agents confirm completion, no cross-phase dependencies blocking Phase 3.

4.  **Refine & Self-Correction/Verification:**
   - *Check against constraints:* "Isolate development boundaries so sub-agents never overlap." -> I've explicitly defined allowed paths, endpoints, and excluded scopes. Each agent has distinct deliverables.
   - *Check structure:* Matches exactly the required Markdown structure.
   - *Check alignment with raw requirements:* Covers QR attendance, daily deduplication, validity countdown, Kafka events, Next.js frontend, Quarkus backend, multi-tenant isolation. Explicitly defers Auth, Notifications, i18n/SEO, GKE deployment to other phases.
   - *Technical depth:* Uses appropriate terminology (idempotency keys, DDD, Clean Architecture, Kafka schema, JWT-signed QR, Row-Level Security, multi-stage Docker, OpenAPI).
   - *Phase 2 focus:* Clearly positioned as the core business logic phase, bridging Phase 1 (foundation/auth) and Phase 3 (notifications/i18n).
   - *Agent directives:* Clearly separated. Coder builds, Tester validates, Reviewer audits, DevOps containerizes/localizes. No overlap in responsibilities.
   - *DoD:* Measurable, verifiable, aligned with phase scope.

   One minor adjustment: The prompt mentions "DevOps" in the directive section, but the global context listed "Docker, Deployer". I'll adapt to "DevOps (Docker & Local Infra)" to match the prompt's exact wording while keeping the spirit. I'll ensure the boundaries are extremely strict to prevent overlap.

   I will now generate the response exactly matching the required structure. I'll make sure the tone is authoritative and architectural. I'll double-check the directory paths and endpoints to ensure they are realistic and strictly bounded. I'll explicitly state what is OUT OF SCOPE to reinforce boundary isolation. All good. Proceed. 
   Structure check:
   # PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
   ## 1. Phase Operational Scope & Objectives
   ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)