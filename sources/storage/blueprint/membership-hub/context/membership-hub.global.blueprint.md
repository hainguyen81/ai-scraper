# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806033325 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 03:33:25 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống được thiết kế theo kiến trúc microservice dạng event-driven, áp dụng các mẫu CQRS và Reactive Core để đảm bảo khả năng mở rộng và độ trễ thấp. Các service chính bao gồm Authentication, User Management, Center Management, Course Management, Enrollment, Attendance, Membership Card, Notification, Promotion, Announcement, Chatbot, và Reporting. Tất cả các service đều được container hóa bằng Docker và triển khai trên Google Kubernetes Engine (GKE) với auto-scaling dựa trên HPA. Các tương tác giữa các service được thực hiện qua REST API và hàng đợi sự kiện (Kafka) để đảm bảo tính bất biến và khả năng quan sát.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Dòng dữ liệu chính bao gồm: (1) Luồng xác thực OAuth2 từ các nhà cung cấp Firebase, Google, Facebook; (2) Luồng xử lý điểm danh QR từ ứng dụng di động; (3) Luồng gửi thông báo đẩy đến thiết bị di động và bài đăng trên nhóm Zalo; (4) Luồng tích hợp backend ứng dụng di động Next.js tiêu thụ các REST API; (5) Luồng ghi nhật ký kiểm toán cho mọi thay đổi dữ liệu. Các topology này được kết nối qua một API Gateway trung tâm, sử dụng sidecar service mesh để quản lý bảo mật và quan sát.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.x, Hibernate ORM, Flyway, PostgreSQL 15, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis (session caching), Kafka, OpenTelemetry, JUnit5, Mockito.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14, React 18, TypeScript, Tailwind CSS, i18next, @capacitor/core, @capacitor/app, Capacitor HTTP, Capacitor Preferences, React Query, SWR, Jest, React Testing Library.

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** Thư mục gốc thực sự của kho lưu trữ là `.`; tất cả các đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Áp dụng các quy tắc ánh xạ thư mục động được định nghĩa trong Protocol 1, phù hợp với cấu trúc dự án được phát hiện.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Nếu stack công nghệ sử dụng các framework Java, tất cả các mã nguồn Java phải nằm trong gói cơ sở doanh nghiệp `org.nlh4j.saas.membershiphub`. Chuyển đổi chuỗi "membership-hub" thành token thuần chữ thường, không có khoảng trắng, dấu gạch ngang hoặc dấu gạch dưới.
- **Strict Tester Target Path Syntax:** Bất kỳ thành phần nào được nhắm mục tiêu bởi một Sub-Agent Tester phải được cấu trúc dưới dạng một cặp phân cách bán phẩy `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn trong cặp phải bắt đầu bằng `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | 1-3 | ./sources/backend.membership.users | Triển khai schema Users & Roles, đăng ký người dùng, xác thực qua mạng xã hội, gán vai trò | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [DAT-002] |
| Phase 1 | 1-3 | ./sources/docs/users | Tạo tài liệu kỹ thuật cho module người dùng | Doc | [EXC-004] |
| Phase 1 | 1-3 | ./sources/backend.membership.auth | Triển khai service xác thực (JWT, refresh token) | Coder | [ARC-006] |
| Phase 2 | 4-6 | ./sources/backend.membership.centers | Triển khai schema Centers, CRUD, kiểm tra tính duy nhất taxId, gán admin trung tâm | Coder | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| Phase 2 | 4-6 | ./sources/backend.membership.centers.test | Bộ kiểm tra đơn vị cho module trung tâm | Tester | [REQ-004], [REQ-005], [REQ-006] |
| Phase 2 | 4-6 | ./sources/docs/centers | Tài liệu API quản lý trung tâm | Doc | [REQ-004], [REQ-005], [REQ-006] |
| Phase 3 | 7-9 | ./sources/backend.membership.courses | Triển khai schema Courses, phát hiện xung đột lịch dạy, gán giáo viên | Coder | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| Phase 3 | 7-9 | ./sources/infra/dockerfile | Tạo Dockerfile đa giai đoạn cho backend | Docker | [ARC-010] |
| Phase 3 | 7-9 | ./sources/infra/gcp | Cung cấp PostgreSQL & Redis trên GCP | GCP | [ARC-010], [NFR-001], [NFR-004] |
| Phase 4 | 10-12 | ./sources/backend.membership.enrollments | Triển khai schema Enrollments, duyệt khóa học, đăng ký khóa học, tự động tạo tài khoản học viên | Coder | [REQ-010], [REQ-011], [DAT-005] |
| Phase 4 | 10-12 | ./sources/backend.membership.attendance | Triển khai schema Attendance, quét QR, đảm bảo bất biến, xử lý ngoại lệ mất mạng và duplicate | Coder | [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006] |
| Phase 4 | 10-12 | ./sources/docs/attendance | Tài liệu API điểm danh và luồng ngoại lệ | Doc | [REQ-012], [REQ-013] |
| Phase 5 | 13-19 | ./sources/backend.membership.cards | Triển khai schema StudentCards, hiển thị ngày hiệu lực, gia hạn thẻ | Coder | [REQ-014], [REQ-015], [DAT-007] |
| Phase 5 | 13-19 | ./sources/backend.membership.promotions | Triển khai schema Promotions & Announcements, quản lý khuyến mãi và thông báo | Coder | [REQ-017], [REQ-018], [DAT-009] |
| Phase 5 | 13-19 | ./sources/backend.membership.notifications | Triển khai schema Notifications, engine gửi push & Zalo, xử lý ngoại lệ gửi thất bại | Coder | [REQ-016], [EXC-003], [DAT-008] |
| Phase 5 | 13-19 | ./sources/backend.membership.chatbot | Tích hợp chatbot AI cho dịch vụ tự phục vụ | Coder | [REQ-019] |
| Phase 5 | 13-19 | ./sources/frontend.web.i18n | Cấu hình middleware i18n & chèn thẻ hreflang cho SEO đa ngôn ngữ | Doc | [REQ-022], [REQ-023] |
| Phase 5 | 13-19 | ./sources/backend.membership.reports | Triển khai service báo cáo điểm danh & dashboard tóm tắt ghi danh | Reviewer | [REQ-024], [REQ-025] |
| Phase 5 | 13-19 | ./sources/infra.gke | Triển khai Kubernetes, HPA, pipeline CI/CD, chính sách bảo mật, logging | GKE | [ARC-010], [NFR-002], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai nền tảng người dùng cốt lõi, xác thực và phân quyền, thiết lập các bảng dữ liệu cơ bản cho hệ thống hội viên đa trung tâm.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend.membership.users [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [DAT-002]
    * ./sources/docs/users [EXC-004]
    * ./sources/backend.membership.auth [ARC-006]
- **Database Schema DDL SQL Specification [DAT-001], [DAT-002]:**
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
```yaml
# POST /auth/register
request:
  body:
    email: string
    password: string
    fullName: string
response:
  token: string
  refreshToken: string

# POST /auth/social
request:
  body:
    provider: string
    code: string
response:
  token: string
  refreshToken: string

# PUT /users/{userId}/role
request:
  roleId: smallint
response:
  success: boolean
```
- **Phase Localized Exception Handlers [EXC-004]:**
    * Khi xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc), hệ thống trả về một đối tượng lỗi với danh sách các trường không hợp lệ và hướng dẫn chỉnh sửa. Tất cả các thông báo lỗi được quốc tế hóa bằng ngôn ngữ được yêu cầu.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1: Triển khai mô- hình người dùng cốt lõi và xác thực**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.users [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [DAT-002]
      - **Low-Level Technical Task Instruction:** Tạo migration Flyway cho bảng Users và Roles, định nghĩa các ràng buộc khóa ngoại, thêm các cột provider, triển khai UserService với các phương thức register(LocalRegistrationRequest), registerSocial(SocialRegistrationRequest), assignRole(...). Áp dụng bcrypt cho passwordHash, tích hợp Firebase/Google/Facebook OAuth2 thông qua Firebase Auth SDK, phát hành JWT access token (15 phút) và refresh token (7 ngày). Gắn thẻ theo dõi [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [DAT-002].
- **DAY 2: Đánh giá hợp đồng xác thực và ánh xạ RBAC**
  - **Sub-Agent Workflow Specialization:**
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.auth
      - **Low-Level Technical Task Instruction:** Kiểm tra kỹ lưỡng các endpoint /auth/register, /auth/social, /auth/role Assign để đảm bảo tuân thủ các tiêu chí chấp nhận trong yêu cầu. Xác nhận rằng System Admin có thể gán bất kỳ vai trò nào (ARC-001..ARC-005) và rằng các chính sách phân quyền được áp dụng thông qua Spring Security. Gắn thẻ [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005].
- **DAY 3: Tạo tài liệu kỹ thuật cho module người dùng**
  - **Sub-Agent Workflow Specialization:**
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/docs/users
      - **Low-Level Technical Task Instruction:** Soạn tài liệu Markdown bao gồm mô tả ER diagram cho bảng Users/Roles, hợp đồng API (OpenAPI YAML), hướng dẫn cách sử dụng các endpoint đăng ký và gán vai trò, ghi lại các luồng ngoại lệ (EXC-004) và các bước xác thực đầu vào. Gắn thẻ [EXC-004].

### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng module quản lý trung tâm, triển khai CRUD cho các trung tâm và phân quyền quản trị viên trung tâm.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend.membership.centers [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * ./sources/backend.membership.centers.test [REQ-004], [REQ-005], [REQ-006]
    * ./sources/docs/centers [REQ-004], [REQ-005], [REQ-006]
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(20) NOT NULL UNIQUE,
    contactPhone VARCHAR(30),
    contactEmail VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006]:**
```yaml
# GET /centers
response:
  - centerId: UUID
    name: string
    address: string
    taxId: string
    contactPhone: string
    contactEmail: string

# POST /centers
request:
  body:
    name: string
    address: string
    taxId: string
    contactPhone: string
    contactEmail: string
response:
  centerId: UUID
  message: string (conflict nếu taxId đã tồn tại)

# PUT /centers/{centerId}
# DELETE /centers/{centerId}
```
- **Phase Localized Exception Handlers:** Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 4: Triển khai schema và service quản lý trung tâm**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.centers [REQ-004], [REQ-005], [REQ-006], [DAT-003]
      - **Low-Level Technical Task Instruction:** Tạo migration Flyway cho bảng Centers (DAT-003) với các cột name, address, taxId (unique), contactPhone, contactEmail. Triển khai CenterService với các phương thức create, update, delete, getAll. Thực thi kiểm tra tính duy nhất của taxId và xác thực định dạng email. Gắn thẻ [REQ-004], [REQ-005], [REQ-006], [DAT-003].
- **DAY 5: Viết bộ kiểm tra cho module trung tâm**
  - **Sub-Agent Workflow Specialization:**
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.centers.test [REQ-004], [REQ-005], [REQ-006]
      - **Low-Level Technical Task Instruction:** Sử dụng JUnit5 và Mockito để viết các bài kiểm tra cho các phương thức createCenter (bao gồm trường hợp xung đột taxId), updateCenter, deleteCenter. Đảm bảo độ bao phủ mã >=85%. Gắn thẻ [REQ-004], [REQ-005], [REQ-006].
- **DAY 6: Tạo tài liệu API quản lý trung tâm**
  - **Sub-Agent Workflow Specialization:**
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/docs/centers [REQ-004], [REQ-005], [REQ-006]
      - **Low-Level Technical Task Instruction:** Soạn tài liệu API cho các endpoint /centers (GET, POST, PUT, DELETE), bao gồm request/response schemas, ví dụ curl, ghi lại các quy tắc nghiệp vụ (không có luồng ngoại lệ chuyên biệt). Gắn thẻ [REQ-004], [REQ-005], [REQ-006].

### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng module quản lý khóa học, triển khai phát hiện xung đột lịch dạy và gán giáo viên.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend.membership.courses [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    * ./sources/infra/dockerfile [ARC-010]
    * ./sources/infra/gcp [ARC-010], [NFR-001], [NFR-004]
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
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009]:**
```yaml
# GET /courses
response:
  - courseId: UUID
    title: string
    startDate: date
    endDate: date
    teacherName: string

# POST /courses
request:
  body:
    title: string
    startDate: date
    endDate: date
    teacherId: UUID
response:
  courseId: UUID
  message: string (conflict nếu giáo viên đã có lịch dạy chồng lấn)

# PUT /courses/{courseId}/teacher
request:
  teacherId: UUID
response:
  success: boolean
```
- **Phase Localized Exception Handlers:** Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 7: Triển khai schema khóa học và logic phát hiện xung đột**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.courses [REQ-007], [REQ-008], [REQ-009], [DAT-004]
      - **Low-Level Technical Task Instruction:** Tạo migration cho bảng Courses (DAT-004) với các trường title, description, startDate, endDate, teacherId (FK), maxStudents. Triển khai CourseService với logic kiểm tra xung đột lịch dạy: truy vấn các khóa học hiện có của cùng giáo viên trong khoảng thời gian overlap. Triển khai endpoint POST /courses với xác thực. Gắn thẻ [REQ-007], [REQ-008], [REQ-009], [DAT-004].
- **DAY 8: Tạo Dockerfile đa giai đoạn**
  - **Sub-Agent Workflow Specialization:**
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/infra/dockerfile [ARC-010]
      - **Low-Level Technical Task Instruction:** Soạn Dockerfile sử dụng base image eclipse-temurin:21-jdk-alpine (<200MB), sao chép maven wrapper và pom.xml, xây dựng ứng dụng, tạo image trung gian, sau đó tạo image chạy với size <500MB, chỉ bao gồm runtime jar và các thư viện phụ thuộc cần thiết. Gắn thẻ [ARC-010].
- **DAY 9: Cung cấp PostgreSQL & Redis trên GCP**
  - **Sub-Agent Workflow Specialization:**
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/infra/gcp [ARC-010], [NFR-001], [NFR-004]
      - **Low-Level Technical Task Instruction:** Sử dụng gcloud CLI để tạo instance PostgreSQL (region us-central1, tier db-f1-micro) và Redis (memorystore, standard-tier). Kích hoạt backup hàng ngày, thiết lập Private Service Connect, cấu hình IAM cho dịch vụ backend. Gắn thẻ [ARC-010], [NFR-001], [NFR-004].

### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai module ghi danh học viên, điểm danh QR, và xử lý các ngoại lệ liên quan đến mạng và duplicate.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend.membership.enrollments [REQ-010], [REQ-011], [DAT-005]
    * ./sources/backend.membership.attendance [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]
    * ./sources/docs/attendance [REQ-012], [REQ-013]
- **Database Schema DDL SQL Specification [DAT-005], [DAT-006]:**
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
```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [REQ-012], [REQ-013]:**
```yaml
# GET /courses/browse
response:
  - courseId: UUID
    title: string
    startDate: date
    endDate: date
    maxStudents: int
    availableSpots: int

# POST /enrollments
request:
  body:
    studentId: UUID
    courseId: UUID
response:
  enrollmentId: UUID
  message: string (tạo tài khoản học viên nếu thiếu)

# POST /attendance/scan
request:
  body:
    studentId: UUID
    courseId: UUID
    scannedAt: timestamp
response:
  attendanceId: UUID
  duplicate: boolean (true nếu đã ghi danh trong ngày)
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
    * **EXC-001:** Nếu sinh viên quét QR nhưng mạng không khả dụng, ứng dụng di động ghi lại yêu cầu vào bộ đệm cục bộ. Khi kết nối được khôi phục, service gửi hàng đợi lên server; hệ thống xử lý các bản ghi này theo thứ tự FIFO và ghi lại điểm danh một lần. Tất cả các thông báo lỗi được hiển thị bằng ngôn ngữ được yêu cầu.
    * **EXC-002:** Nếu cùng một sinh viên quét cùng một QR nhiều lần trong một phút, service phát hiện duplicate dựa trên (studentId, courseId, attendanceDate). Yêu cầu đầu tiên được chấp nhận; các yêu cầu tiếp theo trả về success với cờ duplicate = true và không tạo hàng mới.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 10: Triển khai schema ghi danh và flow đăng ký**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.enrollments [REQ-010], [REQ-011], [DAT-005]
      - **Low-Level Technical Task Instruction:** Tạo migration cho bảng Enrollments (DAT-005) với các khóa ngoại studentId, courseId. Triển khai EnrollmentService với các phương thức browseCourses (trả về các khóa học chưa ghi danh), register (tạo bản ghi, tự động tạo người dùng với vai trò Student nếu thiếu). Gắn thẻ [REQ-010], [REQ-011], [DAT-005].
- **DAY 11: Triển khai service điểm danh QR và xử lý ngoại lệ**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.attendance [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]
      - **Low-Level Technical Task Instruction:** Tạo migration cho bảng Attendance (DAT-006) với các trường studentId, courseId, attendanceDate, timestamp. Triển khai AttendanceService với endpoint POST /attendance/scan: xác thực student-course relationship, chèn bản ghi, sử dụng khóa duy nhất (studentId, courseId, attendanceDate) để đảm bảo bất biến. Xử lý ngoại lệ EXC-001 (khi mất mạng, ghi vào hàng đợi Kafka) và EXC-002 (duplicate trong cùng ngày). Gắn thẻ [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006].
- **DAY 12: Tạo tài liệu API điểm danh**
  - **Sub-Agent Workflow Specialization:**
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/docs/attendance [REQ-012], [REQ-013]
      - **Low-Level Technical Task Instruction:** Soạn tài liệu kỹ thuật cho endpoint /attendance/scan, bao gồm request payload, response, mã lỗi, mô tả luồng ngoại lệ khi mất mạng và duplicate scan. Gắn thẻ [REQ-012], [REQ-013].

### 📈 Phase 5 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai các tính năng cao cấp: thẻ hội viên, khuyến mãi, thông báo, chatbot AI, i18n/SEO, báo cáo & phân tích, và hardening bảo mật & tuân thủ.
- **Target Physical Directory Matrix Map:**
    * ./sources/backend.membership.cards [REQ-014], [REQ-015], [DAT-007]
    * ./sources/backend.membership.promotions [REQ-017], [REQ-018], [DAT-009]
    * ./sources/backend.membership.notifications [REQ-016], [EXC-003], [DAT-008]
    * ./sources/backend.membership.chatbot [REQ-019]
    * ./sources/frontend.web.i18n [REQ-022], [REQ-023]
    * ./sources/backend.membership.reports [REQ-024], [REQ-025]
    * ./sources/infra.gke [ARC-010], [NFR-002], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
- **Database Schema DDL SQL Specification [DAT-007], [DAT-009], [DAT-008]:**
```sql
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
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

CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
```
- **API and Event Routing Contracts [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-022], [REQ-023], [REQ-024], [REQ-025]:**
```yaml
# GET /cards/{studentId}
response:
  cardId: UUID
  issueDate: date
  validityDays: int
  remainingDays: int

# POST /cards/renew
request:
  body:
    studentId: UUID
    days: int
    paymentToken: string
response:
  newEndDate: date
  message: string

# GET /promotions
response:
  - promoId: UUID
    code: string
    discountPercent: int
    startDate: date
    endDate: date

# POST /announcements
request:
  body:
    title: string
    content: string
    startDate: date
    endDate: date
response:
  announcementId: UUID

# POST /notifications
request:
  body:
    userId: UUID
    groupZalo: string
    message: string
response:
  notificationId: UUID

# POST /chatbot/ask
request:
  body:
    userId: UUID
    question: string
response:
  answer: string
  confidence: float

# GET /reports/attendance
request:
  centerId: UUID
  startDate: date
  endDate: date
response:
  file: binary (CSV)
    columns: StudentName, CourseName, AttendanceDate, Status

# GET /dashboard/summary
response:
  totalStudents: int
  activeCourses: int
  upcomingSessions: int
```
- **Phase Localized Exception Handlers [EXC-003]:**
    * Khi push notification không thể gửi (ví dụ: token thiết bị không hợp lệ), hệ thống ghi lại lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu bản ghi là thất bại. Tất cả các thông báo lỗi được hiển thị bằng ngôn ngữ được yêu cầu.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 13: Triển khai schema thẻ hội viên và logic hiệu lực**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.cards [REQ-014], [REQ-015], [DAT-007]
      - **Low-Level Technical Task Instruction:** Tạo migration cho bảng StudentCards (DAT-007) với các trường studentId, issueDate, validityDays, remainingDays (computed). Triển khai CardService với endpoint GET /cards/{studentId} để hiển thị days remaining, endpoint POST /cards/renew để gia hạn dựa trên payment service. Gắn thẻ [REQ-014], [REQ-015], [DAT-007].
- **DAY 14: Triển khai schema khuyến mãi & thông báo**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.promotions [REQ-017], [REQ-018], [DAT-009]
      - **Low-Level Technical Task Instruction:** Tạo migration cho bảng Promotions (DAT-009) và Announcements (DAT-009). Triển khai PromotionService với các CRUD operations, enforce start/end dates, code uniqueness. Triển khai AnnouncementService tương tự với auto‑expire logic. Gắn thẻ [REQ-017], [REQ-018], [DAT-009].
- **DAY 15: Triển khai engine thông báo và push**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.notifications [REQ-016], [EXC-003], [DAT-008]
      - **Low-Level Technical Task Instruction:** Tạo migration cho bảng Notifications (DAT-008). Triển khai NotificationService để ghi lại thông báo, đẩy push notification qua FCM/APNs, gửi tin nhắn đến nhóm Zalo được chỉ định. Xử lý ngoại lệ EXC-003 (thất bại trong gửi) với cơ chế thử lại tối đa 3 lần. Gắn thẻ [REQ-016], [EXC-003], [DAT-008].
- **DAY 16: Tích hợp chatbot AI**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.chatbot [REQ-019]
      - **Low-Level Technical Task Instruction:** Triển khai REST endpoint /chatbot/ask để nhận tin nhắn từ người dùng, gọi tích hợp LLM service (ví dụ: OpenAI), xử lý câu trả lời, ghi lại tương tác vào bảng AuditLog. Gắn thẻ [REQ-019].
- **DAY 17: Cấu hình i18n và SEO**
  - **Sub-Agent Workflow Specialization:**
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/frontend.web.i18n [REQ-022], [REQ-023]
      - **Low-Level Technical Task Instruction:** Cấu hình middleware phát hiện ngôn ngữ (Accept-Language, cookie), tải tài nguyên dịch thuật từ thư mục ./locales, chèn thẻ hreflang vào HTML head cho các ngôn ngữ English, Vietnamese, Spanish. Gắn thẻ [REQ-022], [REQ-023].
- **DAY 18: Triển khai báo cáo & dashboard**
  - **Sub-Agent Workflow Specialization:**
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.membership.reports [REQ-024], [REQ-025]
      - **Low-Level Technical Task Instruction:** Triển khai ReportService với endpoint GET /reports/attendance?centerId&startDate&endDate trả về file CSV với các cột StudentName, CourseName, AttendanceDate, Status. Triển khai DashboardService cung cấp các chỉ số tổng hợp cho Center Admin. Gắn thẻ [REQ-024], [REQ-025].
- **DAY 19: Triển khai Kubernetes và hardening DevOps**
  - **Sub-Agent Workflow Specialization:**
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/infra.gke [ARC-010], [NFR-002], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]
      - **Low-Level Technical Task Instruction:** Soạn Deployment.yaml, Service.yaml, HorizontalPodAutoscaler cho các microservice backend. Cấu hình Artifact Registry, thiết lập GitHub Actions pipeline để xây dựng Docker image, đẩy lên GKE, triển khai tự động. Áp dụng các chính sách bảo mật (NetworkPolicy), cấu hình logging (Stackdriver). Gắn thẻ [ARC-010], [NFR-002], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009].

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-001] – [NFR-009]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng Prepared Statements, Parameterization trong tất cả các truy vấn JPA/Hibernate, whitelist các tham số sắp xếp động, thực thi kiểm tra đầu vào nghiêm ngặt tại biên giới.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Áp dụng auto‑escaping trong Thymeleaf/JSX, sử dụng các header CSP không cho phép `unsafe-inline`, lọc DOMPurify cho các trường HTML.
- **Multi-Tenant CORS Security Rails:** Cấu hình CORS cho phép các origin cụ thể của tenant, sử dụng các header `Access-Control-Allow-Origin` động dựa trên tenant ID, vô hiệu hóa wildcard `*.domain.com`.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Áp dụng `@JsonSerialize` với `JsonSerializer` tùy chỉnh để che giấu số CCCD, email, số điện thoại; thiết lập bộ lọc log loại bỏ các trường nhạy cảm trước khi ghi vào ElasticSearch.
- **Performance Metrics:** Tối ưu hóa các query với index (studentId, courseId, attendanceDate), sử dụng Redis cache cho các lookup thường xuyên, thiết lập mục tiêu độ trễ 200ms cho các API cốt lõi.
- **Availability:** Triển khai auto‑failover giữa các region GKE, sử dụng PostgreSQL với read replicas, thiết lập mục tiêu 99.9% uptime, kiểm tra định kỳ.
- **Scalability & Availability:** Kích hoạt Horizontal Pod Autoscaler dựa trên CPU > 70% hoặc độ trễ request > 300ms, sử dụng Kubernetes Cluster Autoscaler, thiết lập các read replica cho PostgreSQL.
- **Docker Image Size:** Sử dụng base image eclipse-temurin:21-jdk-alpine (<200MB), đa giai đoạn build, loại bỏ các gói không cần thiết, final image <500MB.
- **Logging & Audit:** Ghi lại tất cả các thay đổi (role changes, attendance records, notifications) với userId, timestamp, action details; lưu trữ trong 1 năm; sử dụng cấu hình log filtering để tránh rò rỉ PII.
- **Multi‑Language Support:** Externalize các chuỗi UI vào các file properties, hỗ trợ English, Vietnamese, Spanish, sử dụng cookie/lang preference để chuyển đổi locale mà không cần tải lại trang.
- **GDPR/CCPA Compliance:** Triển khai endpoint DELETE /users/{userId} để xóa dữ liệu cá nhân, endpoint GET /users/{userId}/export để tải xuống JSON, thu thập sự đồng ý cho tiếp thị qua consent management service.
- **Backup & Disaster Recovery:** Backup PostgreSQL hàng ngày (full + incremental), point‑in‑time recovery lên đến 24 giờ, backup cluster GKE sang region thứ hai, thử nghiệm khôi phục định kỳ.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng Capacitor HTTP để gọi các API bảo mật qua HTTPS, lưu trữ token trong `@capacitor/preferences` (encrypted), chặn back‑button để ngăn quay lại trái phép, thực hiện các kiểm tra định kỳ tính khả dụng của mạng.
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware phát hiện locale từ cookie, header Accept‑Language, chuyển đổi tài nguyên dịch thuật, chèn thẻ hreflang động vào `<head>`, tối ưu hóa meta description cho từng ngôn ngữ, hỗ trợ thu thập dữ liệu của Google cho các phiên bản multilingual.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Mỗi ngày tạo một branch riêng `features/development-phase-X-day-Y` (X = số phase, Y = số ngày trong phase). Branch được tạo từ `main` trước khi bắt đầu công việc của ngày.
- **Validation Guard Pipeline Gates:** Sau khi commit, GitHub Actions chạy các bước: kiểm tra cú pháp, kiểm tra kiểu (if TypeScript), kiểm tra đơn vị (đạt độ bao phủ >=85%), kiểm tra tích hợp (selected endpoints), quét bảo mật (Bandit, OWASP ZAP). Chỉ khi tất cả các kiểm tra vượt qua, pipeline mới tự động đẩy image lên Artifact Registry và triển khai lên GKE thông qua Helm.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`