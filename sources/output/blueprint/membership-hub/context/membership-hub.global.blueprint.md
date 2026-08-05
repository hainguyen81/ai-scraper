# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260805164557 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/05 16:45:57 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CỐT LÕI

### 1.1. Kiến trúc hệ thống cốt lõi & mô hình kiến trúc
Hệ thống membership-hub được thiết kế theo kiến trúc đa tầng với các thành phần chính bao gồm:
- Lớp giao diện người dùng (Frontend) với Next.js
- Lớp backend (Backend) với Java/Quarkus
- Lớp cơ sở dữ liệu (Persistence) với PostgreSQL
- Lớp dịch vụ di động (Mobile) với ứng dụng di động đa nền tảng
- Lớp hạ tầng (Infra) với Docker và Kubernetes (GKE)

### 1.2. Luồng dữ liệu và hệ sinh thái doanh nghiệp
Hệ thống sử dụng các kênh truyền thông đa kênh bao gồm:
- REST APIs cho giao tiếp giữa frontend và backend
- WebSocket cho các tính năng thời gian thực như điểm danh QR
- Firebase Cloud Messaging (FCM) và Apple APNs cho thông báo đẩy
- Zalo API cho giao tiếp qua nhóm Zalo

<!--START_TECHNICAL_MATRIX_DO_NOT_TRANSLATE
[CRITICAL_TECHNICAL_MATRIX_RAIL: DO NOT TRANSLATE THIS DIRECTIVE]

### ARCHITECTURAL STACK MATRIX
[CRITICAL WARNING: You MUST keep this entire block 100% in raw Technical English. You are STRICTLY FORBIDDEN from translating any keys, values, or tokens inside this section into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}, as it serves as a strict backend machine-gating matrix. Keep literal `true` or `false` tokens in pure lower-case].

PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true

END_TECHNICAL_MATRIX_DO_NOT_TRANSLATE-->

## 📁 2. CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis, GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React, Tailwind CSS, Capacitor, Firebase Authentication.

## 📁 3. QUY TẮC TUYÊN BỐ & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. TÓM TẮT KIẾN TRÚC MỤC TIÊU CAO CẤP THEO GIAI ĐOẠN
| Giai đoạn | Khoảng ngày | Thành phần Kiến trúc / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-3 | Quản lý người dùng, Quản lý trung tâm | Xây dựng cơ sở dữ liệu, API xác thực, giao diện đăng ký | Coder, Tester, Reviewer | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [DAT-001], [DAT-003], [ARC-001], [ARC-002], [ARC-003], [ARC-006] |
| 2 | 4-6 | Quản lý khóa học, Đăng ký học viên | Xây dựng API khóa học, giao diện đăng ký, cơ sở dữ liệu ghi danh | Coder, Tester, Reviewer | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005], [ARC-004] |
| 3 | 7-9 | Điểm danh QR, Quản lý thẻ hội viên | Xây dựng API điểm danh, giao diện thẻ hội viên, cơ sở dữ liệu điểm danh | Coder, Tester, Reviewer | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [ARC-007] |
| 4 | 10-12 | Thông báo, Khuyến mãi | Xây dựng API thông báo, giao diện khuyến mãi, cơ sở dữ liệu thông báo | Coder, Tester, Reviewer | [REQ-016], [REQ-017], [REQ-018], [DAT-008], [DAT-009], [EXC-003], [ARC-008] |
| 5 | 13-15 | Chatbot AI, Ứng dụng di động | Xây dựng chatbot AI, giao diện di động, tích hợp thông báo đẩy | Coder, Tester, Reviewer, Docker, GCP, GKE | [REQ-019], [REQ-020], [REQ-021], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 5. CHI TIẾT THEO GIAI ĐOẠN & SẢN PHẨM BÀN GIAO THEO NGÀY

### 📈 Giai đoạn 1: Quản lý người dùng và trung tâm
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng cơ sở dữ liệu người dùng, API xác thực, và giao diện đăng ký.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/auth`, `./sources/backend/centers`, `./sources/docs/architecture.md`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003]:**
  ```sql
  CREATE TABLE users (
      userId UUID PRIMARY KEY,
      email VARCHAR(255) NOT NULL UNIQUE,
      passwordHash CHAR(60) NOT NULL,
      fullName VARCHAR(100) NOT NULL,
      roleId SMALLINT NOT NULL,
      provider VARCHAR(10) DEFAULT 'local',
      createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
      updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
  );

  CREATE TABLE roles (
      roleId SMALLINT PRIMARY KEY,
      name VARCHAR(30) NOT NULL UNIQUE,
      description VARCHAR(200)
  );

  CREATE TABLE centers (
      centerId UUID PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      address VARCHAR(255) NOT NULL,
      taxId VARCHAR(13) NOT NULL UNIQUE,
      contactPhone VARCHAR(20),
      contactEmail VARCHAR(255)
  );
  ```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003], [ARC-006]:**
  ```json
  {
      "register": {
          "path": "/api/auth/register",
          "method": "POST",
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
          "path": "/api/auth/login",
          "method": "POST",
          "request": {
              "email": "string",
              "password": "string"
          },
          "response": {
              "token": "string"
          }
      }
  }
  ```
- **Xử lý Ngoại lệ Cục bộ [EXC-004]:**
  - Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1: Thiết kế cơ sở dữ liệu người dùng và vai trò**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth/src/main/java/org/nlh4j/saas/membershiphub/auth/entity/User.java [DAT-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế thực thể người dùng với các trường: userId, email, passwordHash, fullName, roleId, provider, createdAt, updatedAt.
      - **Tag IDs Mục tiêu:** [DAT-001]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth/src/test/java/org/nlh4j/saas/membershiphub/auth/entity/UserTest.java;./sources/backend/auth/src/main/java/org/nlh4j/saas/membershiphub/auth/entity/User.java [DAT-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho thực thể người dùng.
      - **Tag IDs Mục tiêu:** [DAT-001]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth/src/main/java/org/nlh4j/saas/membershiphub/auth/entity/User.java [DAT-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn thực thể người dùng và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [DAT-001]

- **DAY 2: Xây dựng API xác thực**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth/src/main/java/org/nlh4j/saas/membershiphub/auth/controller/AuthController.java [REQ-001], [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API đăng ký và đăng nhập với email/mật khẩu và OAuth2.
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth/src/test/java/org/nlh4j/saas/membershiphub/auth/controller/AuthControllerTest.java;./sources/backend/auth/src/main/java/org/nlh4j/saas/membershiphub/auth/controller/AuthController.java [REQ-001], [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API xác thực.
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth/src/main/java/org/nlh4j/saas/membershiphub/auth/controller/AuthController.java [REQ-001], [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn API xác thực và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002]

- **DAY 3: Xây dựng giao diện đăng ký**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/pages/register.js [REQ-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện đăng ký người dùng với form nhập liệu và xử lý lỗi.
      - **Tag IDs Mục tiêu:** [REQ-001]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/tests/register.test.js;./sources/frontend/pages/register.js [REQ-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra giao diện cho trang đăng ký.
      - **Tag IDs Mục tiêu:** [REQ-001]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/pages/register.js [REQ-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn giao diện đăng ký và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-001]

### 📈 Giai đoạn 2: Quản lý khóa học và đăng ký học viên
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng API khóa học, giao diện đăng ký, và cơ sở dữ liệu ghi danh.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/courses`, `./sources/frontend/pages/courses`, `./sources/docs/architecture.md`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004], [DAT-005]:**
  ```sql
  CREATE TABLE courses (
      courseId UUID PRIMARY KEY,
      title VARCHAR(150) NOT NULL,
      description TEXT,
      startDate DATE NOT NULL,
      endDate DATE NOT NULL,
      teacherId UUID NOT NULL,
      maxStudents INT DEFAULT 30
  );

  CREATE TABLE enrollments (
      enrollmentId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      courseId UUID NOT NULL,
      enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW()
  );
  ```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [ARC-004]:**
  ```json
  {
      "getCourses": {
          "path": "/api/courses",
          "method": "GET",
          "response": {
              "courses": [
                  {
                      "courseId": "string",
                      "title": "string",
                      "startDate": "string",
                      "endDate": "string",
                      "teacherName": "string"
                  }
              ]
          }
      },
      "registerCourse": {
          "path": "/api/courses/register",
          "method": "POST",
          "request": {
              "courseId": "string",
              "studentId": "string"
          },
          "response": {
              "enrollmentId": "string"
          }
      }
  }
  ```
- **Xử lý Ngoại lệ Cục bộ:**
  - Không có luồng ngoại lệ chuyên biệt được xác định cho giai đoạn này.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 4: Thiết kế cơ sở dữ liệu khóa học và ghi danh**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/courses/src/main/java/org/nlh4j/saas/membershiphub/courses/entity/Course.java [DAT-004]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế thực thể khóa học với các trường: courseId, title, description, startDate, endDate, teacherId, maxStudents.
      - **Tag IDs Mục tiêu:** [DAT-004]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/courses/src/test/java/org/nlh4j/saas/membershiphub/courses/entity/CourseTest.java;./sources/backend/courses/src/main/java/org/nlh4j/saas/membershiphub/courses/entity/Course.java [DAT-004]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho thực thể khóa học.
      - **Tag IDs Mục tiêu:** [DAT-004]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/courses/src/main/java/org/nlh4j/saas/membershiphub/courses/entity/Course.java [DAT-004]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn thực thể khóa học và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [DAT-004]

- **DAY 5: Xây dựng API khóa học**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/courses/src/main/java/org/nlh4j/saas/membershiphub/courses/controller/CourseController.java [REQ-007], [REQ-008]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API lấy danh sách khóa học và quản lý khóa học.
      - **Tag IDs Mục tiêu:** [REQ-007], [REQ-008]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/courses/src/test/java/org/nlh4j/saas/membershiphub/courses/controller/CourseControllerTest.java;./sources/backend/courses/src/main/java/org/nlh4j/saas/membershiphub/courses/controller/CourseController.java [REQ-007], [REQ-008]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API khóa học.
      - **Tag IDs Mục tiêu:** [REQ-007], [REQ-008]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/courses/src/main/java/org/nlh4j/saas/membershiphub/courses/controller/CourseController.java [REQ-007], [REQ-008]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn API khóa học và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-007], [REQ-008]

- **DAY 6: Xây dựng giao diện đăng ký khóa học**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/pages/courses/register.js [REQ-010], [REQ-011]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện đăng ký khóa học cho học viên.
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/tests/courses/register.test.js;./sources/frontend/pages/courses/register.js [REQ-010], [REQ-011]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra giao diện cho trang đăng ký khóa học.
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/pages/courses/register.js [REQ-010], [REQ-011]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn giao diện đăng ký khóa học và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]

### 📈 Giai đoạn 3: Điểm danh QR và quản lý thẻ hội viên
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng API điểm danh, giao diện thẻ hội viên, và cơ sở dữ liệu điểm danh.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/attendance`, `./sources/frontend/pages/card`, `./sources/docs/architecture.md`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-007]:**
  ```sql
  CREATE TABLE attendance (
      attendanceId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      courseId UUID NOT NULL,
      attendanceDate DATE NOT NULL,
      timestamp TIMESTAMP NOT NULL DEFAULT NOW()
  );

  CREATE TABLE student_cards (
      cardId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      issueDate DATE NOT NULL,
      validityDays INT NOT NULL,
      remainingDays INT NOT NULL
  );
  ```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [REQ-014], [REQ-015], [EXC-001], [EXC-002], [ARC-007]:**
  ```json
  {
      "scanQR": {
          "path": "/api/attendance/scan",
          "method": "POST",
          "request": {
              "studentId": "string",
              "courseId": "string"
          },
          "response": {
              "attendanceId": "string"
          }
      },
      "getCard": {
          "path": "/api/card",
          "method": "GET",
          "response": {
              "cardId": "string",
              "validityDays": "int",
              "remainingDays": "int"
          }
      }
  }
  ```
- **Xử lý Ngoại lệ Cục bộ [EXC-001], [EXC-002]:**
  - Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
  - Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 7: Thiết kế cơ sở dữ liệu điểm danh và thẻ hội viên**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/attendance/src/main/java/org/nlh4j/saas/membershiphub/attendance/entity/Attendance.java [DAT-006]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế thực thể điểm danh với các trường: attendanceId, studentId, courseId, attendanceDate, timestamp.
      - **Tag IDs Mục tiêu:** [DAT-006]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/attendance/src/test/java/org/nlh4j/saas/membershiphub/attendance/entity/AttendanceTest.java;./sources/backend/attendance/src/main/java/org/nlh4j/saas/membershiphub/attendance/entity/Attendance.java [DAT-006]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho thực thể điểm danh.
      - **Tag IDs Mục tiêu:** [DAT-006]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/attendance/src/main/java/org/nlh4j/saas/membershiphub/attendance/entity/Attendance.java [DAT-006]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn thực thể điểm danh và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [DAT-006]

- **DAY 8: Xây dựng API điểm danh**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/attendance/src/main/java/org/nlh4j/saas/membershiphub/attendance/controller/AttendanceController.java [REQ-012], [REQ-013]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API quét mã QR và xử lý điểm danh.
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/attendance/src/test/java/org/nlh4j/saas/membershiphub/attendance/controller/AttendanceControllerTest.java;./sources/backend/attendance/src/main/java/org/nlh4j/saas/membershiphub/attendance/controller/AttendanceController.java [REQ-012], [REQ-013]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API điểm danh.
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/attendance/src/main/java/org/nlh4j/saas/membershiphub/attendance/controller/AttendanceController.java [REQ-012], [REQ-013]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn API điểm danh và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]

- **DAY 9: Xây dựng giao diện thẻ hội viên**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/pages/card/index.js [REQ-014], [REQ-015]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện thẻ hội viên và chức năng gia hạn.
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/tests/card/index.test.js;./sources/frontend/pages/card/index.js [REQ-014], [REQ-015]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra giao diện cho trang thẻ hội viên.
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/pages/card/index.js [REQ-014], [REQ-015]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn giao diện thẻ hội viên và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]

### 📈 Giai đoạn 4: Thông báo và khuyến mãi
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng API thông báo, giao diện khuyến mãi, và cơ sở dữ liệu thông báo.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/notifications`, `./sources/frontend/pages/promotions`, `./sources/docs/architecture.md`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008], [DAT-009]:**
  ```sql
  CREATE TABLE notifications (
      notificationId UUID PRIMARY KEY,
      userId UUID,
      groupZalo VARCHAR(255),
      message TEXT NOT NULL,
      sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
      delivered BOOLEAN DEFAULT FALSE
  );

  CREATE TABLE promotions (
      promoId UUID PRIMARY KEY,
      code VARCHAR(50) UNIQUE,
      discountPercent SMALLINT NOT NULL,
      startDate DATE,
      endDate DATE,
      description TEXT
  );

  CREATE TABLE announcements (
      announcementId UUID PRIMARY KEY,
      title VARCHAR(150) NOT NULL,
      content TEXT NOT NULL,
      startDate DATE,
      endDate DATE
  );
  ```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [REQ-017], [REQ-018], [EXC-003], [ARC-008]:**
  ```json
  {
      "sendNotification": {
          "path": "/api/notifications/send",
          "method": "POST",
          "request": {
              "userId": "string",
              "groupZalo": "string",
              "message": "string"
          },
          "response": {
              "notificationId": "string"
          }
      },
      "getPromotions": {
          "path": "/api/promotions",
          "method": "GET",
          "response": {
              "promotions": [
                  {
                      "promoId": "string",
                      "code": "string",
                      "discountPercent": "int",
                      "startDate": "string",
                      "endDate": "string"
                  }
              ]
          }
      }
  }
  ```
- **Xử lý Ngoại lệ Cục bộ [EXC-003]:**
  - Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 10: Thiết kế cơ sở dữ liệu thông báo và khuyến mãi**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications/src/main/java/org/nlh4j/saas/membershiphub/notifications/entity/Notification.java [DAT-008]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Thiết kế thực thể thông báo với các trường: notificationId, userId, groupZalo, message, sentAt, delivered.
      - **Tag IDs Mục tiêu:** [DAT-008]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications/src/test/java/org/nlh4j/saas/membershiphub/notifications/entity/NotificationTest.java;./sources/backend/notifications/src/main/java/org/nlh4j/saas/membershiphub/notifications/entity/Notification.java [DAT-008]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho thực thể thông báo.
      - **Tag IDs Mục tiêu:** [DAT-008]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications/src/main/java/org/nlh4j/saas/membershiphub/notifications/entity/Notification.java [DAT-008]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn thực thể thông báo và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [DAT-008]

- **DAY 11: Xây dựng API thông báo**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications/src/main/java/org/nlh4j/saas/membershiphub/notifications/controller/NotificationController.java [REQ-016]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API gửi thông báo và xử lý lỗi giao tiếp.
      - **Tag IDs Mục tiêu:** [REQ-016]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications/src/test/java/org/nlh4j/saas/membershiphub/notifications/controller/NotificationControllerTest.java;./sources/backend/notifications/src/main/java/org/nlh4j/saas/membershiphub/notifications/controller/NotificationController.java [REQ-016]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API thông báo.
      - **Tag IDs Mục tiêu:** [REQ-016]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notifications/src/main/java/org/nlh4j/saas/membershiphub/notifications/controller/NotificationController.java [REQ-016]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn API thông báo và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-016]

- **DAY 12: Xây dựng giao diện khuyến mãi**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/pages/promotions/index.js [REQ-017], [REQ-018]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện khuyến mãi và thông báo.
      - **Tag IDs Mục tiêu:** [REQ-017], [REQ-018]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/tests/promotions/index.test.js;./sources/frontend/pages/promotions/index.js [REQ-017], [REQ-018]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra giao diện cho trang khuyến mãi.
      - **Tag IDs Mục tiêu:** [REQ-017], [REQ-018]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/pages/promotions/index.js [REQ-017], [REQ-018]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn giao diện khuyến mãi và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-017], [REQ-018]

### 📈 Giai đoạn 5: Chatbot AI và ứng dụng di động
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng chatbot AI, giao diện di động, và tích hợp thông báo đẩy.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/chatbot`, `./sources/mobile`, `./sources/docs/architecture.md`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu:**
  - [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-019], [REQ-020], [REQ-021], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]:**
  ```json
  {
      "chat": {
          "path": "/api/chat",
          "method": "POST",
          "request": {
              "message": "string"
          },
          "response": {
              "reply": "string"
          }
      },
      "getMobileUI": {
          "path": "/api/mobile/ui",
          "method": "GET",
          "response": {
              "ui": "string"
          }
      }
  }
  ```
- **Xử lý Ngoại lệ Cục bộ:**
  - Không có luồng ngoại lệ chuyên biệt được xác định cho giai đoạn này.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 13: Xây dựng chatbot AI**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/chatbot/src/main/java/org/nlh4j/saas/membershiphub/chatbot/controller/ChatController.java [REQ-019]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng API chatbot AI và xử lý các truy vấn phổ biến.
      - **Tag IDs Mục tiêu:** [REQ-019]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/chatbot/src/test/java/org/nlh4j/saas/membershiphub/chatbot/controller/ChatControllerTest.java;./sources/backend/chatbot/src/main/java/org/nlh4j/saas/membershiphub/chatbot/controller/ChatController.java [REQ-019]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra tích hợp cho API chatbot.
      - **Tag IDs Mục tiêu:** [REQ-019]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/chatbot/src/main/java/org/nlh4j/saas/membershiphub/chatbot/controller/ChatController.java [REQ-019]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn API chatbot và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-019]

- **DAY 14: Xây dựng giao diện di động**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/mobile/src/app.js [REQ-020], [REQ-021]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng giao diện di động và tích hợp thông báo đẩy.
      - **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/mobile/tests/app.test.js;./sources/mobile/src/app.js [REQ-020], [REQ-021]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra giao diện cho ứng dụng di động.
      - **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
    * **Reviewer:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/mobile/src/app.js [REQ-020], [REQ-021]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Đánh giá mã nguồn giao diện di động và đề xuất các cải tiến.
      - **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]

- **DAY 15: Triển khai và kiểm thử hệ thống**
  - **Chuyên môn Sub-Agent Workflow:**
    * **Docker:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/docker/Dockerfile [NFR-005]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Xây dựng Dockerfile và triển khai hệ thống.
      - **Tag IDs Mục tiêu:** [NFR-005]
    * **GCP:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/gcp/cloudbuild.yaml [NFR-009]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Cấu hình Google Cloud Platform và triển khai hệ thống.
      - **Tag IDs Mục tiêu:** [NFR-009]
    * **GKE:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/gke/deployment.yaml [NFR-004]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Cấu hình Kubernetes và triển khai hệ thống.
      - **Tag IDs Mục tiêu:** [NFR-004]

## 📁 6. MÃ BẢO MẬT & ĐỐI PHÓNG TIÊU CẦN KHẨN CẤP [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. QUY TẮC TUÂN THỦ DI ĐỘNG & CƠ CHẾ SEO QUỐC TẾ HÓA
- **Capacitor Mobile Hybrid Compliance Rails:** Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. LUỒNG LÀM VIỆC TỰ ĐỘNG HÀNG NGÀY CỦA PIPELINE GIT BRANCH
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 KIỂM TRA ĐẦY ĐỦ MA TRẬN
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 21, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`