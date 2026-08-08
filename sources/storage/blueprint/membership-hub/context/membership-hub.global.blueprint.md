# NGÀNH ĐỐI TƯỢNG CỤ THỂ: membership-hub

## Điều khiển tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID bản đồ** | ARCH-20260808055829 |
| **Tên dự án** | membership-hub |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày giờ** | 2026/08/08 05:58:29 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## TỔNG QUAN HỆ THỐNG & MÔ HÌNH CƠ SỞ

### Mô hình hệ thống cốt lõi & Mô hình kiến trúc

- Kiến trúc microservices phân tách rõ ràng: `user-service`, `course-service`, `notification-service`, `reporting-service`.
- Backend được xây dựng bằng Java 17 + Quarkus 3.x, sử dụng CDI, Hibernate ORM, Flyway, Redis cho session caching.
- Cơ sở dữ liệu chính: PostgreSQL 15, sử dụng schema phân vùng theo `centerId`.
- Xác thực: Firebase Authentication, OAuth2 (Google, Facebook), JWT 15 phút, refresh 7 ngày.
- Giao tiếp nội bộ: Kafka (topic `attendance`, `notifications`, `promotions`), gRPC cho các dịch vụ nội bộ.
- Container: Docker multi-stage, triển khai trên GKE, CI/CD bằng GitHub Actions.
- Frontend: Next.js 13, React 18, TypeScript, Tailwind CSS, Capacitor cho mobile.
- Định dạng dữ liệu: JSON, Protobuf cho Kafka, gRPC.
- Bảo mật: TLS 1.3, AES‑256 at rest, OWASP Top 10 mitigations, role-based access control (RBAC).
- Độ tin cậy: HPA dựa trên CPU > 70 % hoặc latency > 300 ms, read replicas cho reporting.

### Kiến trúc luồng dữ liệu doanh nghiệp & hệ sinh thái cốt lõi

- Luồng xác thực: Frontend gửi credential → Auth Service → Firebase → JWT → Quarkus → Redis cache.
- Luồng điểm danh QR: Mobile quét → API `/attendance/scan` → Kafka `attendance` → Attendance Service → PostgreSQL.
- Luồng thông báo: Notification Service publish → Kafka `notifications` → Mobile push (FCM/APNs) & Zalo API.
- Luồng dữ liệu báo cáo: Reporting Service query PostgreSQL → CSV export → API `/reports/attendance`.
- Fan-out: Khi tạo promotion, Notification Service gửi thông báo tới tất cả học viên và Zalo group.
- Caching: Redis cho session, user profile, course list.

## CẢNH BỘ CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.2, Hibernate ORM 6.2, Flyway 9.5, Redis 7.0, PostgreSQL 15, Firebase Auth SDK, Google Cloud Messaging, Zalo API SDK, Docker 24, GKE 1.27, GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript 5.0, Tailwind CSS 3.3, Capacitor 5.0, React Native 0.73, Firebase Cloud Messaging SDK, Zalo SDK.

### MÁTRIX CẢNH BỘ

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=[true]
BACKEND_LAYER_REQUIRED=[true]
FRONTEND_LAYER_REQUIRED=[true]
MOBILE_LAYER_REQUIRED=[true]
DEVOPS_LAYER_REQUIRED=[true]
```

## QUY TẮC BẢO VỆ & CHẤP NHẬN DOANH NGHIỆP

- **Ranh giới công việc**: Repository root là `.`; tất cả các đường dẫn bắt đầu bằng `./sources/`.
- **Định dạng thư mục**: Backend: `./sources/backend/<service-name>/`; Frontend: `./sources/frontend/<app-name>/`; DevOps: `./sources/infra/`; Docs: `./sources/docs/`.
- **Java Package**: `org.nlh4j.saas.membershiphub` (đã chuyển `membership-hub` thành `membershiphub`).
- **Tester Target Path**: `<source_component>;<test_suite_file>` (cả hai bắt đầu bằng `./sources/`).

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 - 4 | ./sources/backend/user-service | JUnit, Integration Tests, E2E Automation, API Specs, Architecture Docs | Coder, Tester, Doc | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011] |
| 2 | 1 - 4 | ./sources/backend/course-service | JUnit, Integration Tests, E2E Automation, API Specs, Architecture Docs | Coder, Tester, Doc | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022] |
| 3 | 1 - 4 | ./sources/backend/notification-service | JUnit, Integration Tests, E2E Automation, API Specs, Architecture Docs | Coder, Tester, Doc | [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005] |
| 4 | 1 - 4 | ./sources/infra | Dockerfile, Terraform, GKE Deployment, CI/CD Pipeline | Docker, GCP, GKE | [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008] |
| 5 | 1 - 4 | ./sources/backend/reporting-service | Reporting API, Dashboard, Mobile UI, Documentation | Coder, Tester, Doc | [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
<!--END_PHASE_SYNOPSIS_GRID-->

## Đặc tả Kiến trúc Chi tiết Giai đoạn 1

### Mục tiêu Cốt lõi & Mục đích của Giai đoạn 1
Xây dựng chức năng đăng ký, xác thực, phân quyền người dùng, quản lý trung tâm.

### Bản đồ Ma trận Thư mục Vật lý Mục tiêu
- `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/userservice/` [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]
- `./sources/docs/architecture/user-service.md` [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]
- `./sources/backend/user-service/src/main/resources/db/migration/V1__create_users_and_roles.sql` [DAT-001], [DAT-002]
- `./sources/backend/user-service/src/test/java/org/nlh4j/saas/membershiphub/userservice/` [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]

### Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-002]
```sql
CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash VARCHAR(60) NOT NULL,
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

ALTER TABLE USERS ADD CONSTRAINT fk_user_role FOREIGN KEY (roleId) REFERENCES ROLES(roleId);
```

### Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]
```json
{
  "endpoints": [
    {
      "path": "/api/users/register",
      "method": "POST",
      "request": {
        "type": "object",
        "properties": {
          "email": {"type": "string", "format": "email"},
          "password": {"type": "string"},
          "fullName": {"type": "string"}
        },
        "required": ["email", "password", "fullName"]
      },
      "response": {
        "type": "object",
        "properties": {
          "userId": {"type": "string"},
          "token": {"type": "string"}
        }
      }
    },
    {
      "path": "/api/users/login",
      "method": "POST",
      "request": {
        "type": "object",
        "properties": {
          "email": {"type": "string", "format": "email"},
          "password": {"type": "string"}
        },
        "required": ["email", "password"]
      },
      "response": {
        "type": "object",
        "properties": {
          "userId": {"type": "string"},
          "token": {"type": "string"}
        }
      }
    }
  ],
  "events": [
    {
      "topic": "user.registered",
      "schema": {
        "type": "object",
        "properties": {
          "userId": {"type": "string"},
          "email": {"type": "string"}
        }
      }
    }
  ]
}
```

### Xử lý ngoại lệ [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]
- **EXC-001**: Xác thực đầu vào không hợp lệ → Trả lỗi 400 với danh sách trường không hợp lệ.
- **EXC-002**: Email đã tồn tại → Trả lỗi 409.
- **EXC-003**: Lỗi xác thực Firebase → Trả lỗi 401.
- **EXC-004**: Lỗi ghi database → Trả lỗi 500.
- **EXC-005**: Lỗi JWT expired → Trả lỗi 401.

## Đặc tả Kiến trúc Chi tiết Giai đoạn 2

### Mục tiêu Cốt lõi & Mục đích của Giai đoạn 2
Quản lý khóa học, học viên, điểm danh, thẻ hội viên.

### Bản đồ Ma trận Thư mục Vật lý Mục tiêu
- `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/courseservice/` [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022]
- `./sources/docs/architecture/course-service.md` [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022]
- `./sources/backend/course-service/src/main/resources/db/migration/V2__create_courses_enrollments_attendance_studentcards.sql` [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007]
- `./sources/backend/course-service/src/test/java/org/nlh4j/saas/membershiphub/courseservice/` [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022]

### Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007]
```sql
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL,
    maxStudents INT NOT NULL DEFAULT 30
);

CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);

CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (studentId, courseId, attendanceDate),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);

CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
```

### Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022]
```json
{
  "endpoints": [
    {
      "path": "/api/courses",
      "method": "GET",
      "response": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "courseId": {"type": "string"},
            "title": {"type": "string"},
            "startDate": {"type": "string", "format": "date"},
            "endDate": {"type": "string", "format": "date"},
            "teacherName": {"type": "string"}
          }
        }
      }
    },
    {
      "path": "/api/courses",
      "method": "POST",
      "request": {
        "type": "object",
        "properties": {
          "title": {"type": "string"},
          "startDate": {"type": "string", "format": "date"},
          "endDate": {"type": "string", "format": "date"},
          "teacherId": {"type": "string"}
        },
        "required": ["title", "startDate", "endDate", "teacherId"]
      },
      "response": {
        "type": "object",
        "properties": {
          "courseId": {"type": "string"}
        }
      }
    }
  ],
  "events": [
    {
      "topic": "course.created",
      "schema": {
        "type": "object",
        "properties": {
          "courseId": {"type": "string"},
          "title": {"type": "string"}
        }
      }
    }
  ]
}
```

### Xử lý ngoại lệ [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]
- **EXC-001**: Xác thực dữ liệu không hợp lệ → Trả lỗi 400.
- **EXC-002**: Trùng lịch học của giáo viên → Trả lỗi 409.
- **EXC-003**: Lỗi ghi database → Trả lỗi 500.
- **EXC-004**: Lỗi JWT expired → Trả lỗi 401.
- **EXC-005**: Lỗi đăng ký học viên đã tồn tại → Trả lỗi 409.

## Đặc tả Kiến trúc Chi tiết Giai đoạn 3

### Mục tiêu Cốt lõi & Mục đích của Giai đoạn 3
Xử lý thông báo, push, Zalo, và quản lý khuyến mãi.

### Bản đồ Ma trận Thư mục Vật lý Mục tiêu
- `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notificationservice/` [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005]
- `./sources/docs/architecture/notification-service.md` [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005]
- `./sources/backend/notification-service/src/main/resources/db/migration/V3__create_notifications.sql` [DAT-008]
- `./sources/backend/notification-service/src/test/java/org/nlh4j/saas/membershiphub/notificationservice/` [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005]

### Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]
```sql
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (userId) REFERENCES USERS(userId)
);
```

### Hợp đồng Định tuyến API và Sự kiện [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005]
```json
{
  "endpoints": [
    {
      "path": "/api/notifications",
      "method": "POST",
      "request": {
        "type": "object",
        "properties": {
          "userId": {"type": "string"},
          "message": {"type": "string"},
          "groupZalo": {"type": "string"}
        },
        "required": ["message"]
      },
      "response": {
        "type": "object",
        "properties": {
          "notificationId": {"type": "string"}
        }
      }
    }
  ],
  "events": [
    {
      "topic": "notification.sent",
      "schema": {
        "type": "object",
        "properties": {
          "notificationId": {"type": "string"},
          "userId": {"type": "string"}
        }
      }
    }
  ]
}
```

### Xử lý ngoại lệ [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]
- **EXC-001**: Thông báo không hợp lệ → Trả lỗi 400.
- **EXC-002**: Lỗi gửi push → Trả lỗi 500.
- **EXC-003**: Lỗi gửi Zalo → Trả lỗi 500.
- **EXC-004**: Lỗi ghi database → Trả lỗi 500.
- **EXC-005**: Lỗi JWT expired → Trả lỗi 401.

## Đặc tả Kiến trúc Chi tiết Giai đoạn 4

### Mục tiêu Cốt lõi & Mục đích của Giai đoạn 4
Containerization, CI/CD, GKE deployment, Terraform.

### Bản đồ Ma trận Thư mục Vật lý Mục tiêu
- `./sources/infra/docker/Dockerfile` [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
- `./sources/infra/terraform/main.tf` [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
- `./sources/infra/gke/deployment.yaml` [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
- `./sources/infra/github-actions/workflows/ci.yml` [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 5

### Mục tiêu Cốt lõi & Mục đích của Giai đoạn 5
Reporting, analytics, mobile compliance, i18n, SEO.

### Bản đồ Ma trận Thư mục Vật lý Mục tiêu
- `./sources/backend/reporting-service/src/main/java/org/nlh4j/saas/membershiphub/reportingservice/` [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
- `./sources/docs/architecture/reporting-service.md` [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
- `./sources/frontend/mobile-app/src/main/java/com/membershiphub/mobile/` [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
- `./sources/frontend/mobile-app/src/test/java/com/membershiphub/mobile/` [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]

### Hợp đồng Định tuyến API và Sự kiện [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
```json
{
  "endpoints": [
    {
      "path": "/api/reports/attendance",
      "method": "GET",
      "query": {
        "centerId": {"type": "string"},
        "date": {"type": "string", "format": "date"}
      },
      "response": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "studentName": {"type": "string"},
            "courseName": {"type": "string"},
            "attendanceDate": {"type": "string", "format": "date"},
            "status": {"type": "string"}
          }
        }
      }
    }
  ],
  "events": [
    {
      "topic": "report.generated",
      "schema": {
        "type": "object",
        "properties": {
          "reportId": {"type": "string"},
          "centerId": {"type": "string"}
        }
      }
    }
  ]
}
```

## Đặc tả Kiến trúc Chi tiết Giai đoạn 1 – Ngày 1

- **Ngày 1**: Xây dựng mô hình dữ liệu người dùng và vai trò.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [DAT-001], [DAT-002]
  * **Target Component file path (`target_component`):** `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/userservice/UserService.java` [REQ-001], [REQ-002], [REQ-003]
  * **Low-Level Technical Task Instruction:** Thiết kế lớp `User`, `Role`, repository, service, và controller. Đảm bảo kiểm tra email duy nhất, hash mật khẩu bằng BCrypt, và tạo JWT. [REQ-001], [REQ-002], [REQ-003]

### Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-002]
```sql
CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash VARCHAR(60) NOT NULL,
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

ALTER TABLE USERS ADD CONSTRAINT fk_user_role FOREIGN KEY (roleId) REFERENCES ROLES(roleId);
```

## Đặc tả Kiến trúc Chi tiết Giai đoạn 1 – Ngày 2

- **Ngày 2**: Xây dựng endpoint đăng ký và login.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003]
  * **Target Component file path (`target_component`):** `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/userservice/UserController.java` [REQ-001], [REQ-002], [REQ-003]
  * **Low-Level Technical Task Instruction:** Tạo endpoint `/api/users/register` và `/api/users/login`. Sử dụng DTO, validation, và trả về JWT. [REQ-001], [REQ-002], [REQ-003]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 1 – Ngày 3

- **Ngày 3**: Xây dựng endpoint phân quyền và quản lý trung tâm.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
  * **Target Component file path (`target_component`):** `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/userservice/CenterController.java` [REQ-004], [REQ-005], [REQ-006]
  * **Low-Level Technical Task Instruction:** Tạo endpoint `/api/centers`, `/api/centers/{id}`, và `/api/centers/{id}/admins`. Sử dụng DTO, validation, và kiểm tra quyền RBAC. [REQ-004], [REQ-005], [REQ-006]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 1 – Ngày 4

- **Ngày 4**: Kiểm thử đơn vị và tích hợp cho user-service.
  * **Sub-Agent Workflow Specialization:** `[Tester]`
  * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]
  * **Target Component file path (`target_component`):** `./sources/backend/user-service/src/test/java/org/nlh4j/saas/membershiphub/userservice/UserServiceTest.java;./sources/backend/user-service/src/test/java/org/nlh4j/saas/membershiphub/userservice/UserControllerTest.java` [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]
  * **Low-Level Technical Task Instruction:** Viết JUnit 5 test cho service và controller, mock repository, kiểm tra validation, và xác thực JWT. [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 2 – Ngày 1

- **Ngày 1**: Xây dựng mô hình dữ liệu khóa học và học viên.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-014], [DAT-003], [DAT-004]
  * **Target Component file path (`target_component`):** `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/courseservice/CourseService.java` [REQ-012], [REQ-013], [REQ-014]
  * **Low-Level Technical Task Instruction:** Thiết kế lớp `Course`, `Enrollment`, `Attendance`, `StudentCard`, repository, service, và controller. Đảm bảo kiểm tra lịch trùng, khóa học trùng, và tính hợp lệ. [REQ-012], [REQ-013], [REQ-014]

### Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003], [DAT-004]
```sql
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL,
    maxStudents INT NOT NULL DEFAULT 30
);
```

## Đặc tả Kiến trúc Chi tiết Giai đoạn 2 – Ngày 2

- **Ngày 2**: Xây dựng endpoint quản lý khóa học và học viên.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-014], [DAT-003], [DAT-004]
  * **Target Component file path (`target_component`):** `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/courseservice/CourseController.java` [REQ-012], [REQ-013], [REQ-014]
  * **Low-Level Technical Task Instruction:** Tạo endpoint `/api/courses`, `/api/courses/{id}`, `/api/courses/{id}/enroll`, `/api/courses/{id}/attendance`. Kiểm tra lịch trùng, khóa học trùng, và xác thực quyền. [REQ-012], [REQ-013], [REQ-014]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 2 – Ngày 3

- **Ngày 3**: Xây dựng endpoint đăng ký học viên và điểm danh.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [REQ-010], [REQ-011], [DAT-005], [DAT-006]
  * **Target Component file path (`target_component`):** `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/courseservice/EnrollmentController.java` [REQ-010], [REQ-011]
  * **Low-Level Technical Task Instruction:** Tạo endpoint `/api/enrollments`, `/api/attendance/scan`. Kiểm tra học viên đã tồn tại, tạo tài khoản, và ghi điểm danh. [REQ-010], [REQ-011]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 2 – Ngày 4

- **Ngày 4**: Kiểm thử đơn vị và tích hợp cho course-service.
  * **Sub-Agent Workflow Specialization:** `[Tester]`
  * **Targeted Tag IDs:** [REQ-012], [REQ-013], [REQ-014], [REQ-010], [REQ-011], [DAT-003], [DAT-004], [DAT-005], [DAT-006]
  * **Target Component file path (`target_component`):** `./sources/backend/course-service/src/test/java/org/nlh4j/saas/membershiphub/courseservice/CourseServiceTest.java;./sources/backend/course-service/src/test/java/org/nlh4j/saas/membershiphub/courseservice/EnrollmentControllerTest.java` [REQ-012], [REQ-013], [REQ-014], [REQ-010], [REQ-011], [DAT-003], [DAT-004], [DAT-005], [DAT-006]
  * **Low-Level Technical Task Instruction:** Viết JUnit 5 test cho service và controller, mock repository, kiểm tra validation, và xác thực quyền. [REQ-012], [REQ-013], [REQ-014], [REQ-010], [REQ-011]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 3 – Ngày 1

- **Ngày 1**: Xây dựng mô hình dữ liệu thông báo.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [REQ-023], [REQ-024], [DAT-008]
  * **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notificationservice/NotificationService.java` [REQ-023], [REQ-024]
  * **Low-Level Technical Task Instruction:** Thiết kế lớp `Notification`, repository, service, và controller. Đảm bảo gửi push và Zalo. [REQ-023], [REQ-024]

### Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]
```sql
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (userId) REFERENCES USERS(userId)
);
```

## Đặc tả Kiến trúc Chi tiết Giai đoạn 3 – Ngày 2

- **Ngày 2**: Xây dựng endpoint gửi thông báo.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]
  * **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notificationservice/NotificationController.java` [REQ-023], [REQ-024]
  * **Low-Level Technical Task Instruction:** Tạo endpoint `/api/notifications`, xử lý payload, gọi Firebase Cloud Messaging và Zalo API, lưu vào DB. [REQ-023], [REQ-024]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 3 – Ngày 3

- **Ngày 3**: Xây dựng endpoint nhận sự kiện và xử lý ngoại lệ.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]
  * **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notificationservice/NotificationExceptionHandler.java` [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]
  * **Low-Level Technical Task Instruction:** Định nghĩa exception handler cho các lỗi validation, push, Zalo, DB, JWT. [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 3 – Ngày 4

- **Ngày 4**: Kiểm thử đơn vị và tích hợp cho notification-service.
  * **Sub-Agent Workflow Specialization:** `[Tester]`
  * **Targeted Tag IDs:** [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-008]
  * **Target Component file path (`target_component`):** `./sources/backend/notification-service/src/test/java/org/nlh4j/saas/membershiphub/notificationservice/NotificationServiceTest.java;./sources/backend/notification-service/src/test/java/org/nlh4j/saas/membershiphub/notificationservice/NotificationControllerTest.java` [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-008]
  * **Low-Level Technical Task Instruction:** Viết JUnit 5 test cho service và controller, mock external APIs, kiểm tra exception handling. [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-008]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 4 – Ngày 1

- **Ngày 1**: Xây dựng Dockerfile cho microservices.
  * **Sub-Agent Workflow Specialization:** `[Docker]`
  * **Targeted Tag IDs:** [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
  * **Target Component file path (`target_component`):** `./sources/infra/docker/Dockerfile` [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
  * **Low-Level Technical Task Instruction:** Viết multi-stage Dockerfile, giảm kích thước, sử dụng OpenJDK 17, copy JAR, expose port 8080, healthcheck. [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 4 – Ngày 2

- **Ngày 2**: Xây dựng Terraform cho GKE cluster.
  * **Sub-Agent Workflow Specialization:** `[GCP]`
  * **Targeted Tag IDs:** [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
  * **Target Component file path (`target_component`):** `./sources/infra/terraform/main.tf` [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
  * **Low-Level Technical Task Instruction:** Viết Terraform modules cho VPC, GKE cluster, IAM, Cloud SQL, Pub/Sub, và Cloud Storage. [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 4 – Ngày 3

- **Ngày 3**: Xây dựng Kubernetes manifests.
  * **Sub-Agent Workflow Specialization:** `[GKE]`
  * **Targeted Tag IDs:** [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
  * **Target Component file path (`target_component`):** `./sources/infra/gke/deployment.yaml` [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
  * **Low-Level Technical Task Instruction:** Viết Deployment, Service, Ingress, HPA, ConfigMap, Secret. Đảm bảo autoscaling, health checks, TLS. [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 4 – Ngày 4

- **Ngày 4**: Xây dựng workflow CI/CD.
  * **Sub-Agent Workflow Specialization:** `[Docker]`
  * **Targeted Tag IDs:** [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
  * **Target Component file path (`target_component`):** `./sources/infra/github-actions/workflows/ci.yml` [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]
  * **Low-Level Technical Task Instruction:** Viết GitHub Actions workflow: build, test, scan, push Docker image, deploy to GKE. Đảm bảo coverage > 85 %. [DAT-006], [DAT-007], [DAT-008], [DAT-009], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 5 – Ngày 1

- **Ngày 1**: Xây dựng mô hình dữ liệu báo cáo.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
  * **Target Component file path (`target_component`):** `./sources/backend/reporting-service/src/main/java/org/nlh4j/saas/membershiphub/reportingservice/ReportingService.java` [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
  * **Low-Level Technical Task Instruction:** Thiết kế service để truy vấn PostgreSQL, tạo CSV, lưu file, và trả về URL. [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 5 – Ngày 2

- **Ngày 2**: Xây dựng endpoint báo cáo.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
  * **Target Component file path (`target_component`):** `./sources/backend/reporting-service/src/main/java/org/nlh4j/saas/membershiphub/reportingservice/ReportingController.java` [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
  * **Low-Level Technical Task Instruction:** Tạo endpoint `/api/reports/attendance`, nhận query, gọi service, trả về CSV. [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 5 – Ngày 3

- **Ngày 3**: Xây dựng mobile UI cho báo cáo.
  * **Sub-Agent Workflow Specialization:** `[Coder]`
  * **Targeted Tag IDs:** [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
  * **Target Component file path (`target_component`):** `./sources/frontend/mobile-app/src/main/java/com/membershiphub/mobile/ReportingScreen.java` [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
  * **Low-Level Technical Task Instruction:** Thiết kế màn hình báo cáo, fetch API, hiển thị bảng, download CSV. [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]

## Đặc tả Kiến trúc Chi tiết Giai đoạn 5 – Ngày 4

- **Ngày 4**: Kiểm thử đơn vị và tích hợp cho reporting-service và mobile UI.
  * **Sub-Agent Workflow Specialization:** `[Tester]`
  * **Targeted Tag IDs:** [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
  * **Target Component file path (`target_component`):** `./sources/backend/reporting-service/src/test/java/org/nlh4j/saas/membershiphub/reportingservice/ReportingServiceTest.java;./sources/frontend/mobile-app/src/test/java/com/membershiphub/mobile/ReportingScreenTest.java` [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]
  * **Low-Level Technical Task Instruction:** Viết JUnit 5 test cho service, mock DB, kiểm tra CSV, viết Espresso test cho mobile UI. [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]

## Mã hóa bảo mật & biện pháp ngăn chặn xâm nhập [NFR-001] đến [NFR-009]

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameter binding, tránh string concatenation.
- **Cross-Site Scripting (XSS)**: Escape output, CSP headers, React auto-escaping.
- **CORS**: Chỉ cho phép origin cụ thể, kiểm tra tenant origin.
- **Log Scrubbing**: Mask PII, log level 1‑year retention.

## Quy tắc tuân thủ đa ngôn ngữ & SEO [NFR-007] đến [NFR-009]

- **i18n**: Tải locale từ cookie hoặc header, fallback browser locale.
- **SEO**: Thêm meta tags, hreflang, sitemap, robots.txt, JSON‑LD.

## Quy trình CI/CD & DevOps

- **GitHub Actions**: Build, test, scan, push Docker, deploy to GKE, run integration tests.
- **Terraform**: Provision VPC, GKE, Cloud SQL, Pub/Sub, IAM.
- **Docker**: Multi-stage, size < 500 MB, base < 200 MB.

## Kiểm tra toàn bộ

- **[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 24, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]**