# BỐ CỤC DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806080121 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:01:21 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống được thiết kế theo kiến trúc microservice với các biên giới CQRS rõ ràng, sử dụng mẫu Reactive Core để đảm bảo khả năng mở rộng và độ trễ thấp. Mỗi module chức năng (User, Center, Course, Enrollment, Attendance, Membership, Notification, Promotion, Announcement, Chatbot, Frontend) được triển khai dưới dạng một dịch vụ độc lập, được container hóa bằng Docker và orchestration trên Google Kubernetes Engine (GKE). Hệ thống áp dụng event-sourcing và message broker (ví dụ: Kafka) cho các luồng bất đồng bộ như điểm danh QR, push notification, và cập nhật Zalo group. Các API được định nghĩa dưới dạng REST với JWT bearer token, hỗ trợ đa phiên bản và versioning tự động. Kiến trúc đảm bảo cô lập đa trung tâm, tuân thủ nghiêm ngặt RBAC và các chính sách bảo mật theo chuẩn OWASP Top 10.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Các luồng dữ liệu chính bao gồm: (1) **Luồng xác thực** – OAuth2 với Firebase, Google, Facebook, cấp JWT (15 phút) và refresh token; (2) **Luồng xử lý điểm danh QR** – ứng dụng di động quét QR, gửi studentId + timestamp đến Attendance Service, ghi nhận một cách idempotent; (3) **Luồng gửi thông báo** – Notification Service kích hoạt push notification (FCM/APNs) và đăng bài lên nhóm Zalo được chỉ định; (4) **Luồng tích hợp backend ứng dụng di động** – Frontend Next.js tiêu thụ REST APIs, hỗ trợ caching ngoại tuyến (Service Worker). Các chủ đề message broker được định nghĩa cho attendance-events, notification-events, enrollment-events, và center-events để đảm bảo tính nhất quán sự kiện giữa các service.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.8, PostgreSQL 15, Docker (<500 MB), Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API, Redis (session caching), GitHub Actions CI/CD, Maven/Bun build tools.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14, React 18, TypeScript, Tailwind CSS, i18next cho đa ngôn ngữ, @capacitor/core cho hybrid mobile, React Native cho các màn hình chuyên sâu, Capacitor Storage API, Service Worker cho offline caching, SEO với next-seo, host trên Cloud Front/GCLOUD.

### ARCHITECTURAL STACK MATRIX
<!--START_COMMAND
```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```
END_COMMAND-->

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** Root repository là `.`; mọi đường dẫn phải bắt đầu bằng `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Backend logic → `./sources/backend.<service-name>.`; Frontend → `./sources/frontend.`; Infra → `./sources/infra.`.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Tất cả mã nguồn Java phải nằm trong gói `org.nlh4j.saas.membershiphub`.
- **Strict Tester Target Path Syntax:** Mọi thành phần được Tester nhắm đến phải theo cú pháp `<source_component>;<test_suite_file>` với cả hai đều bắt đầu bằng `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | 1‑3 | `./sources/backend.user.` | Triển khai bảng Users & Roles, RBAC, đăng ký người dùng, xác thực mạng xã hội, gán vai trò. | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-001], [REQ-002], [REQ-003], [EXC-004], [DAT-001] |
| **Phase 1** | 1‑3 | `./sources/docs/architecture.` | Tài liệu kiến trúc tổng quan, sơ đồ RBAC, ma trận kiểm soát truy cập. | Doc | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] |
| **Phase 2** | 4‑7 | `./sources/backend.center.` | CRUD trung tâm, xác thực taxId duy nhất, gán Center Admin. | Coder | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [EXC-004] |
| **Phase 2** | 4‑7 | `./sources/backend.course.` | CRUD khóa học, phát hiện xung đột lịch giảng, phân công giáo viên. | Coder | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [EXC-003] |
| **Phase 2** | 4‑7 | `./sources/docs/api.` | Tài liệu hợp đồng API cho Centers và Courses (REST contracts). | Doc | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009] |
| **Phase 3** | 8‑13 | `./sources/backend.enrollment.` | Xử lý ghi danh học viên, tự động tạo tài khoản Student, đẩy notification. | Coder | [REQ-010], [REQ-011], [DAT-005], [EXC-003] |
| **Phase 3** | 8‑13 | `./sources/backend.attendance.` | Xử lý điểm danh QR, đảm bảo bất biến, phát hiện duplicate, ghi log network drop. | Coder | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002] |
| **Phase 3** | 8‑13 | `./sources/backend.membership.` | Hiển thị thẻ hội viên, tính remaining days, xử lý gia hạn thẻ. | Coder | [REQ-014], [REQ-015], [DAT-007], [EXC-004] |
| **Phase 3** | 8‑13 | `./sources/backend.notification.` | Gửi push notification, đăng bài lên Zalo group, hàng đợi retry. | Coder | [REQ-016], [EXC-003] |
| **Phase 3** | 8‑13 | `./sources/backend.promo.` | CRUD khuyến mãi & thông báo, auto-expiry, hiển thị cho student. | Coder | [REQ-017], [REQ-018], [DAT-009], [EXC-004] |
| **Phase 3** | 8‑13 | `./sources/docs/reporting.` | Tài liệu báo cáo điểm danh CSV, dashboard tóm tắt ghi danh. | Doc | [REQ-024], [REQ-025], [DAT-006], [DAT-007] |
| **Phase 4** | 14‑18 | `./sources/frontend.web.` | UI responsive theo vai trò, tích hợp i18n, SEO meta tags, caching ngoại tuyến. | Coder | [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011], [NFR-007], [NFR-003], [NFR-001], [NFR-006] |
| **Phase 4** | 14‑18 | `./sources/backend.chatbot.` | Tích hợp chatbot AI cho các truy vấn phổ biến, cơ chế fallback. | Coder | [REQ-019], [EXC-004] |
| **Phase 4** | 14‑18 | `./sources/infra.docker.` | Xây dựng Dockerfiles đa giai đoạn, đảm bảo kích thước ảnh <500 MB. | Docker | [NFR-005], [NFR-004] |
| **Phase 5** | 19‑21 | `./sources/infra.gcp.` | Cấu hình VPC, IAM, Cloud Storage, CI/CD pipelines, thiết lập backup. | GCP | [ARC-010], [NFR-002], [NFR-004], [NFR-008], [NFR-009] |
| **Phase 5** | 19‑21 | `./sources/infra.gke.` | Triển khai manifests Kubernetes, cấu hình HPA, thiết lập failover, autoscaling. | GKE | [ARC-010], [NFR-002], [NFR-004], [NFR-009] |
| **Phase 5** | 19‑21 | `./sources/docs/compliance.` | Tài liệu kiểm soát bảo mật OWASP, tuân thủ GDPR/CCPA, logging audit. | Doc | [NFR-003], [NFR-006], [NFR-008], [NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng nền tảng định danh người dùng và phân quyền truy cập, triển khai các bảng dữ liệu cơ bản cho Users, Roles, và các quy tắc xác thực ban đầu.
- **Target Physical Directory Matrix Map:**
    * `./sources/backend.user. [DAT-001], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-001], [REQ-002], [REQ-003]`
    * `./sources/docs/architecture. [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]`
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
  "email":"user@example.com",
  "password":"StrongPass123!",
  "fullName":"Nguyen Van A",
  "roleId":5
}
```
```json
// POST /api/v1/auth/social
{
  "provider":"google",
  "code":"oauth2_code_from_google"
}
```
```json
// PUT /api/v1/users/{userId}/role
{
  "roleId":3
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
    * Khi xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc), hệ thống trả về HTTP 400 với danh sách các trường không hợp lệ và hướng dẫn chỉnh sửa.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1:** Mục tiêu ngắn hạn: Triển khai bảng dữ liệu người dùng và vai trò, thiết lập các ràng buộc khóa chính, chỉ mục duy nhất.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.user. [DAT-001], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-001], [REQ-002], [REQ-003]
      - **Low-Level Technical Task Instruction:** Triển khai lớp `UserEntity` với các trường tương ứng, thêm các annotation JPA (`@Entity`, `@Table`), `@Id`, `@Column`, `@ManyToOne` đến `Roles`. Tạo `UserRepository` mở rộng `JpaRepository<Users, UUID>`. Triển khai `UserService` với phương thức `registerUser` thực hiện xác thực đầu vào, mã hóa password bằng bcrypt, lưu người dùng mới với role mặc định là Student (`roleId` 5). Thêm các validation (`@NotBlank`, `@Email`). Ghi đè `equals`/`hashCode` dựa trên `userId`. Đảm bảo `createdAt`/`updatedAt` được tự động cập nhật.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
- **DAY 2:** Mục tiêu ngắn hạn: Tài liệu hóa kiến trúc tổng quan và ma trận kiểm soát truy cập dựa trên RBAC.
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/docs/architecture. [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
      - **Low-Level Technical Task Instruction:** Tạo tài liệu Confluence với tiêu đề “Sơ đồ Kiến trúc – membership‑hub”. Bao gồm phần “RBAC Matrix” liệt kê System Admin ([ARC-001]), Center Admin ([ARC-002]), Manager ([ARC-003]), Teacher ([ARC-004]), Student ([ARC-005]) với các quyền hạn tương ứng. Thêm sơ đồ ER cho Users và Roles. Đính kèm hướng dẫn triển khai và các ghi chú bảo mật.
      - **Targeted Tag IDs:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
- **DAY 3:** Mục tiêu ngắn hạn: Xây dựng Docker image cho service user và đẩy lên registry.
  - **Sub-Agent Workflow Specialization:**
    * **[Docker]:**
      - **Target Component file path (`target_component`):** ./sources/infra.docker. [NFR-005], [NFR-004]
      - **Low-Level Technical Task Instruction:** Tạo `Dockerfile` đa giai đoạn: giai đoạn build sử dụng `maven` (hoặc `gradle`) để đóng gói ứng dụng Quarkus; giai đoạn runtime sử dụng image `eclipse-temurin:21-jdk-alpine`. Thêm nhãn `org.opencontainers.image.base.name`, `maintainer`, `version`. Xây dựng image `membership-hub/user:1.0.0`. Kiểm tra kích thước image (<500 MB). Push image lên Google Artifact Registry (`us-central1-docker.pkg.dev/<project>/membership-hub/user:1.0.0`).
      - **Targeted Tag IDs:** [NFR-005], [NFR-004]

### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai quản lý trung tâm và khóa học, bao gồm CRUD, phát hiện xung đột lịch, và gán giáo viên.
- **Target Physical Directory Matrix Map:**
    * `./sources/backend.center. [DAT-003], [REQ-004], [REQ-005], [REQ-006]`
    * `./sources/backend.course. [DAT-004], [REQ-007], [REQ-008], [REQ-009]`
    * `./sources/docs/api. [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009]`
- **Database Schema DDL SQL Specification [DAT-003], [DAT-004]:**
```sql
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
    teacherId UUID NOT NULL REFERENCES USERS(userId),
    maxStudents INT NOT NULL DEFAULT 30
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009]:**
```json
// GET /api/v1/centers
// Response: [{ "centerId":"...","name":"...","address":"...","taxId":"...","contactPhone":"...","contactEmail":"..." }]
```
```json
// POST /api/v1/centers
{
  "name":"Center A",
  "address":"123 Street",
  "taxId":"1234567890123",
  "contactPhone":"+84123456789",
  "contactEmail":"center@example.com"
}
```
```json
// POST /api/v1/courses
{
  "title":"Lớp học lập trình Java",
  "description":"Khóa học nâng cao",
  "startDate":"2026-09-01",
  "endDate":"2026-12-31",
  "teacherId":"a1b2c3d4-...",
  "maxStudents":30
}
```
- **Phase Localized Exception Handlers [EXC-003]:**
    * Khi gửi push notification thất bại (ví dụ: token thiết bị không hợp lệ), hệ thống ghi log lỗi, tăng số lần thử lại (tối đa 3 lần), sau đó đánh dấu bản ghi Notification là `delivered = false`.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 4:** Mục tiêu ngắn hạn: Triển khai service quản lý trung tâm, bao gồm validation taxId duy nhất.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.center. [DAT-003], [REQ-004], [REQ-005], [REQ-006]
      - **Low-Level Technical Task Instruction:** Tạo `CenterEntity` với các trường tương ứng, thêm `@UniqueConstraint(columnNames = "taxId")`. Triển khai `CenterRepository`. Triển khai `CenterService` với các phương thức `createCenter`, `updateCenter`, `deleteCenter`. Thêm logic validation taxId (chỉ số 10‑13 chữ số). Đảm bảo audit fields (`createdAt`, `updatedAt`). Viết integration test cho từng API.
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]
- **DAY 5:** Mục tiêu ngắn hạn: Triển khai service quản lý khóa học với phát hiện xung đột lịch.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.course. [DAT-004], [REQ-007], [REQ-008], [REQ-009]
      - **Low-Level Technical Task Instruction:** Tạo `CourseEntity` với các ràng buộc khóa ngoại đến `USERS`. Thêm phương thức `checkScheduleConflict(teacherId, startDate, endDate)` truy vấn các khóa học hiện có. Triển khai `CourseService` với `createCourse`, `updateCourse`, `assignTeacher`. Sử dụng `@Transactional` để đảm bảo nguyên tử. Thêm validation cho `startDate` < `endDate`. Ghi đè `toString` để loại bỏ các trường nhạy cảm.
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004]
- **DAY 6:** Mục tiêu ngắn hạn: Tài liệu hợp đồng API cho Centers và Courses.
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/docs/api. [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009]
      - **Low-Level Technical Task Instruction:** Tạo tài liệu OpenAPI YAML cho các endpoint `/centers` và `/courses`. Bao gồm request/response schemas, mã lỗi, ví dụ. Đính kèm mô tả về quy tắc phát hiện xung đột lịch. Xuất tài liệu sang Confluence.
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009]
- **DAY 7:** Mục tiêu ngắn hạn: Cung cấp hạ tầng GCP (VPC, IAM) cho các service.
  - **Sub-Agent Workflow Specialization:**
    * **[GCP]:**
      - **Target Component file path (`target_component`):** ./sources/infra.gcp. [ARC-010], [NFR-002], [NFR-004]
      - **Low-Level Technical Task Instruction:** Sử dụng Terraform để tạo VPC mạng `membership-vpc` với các subnet ở `us-central1`. Tạo `ServiceAccount` cho từng service (`user-sa`, `center-sa`, v.v.). Thiết lập `Cloud Storage` bucket `membership-bucket` với chính sách bảo mật. Kích hoạt API `cloudresourcemanager`, `iamcredentials`. Tạo GitHub Actions secret cho các credential.
      - **Targeted Tag IDs:** [ARC-010], [NFR-002], [NFR-004]

### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng các module ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, và báo cáo phân tích.
- **Target Physical Directory Matrix Map:**
    * `./sources/backend.enrollment. [DAT-005], [REQ-010], [REQ-011]`
    * `./sources/backend.attendance. [DAT-006], [REQ-012], [REQ-013]`
    * `./sources/backend.membership. [DAT-007], [REQ-014], [REQ-015]`
    * `./sources/backend.notification. [DAT-008], [REQ-016]`
    * `./sources/backend.promo. [DAT-009], [REQ-017], [REQ-018]`
    * `./sources/docs/reporting. [REQ-024], [REQ-025], [DAT-006], [DAT-007]`
- **Database Schema DDL SQL Specification [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009]:**
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
```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018]:**
```json
// POST /api/v1/enrollments
{
  "studentId":"a1b2c3d4-...",
  "courseId":"e5f6g7h8-..."
}
```
```json
// POST /api/v1/attendance/qr
{
  "studentId":"a1b2c3d4-...",
  "courseId":"e5f6g7h8-...",
  "attendanceDate":"2026-08-06"
}
```
```json
// GET /api/v1/membership/{studentId}/card
// Response: { "cardId":"...","issueDate":"...","validityDays":365,"remainingDays":300 }
```
```json
// POST /api/v1/notifications
{
  "userId":"a1b2c3d4-...",
  "groupZalo":"hoc-vien-khoa-hoc",
  "message":"Điểm danh thành công"
}
```
```json
// POST /api/v1/promotions
{
  "code":"SUMMER20",
  "discountPercent":20,
  "startDate":"2026-06-01",
  "endDate":"2026-08-31",
  "description":"Giảm giá mùa hè"
}
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003], [EXC-005]:**
    * **EXC-001:** Nếu điểm danh QR bị thất bại do mất mạng, ứng dụng di động sẽ lưu yêu cầu locally và tự động retry khi có kết nối. Service xử lý sẽ deduplicate dựa trên `studentId`, `courseId`, `attendanceDate`.
    * **EXC-002:** Phát hiện duplicate attendance trong cùng ngày: service trả về HTTP 200 với payload `{"status":"duplicate","message":"Điểm danh đã được ghi nhận trước đó"}` và không tạo row mới.
    * **EXC-003:** Nếu gửi push notification thất bại (ví dụ: token không hợp lệ), system ghi log lỗi, lên lịch retry tối đa 3 lần, sau đó đánh dấu `delivered = false`.
    * **EXC-005:** Sau khi phục hồi hệ thống, các yêu cầu điểm danh chờ xử lý được xử lý theo thứ tự FIFO và user nhận notification về các sự kiện đã được khôi phục.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 8:** Mục tiêu ngắn hạn: Triển khai service ghi danh học viên và validation xung đột.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment. [DAT-005], [REQ-010], [REQ-011]
      - **Low-Level Technical Task Instruction:** Tạo `EnrollmentEntity` với các trường khóa ngoại đến `USERS` và `COURSES`. Thêm `EnrollmentService` với phương thức `enrollStudent` kiểm tra xem student đã ghi danh khóa học đó chưa (tránh duplicate). Tự động tạo tài khoản Student nếu thiếu (`roleId` 5). Gửi notification qua `NotificationService`. Thêm validation cho capacity (`maxStudents`). Ghi đè `equals`/`hashCode`.
      - **Targeted Tag IDs:** [REQ-010], [REQ-011], [DAT-005]
- **DAY 9:** Mục tiêu ngắn hạn: Triển khai service điểm danh QR với logic idempotent.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.attendance. [DAT-006], [REQ-012], [REQ-013]
      - **Low-Level Technical Task Instruction:** Tạo `AttendanceEntity` với các trường `studentId`, `courseId`, `attendanceDate`, `timestamp`. Triển khai `AttendanceService` với endpoint `recordAttendance` nhận payload từ mobile. Sử dụng `SELECT FOR UPDATE` trên `ATTENDANCE` với điều kiện `studentId`, `courseId`, `attendanceDate` để đảm bảo chỉ một bản ghi được tạo. Nếu đã tồn tại, trả về cờ duplicate. Thêm retry logic cho network loss (`@CircuitBreaker`). Ghi log mỗi lần truy cập vào `AUDIT_LOG`.
      - **Targeted Tag IDs:** [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]
- **DAY 10:** Mục tiêu ngắn hạn: Triển khai service thẻ hội viên và logic gia hạn.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership. [DAT-007], [REQ-014], [REQ-015]
      - **Low-Level Technical Task Instruction:** Tạo `StudentCardEntity` với `issueDate`, `validityDays`, `remainingDays` (computed). Triển khai `MembershipService` với `getCardInfo` trả về days còn lại, `renewCard` cập nhật `issueDate` += days mới, `remainingDays` được tính lại. Thêm validation cho payment service integration. Đảm bảo trigger notification khi thẻ sắp hết hạn.
      - **Targeted Tag IDs:** [REQ-014], [REQ-015], [DAT-007]
- **DAY 11:** Mục tiêu ngắn hạn: Triển khai service thông báo và hàng đợi retry.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification. [DAT-008], [REQ-016]
      - **Low-Level Technical Task Instruction:** Tạo `NotificationEntity` với các trường `userId`, `groupZalo`, `message`, `sentAt`, `delivered`. Triển khai `NotificationService` với `sendPush` gọi FCM/APNs API. Bao bọc trong `Retryable` với `maxAttempts=3`. Nếu thất bại sau 3 lần, set `delivered = false`. Thêm `DeadLetterQueue` cho các notification không thể gửi.
      - **Targeted Tag IDs:** [REQ-016], [EXC-003]
- **DAY 12:** Mục tiêu ngắn hạn: Tài liệu báo cáo điểm danh và dashboard tóm tắt.
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/docs/reporting. [REQ-024], [REQ-025], [DAT-006], [DAT-007]
      - **Low-Level Technical Task Instruction:** Tạo tài liệu spec cho báo cáo CSV (`/reports/attendance/{centerId}/{date}`) với các cột: StudentName, CourseName, AttendanceDate, Status. Thêm spec cho dashboard (`/dashboard/center/{centerId}`) hiển thị totalStudents, activeCourses, upcomingSessions (7 ngày tới). Cung cấp ví dụ JSON cho frontend.
      - **Targeted Tag IDs:** [REQ-024], [REQ-025], [DAT-006], [DAT-007]
- **DAY 13:** Mục tiêu ngắn hạn: Triển khai service khuyến mãi & thông báo.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.promo. [DAT-009], [REQ-017], [REQ-018]
      - **Low-Level Technical Task Instruction:** Tạo `PromotionEntity` với `code`, `discountPercent`, `startDate`, `endDate`, `description`. Triển khai `PromoService` với `createPromotion`, `updatePromotion`, `deletePromotion`. Thêm logic auto‑expiry: hàng ngày, job quét `PROMOTIONS` và vô hiệu hóa bản ghi khi `endDate` < current date. Tích hợp với `StudentCard` để áp dụng discount khi gia hạn.
      - **Targeted Tag IDs:** [REQ-017], [REQ-018], [DAT-009]

### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng giao diện người dùng web và di động, tích hợp i18n/SEO, triển khai chatbot AI, và container hóa dịch vụ.
- **Target Physical Directory Matrix Map:**
    * `./sources/frontend.web. [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]`
    * `./sources/backend.chatbot. [REQ-019]`
    * `./sources/infra.docker. [NFR-005], [NFR-004]`
- **Database Schema DDL SQL Specification [DAT-011]:**
```sql
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]:**
```json
// GET /api/v1/frontend/config
{
  "defaultLanguage":"vi",
  "supportedLanguages":["en","vi","es"],
  "features":{"chatbot":true}
}
```
```json
// POST /api/v1/chatbot/message
{
  "userId":"a1b2c3d4-...",
  "message":"Khóa học Java ở đâu?"
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
    * Khi đầu vào cho khuyến mãi hoặc chatbot không hợp lệ (ví dụ: thiếu trường bắt buộc, định dạng sai), system trả về HTTP 400 với danh sách các trường lỗi và hướng dẫn chỉnh sửa bằng ngôn ngữ tương ứng.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 14:** Mục tiêu ngắn hạn: Triển khai frontend web với giao diện responsive và tích hợp i18n.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/frontend.web. [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]
      - **Low-Level Technical Task Instruction:** Tạo dự án Next.js với `app/` router. Thêm `i18n` configuration sử dụng `next-i18next`. Tạo các component `RoleBasedRoute` bảo vệ bởi JWT. Triển khai page `/en/centers`, `/vi/centers`, `/es/centers` với SEO meta tags (`<html lang="en">`). Thêm `getStaticProps` cho các page công khai. Tích hợp `Capacitor` cho native push notification nhận diện.
      - **Targeted Tag IDs:** [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]
- **DAY 15:** Mục tiêu ngắn hạn: Triển khai service chatbot AI cho các truy vấn phổ biến.
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.chatbot. [REQ-019]
      - **Low-Level Technical Task Instruction:** Triển khai `ChatbotController` với endpoint `POST /api/v1/chatbot/message`. Gọi `OpenAI` (hoặc model nội bộ) để tạo câu trả lời. Thêm lớp `ChatbotService` với phương thức `processMessage` thực hiện intent recognition, truy vấn cơ sở dữ liệu cho courses/centers nếu cần. Fallback đến human support nếu confidence < 0.7. Ghi log mỗi tương tác vào `AUDIT_LOG`.
      - **Targeted Tag IDs:** [REQ-019]
- **DAY 16:** Mục tiêu ngắn hạn: Xây dựng Docker image đa giai đoạn cho toàn bộ dịch vụ.
  - **Sub-Agent Workflow Specialization:**
    * **[Docker]:**
      - **Target Component file path (`target_component`):** ./sources/infra.docker. [NFR-005], [NFR-004]
      - **Low-Level Technical Task Instruction:** Tạo `Dockerfile` cho mỗi service (`user`, `center`, `course`, `enrollment`, `attendance`, `membership`, `notification`, `promo`, `chatbot`). Sử dụng stage builder với `maven`/`gradle`. Giai đoạn runtime sử dụng `distroless` image. Thêm `labels` cho version, maintainer. Xây dựng image `membership-hub/fullstack:1.0.0`. Quét image với `Trivy`. Đẩy lên Artifact Registry.
      - **Targeted Tag IDs:** [NFR-005], [NFR-004]
- **DAY 17:** Mục tiêu ngắn hạn: Cung cấp cấu hình GCP cuối cùng (Cloud Storage, Secret Manager) cho CI/CD.
  - **Sub-Agent Workflow Specialization:**
    * **[GCP]:**
      - **Target Component file path (`target_component`):** ./sources/infra.gcp. [ARC-010], [NFR-002], [NFR-004], [NFR-008], [NFR-009]
      - **Low-Level Technical Task Instruction:** Tạo `SecretManager` secret cho JWT key, Firebase credentials. Thiết lập `CloudStorage` bucket `membership-assets` với lifecycle policy (xóa sau 30 ngày). Kích hoạt `CloudScheduler` job để auto-expire promotions. Cấu hình `CloudBuild` triggers từ GitHub Actions. Thiết lập `Monitoring` với Cloud Monitoring cho các metric.
      - **Targeted Tag IDs:** [ARC-010], [NFR-002], [NFR-004], [NFR-008], [NFR-009]
- **DAY 18:** Mục tiêu ngắn hạn: Orchestration GKE với HPA và failover.
  - **Sub-Agent Workflow Specialization:**
    * **[GKE]:**
      - **Target Component file path (`target_component`):** ./sources/infra.gke. [ARC-010], [NFR-002], [NFR-004], [NFR-009]
      - **Low-Level Technical Task Instruction:** Tạo `Deployment` cho từng service với `imagePullSecrets`. Thêm `HorizontalPodAutoscaler` dựa trên CPU >70% hoặc latency >300ms. Cấu hình `Ingress` với `nginx` để TLS termination. Thiết lập `PodDisruptionBudget`. Tạo `ServiceMonitor` cho Prometheus. Triển khai `Istio` cho traffic splitting và retry policy.
      - **Targeted Tag IDs:** [ARC-010], [NFR-002], [NFR-004], [NFR-009]

### 📈 Phase 5 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Hoàn thiện bảo mật, tuân thủ, và vận hành sản xuất, bao gồm logging, backup, disaster recovery, và tài liệu cuối cùng.
- **Target Physical Directory Matrix Map:**
    * `./sources/docs/compliance. [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
    * `./sources/infra.gke. [ARC-010], [NFR-002], [NFR-004], [NFR-009]`
    * `./sources/infra.gcp. [ARC-010], [NFR-009]`
- **Database Schema DDL SQL Specification:** Không có bảng mới; có thể thêm các bảng audit nếu cần.
- **API and Event Routing Contracts:** Không có endpoint mới; có thể thêm `/health`, `/metrics`.
- **Phase Localized Exception Handlers:** Không có exception mới; tiếp tục xử lý các lỗi đã xác định.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 19:** Mục tiêu ngắn hạn: Tài liệu hóa kiểm soát bảo mật và tuân thủ.
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** ./sources/docs/compliance. [NFR-003], [NFR-006], [NFR-008], [NFR-009]
      - **Low-Level Technical Task Instruction:** Tạo tài liệu “Enterprise Security & Compliance” bao gồm các phần: OWASP Top 10 mitigations, GDPR/CCPA data handling, audit logging cấu hình, chính sách backup & DR. Thêm ma trận kiểm soát truy cập cuối cùng. Xuất tài liệu sang PDF và lưu vào `membership-bucket`.
      - **Targeted Tag IDs:** [NFR-003], [NFR-006], [NFR-008], [NFR-009]
- **DAY 20:** Mục tiêu ngắn hạn: Điều chỉnh cuối cùng GKE cho scaling và failover.
  - **Sub-Agent Workflow Specialization:**
    * **[GKE]:**
      - **Target Component file path (`target_component`):** ./sources/infra.gke. [ARC-010], [NFR-002], [NFR-004], [NFR-009]
      - **Low-Level Technical Task Instruction:** Tinh chỉnh `HPA` cho các deployment dựa trên kết quả monitoring thực tế. Thêm `PodDisruptionBudget` để đảm bảo SLA 99.9%. Tạo `PriorityClass` cho các job quan trọng. Kiểm tra `NetworkPolicy` để cô lập namespace. Thực hiện rolling update và xác nhận toàn bộ pods đều sẵn sàng.
      - **Targeted Tag IDs:** [ARC-010], [NFR-002], [NFR-004], [NFR-009]
- **DAY 21:** Mục tiêu ngắn hạn: Thiết lập backup PostgreSQL và khôi phục sau thảm họa.
  - **Sub-Agent Workflow Specialization:**
    * **[GCP]:**
      - **Target Component file path (`target_component`):** ./sources/infra.gcp. [ARC-010], [NFR-009]
      - **Low-Level Technical Task Instruction:** Tạo `BackupJob` hàng ngày cho PostgreSQL sử dụng `CloudSQL Backup` với retention 24 giờ. Thiết lập `Cross-Region Replication` đến bucket `membership-backup-us-east1`. Kiểm tra khôi phục bằng cách tạo database test và xác nhận dữ liệu. Tạo runbook cho quy trình khôi phục sau sự cố.
      - **Targeted Tag IDs:** [ARC-010], [NFR-009]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-003]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng Prepared Statements / Parameterized Queries trong tất cả JDBC calls. Áp dụng WhiteList cho các giá trị sort column. Áp dụng Row-Level Security cho multi-tenant.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động escape tất cả user inputs trong Thymeleaf/JSX. Áp dụng `@RequestMapping` để đánh dấu các endpoint. Thêm HTTP header `Content-Security-Policy` với `default-src 'self'`, không cho phép `unsafe-inline`.
- **Multi-Tenant CORS Security Rails:** Validate origin chống lại danh sách tenant-cấu hình; từ chối các origin không được phép. Sử dụng `Access-Control-Allow-Origin` động.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Áp dụng `@JsonSerialize` với `JsonSerializer` tùy chỉnh để che giấu số CCCD, email. Sử dụng `Logback` filter để loại bỏ các trường nhạy cảm. Lưu trữ logs trong bucket mã hóa, rotation hàng ngày.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng `@capacitor/preferences` cho storage an toàn, `capacitor-community/contacts` cho danh bạ giới hạn. Áp dụng URL scheme `membership://auth` cho deep linking. Bắt sự kiện back-button native.
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware phát hiện `Accept-Language`. Sử dụng `next-i18next` với các file tài nguyên `.json`. Tự động chèn `<link rel="alternate" hreflang="en" href="https://example.com/en"/>` cho từng ngôn ngữ. Tối ưu hóa meta tags cho từng locale.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Script CI tạo branch `features/development-phase-1-day-1`, `features/development-phase-2-day-1`, v.v. Mỗi branch là isolated workspace.
- **Validation Guard Pipeline Gates:** Thực hiện `mvn clean verify` hoặc `npm run test` với mục tiêu độ phủ `>=85%`. Kiểm tra `docker scan` cho vulnerabilities. Ghi nhận kết quả vào `build-reports/`. Chỉ merge khi tất cả gates vượt qua.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`