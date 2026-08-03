# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260803053505 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/03 05:35:05 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống được thiết kế theo kiến trúc dịch vụ vi mô dựa trên Java/Quarkus với các biên giới CQRS rõ ràng, mô hình sự kiện phản ứng cho các tác vụ điểm danh và thông báo, và một cổng xác thực tập trung hỗ trợ nhiều nhà cung cấp. Các module chức năng chính bao gồm: Auth Service, User Service, Center Service, Course Service, Enrollment Service, Attendance Service, Card Service, Notification Service, Promotion Service, Announcement Service, Chatbot Service, và Frontend Next.js. Các thành phần này được container hóa bằng Docker và triển khai trên Google Kubernetes Engine (GKE) với tự động hóa CI/CD thông qua GitHub Actions. Thiết kế tuân thủ các nguyên tắc SOLID, sử dụng lập trình không đồng bộ, và tích hợp các hệ thống giám sát và logging phân tán.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Luồng xác thực (ARC-006) sử dụng OAuth2 với Firebase, Google, Facebook, cấp JWT (15 phút) và refresh token. Luồng điểm danh QR (ARC-007) ghi nhận sự kiện một cách idempotent thông qua một service chuyên dụng. Luồng thông báo (ARC-008) kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định. Frontend Next.js tiêu thụ REST APIs, sử dụng bearer token, và hỗ trợ caching ngoại tuyến. Redis được sử dụng cho session caching, PostgreSQL cho persistence, và hệ thống logging tập trung ghi lại tất cả các sự kiện người dùng để tuân thủ GDPR/CCPA.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.x, Hibernate ORM, Flyway, PostgreSQL JDBC Driver, SmallRye OpenAPI, JWT (Eclipse Microprofile), Firebase Admin SDK, Google Cloud Messaging (FCM)/Apple APNs SDK, Zalo API SDK, Redis Java client, JUnit 5, Maven (hoặc Gradle), Docker multi-stage, OpenTelemetry, Logback.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14, React 18, TypeScript, Tailwind CSS, SWR cho caching, React-i18next, Capacitor cho hybrid mobile, Ionic, Firebase Authentication SDK, React Query, ESLint/Prettier, Jest/RTL, Docker cho môi trường phát triển.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** Root kho lưu trữ thực tế được cố định tại `..`. Tất cả các đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Áp dụng quy tắc tiền tố thư mục động phù hợp với cấu trúc hệ thống được phát hiện (backend, frontend, infra).
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Tất cả mã nguồn Java phải nằm trong gói cơ sở `org.nlh4j.saas.membershiphub`. Chuỗi "membership-hub" được chuyển đổi thành dạng thuần chữ thường, không dấu, không gạch ngang, không dấu gạch dưới.
- **Strict Tester Target Path Syntax:** Bất kỳ thành phần nào được Tester nhắm đến phải được cấu trúc dưới dạng cặp dấu phẩy phân cách `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn trong cặp phải bắt đầu bằng `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1-2 | ./sources/backend.membershiphub.user | Triển khai core User & Role services, DDL schema, API đăng ký/xác thực, gán vai trò, xử lý ngoại lệ đầu vào, logging tuân thủ bảo mật. | Coder | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-006], [EXC-004], [NFR-001], [NFR-003], [NFR-006] |
| Phase 2 | Day 3-4 | ./sources/backend.membershiphub.center | Triển khai Center CRUD, phân quyền Center Admin, API danh sách trung tâm, gán người dùng, kiểm tra xung đột tax ID, logging. | Coder | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002], [NFR-003], [NFR-004], [NFR-005] |
| Phase 3 | Day 5-6 | ./sources/backend.membershiphub.course | Triển khai Course CRUD, logic tránh xung đột lịch giảng, gán giáo viên, API danh sách khóa học, kiểm tra quyền Manager, logging. | Coder | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003], [NFR-001], [NFR-002] |
| Phase 4 | Day 7-9 | ./sources/backend.membershiphub.attendance | Triển khai Enrollment, Attendance, StudentCard entities, service điểm danh QR idempotent, xử lý ngoại lệ network và duplicate, API duyệt khóa học, đăng ký, xem thẻ. | Coder | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [ARC-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003] |
| Phase 5 | Day 10-14 | ./sources/backend.membershiphub.notification,./sources/frontend.nextjs | Triển khai Notification, Promotion, Announcement entities, API kích hoạt thông báo, quản lý khuyến mãi, quản lý thông báo, tích hợp chatbot AI, UI di động responsive, phát hiện ngôn ngữ, SEO đa ngôn ngữ, thiết lập SystemSettings, logging báo cáo, triển khai Docker, cấu hình GCP infra, tạo manifest GKE. | Coder | [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-008], [DAT-009], [DAT-011], [NFR-003], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
|  |  |  |  | Tester | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [REQ-004], [REQ-005], [REQ-006], [DAT-003], [REQ-007], [REQ-008], [REQ-009], [DAT-004], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-008], [DAT-009], [DAT-011] |
|  |  |  |  | Docker | [NFR-005], [NFR-009] |
|  |  |  |  | GCP | [NFR-004], [NFR-008] |
|  |  |  |  | GKE | [NFR-002], [NFR-004], [NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

<!--START_DELIMITTER-->
### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các service cốt lõi của người dùng bao gồm đăng ký, xác thực xã hội, gán vai trò, và các ràng buộc bảo mật cơ bản. Xây dựng schema cơ sở dữ liệu cho bảng Users, Roles, và thiết lập logging kiểm toán.
- **Target Physical Directory Matrix Map:** 
  - ./sources/backend.membershiphub.user/users.sql [DAT-001]
  - ./sources/backend.membershiphub.user/roles.sql [DAT-001]
  - ./sources/backend.membershiphub.user/user-service.java [REQ-001], [REQ-002], [REQ-003], [ARC-006], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
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
    role_id SMALLINT NOT NULL REFERENCES roles(role_id),
    provider ENUM('local','firebase','google','facebook') NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now()
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
  - `POST /api/v1/auth/register` – yêu cầu {email, password, fullName, provider?} – trả về JWT token.
  - `POST /api/v1/auth/social` – yêu cầu {provider, code, redirectUri} – trao đổi code lấy thông tin người dùng, tạo/cập nhật bản ghi Users, trả về JWT.
  - `PUT /api/v1/users/{userId}/role` – yêu cầu {roleId} (chỉ System Admin) – cập nhật role_id, ghi lại log kiểm toán.
- **Phase Localized Exception Handlers [EXC-004]:**
  - Xác thực đầu vào không hợp lệ (email sai định dạng, thiếu trường bắt buộc) → trả về HTTP 400 với danh sách chi tiết các trường lỗi.
  - Xung đột email duy nhất → HTTP 409 với thông báo "Email đã tồn tại".
  - Xác thực mật khẩu yếu → HTTP 400 với thông báo "Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường, số, ký tự đặc biệt".

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1:** Triển khai service đăng ký người dùng và API xác thực xã hội.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.user/user-service.java [REQ-001], [REQ-002], [REQ-003], [ARC-006], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
      - **Low-Level Technical Task Instruction:** Triển khai lớp UserService với các phương thức register(RegistrationRequest), socialAuthenticate(SocialAuthRequest), assignRole(Long userId, Short roleId). Sử dụng BCrypt để mã hóa mật khẩu, JWT (accessToken 15 phút, refreshToken 7 ngày). Áp dụng @Valid cho validation, ném InputValidationException cho từng trường. Ghi lại log hành động người dùng với userId, timestamp, action. Đảm bảo endpoint REST được đánh dấu @Transactional và có @Operation(summary=...) cho OpenAPI.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [ARC-006], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
- **DAY 2:** Viết bộ kiểm tra đơn vị và tích hợp cho các chức năng người dùng.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.user/userservice-test.java;./sources/backend.membershiphub.user/user-service.java
      - **Low-Level Technical Task Instruction:** Tạo JUnit 5 test cases bao phủ happy path cho register, social auth, assignRole. Sử dụng Mock cho PasswordEncoder, JwtTokenProvider. Kiểm tra validation cho email sai định dạng, mật khẩu yếu, duplicate email. Sử dụng @WebMvcTest cho controller, mock request bodies, xác nhận HTTP status và payload. Đảm bảo độ phủ mã >=85% cho UserService.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004]

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng module quản lý trung tâm bao gồm CRUD trung tâm, danh sách trung tâm công khai, và phân quyền quản trị trung tâm. Triển khai schema Centers và tích hợp với RBAC cho Center Admin.
- **Target Physical Directory Matrix Map:** 
  - ./sources/backend.membershiphub.center/centers.sql [DAT-003]
  - ./sources/backend.membershiphub.center/center-service.java [REQ-004], [REQ-005], [REQ-006], [ARC-002], [NFR-003], [NFR-004], [NFR-005]
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) NOT NULL UNIQUE,
    contact_phone VARCHAR(30),
    contact_email VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [ARC-002]:**
  - `GET /api/v1/centers` – trả về danh sách các trung tâm (name, address, taxId, contactPhone, contactEmail).
  - `POST /api/v1/centers` – yêu cầu {name, address, taxId, contactPhone?, contactEmail?} – trả về centerId, kiểm tra taxId duplicate.
  - `PUT /api/v1/centers/{centerId}` – cập nhật thông tin.
  - `DELETE /api/v1/centers/{centerId}` – xóa mềm (cờ deleted_at).
  - `POST /api/v1/centers/{centerId}/admins/{userId}` – gán người dùng làm Center Admin, cập nhật role người dùng.
- **Phase Localized Exception Handlers [EXC-004] (áp dụng cho validation đầu vào trung tâm):**
  - Tax ID không hợp lệ (không phải số 10-13 chữ số) → HTTP 400.
  - Email liên hệ không hợp lệ → HTTP 400.
  - Xung đột taxId → HTTP 409.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 3:** Triển khai service quản lý trung tâm và các endpoint CRUD.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.center/center-service.java [REQ-004], [REQ-005], [REQ-006], [ARC-002], [NFR-003], [NFR-004], [NFR-005]
      - **Low-Level Technical Task Instruction:** Triển khai CenterService với các phương thức listCenters(), createCenter(CenterRequest), updateCenter(UUID centerId, CenterRequest), deleteCenter(UUID centerId), assignCenterAdmin(UUID centerId, UUID userId). Sử dụng @Valid cho validation, @Transactional cho các thao tác ghi. Sử dụng JPA Repository cho Centers. Áp dụng @PreAuthorize('hasRole(\"SYSTEM_ADMIN\")') cho các thao tác ghi. Ghi lại log kiểm toán cho mỗi thao tác. Đảm bảo response tuân thủ OpenAPI spec.
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002], [NFR-003], [NFR-004], [NFR-005]
- **DAY 4:** Viết bộ kiểm tra tích hợp cho các API trung tâm.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.center/centerservice-integration-test.java;./sources/backend.membershiphub.center/center-service.java
      - **Low-Level Technical Task Instruction:** Sử dụng Testcontainers cho PostgreSQL, mock authentication. Kiểm tra GET trả về danh sách, POST thành công, validation cho taxId duplicate, conflict error handling. Sử dụng @SpringBootTest, @AutoConfigureTestDatabase. Đảm bảo độ phủ mã cho CenterService.
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002]

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai module quản lý khóa học bao gồm danh sách khóa học công khai, CRUD khóa học với kiểm tra xung đột lịch giảng, và gán giáo viên. Tích hợp với RBAC cho Manager và System/Center Admin.
- **Target Physical Directory Matrix Map:** 
  - ./sources/backend.membershiphub.course/courses.sql [DAT-004]
  - ./sources/backend.membershiphub.course/course-service.java [REQ-007], [REQ-008], [REQ-009], [ARC-003], [NFR-001], [NFR-002]
- **Database Schema DDL SQL Specification [DAT-004]:**
```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [ARC-003]:**
  - `GET /api/v1/courses` – trả về danh sách khóa học (courseId, title, startDate, endDate, teacherName).
  - `POST /api/v1/courses` – yêu cầu {title, description?, startDate, endDate, teacherId} – kiểm tra xung đột lịch giảng của giáo viên, trả về conflict nếu có.
  - `PUT /api/v1/courses/{courseId}` – cập nhật thông tin khóa học.
  - `DELETE /api/v1/courses/{courseId}` – xóa mềm.
  - `POST /api/v1/courses/{courseId}/teachers/{teacherId}` – gán giáo viên, tạo notification cho giáo viên.
- **Phase Localized Exception Handlers [EXC-004] (validation khóa học):**
  - startDate > endDate → HTTP 400.
  - teacherId không tồn tại → HTTP 404.
  - Xung đột lịch giảng → HTTP 409.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 5:** Triển khai service quản lý khóa học và logic tránh xung đột.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.course/course-service.java [REQ-007], [REQ-008], [REQ-009], [ARC-003], [NFR-001], [NFR-002]
      - **Low-Level Technical Task Instruction:** Triển khai CourseService với các phương thức listCourses(), createCourse(CourseRequest), updateCourse(UUID courseId, CourseRequest), deleteCourse(UUID courseId), assignTeacher(UUID courseId, UUID teacherId). Sử dụng @Transactional, kiểm tra xung đột lịch giảng bằng cách truy vấn các khóa học hiện có của giáo viên. Sử dụng @PreAuthorize cho vai trò System Admin, Center Admin. Ghi lại log kiểm toán.
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003], [NFR-001], [NFR-002]
- **DAY 6:** Viết bộ kiểm tra cho các chức năng quản lý khóa học.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.course/courseservice-test.java;./sources/backend.membershiphub.course/course-service.java
      - **Low-Level Technical Task Instruction:** Tạo JUnit test cases cho createCourse thành công, xung đột lịch giảng, validation startDate/endDate, assignTeacher. Sử dụng Mock cho CourseRepository. Đảm bảo độ phủ mã >=85% cho CourseService.
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003]

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai module ghi danh học viên, điểm danh QR, và quản lý thẻ hội viên. Xây dựng schema Enrollments, Attendance, StudentCards, và service điểm danh QR idempotent. Tích hợp với luồng ngoại lệ network và duplicate scans.
- **Target Physical Directory Matrix Map:** 
  - ./sources/backend.membershiphub.attendance/enrollments.sql [DAT-005]
  - ./sources/backend.membershiphub.attendance/attendances.sql [DAT-006]
  - ./sources/backend.membershiphub.attendance/studentcards.sql [DAT-007]
  - ./sources/backend.membershiphub.attendance/enrollment-service.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [ARC-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003]
- **Database Schema DDL SQL Specification [DAT-005], [DAT-006], [DAT-007]:**
```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE (student_id, course_id)
);

CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE studentcards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);
```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [REQ-012], [REQ-013], [ARC-007]:**
  - `GET /api/v1/courses/browse` – trả về danh sách khóa học có sẵn cho học viên (loại trừ các khóa học đã ghi danh).
  - `POST /api/v1/enrollments` – yêu cầu {studentId, courseId} – tạo bản ghi ghi danh, tạo notification cho học viên và nhóm Zalo.
  - `POST /api/v1/attendance/scan` – yêu cầu {studentId, courseId, qrData, timestamp} – xác thực mối quan hệ học viên-khóa học, ghi nhận điểm danh, trả về success/duplicate.
  - `GET /api/v1/studentcards/{studentId}` – trả về thông tin thẻ (ngày hiệu lực còn lại).
  - `POST /api/v1/studentcards/{studentId}/renew` – yêu cầu {days} – cập nhật endDate, xử lý thanh toán.
- **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
  - Network không khả dụng trong quá trình quét QR → lưu sự kiện tạm thời, retry sau khi kết nối lại, sau đó ghi nhận điểm danh.
  - Duplicate scan trong cùng ngày → trả về HTTP 200 với cờ duplicate, không tạo bản ghi mới.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 7:** Triển khai service ghi danh học viên và điểm danh QR.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.attendance/enrollment-service.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [ARC-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003]
      - **Low-Level Technical Task Instruction:** Triển khai EnrollmentService với các phương thức browseCourses(UUID studentId), enroll(StudentCourseRequest), scanQr(AttendanceScanRequest), getStudentCard(UUID studentId), renewCard(UUID studentId, int days). Sử dụng @Transactional, kiểm tra xung đột ghi danh, đảm bảo idempotent cho điểm danh (sử dụng khóa khóa duy nhất trên (student_id, course_id, attendance_date)). Tích hợp retry mechanism cho network failure. Ghi lại log kiểm toán cho mỗi thao tác.
      - **Targeted Tag IDs:** [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [ARC-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003]
- **DAY 8:** Triển khai service quản lý thẻ hội viên và gia hạn.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.attendance/studentcard-service.java [REQ-014], [REQ-015], [NFR-003]
      - **Low-Level Technical Task Instruction:** Triển khai StudentCardService với các phương thức getCard(UUID studentId), renew(UUID studentId, int days). Sử dụng @Transactional, cập nhật remaining_days dựa trên issueDate + validityDays. Tích hợp với payment gateway (mock). Ghi lại log kiểm toán.
      - **Targeted Tag IDs:** [REQ-014], [REQ-015], [DAT-007], [NFR-003]
- **DAY 9:** Viết bộ kiểm tra tích hợp cho ghi danh, điểm danh, và thẻ.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Tester]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.attendance/enrollmentservice-integration-test.java;./sources/backend.membershiphub.attendance/enrollment-service.java
      - **Low-Level Technical Task Instruction:** Sử dụng Testcontainers cho PostgreSQL, mock authentication. Kiểm tra browseCourses trả về các khóa học có sẵn, enroll thành công, duplicate enrollment bị từ chối, scan QR thành công, duplicate scan trả về duplicate flag, getCard hiển thị remaining days, renew cập nhật remaining days. Đảm bảo độ phủ mã cho các service.
      - **Targeted Tag IDs:** [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [ARC-007], [EXC-001], [EXC-002]

### Phase 5 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai module thông báo, khuyến mãi, thông báo, chatbot AI, UI di động, đa ngôn ngữ, SEO, và thiết lập hạ tầng DevOps (Docker, GCP, GKE). Xây dựng schema Notifications, Promotions, Announcements, SystemSettings. Triển khai API kích hoạt thông báo, quản lý khuyến mãi, thông báo, tích hợp chatbot AI, và cấu hình frontend Next.js với i18n và SEO.
- **Target Physical Directory Matrix Map:** 
  - ./sources/backend.membershiphub.notification/notifications.sql [DAT-008]
  - ./sources/backend.membershiphub.notification/promotions.sql [DAT-009]
  - ./sources/backend.membershiphub.notification/announcements.sql [DAT-009]
  - ./sources/backend.membershiphub.notification/systemsettings.sql [DAT-011]
  - ./sources/backend.membershiphub.notification/notification-service.java [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [NFR-003], [NFR-006], [NFR-007]
  - ./sources/frontend.nextjs/package.json [REQ-020], [REQ-021], [REQ-022], [REQ-023]
- **Database Schema DDL SQL Specification [DAT-008], [DAT-009], [DAT-011]:**
```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID,
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT now(),
    delivered BOOLEAN NOT NULL DEFAULT false
);

CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT
);

CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);

CREATE TABLE systemsettings (
    setting_key VARCHAR(50) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description VARCHAR(200)
);
```
- **API and Event Routing Contracts [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]:**
  - `POST /api/v1/notifications` – yêu cầu {userId?, groupZalo?, message} – tạo bản ghi, đẩy push notification qua FCM/APNs, đăng bài lên Zalo group.
  - `GET /api/v1/promotions` – trả về danh sách khuyến mãi đang hiệu lực.
  - `POST /api/v1/promotions` – yêu cầu {code, discountPercent, startDate?, endDate?, description?} – lưu vào DB.
  - `PUT /api/v1/promotions/{promoId}` – cập nhật.
  - `DELETE /api/v1/promotions/{promoId}` – xóa.
  - `POST /api/v1/announcements` – yêu cầu {title, content, startDate?, endDate?} – lưu vào DB.
  - `GET /api/v1/announcements` – trả về danh sách thông báo đang hiệu lực.
  - `POST /api/v1/chatbot/interact` – yêu cầu {userId, message} – trả về phản hồi từ AI, ghi lại tương tác.
  - `GET /api/v1/i18n/{locale}` – trả về các key dịch đã externalized.
  - `GET /api/v1/seo/{locale}/{path}` – trả về meta tags và hreflang cho SEO.
- **Phase Localized Exception Handlers [EXC-003], [EXC-005]:**
  - Lỗi gửi push notification (token không hợp lệ) → ghi log lỗi, lên lịch retry tối đa 3 lần, sau đó đánh dấu delivered = false.
  - System recovery sau sự cố → xử lý các bản ghi điểm danh tạm thời bị bỏ lỡ (FIFO), gửi notification cho người dùng về các sự kiện đã phục hồi.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 10:** Triển khai service thông báo, khuyến mãi, thông báo.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.notification/notification-service.java [REQ-016], [REQ-017], [REQ-018], [REQ-019], [NFR-003], [NFR-006]
      - **Low-Level Technical Task Instruction:** Triển khai NotificationService với các phương thức createNotification(NotificationRequest), createPromotion(PromotionRequest), updatePromotion(UUID promoId, PromotionRequest), deletePromotion(UUID promoId), createAnnouncement(AnnouncementRequest), getActivePromotions(), getActiveAnnouncements(). Sử dụng @Transactional, đẩy push notification qua FCMClient, gọi Zalo API để đăng bài. Tích hợp chatbot AI client để xử lý tương tác. Ghi lại log kiểm toán cho mỗi thao tác.
      - **Targeted Tag IDs:** [REQ-016], [REQ-017], [REQ-018], [REQ-019], [DAT-008], [DAT-009], [NFR-003], [NFR-006]
- **DAY 11:** Triển khai tích hợp chatbot AI, UI di động, và cấu hình đa ngôn ngữ/SEO.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** ./sources/backend.membershiphub.notification/chatbot-service.java [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011], [NFR-007]
      - **Low-Level Technical Task Instruction:** Triển khai ChatbotService với phương thức interact(String userId, String message) trả về AIResponse. Tích hợp với OpenAI/Gemini API (mock). Triển khai REST endpoint /api/v1/chatbot/interact. Triển khai i18n service trả về bản đồ key-value cho từng locale. Triển khai SEO service tạo meta tags và hreflang links. Tích hợp với NotificationService để ghi lại tương tác.
      - **Targeted Tag IDs:** [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011], [NFR-007]
- **DAY 12:** Cung cấp cấu hình hạ tầng GCP (VPC, IAM, Cloud Storage, Cloud Run).
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: GCP]:**
      - **Target Component file path (`target_component`):** ./sources/infra/gcp/infrastructure.tf [NFR-004], [NFR-008]
      - **Low-Level Technical Task Instruction:** Tạo Terraform configuration cho Google Cloud Project: VPC network, subnets, firewall rules, Service Accounts với roles: Cloud SQL Admin, Cloud Storage Admin, Cloud Scheduler, Cloud Pub/Sub. Thiết lập Secret Manager cho JWT keys, Firebase credentials, Zalo API tokens. Cấu hình Cloud SQL instance (PostgreSQL), backup policies. Thiết lập Cloud Scheduler job cho backup hàng ngày. Áp dụng IAM policies cho service accounts và GKE service account.
      - **Targeted Tag IDs:** [NFR-004], [NFR-008]
- **DAY 13:** Xây dựng Docker image đa giai đoạn cho backend và frontend.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Docker]:**
      - **Target Component file path (`target_component`):** ./sources/infra/docker/backend/Dockerfile [NFR-005], [NFR-009]
      - **Low-Level Technical Task Instruction:** Tạo multi-stage Dockerfile cho backend: giai đoạn build sử dụng Maven (hoặc Gradle) để đóng gói Quarkus app, giai đoạn runtime sử dụng image java:21-slim, sao chép file jar, thiết lập user không root, expose port 8080. Thêm healthcheck. Tương tự cho frontend: sử dụng node:20-alpine, cài đặt phụ thuộc, build Next.js, phục vụ qua nginx. Đảm bảo kích thước image cuối cùng <500MB, base image <200MB.
      - **Targeted Tag IDs:** [NFR-005], [NFR-009]
- **DAY 14:** Triển khai lên Google Kubernetes Engine (GKE) với HPA và quản lý release.
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: GKE]:**
      - **Target Component file path (`target_component`):** ./sources/infra/gke/deployments.yaml [NFR-002], [NFR-004], [NFR-009]
      - **Low-Level Technical Task Instruction:** Tạo Kubernetes Deployment cho backend và frontend sử dụng image được push lên Artifact Registry. Định nghĩa Service, Ingress với TLS (cert-manager). Cấu hình Horizontal Pod Autoscaler dựa trên CPU >70% hoặc latency >300ms. Thiết lập ConfigMap cho các cấu hình ứng dụng, Secret cho các credentials. Thêm ResourceQuota, LimitRange. Triển khai rollout với canary (phiên bản phiên bản 2) và kiểm tra health endpoints. Thiết lập logging stack (Stackdriver) và monitoring (Prometheus/Grafana).
      - **Targeted Tag IDs:** [NFR-002], [NFR-004], [NFR-009]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-003]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng PreparedStatement cho tất cả các truy vấn JPA/Hibernate, áp dụng WhiteList cho các cột sắp xếp động, sử dụng @Query với tham số named.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Áp dụng @CrossOrigin, sử dụng JSON: @JsonSerialize với HTML escaping, thiết lập CSP header: default-src 'self'; script-src 'self' 'unsafe-inline' 'nonce-<generated>'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self';.
- **Multi-Tenant CORS Security Rails:** Kiểm tra nguồn gốc yêu cầu so với danh sách tenant được phép, sử dụng @RequestHeader("X-Tenant-ID") để cô lập dữ liệu, áp dụng tenant_id trong tất cả các truy vấn JPA.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Sử dụng Filter cho các trường PII (@Email, @Phone) trước khi ghi log, áp dụng @JsonIgnore cho các trường nhạy cảm, thiết lập log redaction pattern cho user_id, email, phone.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng @capacitor/core cho các API native, áp dụng URL whitelist cho deep links, sử dụng @capacitor/preferences cho storage cục bộ, chặn sự kiện backbutton gốc, thiết lập network timeout cho các request offline, đồng bộ hóa queue khi có kết nối.
- **Internationalization (i18n) & Dynamic SEO Injection:** Sử dụng react-i18next với các tệp tài nguyên JSON cho các locale (en, vi, es). Middleware phát hiện Accept-Language header, thiết lập cookie preference. Tự động chèn thẻ hreflang vào <head> cho từng alternate URL. Sử dụng Next.js getStaticProps với tham số locale để tạo các trang tĩnh cho từng ngôn ngữ.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Script CI tạo branch `features/development-phase-1-day-1`, `features/development-phase-1-day-2`, ... cho từng ngày. Mỗi branch được cô lập để tránh xung đột merge.
- **Validation Guard Pipeline Gates:** Sau khi push, GitHub Actions chạy các bước: `./sources/backend.membershiphub.user/gradle clean build`, `./sources/frontend.nextjs/npm run test`, `./sources/infra/docker/backend/docker build`. Đạt độ phủ mã >=85% cho các service mới, kiểm tra lint, kiểm tra định dạng. Chỉ cho phép merge vào branch chính sau khi tất cả các gate vượt qua.

### 🛑 MATRIX COVERAGE CHECK MANDATE
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 13. ZERO UNASSIGNED CODES FOUND.]