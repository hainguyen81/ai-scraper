# NGÀNH ĐỐI TƯỢNG DỰ ÁN: membership-hub

## 📊 Điều khiển tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806064029 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 06:40:29 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CƠ BẢN

### 1.1. Mô Hình Hệ Thống Cốt Lõi & Mô Hình Kiến Trúc

### 1.2. Kiến Trúc Dòng Dữ Liệu Doanh Nghiệp & Hệ Sinh Thái Cốt Lõi

## 📁 CỤC ĐỘNG CÔNG NGHỆ & THƯ VIỆN HỆ THỐNG

- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

### ARCHITECTURAL STACK MATRIX
<COMMAND>
You MUST keep below block (e.g. block "```properties...```") 100% in raw Technical English. You are STRICTLY FORBIDDEN from translating any keys, values, or tokens inside this block into 🇻🇳 Vietnamese, as it serves as a strict backend machine-gating matrix. Keep literal `true` or `false` tokens in pure lower-case.

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```
</COMMAND>

## 📁 QUY TẮC BẢO VỆ & THUỘC ĐỘNG TUYÊN CHẤT

- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 📁 BẢNG TỔNG QUAN KIẾN TRÚC Đa Giai Đoạn

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Ngày 1-7 | ./sources/backend | Database schema, RBAC, Auth, Center CRUD, Course CRUD, Enrollment, Attendance | Coder | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| 2 | Ngày 1-7 | ./sources/backend | StudentCard, Promotion, Announcement, Notification, Chatbot, Mobile UI, i18n & SEO | Coder | [NONE] |
| 3 | Ngày 1 | ./sources/backend | Reporting service | Coder | [NONE] |
| 4 | Ngày 1-7 | ./sources/infra | Dockerfile, GCP infra, GKE manifests, CI/CD, Tests, Review, Docs | Docker | [NONE] |

## 📁 CHI TIẾT CHIẾN LƯỢC GIAI PHÂN & ĐÁNH GIÁ NGÀY ĐẾN NGÀY

### 📈 Giai đoạn 1: Cơ sở hạ tầng và chức năng cốt lõi

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn 1:** Thiết lập toàn bộ kiến trúc backend, cơ sở dữ liệu, RBAC, xác thực, CRUD cho trung tâm, khóa học, ghi danh và điểm danh.
- **Đường dẫn Cấu phần / Module:** Tất cả các file nguồn và cấu hình nằm trong thư mục `./sources/backend`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu:**  
```sql
-- Users
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
-- Roles
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);
-- Centers
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
-- Courses
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
-- Enrollments
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
-- Attendance
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId),
    UNIQUE (studentId, courseId, attendanceDate)
);
-- StudentCards
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
-- Promotions
CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);
-- Announcements
CREATE TABLE ANNOUNCEMENTS (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);
-- Notifications
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (userId) REFERENCES USERS(userId)
);
-- SystemSettings
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(255) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(255)
);
```
- **Hợp đồng Định tuyến API và Sự kiện:**  
```java
// AuthService.java
// POST /api/auth/register
// POST /api/auth/login
// POST /api/auth/social
// GET /api/auth/me

// RBACService.java
// GET /api/role/assign
// GET /api/role/assign/{userId}/{roleId}

// CenterService.java
// GET /api/centers
// POST /api/centers
// PUT /api/centers/{id}
...
```
- **Exception Handlers:**  
```java
// InvalidInputException.java
// DuplicateAttendanceException.java
// SystemRecoveryException.java
```

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1:** Thiết lập schema toàn bộ bảng dữ liệu
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/database/migrations/20260806064029_create_all_tables.sql
      - **Low-Level Technical Task Instruction:** Tạo các bảng USERS, ROLES, CENTERS, COURSES, ENROLLMENTS, ATTENDANCE, STUDENTCARDS, PROMOTIONS, ANNOUNCEMENTS, NOTIFICATIONS, SYSTEMSETTINGS với các ràng buộc khóa chính, khóa ngoại, chỉ mục và ràng buộc duy nhất.
      - **Targeted Tag IDs:** [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]

- **DAY 2:** Xây dựng RBAC Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/security/RBACService.java
      - **Low-Level Technical Task Instruction:** Triển khai kiểm tra quyền truy cập dựa trên vai trò, sử dụng các enum và annotations để bảo vệ các endpoint.
      - **Targeted Tag IDs:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 3:** Xây dựng Auth Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/auth/AuthService.java
      - **Low-Level Technical Task Instruction:** Triển khai đăng ký, đăng nhập, social login, phát token JWT, refresh token, và bảo vệ endpoint.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [ARC-006], [EXC-004], [DAT-001], [DAT-002], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 4:** Xây dựng Center CRUD Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/center/CenterService.java
      - **Low-Level Technical Task Instruction:** Triển khai các endpoint GET, POST, PUT, DELETE cho trung tâm, kiểm tra tính duy nhất của taxId.
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 5:** Xây dựng Course CRUD Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/course/CourseService.java
      - **Low-Level Technical Task Instruction:** Triển khai các endpoint GET, POST, PUT, DELETE cho khóa học, kiểm tra xung đột lịch học của giáo viên.
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-005], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 6:** Xây dựng Enrollment Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/enrollment/EnrollmentService.java
      - **Low-Level Technical Task Instruction:** Triển khai đăng ký khóa học, tạo tài khoản sinh viên nếu chưa tồn tại, gửi thông báo.
      - **Targeted Tag IDs:** [REQ-010], [REQ-011], [DAT-005], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 7:** Xây dựng Attendance Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/attendance/AttendanceService.java
      - **Low-Level Technical Task Instruction:** Triển khai ghi nhận điểm danh, kiểm tra tính bất biến, xử lý ngoại lệ khi trùng lặp hoặc mất kết nối.
      - **Targeted Tag IDs:** [REQ-012], [REQ-013], [ARC-007], [EXC-001], [EXC-002], [EXC-003], [DAT-006], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

### 📈 Giai đoạn 2: Chức năng nâng cao và tích hợp

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn 2:** Triển khai các chức năng nâng cao như thẻ hội viên, khuyến mãi, thông báo, chatbot, UI di động, i18n và SEO.
- **Đường dẫn Cấu phần / Module:** Tất cả các file nguồn nằm trong thư mục `./sources/backend` và `./sources/frontend`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu:** (đã bao gồm trong Phase 1)
- **Hợp đồng Định tuyến API và Sự kiện:** (đã bao gồm trong Phase 1)
- **Exception Handlers:** (đã bao gồm trong Phase 1)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1:** Xây dựng StudentCard Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/studentcard/StudentCardService.java
      - **Low-Level Technical Task Instruction:** Triển khai các endpoint GET, POST, PUT cho thẻ hội viên, tính toán ngày còn lại, xử lý gia hạn.
      - **Targeted Tag IDs:** [REQ-014], [REQ-015], [DAT-007], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 2:** Xây dựng Promotion Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/promotion/PromotionService.java
      - **Low-Level Technical Task Instruction:** Triển khai CRUD cho khuyến mãi, kiểm tra tính duy nhất của mã giảm giá.
      - **Targeted Tag IDs:** [REQ-017], [DAT-009], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 3:** Xây dựng Announcement Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/announcement/AnnouncementService.java
      - **Low-Level Technical Task Instruction:** Triển khai CRUD cho thông báo, xử lý thời gian hiệu lực.
      - **Targeted Tag IDs:** [REQ-018], [DAT-009], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 4:** Xây dựng Notification Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/notification/NotificationService.java
      - **Low-Level Technical Task Instruction:** Triển khai gửi push notification, đăng bài lên Zalo, quản lý trạng thái gửi.
      - **Targeted Tag IDs:** [REQ-016], [ARC-008], [DAT-008], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 5:** Xây dựng Chatbot Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/chatbot/ChatbotService.java
      - **Low-Level Technical Task Instruction:** Triển khai tích hợp AI, trả lời câu hỏi, chuyển tiếp khi độ tin cậy thấp.
      - **Targeted Tag IDs:** [REQ-019], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 6:** Xây dựng Mobile UI (Next.js)
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/frontend/nextjs-app/pages/index.js
      - **Low-Level Technical Task Instruction:** Triển khai giao diện đáp ứng, routing, gọi API, bảo vệ route bằng token.
      - **Targeted Tag IDs:** [REQ-020], [REQ-021], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

- **DAY 7:** Xây dựng i18n & SEO
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/frontend/nextjs-app/i18n.js
      - **Low-Level Technical Task Instruction:** Triển khai đa ngôn ngữ, meta tags, hreflang, SEO cho các trang.
      - **Targeted Tag IDs:** [REQ-022], [REQ-023], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

### 📈 Giai đoạn 3: Báo cáo và khôi phục

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn 3:** Triển khai báo cáo điểm danh và khôi phục sau sự cố.
- **Đường dẫn Cấu phần / Module:** Tất cả các file nguồn nằm trong thư mục `./sources/backend`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu:** (đã bao gồm trong Phase 1)
- **Hợp đồng Định tuyến API và Sự kiện:** (đã bao gồm trong Phase 1)
- **Exception Handlers:** (đã bao gồm trong Phase 1)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 1:** Xây dựng Reporting Service
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/report/AttendanceReportService.java
      - **Low-Level Technical Task Instruction:** Triển khai endpoint xuất báo cáo CSV, tính toán trạng thái điểm danh, xử lý ngoại lệ khôi phục.
      - **Targeted Tag IDs:** [REQ-024], [EXC-005], [DAT-006], [DAT-004], [DAT-005], [DAT-011], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [NFR-002]

### 📈 Giai đoạn 4: DevOps và Kiểm thử

- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn 4:** Đóng gói, triển khai, kiểm thử, và tài liệu.
- **Đường dẫn Cấu phần / Module:** Tất cả các file nguồn nằm trong thư mục `./sources/infra`, `./sources/backend`, `./sources/frontend`, `./sources/docs`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu:** (đã bao gồm trong Phase 1)
- **Hợp đồng Định tuyến API và Sự kiện:** (đã bao gồm trong Phase 1)
- **Exception Handlers:** (đã bao gồm trong Phase 1)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1:** Xây dựng Dockerfile cho backend
  - **Sub-Agent Workflow Specialization:**
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/infra/docker/Dockerfile.backend
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile đa stage, cài đặt Quarkus, cấu hình entrypoint, tối ưu kích thước.
      - **Targeted Tag IDs:** [ARC-010]

- **DAY 2:** Thiết lập Terraform cho GCP
  - **Sub-Agent Workflow Specialization:**
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/infra/gcp/terraform/main.tf
      - **Low-Level Technical Task Instruction:** Định nghĩa VPC, IAM, GKE cluster, Cloud SQL, Cloud Storage, Cloud Run, và các tài nguyên cần thiết.
      - **Targeted Tag IDs:** []

- **DAY 3:** Xây dựng manifest GKE
  - **Sub-Agent Workflow Specialization:**
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/infra/gke/deployment.yaml
      - **Low-Level Technical Task Instruction:** Định nghĩa Deployment, Service, Ingress, HPA, ConfigMap, Secret.
      - **Targeted Tag IDs:** []

- **DAY 4:** Thiết lập pipeline CI/CD
  - **Sub-Agent Workflow Specialization:**
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/infra/github-actions/ci.yml
      - **Low-Level Technical Task Instruction:** Định nghĩa workflow, build, test, push image, deploy to GKE.
      - **Targeted Tag IDs:** []

- **DAY 5:** Viết unit test cho Auth Service
  - **Sub-Agent Workflow Specialization:**
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/auth/AuthServiceTest.java;./sources/backend/api/auth/AuthService.java
      - **Low-Level Technical Task Instruction:** Kiểm tra đăng ký, đăng nhập, social login, token generation.
      - **Targeted Tag IDs:** []

- **DAY 6:** Kiểm tra code review
  - **Sub-Agent Workflow Specialization:**
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend/api/auth/AuthService.java
      - **Low-Level Technical Task Instruction:** Đánh giá chất lượng code, tuân thủ chuẩn, tối ưu.
      - **Targeted Tag IDs:** []

- **DAY 7:** Viết tài liệu kiến trúc
  - **Sub-Agent Workflow Specialization:**
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/docs/architecture.md
      - **Low-Level Technical Task Instruction:** Tài liệu chi tiết kiến trúc, flow, API, dữ liệu, bảo mật.
      - **Targeted Tag IDs:** []

## 📁 MÃ BẢO MẬT TOÀN CỤC & CHẾ ĐỘ CHỐT NGHIỆP

- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 QUY TẮC TUYÊN CHẤT ỨNG DỤNG HỢP ĐỒNG & CƠ CẤP SEO ĐỊNH DỊCH

- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 DÒNG ĐOÀN TỰ ĐỘNG GIT CHỈNH ĐỊNH NGÀY

- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MÁC CHẤM CẤP ĐÁNH GIÁ

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 24, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`