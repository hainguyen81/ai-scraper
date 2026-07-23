# PHASE 2 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Initialize a Next.js frontend project with multi‑language i18n support and a responsive layout suitable for web and mobile viewing.  
- Implement the initial User Management UI (list, create, edit, delete) and Course Management UI (list, create, edit, delete) with role‑based visibility.  
- Develop backend Java/Quarkus services (`UserManagementService`, `CourseManagementService`, `AuthService`) exposing REST endpoints for user, course, and authentication operations.  
- Integrate email/password authentication and external OAuth2 providers (Google, Facebook, Firebase) via a centralized `AuthService`.  
- Enforce Role‑Based Access Control (RBAC) for System Admin, Admin, Manager, Teacher, and Student roles across both backend and frontend.  
- Create unit tests for all backend services and frontend components; write an integration/E2E test for the login flow.  
- Produce a multi‑stage Docker image for the backend, configure GCP‑specific properties, and draft GKE deployment manifests.  
- Perform static code analysis and compliance review to ensure Java package‑to‑path mapping and enterprise coding standards.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Java sources:** `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/`  
- **Backend tests:** `./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/`  
- **Frontend source tree:** `./sources/frontend/src/`  
  - Pages: `./sources/frontend/src/pages/`  
  - Components: `./sources/frontend/src/components/`  
  - Internationalization: `./sources/frontend/src/locales/`  
- **Docker configuration:** `./sources/backend/Dockerfile` (multi‑stage)  
- **GCP configuration:** `./sources/backend/src/main/resources/application.yml` (datasource, Kafka, GCP project settings)  
- **GKE manifests:** `./sources/backend/kubernetes/` (deployment.yaml, service.yaml, ingress.yaml)  
- **REST API contracts (examples):**  
  - `POST /api/v1/auth/login`  
  - `GET /api/v1/users`  
  - `POST /api/v1/users`  
  - `GET /api/v1/courses`  
  - `POST /api/v1/courses`  

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE)
- **Coder:** Implement all backend service classes, authentication logic, and frontend pages/components for user and course management. Write responsive UI components and integrate i18n.  
- **Tester:** Create JUnit unit tests for backend services (`UserManagementService`, `CourseManagementService`, `AuthService`) and frontend component tests (`user-management.test.tsx`, `auth.spec.ts`). Use `INTEGRATION_SCOPE` for cross‑platform login E2E tests.  
- **Reviewer:** Perform static analysis on Java source files, verify package‑to‑path mapping, enforce naming conventions, and validate frontend code style.  
- **Docker:** Produce a secure multi‑stage Dockerfile for the Quarkus backend, defining build, runtime, and optimization stages.  
- **GCP:** Populate `application.yml` with GCP‑specific datasource, Kafka bootstrap servers, and IAM‑related properties.  
- **GKE:** Draft Kubernetes Deployment, Service, and Ingress manifests for the backend services, including resource limits, liveness probes, and image pull secrets.

## 4. Phase Definition of Done (DoD)
- Next.js project bootstrapped with i18n, responsive layout, and role‑based navigation.  
- Fully functional User Management UI (CRUD) and Course Management UI (CRUD with teacher assignment).  
- Backend REST APIs for users, courses, and authentication with validation and security.  
- Email/password and external OAuth2 authentication integrated and tested.  
- RBAC filter and frontend role‑based navigation enforcing all five roles.  
- Unit test coverage >80 % for backend services; frontend component tests written and passing.  
- Docker image built, tagged, and ready for GKE deployment.  
- GCP configuration applied and GKE manifests generated.  
- Static code review completed; all Java files follow `/org/nlh4j/saas/membership-hub/` package‑to‑path mapping.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: INITIALIZE NEXT.JS FRONTEND & GLOBAL LAYOUT
#### SUB‑TASK 1.1: Scaffold Next.js project and i18n configuration
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/pages/_app.tsx
    * **Architectural Requirements:**
        * Setup Next.js with `next-i18next` for multi‑language support.
        * Implement `getStaticProps` to detect default locale from user preference, browser Accept‑Language, or fallback.
        * Define a responsive global layout using Tailwind CSS or Material‑UI; include navigation bar with role‑aware links.

#### SUB‑TASK 1.2: Create reusable responsive navigation component
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/Layout.tsx
    * **Architectural Requirements:**
        * Build a collapsible sidebar/mobile drawer that adapts to viewport size.
        * Conditionally render menu items based on authenticated user role (System Admin, Admin, Manager, Teacher, Student).
        * Integrate with Next.js Link for client‑side navigation and preserve i18n locale.

### DAY 2: USER MANAGEMENT IMPLEMENTATION
#### SUB‑TASK 2.1: Develop backend UserManagementService
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/UserManagementService.java
    * **Architectural Requirements:**
        * Define CRUD methods (`createUser`, `updateUser`, `deleteUser`, `getUser`, `listUsers`).
        * Use PanacheEntityBase for JPA persistence; enforce email uniqueness and password hashing.
        * Integrate with `AuthService` for role assignment and external provider linking.

#### SUB‑TASK 2.2: Build frontend UserManagementPage
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/pages/user-management.tsx
    * **Architectural Requirements:**
        * Fetch user list via `GET /api/v1/users` with pagination and role filter.
        * Provide a form for creating/editing users with validation (required fields, email format).
        * Implement delete confirmation dialogs and real‑time UI updates using React state management.

#### SUB‑TASK 2.3: Write unit tests for UserManagementService
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/UserManagementService.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/UserManagementServiceTest.java
    * **Architectural Requirements:**
        * Mock `UserRepository` to isolate service logic.
        * Test successful CRUD operations, duplicate email handling, and role assignment.
        * Assert proper exception propagation and data integrity.

### DAY 3: COURSE MANAGEMENT IMPLEMENTATION
#### SUB‑TASK 3.1: Develop backend CourseManagementService
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/CourseManagementService.java
    * **Architectural Requirements:**
        * Provide methods for course CRUD, teacher assignment, and overlap detection (no double‑booking of teachers/slots).
        * Use validation annotations; enforce non‑overlapping time ranges per teacher.
        * Integrate with `UserManagementService` for teacher lookup.

#### SUB‑TASK 3.2: Build frontend CourseManagementPage
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/pages/course-management.tsx
    * **Architectural Requirements:**
        * Display courses in a data table with columns: Course Name, Schedule, Teacher, Capacity.
        * Include a form for creating/editing courses with date/time pickers and teacher dropdown.
        * Implement assign/unassign teacher functionality with real‑time feedback.

#### SUB‑TASK 3.3: Write unit tests for CourseManagementService
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/CourseManagementService.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/CourseManagementServiceTest.java
    * **Architectural Requirements:**
        * Mock `CourseRepository` and `UserRepository`.
        * Test course creation with valid/invalid teacher schedules.
        * Verify overlap detection prevents conflicting assignments.

### DAY 4: AUTHENTICATION & LOGIN IMPLEMENTATION
#### SUB‑TASK 4.1: Implement AuthService with email/password and OAuth2
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/AuthService.java
    * **Architectural Requirements:**
        * Provide `login(String email, String password)` returning JWT token.
        * Integrate with external providers via OIDC configuration (Google, Facebook, Firebase).
        * Use Quarkus Security annotations (`@RolesAllowed`) and token validation filters.

#### SUB‑TASK 4.2: Create frontend login page with provider buttons
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/pages/login.tsx
    * **Architectural Requirements:**
        * Render email/password fields and “Sign in with Google/Facebook” buttons.
        * Use `next-auth` or custom auth client to call `POST /api/v1/auth/login`.
        * Redirect authenticated users to role‑specific dashboards (`/admin`, `/manager`, etc.).
        * Preserve i18n locale across login flow.

#### SUB‑TASK 4.3: Integration/E2E test for login flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts
    * **Architectural Requirements:**
        * Simulate user login with valid credentials and external provider redirect.
        * Verify JWT token storage, role‑based navigation rendering, and protected route access.
        * Capture network requests to `/api/v1/auth/login` and assert response structure.

### DAY 5: ROLE‑BASED ACCESS CONTROL (RBAC)
#### SUB‑TASK 5.1: Implement RBAC filter in backend
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/filter/RBACFilter.java
    * **Architectural Requirements:**
        * Intercept all `/api/v1/*` requests; extract JWT subject and roles.
        * Compare requested resource (e.g., `/users`, `/courses`) with role permissions.
        * Return `403` for unauthorized accesses; log audit trails.

#### SUB‑TASK 5.2: Build role‑based navigation component
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/RoleBasedNavigation.tsx
    * **Architectural Requirements:**
        * Consume authentication context to obtain user roles.
        * Render navigation items only for permitted roles.
        * Support dynamic sub‑menus for admin vs manager vs teacher/student.

#### SUB‑TASK 5.3: Reviewer static analysis on backend Java files
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/UserManagementService.java
    * **Architectural Requirements:**
        * Verify package‑to‑path mapping matches `/org/nlh4j/saas/membership-hub/`.
        * Check for unused imports, proper exception handling, and adherence to Java naming conventions.
        * Ensure no hard‑coded credentials or sensitive data.

### DAY 6: TESTING & COVERAGE
#### SUB‑TASK 6.1: Extend unit tests for CourseManagementService
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/CourseManagementService.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/CourseManagementServiceTest.java
    * **Architectural Requirements:**
        * Add tests for edge cases: zero teachers, schedule overlap validation, capacity limits.
        * Achieve >90 % line coverage for service methods.

#### SUB‑TASK 6.2: Write unit tests for AuthService
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/AuthService.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/AuthServiceTest.java
    * **Architectural Requirements:**
        * Mock password encoder and JWT signer.
        * Test successful login, failed credentials, and external provider token exchange.
        * Validate token payload includes roles and expiration.

#### SUB‑TASK 6.3: Reviewer validation of frontend component tests
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/tests/user-management.test.tsx
    * **Architectural Requirements:**
        * Confirm test suite covers CRUD actions, form validation, and error handling.
        * Ensure tests follow React Testing Library best practices and maintain i18n compatibility.

### DAY 7: CONTAINERIZATION & INFRASTRUCTURE SETUP
#### SUB‑TASK 7.1: Create multi‑stage Dockerfile for backend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/Dockerfile
    * **Architectural Requirements:**
        * Stage 1: Build with Maven (Java 17, Quarkus packaging).
        * Stage 2: Minimal runtime image (distroless or Alpine) copying the jar, setting `JAVA_OPTS`, exposing port `8080`.
        * Include health‑check (`/q/health`) and non‑root user for security.

#### SUB‑TASK 7.2: Configure GCP properties
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/resources/application.yml
    * **Architectural Requirements:**
        * Define datasource URL, username, and connection pool settings for Cloud SQL Postgres.
        * Set Kafka bootstrap servers for GCP Cloud Pub/Sub or Kafka cluster.
        * Include GCP project ID, credentials path, and IAM role mappings.

#### SUB‑TASK 7.3: Draft GKE deployment manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/kubernetes/deployment.yaml
    * **Architectural Requirements:**
        * Specify container image, resource limits/requests, and liveness/readiness probes.
        * Configure `imagePullSecrets` for private registry access.
        * Define environment variables for GCP project, database connection, and Kafka brokers.

#### SUB‑TASK 7.4: Final static code review and compliance check
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/
    * **Architectural Requirements:**
        * Validate every Java source file follows `/org/nlh4j/saas/membership-hub/` package‑to‑path mapping.
        * Ensure no hardcoded secrets, proper logging, and consistent code style.
        * Confirm all backend services are referenced correctly in Docker and Kubernetes manifests.