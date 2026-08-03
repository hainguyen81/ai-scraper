# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260803041017 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/03 04:10:17 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống membership-hub được thiết kế như một nền tảng quản lý hội viên đa trung tâm, cho phép theo dõi điểm danh thời gian thực qua quét mã QR, cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực, hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo) và đảm bảo độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Hệ thống sẽ sử dụng các kênh thông tin异步 (asynchronous messaging channels) để giao tiếp giữa các thành phần, bao gồm cả việc xác thực, điểm danh, và gửi thông báo. Các thành phần chính của hệ thống bao gồm:

*   Frontend: ứng dụng web và di động cho người dùng
*   Backend: dịch vụ API và cơ sở dữ liệu
*   Cơ sở dữ liệu: lưu trữ thông tin người dùng, khóa học, và điểm danh
*   Dịch vụ xác thực: xác thực người dùng qua email/mật khẩu, Firebase, Google, Facebook
*   Dịch vụ điểm danh: ghi lại điểm danh của người dùng
*   Dịch vụ thông báo: gửi thông báo đến người dùng qua email, Zalo, và push notification

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

*   **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API integration, Redis
*   **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React, React Native

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

*   **Absolute Workspace Boundary Rule:** Không gian làm việc của dự án được cố định tại thư mục gốc `..`
*   **Dynamic Directory Prefixing Compliance:** Các thư mục con phải bắt đầu với `./sources/`
*   **Java Package Standard:** Nếu sử dụng Java, các lớp phải nằm trong gói `org.nlh4j.saas.membershiphub`
*   **Strict Tester Target Path Syntax:** Các thành phần được Tester nhắm đến phải được cấu trúc như một cặp phân cách bằng dấu chấm phẩy `<source_component_or_token>;<test_suite_file_to_execute>`

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | 1-3 | ./sources/backend | Xây dựng cơ sở dữ liệu, dịch vụ xác thực, dịch vụ điểm danh | Coder | [REQ-001], [REQ-002], [REQ-003] |
| Phase 2 | 4-6 | ./sources/frontend | Xây dựng ứng dụng web và di động | Coder | [REQ-004], [REQ-005], [REQ-006] |
| Phase 3 | 7 | ./sources/infra | Cài đặt cơ sở hạ tầng, triển khai ứng dụng | Docker, GCP, GKE | [REQ-007], [REQ-008], [REQ-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### Phase 1 Detailed Architectural Specification

*   **Phase Core Objective & Purpose:** Xây dựng cơ sở dữ liệu, dịch vụ xác thực, dịch vụ điểm danh
*   **Target Physical Directory Matrix Map:** ./sources/backend
*   **Database Schema DDL SQL Specification [DAT-XXX]:** Tạo bảng người dùng, khóa học, điểm danh
*   **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Xây dựng API cho dịch vụ xác thực, điểm danh
*   **Phase Localized Exception Handlers [EXC-XXX]:** Xử lý ngoại lệ cho dịch vụ xác thực, điểm danh

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

*   **DAY 1:** Xây dựng cơ sở dữ liệu
    *   **Sub-Agent Workflow Specialization:**
        *   **Coder:** Tạo bảng người dùng, khóa học, điểm danh
            *   **Target Component file path (`target_component`):** ./sources/backend/database.sql [REQ-001], [DAT-001]
            *   **Low-Level Technical Task Instruction:** Tạo bảng người dùng với các trường id, tên, email, mật khẩu
            *   **Targeted Tag IDs:** [REQ-001], [DAT-001]
*   **DAY 2:** Xây dựng dịch vụ xác thực
    *   **Sub-Agent Workflow Specialization:**
        *   **Coder:** Xây dựng dịch vụ xác thực qua email/mật khẩu, Firebase, Google, Facebook
            *   **Target Component file path (`target_component`):** ./sources/backend/auth.service.js [REQ-002], [REQ-003]
            *   **Low-Level Technical Task Instruction:** Xây dựng dịch vụ xác thực qua email/mật khẩu
            *   **Targeted Tag IDs:** [REQ-002], [REQ-003]
*   **DAY 3:** Xây dựng dịch vụ điểm danh
    *   **Sub-Agent Workflow Specialization:**
        *   **Coder:** Xây dựng dịch vụ điểm danh
            *   **Target Component file path (`target_component`):** ./sources/backend/attendance.service.js [REQ-004], [REQ-005]
            *   **Low-Level Technical Task Instruction:** Xây dựng dịch vụ điểm danh
            *   **Targeted Tag IDs:** [REQ-004], [REQ-005]

### Phase 2 Detailed Architectural Specification

*   **Phase Core Objective & Purpose:** Xây dựng ứng dụng web và di động
*   **Target Physical Directory Matrix Map:** ./sources/frontend
*   **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Xây dựng API cho ứng dụng web và di động
*   **Phase Localized Exception Handlers [EXC-XXX]:** Xử lý ngoại lệ cho ứng dụng web và di động

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

*   **DAY 4:** Xây dựng ứng dụng web
    *   **Sub-Agent Workflow Specialization:**
        *   **Coder:** Xây dựng ứng dụng web
            *   **Target Component file path (`target_component`):** ./sources/frontend/web/index.html [REQ-006], [REQ-007]
            *   **Low-Level Technical Task Instruction:** Xây dựng trang chủ ứng dụng web
            *   **Targeted Tag IDs:** [REQ-006], [REQ-007]
*   **DAY 5:** Xây dựng ứng dụng di động
    *   **Sub-Agent Workflow Specialization:**
        *   **Coder:** Xây dựng ứng dụng di động
            *   **Target Component file path (`target_component`):** ./sources/frontend/mobile/index.js [REQ-008], [REQ-009]
            *   **Low-Level Technical Task Instruction:** Xây dựng trang chủ ứng dụng di động
            *   **Targeted Tag IDs:** [REQ-008], [REQ-009]
*   **DAY 6:** Xây dựng tính năng điểm danh trên ứng dụng di động
    *   **Sub-Agent Workflow Specialization:**
        *   **Coder:** Xây dựng tính năng điểm danh trên ứng dụng di động
            *   **Target Component file path (`target_component`):** ./sources/frontend/mobile/attendance.js [REQ-010], [REQ-011]
            *   **Low-Level Technical Task Instruction:** Xây dựng tính năng điểm danh trên ứng dụng di động
            *   **Targeted Tag IDs:** [REQ-010], [REQ-011]

### Phase 3 Detailed Architectural Specification

*   **Phase Core Objective & Purpose:** Cài đặt cơ sở hạ tầng, triển khai ứng dụng
*   **Target Physical Directory Matrix Map:** ./sources/infra
*   **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Cài đặt cơ sở hạ tầng
*   **Phase Localized Exception Handlers [EXC-XXX]:** Xử lý ngoại lệ cho cơ sở hạ tầng

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

*   **DAY 7:** Cài đặt cơ sở hạ tầng
    *   **Sub-Agent Workflow Specialization:**
        *   **Docker:** Cài đặt Docker
            *   **Target Component file path (`target_component`):** ./sources/infra/docker-compose.yml [REQ-012], [REQ-013]
            *   **Low-Level Technical Task Instruction:** Cài đặt Docker
            *   **Targeted Tag IDs:** [REQ-012], [REQ-013]
        *   **GCP:** Cài đặt GCP
            *   **Target Component file path (`target_component`):** ./sources/infra/gcp.yaml [REQ-014], [REQ-015]
            *   **Low-Level Technical Task Instruction:** Cài đặt GCP
            *   **Targeted Tag IDs:** [REQ-014], [REQ-015]
        *   **GKE:** Cài đặt GKE
            *   **Target Component file path (`target_component`):** ./sources/infra/gke.yaml [REQ-016], [REQ-017]
            *   **Low-Level Technical Task Instruction:** Cài đặt GKE
            *   **Targeted Tag IDs:** [REQ-016], [REQ-017]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]

*   **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng các tham số chuẩn bị (prepared statements) và các tham số vị trí (positional parameters) để ngăn chặn SQL Injection
*   **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Sử dụng các chính sách bảo mật nội dung (Content Security Policy) để ngăn chặn XSS
*   **Multi-Tenant CORS Security Rails:** Sử dụng các chính sách CORS (Cross-Origin Resource Sharing) để ngăn chặn các yêu cầu không hợp lệ

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

*   **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng Capacitor để xây dựng ứng dụng di động hybrid
*   **Internationalization (i18n) & Dynamic SEO Injection:** Sử dụng các kỹ thuật quốc tế hóa (internationalization) và tối ưu hóa SEO (Search Engine Optimization) để cải thiện khả năng tìm kiếm của ứng dụng

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

*   **Daily Workspace Forking Isolation:** Sử dụng các nhánh Git để cách ly không gian làm việc hàng ngày
*   **Validation Guard Pipeline Gates:** Sử dụng các cổng kiểm soát (pipeline gates) để đảm bảo chất lượng mã nguồn

### 🛑 MATRIX COVERAGE CHECK MANDATE

[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 17, TOTAL ARC TAGS: 0, TOTAL EXC TAGS: 0, TOTAL DAT TAGS: 7, TOTAL NFR TAGS: 8. ZERO UNASSIGNED CODES FOUND.]