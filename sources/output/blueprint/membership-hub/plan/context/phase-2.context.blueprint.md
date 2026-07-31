# PHASE 2 CONTEXT BLUEPRINT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260731045806 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date/Time** | 2026/07/31 04:58:06 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
Phase 2 focuses on implementing the Course Management module, including course creation, update, deletion with conflict avoidance, teacher assignment, and comprehensive database schema implementation. This phase requires developing the CourseService with full CRUD operations, implementing teacher-course assignment functionality with notification queuing, and creating all necessary database tables with proper constraints and indexes. All components must enforce OWASP security standards, implement proper input validation, and maintain strict RBAC enforcement through role-based access control.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Services Directory:** `./sources/backend/coursemanagement/`
- **Database Schema Files:** `./sources/backend/database/schema/`
- **API Endpoints:** 
  - GET `/courses` for course list view [REQ-007]
  - POST, PUT, DELETE `/courses` for course management [REQ-008]
  - POST `/courses/{courseId}/teachers` for teacher assignment [REQ-009]

## 3. Dedicated Sub-Agent Functional Directives
- **coder:** Develop Java services with Spring Boot framework, implement database schema, ensure OWASP compliance and conflict avoidance logic
- **tester:** Create and execute unit tests with minimum 85% code coverage for all course management functionality
- **reviewer:** Perform static code analysis and compiler validation for course management components
- **doc:** Generate technical documentation including API specifications and database schema documentation for course management

## 4. Phase Definition of Done (DoD)
- Course Service implemented with full CRUD operations and conflict avoidance logic
- Teacher assignment functionality with notification queuing mechanism
- Database schema deployed with courses table and all required constraints
- 100% test coverage for all implemented requirements ([REQ-007], [REQ-008], [REQ-009])
- OWASP security standards implemented for all input validation
- All Tag IDs ([REQ-007], [REQ-008], [REQ-009], [DAT-003], [EXC-001], [EXC-004]) properly mapped and implemented

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 4: COURSE SERVICE DEVELOPMENT WITH CONFLICT AVOIDANCE

#### SUB-TASK 4.1: Implement Course Service with CRUD operations and teacher conflict validation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/coursemanagement/org/nlh4j/saas/membershiphub/CourseService.java [REQ-007], [REQ-008], [REQ-009], [DAT-003]`
* **Architectural Requirements:**
  * Implement Spring Boot service with @RestController annotation for all course operations
  * Validate teacher schedule conflicts using database-level constraints and service-layer validation [REQ-008]
  * Implement proper input validation for course title, dates, and teacher assignments [EXC-004]
  * Use prepared statements for all database operations to prevent SQL injection [NFR-003]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-003], [EXC-004], [NFR-003]

#### SUB-TASK 4.2: Create courses table schema with proper constraints and indexes
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/database/schema/courses_table.sql [DAT-003]`
* **Architectural Requirements:**
  * Implement courses table with all specified columns: course_id (UUID PK), title (VARCHAR(150) NOT NULL), description (TEXT), start_date (DATE NOT NULL), end_date (DATE NOT NULL), teacher_id (UUID NOT NULL FOREIGN KEY Users.user_id), max_students (INT DEFAULT 30)
  * Add constraint to ensure end_date >= start_date [REQ-008]
  * Create indexes for performance optimization on teacher_id and date ranges [NFR-001]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [DAT-003], [REQ-008], [NFR-001]

### DAY 5: TEACHER ASSIGNMENT AND NOTIFICATION INTEGRATION

#### SUB-TASK 5.1: Implement teacher assignment functionality with notification queuing
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/coursemanagement/org/nlh4j/saas/membershiphub/TeacherAssignmentService.java [REQ-009]`
* **Architectural Requirements:**
  * Implement teacher assignment/unassignment endpoints with proper validation
  * Queue notifications for teacher mobile apps when assignments are made [REQ-009]
  * Validate that teacher exists and is assigned the Teacher role before assignment
  * Implement idempotent assignment operations to prevent duplicate notifications
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-009]

#### SUB-TASK 5.2: Create database trigger for teacher schedule conflict prevention
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/database/triggers/teacher_schedule_conflict_prevention.sql [REQ-008]`
* **Architectural Requirements:**
  * Implement database trigger to prevent overlapping course assignments for the same teacher
  * Validate that no teacher is assigned to multiple courses with intersecting date ranges
  * Raise appropriate error when conflict is detected [REQ-008]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-008]

### DAY 6: COMPREHENSIVE TESTING AND VALIDATION

#### SUB-TASK 6.1: Execute unit tests for course management functionality
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/coursemanagement/org/nlh4j/saas/membershiphub/CourseService.java;./sources/backend/coursemanagement/org/nlh4j/saas/membershiphub/CourseServiceTest.java [REQ-007], [REQ-008], [REQ-009]`
* **Architectural Requirements:**
  * Achieve minimum 85% code coverage for all course management operations
  * Test conflict detection logic for teacher schedule overlaps [REQ-008]
  * Validate notification queuing for teacher assignments [REQ-009]
  * Test input validation and error handling for all endpoints [EXC-004]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [EXC-004]

#### SUB-TASK 6.2: Perform static code analysis and compiler validation
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/coursemanagement/org/nlh4j/saas/membershiphub/CourseService.java [REQ-007], [REQ-008], [REQ-009]`
* **Architectural Requirements:**
  * Validate OWASP compliance for all input handling and database operations
  * Check for proper exception handling and error reporting [EXC-001], [EXC-004]
  * Verify RBAC enforcement for course management operations
  * Ensure proper logging and audit trail implementation [NFR-006]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [EXC-001], [EXC-004], [NFR-006]