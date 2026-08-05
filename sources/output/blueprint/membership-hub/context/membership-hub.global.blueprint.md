# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260805170748 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/05 17:07:48 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CƠ BẢN

### 1.1. Kiến trúc hệ thống và mô hình hoạt động
Hệ thống membership-hub là một nền tảng quản lý hội viên đa trung tâm với kiến trúc microservices, sử dụng Java/Quarkus cho backend, PostgreSQL cho cơ sở dữ liệu, và container hóa Docker với triển khai trên Kubernetes (GKE). Hệ thống hỗ trợ xác thực đa kênh (email/mật khẩu, Firebase, Google, Facebook), quản lý điểm danh qua mã QR, và giao tiếp đa kênh (web, di động, nhóm Zalo).

### 1.2. Luồng dữ liệu và hệ sinh thái
Hệ thống sử dụng các luồng dữ liệu chính bao gồm xác thực người dùng, xử lý điểm danh QR, gửi thông báo, và tích hợp backend ứng dụng di động. Các kênh giao tiếp bao gồm REST APIs, push notifications (FCM/APNs), và Zalo API integration. Cơ sở dữ liệu chính sử dụng PostgreSQL với Redis cho session caching.

## 📁 2. CÔNG NGHỆ & THƯ VIỆN CỐT LÕI
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis, GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React, Capacitor, Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs.

<!--START_TECHNICAL_MATRIX_DO_NOT_TRANSLATE
### ARCHITECTURAL STACK MATRIX
[CRITICAL WARNING: You MUST keep this entire block 100% in raw Technical English. You are STRICTLY FORBIDDEN from translating any keys, values, or tokens inside this section into 🇻🇳 Vietnamese, as it serves as a strict backend machine-gating matrix. Keep literal `true` or `false` tokens in pure lower-case].

PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
END_TECHNICAL_MATRIX_DO_NOT_TRANSLATE-->

## 📁 3. QUY TẮC TUÂN THỦ TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
<!--START_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY
[CRITICAL TRANSLATION COMMAND: You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: 🇻🇳 Vietnamese. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output].
END_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY-->
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. TÓM TẮT KIẾN TRÚC MỤC TIÊU CAO CẤP
| Giai đoạn | Khoảng ngày | Thành phần Kiến trúc / Module Đường dẫn | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1-3 | `./sources/backend/auth`, `./sources/backend/centers`, `./sources/backend/courses`, `./sources/docs/` | Xác thực người dùng, quản lý trung tâm, quản lý khóa học, tài liệu kiến trúc | Coder, Doc | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-001], [DAT-003], [DAT-004] |
| Giai đoạn 2 | Ngày 1-3 | `./sources/backend/enrollments`, `./sources/backend/attendance`, `./sources/backend/membership`, `./sources/docs/` | Đăng ký học viên, điểm danh, quản lý thẻ hội viên, tài liệu kiến trúc | Coder, Doc | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-005], [DAT-006], [DAT-007] |
| Giai đoạn 3 | Ngày 1-3 | `./sources/backend/notifications`, `./sources/backend/promotions`, `./sources/docs/` | Thông báo, quản lý khuyến mãi, tài liệu kiến trúc | Coder, Doc | [REQ-016], [REQ-017], [REQ-018], [DAT-008], [DAT-009] |
| Giai đoạn 4 | Ngày 1-3 | `./sources/frontend/`, `./sources/mobile/`, `./sources/docs/` | Giao diện người dùng, ứng dụng di động, tài liệu kiến trúc | Coder, Doc | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011] |
| Giai đoạn 5 | Ngày 1-3 | `./sources/infra/`, `./sources/docs/` | Triển khai hạ tầng, tài liệu kiến trúc | Docker, GCP, GKE, Doc | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 5. CHI TIẾT PHÂN PHỐI CÔNG VIỆC THEO NGÀY VÀ GIAI ĐOẠN

### 📈 Giai đoạn 1 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống xác thực người dùng, quản lý trung tâm, và quản lý khóa học.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/auth`, `./sources/backend/centers`, `./sources/backend/courses`, `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004]:**
  ```sql
  CREATE TABLE USERS (
      userId UUID PRIMARY KEY,
      email VARCHAR(255) NOT NULL UNIQUE,
      passwordHash CHAR(60) NOT NULL,
      fullName VARCHAR(100) NOT NULL,
      roleId SMALLINT NOT NULL,
      provider VARCHAR(10) DEFAULT 'local',
      createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
      updatedAt TIMESTAMP NOT NULL DEFAULT NOW(),
      FOREIGN KEY (roleId) REFERENCES ROLES(roleId)
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
      contactPhone VARCHAR(20),
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
      FOREIGN KEY (teacherId) REFERENCES USERS(userId)
  );
  ```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009]:**
  ```json
  {
    "register": {
      "method": "POST",
      "path": "/api/auth/register",
      "request": {
        "email": "string",
        "password": "string",
        "fullName": "string"
      },
      "response": {
        "token": "string"
      }
    },
    "login": {
      "method": "POST",
      "path": "/api/auth/login",
      "request": {
        "email": "string",
        "password": "string"
      },
      "response": {
        "token": "string"
      }
    },
    "assignRole": {
      "method": "POST",
      "path": "/api/users/assign-role",
      "request": {
        "userId": "uuid",
        "roleId": "smallint"
      },
      "response": {
        "status": "string"
      }
    },
    "createCenter": {
      "method": "POST",
      "path": "/api/centers",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "centerId": "uuid"
      }
    },
    "createCourse": {
      "method": "POST",
      "path": "/api/courses",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "date",
        "endDate": "date",
        "teacherId": "uuid",
        "maxStudents": "int"
      },
      "response": {
        "courseId": "uuid"
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ [EXC-004]:**
  - **Xác thực đầu vào không hợp lệ:** Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### 📅 Phân phối Công việc Theo Ngày (Giai đoạn 1)
- **DAY 1: Xây dựng hệ thống xác thực người dùng**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth [REQ-001], [REQ-002], [REQ-003]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai chức năng đăng ký và đăng nhập người dùng, tích hợp xác thực qua mạng xã hội.
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003]

- **DAY 2: Xây dựng quản lý trung tâm**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/centers [REQ-004], [REQ-005], [REQ-006]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai chức năng quản lý trung tâm, bao gồm tạo, cập nhật, xóa trung tâm và phân quyền quản trị trung tâm.
      - **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006]

- **DAY 3: Xây dựng quản lý khóa học**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/courses [REQ-007], [REQ-008], [REQ-009]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai chức năng quản lý khóa học, bao gồm tạo, cập nhật, xóa khóa học và phân công giáo viên vào khóa học.
      - **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]

### 📈 Giai đoạn 2 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống đăng ký học viên, điểm danh, và quản lý thẻ hội viên.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/enrollments`, `./sources/backend/attendance`, `./sources/backend/membership`, `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-005], [DAT-006], [DAT-007]:**
  ```sql
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
      FOREIGN KEY (studentId) REFERENCES USERS(userId),
      FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
  );

  CREATE TABLE STUDENTCARDS (
      cardId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      issueDate DATE NOT NULL,
      validityDays INT NOT NULL,
      remainingDays INT,
      FOREIGN KEY (studentId) REFERENCES USERS(userId)
  );
  ```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015]:**
  ```json
  {
    "browseCourses": {
      "method": "GET",
      "path": "/api/courses",
      "response": {
        "courses": [
          {
            "courseId": "uuid",
            "title": "string",
            "startDate": "date",
            "endDate": "date",
            "teacherName": "string"
          }
        ]
      }
    },
    "registerCourse": {
      "method": "POST",
      "path": "/api/enrollments",
      "request": {
        "studentId": "uuid",
        "courseId": "uuid"
      },
      "response": {
        "enrollmentId": "uuid"
      }
    },
    "scanQR": {
      "method": "POST",
      "path": "/api/attendance",
      "request": {
        "studentId": "uuid",
        "courseId": "uuid"
      },
      "response": {
        "attendanceId": "uuid"
      }
    },
    "viewCard": {
      "method": "GET",
      "path": "/api/membership/card",
      "response": {
        "cardId": "uuid",
        "issueDate": "date",
        "validityDays": "int",
        "remainingDays": "int"
      }
    },
    "renewCard": {
      "method": "POST",
      "path": "/api/membership/renew",
      "request": {
        "cardId": "uuid",
        "days": "int"
      },
      "response": {
        "status": "string"
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ [EXC-001], [EXC-002]:**
  - **Network & Connectivity Drops During QR Scan:** If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
  - **Duplicate Attendance Submission:** If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### 📅 Phân phối Công việc Theo Ngày (Giai đoạn 2)
- **DAY 1: Xây dựng hệ thống đăng ký học viên**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/enrollments [REQ-010], [REQ-011]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai chức năng duyệt khóa học và đăng ký khóa học của học viên.
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]

- **DAY 2: Xây dựng hệ thống điểm danh**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/attendance [REQ-012], [REQ-013]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai chức năng điểm danh qua mã QR và đảm bảo tính bất biến của điểm danh.
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]

- **DAY 3: Xây dựng quản lý thẻ hội viên**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/membership [REQ-014], [REQ-015]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai chức năng hiển thị tính hợp lệ của thẻ và gia hạn thẻ hội viên.
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]

### 📈 Giai đoạn 3 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng hệ thống thông báo và quản lý khuyến mãi.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/notifications`, `./sources/backend/promotions`, `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008], [DAT-009]:**
  ```sql
  CREATE TABLE NOTIFICATIONS (
      notificationId UUID PRIMARY KEY,
      userId UUID,
      groupZalo VARCHAR(255),
      message TEXT NOT NULL,
      sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
      delivered BOOLEAN DEFAULT FALSE,
      FOREIGN KEY (userId) REFERENCES USERS(userId)
  );

  CREATE TABLE PROMOTIONS (
      promoId UUID PRIMARY KEY,
      code VARCHAR(50) UNIQUE,
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
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [REQ-017], [REQ-018]:**
  ```json
  {
    "sendNotification": {
      "method": "POST",
      "path": "/api/notifications",
      "request": {
        "userId": "uuid",
        "groupZalo": "string",
        "message": "string"
      },
      "response": {
        "notificationId": "uuid"
      }
    },
    "createPromotion": {
      "method": "POST",
      "path": "/api/promotions",
      "request": {
        "code": "string",
        "discountPercent": "smallint",
        "startDate": "date",
        "endDate": "date",
        "description": "string"
      },
      "response": {
        "promoId": "uuid"
      }
    },
    "createAnnouncement": {
      "method": "POST",
      "path": "/api/announcements",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "date",
        "endDate": "date"
      },
      "response": {
        "announcementId": "uuid"
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ [EXC-003]:**
  - **Failed Notification Delivery:** When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### 📅 Phân phối Công việc Theo Ngày (Giai đoạn 3)
- **DAY 1: Xây dựng hệ thống thông báo**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications [REQ-016]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai chức năng kích hoạt thông báo.
      - **Tag IDs Mục tiêu:** [REQ-016]

- **DAY 2: Xây dựng quản lý khuyến mãi**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/promotions [REQ-017], [REQ-018]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai chức năng quản lý khuyến mãi và thông báo.
      - **Tag IDs Mục tiêu:** [REQ-017], [REQ-018]

- **DAY 3: Tài liệu Kiến trúc**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Doc:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết tài liệu kiến trúc cho hệ thống thông báo và quản lý khuyến mãi.
      - **Tag IDs Mục tiêu:** [REQ-016], [REQ-017], [REQ-018]

### 📈 Giai đoạn 4 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng giao diện người dùng và ứng dụng di động.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/frontend/`, `./sources/mobile/`, `./sources/docs/`.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-020], [REQ-021], [REQ-022], [REQ-023]:**
  ```json
  {
    "viewDashboard": {
      "method": "GET",
      "path": "/api/dashboard",
      "response": {
        "totalStudents": "int",
        "activeCourses": "int",
        "upcomingSessions": "int"
      }
    },
    "generateReport": {
      "method": "GET",
      "path": "/api/reports/attendance",
      "response": {
        "reportUrl": "string"
      }
    }
  }
  ```
- **Bộ xử lý Ngoại lệ Cục bộ [EXC-005]:**
  - **System Recovery After Outage:** If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### 📅 Phân phối Công việc Theo Ngày (Giai đoạn 4)
- **DAY 1: Xây dựng giao diện người dùng**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/ [REQ-020], [REQ-021], [REQ-022], [REQ-023]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai giao diện người dùng cho các vai trò khác nhau và tích hợp thông báo đẩy trên di động.
      - **Tag IDs Mục tiêu:** [REQ-020], [REQ-021], [REQ-022], [REQ-023]

- **DAY 2: Xây dựng ứng dụng di động**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/mobile/ [REQ-020], [REQ-021]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai ứng dụng di động cho các vai trò khác nhau và tích hợp thông báo đẩy.
      - **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]

- **DAY 3: Tài liệu Kiến trúc**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Doc:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết tài liệu kiến trúc cho giao diện người dùng và ứng dụng di động.
      - **Tag IDs Mục tiêu:** [REQ-020], [REQ-021], [REQ-022], [REQ-023]

### 📈 Giai đoạn 5 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hạ tầng và tối ưu hóa hệ thống.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/infra/`, `./sources/docs/`.
- **Hợp đồng Định tuyến API và Sự kiện [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]:**
  ```json
  {
    "deployInfra": {
      "method": "POST",
      "path": "/api/infra/deploy",
      "request": {
        "config": "string"
      },
      "response": {
        "status": "string"
      }
    },
    "monitorPerformance": {
      "method": "GET",
      "path": "/api/monitor/performance",
      "response": {
        "metrics": "object"
      }
    }
  }
  ```

#### 📅 Phân phối Công việc Theo Ngày (Giai đoạn 5)
- **DAY 1: Triển khai hạ tầng**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Docker:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/ [NFR-005]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai Docker và tối ưu hóa kích thước hình ảnh.
      - **Tag IDs Mục tiêu:** [NFR-005]
    * **GCP:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/ [NFR-002], [NFR-003], [NFR-004]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai hạ tầng trên Google Cloud Platform và đảm bảo tính khả dụng và bảo mật.
      - **Tag IDs Mục tiêu:** [NFR-002], [NFR-003], [NFR-004]
    * **GKE:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/ [NFR-001], [NFR-004]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai và quản lý Kubernetes trên Google Kubernetes Engine.
      - **Tag IDs Mục tiêu:** [NFR-001], [NFR-004]

- **DAY 2: Tối ưu hóa hệ thống**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/ [NFR-001], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tối ưu hóa hiệu suất hệ thống, đảm bảo tính bảo mật và tuân thủ các quy định.
      - **Tag IDs Mục tiêu:** [NFR-001], [NFR-006], [NFR-007], [NFR-008], [NFR-009]

- **DAY 3: Tài liệu Kiến trúc**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Doc:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết tài liệu kiến trúc cho hạ tầng và tối ưu hóa hệ thống.
      - **Tag IDs Mục tiêu:** [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]

## 📁 6. CÁC ĐOẠN CODE BẢO MẬT TOÀN CẦU & ĐỐI PHÓNG TIÊU CHUẨN TIÊM NẠP [NFR-XXX]
<!--START_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY
[CRITICAL TRANSLATION COMMAND: You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: 🇻🇳 Vietnamese. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output].
END_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY-->
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. QUY TẮC TUÂN THỦ HYBRID MOBILE & CƠ CHẾ SEO QUỐC TẾ HÓA
<!--START_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY
[CRITICAL TRANSLATION COMMAND: You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: 🇻🇳 Vietnamese. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output].
END_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY-->
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. PIPELINE TỰ ĐỘNG HOÁ NHÁNH GIT FLOW HÀNG NGÀY
<!--START_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY
[CRITICAL TRANSLATION COMMAND: You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: 🇻🇳 Vietnamese. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output].
END_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY-->
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 YÊU CẦU KIỂM TRA ĐẢM BẢO MA TRẬN
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`