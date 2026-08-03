# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260803050419 |
| **Tên Dự án** | membership-hub |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày.Giờ** | 2026/08/03 05:04:19 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1 Core System Modality & Architecture
Hệ thống được thiết kế theo kiến trúc **Microservices** với mỗi lĩnh vực nghiệp vụ (Auth, User, Center, Course, Enrollment, Attendance, Membership, Notification, Promotion, Announcement, Chatbot, Reporting, Localization) được triển khai dưới dạng một service độc lập. Các service giao tiếp với nhau qua **REST API** và **Event Bus** (ví dụ: Pub/Sub) để đảm bảo tính bất biến của điểm danh và đồng bộ thông báo. Kiến trúc tuân thủ **CQRS** với read model được cache qua Redis, và **Reactive Core** sử dụng Quarkus để xử lý bất đồng bộ một cách phi khối hóa. JWT tokens (15 phút) và refresh tokens (7 ngày) được cấp qua OAuth2 từ Firebase, Google, Facebook. RBAC được thực thi ở tầng gateway với các vai trò System Admin, Center Admin, Manager, Teacher, Student.

### 1.2 Enterprise Data Flow Topologies & Core Ecosystems
Dòng dữ liệu chính bao gồm:
- **Luồng xác thực** (`[ARC-006]`) – OAuth2 authorization code exchange, cấp JWT.
- **Luồng xử lý điểm danh QR** (`[ARC-007]`) – Mobile app quét QR, gửi studentId + timestamp đến Attendance service, ghi nhận bất biến.
- **Luồng gửi thông báo** (`[ARC-008]`) – Push notification qua FCM/APNs đồng thời đăng bài lên nhóm Zalo được chỉ định.
- **Luồng tích hợp backend ứng dụng di động** (`[ARC-009]`) – Frontend Next.js tiêu thụ REST APIs, caching ngoại tuyến qua Service Workers.
Tất cả các event được ghi lại trong audit log (`[ARC-006]`) để đảm bảo khả năng kiểm toán.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.x, PostgreSQL 15, Docker (multi‑stage), Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM) / Apple APNs, Zalo API integration, Redis 7 (caching & session store), GitHub Actions CI/CD.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14, React 18, TypeScript, Tailwind CSS, i18next cho đa ngôn ngữ, Capacitor cho hybrid mobile, Service Workers cho caching ngoại tuyến, React Query cho data sync.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Quy tắc Ranh giới Không gian Làm việc Tuyệt đối:** Workspace gốc cố định ở `..`. Tất cả đường dẫn phải bắt đầu với `./sources/`.
- **Tuân thủ Quy tắc Tiền tố Thư mục Động:** Áp dụng quy tắc ánh xạ thư mục động phù hợp với cấu trúc dự án.
- **[ĐIỀU KIỆN: JAVA_STACK_ONLY] Tiêu chuẩn Gói Java:** Nếu stack sử dụng Java, tất cả mã nguồn Java phải nằm trong gói cơ sở doanh nghiệp: `org.nlh4j.saas.membershiphub`. Chuyển đổi tên dự án thành token thuần chữ thường, số, loại bỏ khoảng trắng, dấu gạch ngang, dấu gạch dưới.
- **Cú pháp Mục tiêu Đường dẫn Kiểm tra nghiêm ngặt:** Bất kỳ thành phần nào được Tester nhắm mục tiêu phải được cấu trúc dưới dạng cặp phân cách bán phẩy `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn trong cặp phải bắt đầu với `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Giai đoạn | Khoảng ngày | Đường dẫn Thành phần / Module Kiến trúc | Tóm tắt Sản phẩm Kỹ thuật | Sub-Agent được chỉ định | Tag IDs Mục tiêu |
|----------|------------|-----------------------------------|----------------------|-------------------|-----------------|
| 1 | Ngày 1 | ./sources/backend.auth, ./sources/backend.user, ./sources/backend.center, ./sources/backend.course, ./sources/backend.enrollment, ./sources/backend.attendance, ./sources/backend.membership | Triển khai core services: đăng ký người dùng, xác thực OAuth, phân quyền, quản lý trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, validation đầu vào, exception handling | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [DAT-003], [EXC-004], [NFR-001], [NFR-003], [NFR-006] |
| 2 | Ngày 2 | ./sources/backend.notification, ./sources/backend.promotion, ./sources/backend.announcement, ./sources/backend.chatbot, ./sources/backend.reporting, ./sources/backend.localization | Triển khai thông báo đa kênh, khuyến mãi, thông báo hệ thống, chatbot AI, báo cáo, localization | Tester | [REQ-016], [EXC-003], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-008], [DAT-009], [DAT-011], [NFR-001], [NFR-007], [NFR-008] |
| 3 | Ngày 3 | ./sources/infra | Xây dựng image Docker, multi‑stage Dockerfile cho tất cả service, push lên registry | Docker | [NFR-005], [NFR-004], [ARC-010] |
| 4 | Ngày 4 | ./sources/infra | Cung cấp hạ tầng GCP: VPC, IAM, Firebase Auth, FCM/APNs, Zalo API, Redis, Cloud Storage, Secret Manager | GCP | [ARC-008], [ARC-009], [NFR-003], [NFR-006], [NFR-004] |
| 5 | Ngày 5 | ./sources/infra | Triển khai cluster GKE, tạo Deployment, Service, HPA, tích hợp CI/CD, bảo mật, giám sát | GKE | [ARC-010], [NFR-002], [NFR-004], [NFR-005] |
| 5 | Ngày 5 | ./sources/backend.notification, ./sources/backend.promotion, ./sources/backend.announcement, ./sources/backend.chatbot, ./sources/backend.reporting, ./sources/backend.localization | Tài liệu API contracts, hướng dẫn vận hành, tài liệu kỹ thuật | Doc | [REQ-016], [EXC-003], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-008], [DAT-009], [DAT-011] |
| 5 | Ngày 5 | ./sources/backend.notification, ./sources/backend.promotion, ./sources/backend.announcement, ./sources/backend.chatbot, ./sources/backend.reporting, ./sources/backend.localization | Đánh giá chất lượng code, phát hiện lỗ hổng bảo mật, tối ưu hiệu năng, đảm bảo tuân thủ NFR | Reviewer | [REQ-016], [EXC-003], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-008], [DAT-009], [DAT-011], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai core services: đăng ký người dùng, xác thực OAuth, phân quyền, quản lý trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, validation đầu vào, exception handling.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend.auth [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
  * ./sources/backend.user [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004]
  * ./sources/backend.center [REQ-004], [REQ-005], [REQ-006], [DAT-003], [NFR-001], [NFR-003]
  * ./sources/backend.course [REQ-007], [REQ-008], [REQ-009], [DAT-004], [NFR-001], [NFR-003]
  * ./sources/backend.enrollment [REQ-010], [REQ-011], [DAT-005], [NFR-001]
  * ./sources/backend.attendance [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006], [NFR-001]
  * ./sources/backend.membership [REQ-014], [REQ-015], [DAT-007], [NFR-001]
- **Database Schema DDL SQL Specification [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007]:**
```sql
-- [DAT-001] Users & Roles
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
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);
-- Indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role_id);

-- [DAT-003] Centers
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255)
);
CREATE INDEX idx_centers_tax_id ON centers(tax_id);

-- [DAT-004] Courses
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
);
CREATE INDEX idx_courses_teacher ON courses(teacher_id);
CREATE INDEX idx_courses_date_range ON courses(start_date, end_date);

-- [DAT-005] Enrollments
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_unique_enrollment ON enrollments(student_id, course_id);
CREATE INDEX idx_enrollments_course ON enrollments(course_id);

-- [DAT-006] Attendance
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    recorded_at TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE INDEX idx_attendance_student ON attendance(student_id);
CREATE INDEX idx_attendance_course ON attendance(course_id);
CREATE INDEX idx_attendance_date ON attendance(attendance_date);

-- [DAT-007] StudentCards
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL GENERATED ALWAYS AS (validity_days - EXTRACT(DAY FROM (CURRENT_DATE - issue_date))) STORED
);
CREATE INDEX idx_studentcards_student ON student_cards(student_id);
```

- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
```http
POST /api/v1/auth/register
Content-Type: application/json
Request:
{
  "email":"user@example.com",
  "password":"StrongPass123!",
  "fullName":"Nguyen Van A",
  "roleId":5
}
Response:
HTTP/1.1 201 Created
{
  "userId":"a1b2c3d4-...",
  "email":"user@example.com",
  "roleId":5,
  "token":"jwt.access.token.here",
  "refreshToken":"jwt.refresh.token.here"
}
```
```http
POST /api/v1/auth/social
Content-Type: application/json
Request:
{
  "provider":"google",
  "code":"oauth2.code.here"
}
Response:
HTTP/1.1 200 OK
{
  "userId":"a1b2c3d4-...",
  "token":"jwt.access.token.here"
}
```
```http
PUT /api/v1/users/{userId}/role
Content-Type: application/json
Request:
{
  "newRoleId":3
}
Response:
HTTP/1.1 200 OK
{
  "userId":"a1b2c3d4-...",
  "roleId":3
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
  * Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc) – trả về HTTP 400 với JSON body: `{"error":"VALIDATION_FAILED","message":"Email không hợp lệ hoặc thiếu trường bắt buộc.","details":[{"field":"email","issue":"Sai định dạng"}]}`.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1:** Triển khai core authentication và quản lý người dùng cho hệ thống membership.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
      - **Low-Level Technical Task Instruction:** Triển khai các endpoint `/register`, `/social`, `/role` trong service Auth. Sử dụng Spring Security với OAuth2 login cho Firebase/Google/Facebook. Hash mật khẩu bằng bcrypt. Tạo JWT với thời gian sống 15 phút, lưu refresh token trong bảng người dùng. Áp dụng validation đầu vào nghiêm ngặt (email, password strength). Ghi log mọi thay đổi vai trò người dùng vào bảng audit log. Đảm bảo endpoint trả về JSON response chuẩn và xử lý lỗi đồng nhất.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
    * **[Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth;./sources/backend.auth[TestAuthSuite]
      - **Low-Level Technical Task Instruction:** Viết unit tests cho các method đăng ký, xác thực xã hội, cập nhật vai trò. Sử dụng JUnit5, Mockito, và test data factory để mô phỏng OAuth2 code. Kiểm tra response code, payload, và token generation. Đảm bảo các trường hợp lỗi (email duplicate, password yếu) trả về HTTP 400 với message phù hợp.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
    * **[Reviewer]:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth
      - **Low-Level Technical Task Instruction:** Đánh giá chất lượng code: tuân thủ Clean Code, thiết kế SOLID, xử lý ngoại lệ, bảo mật (OWASP). Kiểm tra các vấn đề về race condition trong quá trình tạo userId, xung đột khóa duy nhất email. Đề xuất cải tiến hiệu năng và ghi lại mọi phát hiện trong báo cáo review.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth
      - **Low-Level Technical Task Instruction:** Soạn thảo OpenAPI spec cho các endpoint auth, bao gồm request/response schemas, error responses, và ví dụ. Xuất tài liệu dưới dạng Markdown cho developer portal. Đảm bảo spec bao phủ tất cả các trường hợp sử dụng và tag IDs tương ứng.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
    * **[Docker]:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth
      - **Low-Level Technical Task Instruction:** Tạo multi‑stage Dockerfile: giai đoạn build (Maven/Gradle) → giai đoạn runtime (distroless Java21). Thiết lập healthcheck endpoint `/actuator/health`. Push image lên registry với tag `latest` và `v1.0`. Đảm bảo image size < 500MB.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
    * **[GCP]:**
      - **Target Component file path (`target_component`):** ./sources/infra
      - **Low-Level Technical Task Instruction:** Tạo project GCP, bật Firebase Authentication, cấp IAM role `cloud.run.admin` cho service account. Thiết lập Secret Manager cho JWT secret và khóa bcrypt. Kích hoạt Cloud Logging để ghi lại audit trail cho các thao tác người dùng.
      - **Targeted Tag IDs:** [ARC-006], [NFR-003], [NFR-006]
    * **[GKE]:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth
      - **Low-Level Technical Task Instruction:** Viết Kubernetes Deployment và Service cho Auth service. Cấu hình HPA dựa trên CPU > 70% hoặc latency > 300ms. Thiết lập Ingress với TLS. Tích hợp CI/CD để tự động deploy khi có thay đổi code.
      - **Targeted Tag IDs:** [ARC-006], [NFR-002], [NFR-004]

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai thông báo đa kênh, khuyến mãi, thông báo hệ thống, chatbot AI, báo cáo, localization.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend.notification [REQ-016], [EXC-003], [DAT-008], [NFR-001], [NFR-003]
  * ./sources/backend.promotion [REQ-017], [DAT-009], [NFR-001]
  * ./sources/backend.announcement [REQ-018], [DAT-009], [NFR-001]
  * ./sources/backend.chatbot [REQ-019], [NFR-001], [NFR-007]
  * ./sources/backend.reporting [REQ-024], [REQ-025], [DAT-011], [NFR-001], [NFR-008]
  * ./sources/backend.localization [REQ-022], [REQ-023], [NFR-007], [NFR-008]
- **Database Schema DDL SQL Specification [DAT-008], [DAT-009], [DAT-011]:**
```sql
-- [DAT-008] Notifications
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
CREATE INDEX idx_notifications_user ON notifications(user_id);
CREATE INDEX idx_notifications_sent ON notifications(sent_at);

-- [DAT-009] Promotions
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT
);
CREATE INDEX idx_promotions_code ON promotions(code);

-- [DAT-009] Announcements
CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);
CREATE INDEX idx_announcements_date_range ON announcements(start_date, end_date);

-- [DAT-011] SystemSettings
CREATE TABLE system_settings (
    setting_key VARCHAR(50) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **API and Event Routing Contracts [REQ-016], [EXC-003], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]:**
```http
POST /api/v1/notifications
Content-Type: application/json
Request:
{
  "userId":"a1b2c3d4-...",
  "groupZalo":"group123",
  "message":"Khóa học mới đã bắt đầu!"
}
Response:
HTTP/1.1 202 Accepted
{
  "notificationId":"n1o2p3q4-...",
  "sentAt":"2026-08-03T05:04:19Z"
}
```
```http
POST /api/v1/promotions
Content-Type: application/json
Request:
{
  "code":"SUMMER20",
  "discountPercent":20,
  "startDate":"2026-06-01",
  "endDate":"2026-08-31",
  "description":"Giảm giá 20% cho tất cả khóa học"
}
Response:
HTTP/1.1 201 Created
{
  "promoId":"r1s2t3u4-..."
}
```
```http
POST /api/v1/announcements
Content-Type: application/json
Request:
{
  "title":"Thông báo bảo trì hệ thống",
  "content":"Hệ thống sẽ bảo trì vào ngày mai.",
  "startDate":"2026-08-03",
  "endDate":"2026-08-04"
}
Response:
HTTP/1.1 201 Created
{
  "announcementId":"a1b2c3d4-..."
}
```
```http
POST /api/v1/chatbot/query
Content-Type: application/json
Request:
{
  "userId":"a1b2c3d4-...",
  "question":"Khóa học toán ở trung tâm nào có sẵn?"
}
Response:
HTTP/1.1 200 OK
{
  "answer":"Có khóa học Toán cơ bản tại trung tâm Hà Nội."
}
```
```http
GET /api/v1/reports/attendance?centerId=c1d2e3f4&dateFrom=2026-07-01&dateTo=2026-07-31
Response:
HTTP/1.1 200 OK
[
  {
    "studentName":"Nguyen Van A",
    "courseName":"Toán cơ bản",
    "attendanceDate":"2026-07-15",
    "status":"present"
  }
]
```
```http
GET /api/v1/i18n/{lang}
Response:
HTTP/1.1 200 OK
{
  "locale":"vi",
  "strings":{
    "welcome":"Chào mừng bạn",
    "login":"Đăng nhập"
  }
}
```

- **Phase Localized Exception Handlers [EXC-003]:**
  * Lỗi gửi push notification không thành công (ví dụ: device token không hợp lệ) – ghi log lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu delivered = false và tạo sự kiện `NotificationFailed`.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 2:** Triển khai và kiểm thử các service thông báo, khuyến mãi, chatbot, báo cáo, và localization.
  - **Sub-Agent Workflow Specialization:**
    * **[Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification;./sources/backend.notification[TestNotificationSuite]
      - **Low-Level Technical Task Instruction:** Viết integration tests cho endpoint tạo notification, kiểm tra việc push qua FCM/APNs, ghi log vào bảng notifications. Mô phỏng device token không hợp lệ để xác nhận logic retry và đánh dấu delivered.
      - **Targeted Tag IDs:** [REQ-016], [EXC-003], [DAT-008], [NFR-001], [NFR-003]
    * **[Reviewer]:**
      - **Target Component file path (`target_component`):** ./sources/backend.promotion
      - **Low-Level Technical Task Instruction:** Đánh giá logic validation cho promotion code (unique, date ranges), kiểm tra SQL injection, XSS trong description, đảm bảo discountPercent nằm trong 0-100. Đề xuất index cho code và date ranges.
      - **Targeted Tag IDs:** [REQ-017], [DAT-009], [NFR-001]
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/backend.announcement
      - **Low-Level Technical Task Instruction:** Soạn thảo OpenAPI spec cho Announcement API, bao gồm schema cho startDate/endDate optional, quy tắc hiển thị tự động dựa trên ngày. Ghi chú quy trình tự động ẩn thông báo sau endDate.
      - **Targeted Tag IDs:** [REQ-018], [DAT-009], [NFR-001]
    * **[Docker]:**
      - **Target Component file path (`target_component`):** ./sources/backend.chatbot
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho Chatbot service (Java + Spring AI). Tối ưu hóa image size < 200MB. Thêm healthcheck `/ready`. Push image với tag `chatbot:v1`.
      - **Targeted Tag IDs:** [REQ-019], [NFR-005], [NFR-001]
    * **[GCP]:**
      - **Target Component file path (`target_component`):** ./sources/infra
      - **Low-Level Technical Task Instruction:** Cấu hình Pub/Sub topic `notifications`, Cloud Scheduler cho job định kỳ gửi thông báo, Secret Manager cho khóa Zalo API. Thiết lập IAM cho service account `event.receiver`.
      - **Targeted Tag IDs:** [ARC-008], [NFR-003], [NFR-004]
    * **[GKE]:**
      - **Target Component file path (`target_component`):** ./sources/backend.reporting
      - **Low-Level Technical Task Instruction:** Tạo Deployment cho Reporting service, expose HTTP endpoint `/reports/attendance`. Cấu hình resource limits (CPU 250m, Memory 512Mi). Thiết lập HPA dựa trên latency.
      - **Targeted Tag IDs:** [REQ-024], [REQ-025], [DAT-011], [NFR-002], [NFR-004]

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng container hóa và triển khai hạ tầng cloud cho tất cả services.
- **Target Physical Directory Matrix Map:**
  * ./sources/infra (Dockerfiles cho tất cả services)
  * ./sources/infra (Cấu hình CI/CD pipeline)
- **Database Schema DDL SQL Specification:** (Không có schema mới trong phase này)
- **API and Event Routing Contracts:** (Không có contract mới)
- **Phase Localized Exception Handlers:** (Không có exception mới)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 3:** Xây dựng và push Docker images, thiết lập CI/CD.
  - **Sub-Agent Workflow Specialization:**
    * **[Docker]:**
      - **Target Component file path (`target_component`):** ./sources/infra
      - **Low-Level Technical Task Instruction:** Tạo root Dockerfile (multi‑stage) tham chiếu đến từng service subdirectory. Cấu hình GitHub Actions workflow `.github/workflows/deploy.yml` để build, test, push image, trigger GKE rollout khi có commit mới vào branch `main`. Đảm bảo image tag bao gồm `latest` và `build-${GITHUB_RUN_NUMBER}`.
      - **Targeted Tag IDs:** [NFR-005], [NFR-004], [ARC-010]
    * **[GCP]:**
      - **Target Component file path (`target_component`):** ./sources/infra
      - **Low-Level Technical Task Instruction:** Provision VPC với private subnets, Cloud NAT, Private Service Connect cho PostgreSQL. Tạo Service Account `gke-admin` với role `roles/container.admin`. Thiết lập Cloud Monitoring và Cloud Alerting cho các metric quan trọng.
      - **Targeted Tag IDs:** [ARC-008], [ARC-009], [NFR-003], [NFR-006]
    * **[GKE]:**
      - **Target Component file path (`target_component`):** ./sources/infra
      - **Low-Level Technical Task Instruction:** Viết Helm charts cho từng service (Auth, User, Center, Course, Enrollment, Attendance, Membership, Notification, Promotion, Announcement, Chatbot, Reporting, Localization). Cấu hình Ingress TLS, HPA, PodDisruptionBudgets. Triển khai cluster với Node Auto Provisioning.
      - **Targeted Tag IDs:** [ARC-010], [NFR-002], [NFR-004], [NFR-005]

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai và tối ưu hóa môi trường sản xuất trên GKE, đảm bảo tuân thủ NFR.
- **Target Physical Directory Matrix Map:**
  * ./sources/infra (K8s manifests cho tất cả services)
  * ./sources/infra (ConfigMap/Secret cho cấu hình ứng dụng)
- **Database Schema DDL SQL Specification:** (Không có schema mới)
- **API and Event Routing Contracts:** (Không có contract mới)
- **Phase Localized Exception Handlers:** (Không có exception mới)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 4:** Triển khai lên GKE và cấu hình autoscaling.
  - **Sub-Agent Workflow Specialization:**
    * **[GKE]:**
      - **Target Component file path (`target_component`):** ./sources/infra
      - **Low-Level Technical Task Instruction:** Áp dụng Helm releases cho từng service: `helm upgrade --install auth ./charts/auth`. Thiết lập ServiceMonitor cho Prometheus. Cấu hình NetworkPolicy để hạn chế giao tiếp giữa các service. Kiểm tra readiness/liveness probes.
      - **Targeted Tag IDs:** [ARC-010], [NFR-002], [NFR-004], [NFR-005]
    * **[Docker]:**
      - **Target Component file path (`target_component`):** ./sources/infra
      - **Low-Level Technical Task Instruction:** Tạo CI/CD job để tự động build và push image khi có thay đổi code. Sử dụng GitHub Actions `docker/build-push-action`. Đảm bảo image được ký với Cosign.
      - **Targeted Tag IDs:** [NFR-005], [NFR-004]
    * **[GCP]:**
      - **Target Component file path (`target_component`):** ./sources/infra
      - **Low-Level Technical Task Instruction:** Thiết lập Cloud Deploy pipeline để triển khai từ artifact repository vào GKE clusters. Cấu hình canary release cho service mới trước khi full traffic.
      - **Targeted Tag IDs:** [ARC-008], [ARC-009], [NFR-003], [NFR-006]

### Phase 5 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Hoàn thiện tài liệu, đánh giá bảo mật, và đảm bảo tuân thủ toàn diện các tiêu chuẩn doanh nghiệp.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend.notification, ./sources/backend.promotion, ./sources/backend.announcement, ./sources/backend.chatbot, ./sources/backend.reporting, ./sources/backend.localization (tài liệu API)
  * ./sources/backend.notification, ./sources/backend.promotion, ./sources/backend.announcement, ./sources/backend.chatbot, ./sources/backend.reporting, ./sources/backend.localization (đánh giá bảo mật)
- **Database Schema DDL SQL Specification:** (Không có schema mới)
- **API and Event Routing Contracts:** (Không có contract mới)
- **Phase Localized Exception Handlers:** (Không có exception mới)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 5:** Hoàn thiện tài liệu và đánh giá bảo mật cuối cùng.
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification, ./sources/backend.promotion, ./sources/backend.announcement, ./sources/backend.chatbot, ./sources/backend.reporting, ./sources/backend.localization
      - **Low-Level Technical Task Instruction:** Soạn thảo tài liệu API hoàn chỉnh cho tất cả các service thông báo, khuyến mãi, thông báo, chatbot, báo cáo, localization. Bao gồm request/response schemas, ví dụ sử dụng, quy tắc lỗi, và hướng dẫn tích hợp cho mobile app. Đính kèm tag IDs tương ứng trong mỗi phần.
      - **Targeted Tag IDs:** [REQ-016], [EXC-003], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-008], [DAT-009], [DAT-011]
    * **[Reviewer]:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification, ./sources/backend.promotion, ./sources/backend.announcement, ./sources/backend.chatbot, ./sources/backend.reporting, ./sources/backend.localization
      - **Low-Level Technical Task Instruction:** Thực hiện đánh giá bảo mật toàn diện: kiểm tra SQL injection, XSS, CSRF, xác thực JWT, quản lý session, logging PII. Sử dụng OWASP ZAP để quét các endpoint. Ghi lại mọi vấn đề và cung cấp fix implementation.
      - **Targeted Tag IDs:** [REQ-016], [EXC-003], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-008], [DAT-009], [DAT-011], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-001]..[NFR-009]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng Prepared Statements / Parameterized Queries cho tất cả truy vấn SQL. Áp dụng whitelist cho các cột sắp xếp động. Áp dụng Row-Level Security (RLS) trên PostgreSQL để đảm bảo tenant isolation (`[ARC-002]`, `[ARC-003]`).
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động escape tất cả đầu vào người dùng trong Thymeleaf/JSX. Áp dụng CSP header: `default-src 'self'; script-src 'self' 'unsafe-inline' https://trusted.cdn.com; style-src 'self' 'unsafe-inline';`. Sử dụng `@CrossOrigin` cho API.
- **Multi-Tenant CORS Security Rails:** Cấu hình CORS per-request dựa trên host của request (`.allowedOrigins` từ SystemSettings). Từ chối wildcard `*.example.com`. Ghi log mỗi request CORS cho audit (`[NFR-006]`).
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Sử dụng Logback với `MaskingFilter` để che giấu email, số điện thoại, CCCD. Áp dụng `@JsonSerialize` cho các trường nhạy cảm. Xóa log sau 1 năm (`[NFR-006]`).

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng `@capacitor/core` cho network status, retry queue cho các request thất bại (ví dụ: điểm danh QR khi offline). Lưu trữ dữ liệu locally với `@capacitor/preferences`. Xử lý back-button native với `SplashScreen` và `StatusBar`.
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware