# BỐ CỤC DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260807024254 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/07 02:42:54 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1 Core System Modality & Architecture Modality
- Xác định mô hình kiến trúc đa dịch vụ với các thành phần độc lập: người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, chatbot AI, giao diện di động.
- Áp dụng mô hình CQRS cho các hoạt động đọc/ghi, đảm bảo tính nhất quán cho điểm danh và thẻ hội viên.
- Sử dụng kiến trúc hướng sự kiện với Kafka để đồng bộ hóa dữ liệu giữa các dịch vụ.
- Triển khai bảo mật theo từng trung tâm với RBAC và phân quyền dựa trên vai trò (ARC-001 đến ARC-005).
- Tích hợp OAuth2/OIDC với Firebase, Google, Facebook để xác thực (ARC-006).
- Thiết kế API REST với JWT (15 phút) và refresh token (7 ngày) (ARC-006).
- Triển khai container hóa Docker với Quarkus và orchestration Kubernetes trên GKE (ARC-010).
- Tích hợp push notification qua FCM/APNs và tích hợp Zalo API (ARC-008).
- Triển khai hệ thống giám sát và ghi nhật ký tập trung (NFR-006).

### 1.2 Enterprise Data Flow Topologies & Core Ecosystems
- Luồng xác thực: Người dùng đăng nhập qua email/mật khẩu hoặc OAuth2 từ Firebase/Google/Facebook → xác thực → cấp JWT.
- Luồng điểm danh QR: Ứng dụng di động quét QR → gửi studentId + timestamp → dịch vụ xác thực → ghi điểm danh (ARC-007, EXC-001, EXC-002).
- Luồng thông báo: Hành động ghi danh/giáo viên/thông báo → tạo bản ghi Notification → đẩy push (FCM/APNs) + gửi tin nhắn Zalo (ARC-008, EXC-003).
- Luồng tích hợp frontend: Next.js tiêu thụ REST API, caching ngoại tuyến qua IndexedDB (ARC-009).
- Luồng xử lý sự kiện: Kafka chủ đề `attendance`, `notifications`, `enrollment` để đồng bộ hóa dữ liệu giữa các dịch vụ.
- Tích hợp cơ sở dữ liệu: PostgreSQL cho dữ liệu quan trọng, Redis cho session caching (ARC-010).
- Triển khai CI/CD qua GitHub Actions với kiểm tra tự động và triển khai canary (ARC-010).
- Vòng lặp đa ngôn ngữ: middleware phát hiện locale, chuyển hướng URL, chèn hreflang cho SEO (REQ-022, REQ-023).

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

### 2.1 Backend Infrastructure Core Stack
- Java/Quarkus **3.2.0**
- PostgreSQL **15.4**
- Docker **24.0.5**
- Kubernetes (GKE) **1.28**
- Firebase Authentication SDK **9.22.0**
- Google Cloud Messaging (FCM) / Apple APNs **latest**
- Zalo API SDK **2.0.1**
- Redis **7.2**
- Maven **3.9.6**
- Liquibase **4.25.5**
- JUnit5/Mockito **5.10**
- OpenTelemetry **1.30.0**

### 2.2 Frontend & Cross-Platform UI Mobile Stack
- Next.js **14.x**
- React Native **0.73.0**
- Node.js **20.12**
- TypeScript **5.3**
- Capacitor **5.5**
- Tailwind CSS **3.4**
- Axios **1.6**
- React Query **5.0**
- Swift (iOS) / Kotlin (Android) native modules cho FCM/APNs

### 2.3 ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Quy tắc biên giới không gian làm việc:** Tất cả các đường dẫn phải bắt đầu với `./sources/`.
- **Quy tắc tiền tố thư mục động:** tuân thủ Protocol 1.
- **Quy tắc gói Java:** `org.nlh4j.saas.membershiphub` (membership-hub được chuẩn hóa thành dạng alphanumeric lowercase).
- **Quy tắc cú pháp mục tiêu kiểm thử:** `<source_component>;<test_suite_file>`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 - 2 | ./sources/backend/users/ | Xây dựng lõi người dùng, vai trò và xác thực cơ bản (bao gồm đăng ký, OAuth2, JWT và validation đầu vào) | Coder | [ARC-001], [ARC-006], [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006], [NFR-008] |
| Phase 2 | Day 1 - 4 | ./sources/backend/centers/ | Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin | Coder | [ARC-002], [REQ-004], [REQ-005], [REQ-006], [DAT-003], [NFR-001], [NFR-003], [NFR-004] |
| Phase 3 | Day 1 - 3 | ./sources/backend/courses/ | Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên | Coder | [ARC-003], [REQ-007], [REQ-008], [REQ-009], [DAT-004], [NFR-001], [NFR-003] |
| Phase 4 | Day 1 - 5 | ./sources/backend/enrollment/ | Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống | Coder | [ARC-004], [ARC-005], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [EXC-001], [EXC-002], [EXC-003], [EXC-005], [NFR-001], [NFR-003], [NFR-004], [NFR-006] |
| Phase 5 | Day 1 - 2 | ./sources/frontend/mobile/ | Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps | Coder | [ARC-007], [ARC-008], [ARC-009], [ARC-010], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-002], [NFR-005], [NFR-007], [NFR-008], [NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Phase 1: Xây dựng lõi người dùng, vai trò và xác thực cơ bản (bao gồm đăng ký, OAuth2, JWT và validation đầu vào)

- **Phase Core Objective & Purpose:** Xây dựng lõi người dùng, vai trò và xác thực cơ bản (bao gồm đăng ký, OAuth2, JWT và validation đầu vào).
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend/users/UserService.java` [ARC-001], [REQ-001], [DAT-001]
    *   `./sources/backend/users/AuthController.java` [ARC-006], [REQ-002], [REQ-003], [DAT-001]
- **Database Schema DDL SQL Specification [DAT-001]:**
```sql
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL REFERENCES ROLES(roleId),
    provider ENUM('local','firebase','google','facebook') NOT NULL DEFAULT 'local',
    createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
    updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
```json
// POST /api/v1/auth/register
{
  "email": "user@example.com",
  "password": "StrongPass123!",
  "fullName": "Nguyen Van A",
  "provider": "local"
}
```
```json
// POST /api/v1/auth/social
{
  "provider": "google",
  "code": "OAuth2_code_from_google",
  "redirectUri": "https://app.example.com/auth/callback"
}
```
```json
// PUT /api/v1/users/{userId}/role
{
  "roleId": 2
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
    * Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc): Trả về HTTP 400 với danh sách các trường không hợp lệ và hướng dẫn chỉnh sửa.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1:** Mục tiêu ngắn hạn: Triển khai dịch vụ quản lý người dùng cơ bản.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-001], [REQ-001], [DAT-001]
    * **Target Component file path (`target_component`):** ./sources/backend/users/UserService.java [ARC-001], [REQ-001], [DAT-001]
    * **Low-Level Technical Task Instruction:** Triển khai lớp UserService để xử lý đăng ký người dùng mới, tạo bản ghi trong bảng Users với vai trò mặc định là Student, tuân thủ REQ-001 và ARC-001.

- **DAY 2:** Mục tiêu ngắn hạn: Xây dựng controller xác thực và tích hợp OAuth2.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-006], [REQ-002], [REQ-003], [DAT-001]
    * **Target Component file path (`target_component`):** ./sources/backend/users/AuthController.java [ARC-006], [REQ-002], [REQ-003], [DAT-001]
    * **Low-Level Technical Task Instruction:** Xây dựng AuthController để xử lý xác thực OAuth2 từ Firebase/Google/Facebook, trao đổi mã lấy thông tin người dùng, cập nhật vai trò và cấp JWT token (ARC-006), đồng thời hỗ trợ phân quyền người dùng (REQ-003).

### 📈 Phase 2: Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin

- **Phase Core Objective & Purpose:** Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin.
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend/centers/CenterController.java` [ARC-002], [REQ-004], [DAT-003]
    *   `./sources/backend/centers/CenterService.java` [REQ-005], [DAT-003]
    *   `./sources/backend/centers/CenterAdminService.java` [REQ-006], [ARC-002], [DAT-003]
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [ARC-002]:**
```json
// GET /api/v1/centers
// trả về danh sách trung tâm
```
```json
// POST /api/v1/centers
{
  "name": "Hà Nội Center",
  "address": "123 Đường Láng, Đống Đa, Hà Nội",
  "taxId": "0123456789",
  "contactPhone": "+84123456789",
  "contactEmail": "contact@hnc.com"
}
```
```json
// PUT /api/v1/centers/{centerId}/admin/{userId}
```
- **Phase Localized Exception Handlers:** Không có ngoại lệ chuyên biệt.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1:** Mục tiêu ngắn hạn: Xây dựng controller danh sách trung tâm.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-002], [REQ-004], [DAT-003]
    * **Target Component file path (`target_component`):** ./sources/backend/centers/CenterController.java [ARC-002], [REQ-004], [DAT-003]
    * **Low-Level Technical Task Instruction:** Triển khai CenterController để hiển thị danh sách trung tâm (REQ-004) và phục vụ các thao tác CRUD cho System Admin (ARC-002).

- **DAY 2:** Mục tiêu ngắn hạn: Triển khai logic tạo/cập nhật trung tâm.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-005], [DAT-003]
    * **Target Component file path (`target_component`):** ./sources/backend/centers/CenterService.java [REQ-005], [DAT-003]
    * **Low-Level Technical Task Instruction:** Triển khai logic tạo/cập nhật trung tâm trong CenterService, thực hiện kiểm tra trùng lặp taxId và ghi dữ liệu vào bảng CENTERS (REQ-005).

- **DAY 3:** Mục tiêu ngắn hạn: Triển khai gán/rút quyền Center Admin.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-006], [ARC-002], [DAT-003]
    * **Target Component file path (`target_component`):** ./sources/backend/centers/CenterAdminService.java [REQ-006], [ARC-002], [DAT-003]
    * **Low-Level Technical Task Instruction:** Triển khai gán/rút quyền Center Admin cho người dùng, cập nhật roleId trong bảng USERS và ghi lại mối quan hệ (REQ-006, ARC-002).

- **DAY 4:** Mục tiêu ngắn hạn: Triển khai manifest GKE cho dịch vụ trung tâm.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [NFR-001], [NFR-003], [NFR-004]
    * **Target Component file path (`target_component`):** ./sources/infra/k8s/center-deployment.yaml [NFR-001], [NFR-003], [NFR-004]
    * **Low-Level Technical Task Instruction:** Tạo manifest triển khai dịch vụ quản lý trung tâm trên GKE với autoscaling dựa trên CPU và request latency (NFR-001, NFR-003, NFR-004).

### 📈 Phase 3: Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên

- **Phase Core Objective & Purpose:** Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên.
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend/courses/CourseController.java` [ARC-003], [REQ-007], [DAT-004]
    *   `./sources/backend/courses/CourseService.java` [REQ-008], [DAT-004]
    *   `./sources/backend/courses/CourseTeacherService.java` [REQ-009], [ARC-003], [DAT-004]
- **Database Schema DDL SQL Specification [DAT-004]:**
```sql
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL REFERENCES USERS(userId),
    maxStudents INT NOT NULL DEFAULT 30
);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [ARC-003]:**
```json
// GET /api/v1/courses
// trả về danh sách khóa học
```
```json
// POST /api/v1/courses
{
  "title": "Lập trình Java nâng cao",
  "description": "Khóa học về Quarkus và Kubernetes",
  "startDate": "2026-09-01",
  "endDate": "2026-12-31",
  "teacherId": "a1b2c3d4-...",
  "maxStudents": 20
}
```
```json
// PUT /api/v1/courses/{courseId}/teacher/{teacherId}
```
- **Phase Localized Exception Handlers:** Không có ngoại lệ chuyên biệt.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 1:** Mục tiêu ngắn hạn: Xây dựng controller danh sách khóa học.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-003], [REQ-007], [DAT-004]
    * **Target Component file path (`target_component`):** ./sources/backend/courses/CourseController.java [ARC-003], [REQ-007], [DAT-004]
    * **Low-Level Technical Task Instruction:** Triển khai CourseController để hiển thị danh sách khóa học (REQ-007) và hỗ trợ CRUD cho System/Center Admin (ARC-003).

- **DAY 2:** Mục tiêu ngắn hạn: Triển khai logic tạo/cập nhật khóa học.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-008], [DAT-004]
    * **Target Component file path (`target_component`):** ./sources/backend/courses/CourseService.java [REQ-008], [DAT-004]
    * **Low-Level Technical Task Instruction:** Triển khai logic tạo/cập nhật khóa học, kiểm tra xung đột lịch với giáo viên (REQ-008) và ghi dữ liệu vào bảng COURSES (DAT-004).

- **DAY 3:** Mục tiêu ngắn hạn: Triển khai gán/rút giáo viên vào khóa học.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-009], [ARC-003], [DAT-004]
    * **Target Component file path (`target_component`):** ./sources/backend/courses/CourseTeacherService.java [REQ-009], [ARC-003], [DAT-004]
    * **Low-Level Technical Task Instruction:** Triển khai gán/rút giáo viên vào khóa học, tạo bản ghi mapping và gửi thông báo push (REQ-009, ARC-003).

### 📈 Phase 4: Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống

- **Phase Core Objective & Purpose:** Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống.
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend/enrollment/EnrollmentController.java` [ARC-004], [REQ-010], [DAT-005]
    *   `./sources/backend/enrollment/EnrollmentService.java` [REQ-011], [DAT-005], [ARC-005]
    *   `./sources/backend/attendance/AttendanceService.java` [ARC-007], [REQ-012], [DAT-006], [EXC-001], [EXC-002]
    *   `./sources/backend/notifications/NotificationService.java` [ARC-008], [REQ-016], [DAT-008], [EXC-003]
    *   `./sources/backend/membership/MembershipController.java` [REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]
- **Database Schema DDL SQL Specification [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:**
```sql
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);

CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID REFERENCES USERS(userId),
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
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
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [ARC-004], [ARC-005], [ARC-007], [ARC-008]:**
```json
// POST /api/v1/enrollments
{
  "studentId": "a1b2c3d4-...",
  "courseId": "e5f6g7h8-..."
}
```
```json
// POST /api/v1/attendance/scan
{
  "studentId": "a1b2c3d4-...",
  "courseId": "e5f6g7h8-...",
  "qrCodeData": "course:e5f6g7h8-...|date:2026-08-07"
}
```
```json
// GET /api/v1/membership/{studentId}/card
// trả về thẻ hội viên với daysRemaining
```
```json
// POST /api/v1/notifications
{
  "userId": "a1b2c3d4-...",
  "groupZalo": "hoc_vien_hn",
  "message": "Bạn đã được ghi danh vào khóa học mới."
}
```
```json
// POST /api/v1/promotions
{
  "code": "SUMMER20",
  "discountPercent": 20,
  "startDate": "2026-06-01",
  "endDate": "2026-08-31",
  "description": "Giảm giá 20% cho tất cả khóa học."
}
```
```json
// POST /api/v1/announcements
{
  "title": "Thông báo nghỉ lễ",
  "content": "Trung tâm nghỉ lễ từ 01/09 đến 05/09.",
  "startDate": "2026-08-31",
  "endDate": "2026-09-05"
}
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003], [EXC-005]:**
    * **Mất mạng khi quét QR (EXC-001):** Nếu sinh viên quét QR nhưng không có kết nối mạng, khi kết nối được khôi phục, ứng dụng sẽ tự động gửi lại yêu cầu điểm danh; dịch vụ sẽ đảm bảo chỉ ghi một bản ghi điểm danh duy nhất.
    * **Điểm danh trùng lặp (EXC-002):** Nếu cùng một sinh viên quét cùng một QR nhiều lần trong ngày, hệ thống sẽ phát hiện duplicate, trả về success với cờ ‘alreadyRecorded’ và không tạo thêm hàng.
    * **Giao hàng thông báo thất bại (EXC-003):** Nếu push notification không thể gửi (ví dụ: token thiết bị không hợp lệ), hệ thống ghi log lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu là thất bại.
    * **Khôi phục hệ thống sau sự cố (EXC-005):** Nếu dịch vụ không khả dụng, khi khôi phục, các lần quét điểm danh chờ xử lý được xử lý theo thứ tự FIFO, và người dùng nhận được thông báo về các sự kiện đã khôi phục.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1:** Mục tiêu ngắn hạn: Xây dựng controller ghi danh khóa học.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-004], [REQ-010], [DAT-005]
    * **Target Component file path (`target_component`):** ./sources/backend/enrollment/EnrollmentController.java [ARC-004], [REQ-010], [DAT-005]
    * **Low-Level Technical Task Instruction:** Triển khai EnrollmentController để duyệt khóa học và xử lý đăng ký (REQ-010, ARC-004), tự động tạo tài khoản Student nếu thiếu.

- **DAY 2:** Mục tiêu ngắn hạn: Triển khai logic đăng ký khóa học.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-011], [DAT-005], [ARC-005]
    * **Target Component file path (`target_component`):** ./sources/backend/enrollment/EnrollmentService.java [REQ-011], [DAT-005], [ARC-005]
    * **Low-Level Technical Task Instruction:** Triển khai logic đăng ký khóa học, ghi bản ghi ENROLLMENTS, cập nhật vai trò người dùng (REQ-011) và gửi thông báo đến mobile app và Zalo group (ARC-005).

- **DAY 3:** Mục tiêu ngắn hạn: Triển khai dịch vụ điểm danh QR.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-007], [REQ-012], [DAT-006], [EXC-001], [EXC-002]
    * **Target Component file path (`target_component`):** ./sources/backend/attendance/AttendanceService.java [ARC-007], [REQ-012], [DAT-006], [EXC-001], [EXC-002]
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ điểm danh QR, ghi nhận timestamp, đảm bảo bất biến cho cùng studentId/courseId/ngày (REQ-012, ARC-007), xử lý ngoại lệ mất mạng (EXC-001) và phát hiện duplicate (EXC-002).

- **DAY 4:** Mục tiêu ngắn hạn: Triển khai dịch vụ thông báo.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-008], [REQ-016], [DAT-008], [EXC-003]
    * **Target Component file path (`target_component`):** ./sources/backend/notifications/NotificationService.java [ARC-008], [REQ-016], [DAT-008], [EXC-003]
    * **Low-Level Technical Task Instruction:** Triển khai NotificationService để tạo bản ghi NOTIFICATIONS, đẩy push qua FCM/APNs và gửi tin nhắn Zalo (REQ-016, ARC-008), xử lý ngoại lệ giao hàng thất bại (EXC-003).

- **DAY 5:** Mục tiêu ngắn hạn: Triển khai controller thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-014], [REQ-15], [DAT-007], [DAT-009], [DAT-011], [EXC-005]
    * **Target Component file path (`target_component`):** ./sources/backend/membership/MembershipController.java [REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]
    * **Low-Level Technical Task Instruction:** Triển khai MembershipController để hiển thị thẻ hội viên (REQ-014) và xử lý gia hạn thẻ (REQ-015), cập nhật STUDENTCARDS, PROMOTIONS, ANNOUNCEMENTS, SYSTEMSETTINGS (DAT-007, DAT-009, DAT-011), xử lý khôi phục hệ thống sau sự cố (EXC-005).

### 📈 Phase 5: Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps

- **Phase Core Objective & Purpose:** Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps.
- **Target Physical Directory Matrix Map:**
    *   `./sources/frontend/mobile/App.js` [ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]
    *   `./sources/docs/reporting-and-seo.md` [ARC-010], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-007], [NFR-008], [NFR-009]
- **Database Schema DDL SQL Specification:** Không có bảng dữ liệu mới trong giai đoạn này.
- **API and Event Routing Contracts [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-009], [ARC-010]:**
```json
// GET /api/v1/mobile/user/{userId}/profile
// trả về thông tin người dùng cho ứng dụng di động
```
```json
// POST /api/v1/mobile/tokens
{
  "userId": "a1b2c3d4-...",
  "token": "FCM_token_here"
}
```
```json
// POST /api/v1/chatbot/query
{
  "userId": "a1b2c3d4-...",
  "question": "Khóa học Java có vào thứ 3 không?"
}
```
```json
// GET /api/v1/reports/attendance?centerId=...&date=...
```
- **Phase Localized Exception Handlers:** Không có ngoại lệ chuyên biệt.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 1:** Mục tiêu ngắn hạn: Xây dựng lõi ứng dụng di động.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]
    * **Target Component file path (`target_component`):** ./sources/frontend/mobile/App.js [ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]
    * **Low-Level Technical Task Instruction:** Triển khai lõi ứng dụng di động hybrid với điều hướng vai trò, tích hợp Firebase Auth và xử lý push notification (REQ-020, ARC-009), đảm bảo kích thước image <500MB (NFR-005) và mục tiêu uptime 99.9% (NFR-002).

- **DAY 2:** Mục tiêu ngắn hạn: Tạo tài liệu báo cáo và SEO.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [ARC-010], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** ./sources/docs/reporting-and-seo.md [ARC-010], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-007], [NFR-008], [NFR-009]
    * **Low-Level Technical Task Instruction:** Tạo tài liệu báo cáo và SEO, bao gồm hướng dẫn tạo báo cáo điểm danh CSV (REQ-024), chèn meta tags đa ngôn ngữ và hreflang (REQ-022, REQ-023), thực hiện tuân thủ GDPR/CCPA (NFR-008) và sao lưu PostgreSQL (NFR-009), đồng thời ghi lại quy trình triển khai Docker và GKE (ARC-010).

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-001] [NFR-003] [NFR-004] [NFR-005] [NFR-006] [NFR-007] [NFR-008] [NFR-009]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng PreparedStatement/ParameterizedQuery, whitelist cho các cột sắp xếp, kiểm tra kiểu dữ liệu đầu vào.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động thoát HTML trong JSX, thiết lập header CSP (`default-src 'self'; script-src 'self' 'unsafe-inline'` bị cấm, sử dụng nonce cho scripts cần thiết).
- **Multi-Tenant CORS Security Rails:** whitelist các origin dựa trên cấu hình trung tâm, từ chối wildcard `null` hoặc `*`, xác thực origin qua JWT tenantId.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Sử dụng `@JsonSerialize` với `SensitiveDataMasker`, xóa trường hợp đặc biệt trước khi ghi log, giới hạn độ dài log theo yêu cầu GDPR.
- **Docker Image Size Enforcement:** Giới hạn kích thước image <500MB, sử dụng multi-stage build, loại bỏ các gói không cần thiết.
- **Multi-Language Support:** Externalize chuỗi UI qua `i18n` (JSON), middleware phát hiện locale, tự động chèn hreflang, fallback sang Accept-Language header.
- **GDPR/CCPA Compliance:** Thêm API xóa dữ liệu `/api/v1/users/{id}/delete`, cung cấp export JSON `/api/v1/users/{id}/export`, quản lý consent cho marketing.
- **Backup & Disaster Recovery:** Sao lưu PostgreSQL đầy đủ hàng ngày, point-in-time recovery 24 giờ, cluster backup GKE sang region khác, kiểm tra khôi phục hàng tuần.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng `@capacitor/preferences` cho storage an toàn, chặn back-button gốc, fetch với timeout và retry, xác thực URL tuyệt đối, ngăn chặn XSS trong WebView.
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware phát hiện locale (`Accept-Language`, cookie), chuyển hướng URL có dấu `/vi/` `/en/`, chèn thẻ `<html lang='vi'>`, tạo thẻ `<link rel="canonical" href="...">`, tự động tạo sitemap XML với hreflang, chặn bot quét theo robots.txt.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Tạo branch `features/development-phase-1-day-1`, `features/development-phase-1-day-2`, ... cho từng ngày, mỗi branch là không gian làm việc riêng biệt.
- **Validation Guard Pipeline Gates:** Thực hiện `mvn clean verify` hoặc `npm run test` trước khi merge, đảm bảo độ phủ mã >=85%, kiểm tra chất lượng code qua SonarQube, tự động tạo PR với checklist tuân thủ.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`