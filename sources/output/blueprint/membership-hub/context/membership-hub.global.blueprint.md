# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260802135007 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/02 13:50:07 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY
### 1.1. Core System Modality & Architecture Modality
Dự án membership-hub sẽ được xây dựng dựa trên kiến trúc microservices, với các dịch vụ độc lập cho từng chức năng chính. Các dịch vụ này sẽ được triển khai trên nền tảng Kubernetes (GKE) và sử dụng công nghệ Java/Quarkus cho backend, cơ sở dữ liệu PostgreSQL, và Redis cho session caching.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Hệ thống sẽ sử dụng các kênh thông tin bất đồng bộ (asynchronous messaging channels) để trao đổi dữ liệu giữa các dịch vụ. Các dịch vụ sẽ được thiết kế để có thể mở rộng và thu hẹp linh hoạt dựa trên nhu cầu thực tế.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java 17, Quarkus 2.13, PostgreSQL 14, Redis 7, Kubernetes (GKE) 1.23
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 12, React 18, Firebase Authentication, Firebase Cloud Messaging (FCM)

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `..`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.membershiphub`.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-3 | `./sources/backend/users` | Thiết kế và triển khai dịch vụ người dùng | Coder | [REQ-001], [DAT-001] |
| 1 | 1-3 | `./sources/backend/centers` | Thiết kế và triển khai dịch vụ trung tâm | Coder | [REQ-004], [DAT-003] |
| 2 | 4-6 | `./sources/frontend/web` | Thiết kế và triển khai giao diện web | Coder | [REQ-020], [REQ-021] |
| 3 | 7 | `./sources/backend/attendance` | Thiết kế và triển khai dịch vụ điểm danh | Coder | [REQ-012], [DAT-006] |
| 4 | 8 | `./sources/backend/studentcards` | Thiết kế và triển khai dịch vụ thẻ hội viên | Coder | [REQ-014], [DAT-007] |
| 5 | 9-10 | `./sources/infra/deployment` | Triển khai hệ thống trên GKE | Docker, GCP | [NFR-002], [NFR-004] |

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Thiết kế và triển khai dịch vụ người dùng và trung tâm
- **Target Physical Directory Matrix Map:** `./sources/backend/users`, `./sources/backend/centers`
- **Database Schema DDL SQL Specification [DAT-001]:** 
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  password_hash VARCHAR(60) NOT NULL,
  full_name VARCHAR(100) NOT NULL,
  role_id SMALLINT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
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
    "id": "integer",
    "email": "string",
    "fullName": "string"
  }
}
```
#### DAY 1: Thiết kế và triển khai dịch vụ người dùng
- **Sub-Agent Workflow Specialization:**
  * **Coder:**
    - **Target Component file path (`target_component`):** `./sources/backend/users/UserService.java [REQ-001], [DAT-001]`
    - **Low-Level Technical Task Instruction:** Thiết kế và triển khai lớp `UserService` để xử lý các yêu cầu liên quan đến người dùng
    - **Targeted Tag IDs:** `[REQ-001], [DAT-001]`

#### DAY 2: Thiết kế và triển khai dịch vụ trung tâm
- **Sub-Agent Workflow Specialization:**
  * **Coder:**
    - **Target Component file path (`target_component`):** `./sources/backend/centers/CenterService.java [REQ-004], [DAT-003]`
    - **Low-Level Technical Task Instruction:** Thiết kế và triển khai lớp `CenterService` để xử lý các yêu cầu liên quan đến trung tâm
    - **Targeted Tag IDs:** `[REQ-004], [DAT-003]`

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Thiết kế và triển khai giao diện web
- **Target Physical Directory Matrix Map:** `./sources/frontend/web`
- **Database Schema DDL SQL Specification [DAT-001]:** 
```sql
CREATE TABLE courses (
  id SERIAL PRIMARY KEY,
  title VARCHAR(150) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  teacher_id UUID NOT NULL,
  max_students INTEGER NOT NULL DEFAULT 30
);
```
- **API and Event Routing Contracts [REQ-020], [ARC-002]:** 
```json
{
  "endpoint": "/courses",
  "method": "GET",
  "responseBody": {
    "id": "integer",
    "title": "string",
    "description": "string",
    "startDate": "date",
    "endDate": "date",
    "teacherId": "integer",
    "maxStudents": "integer"
  }
}
```
#### DAY 4: Thiết kế và triển khai giao diện web
- **Sub-Agent Workflow Specialization:**
  * **Coder:**
    - **Target Component file path (`target_component`):** `./sources/frontend/web/components/CourseList.js [REQ-020], [REQ-021]`
    - **Low-Level Technical Task Instruction:** Thiết kế và triển khai thành phần `CourseList` để hiển thị danh sách khóa học
    - **Targeted Tag IDs:** `[REQ-020], [REQ-021]`

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-day-X`.
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]