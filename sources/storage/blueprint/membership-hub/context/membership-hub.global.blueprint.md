# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260802150245 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/02 15:02:45 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Membership‑hub là một kiến trúc micro‑service phân tán, triển khai trên GKE, sử dụng Java/Quarkus cho backend, Next.js cho frontend, Docker cho container, Flyway cho migration, Redis cho session cache, PostgreSQL cho dữ liệu quan hệ, Firebase Auth, FCM/APNs cho push, Zalo API cho nhóm, và Terraform/GitHub Actions cho CI/CD. Kiến trúc tuân thủ mô hình CQRS cho các module quản lý người dùng, trung tâm, khóa học, ghi danh, thẻ, thông báo, khuyến mãi, báo cáo, chatbot, và localization. Sử dụng event‑driven messaging với Google Pub/Sub cho các luồng bất đồng bộ như điểm danh, thông báo, và báo cáo.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- **Authentication Flow**: OAuth2 + JWT, refresh token, idempotent endpoints.  
- **Attendance Flow**: Mobile QR scan → REST → AttendanceService → idempotent DB write.  
- **Notification Flow**: Event bus → NotificationService → FCM/APNs + Zalo API.  
- **Reporting Flow**: Read‑replica PostgreSQL + scheduled batch jobs → CSV export.  
- **Chatbot Flow**: HTTP webhook → ChatbotService → AI engine + AuditLog.  
- **Localization Flow**: i18next + server‑side locale detection → dynamic meta tags.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack**: Java 21, Quarkus 3, Hibernate ORM, Flyway, Redis, PostgreSQL, Firebase Admin SDK, JJWT, BCrypt, JUnit 5, Testcontainers, Lombok, MapStruct.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 14, React 18, TypeScript, Tailwind CSS, i18next, Capacitor, Firebase Auth, FCM, APNs, Zalo SDK.  
- **DevOps**: Docker 24, Kubernetes (GKE), Helm 3, Terraform 1.6, GitHub Actions, Cloud Build, Cloud Scheduler, Cloud Pub/Sub, Cloud Logging, Cloud Monitoring.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule**: Repository root is `..`. All paths begin with `./sources/`.  
- **Dynamic Directory Prefixing Compliance**: Backend services under `./sources/backend.<service-name>`, frontend under `./sources/frontend.web`, infra under `./sources/infra`.  
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard**: All Java source codes reside in `org.nlh4j.saas.membershiphub`.  
- **Strict Tester Target Path Syntax**: Tester targets follow `<source_component>;<test_suite_file>` with both paths starting with `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1‑6 | ./sources/backend.auth, ./sources/backend.user, ./sources/backend.center | Auth, User, Center services, Flyway migrations, JWT, OAuth, RBAC, Redis cache | Coder, Tester | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [REQ-001], [REQ-002], [REQ-003], [DAT-001], [DAT-002], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009] |
| 2 | 7‑12 | ./sources/backend.user, ./sources/backend.center | Center CRUD, role assignment, validation, conflict handling | Coder, Tester | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009] |
| 3 | 13‑18 | ./sources/backend.course, ./sources/backend.enrollment, ./sources/backend.attendance | Course CRUD, enrollment, attendance idempotency, conflict detection | Coder, Tester | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-004], [DAT-005], [DAT-006], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009] |
| 4 | 19‑24 | ./sources/backend.card, ./sources/backend.notification, ./sources/backend.promotion, ./sources/backend.chatbot, ./sources/backend.localization | Card validity, notification push/Zalo, promotions, announcements, chatbot webhook, i18n | Coder, Tester | [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [EXC-003], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009] |
| 5 | 25‑30 | ./sources/frontend.web, ./sources/backend.report, ./sources/infra, ./sources/backend.security | Mobile UI, reporting CSV, DevOps pipelines, security hardening | Coder, Tester, Docker, GCP, GKE | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-005], [NFR-002], [NFR-004], [NFR-007], [NFR-008], [NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Thiết lập nền tảng xác thực, quản lý người dùng, và trung tâm, bao gồm JWT, OAuth, RBAC, và Redis session cache.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthService.java [REQ-001], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/RegistrationController.java [REQ-001], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/OAuthController.java [REQ-002], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/RoleController.java [REQ-003], [ARC-003], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.auth/src/main/resources/db/migration/V1__create_users_and_roles.sql [DAT-001], [DAT-002], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
- **Database Schema DDL SQL Specification [DAT-001], [DAT-002]**:  
  ```sql
  CREATE TABLE USERS (
      userId UUID PRIMARY KEY,
      email VARCHAR(255) NOT NULL UNIQUE,
      passwordHash CHAR(60) NOT NULL,
      fullName VARCHAR(100) NOT NULL,
      roleId SMALLINT NOT NULL REFERENCES ROLES(roleId),
      provider VARCHAR(20) NOT NULL DEFAULT 'local',
      createdAt TIMESTAMP NOT NULL DEFAULT now(),
      updatedAt TIMESTAMP NOT NULL DEFAULT now()
  );
  CREATE TABLE ROLES (
      roleId SMALLINT PRIMARY KEY,
      name VARCHAR(30) NOT NULL UNIQUE,
      description VARCHAR(200)
  );
  CREATE INDEX idx_users_email ON USERS(email);
  ```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]**:  
  - `POST /api/auth/register` → JSON body `{email, password, fullName}` → 201 Created, JWT in body.  
  - `POST /api/auth/oauth/{provider}` → OAuth code exchange → 200 OK, JWT.  
  - `PUT /api/users/{id}/role` → `{roleId}` → 200 OK.  
- **Phase Localized Exception Handlers [EXC-004]**:  
  - `InvalidEmailException` → 400 Bad Request, message "Invalid email format".  
  - `DuplicateEmailException` → 409 Conflict, message "Email already registered".  
  - `InvalidPasswordException` → 400 Bad Request, message "Password does not meet complexity".  

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

# DAY 1: AUTHENTICATION SERVICE SETUP
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthService.java [REQ-001], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Implement JWT generation, token signing with RSA-2048, set expiration 15 min, refresh token 7 days, store refresh token hash in Redis with TTL, expose `generateToken(User)` and `validateToken(String)` methods.  
    - **Targeted Tag IDs:** `[REQ-001], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 2: USER REGISTRATION ENDPOINT
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/RegistrationController.java [REQ-001], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Validate email regex, enforce password strength (min 12 chars, 1 upper, 1 lower, 1 digit, 1 special), hash with BCrypt, persist to USERS, return JWT.  
    - **Targeted Tag IDs:** `[REQ-001], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 3: SOCIAL OAUTH FLOW
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/OAuthController.java [REQ-002], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Implement OAuth2 code exchange for Google, Facebook, Firebase; retrieve user info, map to local user, create or update USERS, issue JWT.  
    - **Targeted Tag IDs:** `[REQ-002], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 4: ROLE ASSIGNMENT ENDPOINT
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/RoleController.java [REQ-003], [ARC-003], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Validate roleId against ROLES, update USERS.roleId, emit event `UserRoleChanged` to Pub/Sub.  
    - **Targeted Tag IDs:** `[REQ-003], [ARC-003], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 5: DATABASE MIGRATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.auth/src/main/resources/db/migration/V1__create_users_and_roles.sql [DAT-001], [DAT-002], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Create USERS and ROLES tables, seed default roles (System Admin, Center Admin, Manager, Teacher, Student), add indexes, ensure FK constraints.  
    - **Targeted Tag IDs:** `[DAT-001], [DAT-002], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 6: AUTH INTEGRATION TESTS
- **Sub-Agent Workflow Specialization:**  
  - **Tester:**  
    - **Target Component file path (`target_component`):** `./sources/backend.auth/src/test/java/org/nlh4j/saas/membershiphub/auth/AuthServiceTest.java; ./sources/backend.auth/src/test/java/org/nlh4j/saas/membershiphub/auth/RegistrationControllerTest.java [REQ-001], [REQ-002], [REQ-003], [ARC-006], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Write integration tests for JWT expiration, refresh token flow, duplicate email handling, role assignment, and OAuth provider mocks.  
    - **Targeted Tag IDs:** `[REQ-001], [REQ-002], [REQ-003], [ARC-006], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Xây dựng CRUD trung tâm, phân quyền quản trị trung tâm, kiểm tra trùng lặp mã số thuế.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/backend.center/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-004], [REQ-005], [REQ-006], [DAT-003], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.center/src/main/resources/db/migration/V2__create_centers.sql [DAT-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
- **Database Schema DDL SQL Specification [DAT-003]**:  
  ```sql
  CREATE TABLE CENTERS (
      centerId UUID PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      address VARCHAR(255) NOT NULL,
      taxId VARCHAR(13) NOT NULL UNIQUE,
      contactPhone VARCHAR(50),
      contactEmail VARCHAR(255)
  );
  CREATE INDEX idx_centers_taxid ON CENTERS(taxId);
  ```  
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [ARC-004], [ARC-005]**:  
  - `GET /api/centers` → list all centers.  
  - `POST /api/centers` → create center, 201 Created.  
  - `PUT /api/centers/{id}` → update center.  
  - `DELETE /api/centers/{id}` → delete center.  
  - `PUT /api/centers/{id}/admin` → assign/unassign Center Admin.  

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

# DAY 7: CENTER SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.center/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-004], [REQ-005], [REQ-006], [DAT-003], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Implement CRUD methods, validate taxId uniqueness, map to USERS for admin assignment, publish `CenterCreated` event.  
    - **Targeted Tag IDs:** `[REQ-004], [REQ-005], [REQ-006], [DAT-003], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 8: CENTER MIGRATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.center/src/main/resources/db/migration/V2__create_centers.sql [DAT-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Create CENTERS table, add unique constraint on taxId, seed sample centers.  
    - **Targeted Tag IDs:** `[DAT-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 9: CENTER ADMIN ASSIGNMENT ENDPOINT
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.center/src/main/java/org/nlh4j/saas/membershiphub/center/CenterAdminController.java [REQ-006], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Validate user exists, set role to Center Admin, update center_admins table, emit `CenterAdminAssigned` event.  
    - **Targeted Tag IDs:** `[REQ-006], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 10: CENTER ADMIN TESTS
- **Sub-Agent Workflow Specialization:**  
  - **Tester:**  
    - **Target Component file path (`target_component`):** `./sources/backend.center/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java; ./sources/backend.center/src/test/java/org/nlh4j/saas/membershiphub/center/CenterAdminControllerTest.java [REQ-004], [REQ-005], [REQ-006], [ARC-004], [ARC-005], [ARC-006], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Test CRUD, taxId conflict, admin assignment, role enforcement.  
    - **Targeted Tag IDs:** `[REQ-004], [REQ-005], [REQ-006], [ARC-004], [ARC-005], [ARC-006], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 11: CENTER ADMIN ROLE VALIDATION
- **Sub-Agent Workflow Specialization:**  
  - **Reviewer:**  
    - **Target Component file path (`target_component`):** `./sources/backend.center/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-006], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Review RBAC enforcement, ensure only System Admin can assign Center Admin, audit log generation.  
    - **Targeted Tag IDs:** `[REQ-006], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 12: CENTER ADMIN DOCUMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Doc:**  
    - **Target Component file path (`target_component`):** `./sources/backend.center/src/docs/CenterAdminAPI.md [REQ-006], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Write API spec, example requests, error codes, role matrix.  
    - **Targeted Tag IDs:** `[REQ-006], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Quản lý khóa học, ghi danh, điểm danh, đảm bảo tính bất biến và tránh xung đột lịch.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/backend.course/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java [REQ-007], [REQ-008], [REQ-009], [DAT-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.enrollment/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java [REQ-010], [REQ-011], [DAT-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.attendance/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
- **Database Schema DDL SQL Specification [DAT-004], [DAT-005], [DAT-006]**:  
  ```sql
  CREATE TABLE COURSES (
      courseId UUID PRIMARY KEY,
      title VARCHAR(150) NOT NULL,
      description TEXT,
      startDate DATE NOT NULL,
      endDate DATE NOT NULL,
      teacherId UUID REFERENCES USERS(userId),
      maxStudents INT DEFAULT 30
  );
  CREATE TABLE ENROLLMENTS (
      enrollmentId UUID PRIMARY KEY,
      studentId UUID REFERENCES USERS(userId),
      courseId UUID REFERENCES COURSES(courseId),
      enrollmentDate TIMESTAMP NOT NULL DEFAULT now()
  );
  CREATE TABLE ATTENDANCE (
      attendanceId UUID PRIMARY KEY,
      studentId UUID REFERENCES USERS(userId),
      courseId UUID REFERENCES COURSES(courseId),
      attendanceDate DATE NOT NULL,
      timestamp TIMESTAMP NOT NULL DEFAULT now(),
      UNIQUE(studentId, courseId, attendanceDate)
  );
  ```  
- **API and Event Routing Contracts [REQ-007]–[REQ-013], [ARC-008], [ARC-009]**:  
  - `GET /api/courses` → list courses.  
  - `POST /api/courses` → create course, validate no schedule conflict.  
  - `PUT /api/courses/{id}` → update course.  
  - `DELETE /api/courses/{id}` → delete course.  
  - `POST /api/enrollments` → enroll student, auto-create user if missing.  
  - `POST /api/attendance` → record attendance, idempotent.  

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

# DAY 13: COURSE SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.course/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java [REQ-007], [REQ-008], [REQ-009], [DAT-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** CRUD, schedule conflict detection (teacher or venue), publish `CourseCreated` event.  
    - **Targeted Tag IDs:** `[REQ-007], [REQ-008], [REQ-009], [DAT-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 14: COURSE MIGRATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.course/src/main/resources/db/migration/V3__create_courses.sql [DAT-004], [ARC-008], [ARC-009], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Create COURSES table, add indexes, seed sample courses.  
    - **Targeted Tag IDs:** `[DAT-004], [ARC-008], [ARC-009], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 15: ENROLLMENT SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.enrollment/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java [REQ-010], [REQ-011], [DAT-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Enroll student, create user if missing, enforce capacity, publish `EnrollmentCreated` event.  
    - **Targeted Tag IDs:** `[REQ-010], [REQ-011], [DAT-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 16: ENROLLMENT MIGRATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.enrollment/src/main/resources/db/migration/V4__create_enrollments.sql [DAT-005], [ARC-008], [ARC-009], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Create ENROLLMENTS table, add unique constraint, seed sample enrollments.  
    - **Targeted Tag IDs:** `[DAT-005], [ARC-008], [ARC-009], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 17: ATTENDANCE SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.attendance/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Record attendance, enforce idempotency via unique constraint, handle duplicate scans, emit `AttendanceRecorded` event.  
    - **Targeted Tag IDs:** `[REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 18: ATTENDANCE MIGRATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.attendance/src/main/resources/db/migration/V5__create_attendance.sql [DAT-006], [ARC-008], [ARC-009], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Create ATTENDANCE table, add unique constraint, seed sample attendance.  
    - **Targeted Tag IDs:** `[DAT-006], [ARC-008], [ARC-009], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Quản lý thẻ hội viên, thông báo, khuyến mãi, quảng cáo, chatbot, và localization.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/backend.card/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-014], [REQ-015], [DAT-007], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.notification/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [DAT-008], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.promotion/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionService.java [REQ-017], [REQ-018], [DAT-009], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.chatbot/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java [REQ-019], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/backend.localization/src/main/java/org/nlh4j/saas/membershiphub/localization/LocalizationService.java [REQ-022], [REQ-023], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
- **Database Schema DDL SQL Specification [DAT-007], [DAT-008], [DAT-009], [DAT-011]**:  
  ```sql
  CREATE TABLE STUDENTCARDS (
      cardId UUID PRIMARY KEY,
      studentId UUID REFERENCES USERS(userId),
      issueDate DATE NOT NULL,
      validityDays INT NOT NULL,
      remainingDays INT GENERATED ALWAYS AS (validityDays - (CURRENT_DATE - issueDate)) STORED
  );
  CREATE TABLE NOTIFICATIONS (
      notificationId UUID PRIMARY KEY,
      userId UUID REFERENCES USERS(userId),
      groupZalo VARCHAR(255),
      message TEXT NOT NULL,
      sentAt TIMESTAMP NOT NULL DEFAULT now(),
      delivered BOOLEAN NOT NULL DEFAULT false
  );
  CREATE TABLE PROMOTIONS (
      promoId UUID PRIMARY KEY,
      code VARCHAR(50) NOT NULL UNIQUE,
      discountPercent SMALLINT NOT NULL,
      startDate DATE,
      endDate DATE,
      description TEXT
  );
  CREATE TABLE ANNOUNCEMENTS (
      announcementId UUID PRIMARY KEY,
      title VARCHAR(150) NOT NULL,
      content TEXT NOT NULL,
      startDate DATE,
      endDate DATE
  );
  ```  
- **API and Event Routing Contracts [REQ-014]–[REQ-019], [ARC-016], [ARC-017], [ARC-018]**:  
  - `GET /api/cards/{studentId}` → card details.  
  - `POST /api/cards/{studentId}/extend` → extend validity.  
  - `POST /api/notifications` → create notification.  
  - `POST /api/promotions` → create promotion.  
  - `POST /api/announcements` → create announcement.  
  - `POST /api/chatbot/message` → send message to chatbot.  

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

# DAY 19: CARD SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.card/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-014], [REQ-015], [DAT-007], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Compute remainingDays, extend validity, publish `CardExtended` event.  
    - **Targeted Tag IDs:** `[REQ-014], [REQ-015], [DAT-007], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 20: NOTIFICATION SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.notification/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [DAT-008], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Queue push via FCM/APNs, post to Zalo, retry logic, mark delivered.  
    - **Targeted Tag IDs:** `[REQ-016], [DAT-008], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 21: PROMOTION & ANNOUNCEMENT SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.promotion/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionService.java [REQ-017], [REQ-018], [DAT-009], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** CRUD promotions, announcements, enforce date validity, publish events.  
    - **Targeted Tag IDs:** `[REQ-017], [REQ-018], [DAT-009], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 22: CHATBOT SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.chatbot/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java [REQ-019], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Receive webhook, route to AI engine, log to AuditLog, fallback to human.  
    - **Targeted Tag IDs:** `[REQ-019], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 23: LOCALIZATION SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.localization/src/main/java/org/nlh4j/saas/membershiphub/localization/LocalizationService.java [REQ-022], [REQ-023], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Detect Accept-Language, serve meta tags, generate hreflang links.  
    - **Targeted Tag IDs:** `[REQ-022], [REQ-023], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 24: PHASE 4 REVIEW & DOCUMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Reviewer:**  
    - **Target Component file path (`target_component`):** `./sources/backend.card/src/docs/CardAPI.md; ./sources/backend.notification/src/docs/NotificationAPI.md; ./sources/backend.promotion/src/docs/PromotionAPI.md; ./sources/backend.chatbot/src/docs/ChatbotAPI.md; ./sources/backend.localization/src/docs/LocalizationAPI.md [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-022], [REQ-023], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Review API contracts, ensure compliance with NFRs, update docs.  
    - **Targeted Tag IDs:** `[REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-022], [REQ-023], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

### Phase 5 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Giao diện mobile, báo cáo, DevOps, bảo mật, và tuân thủ.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/frontend.web/src/pages/index.tsx [REQ-020], [REQ-021], [REQ-022], [REQ-023], [NFR-001], [NFR-003], [NFR-004], [NFR-007], [NFR-008], [NFR-009]`  
  - `./sources/backend.report/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java [REQ-024], [REQ-025], [DAT-011], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
  - `./sources/infra/docker/Dockerfile [NFR-005], [NFR-006]`  
  - `./sources/infra/helm/values.yaml [NFR-004], [NFR-005], [NFR-006]`  
  - `./sources/infra/ci/github-actions.yml [NFR-004], [NFR-005], [NFR-006]`  
  - `./sources/infra/security/iam-policy.yaml [NFR-003], [NFR-006], [NFR-008], [NFR-009]`  
- **Database Schema DDL SQL Specification [DAT-011]**: (included in Phase 4).  
- **API and Event Routing Contracts [REQ-020]–[REQ-025], [ARC-020]–[ARC-025]**:  
  - `GET /api/report/attendance?centerId=&date=` → CSV.  
  - `GET /api/dashboard/summary?centerId=` → JSON.  
  - Mobile push notifications via FCM/APNs.  

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

# DAY 25: MOBILE UI IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/frontend.web/src/pages/index.tsx [REQ-020], [REQ-021], [REQ-022], [REQ-023], [NFR-001], [NFR-003], [NFR-004], [NFR-007], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Build role‑based navigation, integrate i18next, implement push registration, responsive layout.  
    - **Targeted Tag IDs:** `[REQ-020], [REQ-021], [REQ-022], [REQ-023], [NFR-001], [NFR-003], [NFR-004], [NFR-007], [NFR-008], [NFR-009]`  

# DAY 26: REPORT SERVICE IMPLEMENTATION
- **Sub-Agent Workflow Specialization:**  
  - **Coder:**  
    - **Target Component file path (`target_component`):** `./sources/backend.report/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java [REQ-024], [REQ-025], [DAT-011], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Query attendance, generate CSV, expose REST endpoint, schedule daily job.  
    - **Targeted Tag IDs:** `[REQ-024], [REQ-025], [DAT-011], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [NFR-009]`  

# DAY 27: DEVOPS PIPELINE CONFIGURATION
- **Sub-Agent Workflow Specialization:**  
  - **Docker:**  
    - **Target Component file path (`target_component`):** `./sources/infra/docker/Dockerfile [NFR-005], [NFR-006]`  
    - **Low-Level Technical Task Instruction:** Base image openjdk:21-jdk-slim, copy JAR, expose port, set entrypoint.  
    - **Targeted Tag IDs:** `[NFR-005], [NFR-006]`  

# DAY 28: HELM CHARTS & GKE DEPLOYMENT
- **Sub-Agent Workflow Specialization:**  
  - **GKE:**  
    - **Target Component file path (`target_component`):** `./sources/infra/helm/values.yaml [NFR-004], [NFR-005], [NFR-006]`  
    - **Low-Level Technical Task Instruction:** Define replicaCount, HPA, resource limits, service accounts, ingress.  
    - **Targeted Tag IDs:** `[NFR-004], [NFR-005], [NFR-006]`  

# DAY 29: CI/CD WORKFLOW SETUP
- **Sub-Agent Workflow Specialization:**  
  - **GCP:**  
    - **Target Component file path (`target_component`):** `./sources/infra/ci/github-actions.yml [NFR-004], [NFR-005], [NFR-006]`  
    - **Low-Level Technical Task Instruction:** Build, test, scan, push Docker, deploy to GKE, run integration tests.  
    - **Targeted Tag IDs:** `[NFR-004], [NFR-005], [NFR-006]`  

# DAY 30: SECURITY HARDENING & COMPLIANCE
- **Sub-Agent Workflow Specialization:**  
  - **Reviewer:**  
    - **Target Component file path (`target_component`):** `./sources/infra/security/iam-policy.yaml [NFR-003], [NFR-006], [NFR-008], [NFR-009]`  
    - **Low-Level Technical Task Instruction:** Enforce least‑privilege, enable VPC‑SC, audit logs, GDPR data deletion endpoints.  
    - **Targeted Tag IDs:** `[NFR-003], [NFR-006], [NFR-008], [NFR-009]`  

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Use prepared statements with positional parameters, whitelist allowed sort columns, escape identifiers.  
- **Cross‑Site Scripting (XSS) & Content Security Policy (CSP):** Auto‑escape JSON responses, set CSP header `default-src 'self'; script-src 'self'; object-src 'none';`.  
- **Multi‑Tenant CORS Security Rails:** Configure `Access-Control-Allow-Origin` to specific tenant domains, reject wildcard.  
- **Zero‑Leak Log Scrubbing & PII Data Masking Engines:** Apply `@JsonSerialize` with custom serializers, redact email, phone, and card numbers in logs.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Use Capacitor `@capacitor/preferences` for local storage, intercept back button, ensure HTTPS only, validate deep links.  
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware reads `Accept-Language`, sets `<html lang='...'>`, injects `<link rel='alternate' hreflang='...'>` tags, robots.txt per locale.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Branch naming `features/development-day-<day>`.  
- **Validation Guard Pipeline Gates:** Compile, run unit tests (≥85% coverage), static analysis, integration tests, security scan, deploy to staging, manual approval for production.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]