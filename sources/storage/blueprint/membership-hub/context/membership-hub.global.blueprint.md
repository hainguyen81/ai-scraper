# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260805144718 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/05 14:47:18 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống membership-hub là một nền tảng quản lý hội viên đa trung tâm với kiến trúc đa lớp bao gồm:
- Lớp giao diện người dùng (UI) bao gồm web và ứng dụng di động
- Lớp backend với các dịch vụ microservices
- Lớp cơ sở dữ liệu với PostgreSQL
- Lớp hạ tầng với Docker và Kubernetes (GKE)
- Lớp tích hợp với Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, và Zalo API

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Hệ thống sử dụng các kênh truyền thông đa kênh bao gồm:
- REST APIs cho giao tiếp giữa frontend và backend
- Event-driven architecture cho các thông báo và điểm danh
- Push notifications thông qua FCM/APNs
- Tích hợp với Zalo API cho các thông báo nhóm

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis, GitHub Actions
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React, Capacitor, Firebase Authentication

<!-- START_TECHNICAL_MATRIX_DO_NOT_TRANSLATE -->
### ARCHITECTURAL STACK MATRIX
[CRITICAL WARNING: You MUST keep this entire block 100% in raw Technical English. You are STRICTLY FORBIDDEN from translating any keys, values, or tokens inside this section into 🇻🇳 Vietnamese, as it serves as a strict backend machine-gating matrix. Keep literal `true` or `false` tokens in pure lower-case].

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```
<!-- END_TECHNICAL_MATRIX_DO_NOT_TRANSLATE -->

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `..`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Giai đoạn | Khoảng ngày | Cấu phần Kiến trúc / Module Đường dẫn | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Ngày 1-3 | `./sources/backend`, `./sources/frontend`, `./sources/infra` | Thiết kế kiến trúc tổng thể, thiết lập cơ sở hạ tầng, triển khai cơ sở dữ liệu | Coder, Docker, GCP, GKE | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| 2 | Ngày 4-5 | `./sources/backend`, `./sources/frontend` | Triển khai các tính năng quản lý người dùng, trung tâm, khóa học | Coder, Tester, Reviewer | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-001], [DAT-003], [DAT-004] |
| 3 | Ngày 6-7 | `./sources/backend`, `./sources/frontend` | Triển khai các tính năng đăng ký học viên, điểm danh QR, quản lý thẻ hội viên | Coder, Tester, Reviewer | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-005], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [EXC-004] |
| 4 | Ngày 1-2 | `./sources/backend`, `./sources/frontend` | Triển khai các tính năng thông báo, khuyến mãi, chatbot AI | Coder, Tester, Reviewer | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [DAT-008], [DAT-009], [EXC-003] |
| 5 | Ngày 3-4 | `./sources/backend`, `./sources/frontend` | Triển khai các tính năng báo cáo, phân tích, bản địa hóa, SEO | Coder, Tester, Reviewer | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-011], [EXC-005], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Thiết kế kiến trúc tổng thể, thiết lập cơ sở hạ tầng, triển khai cơ sở dữ liệu
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1: Thiết kế kiến trúc tổng thể và thiết lập cơ sở hạ tầng**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthService.java [ARC-006]`
      - **Low-Level Technical Task Instruction:** Triển khai dịch vụ xác thực với email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token
      - **Targeted Tag IDs:** [ARC-006]
    * **Docker:**
      - **Target Component file path (`target_component`):** `./sources/infra/docker-compose.yml [ARC-010]`
      - **Low-Level Technical Task Instruction:** Viết Docker Compose file để triển khai PostgreSQL, Redis, và các dịch vụ backend
      - **Targeted Tag IDs:** [ARC-010]
    * **GCP:**
      - **Target Component file path (`target_component`):** `./sources/infra/gcp/terraform/main.tf [ARC-010]`
      - **Low-Level Technical Task Instruction:** Viết Terraform script để triển khai cơ sở hạ tầng trên Google Cloud Platform
      - **Targeted Tag IDs:** [ARC-010]
    * **GKE:**
      - **Target Component file path (`target_component`):** `./sources/infra/gke/deployment.yml [ARC-010]`
      - **Low-Level Technical Task Instruction:** Viết Kubernetes deployment manifest để triển khai các dịch vụ backend trên Google Kubernetes Engine
      - **Targeted Tag IDs:** [ARC-010]

- **DAY 2: Triển khai cơ sở dữ liệu và các dịch vụ cơ bản**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]`
      - **Low-Level Technical Task Instruction:** Triển khai dịch vụ quản lý người dùng với các vai trò System Admin, Center Admin, Manager, Teacher, Student
      - **Targeted Tag IDs:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
    * **Docker:**
      - **Target Component file path (`target_component`):** `./sources/infra/docker-compose.yml [ARC-010]`
      - **Low-Level Technical Task Instruction:** Cập nhật Docker Compose file để triển khai các dịch vụ cơ bản
      - **Targeted Tag IDs:** [ARC-010]
    * **GCP:**
      - **Target Component file path (`target_component`):** `./sources/infra/gcp/terraform/main.tf [ARC-010]`
      - **Low-Level Technical Task Instruction:** Cập nhật Terraform script để triển khai cơ sở hạ tầng trên Google Cloud Platform
      - **Targeted Tag IDs:** [ARC-010]
    * **GKE:**
      - **Target Component file path (`target_component`):** `./sources/infra/gke/deployment.yml [ARC-010]`
      - **Low-Level Technical Task Instruction:** Cập nhật Kubernetes deployment manifest để triển khai các dịch vụ cơ bản trên Google Kubernetes Engine
      - **Targeted Tag IDs:** [ARC-010]

- **DAY 3: Triển khai các tính năng cơ bản và kiểm thử**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [ARC-008]`
      - **Low-Level Technical Task Instruction:** Triển khai dịch vụ thông báo với push notification đến ứng dụng di động và đăng bài lên nhóm Zalo
      - **Targeted Tag IDs:** [ARC-008]
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend/auth-service/src/test/java/org/nlh4j/saas/membershiphub/auth/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthService.java [ARC-006]`
      - **Low-Level Technical Task Instruction:** Viết các test case cho dịch vụ xác thực
      - **Targeted Tag IDs:** [ARC-006]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthService.java [ARC-006]`
      - **Low-Level Technical Task Instruction:** Review code cho dịch vụ xác thực
      - **Targeted Tag IDs:** [ARC-006]

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các tính năng quản lý người dùng, trung tâm, khóa học
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 4: Triển khai các tính năng quản lý người dùng**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java [REQ-001], [REQ-002], [REQ-003]`
      - **Low-Level Technical Task Instruction:** Triển khai các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003]
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend/user-service/src/test/java/org/nlh4j/saas/membershiphub/user/UserServiceTest.java;./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java [REQ-001], [REQ-002], [REQ-003]`
      - **Low-Level Technical Task Instruction:** Viết các test case cho các tính năng quản lý người dùng
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java [REQ-001], [REQ-002], [REQ-003]`
      - **Low-Level Technical Task Instruction:** Review code cho các tính năng quản lý người dùng
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003]

- **DAY 5: Triển khai các tính năng quản lý trung tâm và khóa học**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-004], [REQ-005], [REQ-006]`
      - **Low-Level Technical Task Instruction:** Triển khai các tính năng xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend/center-service/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-004], [REQ-005], [REQ-006]`
      - **Low-Level Technical Task Instruction:** Viết các test case cho các tính năng quản lý trung tâm
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-004], [REQ-005], [REQ-006]`
      - **Low-Level Technical Task Instruction:** Review code cho các tính năng quản lý trung tâm
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các tính năng đăng ký học viên, điểm danh QR, quản lý thẻ hội viên
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 6: Triển khai các tính năng đăng ký học viên và điểm danh QR**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java [REQ-010], [REQ-011]`
      - **Low-Level Technical Task Instruction:** Triển khai các tính năng duyệt khóa học, đăng ký khóa học của học viên
      - **Targeted Tag IDs:** [REQ-010], [REQ-011]
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend/enrollment-service/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentServiceTest.java;./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java [REQ-010], [REQ-011]`
      - **Low-Level Technical Task Instruction:** Viết các test case cho các tính năng đăng ký học viên
      - **Targeted Tag IDs:** [REQ-010], [REQ-011]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java [REQ-010], [REQ-011]`
      - **Low-Level Technical Task Instruction:** Review code cho các tính năng đăng ký học viên
      - **Targeted Tag IDs:** [REQ-010], [REQ-011]

- **DAY 7: Triển khai các tính năng quản lý thẻ hội viên**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-014], [REQ-015]`
      - **Low-Level Technical Task Instruction:** Triển khai các tính năng hiển thị tính hợp lệ của thẻ, gia hạn thẻ
      - **Targeted Tag IDs:** [REQ-014], [REQ-015]
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend/card-service/src/test/java/org/nlh4j/saas/membershiphub/card/CardServiceTest.java;./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-014], [REQ-015]`
      - **Low-Level Technical Task Instruction:** Viết các test case cho các tính năng quản lý thẻ hội viên
      - **Targeted Tag IDs:** [REQ-014], [REQ-015]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-014], [REQ-015]`
      - **Low-Level Technical Task Instruction:** Review code cho các tính năng quản lý thẻ hội viên
      - **Targeted Tag IDs:** [REQ-014], [REQ-015]

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các tính năng thông báo, khuyến mãi, chatbot AI
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1: Triển khai các tính năng thông báo và khuyến mãi**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016]`
      - **Low-Level Technical Task Instruction:** Triển khai các tính năng kích hoạt thông báo, quản lý khuyến mãi, quản lý thông báo
      - **Targeted Tag IDs:** [REQ-016]
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/test/java/org/nlh4j/saas/membershiphub/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016]`
      - **Low-Level Technical Task Instruction:** Viết các test case cho các tính năng thông báo và khuyến mãi
      - **Targeted Tag IDs:** [REQ-016]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016]`
      - **Low-Level Technical Task Instruction:** Review code cho các tính năng thông báo và khuyến mãi
      - **Targeted Tag IDs:** [REQ-016]

- **DAY 2: Triển khai các tính năng chatbot AI**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java [REQ-019]`
      - **Low-Level Technical Task Instruction:** Triển khai các tính năng tích hợp chatbot AI
      - **Targeted Tag IDs:** [REQ-019]
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend/chatbot-service/src/test/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotServiceTest.java;./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java [REQ-019]`
      - **Low-Level Technical Task Instruction:** Viết các test case cho các tính năng chatbot AI
      - **Targeted Tag IDs:** [REQ-019]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java [REQ-019]`
      - **Low-Level Technical Task Instruction:** Review code cho các tính năng chatbot AI
      - **Targeted Tag IDs:** [REQ-019]

### Phase 5 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các tính năng báo cáo, phân tích, bản địa hóa, SEO
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 3: Triển khai các tính năng báo cáo và phân tích**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java [REQ-024], [REQ-025]`
      - **Low-Level Technical Task Instruction:** Triển khai các tính năng tạo báo cáo điểm danh, bảng điều khiển tóm tắt ghi danh
      - **Targeted Tag IDs:** [REQ-024], [REQ-025]
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend/report-service/src/test/java/org/nlh4j/saas/membershiphub/report/ReportServiceTest.java;./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java [REQ-024], [REQ-025]`
      - **Low-Level Technical Task Instruction:** Viết các test case cho các tính năng báo cáo và phân tích
      - **Targeted Tag IDs:** [REQ-024], [REQ-025]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java [REQ-024], [REQ-025]`
      - **Low-Level Technical Task Instruction:** Review code cho các tính năng báo cáo và phân tích
      - **Targeted Tag IDs:** [REQ-024], [REQ-025]

- **DAY 4: Triển khai các tính năng bản địa hóa và SEO**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend/i18n-service/src/main/java/org/nlh4j/saas/membershiphub/i18n/I18nService.java [REQ-022], [REQ-023]`
      - **Low-Level Technical Task Instruction:** Triển khai các tính năng phát hiện ngôn ngữ mặc định, SEO đa ngôn ngữ
      - **Targeted Tag IDs:** [REQ-022], [REQ-023]
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend/i18n-service/src/test/java/org/nlh4j/saas/membershiphub/i18n/I18nServiceTest.java;./sources/backend/i18n-service/src/main/java/org/nlh4j/saas/membershiphub/i18n/I18nService.java [REQ-022], [REQ-023]`
      - **Low-Level Technical Task Instruction:** Viết các test case cho các tính năng bản địa hóa và SEO
      - **Targeted Tag IDs:** [REQ-022], [REQ-023]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend/i18n-service/src/main/java/org/nlh4j/saas/membershiphub/i18n/I18nService.java [REQ-022], [REQ-023]`
      - **Low-Level Technical Task Instruction:** Review code cho các tính năng bản địa hóa và SEO
      - **Targeted Tag IDs:** [REQ-022], [REQ-023]

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