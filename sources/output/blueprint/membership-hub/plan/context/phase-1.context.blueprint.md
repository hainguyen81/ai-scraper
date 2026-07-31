# PHASE 1 CONTEXT BLUEPRINT: membership-hub

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
Phase 1 focuses on implementing the foundational backend modules for User Management and Center Management. This includes developing the User Registration Service, User Authentication Service, and Center Service with complete database schema implementation, API contracts, and exception handling. All components must adhere to OWASP security standards, implement proper input validation, and maintain strict RBAC enforcement through role-based access control.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Services Directory:** `./sources/backend/usermanagement/`
- **Backend Services Directory:** `./sources/backend/centermanagement/`
- **Database Schema Files:** `./sources/backend/database/schema/`
- **API Endpoints:** 
  - POST `/users` for user registration [REQ-001]
  - POST `/auth/login` for user authentication [REQ-002]
  - GET, POST, PUT, DELETE `/centers` for center management [REQ-004], [REQ-005], [REQ-006]

## 3. Dedicated Sub-Agent Functional Directives
- **coder:** Develop Java services with Spring Boot framework, implement database schema, ensure OWASP compliance
- **tester:** Create and execute unit tests with minimum 85% code coverage
- **reviewer:** Perform static code analysis and compiler validation
- **doc:** Generate technical documentation including API specifications and database schema documentation

## 4. Phase Definition of Done (DoD)
- All three core services (UserRegistration, UserAuthentication, CenterService) implemented and functional
- Database schema deployed with all required tables and constraints
- 100% test coverage for all implemented requirements
- OWASP security standards implemented for all input validation
- All Tag IDs ([REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [DAT-001], [DAT-002], [DAT-008], [EXC-004]) properly mapped and implemented

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: USER REGISTRATION SERVICE DEVELOPMENT

#### SUB-TASK 1.1: Implement User Registration Service with OWASP-compliant input validation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/usermanagement/org/nlh4j/saas/membershiphub/UserRegistrationService.java [REQ-001], [DAT-001]`
* **Architectural Requirements:**
  * Implement Spring Boot service with @RestController annotation
  * Use prepared statements for all database operations to prevent SQL injection [NFR-003]
  * Validate email format (must contain single "@" and valid domain) and password strength (min 8 chars, uppercase, lowercase, digit, special char)
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-001], [DAT-001], [EXC-004], [NFR-003]

#### SUB-TASK 1.2: Create database schema for users table
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/database/schema/users_table.sql [DAT-001]`
* **Architectural Requirements:**
  * Implement exact DDL specification from global context
  * Include proper constraints (NOT NULL, UNIQUE, PRIMARY KEY)
  * Add indexes for performance optimization [NFR-001]
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [DAT-001], [NFR-001]

### DAY 2: USER AUTHENTICATION SERVICE DEVELOPMENT

#### SUB-TASK 2.1: Implement User Authentication Service with JWT token generation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/usermanagement/org/nlh4j/saas/membershiphub/UserAuthenticationService.java [REQ-002], [ARC-006]`
* **Architectural Requirements:**
  * Implement JWT token generation with 15-minute expiry [ARC-006]
  * Include refresh token mechanism with 7-day expiry [NFR-003]
  * Implement password hashing using BCrypt with proper salt rounds
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-002], [ARC-006], [NFR-003]

#### SUB-TASK 2.2: Create roles table schema and initial data
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/database/schema/roles_table.sql [DAT-008]`
* **Architectural Requirements:**
  * Implement roles table with predefined roles (System Admin, Center Admin, Manager, Teacher, Student)
  * Include initial data insertion for all role types
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [DAT-008]

### DAY 3: CENTER SERVICE DEVELOPMENT

#### SUB-TASK 3.1: Implement Center Service with CRUD operations
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/centermanagement/org/nlh4j/saas/membershiphub/CenterService.java [REQ-004], [REQ-005], [REQ-006], [DAT-002]`
* **Architectural Requirements:**
  * Implement all center management operations (create, read, update, delete)
  * Enforce tax_id uniqueness constraint at service level [REQ-005]
  * Implement proper input validation for all fields including email format and phone number validation
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-002], [EXC-004]

#### SUB-TASK 3.2: Create centers table schema
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/database/schema/centers_table.sql [DAT-002]`
* **Architectural Requirements:**
  * Implement centers table with all specified columns and constraints
  * Add proper indexes for performance on frequently queried fields
* **DAILY LOGS TRACEABILITY RULES:**
  * **Targeted Tag IDs:** [DAT-002]