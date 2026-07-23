# PHASE 2 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement core attendance, enrollment, notification, promotion/announcement, and AI CSKH capabilities for the membership‑hub platform. Specific deliverables:
- QR attendance service with single‑day flag, Kafka `attendance` topic emission, and tenant‑scoped persistence.
- Student card day‑counter model that decrements on attendance and supports re‑activation.
- Notification engine supporting Zalo SMS group messages, FCM/native push, and Kafka `notifications`/`zalo-message` topics.
- CRUD services for Courses, Teachers, Students, Enrollments with tenant isolation and role‑based access.
- Promotion and Announcement management (full CRUD, tenant filter, automatic broadcast to groups and mobile apps).
- AI CSKH chat scaffold (float UI, intent routing, placeholder NLP integration).
- All components must embed OWASP A01‑A07 controls (parameterized queries, tenant filtering, AES‑256 PII encryption at rest, JWT revocation, secure CORS).

## 2. Allowed Technical Scope & Directory Boundaries
- **Backend Java (Quarkus) source tree**
  - `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/`  
    - `service/` – business services (AttendanceService, StudentCardService, NotificationService, EnrollmentService, PromotionService, AnnouncementService, AiChatService)  
    - `repository/` – JPA repositories (AttendanceRepository, StudentCardRepository, CourseRepository, TeacherRepository, StudentRepository, EnrollmentRepository, PromotionRepository, AnnouncementRepository)  
    - `model/` – entity POJOs (AttendanceRecord, StudentCard, Course, Teacher, Student, Promotion, Announcement)  
    - `dto/` – data transfer objects (EnrollmentDto, NotificationDto)  
    - `config/` – Kafka producer/consumer config, tenant filter interceptors, encryption keys  
  - `./sources/backend/src/main/resources/` – application.yml, Kafka topic definitions, migration scripts  
  - `./sources/backend/docker/` – multi‑stage Dockerfile, Jib config  
- **Frontend (Next.js Web & Mobile)**
  - `./sources/frontend/web/` – admin dashboard pages, i18n resources, role‑based guards, QR scanner integration, real‑time dashboard (15 min polling)  
  - `./sources/frontend/mobile/` – Capacitor/React‑Native app, shared i18n, push notification handlers, QR scanner native module  
- **Testing**
  - `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/` – unit & integration test suites  
  - `./sources/frontend/web/tests/` – Cypress/E2E specs  
  - `./sources/frontend/mobile/tests/` – Detox/Jest mobile specs  
- **DevOps**
  - `./sources/backend/docker/Dockerfile` – final image  
  - `./sources/backend/k8s/` – GKE deployment YAMLs (Deployment, Service, ConfigMap, Secret)  
  - `./sources/ci/` – GitHub Actions workflow (Cloud Build → GKE)  

All paths strictly obey the `./sources/` root rule; no files are generated outside this hierarchy.

## 3. Dedicated Sub-Agent Functional Directives
### Coder
- Implement AttendanceService with `scanQr(studentId, tenantId)` that writes a single‑day AttendanceRecord, emits to Kafka `attendance`, and updates StudentCard day counter.
- Create StudentCard entity and service for decrement/increment logic with tenant isolation.
- Build NotificationService and NotificationEngine supporting Zalo SMS REST calls, FCM/APNs push, and Kafka `notifications`/`zalo-message` producers.
- Develop EnrollmentService CRUD covering Course, Teacher, Student, and Enrollment entities; enforce tenant filtering and role‑based validation.
- Implement PromotionService and AnnouncementService with full CRUD, tenant filter, and automatic broadcast triggers.
- Scaffold AiChatService and a float UI component in `./sources/frontend/web/src/components/ai-chat/` with intent routing placeholder.
- Write Kafka producer/consumer configuration in `./sources/backend/src/main/resources/application.yml` and interceptor for tenant validation.
- Produce OWASP‑compliant code (parameterized queries, AES‑256 encryption for PII fields, secure headers, CORS policies).

### Tester
- Unit test AttendanceService, StudentCardService, NotificationService, EnrollmentService using JUnit5/Mockito; target paths follow `<source>;<test>` syntax.
- Integration test Kafka attendance flow using EmbeddedKafka; target path `INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/integration/AttendanceKafkaIT.java`.
- E2E test QR attendance via web UI and mobile app; target path `INTEGRATION_SCOPE;./sources/frontend/web/tests/attendance.spec.ts`.
- UI test promotion/announcement CRUD and broadcast; target path `INTEGRATION_SCOPE;./sources/frontend/web/tests/promotion.spec.ts`.

### Reviewer
- Perform static code analysis on all Java sources for OWASP compliance, tenant leakage, and package naming.
- Review Dockerfiles for multi‑stage best practices and size optimization.
- Validate i18n/SEO implementation in frontend assets.

### Docker
- Create multi‑stage Dockerfile in `./sources/backend/docker/Dockerfile` with Jib or classic build.
- Include application layer caching, non‑root user, and health‑check endpoint.
- Build and push image to GCP Artifact Registry via Cloud Build.

### GCP
- Configure GCP IAM service accounts with minimal roles (Cloud Deploy, Artifact Registry, Cloud SQL, Pub/Sub, Cloud Scheduler).
- Set up Cloud Build trigger in `./sources/ci/build.yaml` to auto‑build and deploy Docker image.
- Provision Cloud SQL instance with PostgreSQL, enable logical replication for multi‑tenant isolation.

### GKE
- Generate K8s manifests in `./sources/backend/k8s/` (Deployment, Service, Ingress, ConfigMap, Secret).
- Include tenant‑aware resource quotas, PodSecurityPolicies, and autoscaling.
- Apply manifests via gcloud CLI or Cloud Deploy pipeline.

### Manager
- Coordinate cross‑agent progress, ensure all sub‑tasks are completed within Phase 2 window.
- Validate that every generated file respects the `./sources/` boundary and Java package rule.
- Approve final Phase 2 sign‑off after all functional and security checks are verified.

## 4. Phase Definition of Done (DoD)
- **Functional Coverage**
  - QR attendance service functional with Kafka emission (100 % unit test coverage).
  - Student card day‑counter logic validated (unit tests >90 %).
  - Notification engine capable of sending Zalo SMS, FCM, and native push (integration tested).
  - Enrollment CRUD fully implemented with tenant filtering (unit tests >95 %).
  - Promotion & Announcement management with auto‑broadcast (end‑to‑end tested).
  - AI CSKH scaffold UI component present and wired to service (smoke tested).
- **Security & Compliance**
  - All Java code passes OWASP A01‑A07 checks (no SQL injection, proper tenant isolation, AES‑256 encryption for PII).
  - JWT tokens include role and tenant claims; revocation list maintained.
  - All REST endpoints enforce CORS, rate‑limiting, and input validation.
- **DevOps & Deployment**
  - Docker image built, scanned, and pushed to Artifact Registry.
  - GKE manifests ready for rollout; Cloud Build pipeline configured.
  - CI/CD pipeline triggers on code commit and passes all tests.
- **Documentation & Governance**
  - All source files located under `./sources/` with correct Java package naming.
  - No files generated outside the workspace root.
  - Phase 2 acceptance criteria met; ready for Phase 3 frontend implementation.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Core Attendance & Card Logic + Initial Scaffolding
#### SUB‑TASK 1.1: Implement AttendanceService and StudentCard model
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java
    *   **Architectural Requirements:**
        *   Use Quarkus `@Transactional` and `@RolesAllowed` for tenant‑scoped access.
        *   Emit `AttendanceRecord` to Kafka topic `attendance` via `@KafkaProducer`.
        *   Call `StudentCardService.decrementDays(studentId, tenantId)` after successful attendance.
        *   Apply OWASP A03 (SQL Injection) via `@Transactional` and parameterized queries in repository.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/StudentCard.java
    *   **Architectural Requirements:**
        *   Annotate with `@Entity` and `@TenantFilter` interceptor.
        *   Store encrypted `remainingDays` using AES‑256 (`@EncryptField`).
        *   Include `@CreatedTimestamp` and `@LastModifiedTimestamp` for audit.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/AttendanceRepository.java
    *   **Architectural Requirements:**
        *   Extend `JpaRepository<AttendanceRecord, Long>`.
        *   Add custom query `findByStudentIdAndTenantIdAndDate` with `@Query` using parameter binding.
        *   Implement tenant filter via `@TenantId` JPA interceptor.

#### SUB‑TASK 1.2: Build NotificationService skeleton and Kafka config
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java
    *   **Architectural Requirements:**
        *   Define interfaces `sendZaloSms(String phone, String message)`, `sendPush(Student student, String payload)`.
        *   Include `@KafkaListener` for consuming `notifications` and `zalo-message` topics.
        *   Enforce OWASP A01 (Broken Access Control) by validating tenant and roles before sending.
*   **Target Path:** ./sources/backend/src/main/resources/application.yml
    *   **Architectural Requirements:**
        *   Configure Kafka bootstrap servers, `attendance`, `notifications`, `zalo-message` topics.
        *   Define `tenant.id` property injection via `TenantContext`.
        *   Enable `quarkus.hibernate.orm.multitenancy` with `DATA_SOURCE` strategy.

#### SUB‑TASK 1.3: Create Promotion & Announcement entities & repositories
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/Promotion.java
    *   **Architectural Requirements:**
        *   `@Entity` with fields `title`, `description`, `validFrom`, `validTo`, `tenantId`.
        *   Apply `@EncryptField` for any PII in description.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/PromotionRepository.java
    *   **Architectural Requirements:**
        *   Extend `JpaRepository<Promotion, Long>`.
        *   Add `findByTenantId` with tenant filter.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/Announcement.java
    *   **Architectural Requirements:**
        *   Similar structure to Promotion with `isBroadcast` flag.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/AnnouncementRepository.java
    *   **Architectural Requirements:**
        *   Extend `JpaRepository<Announcement, Long>` with tenant filter.

#### SUB‑TASK 1.4: Scaffold AI CSKH service and UI component
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AiChatService.java
    *   **Architectural Requirements:**
        *   Provide `String respond(String userId, String message)` stub.
        *   Integrate with external NLP placeholder (to be wired later).
        *   Enforce tenant isolation via `TenantContext`.
*   **Target Path:** ./sources/frontend/web/src/components/ai-chat/AiChatFloat.jsx
    *   **Architectural Requirements:**
        *   Render float button, chat window, i18n messages via `useTranslation`.
        *   Call `AiChatService.respond` via API endpoint.
        *   Implement auto‑refresh every 30 s for new intents.

#### SUB‑TASK 1.5: Create multi‑stage Docker image for backend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Use `quarkus:3.15` base image.
        *   Copy `target/*-runner` (native image) or `jar` based on build.
        *   Set non‑root user, health‑check endpoint `/q/health`.
        *   Include `jlink` for reduced size; embed Kafka client libraries.
        *   Apply OWASP A09 (Security Misconfiguration) – remove debug flags, restrict exposed ports.

#### SUB‑TASK 1.6: Review all generated Java code for OWASP compliance
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/
    *   **Architectural Requirements:**
        *   Verify parameterized queries in all repository methods.
        *   Confirm tenant filtering annotations present.
        *   Validate encryption usage for PII fields.
        *   Ensure role‑based access control (`@RolesAllowed`) on service methods.

### DAY 2: Notification Engine, Enrollment CRUD, Promotion/Announcement Management, AI Integration, CI/CD & Deployment
#### SUB‑TASK 2.1: Implement NotificationEngine (Zalo SMS, FCM, APNs)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationEngine.java
    *   **Architectural Requirements:**
        *   Concrete implementation of `NotificationService`.
        *   Use `RestTemplate` for Zalo SMS API (`POST /send`).
        *   Integrate `FcmMessaging` for Android push and `ApnsManager` for iOS.
        *   Emit `NotificationEvent` to Kafka `notifications` topic after successful dispatch.
        *   Apply OWASP A02 (Cryptographic Failures) – store API keys encrypted in `Secret` resource.

#### SUB‑TASK 2.2: Develop EnrollmentService with Course, Teacher, Student CRUD
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/EnrollmentService.java
    *   **Architectural Requirements:**
        *   Methods: `enrollStudent(studentId, courseId, teacherId)`, `removeEnrollment`, `getEnrollments(tenantId)`.
        *   Validate that teacher belongs to tenant and course exists.
        *   Trigger `EnrollmentEvent` to Kafka `enrollments` topic.
        *   Use `@Transactional` and `@RolesAllowed` for role enforcement.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/CourseRepository.java
    *   **Architectural Requirements:**
        *   Extend `JpaRepository<Course, Long>` with tenant filter.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/TeacherRepository.java
    *   **Architectural Requirements:**
        *   Extend `JpaRepository<Teacher, Long>` with tenant filter.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/StudentRepository.java
    *   **Architectural Requirements:**
        *   Extend `JpaRepository<Student, Long>` with tenant filter.

#### SUB‑TASK 2.3: Complete Promotion & Announcement management (full CRUD + broadcast)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/controller/PromotionController.java
    *   **Architectural Requirements:**
        *   Expose REST endpoints `POST /promotions`, `GET /promotions`, `PUT /promotions/{id}`, `DELETE /promotions/{id}`.
        *   Validate `validFrom`/`validTo` logic.
        *   On create/update, publish `PromotionEvent` to Kafka `promotions` topic.
        *   Enforce `@RolesAllowed("ADMIN","MANAGER")`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/controller/AnnouncementController.java
    *   **Architectural Requirements:**
        *   Similar CRUD with `isBroadcast` flag.
        *   When `isBroadcast=true`, trigger `AnnouncementEvent` to Kafka `announcements`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/PromotionService.java
    *   **Architectural Requirements:**
        *   Business logic for validation, tenant filtering, and Kafka emission.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AnnouncementService.java
    *   **Architectural Requirements:**
        *   Business logic for broadcast and tenant isolation.

#### SUB‑TASK 2.4: Wire AI CSKH UI to backend service
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/web/src/pages/ai-chat.tsx
    *   **Architectural Requirements:**
        *   Server‑Side Props fetch initial messages via `/api/ai/chat`.
        *   Client‑side `useEffect` subscribes to WebSocket for real‑time responses.
        *   Apply i18n via `useTranslation('ai')`.
*   **Target Path:** ./sources/frontend/web/src/api/ai.ts
    *   **Architectural Requirements:**
        *   Axios wrapper calling `POST /api/ai/respond` which delegates to `AiChatService`.
        *   Include request interceptor for JWT token.

#### SUB‑TASK 2.5: Write unit tests for Attendance, StudentCard, Notification, Enrollment services
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AttendanceServiceTest.java
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/StudentCard.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/StudentCardServiceTest.java
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationEngine.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/NotificationEngineTest.java
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/EnrollmentService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/EnrollmentServiceTest.java

#### SUB‑TASK 2.6: Integration test Kafka attendance flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/integration/AttendanceKafkaIT.java
    *   **Architectural Requirements:**
        *   Use `@EmbeddedKafka` to start Kafka broker.
        *   Produce a sample `AttendanceRecord` via `AttendanceService`.
        *   Consume from `attendance` topic and assert payload.
        *   Verify that `StudentCard` day counter is updated accordingly.

#### SUB‑TASK 2.7: Build final Docker image and push to Artifact Registry
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Add stage `builder` with Maven/Gradle to compile native image.
        *   Add stage `runtime` with minimal JRE.
        *   Include `COPY --from=builder` of native executable.
        *   Set environment variables for Kafka, DB, tenant config.
        *   Add `ENTRYPOINT` with `java -jar app.jar`.

#### SUB‑TASK 2.8: Generate GKE deployment manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/k8s/deployment.yaml
    *   **Architectural Requirements:**
        *   `apiVersion: apps/v1`, `kind: Deployment` with image from Artifact Registry.
        *   Pod template includes `imagePullSecrets`, resource limits, liveness/probe.
        *   Add `env` for `TENANT_ID`, `KAFKA_BOOTSTRAP`, `DB_URL`.
        *   Include `securityContext` runAsNonRoot.
*   **Target Path:** ./sources/backend/k8s/service.yaml
    *   **Architectural Requirements:**
        *   `kind: Service` expose port 8080.
*   **Target Path:** ./sources/backend/k8s/configmap.yaml
    *   **Architectural Requirements:**
        *   Mount `application.yml` as ConfigMap.
*   **Target Path:** ./sources/backend/k8s/secret.yaml
    *   **Architectural Requirements:**
        *   Store encrypted DB credentials and third‑party API keys.

#### SUB‑TASK 2.9: Configure GCP IAM, Cloud Build pipeline, and CI/CD trigger
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/ci/build.yaml
    *   **Architectural Requirements:**
        *   Define Cloud Build steps: `mvn package`, `docker build`, `docker push`.
        *   Include `steps` for `gcloud secrets versions add` for sensitive data.
        *   Add `substitutions` for `*_IMAGE_NAME`.
*   **Target Path:** ./sources/ci/iam-policy.json
    *   **Architectural Requirements:**
        *   Grant `roles/cloudsql.user` to service account.
        *   Grant `roles/pubsub.producer`, `roles/pubsub.consumer`.
        *   Grant `roles/artifactregistry.writer` for backend images.
        *   Grant `roles/container.admin` for GKE deployment.

#### SUB‑TASK 2.10: Manager final validation and Phase 2 sign‑off
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/
    *   **Architectural Requirements:**
        *   Verify all generated files reside under `./sources/` with correct Java package `org.nlh4j.saas.membershiphub`.
        *   Confirm OWASP compliance checklist completed for each service.
        *   Ensure Docker image built, scanned, and pushed.
        *   Validate GKE manifests syntax via `kubectl dry-run`.
        *   Approve CI/CD pipeline configuration and IAM policies.
        *   Sign off Phase 2 deliverables and hand over to Phase 3.