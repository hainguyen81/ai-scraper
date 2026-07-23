# PHASE 2 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement the **Student, Course & Attendance Core** functionality required for the membership‑hub SaaS platform. This phase delivers:

* **Student Management** – registration, profile, membership card validity days, and extension API.  
* **Course Management** – CRUD (admin only), schedule definition, teacher assignment, and overlap‑prevention validation.  
* **Enrollment & Points** – enrollment by Manager or Student, automatic 10‑point accrual per registration, and point tracking.  
* **QR‑Based Attendance** – per‑student QR code generation, idempotent daily scan endpoint, attendance flag, and remaining‑days calculation.  
* **Notification Pipeline** – Zalo group SMS and mobile push triggers on enrollment, attendance, and schedule changes (service layer stub).  
* **Unit‑Test Coverage** – comprehensive tests for point accrual, overlap validation, QR scan idempotency, and attendance logic.  

All components must obey OWASP hardening (parameterized queries, tenant‑isolated `tenant_id`, input validation, and audit logging) and be containerized for GKE deployment.

## 2. Allowed Technical Scope & Directory Boundaries
All artifacts for this phase must reside under the workspace root `./sources/` and follow the topology‑aware prefixes:

* **Backend Java artifacts** – `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/`  
  * Entities, DTOs, Repositories, Services, Controllers.  
* **Backend Test artifacts** – `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/`  
  * Unit tests for core business logic.  
* **Backend Configuration & Resources** – `./sources/backend/src/main/resources/`  
  * Application‑yaml, Kafka topic definitions, validation messages.  
* **Docker Image** – `./sources/backend/Dockerfile` (multi‑stage, Java 17, Quarkus runner).  
* **No Frontend artifacts** – Phase 2 is backend‑only; any frontend references are prohibited.  

All file paths must be absolute to the workspace and start with `./sources/`. Java source files must contain the exact package segment `org/nlh4j/saas/membershiphub`.

## 3. Dedicated Sub-Agent Functional Directives
| Agent | Core Responsibilities for Phase 2 |
|-------|-----------------------------------|
| **Coder** | • Design and implement Student, Course, Enrollment, Attendance, and Point entities with tenant isolation. <br>• Create Spring Data JPA repositories using parameterized queries. <br>• Build Quarkus REST resources exposing registration, course CRUD, enrollment, QR generation, and attendance scan endpoints. <br>• Implement business rules: 10‑point accrual, overlap‑prevention for course schedules, QR idempotency, remaining‑days calculation. <br>• Integrate notification service stubs (Zalo SMS & push) with proper audit logging. <br>• Embed OWASP controls: input validation, `tenant_id` filtering, AES‑256‑GCM for PII where applicable, and secure password handling (Argon2id for student passwords). |
| **Tester** | • Write unit tests for point accrual logic, overlap validation, QR generation, and attendance idempotency. <br>• Verify tenant isolation in repository queries. <br>• Execute tests against the implemented services and assert expected behavior. |
| **Docker** | • Produce a multi‑stage `./sources/backend/Dockerfile` that builds a minimal Quarkus native image, copies compiled artifacts, and defines health‑check probes. |
| **Manager** | • Coordinate daily sub‑task assignments, validate that all generated paths respect the `./sources/` boundary and Java package rules. <br>• Ensure OWASP compliance is explicitly referenced in each Coder task. <br>• Oversee final artifact verification before phase hand‑off. |

## 4. Phase Definition of Done (DoD)
* **Functional Completion** – All core student, course, enrollment, attendance, and point features are implemented and exposed via REST endpoints.  
* **Security Compliance** – Every Java component includes tenant isolation, parameterized queries, input validation, and audit logging; OWASP A01‑A09 controls are applied.  
* **Test Coverage** – Unit tests cover point accrual, overlap validation, QR generation, and attendance idempotency; test suite passes with ≥ 90 % line coverage.  
* **Containerization** – A functional `./sources/backend/Dockerfile` builds a runnable native image.  
* **Path Compliance** – All generated files strictly follow `./sources/` prefixes and the Java package `org/nlh4j/saas/membershiphub`.  
* **Documentation** – Inline code comments and README stubs exist for each new module.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Establish Core Domain Models & Basic Services
#### SUB‑TASK 1.1: Model Student, Course, Enrollment, Attendance, and Point Entities
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Student.java
    *   **Architectural Requirements:** Define JPA entity with `tenant_id` discriminator column, fields for name, email, password hash (Argon2id), cardValidityDays, createdAt, updatedAt. Apply `@TenantFilter` for multi‑tenant query isolation. Include OWASP A03 input validation annotations (`@NotBlank`, `@Email`). Add audit fields (`createdBy`, `updatedBy`).
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Course.java
    *   **Architectural Requirements:** Entity with `tenant_id`, title, description, startDate, endDate, teacherId. Enforce overlap‑prevention via `@CourseOverlapValidator` that throws `ConstraintViolationException` on conflicting schedules.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Enrollment.java
    *   **Architectural Requirements:** Entity linking studentId and courseId, enrollmentDate, pointsAccrued (default 10). Implement `@PrePersist` to auto‑set points and audit fields.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Attendance.java
    *   **Architectural Requirements:** Entity with studentId, courseId, attendanceDate (date only), scannedQrToken (hashed). Ensure idempotency via unique constraint on (`studentId`, `attendanceDate`). Apply OWASP A02 protection against injection in `scannedQrToken` handling.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/PointBalance.java
    *   **Architectural Requirements:** Entity tracking studentId, totalPoints, lastUpdated. Use `@TenantFilter` for query safety.

#### SUB‑TASK 1.2: Create Spring Data JPA Repositories with Tenant Isolation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/StudentRepository.java
    *   **Architectural Requirements:** Extends `JpaRepository<Student, Long>`. Add custom query methods filtered by `tenant_id` using `@Query("SELECT s FROM Student s WHERE s.tenantId = :tenantId")`. Apply parameterized query syntax to prevent SQL injection.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/CourseRepository.java
    *   **Architectural Requirements:** Includes `findOverlappingCourses(tenantId, startDate, endDate)` method; implement overlap validation logic in service layer.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/EnrollmentRepository.java
    *   **Architectural Requirements:** Add `findByStudentIdAndCourseId` with tenant filter.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/AttendanceRepository.java
    *   **Architectural Requirements:** Enforce unique constraint via `@Table(uniqueConstraints = @UniqueConstraint(columnNames = {"student_id", "attendance_date"})`). Provide `findByStudentIdAndAttendanceDate` method.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/PointBalanceRepository.java
    *   **Architectural Requirements:** Standard CRUD; include tenant filter in all derived queries.

#### SUB‑TASK 1.3: Implement Core Services (StudentService, CourseService, EnrollmentService, AttendanceService, PointService)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/StudentService.java
    *   **Architectural Requirements:** Methods `registerStudent(StudentDto)`, `extendCardValidity(Long studentId, int days)`. Validate input via `@Valid`. Hash password with Argon2id. Log activity with `SecurityContextHolder`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java
    *   **Architectural Requirements:** Methods `createCourse(CourseDto)`, `updateCourse`, `assignTeacher`. Enforce overlap‑prevention by calling `courseRepository.findOverlappingCourses` and throwing `BusinessException`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/EnrollmentService.java
    *   **Architectural Requirements:** `enrollStudent(Long studentId, Long courseId)` auto‑creates `Enrollment` with 10 points, persists `PointBalance`. Use `@Transactional` to ensure atomicity. Apply tenant isolation via repository filters.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java
    *   **Architectural Requirements:** `scanQrCode(String qrToken, Long studentId)` validates token, checks existing attendance for the day, creates new `Attendance` if absent. Return remaining card days via `calculateRemainingDays(studentId)`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/PointService.java
    *   **Architectural Requirements:** `addPoints(Long studentId, int points)` updates `PointBalance`. Ensure audit logging and OWASP A07 protection against logic flaws.

#### SUB‑TASK 1.4: Develop QR Code Generation Utility
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/util/QRCodeGenerator.java
    *   **Architectural Requirements:** Static method `generateQrCodeForStudent(Student student)` returning byte[] (PNG). Use `QRCodeWriter` from `com.google.zxing`. Store generated QR token in `Student.qrTokenHash` (hashed with SHA‑256). Ensure token is tenant‑scoped.

#### SUB‑TASK 1.5: Write Unit Tests for Point Accrual and Overlap Validation
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/EnrollmentService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/EnrollmentServiceTest.java
    *   **Architectural Requirements:** Test enrollment triggers 10‑point accrual, verify `PointBalance` update, and assert tenant isolation. Use `@DataJpaTest` and `@MockBean` for repositories.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/CourseServiceTest.java
    *   **Architectural Requirements:** Validate overlap‑prevention throws `BusinessException` when scheduling conflicting courses; ensure valid courses are accepted.

### DAY 2: Implement Attendance Scan Endpoint, Notification Pipeline, and Containerization
#### SUB‑TASK 2.1: Create REST Resources for Student & Course Management
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/rest/StudentResource.java
    *   **Architectural Requirements:** JAX‑RS `@POST /students` for registration, `@PUT /students/{id}/card-extension` for validity extension. Validate request bodies, enforce tenant isolation via `SecurityContext`, return appropriate HTTP status codes.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/rest/CourseResource.java
    *   **Architectural Requirements:** `@GET /courses` (public list), `@POST /courses` (admin only), `@PUT /courses/{id}` (admin), `@POST /courses/{id}/assign-teacher/{teacherId}` (admin). All endpoints apply `@TenantFilter` and input validation.

#### SUB‑TASK 2.2: Implement Attendance Scan Endpoint and Remaining‑Days Calculation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/rest/AttendanceResource.java
    *   **Architectural Requirements:** `@POST /attendance/scan` consumes `QrScanRequest` (qrToken, studentId). Service calls `attendanceService.scanQrCode`. Returns `AttendanceResponse` with scanned status and remainingCardDays. Ensure idempotency via unique constraint and proper error handling (`HttpStatus.CONFLICT` if already scanned today).
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java
    *   **Architectural Requirements:** Add method `calculateRemainingDays(Long studentId)` that computes days left based on `cardValidityDays` minus days since last attendance. Use `java.time.LocalDate` arithmetic. Log each calculation for audit.

#### SUB‑TASK 2.3: Build Notification Service Stub (Zalo SMS & Mobile Push)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java
    *   **Architectural Requirements:** Interface with placeholder implementations `ZaloSmsNotifier` and `FcmPushNotifier`. Methods `notifyEnrollment(Enrollment enrollment)`, `notifyAttendance(Attendance attendance)`, `notifyScheduleChange(Course course)`. All methods include tenant‑scoped logging and OWASP A06 rate‑limiting stub (`@RateLimited`). Ensure no real external calls; return `CompletableFuture<Void>`.

#### SUB‑TASK 2.4: Write Unit Tests for Attendance Idempotency and Remaining‑Days Logic
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AttendanceServiceTest.java
    *   **Architectural Requirements:** Test duplicate QR scans on same day return conflict, test successful scan creates attendance, verify `calculateRemainingDays` returns correct value after attendance. Use `@MockBean` for `StudentRepository` and `AttendanceRepository`.

#### SUB‑TASK 2.5: Produce Backend Dockerfile for GKE Deployment
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/Dockerfile
    *   **Architectural Requirements:** Multi‑stage build: (1) Build stage using Maven/Gradle to compile Quarkus app, (2) Runtime stage using `ubi9-minimal` with OpenJDK 21, copy native image or jar, expose port `8080`, define health‑check (`curl http://localhost:8080/qhealth`). Include labels for `nlh4j.saas.membershiphub` and OWASP compliance metadata.

#### SUB‑TASK 2.6: Final Phase Validation & Hand‑off
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/README-Phase2.md
    *   **Architectural Requirements:** Summarize implemented modules, endpoint specifications, test coverage, Docker usage, and OWASP hardening applied. Ensure all paths referenced are absolute (`./sources/...`). Validate that no file resides outside `./sources/`. Confirm Java package compliance (`org/nlh4j/saas/membershiphub`). Provide checklist for reviewer.