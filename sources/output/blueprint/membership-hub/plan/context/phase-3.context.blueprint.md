# PHASE 3 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Phase 3 focuses on developing the core membership data management capabilities for the membership-hub platform. This includes implementing backend API endpoints for CRUD operations on membership-related entities and building corresponding frontend user interface components. The phase strictly targets requirements [REQ-005], [REQ-006], [REQ-007], and [REQ-008], ensuring multi-tenancy isolation through tenant_id enforcement at the data access layer. All implementations must adhere to OAuth2 JWT token validation and role-based access control (RBAC) as defined in the global context.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Scope:** All Java source files must reside under `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` with subdirectories matching package structure (e.g., `service/`, `repository/`, `entity/`). API endpoints must follow REST conventions with base path `/api/v1/`.
- **Frontend Scope:** All React components and pages must be under `./sources/frontend/src/` with subdirectories `components/`, `pages/`, and `services/`.
- **Strict Path Boundaries:**
  - Backend: `./sources/backend/`
  - Frontend: `./sources/frontend/`
- **API Endpoints:**
  - `GET /api/v1/centers` - List centers ([REQ-004])
  - `POST/PUT/DELETE /api/v1/centers` - Manage centers ([REQ-005])
  - `POST/DELETE /api/v1/centers/{centerId}/admins` - Assign center admins ([REQ-006])
  - `GET /api/v1/courses` - List courses ([REQ-007])
  - `POST/PUT/DELETE /api/v1/courses` - Manage courses ([REQ-008])

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for coder, tester, reviewer, doc, docker, GCP, GKE)
- **coder:** Implements backend services, repositories, entities, and frontend components. Must enforce tenant isolation via `tenant_id` in all SQL queries and apply OWASP input validation.
- **tester:** Writes and executes unit tests for backend services and frontend components. Tests must validate multi-tenancy data segregation and RBAC rules.
- **reviewer:** Performs static code analysis on individual Java files for security flaws (SQL injection, XSS) and compiler errors.
- **doc:** Creates technical documentation for API endpoints, data models, and UI components.
- **docker, GCP, GKE:** Not allocated in this phase.

## 4. Phase Definition of Done (DoD)
- Backend APIs for center and course management implemented with full CRUD operations and tenant isolation.
- Frontend UI components for center and course management built and integrated with backend APIs.
- 100% unit test coverage for all new backend services and repositories, verifying multi-tenancy constraints.
- All code passes static analysis with zero OWASP Top 10 vulnerabilities (SQL injection, XSS).
- API documentation generated in OpenAPI format.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: BACKEND CENTER MANAGEMENT API IMPLEMENTATION

#### SUB-TASK 1.1: Implement Center entity and JPA repository with tenant_id filtering
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/entity/Center.java`
    *   **Architectural Requirements:**
        *   JPA entity with fields: center_id (UUID), name (String), address (String), tax_id (String), contact_phone (String), contact_email (String), tenant_id (UUID)
        *   Apply `@TenantId` annotation or equivalent for automatic multi-tenancy filtering
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-005], [ARC-001], [NFR-002]

#### SUB-TASK 1.2: Create CenterRepository with custom queries for tenant isolation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/CenterRepository.java`
    *   **Architectural Requirements:**
        *   Extend JpaRepository with custom method `findAllByTenantId(UUID tenantId)`
        *   All methods must include `tenant_id` in WHERE clauses to enforce data isolation
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-005], [ARC-002], [NFR-002]

#### SUB-TASK 1.3: Implement CenterService with business logic and validation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CenterService.java`
    *   **Architectural Requirements:**
        *   Service methods for create, update, delete with tax_id uniqueness validation
        *   Inject tenant_id from JWT token context into all operations
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-005], [REQ-006], [NFR-003]

#### SUB-TASK 1.4: Create CenterController with REST endpoints
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/controller/CenterController.java`
    *   **Architectural Requirements:**
        *   Implement endpoints: GET /centers, POST /centers, PUT /centers/{id}, DELETE /centers/{id}
        *   Apply @RolesAllowed annotation with "SYSTEM_ADMIN" role for mutating operations
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]

### DAY 2: BACKEND COURSE MANAGEMENT API IMPLEMENTATION

#### SUB-TASK 2.1: Implement Course entity with teacher assignment and date validation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/entity/Course.java`
    *   **Architectural Requirements:**
        *   JPA entity with fields: course_id (UUID), title (String), description (Text), start_date (Date), end_date (Date), teacher_id (UUID), max_students (Integer), tenant_id (UUID)
        *   Add @Constraint validation for end_date >= start_date
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-008], [ARC-003]

#### SUB-TASK 2.2: Create CourseRepository with teacher schedule conflict detection
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/CourseRepository.java`
    *   **Architectural Requirements:**
        *   Custom query method `findTeacherScheduleConflicts(UUID teacherId, Date startDate, Date endDate, UUID tenantId)`
        *   Native SQL query to detect overlapping date ranges for the same teacher
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-008], [NFR-001]

#### SUB-TASK 2.3: Implement CourseService with teacher conflict validation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java`
    *   **Architectural Requirements:**
        *   Business logic to check for teacher schedule conflicts before create/update
        *   Throw custom exception `TeacherScheduleConflictException` when conflicts detected
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-008], [EXC-004]

#### SUB-TASK 2.4: Create CourseController with RBAC enforcement
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/controller/CourseController.java`
    *   **Architectural Requirements:**
        *   Implement endpoints: GET /courses, POST /courses, PUT /courses/{id}, DELETE /courses/{id}
        *   Apply @RolesAllowed with "SYSTEM_ADMIN" and "CENTER_ADMIN" roles for mutating operations
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-007], [REQ-008], [ARC-002]

### DAY 3: FRONTEND CENTER MANAGEMENT UI COMPONENTS

#### SUB-TASK 3.1: Create CenterList component with data table
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/components/CenterList.tsx`
    *   **Architectural Requirements:**
        *   React component with Material-UI DataGrid displaying centers
        *   Fetch data from GET /api/v1/centers endpoint
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-004]

#### SUB-TASK 3.2: Implement CenterForm component for create/edit operations
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/components/CenterForm.tsx`
    *   **Architectural Requirements:**
        *   Form with validation for all center fields (name, address, tax_id, etc.)
        *   Submit to POST/PUT /api/v1/centers endpoints
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-005]

#### SUB-TASK 3.3: Create CenterAdminAssignment component
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/components/CenterAdminAssignment.tsx`
    *   **Architectural Requirements:**
        *   UI for selecting users and assigning them as center admins
        *   Integration with POST/DELETE /api/v1/centers/{centerId}/admins
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-006]

### DAY 4: FRONTEND COURSE MANAGEMENT UI COMPONENTS

#### SUB-TASK 4.1: Create CourseList component with filtering
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/components/CourseList.tsx`
    *   **Architectural Requirements:**
        *   Data grid showing courses with teacher names and date ranges
        *   Support filtering by teacher, date range, and status
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-007]

#### SUB-TASK 4.2: Implement CourseForm with teacher conflict validation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/components/CourseForm.tsx`
    *   **Architectural Requirements:**
        *   Form with date pickers and teacher selection
        *   Client-side validation for date consistency and teacher availability checking
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-008]

#### SUB-TASK 4.3: Create API service classes for center and course operations
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/services/centerService.ts`
    *   **Architectural Requirements:**
        *   TypeScript service class with methods for all center API operations
        *   Proper error handling and response typing
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]

#### SUB-TASK 4.4: Create API service for course operations
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/services/courseService.ts`
    *   **Architectural Requirements:**
        *   TypeScript service class with methods for all course API operations
        *   Includes teacher conflict detection API calls
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-007], [REQ-008]

### DAY 5: UNIT TESTING AND CODE REVIEW

#### SUB-TASK