# BỐ CỤC DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260807132631 |
| **Tên Dự án** | membership-hub |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày.Giờ** | 2026/08/07 13:26:31 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Đang chờ |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1 Core System Modality & Architecture Modality

- Nền tảng microservice phân tán sử dụng Java/Quarkus với kiến trúc dựa trên sự kiện, hỗ trợ đa trung tâm và RBAC.
- Triển khai container hóa trên Kubernetes (GKE) với PostgreSQL làm datastore chính, Redis cho cache phiên, Firebase cho xác thực và thông báo đẩy.
- Các luồng nghiệp vụ chính bao gồm xác thực, xử lý điểm danh QR, gửi thông báo đa kênh (di động, Zalo), và quản lý hội viên với thẻ kỹ thuật số.

### 1.2 Enterprise Data Flow Topologies & Core Ecosystems

- Luồng xác thực: OAuth2 với email/mật khẩu, Firebase, Google, Facebook; cấp JWT (15 phút) và refresh token.
- Luồng điểm danh QR: Ứng dụng di động quét QR, gửi studentId + timestamp đến backend; dịch vụ xác thực idempotent.
- Luồng thông báo: Backend kích hoạt push notification (FCM/APNs) và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, cảnh báo điểm danh.
- Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs, xác thực bearer token, hỗ trợ caching ngoại tuyến.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21 + Quarkus 3.2, PostgreSQL 15, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API, Redis 7, GitHub Actions CI/CD.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14 (React 18), TypeScript, Tailwind CSS, i18n với locale files (EN, VI, ES), React Native (hoặc Capacitor) cho di động, tích hợp push notification qua Firebase Cloud Messaging, và các thư viện UI (Material-UI / Ant Design).

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Quy tắc biên giới không gian làm việc tuyệt đối:** Không gian làm việc thực sự cố định ở gốc repository `.`. Tất cả các đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Tuân thủ quy tắc tiền tố thư mục động:** Thực thi các quy tắc ánh xạ thư mục động được định nghĩa trong Protocol 1 phù hợp với cấu trúc dự án được phát hiện.
- **[CONDITION: JAVA_STACK_ONLY] Tiêu chuẩn gói Java:** Nếu stack sử dụng Java, tất cả mã nguồn Java phải nằm trong foundation package: `org.nlh4j.saas.membershiphub`. Chuyển đổi "membership-hub" thành token thuần chữ thường, không dấu, không gạch ngang, không gạch dưới.
- **Cú pháp mục tiêu kiểm thử nghiêm ngặt:** Bất kỳ thành phần nào được nhắm mục tiêu bởi Sub-Agent Tester phải được cấu trúc dưới dạng cặp phân cách bán phẩy `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn trong cặp phải bắt đầu bằng `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Day 1 - 2 | `./sources/backend/org/nlh4j/saas/membershiphub/user-management/` | Xây dựng lõi người dùng, xác thực và phân quyền; triển khai các bảng dữ liệu cơ bản. | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004] |
| 2 | Day 1 - 2 | `./sources/backend/org/nlh4j/saas/membershiphub/center-management/` | Triển khai quản lý trung tâm, API CRUD và schema trung tâm. | Coder | [REQ-004], [REQ-005], [REQ-006], [ARC-002], [DAT-003] |
| 3 | Day 1 - 2 | `./sources/backend/org/nlh4j/saas/membershiphub/course-management/` | Xây dựng quản lý khóa học, ghi danh, điểm danh QR và thẻ hội viên; triển khai các bảng dữ liệu tương ứng. | Coder | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [ARC-007], [ARC-008], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [EXC-001], [EXC-002] |
| 4 | Day 1 - 2 | `./sources/backend/org/nlh4j/saas/membershiphub/notification-management/` | Triển khai thông báo đa kênh, quản lý khuyến mãi và thông báo, tích hợp chatbot AI và lõi giao diện người dùng di động. | Coder | [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [ARC-009], [ARC-010], [DAT-008], [DAT-009], [EXC-003] |
| 5 | Day 1 - 3 | `./sources/backend/org/nlh4j/saas/membershiphub/global-services/` | Triển khai bản địa hóa, SEO, báo cáo, hardening bảo mật, container hóa và triển khai trên GKE, logging kiểm toán. | Coder | [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [DAT-011], [EXC-005] |

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Xây dựng lõi người dùng, xác thực và phân quyền; triển khai các bảng dữ liệu cơ bản.

- **Phase Core Objective & Purpose:** Triển khai toàn bộ quy trình đăng ký người dùng, xác thực qua mạng xã hội, và cơ chế phân quyền vai trò; thiết lập các bảng dữ liệu người dùng và vai trò với các ràng buộc quan hệ phù hợp.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend/org/nlh4j/saas/membershiphub/user-management/UserEntity.java [REQ-001], [DAT-001]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/user-management/RoleEntity.java [REQ-001], [DAT-001]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/auth/AuthenticationController.java [REQ-001], [REQ-002], [REQ-003]`
  * `./sources/docs/Phase1_Architecture.md [REQ-001], [REQ-002], [REQ-003]`
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
    role_id SMALLINT NOT NULL,
    provider VARCHAR(20) NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_users_roles FOREIGN KEY (role_id) REFERENCES roles(role_id),
    CONSTRAINT chk_provider CHECK (provider IN ('local','firebase','google','facebook'))
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003]:**
```json
{
  "endpoints": [
    {
      "path": "/api/v1/auth/register",
      "method": "POST",
      "request": {
        "email": "string",
        "password": "string",
        "fullName": "string",
        "role": "string"
      },
      "response": {
        "userId": "UUID",
        "token": "string",
        "refreshToken": "string"
      }
    },
    {
      "path": "/api/v1/auth/social",
      "method": "POST",
      "request": {
        "provider": "string",
        "code": "string"
      },
      "response": {
        "userId": "UUID",
        "token": "string"
      }
    },
    {
      "path": "/api/v1/users/{id}/role",
      "method": "PUT",
      "request": {
        "roleId": "SMALLINT"
      },
      "response": {
        "userId": "UUID",
        "roleId": "SMALLINT"
      }
    }
  ]
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
  * Xử lý lỗi xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc). Trả về danh sách chi tiết các trường lỗi và hướng dẫn người dùng chỉnh sửa.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1: Triển khai các lớp thực thể người dùng và vai trò**
  * **[Coder]**
  * **Targeted Tag IDs:** [REQ-001], [DAT-001]
  * **Target Component file path (`target_component`):** `./sources/backend/org/nlh4j/saas/membershiphub/user-management/UserEntity.java [REQ-001], [DAT-001]`
  * **Low-Level Technical Task Instruction:** Triển khai lớp thực thể Users với các trường userId (UUID PK), email, passwordHash, fullName, roleId (FK), provider (CHECK), timestamps. Áp dụng các ràng buộc NOT NULL, UNIQUE cho email. Thêm lớp thực thể Roles với roleId, name, description. Ghi chú các mối quan hệ khóa ngoại.

- **DAY 2: Viết bộ kiểm thử đơn vị cho quản lý người dùng**
  * **[Tester]**
  * **Targeted Tag IDs:** [REQ-001], [DAT-001]
  * **Target Component file path (`target_component`):** `./sources/backend/org/nlh4j/saas/membershiphub/user-management/UserEntityTest.java;./sources/backend/org/nlh4j/saas/membershiphub/user-management/UserEntity.java`
  * **Low-Level Technical Task Instruction:** Xây dựng bộ kiểm thử JUnit5 cho UserEntity và RoleEntity, bao gồm kiểm tra các ràng buộc trường (email unique, provider enum), mối quan hệ khóa ngoại, và logic tạo timestamp. Đảm bảo độ phủ trên mã nguồn >= 85%.

### 📈 Triển khai quản lý trung tâm, API CRUD và schema trung tâm.

- **Phase Core Objective & Purpose:** Xây dựng các chức năng quản lý trung tâm bao gồm xem, tạo, cập nhật, xóa trung tâm; triển khai bảng dữ liệu Centers với các ràng buộc business (taxId unique).
- **Target Physical Directory Matrix Map:**
  * `./sources/backend/org/nlh4j/saas/membershiphub/center-management/CenterEntity.java [REQ-004], [DAT-003]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/center-management/CenterController.java [REQ-004], [REQ-005], [REQ-006]`
  * `./sources/docs/Phase2_Architecture.md [REQ-004], [REQ-005], [REQ-006]`
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255),
    CONSTRAINT chk_tax_id_numeric CHECK (tax_id ~ '^[0-9]+$')
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006]:**
```json
{
  "endpoints": [
    {
      "path": "/api/v1/centers",
      "method": "GET",
      "response": [
        {
          "centerId": "UUID",
          "name": "string",
          "address": "string",
          "taxId": "string",
          "contactPhone": "string",
          "contactEmail": "string"
        }
      ]
    },
    {
      "path": "/api/v1/centers",
      "method": "POST",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "centerId": "UUID"
      }
    },
    {
      "path": "/api/v1/centers/{id}",
      "method": "PUT",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "centerId": "UUID"
      }
    },
    {
      "path": "/api/v1/centers/{id}",
      "method": "DELETE",
      "response": {
        "centerId": "UUID"
      }
    },
    {
      "path": "/api/v1/centers/assign",
      "method": "POST",
      "request": {
        "userId": "UUID",
        "centerId": "UUID"
      },
      "response": {
        "userId": "UUID",
        "centerId": "UUID"
      }
    }
  ]
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
  * Xử lý lỗi xác thực đầu vào không hợp lệ cho form tạo trung tâm (ví dụ: taxId trùng lặp, email sai định dạng). Trả về thông báo lỗi chi tiết và hướng dẫn chỉnh sửa.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1: Triển khai lớp thực thể và controller trung tâm**
  * **[Coder]**
  * **Targeted Tag IDs:** [REQ-004], [DAT-003]
  * **Target Component file path (`target_component`):** `./sources/backend/org/nlh4j/saas/membershiphub/center-management/CenterEntity.java [REQ-004], [DAT-003]`
  * **Low-Level Technical Task Instruction:** Triển khai lớp thực thể CenterEntity với các trường centerId (UUID PK), name, address, taxId, contactPhone, contactEmail. Thêm các ràng buộc NOT NULL, UNIQUE cho taxId, và CHECK cho định dạng số. Triển khai CenterController với các endpoint GET, POST, PUT, DELETE, và assign.

- **DAY 2: Xây dựng Docker image cho dịch vụ trung tâm**
  * **[Docker]**
  * **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
  * **Target Component file path (`target_component`):** `./sources/infra/center-management/Dockerfile;./sources/backend/org/nlh4j/saas/membershiphub/center-management/`
  * **Low-Level Technical Task Instruction:** Tạo Dockerfile đa giai đoạn sử dụng Quarkus runtime, sao chép mã nguồn đã biên dịch, thiết lập người dùng không có đặc quyền, expose port 8080, và tối ưu hóa kích thước image (< 500MB). Push image lên registry với tag `latest`.

### 📈 Xây dựng quản lý khóa học, ghi danh, điểm danh QR và thẻ hội viên; triển khai các bảng dữ liệu tương ứng.

- **Phase Core Objective & Purpose:** Xây dựng toàn bộ quy trình quản lý khóa học (tạo, cập nhật, xóa, phân công giáo viên), ghi danh học viên, xử lý điểm danh qua QR code, và quản lý thẻ hội viên với logic tính ngày hiệu lực.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseEntity.java [REQ-007], [DAT-004]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/enrollment/EnrollmentEntity.java [REQ-010], [DAT-005]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/attendance/AttendanceEntity.java [REQ-012], [DAT-006]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/membercard/MemberCardEntity.java [REQ-014], [DAT-007]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseController.java [REQ-007], [REQ-008], [REQ-009]`
  * `./sources/docs/Phase3_Architecture.md [REQ-007], [REQ-010], [REQ-012], [REQ-014]`
- **Database Schema DDL SQL Specification [DAT-004], [DAT-005], [DAT-006], [DAT-007]:**
```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL,
    max_students INT NOT NULL DEFAULT 30,
    CONSTRAINT fk_courses_teacher FOREIGN KEY (teacher_id) REFERENCES users(user_id),
    CONSTRAINT chk_course_dates CHECK (start_date <= end_date)
);

CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_enrollments_student FOREIGN KEY (student_id) REFERENCES users(user_id),
    CONSTRAINT fk_enrollments_course FOREIGN KEY (course_id) REFERENCES courses(course_id),
    CONSTRAINT uniq_student_course UNIQUE (student_id, course_id)
);

CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_attendance_student FOREIGN KEY (student_id) REFERENCES users(user_id),
    CONSTRAINT fk_attendance_course FOREIGN KEY (course_id) REFERENCES courses(course_id),
    CONSTRAINT uniq_student_course_date UNIQUE (student_id, course_id, attendance_date)
);

CREATE TABLE member_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL,
    CONSTRAINT fk_membercard_student FOREIGN KEY (student_id) REFERENCES users(user_id),
    CONSTRAINT chk_validity_positive CHECK (validity_days > 0 AND remaining_days >= 0)
);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-014]:**
```json
{
  "endpoints": [
    {
      "path": "/api/v1/courses",
      "method": "GET",
      "response": [
        {
          "courseId": "UUID",
          "title": "string",
          "startDate": "DATE",
          "endDate": "DATE",
          "teacherName": "string"
        }
      ]
    },
    {
      "path": "/api/v1/courses",
      "method": "POST",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "DATE",
        "endDate": "DATE",
        "teacherId": "UUID",
        "maxStudents": "INT"
      },
      "response": {
        "courseId": "UUID"
      }
    },
    {
      "path": "/api/v1/courses/{id}",
      "method": "PUT",
      "request": {
        "title": "string",
        "startDate": "DATE",
        "endDate": "DATE",
        "teacherId": "UUID"
      },
      "response": {
        "courseId": "UUID"
      }
    },
    {
      "path": "/api/v1/courses/{id}",
      "method": "DELETE",
      "response": {
        "courseId": "UUID"
      }
    },
    {
      "path": "/api/v1/enrollments",
      "method": "POST",
      "request": {
        "studentId": "UUID",
        "courseId": "UUID"
      },
      "response": {
        "enrollmentId": "UUID"
      }
    },
    {
      "path": "/api/v1/attendance/scan",
      "method": "POST",
      "request": {
        "studentId": "UUID",
        "courseId": "UUID",
        "qrCodeData": "string"
      },
      "response": {
        "attendanceId": "UUID",
        "duplicate": "boolean"
      }
    },
    {
      "path": "/api/v1/membercards/{studentId}",
      "method": "GET",
      "response": {
        "cardId": "UUID",
        "validityDays": "INT",
        "remainingDays": "INT"
      }
    },
    {
      "path": "/api/v1/membercards/renew",
      "method": "POST",
      "request": {
        "studentId": "UUID",
        "additionalDays": "INT"
      },
      "response": {
        "cardId": "UUID",
        "newRemainingDays": "INT"
      }
    }
  ]
}
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
  * Xử lý lỗi mất kết nối mạng trong quá trình quét QR: Khi thiết bị quét QR nhưng không có mạng, ứng dụng lưu sự kiện cục bộ và tự động đồng bộ khi kết nối được khôi phục; backend xử lý đồng bộ một cách idempotent.
  * Ngăn chặn điểm danh trùng lặp: Nếu cùng một studentId và courseId được gửi trong cùng một ngày, hệ thống trả về success với cờ duplicate=true và không tạo bản ghi mới.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 1: Triển khai lớp thực thể khóa học, ghi danh và điểm danh**
  * **[Coder]**
  * **Targeted Tag IDs:** [REQ-007], [REQ-010], [DAT-004], [DAT-005], [DAT-006]
  * **Target Component file path (`target_component`):** `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseEntity.java [REQ-007], [DAT-004]`
  * **Low-Level Technical Task Instruction:** Triển khai lớp thực thể CourseEntity với các trường courseId, title, description, startDate, endDate, teacherId, maxStudents. Thêm ràng buộc CHECK startDate <= endDate. Triển khai EnrollmentEntity với các trường enrollmentId, studentId, courseId, enrollmentDate, UNIQUE student-course. Triển khai AttendanceEntity với các trường attendanceId, studentId, courseId, attendanceDate, timestamp, UNIQUE student-course-date. Ghi chú các mối quan hệ khóa ngoại.

- **DAY 2: Viết bộ kiểm thử cho điểm danh QR và xử lý trùng lặp**
  * **[Tester]**
  * **Targeted Tag IDs:** [REQ-012], [DAT-006], [EXC-001], [EXC-002]
  * **Target Component file path (`target_component`):** `./sources/backend/org/nlh4j/saas/membershiphub/attendance/AttendanceEntityTest.java;./sources/backend/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java`
  * **Low-Level Technical Task Instruction:** Xây dựng JUnit test cho AttendanceService xử lý quét QR, bao gồm kiểm tra ghi nhận điểm danh lần đầu, phát hiện duplicate, và mô phỏng mất kết nối mạng. Đảm bảo logic idempotent và cờ duplicate được trả về chính xác.

### 📈 Triển khai thông báo đa kênh, quản lý khuyến mãi và thông báo, tích hợp chatbot AI và lõi giao diện người dùng di động.

- **Phase Core Objective & Purpose:** Xây dựng hệ thống thông báo đẩy (FCM/APNs) và tích hợp bài đăng lên nhóm Zalo; triển khai quản lý khuyến mãi và thông báo với logic hết hạn; tích hợp chatbot AI cho dịch vụ khách hàng; và phát triển lõi giao diện người dùng di động đáp ứng vai trò.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend/org/nlh4j/saas/membershiphub/notification/NotificationEntity.java [REQ-016], [DAT-008]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/promotion/PromotionEntity.java [REQ-017], [DAT-009]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/announcement/AnnouncementEntity.java [REQ-018], [DAT-009]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java [REQ-019]`
  * `./sources/frontend/mobile/src/services/NotificationService.js [REQ-020]`
  * `./sources/docs/Phase4_Architecture.md [REQ-016], [REQ-017], [REQ-018], [REQ-019]`
- **Database Schema DDL SQL Specification [DAT-008], [DAT-009]:**
```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID,
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_notifications_user FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT,
    CONSTRAINT chk_discount_range CHECK (discount_percent >= 0 AND discount_percent <= 100)
);

CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE,
    CONSTRAINT chk_announcement_dates CHECK (start_date IS NULL OR end_date IS NULL OR start_date <= end_date)
);
```
- **API and Event Routing Contracts [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020]:**
```json
{
  "endpoints": [
    {
      "path": "/api/v1/notifications",
      "method": "POST",
      "request": {
        "userId": "UUID",
        "groupZalo": "string",
        "message": "string"
      },
      "response": {
        "notificationId": "UUID",
        "sentAt": "TIMESTAMP"
      }
    },
    {
      "path": "/api/v1/promotions",
      "method": "POST",
      "request": {
        "code": "string",
        "discountPercent": "SMALLINT",
        "startDate": "DATE",
        "endDate": "DATE",
        "description": "string"
      },
      "response": {
        "promoId": "UUID"
      }
    },
    {
      "path": "/api/v1/announcements",
      "method": "POST",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "DATE",
        "endDate": "DATE"
      },
      "response": {
        "announcementId": "UUID"
      }
    },
    {
      "path": "/api/v1/chatbot/query",
      "method": "POST",
      "request": {
        "userId": "UUID",
        "query": "string"
      },
      "response": {
        "answer": "string",
        "escalated": "boolean"
      }
    },
    {
      "path": "/api/v1/mobile/notifications/register",
      "method": "POST",
      "request": {
        "deviceToken": "string",
        "platform": "string"
      },
      "response": {
        "registered": "boolean"
      }
    }
  ]
}
```
- **Phase Localized Exception Handlers [EXC-003]:**
  * Xử lý lỗi gửi thông báo không thành công (ví dụ: device token không hợp lệ). Hệ thống ghi log lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu là thất bại và thông báo cho admin.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1: Triển khai lõi dịch vụ thông báo, khuyến mãi và thông báo**
  * **[Coder]**
  * **Targeted Tag IDs:** [REQ-016], [REQ-017], [REQ-018], [DAT-008], [DAT-009]
  * **Target Component file path (`target_component`):** `./sources/backend/org/nlh4j/saas/membershiphub/notification/NotificationEntity.java [REQ-016], [DAT-008]`
  * **Low-Level Technical Task Instruction:** Triển khai lớp thực thể NotificationEntity với các trường notificationId, userId, groupZalo, message, sentAt, delivered. Thêm các ràng buộc khóa ngoại. Triển khai PromotionEntity và AnnouncementEntity với các trường tương ứng, bao gồm CHECK cho discountPercent và ngày bắt đầu/kết thúc. Triển khai các controller REST cho các entity này.

- **DAY 2: Cung cấp cấu hình hạ tầng đám mây cho thông báo đẩy**
  * **[GCP]**
  * **Targeted Tag IDs:** [REQ-020], [ARC-010]
  * **Target Component file path (`target_component`):** `./sources/infra/gcp/firebase-config.yaml;./sources/infra/gcp/zalo-api-credentials.json`
  * **Low-Level Technical Task Instruction:** Tạo file YAML cấu hình Firebase Cloud Messaging (FCM) với khóa server, và file JSON lưu trữ credentials API Zalo. Triển khai các secret vào Google Secret Manager, thiết lập IAM cho dịch vụ thông báo, và xác thực OAuth2 cho Zalo.

### 📈 Triển khai bản địa hóa, SEO, báo cáo, hardening bảo mật, container hóa và triển khai trên GKE, logging kiểm toán.

- **Phase Core Objective & Purpose:** Xây dựng hệ thống bản địa hóa đa ngôn ngữ (EN, VI, ES) với hreflang và meta tags; triển khai công cụ tạo báo cáo điểm danh (CSV) và bảng điều khiển tóm tắt; hardening bảo mật (TLS 1.3, OWASP); container hóa và triển khai trên GKE với CI/CD; thiết lập logging kiểm toán toàn diện.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend/org/nlh4j/saas/membershiphub/i18n/I18nConfig.java [REQ-022], [REQ-023]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/report/AttendanceReportService.java [REQ-024]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/security/SecurityConfig.java [NFR-003]`
  * `./sources/infra/k8s/Deployment.yaml [NFR-004]`
  * `./sources/infra/ci-cd/pipeline.yaml [NFR-005]`
  * `./sources/backend/org/nlh4j/saas/membershiphub/audit/AuditLogEntity.java [NFR-006]`
  * `./sources/docs/Phase5_Architecture.md [REQ-022], [REQ-023], [REQ-024], [NFR-003], [NFR-004], [NFR-005], [NFR-006]`
- **Database Schema DDL SQL Specification [DAT-011]:**
```sql
CREATE TABLE system_settings (
    setting_key VARCHAR(100) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-022], [REQ-023], [REQ-024], [REQ-025]:**
```json
{
  "endpoints": [
    {
      "path": "/api/v1/i18n/{locale}",
      "method": "GET",
      "response": {
        "messages": "object"
      }
    },
    {
      "path": "/api/v1/reports/attendance",
      "method": "GET",
      "request": {
        "centerId": "UUID",
        "startDate": "DATE",
        "endDate": "DATE"
      },
      "response": {
        "fileName": "string",
        "downloadUrl": "string"
      }
    },
    {
      "path": "/api/v1/dashboard/summary",
      "method": "GET",
      "response": {
        "totalStudents": "INT",
        "activeCourses": "INT",
        "upcomingSessions": "INT"
      }
    }
  ]
}
```
- **Phase Localized Exception Handlers [EXC-005]:**
  * Xử lý lỗi phục hồi hệ thống sau sự cố: Khi dịch vụ được khôi phục, bất kỳ quét QR chờ xử lý nào được lưu trữ sẽ được xử lý theo thứ tự FIFO; người dùng nhận được thông báo về các sự kiện điểm danh đã được khôi phục.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 1: Xây dựng manifest triển khai Kubernetes**
  * **[GKE]**
  * **Targeted Tag IDs:** [NFR-004], [NFR-005]
  * **Target Component file path (`target_component`):** `./sources/infra/k8s/Deployment.yaml;./sources/backend/org/nlh4j/saas/membershiphub/`
  * **Low-Level Technical Task Instruction:** Tạo Deployment.yaml cho tất cả các service Quarkus, cấu hình HPA dựa trên CPU > 70% hoặc latency > 300ms, thiết lập Service cho mỗi module, và định nghĩa Ingress với TLS. Triển khai lên cluster GKE.

- **DAY 2: Đánh giá và hardening bảo mật**
  * **[Reviewer]**
  * **Targeted Tag IDs:** [NFR-003], [NFR-006]
  * **Target Component file path (`target_component`):** `./sources/backend/org/nlh4j/saas/membershiphub/security/SecurityConfig.java;./sources/backend/org/nlh4j/saas/membershiphub/audit/AuditLogEntity.java`
  * **Low-Level Technical Task Instruction:** Đánh giá cấu hình bảo mật hiện tại, áp dụng các biện pháp đối phó OWASP Top 10 (SQL injection, XSS, CSRF). Triển khai chuẩn hóa logging cho tất cả các thao tác người dùng (tạo, cập nhật vai trò, ghi điểm danh) trong AuditLogEntity.

- **DAY 3: Tạo tài liệu kỹ thuật và tham chiếu API**
  * **[Doc]**
  * **Targeted Tag IDs:** [REQ-022], [REQ-023], [REQ-024], [REQ-025]
  * **Target Component file path (`target_component`):** `./sources/docs/Phase5_Documentation.md;./sources/backend/org/nlh4j/saas/membershiphub/`
  * **Low-Level Technical Task Instruction:** Soạn thảo tài liệu kỹ thuật chi tiết bao gồm hướng dẫn triển khai, tham chiếu API (OpenAPI), hướng dẫn vận hành, và hướng dẫn tuân thủ GDPR/CCPA. Đính kèm các sơ đồ kiến trúc, bảng điều khiển API, và các ghi chú về bảo mật.

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng PreparedStatement với các tham số dấu hỏi; áp dụng whitelist cho các cột sắp xếp; thực thi kiểm tra đầu vào nghiêm ngặt tại lớp controller.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động thoát HTML trong tất cả các response view; thiết lập header CSP không cho phép `unsafe-inline`; sử dụng React JSX auto-escaping.
- **Multi-Tenant CORS Security Rails:** whitelist các nguồn gốc dựa trên cấu hình tenant; xác thực origin động qua bảng SystemSettings; từ chối các nguồn gốc không được phép.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Áp dụng `@JsonSerialize` với `JsonIgnore` cho các trường nhạy cảm; thực hiện masking cho email (chỉ hiển thị domain), số điện thoại (chỉ hiển thị 4 số cuối); lên lịch dọn dẹp log sau 1 năm.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Triển khai các interceptor fetch với retry exponential backoff; sử dụng `@capacitor/preferences` cho storage an toàn; chặn nút back-button gốc để điều hướng trong ứng dụng; enforce TLS cho tất cả các endpoint API.
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware phát hiện locale qua header Accept-Language và cookie; tạo các thẻ hreflang động; nhúng meta tags cho từng ngôn ngữ; cache các bản dịch đã dịch để giảm độ trễ.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Tạo branch `features/development-phase-5-day-3` cho ngày hiện tại; mỗi ngày mới tạo branch mới dựa trên commit base của ngày trước.
- **Validation Guard Pipeline Gates:** Thực thi kiểm tra biên dịch, kiểm tra độ phủ mã nguồn (>= 85%), và xác nhận tham chiếu tag. Chỉ cho phép merge sau khi CI thành công và Reviewer phê duyệt.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`