# PHASE 1 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Establish the foundational Java 17 Quarkus backend with PostgreSQL multi‑tenant support (`tenant_id` column) and Kafka event bus connectivity.  
- Implement core authentication handling internal email/password (Argon2id), Firebase Auth, Google OAuth 2.0, and Facebook OAuth 2.0; generate signed JWTs with lease expiration and revocation.  
- Define role hierarchy (System Admin, Center Admin, Manager, Teacher, Student) and map them to JWT claims and tenant filtering.  
- Create initial Docker multi‑stage image for the backend service and configure GCP IAM service account policies.  
- Produce GKE deployment manifests and CI/CD pipeline seeds to enable subsequent phases.  
- Embed OWASP A01‑A07 hardening (parameterized queries, tenant filtering, AES‑256 PII encryption at rest, secure OAuth flows) throughout all created components.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend source tree** (`./sources/backend/`):  
  - `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` – Java domain, service, config.  
  - `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/` – Unit tests.  
  - `./sources/backend/src/main/resources/` – Application properties, Kafka client config.  
  - `./sources/backend/docker/` – Dockerfile(s).  
  - `./sources/backend/gcp/` – IAM service‑account YAML.  
  - `./sources/backend/kubernetes/` – GKE deployment & service manifests.  
- **Frontend source tree** (`./sources/frontend/`) – not required for Phase 1 but permitted for future integration.  
- **REST endpoints** (to be defined in Phase 2):  
  - `POST /api/v1/auth/login` (internal)  
  - `POST /api/v1/auth/oauth/{provider}` (Firebase, Google, Facebook)  
  - `GET /api/v1/tenants` (System Admin only)  
  - `GET /api/v1/roles` (all authenticated)  
- **Kafka topics** (pre‑created): `attendance`, `notifications`, `zalo-message`.  

## 3. Dedicated Sub-Agent Functional Directives
- **Coder**: Build domain entities (`Tenant`, `User`, `Role`) with `tenant_id` and OWASP‑compliant fields; implement `AuthService` handling internal password hashing (Argon2id), OAuth token exchange, JWT signing/lease, and role‑based claim injection.  
- **Docker**: Produce a multi‑stage Dockerfile (`./sources/backend/docker/Dockerfile`) that copies compiled JAR, sets JVM options, defines non‑root user, and includes health‑check.  
- **GCP**: Generate `iam-config.yaml` (`./sources/backend/gcp/iam-config.yaml`) defining a service account with `roles/cloudsql.client`, `roles/pubsub.subscriber`, `roles/secretmanager.secretAccessor` and enforce least‑privilege.  
- **GKE**: Create `deployment.yaml` (`./sources/backend/kubernetes/deployment.yaml`) and `service.yaml` referencing the Docker image, exposing port 8080, and injecting `TENANT_ID` env var.  
- **Manager**: Coordinate overall Phase 1 delivery, validate that all artifacts reside under `./sources/`, ensure OWASP hardening flags are present, and produce a Phase 1 orchestration summary (`./sources/backend/Phase1-Orchestration.md`).  
- **Reviewer**: Perform security and code review of all Java source files, confirming tenant filtering, parameterized queries, and JWT best‑practices.  
- **Tester**: Write unit tests for `AuthService` and domain entities, achieving ≥ 90 % line coverage and verifying OAuth flow mocks and role claim mapping.  

## 4. Phase Definition of Done (DoD)
- All Java source files placed under `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` with correct package naming.  
- Domain entities include `tenant_id` and OWASP‑compliant field handling (encryption, validation).  
- `AuthService` fully functional: internal login (Argon2id), OAuth providers, JWT issuance with expiration, role claims.  
- Role definitions enumerated and mapped to JWT `roles` claim.  
- Docker multi‑stage image built and pushed to artifact repository (simulated by Dockerfile existence).  
- GCP IAM config file present with least‑privilege policies.  
- GKE deployment manifests ready for rollout.  
- Unit test suites exist for `AuthService` and entities, meeting ≥ 90 % coverage.  
- Reviewer sign‑off confirming OWASP A01‑A07 compliance.  
- Manager’s orchestration document summarizing completed artifacts and validation results.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Establish Core Backend Foundations
#### SUB‑TASK 1.1: Create Domain Entities with Multi‑Tenant & OWASP Controls
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** 
    *   `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Tenant.java`
    *   `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/User.java`
    *   `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Role.java`
    *   `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/domain/TenantTest.java`
    *   `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/domain/UserTest.java`
    *   `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/domain/RoleTest.java`
    *   **Architectural Requirements:**
        *   Each entity includes a `Long tenantId` field annotated for PostgreSQL multi‑tenant filtering.
        *   Sensitive fields (e.g., password hash, personal info) are marked for AES‑256 encryption at rest.
        *   All JPA repositories use `@Query` with parameter placeholders to enforce parameterized queries (OWASP A03).
        *   Implement `equals`/`hashCode` based on `tenantId` and identifier to avoid cross‑tenant data leakage.
        *   Add validation annotations (e.g., `@NotNull`, `@Size`) per Jakarta Bean Validation.

#### SUB‑TASK 1.2: Build Multi‑Stage Docker Image
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/docker/Dockerfile`
    *   **Architectural Requirements:**
        *   Use `eclipse-temurin:17-jdk-alpine` as base.
        *   Copy `*.jar` from build stage, set `JAVA_OPTS` for container security.
        *   Run as non‑root user (`appuser`).
        *   Include health‑check endpoint (`/q/health`).
        *   Embed OWASP‑recommended JVM flags (`-Djdk.tls.client.protocols=TLSv1.3`).

#### SUB‑TASK 1.3: Provision GCP IAM Service Account
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/gcp/iam-config.yaml`
    *   **Architectural Requirements:**
        *   Define service account `membership-hub-backend@<project>.iam.gserviceaccount.com`.
        *   Grant `roles/cloudsql.client`, `roles/pubsub.subscriber`, `roles/secretmanager.secretAccessor`.
        *   Attach `iam.serviceAccountTokenCreator` for JWT signing if needed.
        *   Include `lifecyclePolicy` to enforce retention and audit logging.

#### SUB‑TASK 1.4: Orchestrate Phase 1 Deliverables
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/Phase1-Orchestration.md`
    *   **Architectural Requirements:**
        *   Summarize created artifacts (entities, Dockerfile, IAM config).
        *   Validate all paths start with `./sources/`.
        *   Confirm OWASP hardening flags are present in code.
        *   Record completion status and any open action items for subsequent phases.

### DAY 2: Implement Authentication, Roles, and Deploy to GKE
#### SUB‑TASK 2.1: Develop Core Authentication Service with OAuth & JWT
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java`
    *   **Architectural Requirements:**
        *   Provide `login(String email, String password)` using Argon2id for password hashing verification.
        *   Implement `oauthLogin(String provider, String idToken)` for Firebase, Google, Facebook; validate token via provider APIs.
        *   Generate JWT with claims: `sub`, `tenant_id`, `roles` (comma‑separated), `exp`, `iat`.
        *   Enforce token lease expiration ≤ 15 min; include revocation list check.
        *   All DB queries use parameterized statements; JWT signing key stored in Secret Manager (OWASP A02).
        *   Add `@RolesAllowed` annotations for role‑based access control.

#### SUB‑TASK 2.2: Review Security & Code Quality
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java`
    *   **Architectural Requirements:**
        *   Verify tenant filtering on all data accesses.
        *   Confirm JWT signing uses RS256 or ES256 with proper key rotation.
        *   Validate Argon2id configuration matches OWASP password storage guidelines.
        *   Ensure no hardcoded credentials or debug logs containing PII.
        *   Check compliance with OWASP A01‑A07 across the reviewed file.

#### SUB‑TASK 2.3: Unit Test Authentication Service
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AuthServiceTest.java`
    *   **Architectural Requirements:**
        *   Mock internal user repository and OAuth provider clients.
        *   Test successful internal login with correct credentials.
        *   Test failed login with incorrect password.
        *   Test OAuth flow for each provider (Firebase, Google, Facebook) with valid/invalid tokens.
        *   Validate JWT claim population (tenant_id, roles) and expiration.
        *   Ensure test coverage ≥ 90 % and no security‑sensitive test data leakage.

#### SUB‑TASK 2.4: Create GKE Deployment Manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/kubernetes/deployment.yaml`
    *   **Architectural Requirements:**
        *   Deploy container image `gcr.io/<project>/membership-hub-backend:latest`.
        *   Define `ReplicaSet` with 3 pods, pod anti‑affinity to avoid co‑location.
        *   Mount Secret Manager secret for JWT signing key.
        *   Set environment variable `TENANT_ID` placeholder for multi‑tenant routing.
        *   Include liveness and readiness probes (`/q/health`).
        *   Apply `securityContext` to run containers as non‑root.