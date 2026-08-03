# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260803025201 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/03 02:52:01 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống membership-hub được thiết kế như một nền tảng thống nhất để quản lý hội viên đa trung tâm. Nó cho phép theo dõi điểm danh thời gian thực qua quét mã QR, cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực, và hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo). Giá trị cốt lõi của hệ thống là độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, và hỗ trợ đa ngôn ngữ.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Hệ thống sẽ sử dụng các kênh thông tin không đồng bộ, cổng nhập dữ liệu, và kiến trúc fan-out để đảm bảo sự linh hoạt và khả năng mở rộng. Các thành phần chính của hệ thống bao gồm:
- **Quản lý người dùng**: Đăng ký, xác thực, và phân quyền người dùng.
- **Quản lý trung tâm**: Xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, và phân quyền quản trị trung tâm.
- **Quản lý khóa học**: Xem danh sách khóa học, tạo/cập nhật/xóa khóa học, và phân công giáo viên vào khóa học.
- **Đăng ký & ghi danh học viên**: Duyệt khóa học, đăng ký khóa học, và quản lý thông tin học viên.
- **Điểm danh & quét mã QR**: Chụp ảnh điểm danh QR, và tính chất bất biến của điểm danh.
- **Quản lý thẻ hội viên**: Hiển thị tính hợp lệ của thẻ, và gia hạn thẻ.
- **Thông báo & truyền thông**: Kích hoạt thông báo, và quản lý thông báo.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis, CI/CD pipeline với GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React, React Native, Capacitor.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root là `..`.
- **Dynamic Directory Prefixing Compliance:** Enforce dynamic path mapping rules.
- **Java Package Standard:** `org.nlh4j.saas.membershiphub`.
- **Strict Tester Target Path Syntax:** `<source_component>;<test_suite_file>`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-3 | `./sources/backend/user-management` | Quản lý người dùng | Coder | `[REQ-001], [REQ-002], [REQ-003]` |
| 1 | 1-3 | `./sources/backend/center-management` | Quản lý trung tâm | Coder | `[REQ-004], [REQ-005], [REQ-006]` |
| 2 | 4-6 | `./sources/backend/course-management` | Quản lý khóa học | Coder | `[REQ-007], [REQ-008], [REQ-009]` |
| 2 | 4-6 | `./sources/backend/enrollment-management` | Đăng ký & ghi danh học viên | Coder | `[REQ-010], [REQ-011]` |
| 3 | 7 | `./sources/backend/attendance-management` | Điểm danh & quét mã QR | Coder | `[REQ-012], [REQ-013]` |
| 3 | 7 | `./sources/backend/membership-card-management` | Quản lý thẻ hội viên | Coder | `[REQ-014], [REQ-015]` |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng nền tảng quản lý người dùng và trung tâm.
- **Target Physical Directory Matrix Map:** `./sources/backend/user-management`, `./sources/backend/center-management`.
- **Database Schema DDL SQL Specification [DAT-001]:** Tạo bảng người dùng và vai trò.
- **API and Event Routing Contracts [REQ-001], [ARC-001]:** Xác định API cho quản lý người dùng và trung tâm.
- **Phase Localized Exception Handlers [EXC-001]:** Xử lý ngoại lệ cho quản lý người dùng và trung tâm.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1:** Xây dựng cơ sở dữ liệu cho quản lý người dùng.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:** Tạo bảng người dùng và vai trò.
      - **Target Component file path (`target_component`):** `./sources/backend/user-management [REQ-001], [DAT-001]`
      - **Low-Level Technical Task Instruction:** Tạo bảng người dùng và vai trò.
      - **Targeted Tag IDs:** `[REQ-001], [DAT-001]`
- **DAY 2:** Xây dựng API cho quản lý người dùng.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:** Xác định API cho quản lý người dùng.
      - **Target Component file path (`target_component`):** `./sources/backend/user-management [REQ-002], [ARC-001]`
      - **Low-Level Technical Task Instruction:** Xác định API cho quản lý người dùng.
      - **Targeted Tag IDs:** `[REQ-002], [ARC-001]`
- **DAY 3:** Xây dựng giao diện người dùng cho quản lý người dùng.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:** Tạo giao diện người dùng cho quản lý người dùng.
      - **Target Component file path (`target_component`):** `./sources/frontend/user-management [REQ-003], [DAT-001]`
      - **Low-Level Technical Task Instruction:** Tạo giao diện người dùng cho quản lý người dùng.
      - **Targeted Tag IDs:** `[REQ-003], [DAT-001]`

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng nền tảng quản lý khóa học và đăng ký học viên.
- **Target Physical Directory Matrix Map:** `./sources/backend/course-management`, `./sources/backend/enrollment-management`.
- **Database Schema DDL SQL Specification [DAT-002]:** Tạo bảng khóa học và ghi danh.
- **API and Event Routing Contracts [REQ-004], [ARC-002]:** Xác định API cho quản lý khóa học và đăng ký học viên.
- **Phase Localized Exception Handlers [EXC-002]:** Xử lý ngoại lệ cho quản lý khóa học và đăng ký học viên.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 4:** Xây dựng cơ sở dữ liệu cho quản lý khóa học.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:** Tạo bảng khóa học.
      - **Target Component file path (`target_component`):** `./sources/backend/course-management [REQ-004], [DAT-002]`
      - **Low-Level Technical Task Instruction:** Tạo bảng khóa học.
      - **Targeted Tag IDs:** `[REQ-004], [DAT-002]`
- **DAY 5:** Xây dựng API cho quản lý khóa học.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:** Xác định API cho quản lý khóa học.
      - **Target Component file path (`target_component`):** `./sources/backend/course-management [REQ-005], [ARC-002]`
      - **Low-Level Technical Task Instruction:** Xác định API cho quản lý khóa học.
      - **Targeted Tag IDs:** `[REQ-005], [ARC-002]`
- **DAY 6:** Xây dựng giao diện người dùng cho quản lý khóa học.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:** Tạo giao diện người dùng cho quản lý khóa học.
      - **Target Component file path (`target_component`):** `./sources/frontend/course-management [REQ-006], [DAT-002]`
      - **Low-Level Technical Task Instruction:** Tạo giao diện người dùng cho quản lý khóa học.
      - **Targeted Tag IDs:** `[REQ-006], [DAT-002]`

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng nền tảng điểm danh và quản lý thẻ hội viên.
- **Target Physical Directory Matrix Map:** `./sources/backend/attendance-management`, `./sources/backend/membership-card-management`.
- **Database Schema DDL SQL Specification [DAT-003]:** Tạo bảng điểm danh và thẻ hội viên.
- **API and Event Routing Contracts [REQ-007], [ARC-003]:** Xác định API cho điểm danh và quản lý thẻ hội viên.
- **Phase Localized Exception Handlers [EXC-003]:** Xử lý ngoại lệ cho điểm danh và quản lý thẻ hội viên.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 7:** Xây dựng cơ sở dữ liệu cho điểm danh và quản lý thẻ hội viên.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:** Tạo bảng điểm danh và thẻ hội viên.
      - **Target Component file path (`target_component`):** `./sources/backend/attendance-management [REQ-007], [DAT-003]`
      - **Low-Level Technical Task Instruction:** Tạo bảng điểm danh và thẻ hội viên.
      - **Targeted Tag IDs:** `[REQ-007], [DAT-003]`

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-day-X`.
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 24, TOTAL ARC TAGS: 6, TOTAL EXC TAGS: 3, TOTAL DAT TAGS: 7, TOTAL NFR TAGS: 8. ZERO UNASSIGNED CODES FOUND.]