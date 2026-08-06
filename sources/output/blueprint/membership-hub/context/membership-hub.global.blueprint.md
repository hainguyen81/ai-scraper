# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806155517 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 15:55:17 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURAL MODALITY

### 1.1. Core System Modality & Architecture Modality
- Hệ thống được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, trung tâm, khóa học, điểm danh, và thẻ hội viên.
- Sử dụng mô hình Event-Driven Architecture (EDA) cho các tính năng như điểm danh QR và thông báo đẩy.
- Áp dụng mô hình CQRS (Command Query Responsibility Segregation) để phân tách các thao tác ghi và đọc dữ liệu.
- Sử dụng mô hình Reactive Programming cho các tính năng thời gian thực như điểm danh và thông báo.
- Hệ thống được thiết kế để hoạt động trong môi trường đa trung tâm với khả năng mở rộng cao.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Sử dụng Kafka để quản lý các luồng dữ liệu bất đồng bộ như điểm danh, thông báo, và tích hợp với Zalo.
- Sử dụng Redis để quản lý session và caching dữ liệu.
- Sử dụng PostgreSQL để lưu trữ dữ liệu quan hệ.
- Sử dụng Firebase Authentication cho xác thực người dùng.
- Sử dụng Firebase Cloud Messaging (FCM) và Apple APNs cho thông báo đẩy.
- Sử dụng Zalo API để gửi thông báo đến nhóm Zalo.
- Sử dụng Docker để container hóa các dịch vụ và triển khai trên Kubernetes (GKE).

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Firebase Cloud Messaging (FCM), Apple APNs, Zalo API, Redis, GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React Native, Firebase Authentication, Firebase Cloud Messaging (FCM), Apple APNs, Zalo API.

### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Giai đoạn | Khoảng ngày | Cấu phần Kiến trúc / Module Đường dẫn | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1 - 2 | `./sources/backend/`, `./sources/frontend/`, `./sources/docs/` | Thiết kế kiến trúc tổng thể, thiết lập cơ sở dữ liệu, triển khai xác thực người dùng | Coder, Doc, GCP | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 2 | Ngày 1 - 2 | `./sources/backend/`, `./sources/frontend/`, `./sources/docs/` | Triển khai quản lý người dùng, trung tâm, khóa học, điểm danh, thẻ hội viên | Coder, Tester, Doc | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005] |
| Giai đoạn 3 | Ngày 1 - 2 | `./sources/backend/`, `./sources/frontend/`, `./sources/docs/` | Triển khai chatbot dịch vụ khách hàng AI, tích hợp với Zalo, triển khai thông báo đẩy | Coder, Tester, Doc, Docker, GKE | [REQ-019], [ARC-008], [ARC-009], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | Ngày 1 - 2 | `./sources/backend/`, `./sources/frontend/`, `./sources/docs/` | Triển khai bản địa hóa và SEO, báo cáo và phân tích | Coder, Tester, Doc, Docker, GKE | [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 5 | Ngày 1 - 2 | `./sources/backend/`, `./sources/frontend/`, `./sources/docs/` | Triển khai các tính năng cốt lõi của ứng dụng di động, kiểm thử và triển khai | Coder, Tester, Doc, Docker, GKE | [REQ-020], [REQ-021], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Giai đoạn 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Thiết kế kiến trúc tổng thể, thiết lập cơ sở dữ liệu, triển khai xác thực người dùng.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Thiết lập cơ sở dữ liệu PostgreSQL với các bảng Users, Roles, Centers, Courses, Enrollments, Attendance, StudentCards, Notifications, Promotions, Announcements, SystemSettings.
- **Hợp đồng Định tuyến API và Sự kiện [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]:** Thiết lập các endpoint cho xác thực người dùng, quản lý trung tâm, khóa học, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]:** Thiết lập các quy tắc bảo mật, hiệu suất, khả dụng, khả năng mở rộng, kích thước hình ảnh Docker, ghi nhật ký và kiểm toán, hỗ trợ đa ngôn ngữ, tuân thủ GDPR/CCPA, sao lưu và phục hồi thảm họa.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 1)

- **DAY 1: Thiết kế kiến trúc tổng thể và thiết lập cơ sở dữ liệu**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Thiết kế kiến trúc tổng thể, thiết lập cơ sở dữ liệu PostgreSQL, triển khai xác thực người dùng.

- **DAY 2: Triển khai xác thực người dùng và quản lý trung tâm**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Targeted Tag IDs:** [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Triển khai xác thực người dùng, quản lý trung tâm, khóa học, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo.

### 📈 Giai đoạn 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai quản lý người dùng, trung tâm, khóa học, điểm danh, thẻ hội viên.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Triển khai các bảng Users, Roles, Centers, Courses, Enrollments, Attendance, StudentCards, Notifications, Promotions, Announcements, SystemSettings.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]:** Triển khai các endpoint cho quản lý người dùng, trung tâm, khóa học, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Thiết lập các quy tắc xử lý ngoại lệ cho điểm danh, thông báo, báo cáo và phân tích.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 2)

- **DAY 1: Triển khai quản lý người dùng và trung tâm**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [DAT-001], [DAT-003], [EXC-004]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Triển khai quản lý người dùng, trung tâm.

- **DAY 2: Triển khai quản lý khóa học và điểm danh**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-004], [DAT-005], [DAT-006], [EXC-001], [EXC-002]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Triển khai quản lý khóa học, điểm danh.

### 📈 Giai đoạn 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai chatbot dịch vụ khách hàng AI, tích hợp với Zalo, triển khai thông báo đẩy.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
- **Hợp đồng Định tuyến API và Sự kiện [REQ-019], [ARC-008], [ARC-009]:** Triển khai chatbot dịch vụ khách hàng AI, tích hợp với Zalo, triển khai thông báo đẩy.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [NFR-006], [NFR-007], [NFR-008], [NFR-009]:** Thiết lập các quy tắc bảo mật, hiệu suất, khả dụng, khả năng mở rộng, kích thước hình ảnh Docker, ghi nhật ký và kiểm toán, hỗ trợ đa ngôn ngữ, tuân thủ GDPR/CCPA, sao lưu và phục hồi thảm họa.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 3)

- **DAY 1: Triển khai chatbot dịch vụ khách hàng AI**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-019], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Triển khai chatbot dịch vụ khách hàng AI.

- **DAY 2: Tích hợp với Zalo và triển khai thông báo đẩy**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Targeted Tag IDs:** [ARC-008], [ARC-009], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Tích hợp với Zalo, triển khai thông báo đẩy.

### 📈 Giai đoạn 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai bản địa hóa và SEO, báo cáo và phân tích.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
- **Hợp đồng Định tuyến API và Sự kiện [REQ-022], [REQ-023], [REQ-024], [REQ-025]:** Triển khai bản địa hóa và SEO, báo cáo và phân tích.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [NFR-007], [NFR-008], [NFR-009]:** Thiết lập các quy tắc bảo mật, hiệu suất, khả dụng, khả năng mở rộng, kích thước hình ảnh Docker, ghi nhật ký và kiểm toán, hỗ trợ đa ngôn ngữ, tuân thủ GDPR/CCPA, sao lưu và phục hồi thảm họa.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 4)

- **DAY 1: Triển khai bản địa hóa và SEO**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-022], [REQ-023], [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Triển khai bản địa hóa và SEO.

- **DAY 2: Triển khai báo cáo và phân tích**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [REQ-024], [REQ-025], [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Triển khai báo cáo và phân tích.

### 📈 Giai đoạn 5 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai các tính năng cốt lõi của ứng dụng di động, kiểm thử và triển khai.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
- **Hợp đồng Định tuyến API và Sự kiện [REQ-020], [REQ-021]:** Triển khai các tính năng cốt lõi của ứng dụng di động.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]:** Thiết lập các quy tắc bảo mật, hiệu suất, khả dụng, khả năng mở rộng, kích thước hình ảnh Docker, ghi nhật ký và kiểm toán, hỗ trợ đa ngôn ngữ, tuân thủ GDPR/CCPA, sao lưu và phục hồi thảm họa.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 5)

- **DAY 1: Triển khai các tính năng cốt lõi của ứng dụng di động**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-020], [REQ-021], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Triển khai các tính năng cốt lõi của ứng dụng di động.

- **DAY 2: Kiểm thử và triển khai**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** `./sources/backend/`, `./sources/frontend/`, `./sources/docs/`
    * **Low-Level Technical Task Instruction:** Kiểm thử và triển khai.

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`