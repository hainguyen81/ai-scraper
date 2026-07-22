# PHASE 4 CONTEXT BLUEPRINT: membership-hub
## 1. Phase Operational Scope & Objectives
- **Goal:** Execute comprehensive Testing & Quality Assurance (QA) for the membership‑hub platform.  
- **Focus Areas:** Unit tests for Java/Quarkus services, integration tests for Kafka‑driven event streams, database transaction validation, security & role‑based access tests, end‑to‑end UI tests for Next.js web UI, and functional verification of mobile‑app notifications.  
- **Deliverable:** All automated test suites passing with ≥ 80 % code coverage, security scan clean, and documented test results ready for CI/CD promotion to Phase 5.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
```
src/main/java/com/membership/hub/
    controller/          ← REST endpoints (Auth, User, Attendance, Notification, Course, etc.)
    service/             ← Business logic (AuthService, UserService, AttendanceService, NotificationService, CourseService)
    repository/          ← Spring Data JPA interfaces (StudentRepo, TeacherRepo, CourseRepo, etc.)
    config/              ← SecurityConfig, JwtConfig, KafkaConfig
    model/               ← Entity classes (Student, Teacher, Course, Attendance, etc.)

src/main/resources/
    application.yml      ← Quarkus & Kafka config
    kafka-topics.txt    ← Declarative topic definitions

src/main/docker/
    Dockerfile.jvm      ← Test container image

src/test/java/com/membership/hub/
    controller/         ← *Controller* unit tests (e.g., AuthControllerTest)
    service/            ← *Service* unit tests (e.g., AttendanceServiceTest)
    repository/         ← *Repository* integration tests (e.g., StudentRepositoryTest)
    security/           ← JwtAuthenticationTokenProviderTest, RoleAuthorityMapperTest

src/it/java/com/membership/hub/
    integration/        ← End‑to‑end Kafka + DB tests (e.g., AttendanceKafkaIT)

src/frontend/
    __tests__/          ← Next.js unit tests (React components)
    cypress/            ← UI automation specs

src/docker/
    test-compose.yml   ← Docker‑Compose for test environment
```

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
| Agent | Core Responsibility in Phase 4 |
|-------|--------------------------------|
| **DevOps** | Provision isolated test environments (PostgreSQL, Kafka, Keycloak), configure Docker‑Compose, and integrate test‑setup into the CI pipeline. |
| **Coder** | Build reusable test fixtures, mock data generators, and helper utilities (e.g., `TestDataFactory`, `MockKafkaProducer`). |
| **Tester** | Write, execute, and maintain all unit, integration, and UI test cases covering the functional, security, and performance requirements. |
| **Reviewer** | Perform peer‑review of test code, ensure adherence to coding standards, and validate test coverage reports. |

## 4. Phase Definition of Done (DoD)
- All unit tests pass (JUnit5) with ≥ 80 % coverage on core service layers.  
- Integration tests verify Kafka event flow, database transaction integrity, and cross‑service contracts.  
- UI test suite (Cypress) executes without failures across supported browsers.  
- Security tests confirm proper role‑based access controls and JWT validation.  
- Test reports are generated (Jacoco, Surefire, Cypress) and uploaded to the artifact repository.  
- CI pipeline stage “Test & QA” is green and ready for promotion to Phase 5.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: PROVISION TEST INFRASTRUCTURE & CREATE TEST FIXTURES
#### SUB-TASK 1.1: Setup isolated test environment containers
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/docker/test-compose.yml`
    *   **Architectural Requirements:**
        *   Define services for PostgreSQL (latest), Kafka (single broker), and Keycloak (for auth tests).
        *   Use environment variables for DB connection, Kafka bootstrap servers, and test profiles.
        *   Ensure containers start in detached mode and are linked to the CI job.
*   **Target Path 2:** CI pipeline definition (`.github/workflows/test.yml`)
    *   **Architectural Requirements:**
        *   Add a stage “Test‑Env” that runs `docker-compose -f src/docker/test-compose.yml up -d`.
        *   Wait for services to be ready before proceeding to test execution.
        *   Clean‑up containers after stage completion.

#### SUB-TASK 1.2: Build reusable test fixtures and helper utilities
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/test/java/com/membership/hub/util/TestDataFactory.java`
    *   **Architectural Requirements:**
        *   Provide static methods to generate mock `Student`, `Teacher`, `Course`, `Attendance` entities with realistic data.
        *   Include methods for creating JWT tokens for each role (SystemAdmin, Admin, Manager, Teacher, Student).
        *   Ensure fixtures are deterministic for repeatable tests.
*   **Target Path 2:** `src/test/java/com/membership/hub/util/MockKafkaProducer.java`
    *   **Architectural Requirements:**
        *   Implement a utility that can emit Kafka messages to predefined topics (e.g., `attendance-topic`, `notification-topic`) without requiring a running broker.
        *   Allow injection of test profiles to avoid interfering with production topics.

#### SUB-TASK 1.3: Draft comprehensive test plan and coverage goals
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/test/java/com/membership/hub/qa/TestPlan.md`
    *   **Architectural Requirements:**
        *   Document all test scenarios per module (Auth, User, Attendance, Notification, Course, Security).
        *   Define acceptance criteria, required coverage per module, and any external dependencies (e.g., external SMS/Zalo APIs mocked).
        *   Include a timeline linking to daily execution logs.

### DAY 2: BACKEND UNIT TESTING – AUTH & USER SERVICES
#### SUB-TASK 2.1: Implement unit tests for AuthController and AuthService
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/test/java/com/membership/hub/controller/AuthControllerTest.java`
    *   **Architectural Requirements:**
        *   Test login with email/password, Google, Facebook, and Firebase providers using mocked `AuthService`.
        *   Validate HTTP status codes (200/401) and JWT token generation.
        *   Include edge cases: invalid credentials, locked account, missing request body.
*   **Target Path 2:** `src/test/java/com/membership/hub/service/AuthServiceTest.java`
    *   **Architectural Requirements:**
        *   Verify password hashing, token issuance, and token validation logic.
        *   Mock `UserRepository` and `KeycloakService` to isolate unit behavior.
        *   Ensure exception handling for duplicate email registration.

#### SUB-TASK 2.2: Review and enforce coding standards on test code
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/test/java/com/membership/hub/controller/AuthControllerTest.java`
    *   **Architectural Requirements:**
        *   Check naming conventions (camelCase for methods, descriptive assertions).
        *   Validate use of `@Mock`, `@InjectMocks` annotations and proper cleanup (`@BeforeEach`).
        *   Ensure test independence (no shared mutable state across tests).
*   **Target Path 2:** `src/test/java/com/membership/hub/service/AuthServiceTest.java`
    *   **Architectural Requirements:**
        *   Verify that each test method is self‑contained and uses `@Transactional` where needed.
        *   Confirm that all `assert*` statements follow AssertJ or JUnit best practices.

### DAY 3: BACKEND INTEGRATION TESTING – ATTENDANCE & NOTIFICATION WORKFLOWS
#### SUB-TASK 3.1: Integration test for QR‑based attendance with Kafka event streaming
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/it/java/com/membership/hub/integration/AttendanceKafkaIT.java`
    *   **Architectural Requirements:**
        *   Start Docker‑compose services (PostgreSQL, Kafka) before test execution.
        *   Insert a `Student` via `StudentRepository`, then invoke `AttendanceService.recordQrScan(studentId, scanTime)`.
        *   Consume the produced message from `attendance-topic` and assert payload matches expected schema (studentId, timestamp, courseId).
        *   Verify that the `Attendance` entity is persisted with correct status.
*   **Target Path 2:** `src/main/java/com/membership/hub/listener/AttendanceEventListener.java`
    *   **Architectural Requirements:**
        *   Ensure the listener correctly deserializes incoming Kafka messages and triggers downstream actions (e.g., updating student’s daily attendance count).
        *   Validate that listener is only invoked for expected topics (no cross‑talk).

#### SUB-TASK 3.2: Integration test for notification delivery (Zalo & push)
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/docker/test-compose.yml` (additional service)
    *   **Architectural Requirements:**
        *   Add a mock SMS/Zalo gateway container (e.g., `mock-zalo-service`) that listens on a defined port.
        *   Expose environment variables for API keys and webhook URLs used by `NotificationService`.
*   **Target Path 2:** `src/main/java/com/membership/hub/service/NotificationService.java`
    *   **Architectural Requirements:**
        *   Verify that `NotificationService.sendNotification(studentId, message)` routes messages to both Zalo API and mobile push (mocked).
        *   Ensure retry logic and dead‑letter queue handling are exercised in test environment.

#### SUB-TASK 3.3: Peer review of integration test artifacts
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/it/java/com/membership/hub/integration/AttendanceKafkaIT.java`
    *   **Architectural Requirements:**
        *   Confirm that test uses `@Testcontainers` or equivalent for resource management.
        *   Validate that all external calls are stubbed/mocked except the Kafka broker.
*   **Target Path 2:** `src/it/java/com/membership/hub/integration/NotificationIntegrationIT.java`
    *   **Architectural Requirements:**
        *   Ensure test covers success, failure, and timeout scenarios for external gateways.
        *   Verify that test cleans up Kafka topics after execution to avoid side‑effects.

### DAY 4: FRONTEND & UI TESTING – NEXT.JS & CROSS‑ROLE SECURITY
#### SUB-TASK 4.1: Unit test Next.js React components (multi‑language support)
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/frontend/__tests__/components/LanguageToggle.test.jsx`
    *   **Architectural Requirements:**
        *   Test locale detection based on `i18next` context.
        *   Verify that UI strings change correctly when switching languages.
*   **Target Path 2:** `src/frontend/__tests__/pages/Dashboard.test.jsx`
    *   **Architectural Requirements:**
        *   Simulate authenticated user sessions for each role (Admin, Teacher, Student) using mocked `authContext`.
        *   Assert that role‑specific UI elements are rendered (e.g., “Add Course” button only for Admin).
        *   Validate that data fetching (`getServerSideProps`) respects role‑based authorization.

#### SUB-TASK 4.2: End‑to‑end UI automation with Cypress
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `cypress/support/commands.js`
    *   **Architectural Requirements:**
        *   Add custom commands for login as specific roles (`loginAs(role)`), QR attendance simulation (`qrScan(studentId)`), and navigation to protected routes.
*   **Target Path 2:** `cypress/e2e/role_based_access.spec.js`
    *   **Architectural Requirements:**
        *   Execute scenarios: Admin creates a course, Manager assigns a student, Teacher views schedule, Student registers for a course.
        *   Verify that each role cannot access UI elements outside its permissions (assert DOM elements absent).
        *   Capture screenshots on failure for audit trails.

#### SUB-TASK 4.3: Security test suite – JWT validation & CSRF protection
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `src/test/java/com/membership/hub/security/JwtAuthenticationTokenProviderTest.java`
    *   **Architectural Requirements:**
        *   Validate token generation, expiration, and claim population (roles).
        *   Ensure token refresh mechanism works without compromising existing sessions.
*   **Target Path 2:** `src/test/java/com/membership/hub/security/SecurityConfigTest.java`
    *   **Architectural Requirements:**
        *   Confirm that HTTP endpoints enforce `@PreAuthorize` rules per role.
        *   Verify that CSRF protection is disabled for API endpoints (as per REST design) but active for web forms.

### DAY 5: FINAL TEST EXECUTION, REPORTING & CI PROMOTION (Optional – if not completed on Day 4)
*(If the core objectives are already satisfied after Day 4, this day can be omitted. The output will stop at Day 4 as per the stopping criterion.)*

--- 

**End of Phase 4 Execution Logs**. All sub‑tasks are assigned to a single agent each, target paths are explicitly listed, and architectural requirements are detailed per component. The logs respect the 1‑7 day per phase limit and stop as soon as the Phase’s core technical objectives are met.