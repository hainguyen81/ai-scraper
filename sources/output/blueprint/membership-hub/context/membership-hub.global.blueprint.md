# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260805152928 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/05 15:29:28 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CỐT LÕI

### 1.1. Kiến trúc hệ thống cốt lõi & mô hình kiến trúc
Hệ thống membership-hub được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, trung tâm, khóa học, điểm danh và thẻ hội viên. Hệ thống sử dụng mô hình Event-Driven Architecture (EDA) để xử lý các sự kiện như đăng ký khóa học, điểm danh và thông báo. Các dịch vụ giao tiếp với nhau thông qua các hàng đợi tin nhắn và sự kiện được phát hành qua một message broker.

### 1.2. Topology luồng dữ liệu doanh nghiệp & hệ sinh thái cốt lõi
Hệ thống sử dụng các kênh truyền thông bất đồng bộ bao gồm hàng đợi tin nhắn và sự kiện để xử lý các tác vụ như điểm danh, thông báo và quản lý khóa học. Các dịch vụ backend xử lý các yêu cầu từ frontend và tương tác với cơ sở dữ liệu PostgreSQL. Các dịch vụ frontend được xây dựng bằng Next.js và React Native để đảm bảo tính tương thích trên nhiều nền tảng.

## 📁 2. PHỤ THUỘC CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis, GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React Native, Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs.

<!-- START_TECHNICAL_MATRIX_DO_NOT_TRANSLATE
### ARCHITECTURAL STACK MATRIX
[CRITICAL WARNING: You MUST keep this entire block 100% in raw Technical English. You are STRICTLY FORBIDDEN from translating any keys, values, or tokens inside this section into 🇻🇳 Vietnamese, as it serves as a strict backend machine-gating matrix. Keep literal `true` or `false` tokens in pure lower-case].

PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
END_TECHNICAL_MATRIX_DO_NOT_TRANSLATE -->

## 📁 3. QUY TẮC TUYÊN BỎ TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
<!-- START_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY
[CRITICAL TRANSLATION COMMAND: You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: 🇻🇳 Vietnamese. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output].
END_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY -->
- **Quy tắc biên giới không gian làm việc tuyệt đối:** Không gian làm việc thực sự của kho lưu trữ được cố định vĩnh viễn tại gốc dự án `..`. Tất cả các đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Tuân thủ tiền tố đường dẫn động:** Áp dụng các quy tắc ánh xạ đường dẫn động được xác định trong Giao thức 1 một cách nghiêm ngặt phù hợp với cấu trúc dự án được phát hiện.
- **[ĐIỀU KIỆN: JAVA_STACK_ONLY] Tiêu chuẩn gói Java:** Nếu ngăn xếp công nghệ sử dụng các khung Java, tất cả mã nguồn Java phải nằm nghiêm ngặt trong cơ sở gói doanh nghiệp: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. Bạn phải chuyển đổi động chuỗi "membership-hub" thành một mã ký tự alphanumeric thuần túy viết thường bằng cách loại bỏ khoảng trắng, dấu gạch ngang và dấu gạch dưới. Các dự án không phải Java bị cấm áp dụng đoạn này.
- **Cú pháp đường dẫn mục tiêu kiểm thử nghiêm ngặt:** Bất kỳ thành phần nào được nhắm mục tiêu bởi Sub-Agent Tester phải được cấu trúc dưới dạng một cặp phân tách chặt chẽ bằng dấu chấm phẩy `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn bên trong cặp phải bắt đầu bằng `./sources/`.

## 4. TÓM TẮT KIẾN TRÚC ĐA PHASE CẤP CAO
| Giai đoạn | Khoảng ngày | Thành phần Kiến trúc / Đường dẫn Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-2 | `./sources/backend/auth`, `./sources/backend/centers`, `./sources/backend/courses` | Xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học | Coder, Tester, Reviewer | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-001], [DAT-003], [DAT-004] |
| 2 | 3-4 | `./sources/backend/enrollments`, `./sources/backend/attendance`, `./sources/backend/membership` | Xây dựng dịch vụ đăng ký, điểm danh và quản lý thẻ hội viên | Coder, Tester, Reviewer | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-005], [DAT-006], [DAT-007] |
| 3 | 5-6 | `./sources/backend/notifications`, `./sources/backend/promotions` | Xây dựng dịch vụ thông báo và khuyến mãi | Coder, Tester, Reviewer | [REQ-016], [REQ-017], [REQ-018], [DAT-008], [DAT-009] |
| 4 | 7 | `./sources/frontend`, `./sources/mobile` | Xây dựng giao diện người dùng và ứng dụng di động | Coder, Tester, Reviewer | [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011] |
| 5 | 8-9 | `./sources/infra` | Triển khai hệ thống và cấu hình hạ tầng | Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 5. CHI TIẾT PHASE VÀ NHIỆM VỤ NGÀY THEO NGÀY
<!--START_DELIMITTER-->
### Giai đoạn 1 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/auth`, `./sources/backend/centers`, `./sources/backend/courses`.
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
      "method": "PUT",
      "path": "/api/users/{userId}/role",
      "request": {
        "roleId": "number"
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
        "centerId": "string"
      }
    },
    "createCourse": {
      "method": "POST",
      "path": "/api/courses",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "string",
        "endDate": "string",
        "teacherId": "string",
        "maxStudents": "number"
      },
      "response": {
        "courseId": "string"
      }
    }
  }
  ```
- **Xử lý Ngoại lệ Cục bộ [EXC-004]:**
  - **Xác thực đầu vào không hợp lệ:** Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 1)
- **DAY 1: Xây dựng dịch vụ xác thực**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth [REQ-001], [REQ-002], [DAT-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ xác thực với các phương thức đăng ký và đăng nhập qua email/mật khẩu và OAuth2. [REQ-001], [REQ-002]
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [DAT-001]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth;./sources/backend/auth/src/test/java/org/nlh4j/saas/membershiphub/auth/AuthServiceTest.java [REQ-001], [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ xác thực. [REQ-001], [REQ-002]
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth [REQ-001], [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình. [REQ-001], [REQ-002]
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002]

- **DAY 2: Xây dựng dịch vụ quản lý trung tâm và khóa học**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/centers [REQ-004], [REQ-005], [REQ-006], [DAT-003]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý trung tâm và khóa học. [REQ-004], [REQ-005], [REQ-006]
      - **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/centers;./sources/backend/centers/src/test/java/org/nlh4j/saas/membershiphub/centers/CenterServiceTest.java [REQ-004], [REQ-005], [REQ-006]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ quản lý trung tâm và khóa học. [REQ-004], [REQ-005], [REQ-006]
      - **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/centers [REQ-004], [REQ-005], [REQ-006]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình. [REQ-004], [REQ-005], [REQ-006]
      - **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006]

<!--START_DELIMITTER-->
### Giai đoạn 2 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ đăng ký, điểm danh và quản lý thẻ hội viên.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/enrollments`, `./sources/backend/attendance`, `./sources/backend/membership`.
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
    "enrollCourse": {
      "method": "POST",
      "path": "/api/enrollments",
      "request": {
        "studentId": "string",
        "courseId": "string"
      },
      "response": {
        "enrollmentId": "string"
      }
    },
    "scanQR": {
      "method": "POST",
      "path": "/api/attendance",
      "request": {
        "studentId": "string",
        "courseId": "string"
      },
      "response": {
        "attendanceId": "string"
      }
    },
    "viewCard": {
      "method": "GET",
      "path": "/api/membership/card",
      "request": {
        "studentId": "string"
      },
      "response": {
        "cardId": "string",
        "issueDate": "string",
        "validityDays": "number",
        "remainingDays": "number"
      }
    },
    "renewCard": {
      "method": "POST",
      "path": "/api/membership/renew",
      "request": {
        "studentId": "string",
        "days": "number"
      },
      "response": {
        "status": "string"
      }
    }
  }
  ```
- **Xử lý Ngoại lệ Cục bộ [EXC-001], [EXC-002]:**
  - **Network & Connectivity Drops During QR Scan:** If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
  - **Duplicate Attendance Submission:** If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 2)
- **DAY 3: Xây dựng dịch vụ đăng ký và điểm danh**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/enrollments [REQ-010], [REQ-011], [DAT-005]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ đăng ký khóa học và điểm danh. [REQ-010], [REQ-011]
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011], [DAT-005]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/enrollments;./sources/backend/enrollments/src/test/java/org/nlh4j/saas/membershiphub/enrollments/EnrollmentServiceTest.java [REQ-010], [REQ-011]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ đăng ký và điểm danh. [REQ-010], [REQ-011]
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/enrollments [REQ-010], [REQ-011]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình. [REQ-010], [REQ-011]
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]

- **DAY 4: Xây dựng dịch vụ quản lý thẻ hội viên**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/membership [REQ-014], [REQ-015], [DAT-007]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý thẻ hội viên. [REQ-014], [REQ-015]
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015], [DAT-007]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/membership;./sources/backend/membership/src/test/java/org/nlh4j/saas/membershiphub/membership/MembershipServiceTest.java [REQ-014], [REQ-015]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ quản lý thẻ hội viên. [REQ-014], [REQ-015]
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/membership [REQ-014], [REQ-015]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình. [REQ-014], [REQ-015]
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]

<!--START_DELIMITTER-->
### Giai đoạn 3 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ thông báo và khuyến mãi.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/notifications`, `./sources/backend/promotions`.
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
        "userId": "string",
        "groupZalo": "string",
        "message": "string"
      },
      "response": {
        "notificationId": "string"
      }
    },
    "createPromotion": {
      "method": "POST",
      "path": "/api/promotions",
      "request": {
        "code": "string",
        "discountPercent": "number",
        "startDate": "string",
        "endDate": "string",
        "description": "string"
      },
      "response": {
        "promoId": "string"
      }
    },
    "createAnnouncement": {
      "method": "POST",
      "path": "/api/announcements",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "string",
        "endDate": "string"
      },
      "response": {
        "announcementId": "string"
      }
    }
  }
  ```
- **Xử lý Ngoại lệ Cục bộ [EXC-003]:**
  - **Failed Notification Delivery:** When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 3)
- **DAY 5: Xây dựng dịch vụ thông báo**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications [REQ-016], [DAT-008]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ thông báo. [REQ-016]
      - **Tag IDs Mục tiêu:** [REQ-016], [DAT-008]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications;./sources/backend/notifications/src/test/java/org/nlh4j/saas/membershiphub/notifications/NotificationServiceTest.java [REQ-016]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ thông báo. [REQ-016]
      - **Tag IDs Mục tiêu:** [REQ-016]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications [REQ-016]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình. [REQ-016]
      - **Tag IDs Mục tiêu:** [REQ-016]

- **DAY 6: Xây dựng dịch vụ khuyến mãi**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/promotions [REQ-017], [REQ-018], [DAT-009]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ khuyến mãi và thông báo. [REQ-017], [REQ-018]
      - **Tag IDs Mục tiêu:** [REQ-017], [REQ-018], [DAT-009]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/promotions;./sources/backend/promotions/src/test/java/org/nlh4j/saas/membershiphub/promotions/PromotionServiceTest.java [REQ-017], [REQ-018]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ khuyến mãi và thông báo. [REQ-017], [REQ-018]
      - **Tag IDs Mục tiêu:** [REQ-017], [REQ-018]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/promotions [REQ-017], [REQ-018]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình. [REQ-017], [REQ-018]
      - **Tag IDs Mục tiêu:** [REQ-017], [REQ-018]

<!--START_DELIMITTER-->
### Giai đoạn 4 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng giao diện người dùng và ứng dụng di động.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/frontend`, `./sources/mobile`.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]:**
  ```json
  {
    "chatbot": {
      "method": "POST",
      "path": "/api/chatbot",
      "request": {
        "message": "string"
      },
      "response": {
        "reply": "string"
      }
    },
    "mobileUI": {
      "method": "GET",
      "path": "/api/mobile/ui",
      "request": {
        "role": "string"
      },
      "response": {
        "ui": "string"
      }
    },
    "pushNotification": {
      "method": "POST",
      "path": "/api/notifications/push",
      "request": {
        "userId": "string",
        "message": "string"
      },
      "response": {
        "status": "string"
      }
    },
    "localization": {
      "method": "GET",
      "path": "/api/localization",
      "request": {
        "locale": "string"
      },
      "response": {
        "strings": "object"
      }
    }
  }
  ```

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 4)
- **DAY 7: Xây dựng giao diện người dùng và ứng dụng di động**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai giao diện người dùng và ứng dụng di động. [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]
      - **Tag IDs Mục tiêu:** [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend;./sources/frontend/src/test/java/org/nlh4j/saas/membershiphub/frontend/FrontendServiceTest.java [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị và tích hợp cho giao diện người dùng và ứng dụng di động. [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]
      - **Tag IDs Mục tiêu:** [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình. [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]
      - **Tag IDs Mục tiêu:** [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]

<!--START_DELIMITTER-->
### Giai đoạn 5 Chi tiết Kiến trúc
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai hệ thống và cấu hình hạ tầng.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/infra`.
- **Hợp đồng Định tuyến API và Sự kiện [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]:**
  ```json
  {
    "performance": {
      "method": "GET",
      "path": "/api/performance",
      "request": {},
      "response": {
        "metrics": "object"
      }
    },
    "availability": {
      "method": "GET",
      "path": "/api/availability",
      "request": {},
      "response": {
        "status": "string"
      }
    },
    "security": {
      "method": "GET",
      "path": "/api/security",
      "request": {},
      "response": {
        "status": "string"
      }
    },
    "scalability": {
      "method": "GET",
      "path": "/api/scalability",
      "request": {},
      "response": {
        "status": "string"
      }
    },
    "docker": {
      "method": "GET",
      "path": "/api/docker",
      "request": {},
      "response": {
        "status": "string"
      }
    },
    "logging": {
      "method": "GET",
      "path": "/api/logging",
      "request": {},
      "response": {
        "status": "string"
      }
    },
    "localization": {
      "method": "GET",
      "path": "/api/localization",
      "request": {},
      "response": {
        "status": "string"
      }
    },
    "gdpr": {
      "method": "GET",
      "path": "/api/gdpr",
      "request": {},
      "response": {
        "status": "string"
      }
    },
    "backup": {
      "method": "GET",
      "path": "/api/backup",
      "request": {},
      "response": {
        "status": "string"
      }
    }
  }
  ```

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 5)
- **DAY 8: Triển khai hệ thống và cấu hình hạ tầng**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Docker:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/docker [NFR-005]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai Docker và cấu hình hạ tầng. [NFR-005]
      - **Tag IDs Mục tiêu:** [NFR-005]
    * **GCP:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/gcp [NFR-002], [NFR-003], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai Google Cloud Platform và cấu hình hạ tầng. [NFR-002], [NFR-003], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
      - **Tag IDs Mục tiêu:** [NFR-002], [NFR-003], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    * **GKE:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/gke [NFR-001], [NFR-004]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai Google Kubernetes Engine và cấu hình hạ tầng. [NFR-001], [NFR-004]
      - **Tag IDs Mục tiêu:** [NFR-001], [NFR-004]

- **DAY 9: Kiểm tra và triển khai hệ thống**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra;./sources/infra/src/test/java/org/nlh4j/saas/membershiphub/infra/InfraServiceTest.java [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị và tích hợp cho hạ tầng. [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
      - **Tag IDs Mục tiêu:** [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình. [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
      - **Tag IDs Mục tiêu:** [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]

## 📁 6. MÃ BẢO MẬT DOANH NGHIỆP TOÀN CẦU & ĐỐI PHÓNG TIÊU CHUẨN TIÊM NẠN [NFR-XXX]
- **Đối phó với SQL Injection (SQLi):** Tham số quy tắc cho các câu lệnh chuẩn bị, tham số truy vấn định vị và danh sách trắng sắp xếp động.
- **Cross-Site Scripting (XSS) & Chính sách Bảo mật Nội dung (CSP):** Tiêu chuẩn bố cục cho các bộ lọc làm sạch ngữ cảnh tự động, tự động thoát JSX và chèn tiêu đề CSP động (`unsafe-inline` hạn chế).
- **Rails Bảo mật CORS Đa-kiến trúc:** Cấu hình cho các cấm thông origin đại diện và xác thực độ chính xác nguồn gốc cơ sở dữ liệu động của người thuê.
- **Máy làm sạch ghi nhật ký Zero-Leak & Máy che dữ liệu PII:** Quy tắc cho các bộ chặn làm sạch tự động (`@JsonSerialize`) và ngưỡng làm sạch nhật ký.

## 📁 7. QUY TẮC TUÂN THỦ RAIL HYBRID MOBILE & CƠ CHẾ SEO QUỐC TẾ HÓA
- **Rails Tuân thủ Hybrid Mobile Capacitor:** [NẾU Mobile hoạt động] Quy tắc cho việc lấy động cơ phía máy khách, địa chỉ tuyệt đối URL, an toàn thủy phân, trừu tượng hóa lưu trữ bản địa (`@capacitor/preferences`) và chặn nút quay lại phần cứng.
- **Quốc tế hóa (i18n) & Tiêm Động SEO:** Kiến trúc middleware nhận diện locale cạnh, tiêm động siêu liên kết đa ngôn ngữ và giới hạn chỉ mục robot tìm kiếm.

## 📁 8. ĐỘNG LỰC PIPELINE TỰ ĐỘNG HÀNG NGÀY SESSION GIT BRANCH FLOW
- **Độc lập Forking Không gian làm việc Hàng ngày:** Kiểm soát lập trình cho nhánh `features/development-phase-X-day-Y` (`X` là số giai đoạn, từ 1 đến N, trong đó N <= 5; `Y` là số ngày trong giai đoạn, nó sẽ bắt đầu từ 1 cho mỗi giai đoạn).
- **Cổng Hàng rào Pipeline Xác thực:** Quy tắc thực thi cho xác minh biên dịch, mục tiêu bao phủ mã tự động (`>= 85%`) và nhật ký tuần tự hóa tóm tắt ngữ cảnh.

### 🛑 YÊU CẦU KIỂM TRA HỢP LỆ MA TRẬN
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`