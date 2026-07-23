# PHASE 1 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Establish the foundational Quarkus‑based Java backend service for the membership‑hub SaaS platform.
- Define a multi‑tenant PostgreSQL schema with discriminator column `tenant_id` covering core entities (centers, users, roles, courses, enrollments, attendance, points, promotions, announcements).
- Configure SmallRye Kafka topics for real‑time notifications and attendance events.
- Implement authentication & authorization: email/password with Argon2id hashing, OAuth2 adapters (Firebase, Google, Facebook), JWT issuance (HS256), role‑based access control (System Admin, Admin, Manager, Teacher, Student) with tenant isolation.
- Add multi‑language locale detection, per‑user default locale storage, and SEO meta‑tag generation for all pages.
- Produce base Dockerfiles (backend & frontend placeholders) and GCP/GKE manifest skeletons under `./sources/`.
- Generate unit tests for core services and security components, ensuring OWASP compliance (parameterized queries, input validation, tenant scoping, encryption).

## 2. Allowed Technical Scope & Directory Boundaries
All artifacts must reside under `./sources/` with the following strict directory matrices:
- `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` – Java application code.
- `./sources/backend/src/main/resources/` – Configuration (application.yml, kafka topics, JPA entities, OpenAPI specs).
- `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/` – Unit test suites.
- `./sources/backend/src/test/resources/` – Test data & mocks.
- `./sources/backend/docker/` – Dockerfile(s) and build scripts.
- `./sources/backend/kafka/` – Kafka topic definitions (YAML/JSON).
- `./sources/backend/config/` – Tenant‑aware security & encryption configs.
- `./sources/frontend/` – Placeholder Next.js skeleton (optional for Phase 1).
- `./sources/gcp/` – Service account JSON, IAM policies, Cloud Build definitions.
- `./sources/gke/` – Kubernetes Deployment, Service, Ingress, HPA YAMLs.
- `./sources/ci/` – CI pipeline placeholders (GitHub Actions, Cloud Build triggers).

## 3. Dedicated Sub-Agent Functional Directives
- **Coder**: Implement core Quarkus resources, services, repositories, authentication, JWT handling, RBAC filters, locale detection, SEO utilities, and all Java entity definitions. Inject OWASP hardening (parameterized queries, tenant isolation, Argon2id hashing, AES‑256‑GCM encryption) directly into code.
- **Tester**: Write unit tests for authentication, JWT verification, tenant‑scoped repository queries, locale handling, and SEO utilities. Use semi‑colon pair syntax for test targets.
- **Reviewer**: Validate OWASP compliance, ensure tenant isolation, encryption parameters, and secure coding practices across all Java code and configuration.
- **Docker**: Create multi‑stage Dockerfile for backend (`./sources/backend/docker/Dockerfile`) and placeholder frontend Dockerfile (`./sources/frontend/docker/Dockerfile`). Include security best‑practice layers (non‑root user, slim bases).
- **GCP**: Produce Service Account JSON (`./sources/gcp/service-account.json`), IAM policy YAML (`./sources/gcp/iam-policy.yaml`), and Cloud Build pipeline definition (`./sources/gcp/cloudbuild.yaml`) referencing the artifacts.
- **GKE**: Generate Kubernetes manifests (`./sources/gke/deployment.yaml`, `./sources/gke/service.yaml`, `./sources/gke/ingress.yaml`, `./sources/gke/hpa.yaml`) with tenant‑aware resource limits and environment variables.
- **Manager**: Orchestrate overall Phase 1 delivery, verify that all generated paths adhere to the `./sources/` boundary, confirm that each sub‑agent’s work satisfies the Phase Definition of Done, and produce a final Phase 1 summary artifact (`./sources/phase1-summary.md`).

## 4. Phase Definition of Done (DoD)
- Maven/Gradle build resolves and produces a runnable JAR under `./sources/backend/target/`.
- PostgreSQL schema scripts (`V1__init.sql`, `V2__tenant_discriminator.sql`) create all required tables with `tenant_id` discriminator.
- Kafka topic definitions exist for `notifications` and `attendance-events`.
- Authentication service implements `/auth/login`, `/auth/oauth/{provider}` endpoints with JWT tokens; password hashing uses Argon2id; OAuth2 adapters integrated.
- Role‑based access control filters enforce tenant isolation for all REST endpoints.
- Multi‑language locale detection (`Accept-Language` header) stores default locale per user; SEO meta tags generated for all pages.
- Base Dockerfiles and GKE manifests are syntactically valid YAML/JSON.
- Unit test suites achieve ≥ 80 % coverage for core services and security components.
- All generated files strictly follow the `./sources/` directory rules and Java package `org.nlh4j.saas.membershiphub`.
- Phase 1 summary artifact documents completed objectives and any open items.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Establish Quarkus Project Skeleton, Core Config, and Authentication Service
#### SUB‑TASK 1.1: Create Maven Project Structure and Core Package Layout
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/
    *   **Architectural Requirements:**
        *   Generate `pom.xml` (Maven) with Quarkus platform, Java 17, Hibernate ORM, SmallRye Kafka, Argon2id, JWT (HS256) dependencies.
        *   Create `Application.java` (main class) with `@QuarkusMain` and default config.
        *   Add `org/nlh4j/saas/membershiphub/config/` package containing `AppConfig.java` defining `tenantId` property placeholder and `AES256GCMConfig`.
        *   Implement `org/nlh4j/saas/membershiphub/security/` with `PasswordEncoderConfig` (Argon2id), `JwtConfig` (HS256), and `OAuth2Config` for Firebase/Google/Facebook adapters.
        *   **OWASP Compliance:** Enforce parameterized queries via Hibernate `CriteriaBuilder`, tenant isolation via `CriteriaQuery` predicate on `tenant_id`, and input validation using Jakarta Validation annotations.

#### SUB‑TASK 1.2: Define Kafka Topics and Event Models
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/kafka/
    *   **Architectural Requirements:**
        *   Create `notifications.yaml` and `attendance-events.yaml` defining topic names, partitions, and retention.
        *   Add `org/nlh4j/saas/membershiphub/event/` package with `NotificationEvent.java` and `AttendanceEvent.java` POJOs annotated with `@KafkaKey` and `@KafkaTopic`.
        *   **OWASP Compliance:** Ensure event payloads are serialized with Jackson and never contain raw user PII; encrypt sensitive fields using AES‑256‑GCM before Kafka emission.

#### SUB‑TASK 1.3: Implement Authentication & JWT Issuance
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AuthResource.java
    *   **Architectural Requirements:**
        *   Expose `POST /auth/login` accepting `username` and `password`; validate via `UserService` using Argon2id hashed passwords.
        *   Expose `GET /auth/oauth/{provider}` for OAuth2 redirects and callback handling.
        *   Generate JWT token with `tenant_id` claim, user id, role list, and expiration (15 min).
        *   Provide `JwtTokenResponse` DTO.
        *   **OWASP Compliance:** Use parameterized authentication queries, enforce rate‑limiting at the resource level, and store refresh tokens encrypted with AES‑256‑GCM.

#### SUB‑TASK 1.4: Create Base Docker Image for Backend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Multi‑stage build: builder stage (Maven compile) → runtime stage (distroless Java 17).
        *   Set non‑root user (`appuser`), copy JAR, expose port `8080`.
        *   Include health‑check endpoint `/q/health`.
        *   **Security:** Use `java -Dquarkus.profile=prod` and disable debug flags.

#### SUB‑TASK 1.5: Draft GCP Service Account and IAM Policies
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/gcp/
    *   **Architectural Requirements:**
        *   Generate `service-account.json` placeholder with `membership-hub@<project>.iam.gserviceaccount.com`.
        *   Create `iam-policy.yaml` granting `roles/owner` to `serviceAccount:membership-hub@<project>.iam.gserviceaccount.com` and `roles/container.admin` for GKE provisioning.
        *   **Security:** Enforce least‑privilege principle; include `tenant_id` condition in IAM policies where possible.

#### SUB‑TASK 1.6: Initial Unit Tests for Authentication
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AuthResource.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/resource/AuthResourceTest.java
    *   **Architectural Requirements:**
        *   Write JUnit 5 test cases covering successful login, failed credentials, OAuth2 redirect, and JWT claim validation.
        *   Mock `UserService` and `JwtService` to isolate behavior.
        *   Verify Argon2id password verification and JWT `tenant_id` inclusion.
        *   **OWASP Compliance:** Ensure tests do not store real passwords; use test‑specific hashed values.

### DAY 2: Build Multi‑Tenant PostgreSQL Schema, RBAC, and Locale Support
#### SUB‑TASK 2.1: Design and Create PostgreSQL Migration Scripts
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/db/migration/
    *   **Architectural Requirements:**
        *   `V1__init.sql` – create `tenants`, `roles`, `users`, `centers`, `courses`, `enrollments`, `attendance`, `points`, `promotions`, `announcements` tables.
        *   `V2__tenant_discriminator.sql` – add `tenant_id` column to all tenant‑scoped tables, foreign key to `tenants`.
        *   `V3__user_roles.sql` – junction table `user_roles` linking `users` and `roles`.
        *   **OWASP Compliance:** Use `CREATE TABLE` with `IF NOT EXISTS`, enforce `tenant_id` NOT NULL, and apply `CHECK` constraints to prevent injection.

#### SUB‑TASK 2.2: Implement Core JPA Entities with Tenant Isolation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/
    *   **Architectural Requirements:**
        *   Create `TenantEntity.java` (base class) with `Long id`, `String tenantId`.
        *   Derive `User.java`, `Center.java`, `Course.java`, `Enrollment.java`, `Attendance.java`, `Point.java`, `Promotion.java`, `Announcement.java` extending `TenantEntity`.
        *   Annotate each with `@Table`, `@Entity`, `@TenantFilter` (custom JPA query filter).
        *   **OWASP Compliance:** Use `@Column` with `length` limits, `@Enumerated` for enums, and `@Where` clause for tenant filtering.

#### SUB‑TASK 2.3: Develop Role‑Based Access Control (RBAC) Filter
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/filter/RbacFilter.java
    *   **Architectural Requirements:**
        *   Implement `ContainerRequestFilter` that extracts JWT `tenant_id` and `roles`.
        *   Enforce per‑endpoint role permissions (e.g., `System Admin` can access all tenants, `Admin` only own tenant).
        *   Return `403` for unauthorized accesses.
        *   **OWASP Compliance:** Validate JWT signature, ensure `tenant_id` is present, and apply parameterized authorization checks.

#### SUB‑TASK 2.4: Add Multi‑Language Locale Detection and SEO Utilities
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/util/LocaleUtil.java
    *   **Architectural Requirements:**
        *   Read `Accept-Language` header, fallback to user’s stored locale, default to `en`.
        *   Provide `ResourceBundle` loading for messages.
        *   Create `SeoMetaTagUtil.java` generating `<meta>` tags for `og:title`, `og:description`, `og:locale`.
        *   **OWASP Compliance:** Sanitize locale strings to prevent XSS; ensure meta tags are HTML‑escaped.

#### SUB‑TASK 2.5: Write Unit Tests for Schema and RBAC
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/User.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/model/UserTest.java
    *   **Architectural Requirements:**
        *   Test JPA persistence of a `User` with tenant isolation.
        *   Verify `TenantEntity` base class enforces `tenant_id` population.
        *   Test RBAC filter logic with mocked JWT claims.
        *   **OWASP Compliance:** Ensure test data does not contain real PII; use faker libraries.

#### SUB‑TASK 2.6: Security Review and OWASP Validation
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/
    *   **Architectural Requirements:**
        *   Review all Java source files for:
            *   Parameterized queries (no string concatenation).
            *   Proper use of `tenant_id` in `CriteriaQuery` predicates.
            *   Encryption of PII fields (AES‑256‑GCM) in `User` and `Center` models.
            *   Password storage using Argon2id.
        *   Provide a compliance checklist and flag any deviations.

#### SUB‑TASK 2.7: Create Placeholder Frontend Skeleton
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/
    *   **Architectural Requirements:**
        *   Generate `package.json`, `next.config.js`, `tsconfig.json` with TypeScript and i18n plugins.
        *   Add `pages/_app.tsx` with locale detection and SEO `<head>` injection using `LocaleUtil` from backend (via API).
        *   **Security:** Ensure CSRF tokens are set via headers; no client‑side secrets.

### DAY 3: Finalize Docker, GKE, CI/CD, and Integration Validation
#### SUB‑TASK 3.1: Complete Multi‑Stage Docker Build for Backend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Refine builder stage to copy `pom.xml`, run `mvn dependency:go-offline`.
        *   Copy source, compile, package.
        *   Runtime stage: copy JAR, set JVM options (`-XX:+UseContainerSupport`), define health‑check script.
        *   Add label `maintainer` and `version`.

#### SUB‑TASK 3.2: Produce GKE Deployment Manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/gke/
    *   **Architectural Requirements:**
        *   `deployment.yaml` – define `app.kubernetes.io/name: membership-hub`, image pull secret, resource limits, env vars (`TENANT_ID`, `KAFKA_BOOTSTRAP`), and `securityContext` (runAsNonRoot).
        *   `service.yaml` – expose port `8080` clusterIP.
        *   `ingress.yaml` – NGINX ingress with `tls` block.
        *   `hpa.yaml` – autoscale based on CPU utilization.
        *   **Security:** Include pod anti‑affinity to avoid co‑locating same tenant pods.

#### SUB‑TASK 3.3: Draft GCP Cloud Build Pipeline
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/gcp/cloudbuild.yaml
    *   **Architectural Requirements:**
        *   Define steps: `mvn clean package`, `docker build`, `docker push` to Artifact Registry.
        *   Trigger on `main` branch.
        *   Include `substitutions` for `PROJECT_ID`, `IMAGE_NAME`, `SERVICE_ACCOUNT`.
        *   **Security:** Use service account with limited permissions; store secrets in Secret Manager.

#### SUB‑TASK 3.4: Integration Tests for Core Flows
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/integration.spec.ts
    *   **Architectural Requirements:**
        *   End‑to‑end test suite verifying:
            *   User registration → login → JWT acquisition.
            *   Tenant isolation: User from tenant A cannot access tenant B resources.
            *   Attendance QR scan endpoint idempotency.
            *   Notification Kafka event publishing (mock Kafka).
        *   Use Playwright or Cypress with fixtures.
        *   **OWASP Compliance:** Ensure tests do not store real credentials; use encrypted test data.

#### SUB‑TASK 3.5: Phase 1 Summary and Final Validation
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/phase1-summary.md
    *   **Architectural Requirements:**
        *   Document completed artifacts (Maven build, DB migrations, Kafka topics, Auth service, RBAC, locale/SEO, Docker, GKE, GCP pipelines, unit/integration tests).
        *   List any open items (e.g., frontend feature implementation, advanced encryption key management).
        *   Confirm all generated paths adhere to `./sources/` rule and Java package `org.nlh4j.saas.membershiphub`.
        *   Provide sign‑off checklist aligned with Phase Definition of Done.