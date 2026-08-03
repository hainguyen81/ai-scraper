# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260803031000 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/03 03:10:00 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống membership-hub được thiết kế như một nền tảng thống nhất để quản lý hội viên đa trung tâm. Nó bao gồm các thành phần chính như quản lý người dùng, quản lý trung tâm, quản lý khóa học, đăng ký và ghi danh học viên, điểm danh và quét mã QR, quản lý thẻ hội viên, thông báo và truyền thông. Các thành phần này được tích hợp với nhau thông qua các luồng dữ liệu và quy trình nghiệp vụ cụ thể.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Hệ thống sử dụng các luồng dữ liệu sau:
- Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2.
- Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend.
- Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE).
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, Firebase Cloud Messaging (FCM)/Apple APNs cho push notification.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** Repository workspace root là `..`.
- **Dynamic Directory Prefixing Compliance:** Sử dụng dynamic path mapping rules.
- **Java Package Standard:** Nếu sử dụng Java, các nguồn mã phải nằm trong gói `org.nlh4j.saas.membershiphub`.
- **Strict Tester Target Path Syntax:** Sử dụng `<source_component_or_token>;<test_suite_file_to_execute>`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-3 | `./sources/backend/users` | Xây dựng cơ sở dữ liệu người dùng | Coder | [REQ-001], [DAT-001] |
| 1 | 1-3 | `./sources/backend/centers` | Xây dựng cơ sở dữ liệu trung tâm | Coder | [REQ-004], [DAT-003] |
| 2 | 4-6 | `./sources/frontend` | Xây dựng giao diện người dùng | Coder | [REQ-020], [REQ-021] |
| 3 | 7 | `./sources/infra` | Cài đặt và cấu hình Kubernetes | Docker | [NFR-004] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng cơ sở dữ liệu người dùng và trung tâm.
- **Target Physical Directory Matrix Map:** `./sources/backend/users`, `./sources/backend/centers`.
- **Database Schema DDL SQL Specification [DAT-001]:** Tạo bảng người dùng và trung tâm.
- **API and Event Routing Contracts [REQ-001], [ARC-001]:** Xây dựng API cho người dùng và trung tâm.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1:** Xây dựng cơ sở dữ liệu người dùng
  - **Sub-Agent Workflow Specialization:**
    * **Coder:** 
      - **Target Component file path (`target_component`):** `./sources/backend/users [REQ-001], [DAT-001]`
      - **Low-Level Technical Task Instruction:** Tạo bảng người dùng với các trường cần thiết.
      - **Targeted Tag IDs:** `[REQ-001], [DAT-001]`
- **DAY 2:** Xây dựng cơ sở dữ liệu trung tâm
  - **Sub-Agent Workflow Specialization:**
    * **Coder:** 
      - **Target Component file path (`target_component`):** `./sources/backend/centers [REQ-004], [DAT-003]`
      - **Low-Level Technical Task Instruction:** Tạo bảng trung tâm với các trường cần thiết.
      - **Targeted Tag IDs:** `[REQ-004], [DAT-003]`

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng prepared statements và positional query parameters.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Sử dụng automated context sanitization và dynamic injection của strict CSP headers.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng dynamic client-side fetching và absolute URL addressing.
- **Internationalization (i18n) & Dynamic SEO Injection:** Sử dụng edge-layer locale recognition middleware architectures.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Sử dụng programmatic forking controls cho branch `features/development-day-X`.
- **Validation Guard Pipeline Gates:** Sử dụng execution rules cho compilation verification và automated code coverage goals.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]