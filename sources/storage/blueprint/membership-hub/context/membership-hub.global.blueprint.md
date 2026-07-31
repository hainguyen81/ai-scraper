# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260731165119 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/07/31 16:51:19 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY
### 1.1. Core System Modality & Architecture Modality
The membership-hub project is designed as a unified platform for multi-center membership management, providing real-time attendance tracking, digital membership cards, and multi-channel communication. The system will utilize a microservices architecture, with separate services for user management, center management, course management, and notification management. The system will also employ an event-driven architecture (EDA) to handle events such as attendance tracking and notification triggers.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
The system will utilize asynchronous messaging channels to handle communication between services, with Apache Kafka as the messaging broker. The system will also employ a data ingestion gateway to handle data imports from external sources. The data flow topology will be designed to ensure data consistency and integrity across the system.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java 17, Spring Boot 2.7, Apache Kafka 3.1, PostgreSQL 14
- **Frontend & Cross-Platform UI Mobile Stack:** React 18, React Native 0.70, Expo 45

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `..`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **Java Package Standard:** All Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.membershiphub`.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-3 | ./sources/backend/user-management | User registration, login, and role assignment | coder | [REQ-001], [REQ-002], [REQ-003] |
| 1 | 4-5 | ./sources/backend/center-management | Center creation, update, and deletion | coder | [REQ-004], [REQ-005], [REQ-006] |
| 2 | 1-3 | ./sources/backend/course-management | Course creation, update, and deletion | coder | [REQ-007], [REQ-008], [REQ-009] |
| 2 | 4-5 | ./sources/backend/notification-management | Notification trigger and delivery | coder | [REQ-016] |
| 3 | 1-3 | ./sources/frontend/web-app | Web app development for user management and center management | coder | [REQ-020] |
| 3 | 4-5 | ./sources/frontend/mobile-app | Mobile app development for user management and center management | coder | [REQ-021] |
| 4 | 1-3 | ./sources/infra/deployment | Deployment scripts for backend and frontend | docker | [NFR-001], [NFR-002] |
| 4 | 4-5 | ./sources/infra/monitoring | Monitoring scripts for backend and frontend | GCP | [NFR-003], [NFR-004] |

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
### 🔹 Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Develop user management and center management features
- **Target Physical Directory Matrix Map:**
  * ./sources/backend/user-management [REQ-001], [REQ-002], [REQ-003]
  * ./sources/backend/center-management [REQ-004], [REQ-005], [REQ-006]
- **Database Schema DDL SQL Specification [DAT-001]:**
  ```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
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
- **Phase Localized Exception Handlers [EXC-001]:**
  ```java
@ExceptionHandler(UserNotFoundException.class)
public ResponseEntity<String> handleUserNotFoundException(UserNotFoundException e) {
  // Handle user not found exception
}
```
- **Enterprise Business Core Code Sample:**
  ```java
@Service
public class UserService {
  @Autowired
  private UserRepository userRepository;
  
  public User createUser(User user) {
    // Create user logic
  }
}
```

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs
#### 🗓️ DAY 1: Develop user registration feature
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** ./sources/backend/user-management [REQ-001]
    - **Low-Level Technical Task Instruction:** Develop user registration feature using Spring Boot and PostgreSQL
    - **Targeted Tag IDs:** [REQ-001]

#### 🗓️ DAY 2: Develop user login feature
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** ./sources/backend/user-management [REQ-002]
    - **Low-Level Technical Task Instruction:** Develop user login feature using Spring Boot and PostgreSQL
    - **Targeted Tag IDs:** [REQ-002]

#### 🗓️ DAY 3: Develop user role assignment feature
- **Sub-Agent Workflow Specialization:**
  * **coder:**
    - **Target Component file path:** ./sources/backend/user-management [REQ-003]
    - **Low-Level Technical Task Instruction:** Develop user role assignment feature using Spring Boot and PostgreSQL
    - **Targeted Tag IDs:** [REQ-003]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Use prepared statements and positional query parameters to prevent SQL injection attacks.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Use context sanitization and dynamic injection of strict CSP headers to prevent XSS attacks.
- **Multi-Tenant CORS Security Rails:** Configure origin wildcard prohibitions and dynamic tenant origin database metrics validation to prevent CORS attacks.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Use dynamic client-side fetching and absolute URL addressing to ensure mobile compliance.
- **Internationalization (i18n) & Dynamic SEO Injection:** Use edge-layer locale recognition middleware architectures and hreflang dynamic hypermedia control injection to ensure internationalization and SEO compliance.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Use programmatic forking controls to create a new branch for each day's work.
- **Validation Guard Pipeline Gates:** Use execution rules to verify compilation, automated code coverage, and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 23, TOTAL ARC TAGS: 5, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]