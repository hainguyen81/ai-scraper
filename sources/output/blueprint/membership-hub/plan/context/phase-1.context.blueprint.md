# PHASE 1 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Scaffold a Quarkus‑based monolithic micro‑service under `./sources/backend` with the corporate Java package `org.nlh4j.saas.membershiphub`.
- Define domain entities (Tenant, User, Role, Course, Teacher, Student, Enrollment, Attendance, StudentCard) with a `tenant_id` discriminator for strict multi‑center isolation.
- Create PostgreSQL schema via Flyway/Liquibase (versioned scripts) enforcing tenant filtering and OWASP A03 (SQL Injection) mitigation.
- Implement Argon2 password hashing, JWT token generation/validation, and baseline security filters (OWASP A01‑A07).
- Integrate OAuth2 providers (Firebase, Google, Facebook) using SmallRye OAuth2 and secure token verification.
- Define role hierarchy (System Admin, Admin, Manager, Teacher, Student) and enforce RBAC across all resources.
- Build initial REST endpoints: `POST /api/v1/auth/login`, `POST /api/v1/auth/register`, `POST /api/v1/auth/logout`, `GET /api/v1/tenants` (tenant‑isolated), `GET /api/v1/roles`.
- Configure Apache Kafka producers/consumers for real‑time notifications (Zalo groups, FCM) and auth events.
- Produce Docker multi‑stage images (JVM & native) with health‑checks and non‑root users.
- Generate GCP IAM policy (`iam.yml`) and GKE cluster manifest (`gke-cluster.yml`) with workload identity and least‑privilege roles.
- Write unit tests (≥80 % coverage) for Auth, Tenant, and Role services; write integration tests using Testcontainers for PostgreSQL & Kafka.
- Perform security scanning (OWASP ZAP) and ensure zero high‑severity findings.
- Validate all artifacts are placed under `./sources/` with no files directly under repository root.

## 2. Allowed Technical Scope & Directory Boundaries
- **Backend source tree** (all files must start with `./sources/backend/`):
  - `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/`
    - `domain/`
    - `repository/`
    - `service/`
    - `resource/`
    - `security/`
  - `./sources/backend/src/main/resources/`
    - `db/migration/`
    - `application.yml`
    - `kafka/`
  - `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/`
    - `resource/`
    - `service/`
  - `./sources/backend/src/test/resources/`
  - `./sources/backend/docker/`
    - `Dockerfile.jvm`
    - `Dockerfile.native`
  - `./sources/backend/infrastructure/gcp/`
    - `iam.yml`
    - `gke-cluster.yml`
  - `./sources/backend/config/` (optional Quarkus config profiles)
- **REST/GraphQL/Event endpoints** (allowed for this phase):
  - `POST /api/v1/auth/login`
  - `POST /api/v1/auth/register`
  - `POST /api/v1/auth/logout`
  - `GET /api/v1/tenants`
  - `GET /api/v1/tenants/{id}`
  - `GET /api/v1/roles`
  - `GET /api/v1/health`
  - `GET /api/v1/metrics`
- **Kafka topics** (allowed):
  - `membershiphub.auth.events`
  - `membershiphub.notifications`

## 3. Dedicated Sub-Agent Functional Directives
- **Coder**: Implement all Java domain models, repositories, services, security filters, OAuth2 configuration, Argon2 password handling, JWT token lifecycle, RBAC enforcement, Kafka producer/consumer logic, and create the initial REST resources. Ensure OWASP A01‑A07 controls (input validation, parameterized queries, tenant filtering, PII encryption, secure password storage, token verification, role‑based access control, logging).
- **Tester**: Write unit tests for `AuthResource`, `TenantResource`, `RoleService`; write integration tests using Testcontainers for PostgreSQL and Kafka; verify tenant isolation and OAuth2 flows. Use the strict semi‑colon pair syntax for test targets.
- **Reviewer**: Perform comprehensive code review of all Java source files under `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` and corresponding test files. Validate OWASP compliance, tenant filtering, secure credential storage, and absence of hardcoded secrets.
- **Docker**: Create multi‑stage Dockerfile definitions (`Dockerfile.jvm`, `Dockerfile.native`), embed health‑check endpoints, enforce non‑root user, and add security‑hardening labels. Build and locally test the images.
- **GCP**: Draft `iam.yml` defining service accounts and least‑privilege roles; validate syntax with `gcloud iam policies validate`. Ensure workload identity mapping for GKE.
- **GKE**: Draft `gke-cluster.yml` with autoscaling, node pools, workload identity, and network policies; validate with `kubectl apply --dry-run=client`.
- **Manager**: Orchestrate overall phase progress, ensure all generated artifacts respect the `./sources/` boundary, compile a Phase‑1 completion report (`phase1-completion-report.md`), and sign‑off after all deliverables are verified.

## 4. Phase Definition of Done (DoD)
- All Java source files placed under `org.nlh4j.saas.membershiphub` with OWASP A01‑A07 controls applied (tenant filtering, Argon2 hashing, JWT verification, RBAC, input validation, parameterized queries, PII encryption, secure logging).
- PostgreSQL schema (tenant‑aware) created and versioned in `src/main/resources/db/migration/`.
- Kafka producer/consumer services functional with unit tests covering message flow.
- Docker images built successfully (JVM & native) and health‑checks passing.
- GCP IAM policy and GKE cluster manifests syntactically valid and ready for deployment.
- OAuth2 integrations for Firebase, Google, Facebook configured and token validation secured.
- Role definitions and RBAC filters enforced across all resources.
- Initial REST endpoints (`/auth/*`, `/tenants`, `/roles`) implemented, secured, and functional.
- Unit test coverage ≥80 % for core services; integration tests for auth and tenant listing passing.
- Security scan (OWASP ZAP) yields zero high‑severity findings.
- All artifacts strictly under `./sources/` with no files at repository root.
- Phase‑1 completion report generated and approved by Manager.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: PROJECT SCAFFOLDING AND CORE DOMAIN SETUP
#### SUB-TASK 1.1: Create Quarkus project structure and corporate Java package
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/
    *   **Architectural Requirements:**
        *   Use Maven with Quarkus platform 3.2.0; generate basic `pom.xml` with necessary extensions (Quarkus, JDBC PostgreSQL, Kafka, OpenTelemetry).
        *   Enforce OWASP A03 (SQL Injection) by configuring JPA repositories with `spring-data-jpa` and using derived queries; avoid native queries unless parameterized.
        *   Apply OWASP A07 (Cryptographic Failures) by marking password fields for Argon2 hashing and storing JWT secrets in environment variables.

#### SUB-TASK 1.2: Define Flyway migration for tenant‑aware PostgreSQL schema
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/db/migration/V1__init_schema.sql
    *   **Architectural Requirements:**
        *   Create tables `tenants`, `roles`, `users`, `courses`, `teachers`, `students`, `enrollments`, `attendance`, `student_cards` with `tenant_id` column as `UUID` (or `INTEGER`) and primary key.
        *   Add `tenant_id` foreign keys referencing `tenants(id)`; enforce `NOT NULL` on `tenant_id` for row‑level isolation.
        *   Apply OWASP A01 (Broken Access Control) by adding a `tenant_filter` view or stored procedure that restricts data access per tenant.

#### SUB-TASK 1.3: Implement User entity with Argon2 hashing and JWT generation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/User.java
    *   **Architectural Requirements:**
        *   Annotate with `@TenantFilter` and `@Entity`; include fields `id`, `email`, `passwordHash`, `tenantId`, `role`.
        *   Use `org.passay.PasswordEncoder` with Argon2 implementation for `passwordHash`.
        *   Provide method `generateJwt()` using SmallRye JWT (sign with HS256, set `tenant_id` claim).
        *   Enforce OWASP A02 (Broken Authentication) by validating token signature and expiration in a security filter.

#### SUB-TASK 1.4: Create AuthResource REST endpoints (login, register, logout)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AuthResource.java
    *   **Architectural Requirements:**
        *   Define `@POST /api/v1/auth/login` – accept `email`/`password`, authenticate via `UserService`, return JWT.
        *   Define `@POST /api/v1/auth/register` – create `User` with Argon2 hashed password; enforce role `STUDENT` for self‑registration; apply OWASP A05 (Broken Access Control) by checking caller’s role (System Admin can create any role).
        *   Define `@POST /api/v1/auth/logout` – invalidate token via blacklist or JWT revocation list.
        *   Apply `@RolesAllowed` annotations for protected methods; use `@TenantFilter` to scope operations.

#### SUB-TASK 1.5: Implement TenantResource for tenant listing with isolation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/TenantResource.java
    *   **Architectural Requirements:**
        *   Define `@GET /api/v1/tenants` – return list of tenants visible to authenticated user.
        *   Apply tenant filtering via `TenantRepository.findByTenantId(currentTenantId)`; enforce OWASP A01 (Broken Access Control) by ensuring users cannot view tenants they do not belong to.

### DAY 2: KAFKA CONNECTORS, DOCKER IMAGES, AND INFRASTRUCTURE MANIFESTS
#### SUB-TASK 2.1: Configure Kafka producer/consumer and NotificationService
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java
    *   **Architectural Requirements:**
        *   Use Apache Kafka client (version 3.5) with `KafkaProducer` for `membershiphub.notifications` and `KafkaConsumer` for `membershiphub.auth.events`.
        *   Serialize events to JSON via Jackson; include `tenant_id` header for routing.
        *   Implement `sendNotification(NotificationEvent event)` method; enforce OWASP A03 by validating event payload size and content.

#### SUB-TASK 2.2: Create Kafka Connect configuration for notification pipeline
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/kafka/connect-notify.properties
    *   **Architectural Requirements:**
        *   Define connector class `io.confluent.connect.jdbc.JdbcSourceConnector` (if needed) or `org.apache.kafka.connect.file.FileStreamSinkConnector`.
        *   Set topics, consumer group, offset storage, and secure credential placeholders (no hardcoded secrets).
        *   Apply OWASP A06 (Vulnerable Crypto) by ensuring TLS settings for Kafka broker connection.

#### SUB-TASK 2.3: Build multi‑stage JVM Docker image
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile.jvm
    *   **Architectural Requirements:**
        *   Base image `eclipse-temurin:21-jdk-alpine`.
        *   Copy `pom.xml` and source, compile with `mvn package -DskipTests`.
        *   Create non‑root user `appuser`; set ownership of application files.
        *   Expose port `8080`; add health‑check `curl http://localhost:8080/q/health`.
        *   Enforce OWASP A12 (Insufficient Logging) by configuring logging to stdout/stderr.

#### SUB-TASK 2.4: Build native Docker image
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile.native
    *   **Architectural Requirements:**
        *   Base image `quay.io/quarkus/ubi9-quarkus-native-image:22.3.0-java21`.
        *   Copy compiled native binary; expose port `8080`; add health‑check.
        *   Ensure image size minimized and no debug symbols.

#### SUB-TASK 2.5: Draft GCP IAM policy YAML
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/infrastructure/gcp/iam.yml
    *   **Architectural Requirements:**
        *   Define service account `membershiphub-sa`.
        *   Grant roles: `roles/cloudsql.client`, `roles/pubsub.subscriber`, `roles/pubsub.publisher`, `roles/container.admin`.
        *   Apply principle of least privilege; enforce OWASP A01 via role‑based access control.

#### SUB-TASK 2.6: Draft GKE cluster manifest YAML
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/infrastructure/gcp/gke-cluster.yml
    *   **Architectural Requirements:**
        *   Cluster name `membershiphub-gke`; location `us-central1`.
        *   Enable autoscaling, workload identity, network policies.
        *   Define node pools for `default` and `spot` (cost‑optimized).
        *   Enforce network isolation; apply OWASP A05 (Broken Access Control) by restricting `cluster-admin` role to System Admin only.

### DAY 3: OAUTH2 INTEGRATION, RBAC, AND SECURITY TESTING
#### SUB-TASK 3.1: Integrate OAuth2 providers (Firebase, Google, Facebook)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/OAuth2Config.java
    *   **Architectural Requirements:**
        *   Configure SmallRye OAuth2 with OIDC providers: `firebase`, `google`, `facebook`.
        *   Load client IDs and secrets from environment variables (`OAUTH_FIREBASE_CLIENT_ID`, etc.).
        *   Validate ID tokens using provider‑specific JWKS; enforce OWASP A02 (Broken Authentication) by verifying token issuer and audience.

#### SUB-TASK 3.2: Implement RoleService with role definitions and permission checks
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/RoleService.java
    *   **Architectural Requirements:**
        *   Define enum `AppRole {SYSTEM_ADMIN, ADMIN, MANAGER, TEACHER, STUDENT}`.
        *   Provide method `boolean hasPermission(User user, Resource resource, Action action)`.
        *   Enforce OWASP A01 (Broken Access Control) by checking tenant and role hierarchy.

#### SUB-TASK 3.3: Create JwtSecurityPolicy for tenant filtering and RBAC
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/JwtSecurityPolicy.java
    *   **Architectural Requirements:**
        *   Intercept inbound requests via `ContainerRequestFilter`.
        *   Extract `tenant_id` and `roles` from JWT; attach to `SecurityContext`.
        *   Apply tenant isolation in repository queries; enforce OWASP A01.

#### SUB-TASK 3.4: Write unit tests for AuthResource
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AuthResource.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/resource/AuthResourceTest.java
    *   **Architectural Requirements:**
        *   Use JUnit 5 and MockMVC; mock `UserService` and `JwtService`.
        *   Test login with valid credentials returns JWT; test registration hashes password with Argon2; test logout invalidates token.
        *   Enforce OWASP A03 by using parameterized test data and avoiding SQL injection in mocks.

#### SUB-TASK 3.5: Write integration test for TenantResource
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/TenantResource.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/resource/TenantResourceIT.java
    *   **Architectural Requirements:**
        *   Use Testcontainers for PostgreSQL and Kafka; spin up a fresh database per test.
        *   Verify tenant listing respects tenant isolation (users see only their tenants).
        *   Enforce OWASP A01 by ensuring test data does not leak other tenants’ records.

#### SUB-TASK 3.6: Perform security code review
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/
    *   **Architectural Requirements:**
        *   Scan all Java files for hardcoded credentials, insecure JWT secret storage, missing `@TenantFilter`, lack of input validation, and unsafe SQL queries.
        *   Verify Argon2 usage and proper password hashing salt handling.
        *   Ensure OWASP A01‑A07 controls are present; flag any violations for remediation.

### DAY 4: FINAL VERIFICATION, BUILD, AND SIGN‑OFF
#### SUB-TASK 4.1: Build and test JVM Docker image locally
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile.jvm
    *   **Architectural Requirements:**
        *   Execute `docker build -t membershiphub-backend .` from `./sources/backend/docker`.
        *   Run container with `-p 8080:8080` and perform health‑check `curl http://localhost:8080/q/health` expecting `UP`.
        *   Validate logs contain no sensitive data; enforce OWASP A12 (Insufficient Logging) by checking that all security events are logged.

#### SUB-TASK 4.2: Validate GCP IAM policy syntax
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/infrastructure/gcp/iam.yml
    *   **Architectural Requirements:**
        *   Run `gcloud iam policies validate --policy-file=iam.yml`.
        *   Ensure no overly permissive roles (e.g., `roles/*` with `*` wildcard) remain.
        *   Apply least‑privilege principle; enforce OWASP A01 via role‑based access control.

#### SUB-TASK 4.3: Validate GKE cluster manifest with dry‑run
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/infrastructure/gcp/gke-cluster.yml
    *   **Architectural Requirements:**
        *   Execute `kubectl apply --dry-run=client -f gke-cluster.yml`.
        *   Verify resource quotas, network policies, and workload identity configuration.
        *   Enforce OWASP A05 (Broken Access Control) by confirming cluster admin role is restricted.

#### SUB-TASK 4.4: Generate Phase‑1 completion report and sign‑off
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/phase1-completion-report.md
    *   **Architectural Requirements:**
        *   List all created files (Java sources, configs, Dockerfiles, IAM/GKE manifests, test suites).
        *   Summarize agent contributions, OWASP compliance status, test coverage metrics, and any open issues.
        *   Ensure all artifacts reside under `./sources/` and no root‑level files exist.
        *   Provide final sign‑off confirmation for progression to Phase 2.