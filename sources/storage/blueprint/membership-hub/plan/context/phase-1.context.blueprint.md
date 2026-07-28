# PHASE 1 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- **Database Context Initialization:** Design and apply a multi‑tenant PostgreSQL schema with a `tenant_id` column across all core tables (users, courses, enrollments, etc.) to guarantee data isolation per center. Generate Flyway/Liquibase migration scripts under `./sources/backend/src/main/resources/db/migration/`.
- **Authentication Service Implementation:** Build a Quarkus‑based authentication microservice supporting internal email/password login, and external providers (Firebase, Google, Facebook) using OAuth2/OpenID Connect. Produce JWT tokens with tenant‑scoped claims, enforce password hashing (bcrypt), and integrate CSRF/rate‑limiting per OWASP guidelines.
- **Tenant‑Isolation Validation Tests:** Write unit tests that verify SQL queries respect tenant boundaries (e.g., SELECT * FROM users WHERE tenant_id = ?). Ensure test coverage for isolation, data leakage prevention, and parameterized query usage.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Java Sources:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` (domain, repository, service, config)
- **Backend Test Sources:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/` (unit & integration tests)
- **Database Migration Scripts:** `./sources/backend/src/main/resources/db/migration/`
- **Configuration & Resources:** `./sources/backend/src/main/resources/application.yml`, `./sources/backend/src/main/resources/application-dev.yml`
- **Docker & Container Files:** `./sources/backend/Dockerfile`, `./sources/backend/docker-compose.yml`
- **Documentation Assets:** `./sources/backend/docs/` (Markdown, diagrams)
- **REST Endpoints (allowed for this phase):** `POST /api/v1/auth/login`, `POST /api/v1/auth/token`, `GET /api/v1/tenants/{id}/schema`, `GET /api/v1/health`, `GET /api/v1/metrics`

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for coder, tester, reviewer, doc, docker, GCP, GKE)
- **coder:** Responsible for all Java code creation, DB migration scripts, authentication service logic, security configuration, and Docker file generation. Must embed OWASP compliance (parameterized queries, bcrypt hashing, JWT tenant claims, rate‑limiting, CSRF tokens).
- **doc:** Generates comprehensive technical documentation (architecture diagrams, API spec, security design) under `./sources/backend/docs/`. Must reference the same functional tags as coder tasks.
- **tester:** Writes unit tests that validate tenant‑isolation SQL queries and authentication flows. Must follow the strict pair syntax `<source file>;<test file>` and include OWASP security assertions.
- **reviewer, docker, GCP, GKE:** Not assigned for Phase 1; remain idle.

## 4. Phase Definition of Done (DoD)
- **Database:** All core tables contain a `tenant_id` column; Flyway migration scripts applied successfully; tenant‑isolation verified via unit tests.
- **Authentication:** AuthenticationService implements login, token issuance, external provider delegation; JWT includes `tenant_id` claim; passwords stored using bcrypt; CSRF and rate‑limiting enabled; OpenAPI spec generated.
- **Security & Compliance:** All SQL uses parameterized queries; input validation and sanitization applied; OWASP Top‑10 mitigations (A01‑A09) enforced; documentation includes security considerations.
- **Testing:** 100 % unit‑test coverage for TenantRepository and AuthenticationService; tenant‑isolation tests pass; test suite executes without failures.
- **Artifacts:** Migration scripts, Java source files, documentation Markdown files, and Dockerfiles reside under `./sources/` with correct package layout (`org.nlh4j.saas.membershiphub`).

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Initialize Multi‑Tenant Database Schema and Base Authentication Skeleton
#### SUB-TASK 1.1: Create Flyway Migration for Multi‑Tenant Schema
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/resources/db/migration/V1__init_multi_tenant.sql`
    * **Architectural Requirements:**
        * Define `tenants` table with `id`, `name`, `tenant_id` (UUID) and `created_at`.
        * Add `tenant_id` column to `users`, `courses`, `enrollments`, `centers` tables using `ALTER TABLE`.
        * Include `CREATE INDEX idx_users_tenant_id` for performance.
        * Use `REVOKE ALL` on public schema and grant per‑tenant roles.
        * Enforce **OWASP A03:2021 – Injection** by using `PREPARED STATEMENT` patterns in migration scripts.
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [REQ-001], [ARC-001], [NFR-001]

#### SUB-TASK 1.2: Draft Multi‑Tenancy Architecture Documentation
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/docs/MultiTenancyArchitecture.md`
    * **Architectural Requirements:**
        * Document schema design, tenant isolation strategy, and data access layer (Repository) using `tenant_id` filters.
        * Include security considerations: row‑level security, principle of least privilege, and OWASP A01‑A09 mapping.
        * Provide diagram (text‑based) of tenant‑aware data flow.
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [REQ-001], [ARC-001], [NFR-001]

### DAY 2: Implement Core Authentication Service and Security Configuration
#### SUB-TASK 2.1: Build AuthenticationService with Internal & External Provider Support
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthenticationService.java`
    * **Architectural Requirements:**
        * Implement `login(String email, String password)` using BCrypt password verification.
        * Implement `authenticateWithFirebase(String idToken)`, `authenticateWithGoogle(String code)`, `authenticateWithFacebook(String code)` delegating to respective OAuth2 clients.
        * Generate JWT (`io.smallrye.jwt.build.Jwt`) containing `sub`, `tenant_id`, `roles`, and expiration.
        * Apply **OWASP A07:2021 – Identification and Authentication Failures** mitigations: account lockout, strong password policy, secure session handling.
        * Use `@RolesAllowed` and `jakarta.annotation.security.DeclareRoles` for role‑based access control.
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [REQ-001], [ARC-001], [NFR-001]

#### SUB-TASK 2.2: Document Auth API Specification
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/docs/AuthApiSpec.md`
    * **Architectural Requirements:**
        * Define request/response payloads for `/api/v1/auth/login`, `/api/v1/auth/token`.
        * Include error schemas (401, 400) and security scheme (HTTP Bearer JWT).
        * Capture external provider endpoints and token exchange flows.
        * Highlight OWASP security controls (rate‑limiting, CSRF tokens) applied per endpoint.
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [REQ-001], [ARC-001], [NFR-001]

### DAY 3: Write Unit Tests for Tenant‑Isolation Database Validation
#### SUB-TASK 3.1: Unit Test TenantRepository Query Isolation
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/TenantRepository.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/repository/TenantRepositoryTest.java`
    * **Architectural Requirements:**
        * Verify `findByTenantId(String tenantId)` returns only rows matching the supplied `tenant_id`.
        * Ensure cross‑tenant data leakage is prevented (assert empty result when mismatched tenant).
        * Use **parameterized queries** in repository methods to mitigate **OWASP A03:2021 – Injection**.
        * Include test cases for edge conditions (null tenant_id, duplicate tenant_id).
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [ARC-001], [NFR-002]