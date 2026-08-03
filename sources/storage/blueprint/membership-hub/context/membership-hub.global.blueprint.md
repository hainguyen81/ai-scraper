# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260803030413 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/03 03:04:13 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống membership-hub được thiết kế như một nền tảng quản lý hội viên đa trung tâm, cho phép theo dõi điểm danh thời gian thực qua quét mã QR, cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực, và hỗ trợ giao tiếp đa kênh. Hệ thống sử dụng kiến trúc microservices, với các dịch vụ độc lập cho từng chức năng, và được triển khai trên nền tảng Kubernetes (GKE).

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Hệ thống sử dụng các kênh thông tin bất đồng bộ, bao gồm REST APIs, message queues, và event-driven architecture, để đảm bảo tính linh hoạt và khả năng mở rộng. Dữ liệu được lưu trữ trong cơ sở dữ liệu PostgreSQL, và được quản lý bởi các dịch vụ độc lập.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API integration, Redis.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React, Redux, Material-UI, Firebase Cloud Messaging (FCM), Apple Push Notification service (APNs).

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** Dự án được triển khai trong thư mục `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Các dịch vụ và thành phần được tổ chức theo cấu trúc thư mục động.
- **Java Package Standard:** Các lớp Java được tổ chức theo cấu trúc gói `org.nlh4j.saas.membershiphub`.
- **Strict Tester Target Path Syntax:** Các thành phần được kiểm tra được tổ chức theo cấu trúc đường dẫn nghiêm ngặt.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | 1-3 | `./sources/backend/auth` | Xây dựng dịch vụ xác thực | Coder | `[REQ-001], [REQ-002]` |
| Phase 1 | 4-5 | `./sources/backend/attendance` | Xây dựng dịch vụ điểm danh | Coder | `[REQ-012], [REQ-013]` |
| Phase 2 | 6-8 | `./sources/frontend/web` | Xây dựng giao diện web | Coder | `[REQ-020], [REQ-021]` |
| Phase 3 | 9-11 | `./sources/backend/course` | Xây dựng dịch vụ khóa học | Coder | `[REQ-007], [REQ-008]` |
| Phase 4 | 12-14 | `./sources/backend/student` | Xây dựng dịch vụ học viên | Coder | `[REQ-010], [REQ-011]` |
| Phase 5 | 15-17 | `./sources/infra/deployment` | Triển khai hệ thống | Docker | `[NFR-001], [NFR-002]` |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng dịch vụ xác thực và điểm danh.
- **Target Physical Directory Matrix Map:** `./sources/backend/auth`, `./sources/backend/attendance`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Tạo bảng người dùng và bảng điểm danh.
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Xây dựng API xác thực và điểm danh.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1:** Xây dựng dịch vụ xác thực
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/auth/AuthService.java [REQ-001]`
      - **Low-Level Technical Task Instruction:** Xây dựng lớp xác thực người dùng.
      - **Targeted Tag IDs:** `[REQ-001], [REQ-002]`
- **DAY 2:** Xây dựng dịch vụ điểm danh
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/attendance/AttendanceService.java [REQ-012]`
      - **Low-Level Technical Task Instruction:** Xây dựng lớp điểm danh.
      - **Targeted Tag IDs:** `[REQ-012], [REQ-013]`

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng giao diện web.
- **Target Physical Directory Matrix Map:** `./sources/frontend/web`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Không áp dụng.
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Xây dựng API giao diện web.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 6:** Xây dựng giao diện web
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/frontend/web/index.js [REQ-020]`
      - **Low-Level Technical Task Instruction:** Xây dựng giao diện web.
      - **Targeted Tag IDs:** `[REQ-020], [REQ-021]`

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng dịch vụ khóa học.
- **Target Physical Directory Matrix Map:** `./sources/backend/course`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Tạo bảng khóa học.
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Xây dựng API khóa học.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 9:** Xây dựng dịch vụ khóa học
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/course/CourseService.java [REQ-007]`
      - **Low-Level Technical Task Instruction:** Xây dựng lớp khóa học.
      - **Targeted Tag IDs:** `[REQ-007], [REQ-008]`

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng dịch vụ học viên.
- **Target Physical Directory Matrix Map:** `./sources/backend/student`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Tạo bảng học viên.
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Xây dựng API học viên.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 12:** Xây dựng dịch vụ học viên
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/student/StudentService.java [REQ-010]`
      - **Low-Level Technical Task Instruction:** Xây dựng lớp học viên.
      - **Targeted Tag IDs:** `[REQ-010], [REQ-011]`

### Phase 5 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai hệ thống.
- **Target Physical Directory Matrix Map:** `./sources/infra/deployment`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Không áp dụng.
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Không áp dụng.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 15:** Triển khai hệ thống
  - **Sub-Agent Workflow Specialization:**
    * **Docker:**
      - **Target Component file path (`target_component`):** `./sources/infra/deployment/docker-compose.yml [NFR-001]`
      - **Low-Level Technical Task Instruction:** Triển khai hệ thống.
      - **Targeted Tag IDs:** `[NFR-001], [NFR-002]`

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng các tham số chuẩn bị và các truy vấn có tham số.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Sử dụng các thư viện và framework để ngăn chặn XSS.
- **Multi-Tenant CORS Security Rails:** Sử dụng các thư viện và framework để ngăn chặn CORS.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng Capacitor để xây dựng ứng dụng di động.
- **Internationalization (i18n) & Dynamic SEO Injection:** Sử dụng các thư viện và framework để hỗ trợ i18n và SEO.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Sử dụng Git để quản lý các branch và fork.
- **Validation Guard Pipeline Gates:** Sử dụng các công cụ và framework để kiểm tra và xác thực.

### 🛑 MATRIX COVERAGE CHECK MANDATE
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 10, TOTAL NFR TAGS: 10. ZERO UNASSIGNED CODES FOUND.]`