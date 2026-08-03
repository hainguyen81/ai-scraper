# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260803132420 |
| **Tên Dự án** | membership-hub |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày.Giờ** | 2026/08/03 13:24:20 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống là một nền tảng hội viên đa trung tâm được thiết kế theo kiến trúc module hóa với backend Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE) và các dịch vụ xác thực bên ngoài (Firebase, Google, Facebook OAuth2). Mô hình kiến trúc tuân theo các nguyên tắc CQRS và sự kiện để tách biệt đọc/ghi, sử dụng Redis cho caching phiên và hàng đợi bất đồng bộ cho thông báo. Các ranh giới an ninh được xác định rõ ràng theo ma trận RBAC (System Admin, Center Admin, Manager, Teacher, Student). Luồng dữ liệu chính bao gồm xác thực (ARC‑006), xử lý điểm danh QR (ARC‑007), thông báo đa kênh (ARC‑008) và tích hợp backend ứng dụng di động (ARC‑009). Hệ thống hỗ trợ đa ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha) với các chuỗi UI được ngoại biên hóa và các thẻ hreflang cho SEO.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Luồng xác thực (ARC‑006) sử dụng OAuth2 để trao đổi mã lấy thông tin người dùng, tạo JWT (15 phút) và refresh token (7 ngày). Luồng xử lý điểm danh QR (ARC‑007) ghi nhận điểm danh một cách bất biến thông qua một service chuyên biệt. Luồng thông báo (ARC‑008) đẩy notification đến ứng dụng di động qua FCM/APNs và đồng thời đăng bài lên nhóm Zalo được chỉ định. Frontend Next.js tiêu thụ các REST API (ARC‑009) với caching ngoại tuyến qua IndexedDB. Các kênh bất đồng bộ sử dụng Redis pub/sub để đảm bảo tính idempotent của điểm danh và hàng đợi thông báo.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.x, PostgreSQL 15, Docker (multi‑stage), Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM) / Apple APNs, Zalo API, Redis (Lettuce), GitHub Actions CI/CD, Flyway/Liquibase, JUnit 5, Mockito, OpenTelemetry.
- **Frontend & Cross‑Platform UI Mobile Stack:** Next.js 14, React 18, TypeScript, i18next cho nội địa hóa, Capacitor (bridge to native), React‑Query cho caching ngoại tuyến, Tailwind CSS, Jest / React‑Testing‑Library, ESLint/Prettier, Swift/Kotlin native modules cho push notification.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** Root repository workspace được cố định tại `..`. Tất cả các đường dẫn vật lý mục tiêu phải bắt đầu bằng `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Backend logic nằm dưới `./sources/backend.` (hoặc `./sources/backend.<service-name>.` nếu có nhiều service). Frontend nằm dưới `./sources/frontend.` (hoặc `./sources/frontend.<app-name>.`). Hạ tầng DevOps nằm dưới `./sources/infra.`.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Tất cả mã nguồn Java phải nằm trong gói `org.nlh4j.saas.membershiphub`. (Tên dự án đã được chuẩn hóa theo quy tắc alphanumeric lowercase).
- **Strict Tester Target Path Syntax:** Bất kỳ thành phần nào được Tester nhắm đến phải được biểu diễn dưới dạng cặp `<source_component>;<test_suite_file>` với cả hai đường dẫn bắt đầu bằng `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Giai đoạn 1** | Ngày 1 - Ngày 3 | `./sources/backend.users`, `./sources/backend.auth`, `./sources/infra.dockerfile` | Xây dựng service người dùng, service xác thực, hình ảnh Docker cơ bản và cấu hình GCP ban đầu. | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [DAT-011], [NFR-001], [NFR-003], [NFR-006], [EXC-004] |
| **Giai đoạn 2** | Ngày 4 - Ngày 5 | `./sources/backend.centers`, `./sources/backend.courses`, `./sources/backend.enrollments`, `./sources/backend.promotions` | Triển khai CRUD trung tâm, khóa học, ghi danh và các bảng khuyến mãi & thông báo. | Coder | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-003], [DAT-004], [DAT-005], [DAT-009], [NFR-002], [NFR-004] |
| **Giai đoạn 3** | Ngày 6 - Ngày 7 | `./sources/backend.attendance`, `./sources/backend.membership`, `./sources/backend.qr` | Xây dựng service điểm danh, service thẻ hội viên, tích hợp quét QR và logic bất biến. | Coder | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [NFR-005], [NFR-007], [NFR-008] |
| **Giai đoạn 4** | Ngày 8 - Ngày 9 | `./sources/infra.dockerfile`, `./sources/infra.gcp`, `./sources/docs.security` | Cập nhật Dockerfile đa giai đoạn, triển khai tài nguyên GCP (VPC, IAM, Cloud Storage) và ghi chép các quy tắc bảo mật. | Docker | [REQ-016], [REQ-017], [REQ-018], [DAT-008], [EXC-003], [NFR-006], [NFR-009] |
| **Giai đoạn 5** | Ngày 10 - Ngày 11 | `./sources/infra.k8s`, `./sources/frontend.web`, `./sources/frontend.mobile`, `./sources/backend.reporting` | Xây dựng manifest Kubernetes (GKE), phát triển UI web Next.js, gói ứng dụng di động Capacitor, triển khai service báo cáo và dashboard. | GKE | [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [EXC-005] |

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

<!--START_DELIMITTER-->
### Phase [1] Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng nền tảng người dùng cốt lõi, xác thực OAuth2 và cấu hình hệ thống ban đầu để hỗ trợ các vai trò RBAC.
- **Target Physical Directory Matrix Map:** `./sources/backend.users [REQ-001], [DAT-001]`; `./sources/backend.auth [REQ-002], [ARC-006]`; `./sources/infra.dockerfile [NFR-005]`; `./sources/infra.gcp [NFR-002]`; `./sources/docs.architecture [DOC]`.
- **Database Schema DDL SQL Specification [DAT-001], [DAT-011]:**
```sql
-- [DAT-001] Users & Roles
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

-- [DAT-011] SystemSettings
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [ARC-006]:**
  * `POST /api/v1/auth/register` – yêu cầu `{email, password, fullName}`; trả về `{token, userId}`.
  * `POST /api/v1/auth/social` – nhận `{provider, code}`; trao đổi mã lấy thông tin người dùng từ Firebase/Google/Facebook; tạo hoặc cập nhật người dùng và trả về JWT.
  * `GET /api/v1/auth/me` – xác thực qua Bearer token; trả về thông tin người dùng hiện tại.
- **Phase Localized Exception Handlers [EXC-004]:**
  * Xác thực đầu vào không hợp lệ (email sai định dạng, thiếu trường bắt buộc) trả về `400 Bad Request` với danh sách các trường lỗi chi tiết.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [1])
- **DAY 1: Xây dựng service người dùng cơ bản**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.users [REQ-001], [DAT-001]`
      - **Low-Level Technical Task Instruction:** Triển khai lớp resource `UserResource` với endpoint `POST /users` để xử lý đăng ký, thực hiện xác thực trường (email không trùng, mật khẩu >=8 ký tự), mã hóa mật khẩu bằng BCrypt, lưu vào bảng `USERS`, trả về JWT token. Áp dụng annotation `@Valid` và `@NotNull`. Ghi nhật ký hành động bằng OpenTelemetry.
      - **Targeted Tag IDs:** [REQ-001], [DAT-001]
- **DAY 2: Xây dựng service xác thực và tích hợp OAuth2**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.auth [REQ-002], [ARC-006]`
      - **Low-Level Technical Task Instruction:** Triển khai `AuthResource` với `POST /auth/social` nhận `{provider, code}`. Sử dụng FirebaseAuth, GoogleIdTokenVerifier, FacebookGraphClient để xác thực code, lấy thông tin người dùng. Tạo hoặc cập nhật bản ghi trong `USERS` dựa trên provider và email, gán role mặc định `Student`. Phát sinh sự kiện `UserAuthenticatedEvent` để ghi audit log. Đảm bảo xử lý lỗi cho provider không hỗ trợ.
      - **Targeted Tag IDs:** [REQ-002], [ARC-006]
- **DAY 3: Đánh giá chất lượng mã và kiểm tra bảo mật**
  - **Sub-Agent Workflow Specialization:**
    * **[Reviewer]:**
      - **Target Component file path (`target_component`):** `./sources/backend.users [REQ-001], [DAT-001]`
      - **Low-Level Technical Task Instruction:** Thực hiện đánh giá tĩnh bằng SonarQube, kiểm tra các vấn đề tiềm ẩn (SQL injection, lộ thông tin nhạy cảm). Chạy bộ kiểm tra tích hợp cho endpoint đăng ký (`POST /users`) và endpoint xác thực xã hội (`POST /auth/social`). Xác nhận rằng các quy tắc RBAC được áp dụng (roleId FK). Tạo báo cáo kiểm tra và ghi lại mọi phát hiện.
      - **Targeted Tag IDs:** [REQ-001], [DAT-001]

### Phase [2] Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai quản lý trung tâm, khóa học, ghi danh và các bảng khuyến mãi & thông báo để hỗ trợ hoạt động học tập đa trung tâm.
- **Target Physical Directory Matrix Map:** `./sources/backend.centers [REQ-004], [DAT-003]`; `./sources/backend.courses [REQ-007], [DAT-004]`; `./sources/backend.enrollments [REQ-010], [DAT-005]`; `./sources/backend.promotions [REQ-017], [DAT-009]`.
- **Database Schema DDL SQL Specification [DAT-003], [DAT-004], [DAT-005], [DAT-009]:**
```sql
-- [DAT-003] Centers
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(20) NOT NULL UNIQUE,
    contactPhone VARCHAR(30),
    contactEmail VARCHAR(255)
);

-- [DAT-004] Courses
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL REFERENCES USERS(userId),
    maxStudents INT NOT NULL DEFAULT 30
);

-- [DAT-005] Enrollments
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE(studentId, courseId)
);

-- [DAT-009] Promotions & Announcements
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
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-017], [REQ-018]:**
  * `GET /api/v1/centers` – trả về danh sách trung tâm.
  * `POST /api/v1/centers` – tạo trung tâm mới, kiểm tra trùng taxId.
  * `PUT /api/v1/centers/{id}` / `DELETE /api/v1/centers/{id}` – CRUD.
  * `POST /api/v1/centers/{centerId}/admin/{userId}` – gán người dùng làm Center Admin.
  * `GET /api/v1/courses` – danh sách khóa học với thông tin giáo viên.
  * `POST /api/v1/courses` – tạo khóa học, kiểm tra xung đột lịch dạy của giáo viên.
  * `PUT /api/v1/courses/{id}` / `DELETE /api/v1/courses/{id}` – CRUD.
  * `POST /api/v1/courses/{courseId}/teacher/{teacherId}` – gán giáo viên, tạo thông báo đẩy.
  * `GET /api/v1/enrollments` – danh sách ghi danh của học viên hiện tại.
  * `POST /api/v1/enrollments` – ghi danh vào khóa học, tự động tạo tài khoản học viên nếu thiếu.
  * `POST /api/v1/promotions` – tạo khuyến mãi mới.
  * `POST /api/v1/announcements` – tạo thông báo mới.

- **Phase Localized Exception Handlers:** Không có ngoại lệ chuyên biệt trong giai đoạn này.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [2])
- **DAY 4: Xây dựng service trung tâm**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.centers [REQ-004], [DAT-003]`
      - **Low-Level Technical Task Instruction:** Triển khai `CenterResource` với các endpoint CRUD cho `/centers`. Thêm kiểm tra ràng buộc duy nhất cho `taxId`. Sử dụng `@Transactional` để đảm bảo tính nguyên tử. Ghi nhật ký mọi thao tác thay đổi trung tâm vào bảng `AUDITLOG`. Đảm bảo role `System Admin` có quyền truy cập.
      - **Targeted Tag IDs:** [REQ-004], [DAT-003]
- **DAY 5: Xây dựng service khóa học và ghi danh**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.courses [REQ-007], [DAT-004]`
      - **Low-Level Technical Task Instruction:** Triển khai `CourseResource` với endpoint `POST /courses`. Thực hiện kiểm tra xung đột lịch dạy: truy vấn `COURSES` theo `teacherId` để đảm bảo không có ngày trùng. Sử dụng `java.time.LocalDate` để so sánh khoảng thời gian. Thêm validation cho `maxStudents`. Ghi nhật ký thao tác tạo khóa học.
      - **Targeted Tag IDs:** [REQ-007], [DAT-004]
- **DAY 6: Xây dựng service ghi danh và khuyến mãi**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.enrollments [REQ-010], [DAT-005]`
      - **Low-Level Technical Task Instruction:** Triển khai `EnrollmentResource` với endpoint `POST /enrollments`. Kiểm tra sự tồn tại của khóa học, capacity (`COUNT(*) < maxStudents`), và ghi danh duy nhất (`UNIQUE(studentId, courseId)`). Tự động tạo tài khoản người dùng với role `Student` nếu `studentId` chưa tồn tại. Phát sinh sự kiện `EnrollmentCompletedEvent` để kích hoạt thông báo đẩy và bài đăng Zalo.
      - **Targeted Tag IDs:** [REQ-010], [DAT-005]
- **DAY 7: Xây dựng service khuyến mãi & thông báo**
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** `./sources/backend.promotions [REQ-017], [DAT-009]`
      - **Low-Level Technical Task Instruction:** Soạn thảo tài liệu kỹ thuật cho API khuyến mãi (`POST /promotions`, `PUT /promotions/{id}`) bao gồm request/response schema, mã lỗi, ví dụ sử dụng. Đảm bảo tài liệu tham chiếu đến các Tag IDs `[REQ-017]`, `[DAT-009]`. Xuất tài liệu dưới dạng Markdown trong `./sources/docs.promotions`.
      - **Targeted Tag IDs:** [REQ-017], [DAT-009]

### Phase [3] Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng các chức năng điểm danh, thẻ hội viên và tích hợp quét QR để ghi nhận sự hiện diện một cách bất biến.
- **Target Physical Directory Matrix Map:** `./sources/backend.attendance [REQ-012], [DAT-006]`; `./sources/backend.membership [REQ-014], [DAT-007]`; `./sources/backend.qr [REQ-012], [EXC-001], [EXC-002]`.
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007]:**
```sql
-- [DAT-006] Attendance
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE(studentId, courseId, attendanceDate)
);

-- [DAT-007] StudentCards
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);
```
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015]:**
  * `POST /api/v1/attendance/scan` – nhận `{studentId, courseId, qrData}`; xác thực mối quan hệ, ghi vào `ATTENDANCE` với ngày hiện tại; trả về `{success, duplicate}`.
  * `GET /api/v1/membership/{studentId}/card` – trả về `StudentCards` với `remainingDays` đã tính toán.
  * `POST /api/v1/membership/{studentId}/renew` – nhận `{additionalDays}`; cập nhật `issueDate` và `remainingDays`; ghi nhận giao dịch thanh toán.

- **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
  * **EXC-001:** Nếu điểm danh QR được thực hiện khi ngoại tuyến, ứng dụng di động lưu sự kiện cục bộ; khi kết nối lại, service xử lý sự kiện chờ và ghi vào `ATTENDANCE` chỉ một lần.
  * **EXC-002:** Nếu cùng một học viên quét cùng một khóa học trong ngày, system trả về `200 OK` với cờ `duplicate:true` và không tạo bản ghi mới.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [3])
- **DAY 8: Xây dựng service điểm danh và logic bất biến**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.attendance [REQ-012], [DAT-006]`
      - **Low-Level Technical Task Instruction:** Triển khai `AttendanceResource` với endpoint `POST /attendance/scan`. Sử dụng `SELECT * FROM ATTENDANCE WHERE studentId=? AND courseId=? AND attendanceDate=CURRENT_DATE FOR UPDATE` để khóa hàng, đảm bảo chỉ một bản ghi được tạo. Nếu đã tồn tại, trả về `duplicate:true`. Ghi nhật ký mọi lần quét vào `AUDITLOG`. Áp dụng rate limiting theo studentId để ngăn lạm dụng.
      - **Targeted Tag IDs:** [REQ-012], [DAT-006]
- **DAY 9: Xây dựng service thẻ hội viên**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membership [REQ-014], [DAT-007]`
      - **Low-Level Technical Task Instruction:** Triển khai `MembershipResource` với endpoint `GET /membership/{studentId}/card` tính toán `remainingDays = issueDate + validityDays - CURRENT_DATE`. Endpoint `POST /membership/{studentId}/renew` cập nhật `issueDate = CURRENT_DATE`, `remainingDays = additionalDays`. Sử dụng `@Versioned` để tránh xung đột ghi. Ghi nhật ký mọi thay đổi thẻ.
      - **Targeted Tag IDs:** [REQ-014], [DAT-007]
- **DAY 10: Xây dựng module tích hợp quét QR**
  - **Sub-Agent Workflow Specialization:**
    * **[Docker]:**
      - **Target Component file path (`target_component`):** `./sources/infra.dockerfile [EXC-001], [EXC-002]`
      - **Low-Level Technical Task Instruction:** Cập nhật `Dockerfile` đa giai đoạn để bao gồm module quét QR mới (`qr-service.jar`). Thêm health-check endpoint `/actuator/health`. Xây dựng image `membership-hub/qr-service:1.0` và đẩy lên registry. Đảm bảo image size < 500MB (NFR-005).
      - **Targeted Tag IDs:** [EXC-001], [EXC-002]

### Phase [4] Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai service thông báo, cấu hình push notification và xử lý các trường hợp ngoại lệ khi gửi thông báo không thành công.
- **Target Physical Directory Matrix Map:** `./sources/infra.dockerfile [REQ-016]` (cập nhật), `./sources/infra.gcp [REQ-016], [NFR-009]` (tài nguyên cloud), `./sources/docs.security [EXC-003]`.
- **Database Schema DDL SQL Specification [DAT-008]:**
```sql
-- [DAT-008] Notifications
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID REFERENCES USERS(userId),
    groupZalo VARCHAR(100) REFERENCES ZALO_GROUPS(groupId),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
```
- **API and Event Routing Contracts [REQ-016], [REQ-017], [REQ-018]:**
  * `POST /api/v1/notifications` – tạo thông báo mới, đẩy vào hàng đợi FCM/APNs, ghi vào `NOTIFICATIONS`.
  * `POST /api/v1/promotions` / `POST /api/v1/announcements` – tạo khuyến mãi/thông báo, tự động kích hoạt endpoint thông báo.

- **Phase Localized Exception Handlers [EXC-003]:**
  * **EXC-003:** Nếu push notification thất bại (token không hợp lệ), system ghi lỗi vào `NOTIFICATIONS` với `delivered=false`, lên lịch lại tối đa 3 lần (exponential backoff). Sau 3 lần thất bại, đánh dấu `delivered=true` và ghi log cảnh báo.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [4])
- **DAY 11: Triển khai service thông báo**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.notifications [REQ-016], [DAT-008]`
      - **Low-Level Technical Task Instruction:** Triển khai `NotificationResource` với endpoint `POST /notifications`. Sử dụng `FcmClient` và `ApnsClient` để gửi push. Ghi nhận kết quả gửi vào `NOTIFICATIONS`. Thêm logic retry với `@Scheduled` (3 lần, cách nhau 5 phút). Ghi nhật ký mọi lần thất bại vào `AUDITLOG`.
      - **Targeted Tag IDs:** [REQ-016], [DAT-008]
- **DAY 12: Cấu hình hạ tầng GCP và ghi chép bảo mật**
  - **Sub-Agent Workflow Specialization:**
    * **[GCP]:**
      - **Target Component file path (`target_component`):** `./sources/infra.gcp [NFR-009]`
      - **Low-Level Technical Task Instruction:** Soạn Terraform/IaC để tạo `vpc`, `cloudsql-instance`, `redis-instance`, `secret-manager`. Thiết lập IAM cho `service-account` của backend. Kích hoạt API `Firebase`, `CloudMessaging`, `Zalo`. Ghi chép các cấu hình này vào `./sources/docs.security` với các tham chiếu Tag IDs.
      - **Targeted Tag IDs:** [NFR-009]

### Phase [5] Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai frontend web, ứng dụng di động hybrid, service báo cáo, triển khai GKE và hoàn thiện các yêu cầu đa ngôn ngữ, SEO, tuân thủ GDPR/CCPA.
- **Target Physical Directory Matrix Map:** `./sources/frontend.web [REQ-019], [REQ-022], [REQ-023]`; `./sources/frontend.mobile [REQ-020], [REQ-021]`; `./sources/backend.reporting [REQ-024], [REQ-025]`; `./sources/infra.k8s [ARC-010]`.
- **API and Event Routing Contracts [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-007], [ARC-008], [ARC-009], [ARC-010]:**
  * `GET /api/v1/reports/attendance` – tạo CSV báo cáo điểm danh cho trung tâm được chọn.
  * `GET /api/v1/dashboard/enrollment` – trả về JSON tóm tắt (`totalStudents`, `activeCourses`, `upcomingSessions`).
  * `GET /api/v1/i18n/{lang}` – trả về các chuỗi nội địa hóa.
  * `GET /api/v1/seo/{lang}` – trả về meta tags và hreflang links.
  * `POST /api/v1/chatbot/query` – nhận câu hỏi, trả về câu trả lời từ AI chatbot.

- **Phase Localized Exception Handlers [EXC-005]:**
  * **EXC-005:** Nếu service bị gián đoạn, khi khôi phục, system xử lý các bản ghi điểm danh chờ (`ATTENDANCE` với `sentAt IS NULL`) theo FIFO, sau đó gửi notification đến người dùng về các sự kiện đã được khôi phục.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [5])
- **DAY 13: Xây dựng UI web và nội địa hóa**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/frontend.web [REQ-019], [REQ-022], [REQ-023]`
      - **Low-Level Technical Task Instruction:** Triển khai các component React cho trang chủ, danh sách khóa học, trang cá nhân. Tích hợp `i18next` với các tệp tài nguyên cho `en`, `vi`, `es`. Thêm thẻ `<html lang='{{lang}}'>` và meta `hreflang`. Triển khai routing cho từng ngôn ngữ. Sử dụng `react-query` để xử lý trường hợp ngoại tuyến.
      - **Targeted Tag IDs:** [REQ-019], [REQ-022], [REQ-023]
- **DAY 14: Xây dựng ứng dụng di động hybrid**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/frontend.mobile [REQ-020], [REQ-021]`
      - **Low-Level Technical Task Instruction:** Sử dụng Capacitor để tạo ứng dụng di động iOS/Android. Triển khai các màn hình vai trò (Student, Teacher, Admin). Tích hợp FCM/APNs để nhận push notification. Thêm scanner QR native bằng `@capacitor/camera` và `@capacitor/geolocation`. Ghi nhật ký các tương tác người dùng vào `AUDITLOG`.
      - **Targeted Tag IDs:** [REQ-020], [REQ-021]
- **DAY 15: Xây dựng service báo cáo và dashboard**
  - **Sub-Agent Workflow Specialization:**
    * **[GKE]:**
      - **Target Component file path (`target_component`):** `./sources/infra.k8s [ARC-010]`
      - **Low-Level Technical Task Instruction:** Soạn manifest Kubernetes (`Deployment`, `Service`, `Ingress`, `ConfigMap`, `Secret`) cho backend, frontend, và reporting services. Cấu hình HPA dựa trên CPU > 70% hoặc latency > 300ms. Thiết lập `Ingress` với TLS cho các host đa ngôn ngữ. Triển khai lên GKE cluster.
      - **Targeted Tag IDs:** [ARC-010]
- **DAY 16: Triển khai CI/CD pipeline và hoàn thiện**
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** `./sources/docs.architecture [NFR-001], [NFR-002], [NFR-003], [NFR-004], [EXC-005]`
      - **Low-Level Technical Task Instruction:** Hoàn thiện tài liệu kiến trúc bao gồm các phần về hiệu năng, khả năng mở rộng, bảo mật, tuân thủ GDPR/CCPA, và quy trình phục hồi sau sự cố. Đảm bảo tất cả các Tag IDs được tham chiếu chính xác. Xuất tài liệu dưới dạng Markdown cuối cùng.
      - **Targeted Tag IDs:** [NFR-001], [NFR-002], [NFR-003], [NFR-004], [EXC-005]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng PreparedStatement/JPA Criteria API, whitelist các cột cho phép sắp xếp, áp dụng `@Pattern` cho các tham số đầu vào.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Sử dụng `jakarta.servlet.annotation.ServletSecurity` với `HttpConstraint` và `ContentSecurityPolicy`. Tự động thoát HTML trong các response `Jackson`.
- **Multi-Tenant CORS Security Rails:** Cấu hình `WebMvcConfigurer` để cho phép các origin động từ bảng `TENANT_ORigins` được lưu trữ trong `SystemSettings`.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Áp dụng `@JsonSerialize` với `SensitiveDataMasker`, xóa trường `passwordHash`, `email` trong `AUDITLOG` sau 30 ngày.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng `@capacitor/preferences` cho storage cục bộ, chặn sự kiện backbutton gốc, thực hiện fetch với `fetch` và fallback `localStorage`. Áp dụng TLS cho mọi request mạng.
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware `LocaleResolver` chọn ngôn ngữ từ cookie, header `Accept-Language`. Tạo `Hreflang` links tự động cho từng trang. Sử dụng `react-helmet` để chèn meta tags.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Mỗi ngày tạo branch `features/development-phase-{X}-day-{Y}` (`X` là số giai đoạn, `Y` là số ngày trong giai đoạn). Ví dụ: `features/development-phase-1-day-1`.
- **Validation Guard Pipeline Gates:** Sau mỗi commit, GitHub Actions chạy `mvn clean verify` (kiểm tra unit), `npm run test` (kiểm tra frontend), `docker build` và push. Yêu cầu độ phủ mã >= 85% cho mỗi module. Ghi nhật ký kết quả vào `build-reports/{phase}-{day}.json`.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]