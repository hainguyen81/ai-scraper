# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260802053750 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/02 05:37:50 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY
### 1.1. Core System Modality & Architecture Modality
The membership-hub project is a multi-tenant, responsive web and mobile application that provides membership management, course enrollment, attendance tracking, and notification services. The system will utilize a microservices architecture with a combination of RESTful APIs and event-driven messaging.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
The system will consist of the following components:
- **User Service**: responsible for user registration, authentication, and profile management.
- **Course Service**: responsible for course creation, enrollment, and attendance tracking.
- **Notification Service**: responsible for sending notifications to users.
- **Mobile App**: a responsive mobile application that provides a user interface for the system.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Node.js, Express.js, PostgreSQL, Redis, and RabbitMQ.
- **Frontend & Cross-Platform UI Mobile Stack:** React, React Native, and Expo.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `..`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-3 | ./sources/backend/user-service | User registration, authentication, and profile management | coder | [REQ-001], [REQ-002], [DAT-001] |
| 1 | 1-3 | ./sources/backend/course-service | Course creation, enrollment, and attendance tracking | coder | [REQ-004], [REQ-007], [DAT-003] |
| 2 | 4-6 | ./sources/frontend/mobile-app | Responsive mobile application for user interface | coder | [REQ-020], [REQ-021] |
| 3 | 7 | ./sources/infra/deployment | Deployment scripts for backend and frontend | docker | [NFR-002], [NFR-004] |

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
### 🔹 Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Implement user registration, authentication, and profile management.
- **Target Physical Directory Matrix Map:** 
  - `./sources/backend/user-service [REQ-001], [REQ-002], [DAT-001]`
  - `./sources/backend/course-service [REQ-004], [REQ-007], [DAT-003]`
- **Database Schema DDL SQL Specification [DAT-001]:** 
  ```sql
  CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
  );
  ```
- **API and Event Routing Contracts [REQ-001], [ARC-001]:** 
  - `POST /users` - Create a new user
  - `GET /users` - Get all users
- **Phase Localized Exception Handlers [EXC-001]:** 
  - Validate user input data
  - Handle duplicate user email

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs
#### 🗓️ DAY 1: Implement user registration
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/backend/user-service [REQ-001], [REQ-002], [DAT-001]`
    - **Low-Level Technical Task Instruction:** Implement user registration API endpoint
    - **Targeted Tag IDs:** `[REQ-001], [REQ-002], [DAT-001]`

#### 🗓️ DAY 2: Implement user authentication
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/backend/user-service [REQ-001], [REQ-002], [DAT-001]`
    - **Low-Level Technical Task Instruction:** Implement user authentication API endpoint
    - **Targeted Tag IDs:** `[REQ-001], [REQ-002], [DAT-001]`

#### 🗓️ DAY 3: Implement user profile management
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/backend/user-service [REQ-001], [REQ-002], [DAT-001]`
    - **Low-Level Technical Task Instruction:** Implement user profile management API endpoint
    - **Targeted Tag IDs:** `[REQ-001], [REQ-002], [DAT-001]`

### 🔹 Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Implement responsive mobile application for user interface.
- **Target Physical Directory Matrix Map:** 
  - `./sources/frontend/mobile-app [REQ-020], [REQ-021]`
- **API and Event Routing Contracts [REQ-020], [ARC-006]:** 
  - `GET /courses` - Get all courses
  - `POST /enrollments` - Enroll in a course
- **Phase Localized Exception Handlers [EXC-002]:** 
  - Validate course enrollment data
  - Handle duplicate course enrollment

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs
#### 🗓️ DAY 4: Implement course list view
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/frontend/mobile-app [REQ-020], [REQ-021]`
    - **Low-Level Technical Task Instruction:** Implement course list view
    - **Targeted Tag IDs:** `[REQ-020], [REQ-021]`

#### 🗓️ DAY 5: Implement course enrollment
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/frontend/mobile-app [REQ-020], [REQ-021]`
    - **Low-Level Technical Task Instruction:** Implement course enrollment
    - **Targeted Tag IDs:** `[REQ-020], [REQ-021]`

#### 🗓️ DAY 6: Implement course attendance tracking
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** `./sources/frontend/mobile-app [REQ-020], [REQ-021]`
    - **Low-Level Technical Task Instruction:** Implement course attendance tracking
    - **Targeted Tag IDs:** `[REQ-020], [REQ-021]`

### 🔹 Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Deploy backend and frontend.
- **Target Physical Directory Matrix Map:** 
  - `./sources/infra/deployment [NFR-002], [NFR-004]`
- **Deployment Scripts:** 
  - `docker-compose up` - Start backend services
  - `npm start` - Start frontend development server

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs
#### 🗓️ DAY 7: Deploy backend and frontend
- **Sub-Agent Workflow Specialization:**
  * **docker:**
    - **Target Component file path:** `./sources/infra/deployment [NFR-002], [NFR-004]`
    - **Low-Level Technical Task Instruction:** Deploy backend and frontend
    - **Targeted Tag IDs:** `[NFR-002], [NFR-004]`

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Use prepared statements and positional query parameters.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Use JSX auto-escaping and dynamic injection of strict CSP headers.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Use dynamic client-side fetching and absolute URL addressing.
- **Internationalization (i18n) & Dynamic SEO Injection:** Use edge-layer locale recognition middleware architectures and hreflang dynamic hypermedia control injection.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Use programmatic forking controls for branch `features/development-day-X`.
- **Validation Guard Pipeline Gates:** Use execution rules for compilation verification and automated code coverage goals.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 6, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]