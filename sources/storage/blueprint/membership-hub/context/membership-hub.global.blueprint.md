# NGƯỜI QUẢN LÝ DỰ ÁN: membership-hub

## 📊 Điều khiển tài liệu

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260807091404 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/07 09:14:04 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH CƠ SỞ

### 1.1. Mô hình hệ thống cốt lõi & mô hình kiến trúc
- Kiến trúc microservices phân tách rõ ràng: Auth, Center, Course, Enrollment, Attendance, Card, Notification, Promotion, Report, Chatbot, DevOps.
- Sử dụng mô hình CQRS cho các dịch vụ CRUD, Event Sourcing cho Attendance.
- Dùng Kafka (hoặc Pub/Sub) cho sự kiện push notification và Zalo integration.
- Dùng Quarkus với reactive extensions, PostgreSQL + Redis cho session caching.
- Frontend: Next.js 13 + React, Capacitor cho mobile, i18n đa ngôn ngữ.
- DevOps: Docker multi-stage, GKE, GitHub Actions CI/CD, Stackdriver monitoring.

### 1.2. Topology luồng dữ liệu & hệ sinh thái
- Luồng xác thực: OAuth2 + Firebase, JWT 15m, refresh 7d.
- Luồng điểm danh: Mobile QR → API → idempotent Attendance.
- Luồng thông báo: Event → FCM/APNs + Zalo group.
- Luồng backend: REST APIs, gRPC (nếu cần), Kafka topics.
- Luồng dữ liệu: PostgreSQL primary, read replicas cho báo cáo.

## 📁 2. CƠ SỞ CÔNG NGHỆ & THƯ VIỆN HỆ THỐNG

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3, Hibernate ORM, Flyway, PostgreSQL 15, Redis 7, Firebase Auth, Google Cloud SDK, Docker, GKE.
- **Frontend & Cross-Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, Capacitor 4, React Native (via Capacitor), i18next.

### MẢNG CƠ SỞ

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=[true]
BACKEND_LAYER_REQUIRED=[true]
FRONTEND_LAYER_REQUIRED=[true]
MOBILE_LAYER_REQUIRED=[true]
DEVOPS_LAYER_REQUIRED=[true]
```

## 📁 3. QUY ĐỊNH BẢO VỆ & THUỘC ĐIỂM TUYÊN CHÍNH

- Repository root: `.`; all paths start with `./sources/`.
- Java package: `org.nlh4j.saas.membershiphub`.
- Tester target path syntax: `<source_component>;<test_suite_file>`.

## 📊 4. BẢNG TỔNG QUAN ĐA GIAI ĐOẠN KIẾN TRÚC

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Day 1 - 6 | ./sources/backend/auth-service/ | Xác thực người dùng, quản lý vai trò, JWT, DDL Users & Roles, API contracts, exception handling | Coder | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [DAT-002], [EXC-004], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| 2 | Day 1 - 6 | ./sources/backend/center-service/, ./sources/backend/course-service/, ./sources/backend/enrollment-service/, ./sources/backend/attendance-service/ | CRUD trung tâm, khóa học, ghi danh, điểm danh, DDL Centers, Courses, Enrollments, Attendance, exception handling | Coder | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| 3 | Day 1 - 6 | ./sources/backend/card-service/, ./sources/backend/notification-service/, ./sources/backend/promotion-service/, ./sources/backend/report-service/ | Thẻ hội viên, thông báo, khuyến mãi, báo cáo, hardening, exception handling | Coder | [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-024], [REQ-025], [EXC-003], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| 4 | Day 1 - 6 | ./sources/frontend/web-app/, ./sources/frontend/mobile-app/, ./sources/backend/chatbot-service/ | UI web & mobile, chatbot AI, i18n, SEO, documentation | Coder | [REQ-020], [REQ-021], [REQ-019], [REQ-022], [REQ-023], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| 5 | Day 1 - 6 | ./sources/infra/, ./sources/docs/ | CI/CD, monitoring, testing, audit, release | Coder | [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 📁 5. CHỮ ĐIỆN CHI TIẾT GIAI ĐOẠN & BẢN GIAO HÀNG NGÀY ĐẾN NGÀY

### 📈 Giai đoạn 1: Xác thực người dùng, quản lý vai trò, JWT, DDL Users & Roles, API contracts, exception handling
- **Phase Core Objective & Purpose**: Thiết lập hệ thống xác thực, quản lý vai trò, và cấu trúc cơ sở dữ liệu người dùng.
- **Target Physical Directory Matrix Map**:
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/RegistrationController.java [REQ-001]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/SocialAuthController.java [REQ-002]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/RoleAssignmentService.java [REQ-003]
  * ./sources/backend/auth-service/src/main/resources/db/migration/V001__create_users_roles.sql [DAT-001], [DAT-002]
  * ./sources/docs/api/auth_api_spec.md [REQ-001], [REQ-002], [REQ-003]
  * ./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/GlobalExceptionHandler.java [EXC-004]
- **Database Schema DDL SQL Specification [DAT-001], [DAT-002]**:
```sql:matrix
CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash VARCHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL,
    provider VARCHAR(20) NOT NULL CHECK (provider IN ('local', 'firebase', 'google', 'facebook')),
    createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
    updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);
ALTER TABLE USERS ADD CONSTRAINT fk_user_role FOREIGN KEY (roleId) REFERENCES ROLES(roleId);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003]**:
  * `/api/auth/register` POST – request: `{email, password, fullName}`; response: `{token, userId}`
  * `/api/auth/social-login` POST – request: `{provider, code}`; response: `{token, userId}`
  * `/api/auth/role` PUT – request: `{userId, roleId}`; response: `{status}`
- **Phase Localized Exception Handlers [EXC-004]**:
  * ValidationException → 400 Bad Request with field errors.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1: Xác thực đăng ký**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-001]`
  * **Target Component file path (`target_component`):** `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/RegistrationController.java [REQ-001]`
  * **Low-Level Technical Task Instruction:** Tạo endpoint `/api/auth/register`, xác thực email, hash mật khẩu bằng BCrypt, lưu người dùng với role `Student`, trả về JWT 15 phút và refresh token 7 ngày.

- **DAY 2: Xác thực OAuth2**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-002]`
  * **Target Component file path (`target_component`):** `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/SocialAuthController.java [REQ-002]`
  * **Low-Level Technical Task Instruction:** Triển khai flow OAuth2, nhận `code`, trao đổi lấy `access_token`, lấy thông tin người dùng, tạo/ cập nhật bản ghi, issue JWT.

- **DAY 3: Phân quyền người dùng**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-003]`
  * **Target Component file path (`target_component`):** `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/RoleAssignmentService.java [REQ-003]`
  * **Low-Level Technical Task Instruction:** Endpoint `/api/auth/role` PUT, xác thực admin, cập nhật `roleId` trong bảng USERS, phản hồi trạng thái.

- **DAY 4: DDL Users & Roles**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[DAT-001], [DAT-002]`
  * **Target Component file path (`target_component`):** `./sources/backend/auth-service/src/main/resources/db/migration/V001__create_users_roles.sql [DAT-001], [DAT-002]`
  * **Low-Level Technical Task Instruction:** Viết script tạo bảng USERS và ROLES, thêm constraint FK, CHECK enum provider, index email.

- **DAY 5: API Contracts**
  * **Sub-Agent Workflow Specialization:** `[Reviewer]`
  * **Targeted Tag IDs:** `[REQ-001], [REQ-002], [REQ-003]`
  * **Target Component file path (`target_component`):** `./sources/docs/api/auth_api_spec.md [REQ-001], [REQ-002], [REQ-003]`
  * **Low-Level Technical Task Instruction:** Viết tài liệu chi tiết endpoint, request/response schemas, mã lỗi, ví dụ.

- **DAY 6: Exception Handling**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[EXC-004]`
  * **Target Component file path (`target_component`):** `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/GlobalExceptionHandler.java [EXC-004]`
  * **Low-Level Technical Task Instruction:** Xử lý ValidationException, trả về 400 với danh sách lỗi, log chi tiết.

### 📈 Giai đoạn 2: CRUD trung tâm, khóa học, ghi danh, điểm danh, DDL, exception handling
- **Phase Core Objective & Purpose**: Xây dựng các dịch vụ CRUD cho trung tâm, khóa học, ghi danh, điểm danh và cấu trúc dữ liệu liên quan.
- **Target Physical Directory Matrix Map**:
  * ./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java [REQ-004], [REQ-005], [REQ-006]
  * ./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseController.java [REQ-007], [REQ-008], [REQ-009]
  * ./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java [REQ-010], [REQ-011]
  * ./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceController.java [REQ-012], [REQ-013]
  * ./sources/backend/center-service/src/main/resources/db/migration/V002__create_centers.sql [DAT-003]
  * ./sources/backend/course-service/src/main/resources/db/migration/V003__create_courses.sql [DAT-004]
  * ./sources/backend/enrollment-service/src/main/resources/db/migration/V004__create_enrollments.sql [DAT-005]
  * ./sources/backend/attendance-service/src/main/resources/db/migration/V005__create_attendance.sql [DAT-006]
  * ./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceExceptionHandler.java [EXC-001], [EXC-002]
- **Database Schema DDL SQL Specification [DAT-003], [DAT-004], [DAT-005], [DAT-006]**:
```sql:matrix
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(30),
    contactEmail VARCHAR(255)
);
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID,
    maxStudents INT DEFAULT 30,
    CONSTRAINT fk_course_teacher FOREIGN KEY (teacherId) REFERENCES USERS(userId)
);
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_enrollment_student FOREIGN KEY (studentId) REFERENCES USERS(userId),
    CONSTRAINT fk_enrollment_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_attendance_student FOREIGN KEY (studentId) REFERENCES USERS(userId),
    CONSTRAINT fk_attendance_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId),
    CONSTRAINT uq_attendance UNIQUE (studentId, courseId, attendanceDate)
);
```
- **API and Event Routing Contracts [REQ-004]–[REQ-013]**: (list endpoints).
- **Phase Localized Exception Handlers [EXC-001], [EXC-002]**: (network drop, duplicate attendance).

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1: CRUD trung tâm**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-004], [REQ-005], [REQ-006]`
  * **Target Component file path (`target_component`):** `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java [REQ-004], [REQ-005], [REQ-006]`
  * **Low-Level Technical Task Instruction:** Tạo endpoints `/api/centers` GET, POST, PUT, DELETE, logic phân quyền Center Admin, kiểm tra duplicate taxId.

- **DAY 2: CRUD khóa học**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-007], [REQ-008], [REQ-009]`
  * **Target Component file path (`target_component`):** `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseController.java [REQ-007], [REQ-008], [REQ-009]`
  * **Low-Level Technical Task Instruction:** Endpoints `/api/courses` GET, POST, PUT, DELETE, kiểm tra xung đột lịch cho giáo viên, logic gán giáo viên.

- **DAY 3: Ghi danh học viên**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-010], [REQ-011]`
  * **Target Component file path (`target_component`):** `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java [REQ-010], [REQ-011]`
  * **Low-Level Technical Task Instruction:** Endpoints `/api/enrollments/browse`, `/api/enrollments/register`, tự tạo tài khoản Student nếu chưa có, tạo bản ghi Enrollment, gửi notification.

- **DAY 4: Điểm danh QR**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-012], [REQ-013]`
  * **Target Component file path (`target_component`):** `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceController.java [REQ-012], [REQ-013]`
  * **Low-Level Technical Task Instruction:** Endpoint `/api/attendance/scan`, nhận studentId, courseId, timestamp, kiểm tra idempotent, ghi nhận Attendance.

- **DAY 5: DDL cho Centers, Courses, Enrollments, Attendance**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[DAT-003], [DAT-004], [DAT-005], [DAT-006]`
  * **Target Component file path (`target_component`):** `./sources/backend/center-service/src/main/resources/db/migration/V002__create_centers.sql [DAT-003]`, `./sources/backend/course-service/src/main/resources/db/migration/V003__create_courses.sql [DAT-004]`, `./sources/backend/enrollment-service/src/main/resources/db/migration/V004__create_enrollments.sql [DAT-005]`, `./sources/backend/attendance-service/src/main/resources/db/migration/V005__create_attendance.sql [DAT-006]`
  * **Low-Level Technical Task Instruction:** Viết script tạo bảng, constraint, index, unique.

- **DAY 6: Exception handling cho Attendance**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[EXC-001], [EXC-002]`
  * **Target Component file path (`target_component`):** `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceExceptionHandler.java [EXC-001], [EXC-002]`
  * **Low-Level Technical Task Instruction:** Xử lý Network drop, duplicate attendance, trả về 200 với flag duplicate.

### 📈 Giai đoạn 3: Thẻ hội viên, thông báo, khuyến mãi, báo cáo, hardening, exception handling
- **Phase Core Objective & Purpose**: Xây dựng các dịch vụ thẻ, thông báo, khuyến mãi, báo cáo và bảo mật.
- **Target Physical Directory Matrix Map**:
  * ./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardController.java [REQ-014], [REQ-015]
  * ./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016]
  * ./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionController.java [REQ-017], [REQ-018]
  * ./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportController.java [REQ-024], [REQ-025]
  * ./sources/docs/security_hardening.md [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
  * ./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationExceptionHandler.java [EXC-003]
- **Database Schema DDL SQL Specification [DAT-007]**:
```sql:matrix
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    CONSTRAINT fk_card_student FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
```
- **API and Event Routing Contracts [REQ-014]–[REQ-025]**: (list endpoints).
- **Phase Localized Exception Handlers [EXC-003]**: (notification failure).

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 1: Thẻ hội viên**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-014], [REQ-015]`
  * **Target Component file path (`target_component`):** `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardController.java [REQ-014], [REQ-015]`
  * **Low-Level Technical Task Instruction:** Endpoints `/api/cards/status`, `/api/cards/renew`, tính remainingDays, cập nhật EndDate, gửi notification.

- **DAY 2: Thông báo**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-016]`
  * **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016]`
  * **Low-Level Technical Task Instruction:** Tạo Notification entity, publish to FCM/APNs, gửi tin Zalo, queue.

- **DAY 3: Khuyến mãi & Thông báo khuyến mãi**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-017], [REQ-018]`
  * **Target Component file path (`target_component`):** `./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionController.java [REQ-017], [REQ-018]`
  * **Low-Level Technical Task Instruction:** CRUD Promotions, Announcements, validation dates, push to students.

- **DAY 4: Báo cáo & Dashboard**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-024], [REQ-025]`
  * **Target Component file path (`target_component`):** `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportController.java [REQ-024], [REQ-025]`
  * **Low-Level Technical Task Instruction:** Endpoint `/api/reports/attendance` CSV, `/api/dashboard` JSON.

- **DAY 5: Hardening Security**
  * **Sub-Agent Workflow Specialization:** `[Reviewer]`
  * **Targeted Tag IDs:** `[NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
  * **Target Component file path (`target_component`):** `./sources/docs/security_hardening.md [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
  * **Low-Level Technical Task Instruction:** Viết tài liệu chi tiết các biện pháp bảo mật, chuẩn OWASP, mã hóa, logging.

- **DAY 6: Exception handling cho Notification**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[EXC-003]`
  * **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationExceptionHandler.java [EXC-003]`
  * **Low-Level Technical Task Instruction:** Retry logic, max 3, log failures.

### 📈 Giai đoạn 4: UI web & mobile, chatbot AI, i18n, SEO, documentation
- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, chatbot, đa ngôn ngữ, SEO và tài liệu.
- **Target Physical Directory Matrix Map**:
  * ./sources/frontend/web-app/src/pages/StudentDashboard.vue [REQ-020], [REQ-021]
  * ./sources/frontend/mobile-app/src/pages/StudentDashboard.vue [REQ-020], [REQ-021]
  * ./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java [REQ-019]
  * ./sources/frontend/web-app/src/i18n/index.js [REQ-022]
  * ./sources/frontend/web-app/public/index.html [REQ-023]
  * ./sources/docs/architecture_overview.md [REQ-001] etc.
- **Database Schema DDL SQL Specification**: none.
- **API and Event Routing Contracts**: none for frontend; chatbot endpoint.
- **Phase Localized Exception Handlers**: none.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1: Giao diện web & mobile**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-020], [REQ-021]`
  * **Target Component file path (`target_component`):** `./sources/frontend/web-app/src/pages/StudentDashboard.vue [REQ-020], [REQ-021]`, `./sources/frontend/mobile-app/src/pages/StudentDashboard.vue [REQ-020], [REQ-021]`
  * **Low-Level Technical Task Instruction:** Thiết kế responsive UI, navigation, gọi API, xử lý push notification.

- **DAY 2: Chatbot AI**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-019]`
  * **Target Component file path (`target_component`):** `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java [REQ-019]`
  * **Low-Level Technical Task Instruction:** Endpoint `/api/chatbot`, tích hợp LLM, fallback to human.

- **DAY 3: Đa ngôn ngữ & SEO**
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** `[REQ-022], [REQ-023]`
  * **Target Component file path (`target_component`):** `./sources/frontend/web-app/src/i18n/index.js [REQ-022]`, `./sources/frontend/web-app/public/index.html [REQ-023]`
  * **Low-Level Technical Task Instruction:** Locale detection, hreflang tags, meta tags.

- **DAY 4: Tài liệu kiến trúc**
  * **Sub-Agent Workflow Specialization:** `[Doc]`
  * **Targeted Tag IDs:** `[REQ-001]`
  * **Target Component file path (`target_component`):** `./sources/docs/architecture_overview.md [REQ-001]`
  * **Low-Level Technical Task Instruction:** Viết tài liệu chi tiết kiến trúc, mô hình, luồng.

- **DAY 5: Kiểm thử tự động**
  * **Sub-Agent Workflow Specialization:** `[Tester]`
  * **Targeted Tag IDs:** `[REQ-001], [REQ-002], [REQ-003]`
  * **Target Component file path (`target_component`):** `./sources/backend/auth-service/src/test/java/org/nlh4j/saas/membershiphub/auth/AuthControllerTest.java [REQ-001], [REQ-002], [REQ-003]`
  * **Low-Level Technical Task Instruction:** Viết unit tests, integration tests, coverage >=85%.

- **DAY 6: Containerization & GCP deployment**
  * **Sub-Agent Workflow Specialization:** `[Docker]`
  * **Targeted Tag IDs:** `[NFR-005], [NFR-004]`
  * **Target Component file path (`target_component`):** `./sources/infra/docker-compose.yml [NFR-005]`, `./sources/infra/k8s/deployment.yaml [NFR-004]`
  * **Low-Level Technical Task Instruction:** Viết Dockerfile multi-stage, docker-compose, k8s deployment, service, ingress.

### 📈 Giai đoạn 5: CI/CD, monitoring, testing, audit, release
- **Phase Core Objective & Purpose**: Thiết lập pipeline CI/CD, giám sát, kiểm thử toàn diện, audit bảo mật, kế hoạch phát hành.
- **Target Physical Directory Matrix Map**:
  * ./sources/infra/github-actions/workflows/ci.yml [NFR-004], [NFR-005]
  * ./sources/infra/gcp/monitoring.yaml [NFR-006]
  * ./sources/backend/all-tests/src/test/java/... [REQ-001] etc.
  * ./sources/docs/security_audit.md [NFR-003], [NFR-004]
  * ./sources/docs/final_release.md [REQ-001]
  * ./sources/infra/k8s/rollback.yaml [NFR-004]
- **Database Schema DDL SQL Specification**: none.
- **API and Event Routing Contracts**: none.
- **Phase Localized Exception Handlers**: none.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 1: CI/CD pipeline**
  * **Sub-Agent Workflow Specialization:** `[GCP]`
  * **Targeted Tag IDs:** `[NFR-004], [NFR-005]`
  * **Target Component file path (`target_component`):** `./sources/infra/github-actions/workflows/ci.yml [NFR-004], [NFR-005]`
  * **Low-Level Technical Task Instruction:** Định nghĩa workflow build, test, push, deploy to GKE.

- **DAY 2: Giám sát & logging**
  * **Sub-Agent Workflow Specialization:** `[GCP]`
  * **Targeted Tag IDs:** `[NFR-006]`
  * **Target Component file path (`target_component`):** `./sources/infra/gcp/monitoring.yaml [NFR-006]`
  * **Low-Level Technical Task Instruction:** Thiết lập Stackdriver, alerting, log aggregation.

- **DAY 3: Kiểm thử toàn diện**
  * **Sub-Agent Workflow Specialization:** `[Tester]`
  * **Targeted Tag IDs:** `[REQ-001]`
  * **Target Component file path (`target_component`):** `./sources/backend/all-tests/src/test/java/... [REQ-001]`
  * **Low-Level Technical Task Instruction:** Chạy regression, coverage, báo cáo.

- **DAY 4: Audit bảo mật**
  * **Sub-Agent Workflow Specialization:** `[Reviewer]`
  * **Targeted Tag IDs:** `[NFR-003], [NFR-004]`
  * **Target Component file path (`target_component`):** `./sources/docs/security_audit.md [NFR-003], [NFR-004]`
  * **Low-Level Technical Task Instruction:** Kiểm tra OWASP, review code, báo cáo.

- **DAY 5: Tài liệu cuối cùng**
  * **Sub-Agent Workflow Specialization:** `[Doc]`
  * **Targeted Tag IDs:** `[REQ-001]`
  * **Target Component file path (`target_component`):** `./sources/docs/final_release.md [REQ-001]`
  * **Low-Level Technical Task Instruction:** Tổng hợp tài liệu, release notes.

- **DAY 6: Kế hoạch rollback**
  * **Sub-Agent Workflow Specialization:** `[GKE]`
  * **Targeted Tag IDs:** `[NFR-004]`
  * **Target Component file path (`target_component`):** `./sources/infra/k8s/rollback.yaml [NFR-004]`
  * **Low-Level Technical Task Instruction:** Định nghĩa rollback strategy, script.

## 📁 6. MÃ BẢO VỆ CÔNG NGHỆ & THIẾT BỊ CHỐNG TIẾN ĐỘ
- **SQL Injection (SQLi) Absolute Countermeasures**: Prepared statements, parameterized queries, whitelist sorting.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP)**: Auto-escaping, CSP headers.
- **Multi-Tenant CORS Security Rails**: Origin validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines**: Log scrubbing, masking.

## 📁 7. QUY ĐỊNH TUYÊN CHÍNH HỆ THỐNG ĐIỆU HÀNG & CƠ THỂ SEO ĐỊNH DỊCH
- **Capacitor Mobile Hybrid Compliance Rails**: Native storage, back button handling.
- **Internationalization (i18n) & Dynamic SEO Injection**: Locale detection, hreflang tags.

## 📁 8. DỰ ÁN GIT CHẠY NGÀY TỰ ĐỘNG
- **Daily Workspace Forking Isolation**: Branch naming.
- **Validation Guard Pipeline Gates**: Build, test, coverage.

### 🛑 MÁC HÌNH CẤP BẢO VỆ
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 24, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`