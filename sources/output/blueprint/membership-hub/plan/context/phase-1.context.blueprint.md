# PHASE 1 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- **Project Initialization:** Establish the foundational directory layout, Maven configuration, Quarkus application properties, and Docker resources under `./sources/` to satisfy the absolute workspace boundary rule.  
- **Multi‑Tenancy & Security Baseline:** Embed OWASP‑compliant security controls at the infrastructure level: define a `tenant_id` scope for all data access, configure AES‑256 encryption for sensitive fields (e.g., passwords), and enable parameterized queries to prevent SQL injection.  
- **User Management Service:** Implement a complete CRUD back‑end for internal users (System Admin, Admin, Manager, Teacher, Student) with role‑based access, secure credential storage, and Kafka event emission for user lifecycle changes.  
- **Course Management Service:** Implement a full CRUD back‑end for courses, including time‑window validation, teacher assignment, student enrollment, and associated Kafka events.  
- **Compliance & Integration:** Ensure all generated Java code follows the corporate package `org.nlh4j.saas.membershiphub` and the strict path‑to‑package mapping derived from the stripped project token `membershiphub`.  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Root:** `./sources/backend/` – contains Maven POM, Quarkus configuration, Java source (`src/main/java/org/nlh4j/saas/membershiphub/...`), resources, and test artifacts.  
- **Frontend Root:** `./sources/frontend/` – not used in Phase 1; reserved for later phases.  
- **Docker / Deployment Assets:** `./sources/backend/src/main/docker/Dockerfile.jvm` – used for local container builds (deployment handled in Phase 4).  
- **Configuration Files:** `./sources/backend/src/main/resources/application.properties` – defines datasource URL, Kafka bootstrap servers, tenant defaults, and security settings.  
- **REST Endpoint Patterns (Phase 1 Scope):**  
  - `POST /api/v1/users` – create user (System Admin only)  
  - `GET /api/v1/users/{id}` – retrieve user by ID (authenticated)  
  - `PUT /api/v1/users/{id}` – update user (role‑restricted)  
  - `DELETE /api/v1/users/{id}` – delete user (Admin/Manager)  
  - `POST /api/v1/courses` – create course (Admin only)  
  - `GET /api/v1/courses/{id}` – retrieve course details  
  - `PUT /api/v1/courses/{id}` – update course (Admin)  
  - `DELETE /api/v1/courses/{id}` – delete course (Admin)  
- **Kafka Topics (Phase 1 Scope):** `user-events`, `course-events` – emitted on create/update/delete actions.  

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE, Manager)
- **Manager Agent:**  
  - Create the Maven project skeleton (`pom.xml`) with Quarkus and necessary dependencies (Hibernate ORM, SmallRye JWT, Kafka client, PostgreSQL driver).  
  - Generate `src/main/resources/application.properties` with datasource, Kafka, and multi‑tenancy defaults (`tenant_id` placeholder).  
  - Add `.dockerignore` and base `Dockerfile.jvm` for local builds.  
  - Validate that the project builds (`mvn clean compile`).  

- **Coder Agent:**  
  - **User Management:**  
    - Implement `User` domain entity (`User.java`) with fields: `id`, `tenantId`, `email`, `passwordHash`, `role`, `fullName`, `contactInfo`. Apply AES‑256 encryption for `passwordHash` and enforce non‑null `tenantId`.  
    - Implement `UserRepository` extending `PanacheRepository<User>` with parameterized queries and tenant‑scoped `findByTenantId`.  
    - Implement `UserService` with business logic, role validation, and Kafka producer for `user-events`.  
    - Implement `UserResource` REST resource exposing the CRUD endpoints defined above, with JAX‑RS annotations and JWT authentication.  
  - **Course Management:**  
    - Implement `Course` domain entity (`Course.java`) with fields: `id`, `tenantId`, `title`, `description`, `startDate`, `endDate`, `teacherId`, `maxStudents`. Enforce overlap validation in service layer.  
    - Implement `CourseRepository` extending `PanacheRepository<Course>` with tenant‑scoped queries.  
    - Implement `CourseService` with enrollment logic, teacher assignment, and Kafka producer for `course-events`.  
    - Implement `CourseResource` REST resource exposing CRUD endpoints, with authorization checks (Admin/Manager).  

- **Tester, Reviewer, Docker, GCP, GKE Agents:** Not assigned in Phase 1 (reserved for later phases).  

## 4. Phase Definition of Done (DoD)
- **Structural Milestones:**  
  - All required files under `./sources/` exist with correct Java package layout (`org/nlh4j/saas/membershiphub`).  
  - `pom.xml` builds successfully (`mvn clean compile`).  
- **Security Milestones:**  
  - Every Java entity includes a `tenantId` field and is used in repository queries to enforce multi‑tenancy.  
  - Passwords are stored as AES‑256 encrypted hashes; encryption/decryption utilities are present.  
  - All repository methods use parameterized queries (no string concatenation).  
  - JWT authentication is configured for `UserResource` and `CourseResource`.  
- **Functional Milestones:**  
  - User CRUD endpoints are defined in `UserResource` with appropriate role checks.  
  - Course CRUD endpoints are defined in `CourseResource` with overlap validation.  
  - Kafka producers emit events for user and course create/update/delete actions.  
- **Compliance Milestones:**  
  - OWASP Top 10 controls (A01:2021 – Broken Access Control, A02:2021 – Cryptographic Failures, A03:2021 – Injection) are addressed per component.  
  - All generated code passes static analysis (no linting violations).  

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Establish Maven Project & Baseline Configuration
#### SUB-TASK 1.1: Initialize Maven skeleton and Quarkus configuration (Manager)
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/pom.xml
    *   **Architectural Requirements:**
        *   Include Quarkus platform version aligned with Java 17, dependencies for Hibernate ORM, SmallRye JWT, Kafka client, PostgreSQL JDBC driver, and Lombok.
        *   Define `<groupId>org.nlh4j.saas</groupId>` and `<artifactId>membershiphub</artifactId>`.
        *   Configure `<packaging>jar</packaging>` and enable Maven Compiler plugin for Java 17.
*   **Target Path:** ./sources/backend/src/main/resources/application.properties
    *   **Architectural Requirements:**
        *   Set `quarkus.datasource.db-kind=postgresql`, `quarkus.datasource.username=membershiphub`, `quarkus.datasource.password=[ENCRYPTED]`, `quarkus.datasource.jdbc.url=jdbc:postgresql://localhost:5432/membershiphub`.
        *   Define `quarkus.kafka.bootstrap-servers=localhost:9092`.
        *   Add `membershiphub.tenant.default=public` and `membershiphub.security.password-encryption-key=[BASE64_KEY]`.
        *   Enable `quarkus.hibernate-orm.multitenant=PER_TENANT` and `quarkus.hibernate-orm.tenant-id=` placeholder.
*   **Target Path:** ./sources/backend/src/main/docker/Dockerfile.jvm
    *   **Architectural Requirements:**
        *   Use official Quarkus JVM base image, copy `target/*-runner.jar` as application jar, expose port `8080`.
*   **Target Path:** ./sources/backend/.dockerignore
    *   **Architectural Requirements:**
        *   Exclude `target/`, `.git/`, `*.iml`, `pom.xml` to keep image lean.  

### DAY 2: Implement User Management Service (CRUD + Security)
#### SUB-TASK 2.1: Develop User domain entity with tenant‑scoped fields and encrypted password (Coder)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/User.java
    *   **Architectural Requirements:**
        *   Annotate with `@Entity`, `@Table(name = "users")`, `@TenantId` (custom annotation for multi‑tenancy).
        *   Define fields: `id` (Long), `tenantId` (String), `email` (String, unique), `passwordHash` (String, encrypted via AES‑256), `role` (String, e.g., "SYS_ADMIN","ADMIN","MANAGER","TEACHER","STUDENT"), `fullName` (String), `contactInfo` (String).
        *   Apply `@EncryptedField` annotation for `passwordHash` referencing a `EncryptionService`.
        *   Include Lombok `@Data`, `@NoArgsConstructor`, `@AllArgsConstructor`.
        *   Implement `Comparable<User>` for audit ordering.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/UserRepository.java
    *   **Architectural Requirements:**
        *   Extend `PanacheRepository<User>` and add `List<User> findByTenantId(String tenantId);`.
        *   Use `@Transactional` on query methods.
        *   Apply `@Param` for all query parameters to enforce parameterized queries.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/UserService.java
    *   **Architectural Requirements:**
        *   Provide methods: `User createUser(User user, String requesterTenant)`, `User getUser(Long id, String tenant)`, `User updateUser(Long id, User updates, String tenant)`, `void deleteUser(Long id, String tenant)`.
        *   Enforce role‑based access: only SYS_ADMIN can create users across tenants; ADMIN/MANAGER limited to own tenant.
        *   Integrate `EncryptionService` for password hashing before persistence.
        *   Emit Kafka event via `KafkaProducer` to `user-events` topic with key `userId`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/UserResource.java
    *   **Architectural Requirements:**
        *   Expose JAX‑RS endpoints: `POST /api/v1/users`, `GET /api/v1/users/{id}`, `PUT /api/v1/users/{id}`, `DELETE /api/v1/users/{id}`.
        *   Secure with `@RolesAllowed` annotations matching the defined roles.
        *   Validate request payload using Bean Validation (`@NotNull`, `@Email`).
        *   Return appropriate HTTP status codes (201, 200, 404, 403).  

### DAY 3: Implement Course Management Service (CRUD + Overlap Validation)
#### SUB-TASK 3.1: Develop Course domain entity with tenant scoping and validation (Coder)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Course.java
    *   **Architectural Requirements:**
        *   Annotate with `@Entity`, `@Table(name = "courses")`, `@TenantId`.
        *   Fields: `id` (Long), `tenantId` (String), `title` (String, not null), `description` (String), `startDate` (LocalDateTime), `endDate` (LocalDateTime), `teacherId` (Long), `maxStudents` (Integer), `enrolledCount` (Integer, default 0).
        *   Add `@NotNull` and `@FutureOrPresent` on `startDate`; enforce `endDate` > `startDate`.
        *   Include Lombok `@Data`, `@NoArgsConstructor`, `@AllArgsConstructor`.
        *   Implement `Comparable<Course>` for chronological ordering.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/CourseRepository.java
    *   **Architectural Requirements:**
        *   Extend `PanacheRepository<Course>` and add `List<Course> findByTenantId(String tenantId);`.
        *   Provide `List<Course> findOverlap(String tenantId, LocalDateTime start, LocalDateTime end);` using native query with tenant filter.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java
    *   **Architectural Requirements:**
        *   Methods: `Course createCourse(Course course, String tenant)`, `Course getCourse(Long id, String tenant)`, `Course updateCourse(Long id, Course updates, String tenant)`, `void deleteCourse(Long id, String tenant)`.
        *   Validate course overlap using `CourseRepository.findOverlap`; throw `IllegalStateException` if conflict.
        *   Manage teacher assignment: verify teacher exists and belongs to same tenant.
        *   Integrate Kafka producer for `course-events` on create/update/delete.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/CourseResource.java
    *   **Architectural Requirements:**
        *   Expose JAX‑RS endpoints: `POST /api/v1/courses`, `GET /api/v1/courses/{id}`, `PUT /api/v1/courses/{id}`, `DELETE /api/v1/courses/{id}`.
        *   Secure with `@RolesAllowed("ADMIN","MANAGER")` for write operations; read accessible to all authenticated roles.
        *   Validate payload with Bean Validation (`@NotBlank`, `@Future`).
        *   Return appropriate HTTP status codes (201, 200, 404, 409 for overlap).