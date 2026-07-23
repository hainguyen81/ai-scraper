# PHASE 3 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement core student-facing features required for the membership hub:
- **Student Registration**: Create a robust registration flow that provisions a new `Student` entity with role `STUDENT`, validates uniqueness of email, securely hashes passwords, and integrates optional external authentication (Firebase/Google/Facebook) via GCP configuration.
- **Course Enrollment**: Enable students to enroll in existing courses. The enrollment service validates course availability, creates a `CourseEnrollment` record, enforces tenant isolation, and emits a Kafka event for downstream notifications.
- **Payment Processing**: Provide a mock payment gateway integration that captures payment details, creates a `Payment` entity, tracks payment status, and triggers Kafka events for payment confirmation.
- **QR Attendance & Notifications**: Wire enrollment and payment events to the existing attendance service (via Kafka) so that QR scans can update student card validity and push notifications to mobile apps and Zalo groups.
- **Frontend Integration**: Deliver Next.js pages for student registration, course enrollment, and payment UI, supporting multi‑language locale detection and responsive design for iOS/Android.
- **Observability & Compliance**: Ensure all new code follows the enterprise package layout (`org.nlh4j.saas.membership-hub`), includes proper JPA annotations, transaction demarcation, and security best practices.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Source Root**: `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/`
  - Domain models (`domain/`)
  - Repositories (`repository/`)
  - DTOs (`dto/`)
  - Services (`service/`)
  - REST resources (`resource/`)
  - Kafka producers (`kafka/`)
  - Configuration (`config/`)
- **Backend Test Root**: `./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/`
  - Service and resource unit tests
  - Kafka producer tests
- **Backend Resources**: `./sources/backend/src/main/resources/` (application.properties, validation messages)
- **Backend Container**: `./sources/backend/Dockerfile` (multi‑stage, native Quarkus image)
- **Frontend Source Root**: `./sources/frontend/src/` (pages, components, i18n)
  - Student registration page: `./sources/frontend/src/pages/student/Register.tsx`
  - Enrollment page: `./sources/frontend/src/pages/student/Enroll.tsx`
  - Payment page: `./sources/frontend/src/pages/student/Payment.tsx`
- **Frontend Tests**: `./sources/frontend/tests/` (Playwright/E2E specs)
- **Allowed REST Endpoints** (examples):
  - `POST /students` – create student
  - `POST /enrollments` – enroll student in course
  - `POST /payments` – process payment
  - `POST /attendance/qr` – record QR attendance (existing)
  - `GET /students/{id}/card` – retrieve student card days left
- **Kafka Topics**: `enrollment-events`, `payment-events`, `attendance-events`, `notification-events`
- **Package Enforcement**: Every Java source/test file under `./sources/backend/` must be under `org/nlh4j/saas/membership-hub/`.

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE)
- **Coder**: Implement domain entities, repositories, services, REST resources, Kafka producers, and frontend React/Next.js pages for registration, enrollment, and payment. Ensure all code follows the strict package‑to‑path mapping and includes proper validation, security, and transaction handling.
- **Tester**: Write unit tests for new service classes and REST resources; write integration/E2E tests for the student enrollment and payment flows using Playwright, leveraging the `INTEGRATION_SCOPE` token for cross‑component verification.
- **Reviewer**: Perform static analysis on all newly created/modified Java files to confirm package compliance, JPA correctness, transaction boundaries, and OpenAPI documentation presence.
- **Docker**: Produce a multi‑stage Dockerfile that builds the Quarkus native image, includes health‑check endpoints, and packages all new modules (student, enrollment, payment, Kafka producer).
- **GCP**: Configure external authentication provider placeholders (Firebase, Google, Facebook) and payment gateway secrets (Stripe, PayPal) in `application.properties` with environment‑specific profiles.
- **GKE**: Not required in this phase; reserved for later deployment phases.

## 4. Phase Definition of Done (DoD)
- **Functional Completion**:
  - Student registration creates a persisted `Student` with role `STUDENT`, hashed password, and optional external auth linkage.
  - Course enrollment successfully creates a `CourseEnrollment` record, emits an `EnrollmentCreated` Kafka event, and updates course capacity.
  - Payment processing creates a `Payment` record with a defined status, emits a `PaymentProcessed` Kafka event, and integrates with mock payment gateway.
  - All new REST endpoints return appropriate HTTP status codes and OpenAPI documentation.
  - Frontend pages for registration, enrollment, and payment are functional, responsive, and support locale detection.
- **Quality & Compliance**:
  - 100 % of new Java source files follow `org/nlh4j/saas/membership-hub/` package layout.
  - Unit test coverage for new services ≥ 80 % (JUnit).
  - Integration/E2E tests pass for enrollment and payment flows.
  - Static analysis passes with no violations.
- **Container & Infrastructure**:
  - Docker image builds successfully (`docker build -t membership-hub-backend .`).
  - Health‑check endpoint (`/q/health`) returns `UP`.
  - GCP configuration placeholders are present and secured.
- **Documentation**:
  - OpenAPI specs generated for new endpoints.
  - README updates for new features.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: IMPLEMENT STUDENT REGISTRATION CORE

#### SUB‑TASK 1.1: Define Student domain model and persistence layer
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/domain/Student.java
    * **Architectural Requirements:**
        * Entity annotated with `@Entity`, `@Table(name = "students")`.
        * Fields: `id`, `fullName`, `email`, `passwordHash`, `phone`, `cccd`, `centerId` (tenant), `createdAt`, `updatedAt`.
        * Use `@jakarta.persistence` annotations; embed audit fields via `@CreatedDate`/`@LastModifiedDate`.
        * Implement `equals`/`hashCode` based on `id`.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/repository/StudentRepository.java
    * **Architectural Requirements:**
        * Extend `PanacheRepositoryBase<Student, Long>`.
        * Add custom queries: `findByEmail(String email)`, `findByCenterId(Long centerId)`.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/dto/StudentDto.java
    * **Architectural Requirements:**
        * Record/DTO with fields matching `Student` except `passwordHash`.
        * Use `@com.fasterxml.jackson.annotation.JsonIgnoreProperties("passwordHash")`.

#### SUB‑TASK 1.2: Create Student service and REST resource
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/StudentService.java
    * **Architectural Requirements:**
        * `@Service` annotated class.
        * Method `registerStudent(StudentDto dto, Long centerId)` throws `EmailAlreadyExistsException`.
        * Hash password with `BCrypt`.
        * Persist `Student` entity.
        * Return `StudentDto`.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/resource/StudentResource.java
    * **Architectural Requirements:**
        * `@Path("/students")` and `@RESTController`.
        * `POST` method `@Consumes(MediaType.APPLICATION_JSON)` returning `Response`.
        * Delegate to `StudentService.registerStudent`.
        * Return HTTP 201 on success, 400 on validation errors.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/config/StudentRoleConfig.java
    * **Architectural Requirements:**
        * Configure default role `ROLE_STUDENT` with permissions for self‑management.

#### SUB‑TASK 1.3: Write unit tests for Student registration
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/StudentService.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/StudentServiceTest.java
    * **Architectural Requirements:**
        * Test `registerStudent` with valid data (success).
        * Test duplicate email throws `EmailAlreadyExistsException`.
        * Verify password hashing using BCrypt.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/resource/StudentResource.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/resource/StudentResourceTest.java
    * **Architectural Requirements:**
        * Test REST endpoint with valid payload returns 201.
        * Test invalid payload returns 400.

#### SUB‑TASK 1.4: Perform static code analysis and compliance review
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/domain/Student.java
    * **Architectural Requirements:**
        * Verify package path matches `org/nlh4j/saas/membership-hub`.
        * Ensure proper JPA annotations and no raw SQL.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/StudentService.java
    * **Architectural Requirements:**
        * Check for transaction demarcation (`@Transactional`) and exception handling.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/resource/StudentResource.java
    * **Architectural Requirements:**
        * Validate OpenAPI/Swagger annotation presence.

#### SUB‑TASK 1.5: Containerize updated backend services
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/Dockerfile
    * **Architectural Requirements:**
        * Multi‑stage Dockerfile using `eclipse-temurin:17-jdk-alpine`.
        * Copy Maven wrapper and `pom.xml`, compile Quarkus app.
        * Final stage copy built JAR, set JVM options, expose port `8080`.
        * Include health‑check endpoint `/q/health`.

#### SUB‑TASK 1.6: Provision Firebase/Google auth configuration in GCP
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/resources/application.properties
    * **Architectural Requirements:**
        * Define `firebase.project-id`, `google.client-id` placeholders.
        * Enable OAuth2 login for external providers.

### DAY 2: IMPLEMENT COURSE ENROLLMENT AND PAYMENT PROCESSING

#### SUB‑TASK 2.1: Define enrollment and payment domain models
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/domain/CourseEnrollment.java
    * **Architectural Requirements:**
        * Entity with `@ManyToOne` to `Student` and `Course`, `enrollmentDate`, `status` (`ACTIVE`, `COMPLETED`).
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/domain/Payment.java
    * **Architectural Requirements:**
        * Entity with `@ManyToOne` to `Student`, `amount`, `paymentDate`, `status` (`PENDING`, `PAID`, `FAILED`), `paymentProvider` (`STRIPE`, `PAYPAL`).
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/repository/CourseEnrollmentRepository.java
    * **Architectural Requirements:**
        * Extend `PanacheRepositoryBase<CourseEnrollment, Long>`.
        * Add `findByStudentIdAndCourseId(Long studentId, Long courseId)`.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/repository/PaymentRepository.java
    * **Architectural Requirements:**
        * Extend `PanacheRepositoryBase<Payment, Long>`.

#### SUB‑TASK 2.2: Implement enrollment service and payment service
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/CourseEnrollmentService.java
    * **Architectural Requirements:**
        * Method `enrollStudent(Long studentId, Long courseId)` throws `CourseNotFoundException`, `AlreadyEnrolledException`.
        * Check course capacity, create `CourseEnrollment`, emit Kafka event `EnrollmentCreated`.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/PaymentService.java
    * **Architectural Requirements:**
        * Method `processPayment(Long studentId, BigDecimal amount, String provider)` throws `PaymentFailedException`.
        * Integrate with mock payment gateway (e.g., `StripeMock`).
        * Create `Payment` entity, update status.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/resource/CourseEnrollmentResource.java
    * **Architectural Requirements:**
        * `POST /enrollments` endpoint, JSON payload `{studentId, courseId}`.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/resource/PaymentResource.java
    * **Architectural Requirements:**
        * `POST /payments` endpoint, JSON payload `{studentId, amount, provider}`.

#### SUB‑TASK 2.3: Implement Kafka event producer for enrollment and payment
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/kafka/KafkaEventProducer.java
    * **Architectural Requirements:**
        * `@ProducerBean` annotated class.
        * Methods `sendEnrollmentEvent(CourseEnrollment enrollment)` and `sendPaymentEvent(Payment payment)`.
        * Use `KafkaTemplate<String, String>` with topics `enrollment-events` and `payment-events`.
* **Target Path:** ./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/kafka/KafkaEventProducerTest.java
    * **Architectural Requirements:**
        * Mock `KafkaTemplate` and verify send calls.

#### SUB‑TASK 2.4: Write integration and UI tests for enrollment and payment flows
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/enrollment.spec.ts
    * **Architectural Requirements:**
        * End‑to‑end test covering student login, course selection, enrollment submission, and verification of enrollment list.
* **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/payment.spec.ts
    * **Architectural Requirements:**
        * Simulate payment process with mock gateway, assert payment success and student dashboard update.

#### SUB‑TASK 2.5: Review code quality and compliance for new services
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/domain/CourseEnrollment.java
    * **Architectural Requirements:**
        * Validate JPA mapping and tenant isolation (`centerId`).
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/CourseEnrollmentService.java
    * **Architectural Requirements:**
        * Ensure transaction annotation `@Transactional`.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/resource/PaymentResource.java
    * **Architectural Requirements:**
        * Confirm OpenAPI `@Operation` and `@APIResponse` annotations.

#### SUB‑TASK 2.6: Update Dockerfile to include new modules
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/Dockerfile
    * **Architectural Requirements:**
        * Add new modules (enrollment, payment, kafka) to Maven build (update `pom.xml` if needed).
        * Ensure multi‑stage build includes native image generation for Quarkus.

#### SUB‑TASK 2.7: Configure GCP payment provider secrets
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/resources/application.properties
    * **Architectural Requirements:**
        * Define `stripe.api-key`, `paypal.client-id` placeholders.
        * Enable conditional bean creation based on active profile.