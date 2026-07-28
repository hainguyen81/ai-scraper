# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Consolidate the three core backend microservices—**Authentication**, **Course Management**, and **Student Management**—into a unified integration layer that provides end‑to‑end service orchestration for the membership‑hub platform.
- Ensure the integration layer respects **multi‑tenant isolation** (`tenant_id` scopes), enforces **OWASP‑compliant security controls** (AES‑256 PII encryption, parameterized queries, input validation), and maintains **scalable, loosely‑coupled communication** via the existing Kafka event bus.
- Deliver a single, coherent API surface that can be consumed by the web admin UI, mobile student app, and any future client extensions while preserving the existing service contracts.
- Validate the integrated flow through comprehensive **integration tests** that exercise authentication token issuance, course enrollment workflows, and student record updates across service boundaries.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Java artifacts** must reside under:
  - `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` (service, controller, config)
  - `./sources/backend/src/main/resources/` (application.yml, kafka topics)
  - `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/` (unit & integration tests)
  - `./sources/backend/src/test/resources/` (test configs)
- **REST endpoint patterns** (all prefixed with `/api/v1`):
  - `POST /auth/token` – authentication integration entry point
  - `GET /courses` – course management retrieval
  - `POST /students` – student management creation
  - `PUT /students/{id}/enroll` – enrollment linking courses to students
- **Kafka topics** (pre‑existing, no creation required):
  - `auth-events`, `course-events`, `student-events`
- **Frontend assets** are **not** part of this phase; only backend integration and its integration tests are in scope.

## 3. Dedicated Sub-Agent Functional Directives
| Agent | Functional Directives for Phase 4 |
|-------|-----------------------------------|
| **coder** | Implement the integration layer that wires Authentication, Course Management, and Student Management services together. Ensure OWASP A01–A03 controls (multi‑tenant `tenant_id`, AES‑256 encryption for sensitive data, parameterized queries) are embedded in every service call. |
| **tester** | Develop integration test suites that validate end‑to‑end workflows across the three services. Tests must cover authentication token flow, course enrollment, and student record updates, exercising Kafka event propagation and tenant isolation. |
| **reviewer** | Perform static code analysis and compiler checks on each Java source file created/modified by the **coder** agent. Verify OWASP compliance annotations and package naming conventions. |
| **doc** | Produce comprehensive technical documentation for the new integration layer: API contracts, data flow diagrams, security controls matrix, and integration test reports. All documentation must be stored under `./sources/backend/docs/`. |
| **docker** | No tasks assigned in this phase. |
| **GCP** | No tasks assigned in this phase. |
| **GKE** | No tasks assigned in this phase. |

## 4. Phase Definition of Done (DoD)
- **Integration Layer**: A fully functional `IntegrationService` (or equivalent) that orchestrates Authentication, Course Management, and Student Management with tenant‑aware routing and security controls.
- **Security Compliance**: All integration code includes explicit OWASP controls (multi‑tenant `tenant_id` scopes, AES‑256 encryption for PII, parameterized queries) and passes static security linting.
- **Integration Test Coverage**: End‑to‑end integration tests for authentication token issuance, course enrollment, and student record updates achieve **≥ 95 %** functional coverage and validate Kafka event propagation.
- **Documentation**: Complete technical docs (`./sources/backend/docs/IntegrationLayer.adoc`) describing APIs, data flows, security controls, and test results.
- **Code Quality**: All Java source files conform to the package layout `org.nlh4j.saas.membershiphub` and pass reviewer validation without compilation errors.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Establish Authentication Integration
#### SUB‑TASK 1.1: Implement Authentication Service Integration
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthenticationIntegrationService.java`
    *   **Architectural Requirements:**
        *   Expose a method `authenticate(String tenantId, AuthRequest request)` that delegates to the existing `AuthenticationService` while injecting the `tenantId` into the request context for multi‑tenant isolation.
        *   Apply **AES‑256** encryption to any sensitive tokens returned (e.g., refresh tokens) using a tenant‑specific key.
        *   Use **parameterized queries** for all database accesses within this service.
        *   Emit an `auth-events` Kafka record containing the authentication outcome and tenant identifier.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-004], [ARC-004], [NFR-006]

#### SUB‑TASK 1.2: Integration Test for Authentication Flow
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `INTEGRATION_SCOPE;./sources/backend/tests/AuthenticationIntegrationTest.java`
    *   **Architectural Requirements:**
        *   Simulate a multi‑tenant authentication request, verify token encryption, and assert that the correct `auth-events` Kafka message is produced.
        *   Validate tenant isolation by ensuring a tenant cannot access another tenant’s authentication data.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-004], [NFR-007]

### DAY 2: Integrate Course Management Service
#### SUB‑TASK 2.1: Implement Course Management Integration
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseManagementIntegrationService.java`
    *   **Architectural Requirements:**
        *   Provide CRUD operations (`listCourses(tenantId)`, `createCourse(tenantId, CourseDto)`, `assignTeacher(tenantId, courseId, teacherId)`) that call the underlying `CourseManagementService`.
        *   Enforce **parameterized queries** for all course data accesses.
        *   Store course metadata encrypted at rest using **AES‑256** with a tenant‑scoped key.
        *   Emit `course-events` Kafka messages for each state change.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-004], [ARC-004], [NFR-006]

#### SUB‑TASK 2.2: Integration Test for Course Management Workflow
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `INTEGRATION_SCOPE;./sources/backend/tests/CourseManagementIntegrationTest.java`
    *   **Architectural Requirements:**
        *   Exercise the full course lifecycle (create, list, assign teacher) across two different tenants.
        *   Verify encryption of sensitive course fields and that `course-events` are correctly published.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-004], [NFR-007]

### DAY 3: Integrate Student Management Service
#### SUB‑TASK 3.1: Implement Student Management Integration
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/StudentManagementIntegrationService.java`
    *   **Architectural Requirements:**
        *   Expose methods `enrollStudent(tenantId, StudentDto)`, `updateStudentRecord(tenantId, studentId, updates)`, and `getStudentStatus(tenantId, studentId)`.
        *   Apply **multi‑tenant `tenant_id` scoping** to all queries and enforce **parameterized queries** to prevent SQL injection.
        *   Encrypt personal identifiers (e.g., SSN, contact info) using **AES‑256** with tenant‑specific keys.
        *   Emit `student-events` Kafka messages for enrollment and status changes.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-004], [ARC-004], [NFR-006]

#### SUB‑TASK 3.2: Integration Test for Student Management Workflow
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `INTEGRATION_SCOPE;./sources/backend/tests/StudentManagementIntegrationTest.java`
    *   **Architectural Requirements:**
        *   Validate student enrollment, record updates, and status retrieval across multiple tenants.
        *   Confirm encryption of PII fields and proper emission of `student-events`.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-004], [NFR-007]

### DAY 4: Consolidate Integration Documentation & Review
#### SUB‑TASK 4.1: Produce Integration Layer Documentation
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/docs/IntegrationLayer.adoc`
    *   **Architectural Requirements:**
        *   Include API contracts for Authentication, Course, and Student integration endpoints.
        *   Document data flow diagrams, Kafka event schemas, and security controls (tenant isolation, AES‑256 encryption, parameterized queries).
        *   Capture test results and coverage metrics.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-004], [NFR-006]

#### SUB‑TASK 4.2: Static Code Review of Integration Services
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthenticationIntegrationService.java`
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseManagementIntegrationService.java`
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/StudentManagementIntegrationService.java`
    *   **Architectural Requirements:**
        *   Verify package naming (`org.nlh4j.saas.membershiphub`), OWASP compliance annotations, and absence of hardcoded credentials.
        *   Ensure all database calls use parameterized queries.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-004], [NFR-006]

### DAY 5: Final Integration Validation & Sign‑off
#### SUB‑TASK 5.1: End‑to‑End Integration Test Suite Execution
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `INTEGRATION_SCOPE;./sources/backend/tests/FullIntegrationTestSuite.java`
    *   **Architectural Requirements:**
        *   Run the three integration test scenarios sequentially, verifying cross‑service data consistency and Kafka event propagation.
        *   Assert tenant isolation and encryption safeguards across all three domains.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-004], [NFR-007]

#### SUB‑TASK 5.2: Documentation Review & Archive
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/docs/IntegrationLayer.adoc`
    *   **Architectural Requirements:**
        *   Incorporate reviewer comments, update diagrams, and finalize test result annexes.
        *   Ensure all OWASP control references are explicitly listed.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-004], [NFR-006]

--- 

*Phase 4 execution complete upon fulfillment of all DoD criteria and successful passage of the integration test suite.*