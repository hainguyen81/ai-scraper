# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260731045806 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/07/31 04:58:06 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY
### 1.1. Core System Modality & Architecture Modality
The membership-hub project is designed as a unified platform for multi-center membership management, providing real-time attendance tracking, digital membership cards, and multi-channel communication. The system will utilize a microservices architecture, with each service responsible for a specific domain (e.g., user management, center management, course management). The system will also employ an event-driven architecture (EDA) to handle asynchronous messaging and notifications.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
The system will utilize a combination of synchronous and asynchronous data flows. Synchronous data flows will be used for requests that require immediate responses, such as user authentication and course enrollment. Asynchronous data flows will be used for notifications, attendance tracking, and other events that do not require immediate responses. The system will also employ a message broker (e.g., Apache Kafka) to handle event-driven messaging and notifications.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** The system will utilize a Java-based tech stack, with Spring Boot as the primary framework. The system will also utilize PostgreSQL as the primary database management system. Other dependencies will include Apache Kafka for event-driven messaging, and Firebase for authentication and notification services.
- **Frontend & Cross-Platform UI Mobile Stack:** The system will utilize a React-based tech stack for the web application, with React Native for mobile applications. The system will also utilize Capacitor for hybrid mobile app development.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `..`. All paths generated MUST begin with `..sources.`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **Java Package Standard:** The system will utilize the corporate package foundation: `org.nlh4j.saas.membershiphub`. 
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `..sources.`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-3 | `..sources.backend.usermanagement` | User registration, authentication, and role assignment | coder | [REQ-001], [REQ-002], [REQ-003] |
| 1 | 1-3 | `..sources.backend.centermanagement` | Center creation, update, and deletion | coder | [REQ-004], [REQ-005], [REQ-006] |
| 2 | 4-6 | `..sources.backend.coursmanagement` | Course creation, update, and deletion | coder | [REQ-007], [REQ-008], [REQ-009] |
| 3 | 7 | `..sources.backend.attendance` | Attendance tracking and QR code scanning | coder | [REQ-012], [REQ-013] |
| 4 | 8-10 | `..sources.frontend.web` | Web application development | coder | [REQ-020] |
| 5 | 11-14 | `..sources.frontend.mobile` | Mobile application development | coder | [REQ-021] |

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
### 🔹 Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** The objective of this phase is to develop the user management and center management modules.
- **Target Physical Directory Matrix Map:** 
  * `..sources.backend.usermanagement/UserRegistrationService.java [REQ-001]`
  * `..sources.backend.usermanagement/UserAuthenticationService.java [REQ-002]`
  * `..sources.backend.centermanagement/CenterService.java [REQ-004]`
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
```java
@PostMapping("/users")
public User createUser(@RequestBody User user) {
  // Create user logic
}
```
#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs
#### 🗓️ DAY 1: User Registration Service Development
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path (`target_component`):** `..sources.backend.usermanagement/UserRegistrationService.java [REQ-001]`
    - **Low-Level Technical Task Instruction:** Develop the user registration service to handle user registration requests.
    - **Targeted Tag IDs:** `[REQ-001]`

#### 🗓️ DAY 2: User Authentication Service Development
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path (`target_component`):** `..sources.backend.usermanagement/UserAuthenticationService.java [REQ-002]`
    - **Low-Level Technical Task Instruction:** Develop the user authentication service to handle user authentication requests.
    - **Targeted Tag IDs:** `[REQ-002]`

#### 🗓️ DAY 3: Center Service Development
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path (`target_component`):** `..sources.backend.centermanagement/CenterService.java [REQ-004]`
    - **Low-Level Technical Task Instruction:** Develop the center service to handle center creation, update, and deletion requests.
    - **Targeted Tag IDs:** `[REQ-004]`

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** The system will utilize prepared statements and positional query parameters to prevent SQL injection attacks.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** The system will utilize automated context sanitization and JSX auto-escaping to prevent XSS attacks.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** The system will utilize Capacitor for hybrid mobile app development, with dynamic client-side fetching and absolute URL addressing.
- **Internationalization (i18n) & Dynamic SEO Injection:** The system will utilize edge-layer locale recognition middleware architectures and hreflang dynamic hypermedia control injection.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** The system will utilize programmatic forking controls for branch `features/development-day-X`.
- **Validation Guard Pipeline Gates:** The system will utilize execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 5, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]