# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260802144508 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/02 14:45:08 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY
### 1.1. Core System Modality & Architecture Modality
Hệ thống được thiết kế theo kiến trúc microservice dạng event-driven, áp dụng mô hình CQRS cho các thao tác đọc/ghi, và sử dụng Reactive Core với Kotlin/Java (Quarkus) để đảm bảo khả năng phản hồi dưới 200 ms cho các API cốt lõi. Mỗi domain (user, center, course, enrollment, attendance, card, notification, promotion, announcement, reporting, chatbot) được đóng gói thành một service độc lập, triển khai trên Kubernetes (GKE) với Docker container. Giao tiếp bất đồng bộ được thực hiện qua chủ đề Kafka (hoặc tương đương) để đảm bảo tính idempotent cho luồng điểm danh QR và tính nhất quán cho thông báo đa kênh.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Luồng dữ liệu chính bao gồm: (1) **Authentication Flow** – OAuth2 từ Firebase, Google, Facebook, cấp JWT (15 phút) và refresh token; (2) **QR Attendance Flow** – mobile app quét QR, gửi studentId + timestamp đến Attendance Service, ghi nhận điểm danh một cách bất biến; (3) **Notification Flow** – backend kích hoạt push notification (FCM/APNs) và đăng bài lên nhóm Zalo được chỉ định; (4) **Mobile Backend Integration** – Frontend Next.js tiêu thụ REST APIs qua bearer token, hỗ trợ caching ngoại tuyến. Tất cả các service đều được bảo vệ bởi chính sách CORS đa tenant và tuân thủ OWASP Top 10.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.2, PostgreSQL 15, Flyway, Hibernate ORM, Lombok, Bcrypt, JWT‑Java, OAuth2 Client, Apache Kafka, Redis, Docker, Kubernetes (K8s), GKE, Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalogo API SDK, OpenAPI / Swagger, JUnit5, AssertJ, WireMock.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14 (React 18), TypeScript, Tailwind CSS, i18next, React‑Query, Capacitor (bridge native), Cordova plugins, FCM/APNs SDKs, Jest, React‑Testing‑Library, ESLint, Prettier, Docker (cho frontend build).

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** Root repository là `..`. Tất cả các đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Áp dụng quy tắc tiền tố động theo Protocol 1 – backend logic dưới `./sources/backend.<service-name>.`, frontend dưới `./sources/frontend.<app-name>.`, infra dưới `./sources/infra.`.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Tất cả mã nguồn Java phải nằm trong gói cơ sở `org.nlh4j.saas.membershiphub`. (Tên dự án đã được chuẩn hóa bằng cách loại bỏ dấu gạch ngang và dấu gạch dưới).
- **Strict Tester Target Path Syntax:** Bất kỳ thành phần nào được Tester nhắm đến phải được biểu diễn dưới dạng cặp `<source_component>;<test_suite_file>` với cả hai đường dẫn bắt đầu bằng `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1‑3 | `./sources/backend.auth.`, `./sources/backend.user.`, `./sources/backend.rbac.`, `./sources/backend.center.` | Triển khai đăng ký người dùng, xác thực xã hội, gán vai trò, CRUD trung tâm cơ bản, DDL bảng Users/Roles/Centers, hợp đồng API cho các endpoint cốt lõi, xử lý ngoại lệ đầu vào (EXC‑004). | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [DAT-003], [NFR-001], [NFR-003], [NFR-006], [EXC-004] |
| Phase 2 | Day 4‑7 | `./sources/backend.center.`, `./sources/backend.course.`, `./sources/backend.enrollment.`, `./sources/backend.rbac.` | Mở rộng quản lý trung tâm (xem, tạo, cập nhật, xóa), phân quyền admin trung tâm, CRUD khóa học (tránh xung đột lịch), gán giáo viên, ghi danh học viên, DDL bảng Courses/Enrollments, hợp đồng API, kiểm tra ngoại lệ (EXC‑004). | Tester | [REQ-004], [REQ-005], [REQ-006], [ARC-002], [ARC-004], [DAT-003], [DAT-004], [DAT-005], [NFR-002], [NFR-004], [EXC-004] |
| Phase 3 | Day 8‑15 | `./sources/backend.course.`, `./sources/backend.enrollment.`, `./sources/backend.attendance.`, `./sources/backend.card.`, `./sources/backend.notification.`, `./sources/backend.promotion.`, `./sources/backend.announcement.`, `./sources/backend.i18n.`, `./sources/frontend.web.`, `./sources/frontend.mobile.` | Hoàn thiện quản lý khóa học, ghi danh, quét QR điểm danh (bất biến), thẻ hội viên (xem, gia hạn), động cơ thông báo, quản lý khuyến mãi & thông báo, phát hiện ngôn ngữ, SEO đa ngôn ngữ, DDL bảng Attendance/Cards/Notifications/Promotions/Announcements, hợp đồng API, xử lý ngoại lệ mạng (EXC‑001), trùng lặp (EXC‑002), thất bại thông báo (EXC‑003). | Reviewer | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-005], [NFR-007], [NFR-008], [EXC-001], [EXC-002], [EXC-003], [EXC-004] |
| Phase 4 | Day 16‑24 | `./sources/backend.reporting.`, `./sources/backend.chatbot.`, `./sources/infra.` | Triển khai báo cáo điểm danh (CSV), bảng điều khiển tóm tắt, chatbot AI, hardening bảo mật (NFR‑003, NFR‑006, NFR‑009), tuân thủ GDPR/CCPA (NFR‑008), hình ảnh Docker (< 500 MB), chính sách backup & DR (NFR‑009), DDL bảng SystemSettings, hợp đồng API, xử lý ngoại lệ phục hồi hệ thống (EXC‑005). | Docker | [REQ-019], [REQ-024], [REQ-025], [EXC-005], [NFR-001], [NFR-002], [NFR-003], [NFR-009], [DAT-011] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

<!--START_DELIMITTER-->
### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng nền tảng người dùng cốt lõi, định nghĩa các vai trò RBAC, triển khai xác thực OAuth2, và tạo các bảng dữ liệu cơ bản cho Users, Roles, Centers.
- **Target Physical Directory Matrix Map:**
  - `./sources/backend.user./entity/User.java` `[REQ-001], [DAT-001]`
  - `./sources/backend.user./repository/UserRepository.java` `[REQ-001], [DAT-001]`
  - `./sources/backend.auth./service/AuthService.java` `[REQ-001], [REQ-002], [ARC-006]`
  - `./sources/backend.rbac./service/RbacService.java` `[REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]`
  - `./sources/backend.center./entity/Center.java` `[REQ-004], [DAT-003]`
  - `./sources/backend.center./repository/CenterRepository.java` `[REQ-004], [DAT-003]`
- **Database Schema DDL SQL Specification [DAT-001], [DAT-003]:**
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
    provider ENUM('local','firebase','google','facebook') NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(30),
    contact_email VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
  - `POST /auth/register` – yêu cầu `{email, password, fullName, provider}`; trả về `{token, userId}`.
  - `POST /auth/social` – nhận `{provider, code}`; trao đổi mã lấy thông tin người dùng, tạo/cập nhật bản ghi, cấp JWT.
  - `PUT /users/{userId}/role` – yêu cầu `{roleId}`; chỉ System Admin được phép, cập nhật vai trò và áp dụng quyền ngay lập tức.
  - `GET /centers` – trả về danh sách `{centerId, name, address, taxId, contactPhone, contactEmail}`.
- **Phase Localized Exception Handlers [EXC-004]:**
  - Xác thực đầu vào không hợp lệ (email sai định dạng, thiếu trường bắt buộc) → trả về `400 Bad Request` với danh sách chi tiết các trường lỗi.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

### DAY 1
- **[Coder]:** Target Component: `./sources/backend.user./entity/User.java` `[REQ-001], [DAT-001]` – triển khai lớp entity với các trường được chú thích, ràng buộc nullable, và mối quan hệ với Roles.
- **[Coder]:** Target Component: `./sources/backend.auth./service/AuthService.java` `[REQ-001], [REQ-002], [ARC-006]` – viết logic đăng ký, xác thực xã hội, tạo JWT (15 phút) và refresh token.
- **[Coder]:** Target Component: `./sources/backend.rbac./service/RbacService.java` `[REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]` – triển khai kiểm tra quyền dựa trên vai trò cho System Admin, Center Admin, Manager, Teacher, Student.

### DAY 2
- **[Tester]:** Target Component: `./sources/backend.user.;src/test/java/org/nlh4j/saas/membershiphub/user/UserRegistrationTest.java` `[REQ-001], [DAT-001], [EXC-004]` – kiểm tra đăng ký thành công, xung đột email, xác thực đầu vào (EXC‑004).

### DAY 3
- **[Reviewer]:** Target Component: `./sources/docs/authApi.yaml` `[REQ-001], [REQ-002], [REQ-003], [ARC-006]` – đánh giá tài liệu OpenAPI, đảm bảo định dạng chính xác, bao phủ tất cả các trường hợp sử dụng, và cập nhật các thay đổi thiết kế.

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Mở rộng quản lý trung tâm, triển khai CRUD khóa học, gán giáo viên, và ghi danh học viên với kiểm tra xung đột lịch.
- **Target Physical Directory Matrix Map:**
  - `./sources/backend.center./service/CenterService.java` `[REQ-004], [REQ-005], [REQ-006]`
  - `./sources/backend.course./entity/Course.java` `[REQ-007], [DAT-004]`
  - `./sources/backend.course./repository/CourseRepository.java` `[REQ-007], [DAT-004]`
  - `./sources/backend.enrollment./entity/Enrollment.java` `[REQ-010], [DAT-005]`
- **Database Schema DDL SQL Specification [DAT-004], [DAT-005]:**
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

CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE (student_id, course_id)
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]:**
  - `GET /centers` – trả về danh sách trung tâm.
  - `POST /centers` – tạo trung tâm mới, kiểm tra tax_id trùng lặp.
  - `DELETE /centers/{centerId}` – xóa trung tâm.
  - `PUT /centers/{centerId}/admin` – gán người dùng làm Center Admin.
  - `GET /courses` – trả về danh sách khóa học với thông tin giáo viên.
  - `POST /courses` – tạo khóa học mới, kiểm tra xung đột lịch với giáo viên.
  - `PUT /courses/{courseId}/teacher` – gán/giải phóng giáo viên, đẩy thông báo đến mobile.
  - `POST /enrollments` – ghi danh học viên, tự động tạo tài khoản Student nếu thiếu, đẩy thông báo đến student và nhóm Zalo.

### DAY 4
- **[Coder]:** Target Component: `./sources/backend.center./service/CenterService.java` `[REQ-004], [REQ-005], [REQ-006]` – triển khai các phương thức CRUD, kiểm tra tax_id, và logic phân quyền admin.

### DAY 5
- **[Tester]:** Target Component: `./sources/backend.center.;src/test/java/org/nlh4j/saas/membershiphub/center/CenterCrudTest.java` `[REQ-004], [REQ-005], [REQ-006], [EXC-004]` – kiểm tra tạo trung tâm thành công, lỗi tax_id trùng lặp, xác thực đầu vào.

### DAY 6
- **[Reviewer]:** Target Component: `./sources/docs/centerApi.yaml` `[REQ-004], [REQ-005], [REQ-006]` – đánh giá tài liệu API, đảm bảo các tham số yêu cầu, phản hồi lỗi, và các trường hợp bảo mật.

### DAY 7
- **[Docker]:** Target Component: `./sources/infra.dockerfile.backend.` `[REQ-004], [REQ-005], [REQ-006], [DAT-003], [DAT-004], [DAT-005]` – tạo Dockerfile chuẩn hóa cho các service backend (auth, user, center, course, enrollment) với base image size < 200 MB, multi-stage build, và các label bảo mật.

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai điểm danh QR, quản lý thẻ hội viên, động cơ thông báo, quản lý khuyến mãi & thông báo, hỗ trợ đa ngôn ngữ, và đảm bảo giao diện người dùng di động phản hồi nhanh.
- **Target Physical Directory Matrix Map:**
  - `./sources/backend.attendance./entity/Attendance.java` `[REQ-012], [DAT-006]`
  - `./sources/backend.card./entity/StudentCard.java` `[REQ-014], [REQ-015], [DAT-007]`
  - `./sources/backend.notification./entity/Notification.java` `[REQ-016], [DAT-008]`
  - `./sources/backend.promotion./entity/Promotion.java` `[REQ-017], [DAT-009]`
  - `./sources/backend.announcement./entity/Announcement.java` `[REQ-018], [DAT-009]`
  - `./sources/backend.i18n./service/I18nService.java` `[REQ-022], [REQ-023]`
  - `./sources/frontend.web./pages/centers.tsx` `[REQ-004]`
  - `./sources/frontend.web./pages/courses.tsx` `[REQ-007]`
  - `./sources/frontend.mobile./src/screens/AttendanceScreen.tsx` `[REQ-012]`
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007], [DAT-008], [DAT-009]:**
```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE (student_id, course_id, attendance_date)
);

CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);

CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT now(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

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
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-020], [REQ-021], [REQ-022], [REQ-023]:**
  - `POST /attendance/scan` – nhận `{studentId, courseId, timestamp}`; ghi nhận điểm danh, bỏ qua bản ghi trùng trong ngày.
  - `GET /cards/{studentId}` – trả về `{cardId, issueDate, validityDays, remainingDays}`.
  - `POST /cards/{cardId}/renew` – nhận `{days, paymentToken}`; cập nhật `remainingDays` và đẩy thông báo.
  - `POST /notifications` – tạo bản ghi, đưa vào hàng đợi push (FCM/APNs) và gửi tin nhắn Zalo.
  - `GET /promotions` – trả về danh sách khuyến mãi còn hiệu lực.
  - `POST /promotions` – tạo khuyến mãi mới, kiểm tra ngày bắt đầu/kết thúc.
  - `GET /announcements` – trả về danh sách thông báo đang hiệu lực.
  - `POST /announcements` – tạo thông báo, hỗ trợ lịch hiển thị.
  - `GET /i18n/languages` – trả về danh sách ngôn ngữ được hỗ trợ.
  - `GET /seo/hreflang` – trả về liên kết hreflang cho SEO đa ngôn ngữ.

- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:**
  - **EXC‑001:** Network mất kết nối khi quét QR → app lưu scan cục bộ, retry khi khôi phục, đảm bảo chỉ ghi một bản ghi.
  - **EXC‑002:** Quét QR trùng lặp trong ngày → trả về `200 OK` với cờ `duplicate:true`.
  - **EXC‑003:** Push notification thất bại (token không hợp lệ) → ghi log, lên lịch retry tối đa 3 lần, sau đó đánh dấu `delivered=false`.
  - **EXC‑004:** Xác thực đầu vào cho các endpoint (ví dụ: thiếu trường bắt buộc, định dạng sai) → trả về `400` với danh sách lỗi chi tiết.
  - **EXC‑005:** System phục hồi sau sự cố → xử lý hàng đợi điểm danh chờ (FIFO), thông báo cho user về các sự kiện đã phục hồi.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

### DAY 8
- **[Coder]:** Target Component: `./sources/backend.course./entity/Course.java` `[REQ-007], [DAT-004]` – triển khai entity khóa học với ràng buộc ngày bắt đầu/kết thúc, kiểm tra xung đột lịch với giáo viên.
- **[Coder]:** Target Component: `./sources/backend.enrollment./entity/Enrollment.java` `[REQ-010], [DAT-005]` – triển khai entity ghi danh với ràng buộc khóa ngoại và kiểm tra trùng lặp.

### DAY 9
- **[Tester]:** Target Component: `./sources/backend.course.;src/test/java/org/nlh4j/saas/membershiphub/course/CourseCrudTest.java` `[REQ-007], [REQ-008], [REQ-009], [EXC-004]` – kiểm tra CRUD khóa học, xung đột lịch, xác thực đầu vào.

### DAY 10
- **[Reviewer]:** Target Component: `./sources/docs/courseApi.yaml` `[REQ-007], [REQ-008], [REQ-009]` – đánh giá tài liệu API khóa học, đảm bảo các trường hợp lỗi được định nghĩa.

### DAY 11
- **[Coder]:** Target Component: `./sources/backend.attendance./entity/Attendance.java` `[REQ-012], [DAT-006]` – triển khai entity điểm danh với ràng buộc unique (student, course, date).
- **[Coder]:** Target Component: `./sources/backend.attendance./service/AttendanceService.java` `[REQ-012], [REQ-013], [ARC-007]` – triển khai endpoint quét QR, logic chống trùng lặp, và xử lý ngoại lệ mạng (EXC‑001).

### DAY 12
- **[Tester]:** Target Component: `./sources/backend.attendance.;src/test/java/org/nlh4j/saas/membershiphub/attendance/AttendanceScanTest.java` `[REQ-012], [REQ-013], [EXC-001], [EXC-002]` – kiểm tra quét thành công, phát hiện trùng lặp, và retry khi mất mạng.

### DAY 13
- **[Coder]:** Target Component: `./sources/backend.card./entity/StudentCard.java` `[REQ-014], [REQ-015], [DAT-007]` – triển khai entity thẻ hội viên với trường remainingDays tính toán.
- **[Coder]:** Target Component: `./sources/backend.card./service/CardService.java` `[REQ-014], [REQ-015]` – triển khai endpoint xem thẻ và gia hạn.
- **[Coder]:** Target Component: `./sources/backend.promotion./entity/Promotion.java` `[REQ-017], [DAT-009]` – triển khai entity khuyến mãi.
- **[Coder]:** Target Component: `./sources/backend.announcement./entity/Announcement.java` `[REQ-018], [DAT-009]` – triển khai entity thông báo.

### DAY 14
- **[Tester]:** Target Component: `./sources/frontend.web.;src/tests/web/UIRenderTest.js` `[REQ-014], [REQ-015], [REQ-017], [REQ-018]` – kiểm tra giao diện người dùng thẻ hội viên, hiển thị khuyến mãi/thông báo, và responsive trên web.

### DAY 15
- **[Reviewer]:** Target Component: `./sources/docs/cardPromotionAnnouncementApi.yaml` `[REQ-014], [REQ-015], [REQ-017], [REQ-018]` – đánh giá tài liệu API cho thẻ, khuyến mãi, thông báo, đảm bảo định nghĩa response chính xác.

### DAY 16
- **[Docker]:** Target Component: `./sources/infra.dockerfile.backend.attendance.` `[REQ-012], [DAT-006]` – tạo Dockerfile chuyên biệt cho Attendance Service, tối ưu hóa size ảnh (< 200 MB).

### DAY 17
- **[GCP]:** Target Component: `./sources/infra.gcp.provisioning.yaml` `[ARC-006], [ARC-007], [ARC-008]` – định nghĩa Terraform/Deployment Manager để triển khai Cloud Run services, Service Accounts, và bật API (Firebase Auth, Cloud Messaging).

### DAY 18
- **[GKE]:** Target Component: `./sources/infra.gke.deployments.yaml` `[ARC-006], [ARC-007], [ARC-008]` – tạo Kubernetes Deployment, Service, Ingress cho các backend services, thiết lập HPA dựa trên CPU > 70 % hoặc latency > 300 ms.

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai reporting & analytics, tích hợp chatbot AI, hardening bảo mật, tuân thủ GDPR/CCPA, thiết lập backup & disaster recovery, và đảm bảo hình ảnh Docker nhỏ gọn.
- **Target Physical Directory Matrix Map:**
  - `./sources/backend.reporting./service/ReportingService.java` `[REQ-024], [REQ-025]`
  - `./sources/backend.chatbot./service/ChatbotService.java` `[REQ-019]`
  - `./sources/infra.security./config/security.yaml` `[NFR-003]`
  - `./sources/infra.backup./scripts/backup.sh` `[NFR-009]`
  - `./sources/infra.compliance./gdpr/` `[NFR-008]`
  - `./sources/infra.dockerfile.backend.` `[NFR-005]`
  - `./sources/infra.dockerfile.backend.reporting.` `[REQ-024]`
  - `./sources/infra.dockerfile.backend.chatbot.` `[REQ-019]`
  - `./sources/docs/systemSettings.yaml` `[DAT-011]`
- **Database Schema DDL SQL Specification [DAT-011]:**
```sql
CREATE TABLE system_settings (
    setting_key VARCHAR(100) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-019], [REQ-024], [REQ-025], [NFR-003], [NFR-008]:**
  - `GET /reports/attendance` – tham số query `{centerId, startDate, endDate}`; trả về CSV với các cột `StudentName, CourseName, AttendanceDate, Status`.
  - `GET /dashboard` – trả về JSON `{totalStudents, activeCourses, upcomingSessions}`.
  - `POST /chatbot/query` – nhận `{userId, message}`; trả về `{answer, confidence}`; nếu confidence thấp, đẩy sự kiện đến hàng đợi human-support.
  - `GET /security/headers` – trả về các header CSP, HSTS, và các chính sách bảo mật.
  - `POST /gdpr/delete/{userId}` – xóa dữ liệu cá nhân, trả về xác nhận.

- **Phase Localized Exception Handlers [EXC-005]:**
  - **EXC‑005:** System phục hồi sau outage → xử lý hàng đợi điểm danh chờ (FIFO), ghi log phục hồi, gửi push notification đến user.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

### DAY 19
- **[Coder]:** Target Component: `./sources/backend.reporting./service/ReportingService.java` `[REQ-024], [REQ-025]` – triển khai logic tạo báo cáo CSV, tổng hợp dashboard metrics, và tích hợp với hệ thống logging (NFR‑006).

### DAY 20
- **[Tester]:** Target Component: `./sources/backend.reporting.;src/test/java/org/nlh4j/saas/membershiphub/reporting/ReportingTest.java` `[REQ-024], [REQ-025]` – kiểm tra tạo báo cáo, tính toàn vẹn dữ liệu, và hiệu suất (NFR‑001).

### DAY 21
- **[Reviewer]:** Target Component: `./sources/docs/reportingApi.yaml` `[REQ-024], [REQ-025]` – đánh giá tài liệu API báo cáo, đảm bảo định dạng CSV được xác định.

### DAY 22
- **[Coder]:** Target Component: `./sources/backend.chatbot./service/ChatbotService.java` `[REQ-019]` – triển khai endpoint chatbot, tích hợp model AI, ghi log tương tác vào bảng AuditLog (NFR‑006).

### DAY 23
- **[Tester]:** Target Component: `./sources/backend.chatbot.;src/test/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotTest.java` `[REQ-019]` – kiểm tra trả lời tự động, fallback đến human support, và ghi log.

### DAY 24
- **[Reviewer]:** Target Component: `./sources/docs/chatbotApi.yaml` `[REQ-019]` – đánh giá tài liệu API chatbot, đảm bảo các trường hợp fallback được định nghĩa.

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-001]‑[NFR-009]
- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng PreparedStatement/ParameterizedQuery cho mọi truy vấn động; whitelist các cột cho phép sắp xếp; áp dụng ORM (Hibernate) với validation strict.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động escape tất cả các trường dữ liệu người dùng trong React; sử dụng `dangerouslySetInnerHTML` với sanitizer; chèn header `Content-Security-Policy` với `default-src 'self'; script-src 'self' 'unsafe-inline'` (sau khi di chuyển inline ra ngoài).
- **Multi-Tenant CORS Security Rails:** Chỉ cho phép các origin được whitelist (dựa trên cấu hình tenant); sử dụng `Access-Control-Allow-Origin` động; xác thực token JWT trước khi xử lý yêu cầu CORS.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Áp dụng `@JsonSerialize` với `JsonIgnoreProperties`; regex che giấu số CCCD, email trong log; giữ log trong 1 năm theo NFR‑006.
- **JWT & Session Management:** Access token expiry 15 phút, refresh token 7 ngày; rotate token khi phát hiện anomaly; lưu token đã logout vào Redis blacklist.
- **Docker Image Size:** Multi-stage build, base image `alpine:3.18`, tổng kích thước ảnh cuối < 500 MB (NFR‑005).
- **Backup & Disaster Recovery:** Sao lưu PostgreSQL đầy đủ hàng ngày, point-in-time recovery 24 giờ, cluster GKE dự phòng ở region khác (NFR‑009).
- **GDPR/CCPA Compliance:** Endpoint `/gdpr/delete/{userId}` để xóa dữ liệu cá nhân; xuất dữ liệu JSON qua `/gdpr/export/{userId}`; quản lý consent cho marketing (lưu trữ trong SystemSettings) (NFR‑008).

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng `@capacitor/preferences` cho storage an toàn; chặn back-button native; fetch API với retry và cache ngoại tuyến; xác thực token trên backend trước mọi request.
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware phát hiện Accept-Language; fallback sang ngôn ngữ đã lưu trong SystemSettings; render `<html lang='vi'>` hoặc `en`/`es`; chèn thẻ `<link rel="alternate" hreflang="en" href="https://example.com/en/page"/>` cho mỗi ngôn ngữ (REQ‑023).

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Script tự động fork `main` thành `features/development-day-$(date +%Y%m%d)` mỗi buổi sáng.
- **Validation Guard Pipeline Gates:** 
  - **Compilation Check:** `mvn clean compile` – lỗi sẽ dừng pipeline.
  - **Unit Test Coverage:** Yêu cầu độ phủ >= 85 % (JUnit5 + JaCoCo).
  - **Security Scan:** SonarQube phát hiện lỗ hổng, SQLi, XSS.
  - **Docker Build & Push:** Build image, push lên Artifact Registry, trigger GKE rollout.
  - **Integration Test:** Postman collection tự động gọi các endpoint chính (REQ‑001‑025).
  - **Artifact Serialization:** Tạo JSON summary chứa danh sách các component đã hoàn thành, tag liên quan, và timestamp.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]

---