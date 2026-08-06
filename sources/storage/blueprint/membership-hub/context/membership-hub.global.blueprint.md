# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806025754 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 02:57:54 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Mô tả kiến trúc hệ thống: membership‑hub được thiết kế theo kiến trúc microservices, áp dụng mô hình CQRS cho các hoạt động đọc/ghi, sử dụng reactive programming cho các luồng xử lý bất đồng bộ như xác thực OAuth2, quét QR điểm danh, và gửi thông báo đẩy. Mỗi trung tâm hoạt động như một tenant độc lập với RBAC nghiêm ngặt. Các service được container hóa bằng Docker, triển khai trên Kubernetes (GKE) với khả năng mở rộng ngang dựa trên HPA.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Mô tả các luồng dữ liệu chính:
- **Đăng ký & Xác thực:** Người dùng đăng ký qua email/mật khẩu hoặc mạng xã hội → OAuth2 → cấp JWT (15 phút) + refresh token.
- **Điểm danh QR:** Ứng dụng di động quét QR → gửi studentId + timestamp → service xác thực quan hệ học viên‑khóa học, ghi lại điểm danh một cách bất biến.
- **Thông báo:** Backend kích hoạt push notification (FCM/APNs) và đăng bài lên nhóm Zalo được chỉ định cho các hành động như tạo thông báo, phân công khóa học, cảnh báo điểm danh.
- **Tích hợp di động:** Frontend Next.js tiêu thụ REST APIs, xác thực qua bearer tokens, hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:**
  * Runtime: Java 21 + Quarkus X.Y
  * Persistence: PostgreSQL 15 với JPA/Hibernate
  * Containerization: Docker (<200 MB base, <500 MB final)
  * Orchestration: Kubernetes (GKE) với HPA
  * Authentication: Firebase Auth + OAuth2 (Google, Facebook)
  * Messaging: Redis cho session cache, Google Cloud Messaging (FCM) / Apple APNs cho push, Zalo API integration
  * CI/CD: GitHub Actions (build, test, image push, deploy)

- **Frontend & Cross-Platform UI Mobile Stack:**
  * Web: Next.js 14 với React 18, TypeScript, i18n (vi, en, es)
  * Mobile: Capacitor hybrid app (Android/iOS) sử dụng cùng codebase React
  * State Management: Redux Toolkit với đồng bộ ngoại tuyến qua IndexedDB
  * Push Notification: Plugin Capacitor Push Notifications tích hợp với FCM/APNs
  * Localization: i18next, hreflang động cho SEO đa ngôn ngữ

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** Workspace gốc là dự án `.`. Tất cả đường dẫn phải bắt đầu với `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Áp dụng quy tắc tiền tố thư mục động theo Protocol 1 (backend, frontend, infra).
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Tất cả mã nguồn Java phải nằm trong package `org.nlh4j.saas.membershiphub`. (Tên dự án được chuẩn hóa thành chuỗi thuần chữ thường, loại bỏ dấu gạch ngang và gạch dưới).
- **Strict Tester Target Path Syntax:** Bất kỳ thành phần nào được Tester nhắm đến phải được biểu diễn dưới dạng cặp đường dẫn phân cách bán phẩy `<source_component>;<test_suite_file>` với cả hai đều bắt đầu bằng `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 | ./sources/backend.user | Implement đăng ký người dùng, xác thực mạng xã hội, gán vai trò, và flow xác thực OAuth2 | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006] |
| Phase 1 | Day 1 | ./sources/docs/users_roles_schema.sql | Tài liệu schema bảng Users & Roles | Doc | [DAT-001] |
| Phase 1 | Day 1 | ./sources/tests/user_registration_validation.test.js | Kiểm tra xác thực đầu vào và xử lý ngoại lệ | Tester | [EXC-004] |
| Phase 1 | Day 1 | ./sources/docs/performance_security_logging_gdpr_review.md | Đánh giá hiệu năng, bảo mật, logging, tuân thủ GDPR | Reviewer | [NFR-001], [NFR-008] |
| Phase 2 | Day 1 | ./sources/backend.center | Implement danh sách trung tâm, CRUD, gán/chuyển quyền Center Admin | Coder | [REQ-004], [REQ-005], [REQ-006], [ARC-002] |
| Phase 2 | Day 1 | ./sources/docs/centers_schema.sql | Tài liệu schema bảng Centers | Doc | [DAT-003] |
| Phase 2 | Day 1 | ./sources/docs/security_scalability_docker_backup_review.md | Đánh giá bảo mật, khả năng mở rộng, docker image size, backup | Reviewer | [NFR-003] |
| Phase 2 | Day 1 | ./sources/infra.docker | Xây dựng Dockerfile với giới hạn kích thước <500 MB | Docker | [NFR-005] |
| Phase 2 | Day 1 | ./sources/infra.gcp | Cấu hình GCP backup & disaster recovery (point‑in‑time) | GCP | [NFR-009] |
| Phase 3 | Day 1 | ./sources/backend.course | Implement danh sách khóa học, CRUD khóa học, phân công giáo viên | Coder | [REQ-007], [REQ-008], [REQ-009], [ARC-009] |
| Phase 3 | Day 1 | ./sources/backend.enrollment | Implement duyệt khóa học, ghi danh học viên (tự động tạo học viên nếu thiếu) | Coder | [REQ-010], [REQ-011] |
| Phase 3 | Day 1 | ./sources/docs/courses_schema.sql | Tài liệu schema bảng Courses | Doc | [DAT-004] |
| Phase 3 | Day 1 | ./sources/docs/enrollments_schema.sql | Tài liệu schema bảng Enrollments | Doc | [DAT-005] |
| Phase 3 | Day 1 | ./sources/docs/logging_review.md | Đánh giá logging (NFR‑006) | Reviewer | [NFR-006] |
| Phase 4 | Day 1 | ./sources/backend.attendance | Implement quét QR điểm danh, đảm bảo bất biến, xử lý ngoại lệ network | Coder | [REQ-012], [REQ-013] |
| Phase 4 | Day 1 | ./sources/docs/attendance_schema.sql | Tài liệu schema bảng Attendance | Doc | [DAT-006] |
| Phase 4 | Day 1 | ./sources/tests/attendance_exceptions.test.js | Kiểm tra ngoại lệ network (EXC‑001) và duplicate scan (EXC‑002) | Tester | [EXC-001], [EXC-002] |
| Phase 4 | Day 1 | ./sources/backend.card | Implement hiển thị thẻ hội viên (ngày hiệu lực còn lại) và gia hạn thẻ | Coder | [REQ-014], [REQ-015] |
| Phase 4 | Day 1 | ./sources/docs/studentcards_schema.sql | Tài liệu schema bảng StudentCards | Doc | [DAT-007] |
| Phase 4 | Day 1 | ./sources/backend.notification | Implement trigger thông báo cho announcement, assignment, enrollment | Coder | [REQ-016] |
| Phase 4 | Day 1 | ./sources/docs/notifications_schema.sql | Tài liệu schema bảng Notifications | Doc | [DAT-008] |
| Phase 4 | Day 1 | ./sources/tests/notification_delivery_failure.test.js | Kiểm tra ngoại lệ gửi thông báo thất bại (EXC‑003) | Tester | [EXC-003] |
| Phase 4 | Day 1 | ./sources/backend.promotion | Implement quản lý khuyến mãi & thông báo (tạo/sửa/xóa) | Coder | [REQ-017], [REQ-018] |
| Phase 4 | Day 1 | ./sources/docs/promotions_announcements_schema.sql | Tài liệu schema bảng Promotions & Announcements | Doc | [DAT-009] |
| Phase 4 | Day 1 | ./sources/docs/availability_security_scalability_logging_backup_review.md | Đánh giá khả năng sẵn sàng, bảo mật, khả năng mở rộng, logging, backup | Reviewer | [NFR-002], [NFR-003], [NFR-004], [NFR-006], [NFR-009] |
| Phase 5 | Day 1 | ./sources/backend.chatbot | Tích hợp chatbot AI để trả lời truy vấn về khóa học, giáo viên, trung tâm, trạng thái tài khoản | Coder | [REQ-019] |
| Phase 5 | Day 1 | ./sources/backend.mobile | Tích hợp backend cho ứng dụng di động (Next.js consumption, bearer token auth, caching ngoại tuyến) | Coder | [ARC-007], [ARC-008], [ARC-009] |
| Phase 5 | Day 1 | ./sources/docs/i18n_seo_spec.md | Tài liệu spec phát hiện ngôn ngữ, hreflang, SEO đa ngôn ngữ | Doc | [REQ-022], [REQ-023] |
| Phase 5 | Day 1 | ./sources/docs/reports_dashboard_spec.md | Tài liệu spec báo cáo điểm danh (CSV) và bảng điều khiển tóm tắt ghi danh | Doc | [REQ-024], [REQ-025] |
| Phase 5 | Day 1 | ./sources/infra.gke | Xây dựng Kubernetes Deployment, Service, HPA cho các service | GKE | [ARC-010] |
| Phase 5 | Day 1 | ./sources/docs/scalability_review.md | Đánh giá khả năng mở rộng (NFR‑004) và đa ngôn ngữ (NFR‑007) | Reviewer | [NFR-004], [NFR-007] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

<!--START_DELIMITTER-->
### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng nền tảng định danh người dùng và xác thực, thiết lập kiểm soát truy cập dựa trên vai trò cho System Admin, Center Admin, Manager, Teacher, và Student. Xác nhận tuân thủ các yêu cầu về hiệu năng, bảo mật, logging, và GDPR.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend.user (Coder)
  * ./sources/docs/users_roles_schema.sql (Doc)
  * ./sources/tests/user_registration_validation.test.js (Tester)
  * ./sources/docs/performance_security_logging_gdpr_review.md (Reviewer)
- **Database Schema DDL SQL Specification [DAT-001]:**
```sql
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL REFERENCES ROLES(roleId),
    provider ENUM('local','firebase','google','facebook') NOT NULL DEFAULT 'local',
    createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
    updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006]:**
```json
{
  "endpoints": [
    {
      "path": "/api/auth/register",
      "method": "POST",
      "payload": {
        "email": "string",
        "password": "string",
        "fullName": "string",
        "roleId": "smallint"
      },
      "response": {"token":"string","userId":"uuid"}
    },
    {
      "path": "/api/auth/social/{provider}",
      "method": "POST",
      "payload": {"code":"string"},
      "response": {"token":"string","userId":"uuid"}
    },
    {
      "path": "/api/users/{userId}/role",
      "method": "PUT",
      "payload": {"roleId":"smallint"},
      "response": {"success":"boolean"}
    }
  ]
}
```
- **Phase Localized Exception Handlers [EXC-004], [NFR-001], [NFR-008]:**
  * Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc) → trả về 400 với danh sách chi tiết các trường lỗi.
  * Vi phạm hiệu năng (phản hồi >200 ms) → ghi log cảnh báo, kích hoạt cảnh báo giám sát.
  * Vi phạm GDPR (yêu cầu xóa dữ liệu) → xóa bản ghi người dùng, ghi log hành động, trả về xác nhận.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1:** Mục tiêu ngắn hạn: Triển khai toàn bộ module quản lý người dùng và xác thực.
  - **Sub-Agent Coder:**
    - **Target Component:** ./sources/backend.user
    - **Low-Level Technical Task Instruction:** Implement các endpoint đăng ký, xác thực mạng xã hội, và gán vai trò. Áp dụng JWT với thời hạn 15 phút, refresh token 7 ngày. Sử dụng bcrypt cho password hash. Tích hợp Firebase Auth, Google OAuth2, Facebook OAuth2. Đảm bảo các quy tắc RBAC cho System Admin, Center Admin, Manager, Teacher, Student theo [ARC-001]‑[ARC-005].
    - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006]
  - **Sub-Agent Doc:**
    - **Target Component:** ./sources/docs/users_roles_schema.sql
    - **Low-Level Technical Task Instruction:** Soạn thảo DDL SQL cho bảng Users và Roles, bao gồm khóa chính, khóa ngoại, ràng buộc duy nhất, và trigger cập nhật updatedAt. Ghi chú các chỉ mục cho email và roleId.
    - **Targeted Tag IDs:** [DAT-001]
  - **Sub-Agent Tester:**
    - **Target Component:** ./sources/tests/user_registration_validation.test.js
    - **Low-Level Technical Task Instruction:** Soạn các trường hợp kiểm tra cho xác thực đầu vào (email định dạng, mật khẩu mạnh, trường bắt buộc). Kiểm tra các lỗi xác thực đầu vào theo [EXC-004] và xác nhận response error chứa danh sách các trường không hợp lệ.
    - **Targeted Tag IDs:** [EXC-004]
  - **Sub-Agent Reviewer:**
    - **Target Component:** ./sources/docs/performance_security_logging_gdpr_review.md
    - **Low-Level Technical Task Instruction:** Đánh giá hiệu năng endpoint (mục tiêu <200 ms), kiểm tra bảo mật (OWASP Top 10), xác nhận logging đầy đủ cho các hành động người dùng, và xác nhận tuân thủ GDPR (xóa dữ liệu theo yêu cầu).
    - **Targeted Tag IDs:** [NFR-001], [NFR-008]
<!--END_DELIMITTER-->

### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng module quản lý trung tâm, cho phép System Admin xem, tạo/sửa/xóa trung tâm, và phân quyền Center Admin. Đảm bảo tuân thủ bảo mật, khả năng mở rộng, docker image size, và backup.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend.center (Coder)
  * ./sources/docs/centers_schema.sql (Doc)
  * ./sources/docs/security_scalability_docker_backup_review.md (Reviewer)
  * ./sources/infra.docker (Docker)
  * ./sources/infra.gcp (GCP)
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(20) NOT NULL UNIQUE,
    contactPhone VARCHAR(30),
    contactEmail VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [ARC-002]:**
```json
{
  "endpoints": [
    {
      "path": "/api/centers",
      "method": "GET",
      "response": [{"centerId":"uuid","name":"string","address":"string","taxId":"string","contactPhone":"string","contactEmail":"string"}]
    },
    {
      "path": "/api/centers",
      "method": "POST",
      "payload": {"name":"string","address":"string","taxId":"string","contactPhone":"string","contactEmail":"string"},
      "response": {"centerId":"uuid","status":"created"}
    },
    {
      "path": "/api/centers/{centerId}",
      "method": "PUT",
      "payload": {"name":"string","address":"string","taxId":"string","contactPhone":"string","contactEmail":"string"},
      "response": {"success":"boolean"}
    },
    {
      "path": "/api/centers/{centerId}",
      "method": "DELETE",
      "response": {"success":"boolean"}
    },
    {
      "path": "/api/centers/{centerId}/assign/{userId}",
      "method": "POST",
      "response": {"success":"boolean"}
    }
  ]
}
```
- **Phase Localized Exception Handlers [NFR-003], [NFR-004], [NFR-005], [NFR-009]:**
  * Xung đột taxId → trả về 409 Conflict.
  * Kiểm tra hiệu năng endpoint <200 ms, kích hoạt cảnh báo nếu vượt quá.
  * Đảm bảo docker image size <500 MB, kiểm tra trong CI.
  * Lên lịch backup PostgreSQL hàng ngày, phục hồi điểm‑in‑thời gian trong vòng 24 giờ.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 1:** Mục tiêu ngắn hạn: Hoàn thành module quản lý trung tâm và cấu hình hạ tầng.
  - **Sub-Agent Coder:**
    - **Target Component:** ./sources/backend.center
    - **Low-Level Technical Task Instruction:** Implement REST API cho các hoạt động CRUD trung tâm và gán Center Admin. Áp dụng xác thực JWT, RBAC cho System Admin. Đảm bảo taxId duy nhất, xử lý lỗi xung đột.
    - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [ARC-002]
  - **Sub-Agent Doc:**
    - **Target Component:** ./sources/docs/centers_schema.sql
    - **Low-Level Technical Task Instruction:** Soạn DDL cho bảng Centers, bao gồm các ràng buộc duy nhất cho taxId, chỉ mục tìm kiếm nhanh.
    - **Targeted Tag IDs:** [DAT-003]
  - **Sub-Agent Reviewer:**
    - **Target Component:** ./sources/docs/security_scalability_docker_backup_review.md
    - **Low-Level Technical Task Instruction:** Đánh giá bảo mật (OWASP), khả năng mở rộng (HPA), docker image size, và quy trình backup. Xác nhận tuân thủ [NFR-003], [NFR-004], [NFR-005], [NFR-009].
    - **Targeted Tag IDs:** [NFR-003], [NFR-004], [NFR-005], [NFR-009]
  - **Sub-Agent Docker:**
    - **Target Component:** ./sources/infra.docker
    - **Low-Level Technical Task Instruction:** Xây dựng multi‑stage Dockerfile cho backend service, tối ưu hóa kích thước image (<500 MB), tích hợp vào GitHub Actions.
    - **Targeted Tag IDs:** [NFR-005]
  - **Sub-Agent GCP:**
    - **Target Component:** ./sources/infra.gcp
    - **Low-Level Technical Task Instruction:** Cấu hình Google Cloud VPC, Secret Manager cho credential, Backup & DR policy cho PostgreSQL (backup hàng ngày, phục hồi điểm‑in‑thời gian 24 giờ).
    - **Targeted Tag IDs:** [NFR-009]

### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng module quản lý khóa học và ghi danh học viên, bao gồm phân công giáo viên, duyệt khóa học, và tự động tạo học viên. Đảm bảo logging và hiệu năng.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend.course (Coder)
  * ./sources/backend.enrollment (Coder)
  * ./sources/docs/courses_schema.sql (Doc)
  * ./sources/docs/enrollments_schema.sql (Doc)
  * ./sources/docs/logging_review.md (Reviewer)
- **Database Schema DDL SQL Specification [DAT-004], [DAT-005]:**
```sql
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL REFERENCES USERS(userId),
    maxStudents INT NOT NULL DEFAULT 30
);

CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW()
);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [ARC-009]:**
```json
{
  "endpoints": [
    {
      "path": "/api/courses",
      "method": "GET",
      "response": [{"courseId":"uuid","title":"string","startDate":"date","endDate":"date","teacherName":"string"}]
    },
    {
      "path": "/api/courses",
      "method": "POST",
      "payload": {"title":"string","description":"string","startDate":"date","endDate":"date","teacherId":"uuid","maxStudents":"int"},
      "response": {"courseId":"uuid","status":"created"}
    },
    {
      "path": "/api/courses/{courseId}",
      "method": "PUT",
      "payload": {"title":"string","description":"string","startDate":"date","endDate":"date","teacherId":"uuid"},
      "response": {"success":"boolean"}
    },
    {
      "path": "/api/courses/{courseId}",
      "method": "DELETE",
      "response": {"success":"boolean"}
    },
    {
      "path": "/api/courses/{courseId}/assign/{teacherId}",
      "method": "POST",
      "response": {"success":"boolean"}
    },
    {
      "path": "/api/enrollments",
      "method": "POST",
      "payload": {"studentId":"uuid","courseId":"uuid"},
      "response": {"enrollmentId":"uuid","status":"enrolled"}
    },
    {
      "path": "/api/courses/{courseId}/students",
      "method": "GET",
      "response": [{"studentId":"uuid","fullName":"string"}]
    }
  ]
}
```
- **Phase Localized Exception Handlers [NFR-006]:**
  * Ghi log tất cả các thao tác CRUD (tạo, cập nhật, xóa) với userId, timestamp, và chi tiết hành động. Giữ log trong 1 năm.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 1:** Mục tiêu ngắn hạn: Hoàn thành module quản lý khóa học và ghi danh.
  - **Sub-Agent Coder:**
    - **Target Component:** ./sources/backend.course
    - **Low-Level Technical Task Instruction:** Implement các endpoint CRUD khóa học, phân công giáo viên, và kiểm tra xung đột lịch (startDate/endDate overlap cho cùng giáo viên). Áp dụng xác thực JWT, RBAC cho System Admin và Center Admin.
    - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [ARC-009]
  - **Sub-Agent Coder:**
    - **Target Component:** ./sources/backend.enrollment
    - **Low-Level Technical Task Instruction:** Implement duyệt khóa học, ghi danh học viên, tự động tạo tài khoản học viên nếu thiếu. Gửi notification đẩy và ghi vào nhóm Zalo tương ứng.
    - **Targeted Tag IDs:** [REQ-010], [REQ-011]
  - **Sub-Agent Doc:**
    - **Target Component:** ./sources/docs/courses_schema.sql
    - **Low-Level Technical Task Instruction:** Soạn DDL cho bảng Courses, bao gồm các ràng buộc kiểm tra startDate <= endDate, chỉ mục cho teacherId.
    - **Targeted Tag IDs:** [DAT-004]
  - **Sub-Agent Doc:**
    - **Target Component:** ./sources/docs/enrollments_schema.sql
    - **Low-Level Technical Task Instruction:** Soạn DDL cho bảng Enrollments, bao gồm các ràng buộc khóa ngoại, chỉ mục cho studentId và courseId.
    - **Targeted Tag IDs:** [DAT-005]
  - **Sub-Agent Reviewer:**
    - **Target Component:** ./sources/docs/logging_review.md
    - **Low-Level Technical Task Instruction:** Đánh giá logging (NFR‑006), đảm bảo ghi log đầy đủ cho các thao tác người dùng, khóa học, ghi danh. Kiểm tra độ trễ ghi log (<200 ms).
    - **Targeted Tag IDs:** [NFR-006]

### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng module điểm danh (quét QR), quản lý thẻ hội viên, trigger thông báo, và quản lý khuyến mãi & thông báo. Đảm bảo xử lý ngoại lệ network, duplicate scan, và delivery failure.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend.attendance (Coder)
  * ./sources/docs/attendance_schema.sql (Doc)
  * ./sources/tests/attendance_exceptions.test.js (Tester)
  * ./sources/backend.card (Coder)
  * ./sources/docs/studentcards_schema.sql (Doc)
  * ./sources/backend.notification (Coder)
  * ./sources/docs/notifications_schema.sql (Doc)
  * ./sources/tests/notification_delivery_failure.test.js (Tester)
  * ./sources/backend.promotion (Coder)
  * ./sources/docs/promotions_announcements_schema.sql (Doc)
  * ./sources/docs/availability_security_scalability_logging_backup_review.md (Reviewer)
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007], [DAT-008], [DAT-009]:**
```sql
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);

CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);

CREATE TABLE ANNOUNCEMENTS (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);
```
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018]:**
```json
{
  "endpoints": [
    {
      "path": "/api/attendance/scan",
      "method": "POST",
      "payload": {"studentId":"uuid","courseId":"uuid","qrCodeData":"string"},
      "response": {"attendanceId":"uuid","duplicate":"boolean"}
    },
    {
      "path": "/api/cards/{studentId}",
      "method": "GET",
      "response": {"cardId":"uuid","validityDays":"int","remainingDays":"int"}
    },
    {
      "path": "/api/cards/{studentId}/renew",
      "method": "POST",
      "payload": {"additionalDays":"int"},
      "response": {"newEndDate":"date","confirmation":"string"}
    },
    {
      "path": "/api/notifications",
      "method": "POST",
      "payload": {"userId":"uuid","groupZalo":"string","message":"string"},
      "response": {"notificationId":"uuid","queued":"boolean"}
    },
    {
      "path": "/api/promotions",
      "method": "POST",
      "payload": {"code":"string","discountPercent":"int","startDate":"date","endDate":"date","description":"string"},
      "response": {"promoId":"uuid","status":"created"}
    },
    {
      "path": "/api/announcements",
      "method": "POST",
      "payload": {"title":"string","content":"string","startDate":"date","endDate":"date"},
      "response": {"announcementId":"uuid","status":"created"}
    }
  ]
}
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003]:**
  * Network thất bại trong khi quét QR → app lưu scan cục bộ, retry khi có kết nối, sau đó ghi điểm danh một lần.
  * Duplicate scan trong cùng ngày → trả về success với cờ duplicate, không tạo row mới.
  * Gửi push notification thất bại (device token không hợp lệ) → ghi log lỗi, lên lịch retry tối đa 3 lần, sau đó đánh dấu delivered=false.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 1:** Mục tiêu ngắn hạn: Hoàn thành module điểm danh và xử lý ngoại lệ.
  - **Sub-Agent Coder:**
    - **Target Component:** ./sources/backend.attendance
    - **Low-Level Technical Task Instruction:** Implement endpoint `/api/attendance/scan`. Xác thực studentId‑courseId relationship, ghi row vào bảng ATTENDANCE với timestamp. Sử dụng khóa duy nhất (studentId, courseId, attendanceDate) để đảm bảo bất biến. Xử lý duplicate scan trả về cờ duplicate.
    - **Targeted Tag IDs:** [REQ-012], [REQ-013]
  - **Sub-Agent Doc:**
    - **Target Component:** ./sources/docs/attendance_schema.sql
    - **Low-Level Technical Task Instruction:** Soạn DDL cho bảng ATTENDANCE, bao gồm các ràng buộc khóa ngoại, chỉ mục cho studentId, courseId, attendanceDate.
    - **Targeted Tag IDs:** [DAT-006]
  - **Sub-Agent Tester:**
    - **Target Component:** ./sources/tests/attendance_exceptions.test.js
    - **Low-Level Technical Task Instruction:** Soạn các trường hợp kiểm tra cho network thất bại (EXC‑001) và duplicate scan (EXC‑002). Mô phỏng mất kết nối, retry logic, và xác nhận chỉ một row được tạo.
    - **Targeted Tag IDs:** [EXC-001], [EXC-002]
  - **Sub-Agent Coder:**
    - **Target Component:** ./sources/backend.card
    - **Low-Level Technical Task Instruction:** Implement endpoint `/api/cards/{studentId}` để hiển thị thông tin thẻ (validityDays, remainingDays). Implement `/api/cards/{studentId}/renew` để gia hạn thẻ dựa trên additionalDays, cập nhật bảng STUDENTCARDS.
    - **Targeted Tag IDs:** [REQ-014], [REQ-015]
  - **Sub-Agent Doc:**
    - **Target Component:** ./sources/docs/studentcards_schema.sql
    - **Low-Level Technical Task Instruction:** Soạn DDL cho bảng STUDENTCARDS, bao gồm trigger tính remainingDays dựa trên issue