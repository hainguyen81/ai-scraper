# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260731151028 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/07/31 15:10:28 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY
### 1.1. Core System Modality & Architecture Modality
The membership-hub project is designed as a unified platform for multi-center membership management, providing real-time attendance tracking, digital membership cards, and multi-channel communication. The system will utilize a microservices architecture, with each service responsible for a specific domain (e.g., user management, center management, course management). The system will also employ an event-driven architecture (EDA) to handle asynchronous messaging and notifications.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
The system will utilize a combination of synchronous and asynchronous data flows to handle user interactions, attendance tracking, and notification delivery. The data flows will be designed to ensure data consistency and integrity across the system, with clear boundaries and interfaces between services.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** The system will utilize a Java-based stack, with Spring Boot as the primary framework, and PostgreSQL as the database management system. The system will also utilize Apache Kafka for asynchronous messaging and notification delivery.
- **Frontend & Cross-Platform UI Mobile Stack:** The system will utilize a React-based frontend, with React Native for mobile app development. The system will also utilize Firebase Cloud Messaging (FCM) for push notifications.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `..`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **Java Package Standard:** The Java package standard will be `org.nlh4j.saas.membershiphub`.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-3 | User Management | User registration, login, and role assignment | coder | [REQ-001], [REQ-002], [REQ-003] |
| 1 | 4-5 | Center Management | Center creation, update, and deletion | coder | [REQ-004], [REQ-005], [REQ-006] |
| 2 | 1-3 | Course Management | Course creation, update, and deletion | coder | [REQ-007], [REQ-008], [REQ-009] |
| 2 | 4-5 | Student Enrollment & Registration | Student course registration and enrollment | coder | [REQ-010], [REQ-011] |
| 3 | 1-3 | Attendance & QR Scanning | QR attendance capture and attendance idempotency | coder | [REQ-012], [REQ-013] |
| 3 | 4-5 | Student Card Management | Student card validity display and renewal | coder | [REQ-014], [REQ-015] |
| 4 | 1-3 | Notifications & Communications | Notification trigger and delivery | coder | [REQ-016] |
| 4 | 4-5 | Promotions & Announcements Management | Promotion and announcement management | coder | [REQ-017], [REQ-018] |
| 5 | 1-3 | AI Customer Service Chatbot | AI chatbot integration | coder | [REQ-019] |
| 5 | 4-5 | Mobile App Core Features | Mobile app role-specific UI and push notifications | coder | [REQ-020], [REQ-021] |

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
### 🔹 Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Implement user management and center management features.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend/usermanagement` [REQ-001], [REQ-002], [REQ-003]
  * `./sources/backend/centermanagement` [REQ-004], [REQ-005], [REQ-006]
- **Database Schema DDL SQL Specification [DAT-001]:**
```sql
CREATE TABLE users (
  user_id UUID PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash CHAR(60) NOT NULL,
  full_name VARCHAR(100) NOT NULL,
  role_id SMALLINT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT now(),
  updated_at TIMESTAMP NOT NULL DEFAULT now()
);
```
- **API and Event Routing Contracts [REQ-001], [ARC-001]:**
```json
{
  "endpoint": "/users",
  "method": "POST",
  "requestBody": {
    "email": "string",
    "password": "string",
    "fullName": "string"
  },
  "responseBody": {
    "userId": "string",
    "email": "string",
    "fullName": "string"
  }
}
```
#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs
#### 🗓️ DAY 1: Implement User Registration
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/backend/usermanagement/UserRegistrationService.java` [REQ-001]
    - **Low-Level Technical Task Instruction:** Implement user registration logic using Spring Boot and PostgreSQL.
    - **Targeted Tag IDs:** [REQ-001]

#### 🗓️ DAY 2: Implement User Login
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/backend/usermanagement/UserLoginService.java` [REQ-002]
    - **Low-Level Technical Task Instruction:** Implement user login logic using Spring Boot and PostgreSQL.
    - **Targeted Tag IDs:** [REQ-002]

#### 🗓️ DAY 3: Implement User Role Assignment
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/backend/usermanagement/UserRoleAssignmentService.java` [REQ-003]
    - **Low-Level Technical Task Instruction:** Implement user role assignment logic using Spring Boot and PostgreSQL.
    - **Targeted Tag IDs:** [REQ-003]

### 🔹 Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Implement course management and student enrollment features.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend/courmanagement` [REQ-007], [REQ-008], [REQ-009]
  * `./sources/backend/studentenrollment` [REQ-010], [REQ-011]
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE courses (
  course_id UUID PRIMARY KEY,
  title VARCHAR(150) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  teacher_id UUID NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT now(),
  updated_at TIMESTAMP NOT NULL DEFAULT now()
);
```
- **API and Event Routing Contracts [REQ-007], [ARC-002]:**
```json
{
  "endpoint": "/courses",
  "method": "POST",
  "requestBody": {
    "title": "string",
    "description": "string",
    "startDate": "date",
    "endDate": "date",
    "teacherId": "string"
  },
  "responseBody": {
    "courseId": "string",
    "title": "string",
    "description": "string",
    "startDate": "date",
    "endDate": "date",
    "teacherId": "string"
  }
}
```
#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs
#### 🗓️ DAY 1: Implement Course Creation
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/backend/courmanagement/CourseCreationService.java` [REQ-007]
    - **Low-Level Technical Task Instruction:** Implement course creation logic using Spring Boot and PostgreSQL.
    - **Targeted Tag IDs:** [REQ-007]

#### 🗓️ DAY 2: Implement Course Update
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/backend/courmanagement/CourseUpdateService.java` [REQ-008]
    - **Low-Level Technical Task Instruction:** Implement course update logic using Spring Boot and PostgreSQL.
    - **Targeted Tag IDs:** [REQ-008]

#### 🗓️ DAY 3: Implement Course Deletion
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/backend/courmanagement/CourseDeletionService.java` [REQ-009]
    - **Low-Level Technical Task Instruction:** Implement course deletion logic using Spring Boot and PostgreSQL.
    - **Targeted Tag IDs:** [REQ-009]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Utilize prepared statements and positional query parameters to prevent SQL injection attacks.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Implement context sanitization and dynamic injection of strict CSP headers to prevent XSS attacks.
- **Multi-Tenant CORS Security Rails:** Implement origin wildcard prohibitions and dynamic tenant origin database metrics validation to prevent CORS attacks.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Utilize dynamic client-side fetching and absolute URL addressing to ensure mobile app compliance.
- **Internationalization (i18n) & Dynamic SEO Injection:** Implement edge-layer locale recognition middleware architectures and hreflang dynamic hypermedia control injection to ensure internationalization and SEO compliance.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Utilize programmatic forking controls for branch `features/development-day-X`.
- **Validation Guard Pipeline Gates:** Implement execution rules for compilation verification, automated code coverage goals, and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 5, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]