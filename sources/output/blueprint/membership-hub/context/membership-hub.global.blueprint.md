# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806034940 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 03:49:40 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống được thiết kế theo kiến trúc microservice hướng sự kiện (EDA) với các biên giới CQRS rõ ràng. Các lõi nghiệp vụ chính bao gồm Quản lý Người dùng, Quản lý Trung tâm, Quản lý Khóa học, Ghi danh, Điểm danh, Thẻ hội viên, Thông báo, Khuyến mãi, Thông báo, Chatbot AI, và Giao diện di động. Các dịch vụ hoạt động độc lập, giao tiếp qua message broker (ví dụ: Kafka) và REST APIs. Các mẫu Reactive Core được áp dụng cho các luồng có tính chất thời gian thực như quét QR điểm danh và push notification. Các chính sách bảo mật được thực thi ở biên giới tenant để đảm bảo cô lập hoàn toàn giữa các trung tâm.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Các luồng dữ liệu chính được định nghĩa như sau:

* **Luồng xác thực ([ARC-006])** – OAuth2 với Firebase, Google, Facebook; cấp JWT (15 phút) và refresh token.
* **Luồng xử lý điểm danh QR ([ARC-007])** – Ứng dụng di động quét QR, gửi studentId + timestamp đến backend; dịch vụ xác thực idempotent.
* **Luồng gửi thông báo ([ARC-008])** – Backend kích hoạt push notification (FCM/APNs) và đăng bài lên nhóm Zalo được chỉ định cho các hành động như chỉ định khóa học, cảnh báo điểm danh.
* **Luồng tích hợp backend ứng dụng di động ([ARC-009])** – Frontend Next.js tiêu thụ REST APIs, xác thực qua bearer token, hỗ trợ caching ngoại tuyến.

Các kênh này được đồng bộ hóa qua hàng đợi bất đồng bộ để đảm bảo tính khả dụng và độ trễ thấp.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:**
  * Runtime: Java 21 + Quarkus 3.x (DI, Reactive, Mutiny).
  * Persistence: PostgreSQL 15+ với JDBC driver, Hibernate ORM (Panache).
  * Messaging: Kafka (hoặc RabbitMQ) cho event bus.
  * Authentication: Firebase Auth SDK tích hợp qua OAuth2.
  * Push Notification: Firebase Cloud Messaging (FCM) cho Android, Apple APNs cho iOS.
  * Integration: REST clients (WebClient), Zalo API SDK.
  * Caching: Redis (Lettuce) cho session và cache ngoại tuyến.
  * DevOps: Docker multi‑stage images, Kubernetes (GKE) với HPA, GitHub Actions CI/CD.
  * Monitoring: Smallrye Health, OpenTelemetry.

- **Frontend & Cross-Platform UI Mobile Stack:**
  * Web: Next.js 14 (React 18) với App Router, Server Components, i18n (next-intl).
  * Mobile: React Native với Capacitor để đóng gói native, tích hợp FCM/APNs, local storage (`@capacitor/preferences`).
  * State Management: Redux Toolkit + RTK Query.
  * UI Framework: Tailwind CSS + Material-UI.
  * Build Tools: Vite cho mobile bundles, Webpack cho web.

### ARCHITECTURAL STACK MATRIX
<COMMAND>
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
</COMMAND>

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** Root repository là `.`; mọi đường dẫn phải bắt đầu bằng `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Backend logic nằm dưới `./sources/backend.<service-name>/`, Frontend dưới `./sources/frontend/`, Di động dưới `./sources/frontend.mobile/`, Infra dưới `./sources/infra/`.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Tất cả mã nguồn Java phải nằm trong gói `org.nlh4j.saas.membershiphub` (đã chuẩn hóa từ "membership-hub").
- **Strict Tester Target Path Syntax:** Mọi mục tiêu kiểm thử phải là cặp `<source_component>;<test_suite_file>` (ví dụ: `./sources/backend.user-management;./sources/backend.user-management/src/test/java/...`).
- **Security Gating:** Tuân thủ OWASP Top 10, chuẩn bị statement, xác thực đầu vào, mã hóa JWT, logging kiểm toán.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | Days 1‑2 | ./sources/docs/system-overview.md | Tài liệu tổng quan kiến trúc hệ thống, luồng dữ liệu, mô hình nghiệp vụ. | Doc | [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| **Phase 1** | Days 1‑2 | ./sources/docs/tech-stack.md | Bản đồ chi tiết công nghệ backend, frontend, di động, devops. | Doc | [ARC-010], [NFR-004], [NFR-005], [NFR-006] |
| **Phase 1** | Days 1‑2 | ./sources/docs/guardrails.md | Quy tắc nghiệp vụ, giới hạn đường dẫn, chuẩn đóng gói Java, quy tắc kiểm thử. | Doc | [NFR-001], [NFR-002], [NFR-003], [NFR-007], [NFR-008], [NFR-009] |
| **Phase 2** | Days 3‑5 | ./sources/backend.user-management (service) | Triển khai đăng ký người dùng, xác thực xã hội, phân quyền. | Coder | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004] |
| **Phase 2** | Days 3‑5 | ./sources/backend.user-management;./sources/backend.user-management/src/test/java/org/nlh4j/saas/membershiphub/user/UserServiceTest.java | Kiểm thử đơn vị cho đăng ký, đăng nhập xã hội, và cập nhật vai trò. | Tester | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004] |
| **Phase 3** | Days 6‑7 | ./sources/backend.center-management (service) | Triển khai CRUD trung tâm và API gán quyền quản trị. | Coder | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| **Phase 3** | Days 6‑7 | ./sources/backend.center-management;./sources/backend.center-management/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java | Kiểm thử danh sách trung tâm, tạo/sửa/xóa, và gán quyền. | Tester | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| **Phase 4** | Days 8‑10 | ./sources/backend.course-management (service) | Triển khai CRUD khóa học, kiểm tra xung đột lịch, và API phân công giáo viên. | Coder | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| **Phase 4** | Days 8‑10 | ./sources/backend.enrollment-management (service) | Triển khai duyệt khóa học, ghi danh học viên, tích hợp thông báo. | Coder | [REQ-010], [REQ-011], [DAT-005] |
| **Phase 4** | Days 8‑10 | ./sources/backend.course-management;./sources/backend.course-management/src/test/java/org/nlh4j/saas/membershiphub/course/CourseServiceTest.java | Kiểm thử logic xung đột lịch, tạo khóa học, và gán giáo viên. | Tester | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| **Phase 4** | Days 8‑10 | ./sources/backend.enrollment-management;./sources/backend.enrollment-management/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentServiceTest.java | Kiểm thử duyệt khóa học, ghi danh, tạo tài khoản học viên, và tích hợp thông báo. | Tester | [REQ-010], [REQ-011], [DAT-005] |
| **Phase 5** | Days 11‑17 | ./sources/backend.attendance (service) | Triển khai API quét QR, ghi nhận điểm danh, đảm bảo bất biến, xử lý ngoại lệ mạng và trùng lặp. | Coder | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002] |
| **Phase 5** | Days 11‑17 | ./sources/backend.membership-card (service) | Triển khai API hiển thị thẻ hội viên và API gia hạn thẻ. | Coder | [REQ-014], [REQ-015], [DAT-007] |
| **Phase 5** | Days 11‑17 | ./sources/backend.notification (service) | Triển khai API tạo thông báo, đẩy push (FCM/APNs), đăng bài Zalo, xử lý lỗi gửi. | Coder | [REQ-016], [DAT-008], [EXC-003] |
| **Phase 5** | Days 11‑17 | ./sources/backend.promotion (service) | Triển khai CRUD khuyến mãi và thông báo. | Coder | [REQ-017], [REQ-018], [DAT-009] |
| **Phase 5** | Days 11‑17 | ./sources/docs/chatbot-ai.md | Tài liệu hóa thiết kế tích hợp chatbot AI. | Doc | [REQ-019] |
| **Phase 5** | Days 11‑17 | ./sources/frontend.mobile (source) | Triển khai giao diện người dùng vai trò trên di động, push notification, phát hiện ngôn ngữ, SEO đa ngôn ngữ. | Coder | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011] |
| **Phase 5** | Days 11‑17 | ./sources/backend.reporting (service) | Triển khai API tạo báo cáo điểm danh (CSV) và API bảng điều khiển tóm tắt. | Coder | [REQ-024], [REQ-025] |
| **Phase 5** | Days 11‑17 | ./sources/infra/docker/Dockerfile | Dockerfile multi-stage tối ưu hóa kích thước image (<500MB). | Docker | [NFR-005] |
| **Phase 5** | Days 11‑17 | ./sources/infra/gcp (scripts) | Cung cấp VPC, IAM, Redis, PostgreSQL, CI/CD trên GCP, tuân thủ NFR-002, NFR-003, NFR-004. | GCP | [NFR-002], [NFR-003], [NFR-004] |
| **Phase 5** | Days 11‑17 | ./sources/infra/gke (manifests) | Tạo Kubernetes Deployment, Service, HPA cho các ứng dụng Quarkus, tuân thủ NFR-004. | GKE | [NFR-004] |
| **Phase 5** | Days 11‑17 | ./sources/docs/security-review.md | Đánh giá tuân thủ OWASP, kiểm soát bảo mật, logging, audit. | Reviewer | [NFR-001], [NFR-003] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

<!--START_DELIMITTER-->
### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng nền tảng tài liệu và thiết kế kiến trúc ban đầu, xác định các biên giới nghiệp vụ, luồng dữ liệu, và các tiêu chuẩn tuân thủ toàn cầu.
- **Target Physical Directory Matrix Map:** 
    * ./sources/docs/system-overview.md ([ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009])
    * ./sources/docs/tech-stack.md ([ARC-010], [NFR-004], [NFR-005], [NFR-006])
    * ./sources/docs/guardrails.md ([NFR-001], [NFR-002], [NFR-003], [NFR-007], [NFR-008], [NFR-009])
- **Database Schema DDL SQL Specification:** *(Không có lớp dữ liệu trong giai đoạn này)*
- **API and Event Routing Contracts:** *(Không có API trong giai đoạn này)*
- **Phase Localized Exception Handlers:** *(Không có ngoại lệ chuyên biệt trong giai đoạn này)*

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1:** Mục tiêu ngắn hạn: Soạn thảo tài liệu tổng quan kiến trúc hệ thống.
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/docs/system-overview.md ([ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009])
      - **Low-Level Technical Task Instruction:** Soạn thảo tài liệu tổng quan kiến trúc hệ thống, bao gồm mô tả các module nghiệp vụ chính, luồng xác thực ([ARC-006]), luồng xử lý điểm danh QR ([ARC-007]), luồng gửi thông báo ([ARC-008]), luồng tích hợp backend ứng dụng di động ([ARC-009]), và các chỉ số hiệu năng then chốt ([NFR-001]‑[NFR-009]).
      - **Targeted Tag IDs:** [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]

- **DAY 2:** Mục tiêu ngắn hạn: Soạn thảo tài liệu công nghệ và guardrails.
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/docs/tech-stack.md ([ARC-010], [NFR-004], [NFR-005], [NFR-006])
      - **Low-Level Technical Task Instruction:** Tài liệu hóa bản đồ công nghệ backend (Java/Quarkus, PostgreSQL, Kafka, Firebase Auth, FCM/APNs, Zalo API, Redis, CI/CD), frontend (Next.js, React, Capacitor), và các quy tắc bảo mật, tuân thủ các yêu cầu hiệu năng ([NFR-004]‑[NFR-006]).
      - **Targeted Tag IDs:** [ARC-010], [NFR-004], [NFR-005], [NFR-006]

    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/docs/guardrails.md ([NFR-001], [NFR-002], [NFR-003], [NFR-007], [NFR-008], [NFR-009])
      - **Low-Level Technical Task Instruction:** Định nghĩa các quy tắc nghiệp vụ: giới hạn đường dẫn vật lý (`./sources/`), chuẩn đóng gói Java (`org.nlh4j.saas.membershiphub`), quy tắc kiểm thử (cặp `<source>;<test>`), và các yêu cầu bảo mật, tuân thủ các tiêu chuẩn toàn cầu ([NFR-001]‑[NFR-009]).
      - **Targeted Tag IDs:** [NFR-001], [NFR-002], [NFR-003], [NFR-007], [NFR-008], [NFR-009]

### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai module Quản lý Người dùng bao gồm đăng ký, xác thực xã hội, và phân quyền người dùng.
- **Target Physical Directory Matrix Map:** 
    * ./sources/backend.user-management ([REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004])
    * ./sources/backend.user-management;./sources/backend.user-management/src/test/java/org/nlh4j/saas/membershiphub/user/UserServiceTest.java ([REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004])
- **Database Schema DDL SQL Specification [DAT-001]:**
```sql
CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL REFERENCES roles(role_id),
    provider ENUM('local','firebase','google','facebook') NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now()
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
```json
// Đăng ký (POST /api/users/register)
{
  "email": "user@example.com",
  "password": "StrongPass123!",
  "fullName": "Nguyen Van A",
  "provider": "local"
}

// Xác thực xã hội (POST /api/auth/social)
{
  "provider": "google",
  "code": "OAuth2_code_from_Google",
  "idToken": "firebase_id_token"
}

// Gán vai trò (PUT /api/users/{userId}/role)
{
  "roleId": 2
}
```
- **Phase Localized Exception Handlers [EXC-004]:** Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc). Khi xác thực form thất bại, hệ thống trả về một đối tượng lỗi liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 3:** Mục tiêu ngắn hạn: Triển khai service quản lý người dùng.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.user-management/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java ([REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004])
      - **Low-Level Technical Task Instruction:** Triển khai các API đăng ký (POST /api/users/register), xác thực xã hội (POST /api/auth/social), và gán vai trò (PUT /api/users/{userId}/role). Sử dụng Spring Data JPA để tương tác với bảng `users` và `roles`, thực hiện xác thực đầu vào theo quy định [EXC-004], và trả về JWT token sau khi tạo thành công.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004]

- **DAY 4:** Mục tiêu ngắn hạn: Soạn thảo kiểm thử cho service người dùng.
  - **Sub-Agent Workflow Specialization:**
    * **[Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.user-management;./sources/backend.user-management/src/test/java/org/nlh4j/saas/membershiphub/user/UserServiceTest.java ([REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004])
      - **Low-Level Technical Task Instruction:** Soạn thảo các trường hợp kiểm thử đơn vị bao phủ đăng ký người dùng thành công, xác thực xã hội, cập nhật vai trò, và các trường hợp ngoại lệ đầu vào không hợp lệ. Đảm bảo độ phủ mã >=85% và tích hợp với CI pipeline.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004]

- **DAY 5:** Mục tiêu ngắn hạn: Triển khai service quản lý trung tâm.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.center-management/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java ([REQ-004], [REQ-005], [REQ-006], [DAT-003])
      - **Low-Level Technical Task Instruction:** Triển khai CRUD cho Trung tâm (GET /api/centers, POST /api/centers, PUT /api/centers/{centerId}, DELETE /api/centers/{centerId}) và API gán quyền quản trị (POST /api/users/{userId}/center/{centerId}). Sử dụng bảng `centers` ([DAT-003]), thực hiện kiểm tra taxId trùng lặp, và tuân thủ các quy tắc RBAC cho Center Admin ([ARC-002]).
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]

### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng module Quản lý Trung tâm với các chức năng CRUD và phân quyền quản trị trung tâm.
- **Target Physical Directory Matrix Map:** 
    * ./sources/backend.center-management ([REQ-004], [REQ-005], [REQ-006], [DAT-003])
    * ./sources/backend.center-management;./sources/backend.center-management/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java ([REQ-004], [REQ-005], [REQ-006], [DAT-003])
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) NOT NULL UNIQUE,
    contact_phone VARCHAR(30),
    contact_email VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [ARC-002]:**
```json
// Danh sách trung tâm (GET /api/centers)
[]

// Tạo trung tâm (POST /api/centers)
{
  "name": "Center A",
  "address": "123 Street, City",
  "taxId": "1234567890",
  "contactPhone": "+84 123 456 789",
  "contactEmail": "center@example.com"
}

// Gán quyền quản trị trung tâm (POST /api/users/{userId}/center/{centerId})
{}
```
- **Phase Localized Exception Handlers:** *(Không có ngoại lệ chuyên biệt trong giai đoạn này)*

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 6:** Mục tiêu ngắn hạn: Soạn thảo kiểm thử cho service trung tâm.
  - **Sub-Agent Workflow Specialization:**
    * **[Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.center-management;./sources/backend.center-management/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java ([REQ-004], [REQ-005], [REQ-006], [DAT-003])
      - **Low-Level Technical Task Instruction:** Soạn thảo các trường hợp kiểm thử cho danh sách trung tâm, tạo/sửa/xóa trung tâm, và gán quyền quản trị, bao gồm kiểm tra taxId trùng lặp và xác thực quyền truy cập của System Admin.
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]

- **DAY 7:** Mục tiêu ngắn hạn: Triển khai service quản lý khóa học.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.course-management/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java ([REQ-007], [REQ-008], [REQ-009], [DAT-004])
      - **Low-Level Technical Task Instruction:** Triển khai CRUD khóa học (GET /api/courses, POST /api/courses, PUT /api/courses/{courseId}, DELETE /api/courses/{courseId}) với kiểm tra xung đột lịch giảng cho giáo viên, và API phân công giáo viên (POST /api/courses/{courseId}/teacher/{teacherId}). Sử dụng bảng `courses` ([DAT-004]) và tuân thủ các quy tắc RBAC cho System Admin và Center Admin.
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004]

### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng module Quản lý Khóa học và Ghi danh Học viên, bao gồm duyệt khóa học, ghi danh, và tích hợp thông báo.
- **Target Physical Directory Matrix Map:** 
    * ./sources/backend.course-management ([REQ-007], [REQ-008], [REQ-009], [DAT-004])
    * ./sources/backend.enrollment-management ([REQ-010], [REQ-011], [DAT-005])
    * ./sources/backend.course-management;./sources/backend.course-management/src/test/java/org/nlh4j/saas/membershiphub/course/CourseServiceTest.java ([REQ-007], [REQ-008], [REQ-009], [DAT-004])
    * ./sources/backend.enrollment-management;./sources/backend.enrollment-management/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentServiceTest.java ([REQ-010], [REQ-011], [DAT-005])
- **Database Schema DDL SQL Specification [DAT-004]:**
```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
);
```
**Database Schema DDL SQL Specification [DAT-005]:**
```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT now()
);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [ARC-001], [ARC-002], [ARC-003]:**
```json
// Danh sách khóa học (GET /api/courses)
[
  {"courseId":"uuid","title":"Lập trình Java","startDate":"2026-09-01","endDate":"2026-12-31","teacherName":"Nguyen A"}
]

// Tạo khóa học (POST /api/courses)
{
  "title":"Lập trình Python",
  "description":"Khóa học về Python",
  "startDate":"2026-10-01",
  "endDate":"2026-12-31",
  "teacherId":"uuid_of_teacher",
  "maxStudents":20
}

// Phân công giáo viên (POST /api/courses/{courseId}/teacher/{teacherId})
{}

// Duyệt khóa học (GET /api/enrollments/courses)
[
  {"courseId":"uuid","title":"Lập trình Java","availableSlots":10}
]

// Ghi danh khóa học (POST /api/enrollments)
{
  "courseId":"uuid"
}
```
- **Phase Localized Exception Handlers:** *(Không có ngoại lệ chuyên biệt trong giai đoạn này)*

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 8:** Mục tiêu ngắn hạn: Soạn thảo kiểm thử cho service khóa học.
  - **Sub-Agent Workflow Specialization:**
    * **[Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.course-management;./sources/backend.course-management/src/test/java/org/nlh4j/saas/membershiphub/course/CourseServiceTest.java ([REQ-007], [REQ-008], [REQ-009], [DAT-004])
      - **Low-Level Technical Task Instruction:** Soạn thảo các trường hợp kiểm thử cho logic tạo khóa học, cập nhật, xóa, và phân công giáo viên, bao gồm kiểm tra xung đột lịch giảng và xác thực quyền truy cập.
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004]

- **DAY 9:** Mục tiêu ngắn hạn: Triển khai service ghi danh học viên.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment-management/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java ([REQ-010], [REQ-011], [DAT-005])
      - **Low-Level Technical Task Instruction:** Triển khai API duyệt khóa học (GET /api/enrollments/courses) và API ghi danh (POST /api/enrollments). Tự động tạo tài khoản học viên nếu thiếu, gán vai trò `Student` ([ARC-005]), và tạo thông báo đẩy cùng bài đăng Zalo. Sử dụng bảng `enrollments` ([DAT-005]) và tuân thủ các quy tắc RBAC.
      - **Targeted Tag IDs:** [REQ-010], [REQ-011], [DAT-005]

- **DAY 10:** Mục tiêu ngắn hạn: Soạn thảo kiểm thử cho service ghi danh.
  - **Sub-Agent Workflow Specialization:**
    * **[Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment-management;./sources/backend.enrollment-management/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentServiceTest.java ([REQ-010], [REQ-011], [DAT-005])
      - **Low-Level Technical Task Instruction:** Soạn thảo các trường hợp kiểm thử cho duyệt khóa học, ghi danh, tạo tài khoản học viên, và tích hợp thông báo, bao gồm kiểm tra xung đột ghi danh và các trường hợp ngoại lệ.
      - **Targeted Tag IDs:** [REQ-010], [REQ-011], [DAT-005]

### 📈 Phase 5 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai các tính năng nâng cao bao gồm Điểm danh QR, Thẻ hội viên, Thông báo, Khuyến mãi, Thông báo, Chatbot AI, Giao diện di động, Bản địa hóa, Báo cáo, và các cấu hình hạ tầng (Docker, GCP, GKE). Hoàn thiện các yêu cầu phi chức năng và đảm bảo tuân thủ bảo mật.
- **Target Physical Directory Matrix Map:** 
    * ./sources/backend.attendance ([REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002])
    * ./sources/backend.membership-card ([REQ-014], [REQ-015], [DAT-007])
    * ./sources/backend.notification ([REQ-016], [DAT-008], [EXC-003])
    * ./sources/backend.promotion ([REQ-017], [REQ-018], [DAT-009])
    * ./sources/docs/chatbot-ai.md ([REQ-019])
    * ./sources/frontend.mobile ([REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011])
    * ./sources/backend.reporting ([REQ-024], [REQ-025])
    * ./sources/infra/docker/Dockerfile ([NFR-005])
    * ./sources/infra/gcp ([NFR-002], [NFR-003], [NFR-004])
    * ./sources/infra/gke ([NFR-004])
    * ./sources/docs/security-review.md ([NFR-001], [NFR-003])
- **Database Schema DDL SQL Specification [DAT-006]:**
```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);
```
**Database Schema DDL SQL Specification [DAT-007]:**
```sql
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);
```
**Database Schema DDL SQL Specification [DAT-008]:**
```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT now(),
    delivered BOOLEAN NOT NULL DEFAULT false
);
```
**Database Schema DDL SQL Specification [DAT-009]:**
```sql
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT
);

CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);
```
**Database Schema DDL SQL Specification [DAT-011]:**
```sql
CREATE TABLE system_settings (
    setting_key VARCHAR(100) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description VARCHAR(200)
);
```
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-001]‑[ARC-010]:**
```json
// Quét điểm danh QR (POST /api/attendance/scan)
{
  "studentId":"uuid_of_student",
  "courseId":"uuid_of_course",
  "timestamp":"2026-08-06T03:49:40Z"
}

// Hiển thị thẻ hội viên (GET /api/membership-card/{studentId})
{
  "cardId":"uuid",
  "validityDays":365,
  "remainingDays":300
}

// Gia hạn thẻ (POST /api/membership-card/{studentId}/renew)
{
  "additionalDays":30
}

// Tạo thông báo (POST /api/notifications)
{
  "userId":"uuid",
  "groupZalo":"group_xyz",
  "message":"Bạn có điểm danh mới"
}

// Quản lý khuyến mãi (POST /api/promotions)
{
  "code":"SUMMER20",
  "discountPercent":20,
  "startDate":"2026-06-01",
  "endDate":"2026-08-31",
  "description":"Giảm giá mùa hè"
}

// Quản lý thông báo (POST /api/announcements)
{
  "title":"Thông báo hệ thống",
  "content":"Hệ thống bảo trì vào cuối tuần.",
  "startDate":"2026-08-09",
  "endDate":"2026-08-10"
}

// Chatbot AI (POST /api/chatbot/ask)
{
  "question":"Khóa học lập trình Java có ở đâu?"
}
{
  "answer":"Khóa học lập trình Java được tổ chức tại trung tâm TP.HCM..."
}

// Giao diện di động vai trò (GET /api/mobile/ui/{role})
{
  "role":"Student",
  "menu":[
    {"label":"Duyệt khóa học","path":"/courses"},
    {"label":"Thẻ hội viên","path":"/card"}
  ]
}

// Thông báo đẩy di động (POST /api/mobile/push)
{
  "userId":"uuid",
  "title":"Điểm danh thành công",
  "body":"Bạn đã điểm danh môn Lập trình Java."
}

// Phát hiện ngôn ngữ mặc định (GET /api/i18n/default)
{
  "locale":"vi"
}

// SEO hreflang (GET /api/seo/hreflang)
[
  {"lang":"en","url":"https://example.com/en"},
  {"lang":"vi","url":"https://example.com/vi"},
  {"lang":"es","url":"https://example.com/es"}
]

// Báo cáo điểm danh (GET /api/reports/attendance?centerId=uuid&date=2026-08-06)
CSV với các cột: StudentName, CourseName, AttendanceDate, Status

// Bảng điều khiển tóm tắt (GET /api/dashboard)
{
  "totalStudents":150,
  "activeCourses":12,
  "upcomingSessions":5
}
```
- **Phase Localized Exception Handlers [EXC-001]‑[EXC-005]:**
  * **[EXC-001] – Network & Connectivity Drops During QR Scan:** Nếu sinh viên quét QR nhưng mạng không khả dụng, ứng dụng di động lưu sự kiện cục bộ. Khi kết nối được khôi phục, ứng dụng tự động gửi lại yêu cầu đến `/api/attendance/scan`. Service xử lý điểm danh đảm bảo idempotent: nhiều lần gửi cho cùng studentId, courseId, attendanceDate chỉ tạo một bản ghi.
  * **[EXC-002] – Duplicate Attendance Submission:** Nếu cùng sinh viên quét cùng course QR nhiều lần trong ngày, service phát hiện bản ghi attendanceDate đã tồn tại, trả về success với cờ `duplicate: true` và không tạo thêm hàng.
  * **[EXC-003] – Failed Notification Delivery:** Khi push notification không thể gửi (ví dụ: token thiết bị không hợp lệ), hệ thống ghi log lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu `delivered: false`.
  * **[EXC-004] – Invalid Input Validation (User Module):** Xác thực đầu vào cho đăng ký và xác thực xã hội, liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.
  * **[EXC-005] – System Recovery After Outage:** Sau khi phục hồi, hàng đợi điểm danh chờ xử lý được thực hiện theo thứ tự FIFO, và người dùng nhận thông báo về các sự kiện đã phục hồi.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 11:** Mục tiêu ngắn hạn: Triển khai service điểm danh QR.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.attendance/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java ([REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002])
      - **Low-Level Technical Task Instruction:** Triển khai API `/api/attendance/scan` nhận `studentId`, `courseId`, `timestamp`. Xác thực mối quan hệ học viên-khóa học, ghi nhận bản ghi điểm danh với `attendance_date` là ngày hiện tại, đảm bảo bất biến cho cùng ngày. Xử lý ngoại lệ mạng [EXC-001] bằng cách lưu sự kiện cục bộ và tái thử khi kết nối được khôi phục. Phát hiện trùng lặp [EXC-002] và trả về cờ duplicate.
      - **Targeted Tag IDs:** [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]

- **DAY 12:** Mục tiêu ngắn hạn: Triển khai service thẻ hội viên.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership-card/src/main/java/org/nlh4j/saas/membershiphub/membershipcard/MembershipCardService.java ([REQ-014], [REQ-015], [DAT-007])
      - **Low-Level Technical Task Instruction:** Triển khai API `/api/membership-card/{studentId}` trả về `validityDays`, `remainingDays` từ bảng `student_cards` ([DAT-007]), và API `/api/membership-card/{studentId}/renew` để gia hạn thẻ bằng cách cộng thêm `additionalDays` vào `remainingDays`. Cập nhật `remainingDays` và lưu bản ghi.
      - **Targeted Tag IDs:** [REQ-014], [REQ-015], [DAT-007]

- **DAY 13:** Mục tiêu ngắn hạn: Triển khai service thông báo.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java ([REQ-016], [DAT-008], [EXC-003])
      - **Low-Level Technical Task Instruction:** Triển khai API `/api/notifications` để tạo thông báo mới, đẩy push notification (FCM/APNs) đến token thiết bị đã đăng ký, và đăng bài lên nhóm Zalo được chỉ định. Ghi log lỗi gửi và lên lịch thử lại tối đa 3 lần theo [EXC-003].
      - **Targeted Tag IDs:** [REQ-016], [DAT-008], [EXC-003]

- **DAY 14:** Mục tiêu ngắn hạn: Triển khai service khuyến mãi & thông báo.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.promotion/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionService.java ([REQ-017], [REQ-018], [DAT-009])
      - **Low-Level Technical Task Instruction:** Triển khai CRUD cho Khuyến mãi (`/api/promotions`) và Thông báo (`/api/announcements`). Hỗ trợ ngày bắt đầu/kết thúc tùy chọn, tự động ẩn thông báo hết hạn. Sử dụng bảng `promotions` và `announcements` ([DAT-009]).
      - **Targeted Tag IDs:** [REQ-017], [REQ-018], [DAT-009]

- **DAY 15:** Mục tiêu ngắn hạn: Soạn thảo tài liệu chatbot AI.
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/docs/chatbot-ai.md ([REQ-019])
      - **Low-Level Technical Task Instruction:** Tài liệu hóa thiết kế tích hợp chatbot AI: các điểm cuối (`/api/chatbot/ask`), quy tắc xử lý câu hỏi, giới hạn độ tin cậy, hướng dẫn triển khai, và các bước kiểm thử.
      - **Targeted Tag IDs:** [REQ-019]

- **DAY 16:** Mục tiêu ngắn hạn: Triển khai giao diện di động & bản địa hóa.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/frontend.mobile/src/app (ví dụ: ./sources/frontend.mobile/src/app/core)
      - **Low-Level Technical Task Instruction:** Triển khai giao diện người dùng vai trò trên di động (Student, Teacher, Admin) với điều hướng dựa trên vai trò, tích hợp push notification (FCM/APNs), middleware phát hiện ngôn ngữ (`Accept-Language`, lưu vào `system_settings` [DAT-011]), và chèn thẻ hreflang cho SEO đa ngôn ngữ. Đảm bảo responsive và tuân thủ các quy tắc Capacitor hybrid.
      - **Targeted Tag IDs:** [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]

- **DAY 17:** Mục tiêu ngắn hạn: Triển khai báo cáo, infra, và đánh giá bảo mật.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.reporting/src/main/java/org/nlh4j/saas/membershiphub/reporting/ReportingService.java ([REQ-024], [REQ-025])
      - **Low-Level Technical Task Instruction:** Triển khai API `/api/reports/attendance` trả về CSV với các cột StudentName, CourseName, AttendanceDate, Status, và API `/api/dashboard` trả về tổng hợp số liệu (totalStudents, activeCourses, upcomingSessions). Sử dụng các bảng hiện có để tổng hợp.
      - **Targeted Tag IDs:** [REQ-024], [REQ-025]

    * **[Docker]:**
      - **Target Component file path (`target_component`):** ./sources/infra/docker/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo multi-stage Dockerfile: giai đoạn build sử dụng Maven + Quarkus, giai đoạn runtime sử dụng OpenJDK 21 slim. Tối ưu hóa kích thước image (<500MB) theo [NFR-005].
      - **Targeted Tag IDs:** [NFR-005]

    * **[GCP]:**
      - **Target Component file path (`target_component`):** ./sources/infra/gcp (ví dụ: ./sources/infra/gcp/terraform/main.tf)
      - **Low-Level Technical Task Instruction:** Triển khai infrastructure as code trên GCP: tạo VPC, Private Subnet, Cloud SQL instance cho PostgreSQL, Cloud Storage cho artifact, IAM service accounts, và kích hoạt API cần thiết. Cấu hình backup tự động và failover theo vùng. Đáp ứng các yêu cầu [NFR-002], [NFR-003], [NFR-004].
      - **Targeted Tag IDs:** [NFR-002], [NFR-003], [NFR-004]

    * **[GKE]:**
      - **Target Component file path (`target_component`):** ./sources/infra/gke (ví dụ: ./sources/infra/gke/deployment.yaml)
      - **Low-Level Technical Task Instruction:** Soạn thảo Kubernetes Deployment, Service, HPA, và ConfigMap cho các ứng dụng Quarkus. Cấu hình resource limits/requests để tuân thủ scaling theo [NFR-004]. Thiết lập Ingress với TLS.
      - **Targeted Tag IDs:** [NFR-004]

    * **[Reviewer]:**
      - **Target Component file path (`target_component`):** ./sources/docs/security-review.md
      - **Low-Level Technical Task Instruction:** Đánh giá mã nguồn để đảm bảo tuân thủ OWASP Top 10, bao gồm prepared statements, xác thực đầu vào, kiểm soát CORS, logging kiểm toán, và các yêu cầu bảo mật [NFR-001], [NFR-003]. Ghi lại các phát hiện và đề xuất remediation.
      - **Targeted Tag IDs:** [NFR-001], [NFR-003]

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`