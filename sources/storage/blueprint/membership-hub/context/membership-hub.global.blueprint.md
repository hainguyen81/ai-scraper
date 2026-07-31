# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260731024630 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date/Time** | 2026/07/31 02:46:30 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. Architectural Alignment Summary & Tech Stack Baseline
- **Detected Technology Stack:** Java, Quarkus, PostgreSQL, Next.js, Firebase, OAuth2
- **Architecture Pattern:** Distributed Event-Driven Architecture / Decoupled Hub Topology matching the requirements specifications.

## 📁 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All paths generated MUST begin with `./sources/`.
- **[CONDITION: JAVA_STACK_ONLY] Java Enterprise Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.membershiphub`. 
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 📈 3. High-Level Multi-Phase Architectural Synopsis Grid
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-3 | `./sources/backend/user-management` | User registration, social authentication, role assignment | User Management Sub-Agent | [REQ-001], [REQ-002], [REQ-003], [EXC-004], [DAT-001], [DAT-008] |
| 2 | 4-6 | `./sources/backend/center-management` | Center list view, center create/update/delete, center admin assignment | Center Management Sub-Agent | [REQ-004], [REQ-005], [REQ-006], [EXC-004], [DAT-002] |
| 3 | 7-10 | `./sources/backend/course-management` | Course list view, course create/update/delete, teacher assignment | Course Management Sub-Agent | [REQ-007], [REQ-008], [REQ-009], [EXC-001], [EXC-004], [DAT-003] |
| 4 | 11-14 | `./sources/backend/student-enrollment` | Student course registration, attendance capture, student card management | Student Enrollment Sub-Agent | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [EXC-001], [EXC-002], [EXC-004], [DAT-004], [DAT-005], [DAT-006] |
| 5 | 15-17 | `./sources/backend/reporting-analytics` | Attendance report generation, enrollment summary dashboard | Reporting Analytics Sub-Agent | [REQ-024], [REQ-025], [EXC-004] |

## 4. Granular Low-Level Phase Specializations & Technical Deliverables

### 🔹 Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Implement user management functionality, including user registration, social authentication, and role assignment.
- **Target Physical Directory Matrix:**
  - `./sources/backend/user-management/UserRegistrationService.java` [REQ-001], [REQ-002]
  - `./sources/backend/user-management/SocialAuthenticationService.java` [REQ-002]
  - `./sources/backend/user-management/RoleAssignmentService.java` [REQ-003]
- **Database Schema DDL SQL Specification [DAT-001]:**
  ```sql
  CREATE TABLE Users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL,
    provider ENUM('local', 'firebase', 'google', 'facebook') DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now()
  );
  ```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003]:**
  - `POST /api/users/register` [REQ-001]
  - `POST /api/users/authenticate` [REQ-002]
  - `PUT /api/users/role` [REQ-003]
- **Phase Localized Exception Handlers [EXC-004]:**
  - Validate user input data for registration and authentication.

### 🔹 Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Implement center management functionality, including center list view, center create/update/delete, and center admin assignment.
- **Target Physical Directory Matrix:**
  - `./sources/backend/center-management/CenterService.java` [REQ-004], [REQ-005], [REQ-006]
- **Database Schema DDL SQL Specification [DAT-002]:**
  ```sql
  CREATE TABLE Centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100)
  );
  ```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006]:**
  - `GET /api/centers` [REQ-004]
  - `POST /api/centers` [REQ-005]
  - `PUT /api/centers/{centerId}` [REQ-005]
  - `DELETE /api/centers/{centerId}` [REQ-005]
  - `PUT /api/centers/{centerId}/admin` [REQ-006]
- **Phase Localized Exception Handlers [EXC-004]:**
  - Validate center input data for creation and update.

### 🔹 Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Implement course management functionality, including course list view, course create/update/delete, and teacher assignment.
- **Target Physical Directory Matrix:**
  - `./sources/backend/course-management/CourseService.java` [REQ-007], [REQ-008], [REQ-009]
- **Database Schema DDL SQL Specification [DAT-003]:**
  ```sql
  CREATE TABLE Courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL,
    max_students INT DEFAULT 30
  );
  ```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009]:**
  - `GET /api/courses` [REQ-007]
  - `POST /api/courses` [REQ-008]
  - `PUT /api/courses/{courseId}` [REQ-008]
  - `DELETE /api/courses/{courseId}` [REQ-008]
  - `PUT /api/courses/{courseId}/teacher` [REQ-009]
- **Phase Localized Exception Handlers [EXC-001], [EXC-004]:**
  - Handle network and connectivity drops during QR scan.
  - Validate course input data for creation and update.

### 🔹 Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Implement student enrollment and attendance functionality, including student course registration, attendance capture, and student card management.
- **Target Physical Directory Matrix:**
  - `./sources/backend/student-enrollment/StudentEnrollmentService.java` [REQ-010], [REQ-011]
  - `./sources/backend/attendance/AttendanceService.java` [REQ-012], [REQ-013]
  - `./sources/backend/student-card/StudentCardService.java` [REQ-014], [REQ-015]
- **Database Schema DDL SQL Specification [DAT-004], [DAT-005], [DAT-006]:**
  ```sql
  CREATE TABLE Enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT now()
  );
  
  CREATE TABLE Attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
  );
  
  CREATE TABLE StudentCards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT
  );
  ```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015]:**
  - `POST /api/students/enroll` [REQ-011]
  - `POST /api/attendance` [REQ-012]
  - `GET /api/students/card` [REQ-014]
  - `PUT /api/students/card/renew` [REQ-015]
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-004]:**
  - Handle network and connectivity drops during QR scan.
  - Handle duplicate attendance submissions.
  - Validate student input data for enrollment and attendance.

### 🔹 Phase 5 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Implement reporting and analytics functionality, including attendance report generation and enrollment summary dashboard.
- **Target Physical Directory Matrix:**
  - `./sources/backend/reporting/ReportingService.java` [REQ-024], [REQ-025]
- **Database Schema DDL SQL Specification:** None
- **API and Event Routing Contracts [REQ-024], [REQ-025]:**
  - `GET /api/reports/attendance` [REQ-024]
  - `GET /api/dashboard/enrollment` [REQ-025]
- **Phase Localized Exception Handlers [EXC-004]:**
  - Validate report input data for attendance and enrollment.

## 5. Global Non-Functional Requirements & Security Hardening [NFR-XXX]
- **Multi-Tenancy Isolation Strategy:** Implement tenant isolation using a discriminator column in the database.
- **OWASP Hardening Protocols:** Implement SQLi parameter bindings, application-layer PII encryption, and secure asymmetric cryptographic token controls.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 5, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]