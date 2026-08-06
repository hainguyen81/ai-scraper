# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806041651 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 04:16:51 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CƠ BẢN

### 1.1. Mô Hình Kiến Trúc Cơ Bản
Mô hình kiến trúc dựa trên kiến trúc microservices, sử dụng Quarkus cho backend, PostgreSQL làm cơ sở dữ liệu quan hệ, Redis cho session caching, Firebase Authentication cho xác thực, GKE cho triển khai container, Docker multi-stage, CI/CD bằng GitHub Actions. Dữ liệu được chia thành các module: user, center, course, enrollment, attendance, studentcard, notification, promotion, chatbot, reporting, dashboard, i18n, mobile-app.

### 1.2. Kiến Trúc Dòng Dữ Liệu Doanh Nghiệp & Hệ Sinh Thái Cốt Lõi
- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT 15 phút + refresh token 7 ngày.  
- **Attendance Flow**: Mobile QR scan → API idempotent → Attendance record.  
- **Notification Flow**: Event bus → Push (FCM/APNs) + Zalo group.  
- **Data Flow**: Event-driven (Kafka) for notifications, promotions, reporting.  
- **External Integration**: Zalo API, Firebase, Google Cloud Messaging.

## 📁 2. CƠ SỞ CÔNG NGHỆ & THƯ VIỆN HỆ SỐ

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, PostgreSQL, Redis, Firebase Admin SDK, Google Cloud SDK, JUnit5, Mockito.  
- **Frontend & Cross-Platform UI Mobile Stack**: Next.js 13, React, TypeScript, Tailwind CSS, Capacitor, i18next, FCM SDK, APNs SDK.

<COMMAND>
You MUST keep this entire block 100% in raw Technical English. You are STRICTLY FORBIDDEN from translating any keys, values, or tokens inside this section into 🇻🇳 Vietnamese, as it serves as a strict backend machine-gating matrix. Keep literal `true` or `false` tokens in pure lower-case.

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```
</COMMAND>

## 📁 3. CHÂU PHÁI BẢO VỆ & THUỘC ĐỘ HỢP ĐỒNG DOANH NGHIỆP

- **Workspace Boundary**: Root repository is `.`; all paths start with `./sources/`.  
- **Dynamic Directory Prefixing**: Backend modules under `./sources/backend.<service>`, frontend under `./sources/frontend.<app>`, infra under `./sources/infra`.  
- **Java Package Standard**: `org.nlh4j.saas.membershiphub`.  
- **Tester Target Path Syntax**: `./sources/<source>;<test_suite>`.

## 4. BẢNG TỔNG QUAN KIẾN TRÚC Đa Giai Đoạn

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Day 1-7 | ./sources/backend/user-service, ./sources/backend/center-service, ./sources/backend/security, ./sources/backend/database | Tạo schema, API đăng ký, đăng nhập, quản lý trung tâm, RBAC, tài liệu API | Coder | [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [EXC-004], [NFR-003] |
| 2 | Day 1-7 | ./sources/backend/course-service, ./sources/backend/enrollment-service, ./sources/backend/attendance-service, ./sources/backend/studentcard-service | CRUD khóa học, ghi danh, điểm danh, thẻ hội viên, exception handling, unit tests | Coder | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007], [ARC-008], [ARC-009], [EXC-001], [EXC-002], [EXC-004], [NFR-001], [NFR-002], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| 3 | Day 1-7 | ./sources/backend/notification-service, ./sources/backend/promotion-service, ./sources/backend/chatbot-service, ./sources/frontend/mobile-app | Thông báo, khuyến mãi, chatbot, UI mobile, localization, SEO | Coder | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [ARC-010], [ARC-009], [EXC-003], [NFR-003] |
| 4 | Day 1-7 | ./sources/backend/reporting-service, ./sources/backend/dashboard-service, ./sources/backend/i18n, ./sources/frontend/mobile-app/components | Báo cáo điểm danh, dashboard, localization middleware, SEO meta tags | Coder | [REQ-024], [REQ-025], [REQ-022], [REQ-023], [EXC-005], [NFR-001], [NFR-002], [NFR-004] |
| 5 | Day 1-7 | ./sources/backend/*/Dockerfile, ./sources/infra/k8s, ./sources/infra/gcp, ./sources/infra/github-actions | Docker images, GKE deployments, Cloud Build, CI/CD pipeline | Docker | [ARC-010], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 5. ĐẶT CHỈ ĐẶC ĐIỂM KIẾN TRÚC CHI TIẾT MỖI GIAI ĐOẠN

### 📈 Giai đoạn 1: Kiến trúc cơ bản và xác thực

- **Mục tiêu cốt lõi & mục đích**: Thiết lập cơ sở dữ liệu, API đăng ký/đăng nhập, quản lý trung tâm, RBAC, tài liệu API.  
- **Bản đồ thư mục vật lý**:  
  - `./sources/backend/database/migration/001_create_tables.sql [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]`  
  - `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserRegistrationService.java [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006]`  
  - `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java [REQ-004], [REQ-005], [REQ-006], [ARC-004], [ARC-005]`  
  - `./sources/backend/security/RBACFilter.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]`  
  - `./sources/docs/api/user-api.md; ./sources/docs/api/center-api.md [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]`  
  - `./sources/backend/user-service/src/test/java/org/nlh4j/saas/membershiphub/user/UserRegistrationServiceTest.java; ./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserRegistrationService.java [REQ-001], [REQ-002], [REQ-003], [EXC-004]`  
  - `./sources/backend/security/SecurityConfig.java [ARC-006], [NFR-003]`  
- **DDL SQL**:  
  ```sql
  CREATE TABLE USERS (
      userId UUID PRIMARY KEY,
      email VARCHAR(255) NOT NULL UNIQUE,
      passwordHash CHAR(60) NOT NULL,
      fullName VARCHAR(100) NOT NULL,
      roleId SMALLINT NOT NULL,
      provider VARCHAR(20) NOT NULL DEFAULT 'local',
      createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
      updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
  );
  CREATE TABLE ROLES (
      roleId SMALLINT PRIMARY KEY,
      name VARCHAR(30) NOT NULL UNIQUE,
      description VARCHAR(200)
  );
  CREATE TABLE CENTERS (
      centerId UUID PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      address VARCHAR(255) NOT NULL,
      taxId VARCHAR(13) NOT NULL UNIQUE,
      contactPhone VARCHAR(50),
      contactEmail VARCHAR(255)
  );
  CREATE TABLE COURSES (
      courseId UUID PRIMARY KEY,
      title VARCHAR(150) NOT NULL,
      description TEXT,
      startDate DATE NOT NULL,
      endDate DATE NOT NULL,
      teacherId UUID,
      maxStudents INT DEFAULT 30
  );
  CREATE TABLE ENROLLMENTS (
      enrollmentId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      courseId UUID NOT NULL,
      enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW()
  );
  CREATE TABLE ATTENDANCE (
      attendanceId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      courseId UUID NOT NULL,
      attendanceDate DATE NOT NULL,
      timestamp TIMESTAMP NOT NULL DEFAULT NOW()
  );
  CREATE TABLE STUDENTCARDS (
      cardId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      issueDate DATE NOT NULL,
      validityDays INT NOT NULL,
      remainingDays INT NOT NULL
  );
  CREATE TABLE NOTIFICATIONS (
      notificationId UUID PRIMARY KEY,
      userId UUID,
      groupZalo VARCHAR(255),
      message TEXT NOT NULL,
      sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
      delivered BOOLEAN NOT NULL DEFAULT FALSE
  );
  CREATE TABLE PROMOTIONS (
      promoId UUID PRIMARY KEY,
      code VARCHAR(50) NOT NULL UNIQUE,
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
  CREATE TABLE SYSTEMSETTINGS (
      settingKey VARCHAR(100) PRIMARY KEY,
      settingValue TEXT NOT NULL,
      description VARCHAR(200)
  );
  ```
- **API Contracts**:  
  - `POST /api/auth/register` → `{email, password, provider}` → `{token, user}`.  
  - `POST /api/auth/login` → `{email, password}` → `{token, user}`.  
  - `GET /api/centers` → `{centers}`.  
  - `POST /api/centers` → `{name, address, taxId, contactPhone, contactEmail}` → `{center}`.  
  - `PUT /api/centers/{id}` → `{name, address, taxId, contactPhone, contactEmail}` → `{center}`.  
  - `DELETE /api/centers/{id}` → `{status}`.  
  - `PUT /api/users/{id}/role` → `{roleId}` → `{user}`.  
- **Exception Handlers**:  
  - `EXC-004`: ValidationException → 400 Bad Request with field errors.  
  - `EXC-001`: NetworkError → 503 Service Unavailable.  
  - `EXC-002`: DuplicateAttendanceException → 409 Conflict.  
  - `EXC-003`: NotificationDeliveryException → 502 Bad Gateway.  
  - `EXC-005`: ReportingDataError → 500 Internal Server Error.  

#### 📅 Lịch trình ngày theo ngày (Giai đoạn 1)

- **DAY 1**: Thiết lập schema database.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/database/migration/001_create_tables.sql [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]`  
      - **Low-Level Technical Task Instruction**: Viết câu lệnh DDL cho tất cả bảng, đảm bảo khóa chính, khóa ngoại, chỉ mục, và ràng buộc NOT NULL.  
      - **Targeted Tag IDs**: [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]  

- **DAY 2**: Xây dựng API đăng ký/đăng nhập.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserRegistrationService.java [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006]`  
      - **Low-Level Technical Task Instruction**: Cài đặt logic đăng ký, xác thực OAuth2, tạo JWT, lưu user, trả về token.  
      - **Targeted Tag IDs**: [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006]  

- **DAY 3**: Xây dựng API quản lý trung tâm.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java [REQ-004], [REQ-005], [REQ-006], [ARC-004], [ARC-005]`  
      - **Low-Level Technical Task Instruction**: CRUD trung tâm, kiểm tra trùng taxId, trả về danh sách.  
      - **Targeted Tag IDs**: [REQ-004], [REQ-005], [REQ-006], [ARC-004], [ARC-005]  

- **DAY 4**: Cài đặt RBAC filter.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/security/RBACFilter.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]`  
      - **Low-Level Technical Task Instruction**: Kiểm tra role, phân quyền, trả 403 nếu không đủ.  
      - **Targeted Tag IDs**: [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]  

- **DAY 5**: Viết tài liệu API.  
  * **Sub-Agent Workflow Specialization**:  
    - **Doc**:  
      - **Target Component file path**: `./sources/docs/api/user-api.md; ./sources/docs/api/center-api.md [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]`  
      - **Low-Level Technical Task Instruction**: Mô tả endpoint, request/response, status code, ví dụ JSON.  
      - **Targeted Tag IDs**: [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]  

- **DAY 6**: Viết unit test đăng ký.  
  * **Sub-Agent Workflow Specialization**:  
    - **Tester**:  
      - **Target Component file path**: `./sources/backend/user-service/src/test/java/org/nlh4j/saas/membershiphub/user/UserRegistrationServiceTest.java; ./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserRegistrationService.java [REQ-001], [REQ-002], [REQ-003], [EXC-004]`  
      - **Low-Level Technical Task Instruction**: Mock Firebase, kiểm tra trường hợp thành công và lỗi.  
      - **Targeted Tag IDs**: [REQ-001], [REQ-002], [REQ-003], [EXC-004]  

- **DAY 7**: Review bảo mật.  
  * **Sub-Agent Workflow Specialization**:  
    - **Reviewer**:  
      - **Target Component file path**: `./sources/backend/security/SecurityConfig.java [ARC-006], [NFR-003]`  
      - **Low-Level Technical Task Instruction**: Kiểm tra TLS, JWT expiration, refresh token logic.  
      - **Targeted Tag IDs**: [ARC-006], [NFR-003]  

### 📈 Giai đoạn 2: Quản lý khóa học, ghi danh, điểm danh, thẻ hội viên

- **Mục tiêu cốt lõi & mục đích**: Xây dựng CRUD khóa học, ghi danh, điểm danh, thẻ hội viên, exception handling, unit tests.  
- **Bản đồ thư mục vật lý**:  
  - `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseController.java [REQ-007], [REQ-008], [REQ-009], [ARC-008], [ARC-009]`  
  - `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java [REQ-010], [REQ-011], [ARC-009]`  
  - `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceController.java [REQ-012], [REQ-013], [ARC-007], [ARC-009]`  
  - `./sources/backend/studentcard-service/src/main/java/org/nlh4j/saas/membershiphub/studentcard/StudentCardService.java [REQ-014], [REQ-015], [ARC-009]`  
  - `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceExceptionHandler.java [EXC-001], [EXC-002]`  
  - `./sources/backend/enrollment-service/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentControllerTest.java; ./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java [REQ-010], [REQ-011], [EXC-004]`  
  - `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java [ARC-007], [ARC-009]`  
- **API Contracts**:  
  - `GET /api/courses` → `{courses}`.  
  - `POST /api/courses` → `{title, startDate, endDate, teacherId, maxStudents}` → `{course}`.  
  - `PUT /api/courses/{id}` → `{title, startDate, endDate, teacherId, maxStudents}` → `{course}`.  
  - `DELETE /api/courses/{id}` → `{status}`.  
  - `POST /api/enrollments` → `{studentId, courseId}` → `{enrollment}`.  
  - `POST /api/attendance` → `{studentId, courseId}` → `{attendance}`.  
- **Exception Handlers**:  
  - `EXC-001`: NetworkError → 503.  
  - `EXC-002`: DuplicateAttendanceException → 409.  
  - `EXC-004`: ValidationException → 400.  
  - `EXC-005`: ReportingDataError → 500.  

#### 📅 Lịch trình ngày theo ngày (Giai đoạn 2)

- **DAY 1**: CRUD khóa học.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseController.java [REQ-007], [REQ-008], [REQ-009], [ARC-008], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Xây dựng endpoint, kiểm tra trùng lịch, trả về lỗi 409 khi xung đột.  
      - **Targeted Tag IDs**: [REQ-007], [REQ-008], [REQ-009], [ARC-008], [ARC-009]  

- **DAY 2**: Ghi danh học viên.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java [REQ-010], [REQ-011], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Kiểm tra tồn tại học viên, tạo enrollment, trả về 201.  
      - **Targeted Tag IDs**: [REQ-010], [REQ-011], [ARC-009]  

- **DAY 3**: Điểm danh QR.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceController.java [REQ-012], [REQ-013], [ARC-007], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Kiểm tra quan hệ student-course, idempotent, tạo attendance.  
      - **Targeted Tag IDs**: [REQ-012], [REQ-013], [ARC-007], [ARC-009]  

- **DAY 4**: Thẻ hội viên.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/studentcard-service/src/main/java/org/nlh4j/saas/membershiphub/studentcard/StudentCardService.java [REQ-014], [REQ-015], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Tính toán remainingDays, cập nhật endDate, trả về card.  
      - **Targeted Tag IDs**: [REQ-014], [REQ-015], [ARC-009]  

- **DAY 5**: Exception handling attendance.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceExceptionHandler.java [EXC-001], [EXC-002]`  
      - **Low-Level Technical Task Instruction**: Định nghĩa exception handler, trả 503/409.  
      - **Targeted Tag IDs**: [EXC-001], [EXC-002]  

- **DAY 6**: Unit test ghi danh.  
  * **Sub-Agent Workflow Specialization**:  
    - **Tester**:  
      - **Target Component file path**: `./sources/backend/enrollment-service/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentControllerTest.java; ./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java [REQ-010], [REQ-011], [EXC-004]`  
      - **Low-Level Technical Task Instruction**: Mock repository, kiểm tra thành công và lỗi.  
      - **Targeted Tag IDs**: [REQ-010], [REQ-011], [EXC-004]  

- **DAY 7**: Review idempotency.  
  * **Sub-Agent Workflow Specialization**:  
    - **Reviewer**:  
      - **Target Component file path**: `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java [ARC-007], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Kiểm tra logic idempotent, tránh duplicate.  
      - **Targeted Tag IDs**: [ARC-007], [ARC-009]  

### 📈 Giai đoạn 3: Thông báo, khuyến mãi, chatbot, UI mobile

- **Mục tiêu cốt lõi & mục đích**: Xây dựng dịch vụ thông báo, khuyến mãi, chatbot, UI mobile, localization, SEO.  
- **Bản đồ thư mục vật lý**:  
  - `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [ARC-008], [ARC-009]`  
  - `./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionController.java [REQ-017], [REQ-018], [ARC-009]`  
  - `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java [REQ-019], [ARC-009]`  
  - `./sources/frontend/mobile-app/pages/index.js; ./sources/frontend/mobile-app/pages/attendance.js [REQ-020], [REQ-021], [ARC-009]`  
  - `./sources/frontend/mobile-app/i18n/vi.js; ./sources/frontend/mobile-app/i18n/en.js; ./sources/frontend/mobile-app/i18n/es.js; ./sources/frontend/mobile-app/seo-config.js [REQ-022], [REQ-023], [ARC-009]`  
  - `./sources/backend/notification-service/src/test/java/org/nlh4j/saas/membershiphub/notification/NotificationServiceTest.java; ./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [EXC-003]`  
  - `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [ARC-010], [NFR-003]`  
- **API Contracts**:  
  - `POST /api/notifications` → `{userId, groupZalo, message}` → `{notification}`.  
  - `POST /api/promotions` → `{code, discountPercent, startDate, endDate, description}` → `{promotion}`.  
  - `POST /api/chatbot` → `{message}` → `{response}`.  
- **Exception Handlers**:  
  - `EXC-003`: NotificationDeliveryException → 502.  

#### 📅 Lịch trình ngày theo ngày (Giai đoạn 3)

- **DAY 1**: Dịch vụ thông báo.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [ARC-008], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Xây dựng logic gửi push, lưu notification, queue.  
      - **Targeted Tag IDs**: [REQ-016], [ARC-008], [ARC-009]  

- **DAY 2**: CRUD khuyến mãi.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionController.java [REQ-017], [REQ-018], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Xây dựng endpoint, kiểm tra trùng code, trả 409.  
      - **Targeted Tag IDs**: [REQ-017], [REQ-018], [ARC-009]  

- **DAY 3**: Chatbot integration.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java [REQ-019], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Gọi API AI, trả lời, fallback.  
      - **Targeted Tag IDs**: [REQ-019], [ARC-009]  

- **DAY 4**: UI mobile pages.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/frontend/mobile-app/pages/index.js; ./sources/frontend/mobile-app/pages/attendance.js [REQ-020], [REQ-021], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Xây dựng component, gọi API, hiển thị dữ liệu.  
      - **Targeted Tag IDs**: [REQ-020], [REQ-021], [ARC-009]  

- **DAY 5**: Localization & SEO.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/frontend/mobile-app/i18n/vi.js; ./sources/frontend/mobile-app/i18n/en.js; ./sources/frontend/mobile-app/i18n/es.js; ./sources/frontend/mobile-app/seo-config.js [REQ-022], [REQ-023], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Cấu hình i18next, meta tags, hreflang.  
      - **Targeted Tag IDs**: [REQ-022], [REQ-023], [ARC-009]  

- **DAY 6**: Unit test thông báo.  
  * **Sub-Agent Workflow Specialization**:  
    - **Tester**:  
      - **Target Component file path**: `./sources/backend/notification-service/src/test/java/org/nlh4j/saas/membershiphub/notification/NotificationServiceTest.java; ./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [EXC-003]`  
      - **Low-Level Technical Task Instruction**: Mock FCM, kiểm tra thành công/không.  
      - **Targeted Tag IDs**: [REQ-016], [EXC-003]  

- **DAY 7**: Review push integration.  
  * **Sub-Agent Workflow Specialization**:  
    - **Reviewer**:  
      - **Target Component file path**: `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [ARC-010], [NFR-003]`  
      - **Low-Level Technical Task Instruction**: Kiểm tra TLS, retry logic.  
      - **Targeted Tag IDs**: [ARC-010], [NFR-003]  

### 📈 Giai đoạn 4: Báo cáo, dashboard, localization, SEO

- **Mục tiêu cốt lõi & mục đích**: Xây dựng báo cáo điểm danh, dashboard, middleware localization, SEO meta tags.  
- **Bản đồ thư mục vật lý**:  
  - `./sources/backend/reporting-service/src/main/java/org/nlh4j/saas/membershiphub/reporting/AttendanceReportController.java [REQ-024], [ARC-009]`  
  - `./sources/backend/dashboard-service/src/main/java/org/nlh4j/saas/membershiphub/dashboard/DashboardController.java [REQ-025], [ARC-009]`  
  - `./sources/backend/i18n/LocaleFilter.java [REQ-022], [ARC-009]`  
  - `./sources/frontend/mobile-app/components/MetaTags.js [REQ-023], [ARC-009]`  
  - `./sources/backend/reporting-service/src/test/java/org/nlh4j/saas/membershiphub/reporting/AttendanceReportControllerTest.java; ./sources/backend/reporting-service/src/main/java/org/nlh4j/saas/membershiphub/reporting/AttendanceReportController.java [REQ-024], [EXC-005]`  
  - `./sources/backend/reporting-service/src/main/java/org/nlh4j/saas/membershiphub/reporting/AttendanceReportService.java [NFR-001], [NFR-002]`  
- **API Contracts**:  
  - `GET /api/reporting/attendance?centerId=&date=` → `{csv}`.  
  - `GET /api/dashboard` → `{totalStudents, activeCourses, upcomingSessions}`.  
- **Exception Handlers**:  
  - `EXC-005`: ReportingDataError → 500.  

#### 📅 Lịch trình ngày theo ngày (Giai đoạn 4)

- **DAY 1**: Báo cáo điểm danh.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/reporting-service/src/main/java/org/nlh4j/saas/membershiphub/reporting/AttendanceReportController.java [REQ-024], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Xây dựng endpoint, xuất CSV, filter.  
      - **Targeted Tag IDs**: [REQ-024], [ARC-009]  

- **DAY 2**: Dashboard.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/dashboard-service/src/main/java/org/nlh4j/saas/membershiphub/dashboard/DashboardController.java [REQ-025], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Tính toán tổng, active, upcoming.  
      - **Targeted Tag IDs**: [REQ-025], [ARC-009]  

- **DAY 3**: Middleware localization.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/backend/i18n/LocaleFilter.java [REQ-022], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Đọc cookie, header, fallback.  
      - **Targeted Tag IDs**: [REQ-022], [ARC-009]  

- **DAY 4**: SEO meta tags.  
  * **Sub-Agent Workflow Specialization**:  
    - **Coder**:  
      - **Target Component file path**: `./sources/frontend/mobile-app/components/MetaTags.js [REQ-023], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Thêm meta, hreflang.  
      - **Targeted Tag IDs**: [REQ-023], [ARC-009]  

- **DAY 5**: Unit test báo cáo.  
  * **Sub-Agent Workflow Specialization**:  
    - **Tester**:  
      - **Target Component file path**: `./sources/backend/reporting-service/src/test/java/org/nlh4j/saas/membershiphub/reporting/AttendanceReportControllerTest.java; ./sources/backend/reporting-service/src/main/java/org/nlh4j/saas/membershiphub/reporting/AttendanceReportController.java [REQ-024], [EXC-005]`  
      - **Low-Level Technical Task Instruction**: Mock repo, kiểm tra CSV.  
      - **Targeted Tag IDs**: [REQ-024], [EXC-005]  

- **DAY 6**: Review performance.  
  * **Sub-Agent Workflow Specialization**:  
    - **Reviewer**:  
      - **Target Component file path**: `./sources/backend/reporting-service/src/main/java/org/nlh4j/saas/membershiphub/reporting/AttendanceReportService.java [NFR-001], [NFR-002]`  
      - **Low-Level Technical Task Instruction**: Kiểm tra độ trễ, index.  
      - **Targeted Tag IDs**: [NFR-001], [NFR-002]  

- **DAY 7**: Review dashboard logic.  
  * **Sub-Agent Workflow Specialization**:  
    - **Reviewer**:  
      - **Target Component file path**: `./sources/backend/dashboard-service/src/main/java/org/nlh4j/saas/membershiphub/dashboard/DashboardController.java [REQ-025], [ARC-009]`  
      - **Low-Level Technical Task Instruction**: Kiểm tra tính đúng dữ liệu.  
      - **Targeted Tag IDs**: [REQ-025], [ARC-009]  

### 📈 Giai đoạn 5: DevOps, CI/CD, GKE, Docker

- **Mục tiêu cốt lõi & mục đích**: Xây dựng Docker images, GKE deployments, Cloud Build, CI/CD pipeline.  
- **Bản đồ thư mục vật lý**:  
  - `./sources/backend/user-service/Dockerfile [ARC-010], [NFR-005]`  
  - `./sources/backend/center-service/Dockerfile [ARC-010], [NFR-005]`  
  - `./sources/backend/course-service/Dockerfile [ARC-010], [NFR-005]`  
  - `./sources/infra/k8s/user-service-deployment.yaml [ARC-010], [NFR-004]`  
  - `./sources/infra/k8s/center-service-deployment.yaml [ARC-010], [NFR-004]`  
  - `./sources/infra/gcp/cloudbuild.yaml [ARC-010], [NFR-006]`  
  - `./sources/infra/github-actions/ci.yml [ARC-010], [NFR-007], [NFR-008], [NFR-009]`  
- **Exception Handlers**: None specific.  

#### 📅 Lịch trình ngày theo ngày (Giai đoạn 5)

- **DAY 1**: Dockerfile user-service.  
  * **Sub-Agent Workflow Specialization**:  
    - **Docker**:  
      - **Target Component file path**: `./sources/backend/user-service/Dockerfile [ARC-010], [NFR-005]`  
      - **Low-Level Technical Task Instruction**: Multi-stage build, copy JAR, set entrypoint.  
      - **Targeted Tag IDs**: [ARC-010], [NFR-005]  

- **DAY 2**: Dockerfile center-service.  
  * **Sub-Agent Workflow Specialization**:  
    - **Docker**:  
      - **Target Component file path**: `./sources/backend/center-service/Dockerfile [ARC-010], [NFR-005]`  
      - **Low-Level Technical Task Instruction**: Build image, tag.  
      - **Targeted Tag IDs**: [ARC-010], [NFR-005]  

- **DAY 3**: Dockerfile course-service.  
  * **Sub-Agent Workflow Specialization**:  
    - **Docker**:  
      - **Target Component file path**: `./sources/backend/course-service/Dockerfile [ARC-010], [NFR-005]`  
      - **Low-Level Technical Task Instruction**: Build image, push.  
      - **Targeted Tag IDs**: [ARC-010], [NFR-005]  

- **DAY 4**: GKE deployment user-service.  
  * **Sub-Agent Workflow Specialization**:  
    - **GKE**:  
      - **Target Component file path**: `./sources/infra/k8s/user-service-deployment.yaml [ARC-010], [NFR-004]`  
      - **Low-Level Technical Task Instruction**: Define deployment, service, HPA.  
      - **Targeted Tag IDs**: [ARC-010], [NFR-004]  

- **DAY 5**: GKE deployment center-service.  
  * **Sub-Agent Workflow Specialization**:  
    - **GKE**:  
      - **Target Component file path**: `./sources/infra/k8s/center-service-deployment.yaml [ARC-010], [NFR-004]`  
      - **Low-Level Technical Task Instruction**: Deployment, service, HPA.  
      - **Targeted Tag IDs**: [ARC-010], [NFR-004]  

- **DAY 6**: Cloud Build config.  
  * **Sub-Agent Workflow Specialization**:  
    - **GCP**:  
      - **Target Component file path**: `./sources/infra/gcp/cloudbuild.yaml [ARC-010], [NFR-006]`  
      - **Low-Level Technical Task Instruction**: Build steps, push to Artifact Registry.  
      - **Targeted Tag IDs**: [ARC-010], [NFR-006]  

- **DAY 7**: CI/CD pipeline.  
  * **Sub-Agent Workflow Specialization**:  
    - **GCP**:  
      - **Target Component file path**: `./sources/infra/github-actions/ci.yml [ARC-010], [NFR-007], [NFR-008], [NFR-009]`  
      - **Low-Level Technical Task Instruction**: Triggers, jobs, test, build, deploy.  
      - **Targeted Tag IDs**: [ARC-010], [NFR-007], [NFR-008], [NFR-009]  

## 📁 6. Mã Bảo Mật Toàn Cục & Biện Pháp Phòng Ngừa XSS, SQLi, CORS

- **SQL Injection (SQLi) Countermeasures**: Sử dụng prepared statements, parameterized queries, whitelist các tham số sắp xếp.  
- **Cross-Site Scripting (XSS) & CSP**: Escape nội dung, CSP header `default-src 'self'; script-src 'self'; style-src 'self';`  
- **CORS Security**: Origin whitelist, dynamic tenant origin validation, `Access-Control-Allow-Origin` chỉ cho domain hợp lệ.  
- **Log Scrubbing**: Mask PII trong logs, sử dụng `@JsonSerialize` để mask, giới hạn độ dài.  

## 📁 7. Quy tắc Tuân thủ Mobile Hybrid & SEO

- **Capacitor Mobile Compliance**: Sử dụng `@capacitor/preferences` cho lưu trữ, intercept back button, URL deep linking.  
- **i18n & SEO**: Middleware `LocaleFilter`, meta tags, `hreflang` dynamic, robots.txt.  

## 📁 8. Quy trình Git Branch & CI

- **Daily Workspace Forking**: Branch `features/development-phase-X-day-Y`.  
- **Validation Gates**: Compile, test coverage ≥ 85%, lint, security scan.  

### 🛑 Kiểm tra Bảo mật

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 10, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`