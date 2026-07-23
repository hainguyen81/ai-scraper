# PHASE 2 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement the core domain model and services required for multi‑tenant learning management:
- Define JPA entities for **Center, Course, Teacher, Student, Enrollment, Attendance, StudentCard** with `tenant_id` discriminator and PII encryption.
- Generate Flyway/SQL schema scripts under `./sources/backend/src/main/resources/db/migration/` to create tenant‑isolated tables.
- Build CRUD REST resources (JAX-RS) for each entity exposing standard endpoints (`/centers`, `/courses`, `/teachers`, `/students`, `/enrollments`, `/attendance`, `/studentcards`).
- Develop QR‑code generation/scanning utility (barcode format: UTF‑8 payload) and integrate into attendance workflow.
- Implement attendance service that records a single attendance per student per course per day (idempotent) and calculates remaining validity days for the associated StudentCard.
- Create Notification service that publishes events to Apache Kafka, consumes them, and forwards to **Zalo API** (group messaging) and **FCM** (mobile push) with proper tenant routing.
- Add Course overlap validation to prevent scheduling conflicts (same teacher, same time slot across courses).
- Enforce Role‑Based Access Control (RBAC) using Quarkus security annotations and a custom `TenantFilter` to guarantee data isolation per tenant and role.
- Ensure OWASP A01‑A07 hardening: parameterized queries, input validation, output encoding, secure password handling (Argon2), JWT token verification, and audit logging for all domain changes.
- Produce unit and integration test suites covering all new services, Kafka event flows, and RBAC enforcement.

## 2. Allowed Technical Scope & Directory Boundaries
All artifacts must reside under `./sources/` with the following strict directory matrices:

- `./sources/backend/src/main/java/org/nlhj/saas/membershiphub/` – Java domain, service, repository, security, and configuration classes.
- `./sources/backend/src/main/resources/` – Application YAML, logging config, and Flyway migration scripts.
- `./sources/backend/src/main/resources/db/migration/` – SQL DDL scripts (e.g., `V1__create_tables.sql`).
- `./sources/backend/src/main/docker/` – Multi‑stage Docker build definitions.
- `./sources/backend/src/test/java/org/nlhj/saas/membershiphub/` – Unit test source tree.
- `./sources/backend/tests/` – Integration/E2E test suites (JUnit 5).
- `./sources/backend/gcp/` – GCP IAM, Cloud SQL, and service‑account YAML definitions.
- `./sources/backend/k8s/` – GKE Deployment, Service, and ConfigMap manifests.
- `./sources/backend/docker/` – Standalone Dockerfile (must not be placed at repository root).

No frontend, mobile, or AI chat widget files are required in this phase.

## 3. Dedicated Sub-Agent Functional Directives
- **Coder Agent:** Implement all domain entities, CRUD resources, QR code utility, attendance & notification services, course overlap validator, and RBAC filter. Inject OWASP security controls (tenant filtering, PII encryption, parameterized queries) into each component.
- **Tester Agent:** Write unit tests for domain services, QR code, attendance, notification, overlap validation, and RBAC filter. Produce integration/E2E tests for Kafka event pipelines and end‑to‑end CRUD flows.
- **Reviewer Agent:** Conduct security and code reviews ensuring compliance with OWASP guidelines, tenant isolation, and proper error handling across all Java components.
- **Docker Agent:** Craft a multi‑stage Dockerfile under `./sources/backend/docker/` and a container build script (`build.sh`) that respects the corporate image naming convention.
- **GCP Agent:** Generate Cloud SQL instance definition (`sql-instance.yaml`) and IAM service‑account policy (`iam-policy.yaml`) with least‑privilege roles for the backend service.
- **GKE Agent:** Produce Kubernetes Deployment (`deployment.yaml`), Service (`service.yaml`), and ConfigMap (`configmap.yaml`) manifests for stateless scaling and environment variable injection.
- **Manager Agent:** Orchestrate the overall Phase‑2 delivery, coordinate sub‑agent progress, validate final integration test results, and ensure all generated artifacts adhere to the workspace boundary rules.

## 4. Phase Definition of Done (DoD)
- All seven domain entities defined with `tenant_id` and encrypted PII fields.
- Flyway migration scripts create tenant‑scoped tables and indexes.
- Complete CRUD REST APIs (GET/POST/PUT/DELETE) for each entity with OpenAPI documentation.
- QR code generator and scanner functional (generate payload, decode with error handling).
- Attendance service guarantees at most one record per student per course per day and computes remaining card days accurately.
- Notification service publishes to Kafka, consumes, and successfully pushes to Zalo groups and FCM with acknowledgment.
- Course overlap validation prevents scheduling conflicts using DB constraints or service logic.
- RBAC filter enforces role‑based data access (System Admin > Admin > Manager > Teacher > Student) and tenant isolation.
- OWASP A01‑A07 controls embedded: input validation, output encoding, parameterized queries, Argon2 password hashing, JWT verification, audit logging.
- 100 % unit test coverage for new Java services and 90 % integration test coverage for Kafka and REST endpoints.
- Docker image built, scanned, and tagged per corporate standards.
- GCP Cloud SQL and IAM resources declared and syntactically valid.
- GKE manifests ready for `kubectl apply` with resource limits and liveness probes.
- All artifacts placed under `./sources/` with correct Java package layout (`org.nlh4j.saas.membershiphub`).
- Phase‑2 acceptance sign‑off completed by Manager and Reviewer.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: DOMAIN ENTITY CREATION & INITIAL BACKEND SCAFFOLDING
#### SUB-TASK 1.1: Define JPA domain entities with tenant isolation and PII encryption
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/domain/Center.java
    *   **Architectural Requirements:**
        *   Annotate with `@TenantEntity` (custom) to enforce `tenant_id` column.
        *   Apply `@PIIEncrypted` on fields containing personal data (e.g., admin contact).
        *   Use Lombok `@Data` `@Entity` `@Table` with `schema = "centers"`.
        *   Implement `@PrePersist` to generate UUID primary key.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/domain/Course.java
    *   **Architectural Requirements:**
        *   Include `tenant_id` discriminator column.
        *   Define `@CourseTimeSlot` validation to prevent null start/end times.
        *   Apply OWASP A03: Use parameterized queries via `@Query` methods.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/domain/Teacher.java
    *   **Architectural Requirements:**
        *   Encrypt SSN/CitizenID using AES‑256 (`PIIEncryptionService`).
        *   Add `@TenantEntity` and `@RoleAllowed("TEACHER")`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/domain/Student.java
    *   **Architectural Requirements:**
        *   Store password hash with Argon2 (`@PasswordHash`).
        *   Include `tenant_id` and `@TenantEntity`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/domain/Enrollment.java
    *   **Architectural Requirements:**
        *   Enforce referential integrity via `@ManyToOne` with cascade `Persist`.
        *   Add `@TenantEntity` and `@AuditLog`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/domain/Attendance.java
    *   **Architectural Requirements:**
        *   Unique constraint on `(student_id, course_id, attendance_date)`.
        *   Use `@TenantEntity` and `@IdempotentWrite`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/domain/StudentCard.java
    *   **Architectural Requirements:**
        *   Include `valid_until` calculated field.
        *   Apply `@PIIEncrypted` on card number.
*   **Target Path:** ./sources/backend/src/main/resources/db/migration/V1__create_tables.sql
    *   **Architectural Requirements:**
        *   Create tables matching entity schemas with `tenant_id` column.
        *   Add indexes for fast tenant‑scoped queries.
        *   Include `CHECK` constraints for attendance uniqueness.
*   **Target Path:** ./sources/backend/src/main/resources/application.yml
    *   **Architectural Requirements:**
        *   Configure datasource with `jdbc:postgresql://` and `currentSchema=public`.
        *   Enable Hibernate `multitenant=COLUMN` with `tenant_id` field.
        *   Set `quarkus.oidc.enabled=false` (internal auth) and `quarkus.security.jaxrs.permit-all` for health endpoints.

#### SUB-TASK 1.2: Create CRUD JAX‑RS resources for each entity
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/resource/CenterResource.java
    *   **Architectural Requirements:**
        *   Define REST methods (`GET`, `POST`, `PUT`, `DELETE`) with `@RolesAllowed("ADMIN","MANAGER","SYSTEM_ADMIN")`.
        *   Use `@Transactional` and `@TenantFilter` to scope operations.
        *   Return `Response` with appropriate HTTP status codes.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/resource/CourseResource.java
    *   **Architectural Requirements:**
        *   Implement overlap validation via `@CourseOverlapValidator` before persist.
        *   Enforce `@RolesAllowed("ADMIN","MANAGER")`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/resource/TeacherResource.java
    *   **Architectural Requirements:**
        *   Include `@RolesAllowed("ADMIN","MANAGER")` for create/update.
        *   Expose endpoint to assign/unassign courses (`POST /teachers/{id}/courses`).
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/resource/StudentResource.java
    *   **Architectural Requirements:**
        *   Provide self‑service enrollment (`POST /students/{id}/enrollments`).
        *   Enforce `@RolesAllowed("STUDENT","MANAGER","ADMIN")` for read.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/resource/EnrollmentResource.java
    *   **Architectural Requirements:**
        *   Manage enrollment lifecycle with business rules (max courses per student).
        *   Trigger notification event on creation (`@KafkaProducer`).
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/resource/AttendanceResource.java
    *   **Architectural Requirements:**
        *   Accept QR scan payload (`POST /attendance/scan`).
        *   Call `AttendanceService` ensuring idempotency.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/resource/StudentCardResource.java
    *   **Architectural Requirements:**
        *   Expose endpoint to extend validity (`PUT /studentcards/{id}/extend`).
        *   Apply `@RolesAllowed("STUDENT","MANAGER","ADMIN")`.

#### SUB-TASK 1.3: Build initial Docker image for backend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Use `quarkus:3.15.2` base image with JDK 21.
        *   Copy `target/membership-hub-runner` (Quarkus native) into final image.
        *   Set `USER 1001` for non‑root execution.
        *   Define health‑check endpoint (`/q/health`).
        *   Include `ENV QUARKUS_PROFILE=prod`.

### DAY 2: QR CODE, ATTENDANCE, NOTIFICATION & TESTING
#### SUB-TASK 2.1: Implement QR code generation and scanning utility
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/service/QRCodeService.java
    *   **Architectural Requirements:**
        *   Provide `String generateQr(String payload)` using `QRCodeWriter` (ZXing).
        *   Provide `String decodeQr(String base64Image)` with error handling.
        *   Validate payload length and characters (OWASP A03).
        *   Log all generation/decoding events for audit.

#### SUB-TASK 2.2: Implement attendance service with once‑per‑day logic and remaining days calculation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/service/AttendanceService.java
    *   **Architectural Requirements:**
        *   Method `recordAttendance(Long studentId, Long courseId, LocalDate date)` with `@Transactional` and `@Idempotent`.
        *   Query existing attendance using tenant‑filtered repository.
        *   Update `StudentCard.valid_until` by adding one day per successful attendance.
        *   Emit `@KafkaEvent(AttendanceRecorded.class)` for downstream notifications.
        *   Enforce OWASP A01: Input validation on IDs and date format.

#### SUB-TASK 2.3: Implement notification service with Kafka integration, Zalo & FCM
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/service/NotificationService.java
    *   **Architectural Requirements:**
        *   `@KafkaListener` for `AttendanceRecorded` events.
        *   Produce `ZaloMessage` and `FcmMessage` payloads.
        *   Use `ZaloApiClient` (HTTP client) with OAuth2 token rotation.
        *   Use `FcmClient` with service account credentials (encrypted at rest).
        *   Implement retry logic with exponential backoff.
        *   Log all outbound calls for audit (OWASP A09).

#### SUB-TASK 2.4: Write unit tests for QRCodeService, AttendanceService, NotificationService
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/service/QRCodeService.java;./sources/backend/src/test/java/org/nlhj/saas/membershiphub/service/QRCodeServiceTest.java
    *   **Architectural Requirements:**
        *   Test generation of valid QR strings.
        *   Test decoding of known payloads.
        *   Validate input sanitization.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/service/AttendanceService.java;./sources/backend/src/test/java/org/nlhj/saas/membershiphub/service/AttendanceServiceTest.java
    *   **Architectural Requirements:**
        *   Verify idempotent behavior (second call does not create duplicate).
        *   Validate remaining days calculation.
        *   Mock repository and Kafka producer.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/service/NotificationService.java;./sources/backend/src/test/java/org/nlhj/saas/membershiphub/service/NotificationServiceTest.java
    *   **Architectural Requirements:**
        *   Simulate Kafka event consumption.
        *   Mock Zalo and FCM clients.
        *   Assert correct message payloads.

#### SUB-TASK 2.5: Security and code review for OWASP compliance
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/domain/
    *   **Architectural Requirements:**
        *   Verify `tenant_id` presence on all entities.
        *   Confirm PII fields encrypted via `@PIIEncrypted`.
        *   Check usage of parameterized queries in repository methods.
        *   Validate password hashing uses Argon2.
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/resource/
    *   **Architectural Requirements:**
        *   Ensure `@RolesAllowed` annotations align with role matrix.
        *   Confirm `@TenantFilter` applied to all CRUD methods.
        *   Review input validation and output encoding.

### DAY 3: COURSE OVERLAP VALIDATION, RBAC, DEPLOYMENT & INTEGRATION
#### SUB-TASK 3.1: Implement course overlap validation service
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/service/CourseOverlapService.java
    *   **Architectural Requirements:**
        *   Method `boolean isOverlap(Course newCourse, List<Course> existing)` using DB indexes on `teacher_id` and `time_slot`.
        *   Throw `OverlapException` with detailed message.
        *   Enforce validation in `CourseResource` before persist.
        *   Log overlap attempts for audit.

#### SUB-TASK 3.2: Implement RBAC filter and security configuration
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershiphub/security/RBACFilter.java
    *   **Architectural Requirements:**
        *   Extend `ContainerRequestFilter` to inspect `SecurityContext`.
        *   Map roles to allowed resource paths (e.g., `/centers` → `ADMIN`).
        *   Apply tenant filtering based on `tenant_id` from JWT claims.
        *   Return `403` for unauthorized accesses.
*   **Target Path:** ./sources/backend/src/main/resources/application.yml
    *   **Architectural Requirements:**
        *   Configure `quarkus.security.jaxrs.deny-unannotated=false`.
        *   Define `quarkus.http.auth.proactive=false`.
        *   Set `quarkus.oidc.auth-enabled=true` for external OAuth2 providers.

#### SUB-TASK 3.3: Build GCP Cloud SQL and IAM definitions
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/gcp/sql-instance.yaml
    *   **Architectural Requirements:**
        *   Define `GoogleSQL` instance with `tier: db-f1-micro`.
        *   Set `databaseVersion: POSTGRES_15`.
        *   Include `settings.backupConfiguration.enabled: true`.
        *   Tag with `environment: production`.
*   **Target Path:** ./sources/backend/gcp/iam-policy.yaml
    *   **Architectural Requirements:**
        *   Bind `serviceAccount:` to `membership-hub@<project>.iam.gserviceaccount.com`.
        *   Grant `roles/cloudsql.client` and `roles/pubsub.consumer`.
        *   Enforce least‑privilege principle.

#### SUB-TASK 3.4: Create GKE deployment and service manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/k8s/deployment.yaml
    *   **Architectural Requirements:**
        *   Use image `gcr.io/<project>/membership-hub:latest`.
        *   Set `replicas: 3` with `resources.limits.cpu: 500m`.
        *   Include `readinessProbe` (`/q/health/ready`) and `livenessProbe` (`/q/health/live`).
        *   Mount ConfigMap for `application.yml`.
*   **Target Path:** ./sources/backend/k8s/service.yaml
    *   **Architectural Requirements:**
        *   Expose port `8080` with `type: LoadBalancer`.
        *   Define `selector.app: membership-hub`.
        *   Add `annotations.service.beta.kubernetes.io/google-cloud-load-balancer-type: "Internal"`.

#### SUB-TASK 3.5: Produce final Docker build script
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/build.sh
    *   **Architectural Requirements:**
        *   Execute `docker build -t gcr.io/<project>/membership-hub:${BUILD_NUMBER} .`
        *   Push to Google Artifact Registry with `docker push`.
        *   Validate image digest via `docker inspect`.

#### SUB-TASK 3.6: Execute integration/E2E test suite
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/backend/tests/IntegrationTestSuite.java
    *   **Architectural Requirements:**
        *   Orchestrates end‑to‑end flows: create center, course, teacher, student, enrollment, attendance via QR, verify notification Kafka events, and assert Zalo/FCM payloads.
        *   Uses `@QuarkusTest` and `@KafkaEmbedded` for isolated Kafka broker.
        *   Cleans up test data after each run.
        *   Reports pass/fail status to CI pipeline.

#### SUB-TASK 3.7: Run integration/E2E test suite verification
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/backend/tests/IntegrationTestSuite.java
    *   **Architectural Requirements:**
        *   Execute the suite using Maven `failsafe:integration-test`.
        *   Capture logs and generate JUnit XML report.
        *   Validate that all assertions pass (100 % success rate).
        *   If any test fails, halt pipeline and raise alert.