# PHASE 3 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Implement course management and student management services using Java 17 and Quarkus within a multi‑tenant architecture.  
- Provide full CRUD, enrollment, scheduling, and tenant‑isolated operations for courses and students.  
- Enforce OWASP best practices: tenant‑scoped `tenant_id` filtering, AES‑256 encryption of PII, parameterized queries, and comprehensive audit logging.  
- Expose RESTful endpoints (`/api/v1/courses`, `/api/v1/students`) with OpenAPI documentation and role‑based access control.  
- Develop unit tests achieving ≥ 90 % branch coverage for service layers and ≥ 85 % for repository layers, validating security and business rules.  
- Align with allocated requirement tags: `[REQ-003]`, `[ARC-003]`, `[NFR-004]`, `[NFR-005]`.

## 2. Allowed Technical Scope & Directory Boundaries
- **Backend root:** `./sources/backend/`  
- **Java package foundation:** `org.nlh4j.saas.membershiphub` (lowercase token `membershiphub`)  
- **Core service artifacts:**  
  * `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java`  
  * `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course/CourseRepository.java`  
  * `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course/CourseResource.java`  
  * `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/student/StudentService.java`  
  * `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/student/StudentRepository.java`  
  * `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/student/StudentResource.java`  
- **Configuration & integration:**  
  * `./sources/backend/src/main/resources/application.yml` (multi‑tenancy, datasource, Kafka settings)  
  * `./sources/backend/src/main/resources/kafka/topics.properties`  
- **Test artifacts:**  
  * `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/course/CourseServiceTest.java`  
  * `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/course/CourseRepositoryTest.java`  
  * `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/student/StudentServiceTest.java`  
  * `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/student/StudentRepositoryTest.java`  
- **Documentation (doc agent):** `./sources/backend/docs/` for architecture diagrams, OpenAPI specs, and design documents.  
- **Reviewer scope:** Individual Java source files under `./sources/backend/src/main/java/` and `./sources/backend/src/test/java/` for static analysis and compiler validation.  

## 3. Dedicated Sub-Agent Functional Directives
- **coder:**  
  * Implement `CourseService`, `CourseRepository`, `CourseResource` and `StudentService`, `StudentRepository`, `StudentResource`.  
  * Embed tenant‑id scoping, AES‑256 encryption for PII, and parameterized queries throughout.  
  * Configure Kafka producers for enrollment notifications and integrate with existing notification flows.  
  * Generate OpenAPI contracts and ensure Jakarta Validation on request payloads.  
- **tester:**  
  * Write unit tests for all service and repository classes, mocking Kafka and repositories.  
  * Validate tenant isolation, encryption handling, and parameterized query usage.  
  * Achieve required coverage thresholds and verify security constraints.  
- **doc:**  
  * Produce architecture diagrams, API documentation (OpenAPI YAML), and detailed design specs stored under `./sources/backend/docs/`.  
- **reviewer:**  
  * Perform static code analysis and compiler checks on each Java source file to enforce OWASP guidelines and code quality.  

## 4. Phase Definition of Done (DoD)
- All course and student service endpoints functional, secured, and documented.  
- Unit test coverage ≥ 90 % for service layers and ≥ 85 % for repository layers.  
- OWASP compliance verified: tenant isolation, AES‑256 PII encryption, parameterized queries, audit logging.  
- All artifacts placed under correct `./sources/` directory structure with proper Java package naming.  
- Documentation and OpenAPI specs generated and stored in `./sources/backend/docs/`.  

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Implement Core Course Management Service
#### SUB-TASK 1.1: Develop CourseService and CourseRepository
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java
    *   **Architectural Requirements:**
        *   Implement CRUD operations for Course entity, include tenant_id filtering for multi-tenancy.
        *   Use Panache JPA for repository integration; inject CourseRepository.
        *   Apply AES-256 encryption for sensitive course fields (e.g., instructor contact).
        *   Include logging and audit trail for create/update/delete actions.
        *   Ensure all database queries use parameterized statements to prevent SQL injection.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-003], [ARC-003], [NFR-004]
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course/CourseRepository.java
    *   **Architectural Requirements:**
        *   Extend PanacheRepository<Course> with tenant-scoped find methods.
        *   Define custom query methods using @Query native SQL with parameter placeholders.
        *   Implement soft-delete flag handling per tenant.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-003], [ARC-003], [NFR-004]
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course/CourseResource.java
    *   **Architectural Requirements:**
        *   Expose REST endpoints (GET, POST, PUT, DELETE) under /api/v1/courses.
        *   Validate request payloads using Jakarta Validation.
        *   Return appropriate HTTP status codes and OpenAPI annotations.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-003], [ARC-003], [NFR-004]

### DAY 2: Implement Core Student Management Service and Unit Tests
#### SUB-TASK 2.1: Develop StudentService and StudentRepository
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/student/StudentService.java
    *   **Architectural Requirements:**
        *   Provide enrollment, profile update, and enrollment history operations.
        *   Incorporate tenant_id isolation for all student records.
        *   Encrypt PII fields (name, email, phone) using AES-256.
        *   Use Kafka producer to emit student enrollment events.
        *   Ensure all database interactions use prepared statements.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-003], [ARC-003], [NFR-004]
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/student/StudentRepository.java
    *   **Architectural Requirements:**
        *   Extend PanacheRepository<Student> with tenant-aware queries.
        *   Implement methods for finding students by course enrollment.
        *   Use @Transactional and parameter binding.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-003], [ARC-003], [NFR-004]
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/student/StudentResource.java
    *   **Architectural Requirements:**
        *   Expose REST endpoints under /api/v1/students.
        *   Include role-based access control (RBAC) checks for Student, Teacher, Manager, Admin.
        *   Validate input and produce OpenAPI docs.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-003], [ARC-003], [NFR-004]

#### SUB-TASK 2.2: Write Unit Tests for Course and Student Services
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/course/CourseServiceTest.java
    *   **Architectural Requirements:**
        *   Test CRUD operations, tenant isolation, encryption handling, and exception scenarios.
        *   Mock CourseRepository and Kafka producer.
        *   Verify parameterized query usage via log inspection.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-003], [NFR-005]
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course/CourseRepository.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/course/CourseRepositoryTest.java
    *   **Architectural Requirements:**
        *   Validate tenant-scoped queries, soft-delete logic, and native SQL parameter binding.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-003], [NFR-005]
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/student/StudentService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/student/StudentServiceTest.java
    *   **Architectural Requirements:**
        *   Test enrollment flows, PII encryption, Kafka event emission, and tenant isolation.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-003], [NFR-005]
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/student/StudentRepository.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/student/StudentRepositoryTest.java
    *   **Architectural Requirements:**
        *   Verify repository methods for student lookup, enrollment queries, and parameter binding.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-003], [NFR-005]