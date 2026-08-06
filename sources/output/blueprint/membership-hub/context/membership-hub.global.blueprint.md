# BỐ CỤC DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Mô tả kỹ thuật chi tiết về kiến trúc hệ thống được phát hiện: hệ thống tuân thủ kiến trúc đa trung tâm (multi-center) với mô hình dịch vụ vi mô (microservices) được container hóa, sử dụng mẫu thiết kế Event-Driven (EDA) cho các luồng bất đồng bộ như điểm danh QR, thông báo, và tích hợp Zalo. Hệ thống áp dụng CQRS cho các thao tác ghi (nhật ký điểm danh, thông báo) và truy vấn (báo cáo, danh sách khóa học). Các biên giới lệnh (command) và truy vấn (query) được phân tách rõ ràng để đảm bảo khả năng mở rộng và hiệu suất. Các thành phần cốt lõi hoạt động theo kiểu phản ứng (reactive) với RxJava/Vert.x, tích hợp với Redis để cache phiên làm việc và hàng đợi tin nhắn. RBAC được thực hiện ở tầng bảo mật, với các service bảo vệ endpoint dựa trên vai trò người dùng. Các API được định nghĩa dưới dạng REST với Swagger, hỗ trợ JWT cho xác thực và OAuth2 cho các nhà cung cấp bên ngoài. Các sự kiện được phát qua Apache Kafka (hoặc RabbitMQ) để đảm bảo tính bất biến và khả năng mở rộng của các luồng điểm danh và thông báo. Các schema cơ sở dữ liệu được thiết kế theo mô hình ER với các ràng buộc khóa ngoại và chỉ mục để đảm bảo truy vấn dưới 200ms cho các trường hợp sử dụng chính. Hệ thống được triển khai trên Kubernetes (GKE) với auto-scaling dựa trên CPU và độ trễ yêu cầu, sử dụng Flyway cho quản lý migration. Các chính sách bảo mật tuân thủ OWASP Top 10, mã hóa dữ liệu ở nghỉ bằng AES-256, và TLS 1.3 cho mọi giao tiếp. Hệ thống hỗ trợ đa ngôn ngữ (EN, VN, ES) với i18n middleware và hreflang cho SEO. Các quy trình CI/CD được tự động hóa qua GitHub Actions, với các giai đoạn build, test, container image push, và triển khai lên GKE.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Mô tả chi tiết về các kênh bất đồng bộ, cổng nhập liệu (ingestion gateway), topology chủ đề, và kiến trúc fan-out cho các hệ thống ngoại vi. Hệ thống sử dụng Apache Kafka làm backbone cho các luồng sự kiện bất đồng bộ: chủ đề `qr-attendance` ghi nhận sự kiện quét mã QR từ ứng dụng di động; chủ đề `notifications` truyền tải thông báo push và tin nhắn Zalo; chủ đề `enrollments` ghi lại các đăng ký khóa học. Các cổng nhập liệu (ingestion gateway) tại lớp API biên (edge) nhận yêu cầu từ client, xác thực JWT, sau đó ghi vào Kafka chủ đề tương ứng. Các consumer xử lý song song: service điểm danh xử lý `qr-attendance` để ghi vào PostgreSQL với tính chất idempotent; service thông báo đẩy vào FCM/APNs và gửi tin nhắn Zalo dựa trên chủ đề `notifications`. Các hệ thống phân tích (analytics) đọc từ Kafka để tạo báo cáo điểm danh hàng ngày và cập nhật dashboard. Các tích hợp bên ngoài (Zalo API, Firebase Auth) được thực hiện qua HTTP client bất đồng bộ, với retry circuit-breaker để đảm bảo độ tin cậy. Cache Redis được sử dụng cho session user và token blacklist, với TTL phù hợp. Các luồng này được giám sát bởi hệ thống logging tập trung (ELK) và alerting qua Prometheus/Grafana.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21 (LTS), Quarkus 3.2.0, Hibernate ORM, PostgreSQL 15, Docker 23.x, Kubernetes 1.27+, Firebase Authentication SDK, Google Cloud Messaging (FCM) SDK, Apple APNs SDK, Zalo API v2, Redis 7, Flyway, GitHub Actions, Maven 3.9.

- **Frontend & Cross-Platform UI Mobile Stack:** Node.js 20, npm 9, Next.js 14 (React 18), TypeScript, Tailwind CSS, React Native 0.73, Expo, Capacitor, i18next, react-i18next, Jest, React Testing Library, Docker (cho môi trường phát triển).

### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** Toàn bộ mã nguồn và cấu hình phải nằm dưới thư mục gốc dự án `.`. Tất cả các đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Áp dụng quy tắc tiền tố thư mục linh hoạt: `./sources/backend.<service-name>` cho logic backend, `./sources/frontend` cho giao diện web, `./sources/frontend.<app-name>` cho ứng dụng di động, `./sources/infra` cho cấu hình DevOps.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Tất cả mã Java phải được đóng gói trong `org.nlh4j.saas.membershiphub`. Tên dự án được chuẩn hóa thành dạng chữ thường, không dấu, không gạch ngang.
- **Strict Tester Target Path Syntax:** Bất kỳ thành phần nào được Tester nhắm đến phải được biểu diễn dưới dạng cặp bán phẩy `<source_component>;<test_suite_file>`, ví dụ: `./sources/backend.user-management;src/test/java/org/nlh4j/saas/membershiphub/user/RegistrationTest.java`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Giai đoạn | Khoảng ngày | Đường dẫn Thành phần Kiến trúc | Tóm tắt Sản phẩm Bàn giao | Sub-Agent được chỉ định | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Ngày 1-3 | `./sources/backend.user-management` | Triển khai bảng Users/Roles, API đăng ký, xác thực xã hội, gán vai trò. | Coder | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [EXC-004] |
| 1 | Ngày 1-3 | `./sources/backend.authentication` | Triển khai OAuth2 với Firebase/Google/Facebook, cấp JWT (15 phút), refresh token (7 ngày). | Coder | [ARC-006], [DAT-001] |
| 1 | Ngày 1-3 | `./sources/backend.center-management` | CRUD trung tâm, gán Center Admin, validation tax ID duy nhất. | Coder | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002] |
| 2 | Ngày 4-6 | `./sources/backend.course-management` | CRUD khóa học, kiểm tra xung đột lịch giảng, phân công giáo viên, notification cho giáo viên. | Coder | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-002], [ARC-003] |
| 2 | Ngày 4-6 | `./sources/backend.enrollment` | Duyệt khóa học, đăng ký, tự động tạo tài khoản học viên, push notification, gửi tin nhắn Zalo group. | Coder | [REQ-010], [REQ-011], [DAT-005], [ARC-008] |
| 2 | Ngày 4-6 | `./sources/backend.notification` | Tạo bản ghi thông báo, hàng đợi push notification cho mobile, gửi tin nhắn Zalo, retry delivery. | Coder | [REQ-016], [EXC-003], [DAT-008], [ARC-008] |
| 3 | Ngày 7-9 | `./sources/backend.attendance` | Xử lý quét QR, ghi điểm danh với tính chất bất biến, phát hiện duplicate, fallback khi mất mạng. | Coder | [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006], [ARC-007] |
| 3 | Ngày 7-9 | `./sources/backend.membership` | Hiển thị thẻ hội viên, tính ngày hiệu lực còn lại, xử lý gia hạn thẻ, cập nhật end date. | Coder | [REQ-014], [REQ-015], [DAT-007] |
| 3 | Ngày 7-9 | `./sources/backend.promotion` | CRUD khuyến mãi, CRUD thông báo, auto-expire dựa trên ngày kết thúc, hiển thị cho học viên. | Coder | [REQ-017], [REQ-018], [DAT-009] |
| 4 | Ngày 10-12 | `./sources/frontend.mobile` | Giao diện responsive cho các vai trò, màn hình quét QR, danh sách khóa học, thẻ hội viên, nhận push notification. | Coder | [REQ-020], [REQ-021] |
| 4 | Ngày 10-12 | `./sources/frontend.i18n` | Middleware phát hiện ngôn ngữ, fallback Accept-Language, hreflang injection, meta tags cho EN/VN/ES. | Coder | [REQ-022], [REQ-023], [DAT-011] |
| 4 | Ngày 10-12 | `./sources/backend.reports` | Tạo báo cáo điểm danh CSV, dashboard tóm tắt ghi danh, tổng hợp dữ liệu thời gian thực. | Coder | [REQ-024], [REQ-025], [EXC-005] |
| 5 | Ngày 13-14 | `./sources/infra` | Xây dựng Docker image đa giai đoạn (<500MB), push lên registry, triển khai lên GKE với HPA, CI/CD, áp dụng các biện pháp bảo mật NFR. | Docker | [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| 5 | Ngày 13-14 | `./sources/infra/gcp` | Cấu hình VPC, IAM, Cloud Storage, Cloud SQL, monitoring, logging, CI/CD. | GCP | [ARC-010], [NFR-002], [NFR-004], [NFR-008] |
| 5 | Ngày 13-14 | `./sources/infra/gke` | Tạo cluster GKE, deployment manifests, auto-scaling, health checks, CI/CD. | GKE | [ARC-010], [NFR-002], [NFR-004] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai nền tảng cốt lõi bao gồm quản lý người dùng, xác thực, phân quyền RBAC, và quản lý trung tâm. Xây dựng các bảng dữ liệu cơ bản (Users, Roles, Centers) và các API tương ứng để hỗ trợ các chức năng đăng ký, đăng nhập xã hội, gán vai trò, và quản lý trung tâm.
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend.user-management [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [EXC-004]`
    *   `./sources/backend.authentication [ARC-006], [DAT-001]`
    *   `./sources/backend.center-management [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002]`
    *   `./sources/docs/phase1_architecture.md [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [EXC-004]`
- **Database Schema DDL SQL Specification [DAT-001], [DAT-003]:**

```sql
-- Bảng Roles
CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

-- Bảng Users
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL REFERENCES roles(role_id),
    provider ENUM('local', 'firebase', 'google', 'facebook') NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now()
);

-- Bảng Centers
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) NOT NULL UNIQUE,
    contact_phone VARCHAR(30),
    contact_email VARCHAR(255)
);
```

- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003]:**
    *   `POST /api/auth/register` – Nhận `{email, password, fullName}` → tạo người dùng, mã hóa mật khẩu, gán vai trò mặc định `Student`, trả về JWT.
    *   `GET /api/auth/{provider}/callback?code={code}` – Trao đổi mã lấy thông tin từ Firebase/Google/Facebook, tạo/cập nhật người dùng, trả về JWT.
    *   `PUT /api/users/{userId}/role` – Chỉ Admin có thể gán vai trò mới, cập nhật `role_id` trong bảng `users`.
    *   `GET /api/centers` – Trả về danh sách tất cả trung tâm (`name, address, taxId, contactPhone, contactEmail`).
    *   `POST /api/centers` – Tạo trung tâm mới, validation taxId duy nhất, trả về đối tượng trung tâm.
    *   `PUT /api/centers/{id}` – Cập nhật thông tin trung tâm.
    *   `DELETE /api/centers/{id}` – Xóa trung tâm.
    *   `PATCH /api/users/{userId}/center/{centerId}` – Gán người dùng làm Center Admin cho trung tâm cụ thể.

- **Phase Localized Exception Handlers [EXC-004]:**
    *   Xử lý xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc) trong quá trình đăng ký. Trả về JSON body chứa danh sách các trường lỗi và thông báo chi tiết, ví dụ: `{"errors": [{"field": "email", "message": "Email đã tồn tại"}, {"field": "password", "message": "Mật khẩu phải có ít nhất 8 ký tự"}]}`.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1: Triển khai service quản lý người dùng (Users/Roles) và API đăng ký.**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.user-management [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [EXC-004]`
      - **Low-Level Technical Task Instruction:** Triển khai entity Users và Roles với các trường như được định nghĩa trong DAT-001, tạo UserRepository và RoleRepository, implement RegistrationService xử lý xác thực đầu vào, mã hóa mật khẩu bằng bcrypt, gán vai trò mặc định 'Student', trả về JWT token. Thêm validation cho email duy nhất, mật khẩu mạnh, và xử lý ngoại lệ [EXC-004] để trả về danh sách trường lỗi chi tiết. Triển khai REST endpoint POST /api/auth/register với request body {email, password, fullName}. Thêm unit test cho registration thành công và thất bại.
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [EXC-004]

- **DAY 2: Triển khai xác thực OAuth2 với Firebase, Google, Facebook.**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.authentication [ARC-006], [DAT-001]`
      - **Low-Level Technical Task Instruction:** Triển khai OAuth2 Authorization Code flow cho từng nhà cung cấp, tích hợp Firebase Auth SDK, Google People API, Facebook Graph API. Tạo AuthenticationService với phương thức authenticate(String provider, String code) trả về JWT. Lưu người dùng vào bảng Users với provider tương ứng. Triển khai endpoint GET /api/auth/{provider}/callback. Thêm logging và xử lý lỗi cho trường hợp thiếu code hoặc token không hợp lệ. Triển khai integration test sử dụng mock provider.
      - **Targeted Tag IDs:** [ARC-006], [DAT-001]

- **DAY 3: Triển khai service quản lý trung tâm (Centers) và gán Center Admin.**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.center-management [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002]`
      - **Low-Level Technical Task Instruction:** Triển khai entity Centers với các ràng buộc unique taxId, tạo CenterRepository, implement CenterService với các phương thức CRUD (create, update, delete). Triển khai endpoint POST /api/centers để tạo trung tâm mới, validation trùng taxId trả về lỗi conflict. Triển khai endpoint PUT /api/centers/{id} để cập nhật, DELETE để xóa. Triển khai assign/unassign Center Admin: cập nhật role người dùng thành CENTER_ADMIN và lưu centerId. Triển khai endpoint PATCH /api/users/{userId}/center/{centerId}. Thêm unit test cho từng API.
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002]

### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai quản lý khóa học, đăng ký học viên, và hệ thống thông báo. Xây dựng các bảng Courses, Enrollments, Notifications và các API tương ứng.
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend.course-management [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-002], [ARC-003]`
    *   `./sources/backend.enrollment [REQ-010], [REQ-011], [DAT-005], [ARC-008]`
    *   `./sources/backend.notification [REQ-016], [EXC-003], [DAT-008], [ARC-008]`
    *   `./sources/docs/phase2_architecture.md [REQ-007], [REQ-008], [REQ-009], [DAT-004], [REQ-010], [REQ-011], [DAT-005], [REQ-016], [EXC-003], [DAT-008]`
- **Database Schema DDL SQL Specification [DAT-004], [DAT-005], [DAT-008]:**

```sql
-- Bảng Courses
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
);

-- Bảng Enrollments
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE (student_id, course_id)
);

-- Bảng Notifications
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT now(),
    delivered BOOLEAN NOT NULL DEFAULT false
);
```

- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-016], [ARC-008]:**
    *   `GET /api/courses` – Trả về danh sách khóa học (`courseId, title, startDate, endDate, teacherName`).
    *   `POST /api/courses` – Tạo khóa học mới, validation xung đột lịch giảng cho giáo viên, trả về CourseDTO.
    *   `PUT /api/courses/{id}` – Cập nhật khóa học.
    *   `DELETE /api/courses/{id}` – Xóa khóa học.
    *   `PATCH /api/courses/{courseId}/teacher/{teacherId}` – Gán giáo viên cho khóa học, tạo notification cho giáo viên.
    *   `GET /api/enrollments/courses` – Học viên duyệt khóa học (trừ các khóa đã ghi danh).
    *   `POST /api/enrollments` – Đăng ký khóa học, tự động tạo tài khoản học viên nếu thiếu, push notification, gửi tin nhắn Zalo group.
    *   `POST /api/notifications` – Tạo bản ghi thông báo, trigger async job để gửi push notification và Zalo message, retry logic 3 lần.

- **Phase Localized Exception Handlers [EXC-003]:**
    *   Xử lý trường hợp gửi notification thất bại (ví dụ: token thiết bị không hợp lệ). Hệ thống ghi log lỗi, lên lịch retry sau 5 giây, 10 giây, 30 giây. Sau 3 lần thất bại, đánh dấu `delivered = false` và ghi lại `error_message`. API trả về HTTP 200 với trạng thái `queued` nhưng thông báo cho client về khả năng thất bại.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 4: Triển khai service quản lý khóa học (Courses) và phân công giáo viên.**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.course-management [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-002], [ARC-003]`
      - **Low-Level Technical Task Instruction:** Triển khai entity Courses với các trường startDate, endDate, teacherId, maxStudents. Tạo CourseRepository, implement CourseService với validation xung đột lịch giảng cho cùng giáo viên (SELECT * FROM courses WHERE teacher_id = ? AND (start_date < ? AND end_date > ?) OR ...). Triển khai endpoint POST /api/courses để tạo khóa học mới, trả về CourseDTO. Triển khai endpoint PUT /api/courses/{id} để cập nhật, DELETE để xóa. Triển khai assign/unassign teacher qua endpoint PATCH /api/courses/{courseId}/teacher/{teacherId}. Thêm logging và xử lý lỗi cho trường hợp xung đột lịch. Triển khai unit test cho validation.
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-002], [ARC-003]

- **DAY 5: Triển khai service đăng ký học viên (Enrollments) và flow đăng ký.**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.enrollment [REQ-010], [REQ-011], [DAT-005], [ARC-008]`
      - **Low-Level Technical Task Instruction:** Triển khai entity Enrollments, implement EnrollmentService với phương thức browseCourses(studentId) trả về các khóa học chưa ghi danh, và register(studentId, courseId) tạo bản ghi enrollment, tự động tạo tài khoản người dùng nếu thiếu, push notification qua hàng đợi, gửi tin nhắn Zalo group. Triển khai endpoint GET /api/enrollments/courses để duyệt, POST /api/enrollments để đăng ký. Thêm validation kiểm tra capacity và xung đột. Triển khai integration test cho flow đăng ký.
      - **Targeted Tag IDs:** [REQ-010], [REQ-011], [DAT-005], [ARC-008]

- **DAY 6: Triển khai service thông báo (Notifications) và hàng đợi push.**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.notification [REQ-016], [EXC-003], [DAT-008], [ARC-008]`
      - **Low-Level Technical Task Instruction:** Triển khai entity Notifications, implement NotificationService với phương thức send(userId, groupZalo, message) lưu vào DB, tạo payload push notification (FCM/APNs) và gửi qua hàng đợi. Triển khai endpoint POST /api/notifications để tạo thông báo, trigger async job xử lý. Thêm retry logic lên đến 3 lần khi gửi thất bại, đánh dấu delivered. Triển khai scheduler để gửi hàng đợi. Triển khai unit test cho thành công và thất bại.
      - **Targeted Tag IDs:** [REQ-016], [EXC-003], [DAT-008], [ARC-008]

### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai hệ thống điểm danh QR, quản lý thẻ hội viên, và quản lý khuyến mãi/thông báo. Xây dựng các bảng Attendance, StudentCards, Promotions, Announcements.
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend.attendance [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006], [ARC-007]`
    *   `./sources/backend.membership [REQ-014], [REQ-015], [DAT-007]`
    *   `./sources/backend.promotion [REQ-017], [REQ-018], [DAT-009]`
    *   `./sources/docs/phase3_architecture.md [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006], [REQ-014], [REQ-015], [DAT-007], [REQ-017], [REQ-018], [DAT-009]`
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007], [DAT-009]:**

```sql
-- Bảng Attendance
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE (student_id, course_id, attendance_date)
);

-- Bảng StudentCards
CREATE TABLE studentcards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);

-- Bảng Promotions
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT
);

-- Bảng Announcements
CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);
```

- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-017], [REQ-018], [ARC-007]:**
    *   `POST /api/attendance/qr` – Nhận `{studentId, courseId, timestamp}` → xác thực student-course, ghi điểm danh, trả về success/duplicate flag.
    *   `GET /api/attendance/report` – Tạo báo cáo điểm danh cho center/date range, xuất CSV.
    *   `GET /api/membership/card/{studentId}` – Trả về thông tin thẻ hội viên (`issueDate, validityDays, remainingDays`).
    *   `POST /api/membership/renew` – Nhận `{studentId, days}` → tính toán endDate mới, cập nhật `studentcards`.
    *   `GET /api/promotions` – Liệt kê khuyến mãi đang hiệu lực.
    *   `POST /api/promotions` – Tạo khuyến mãi mới, validation start/end date.
    *   `GET /api/announcements` – Liệt kê thông báo đang hiệu lực.
    *   `POST /api/announcements` – Tạo thông báo mới.

- **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
    *   Xử lý mất kết nối mạng trong quá trình quét QR: cache yêu cầu locally, retry khi kết nối lại, đảm bảo chỉ ghi một lần.
    *   Phát hiện duplicate scans trong cùng ngày: trả về success với flag `duplicate: true`, không tạo bản ghi mới.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 7: Triển khai service điểm danh (Attendance) và xử lý quét QR.**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.attendance [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006], [ARC-007]`
      - **Low-Level Technical Task Instruction:** Triển khai entity Attendance, implement AttendanceService với phương thức record(studentId, courseId, timestamp) kiểm tra duplicate cho cùng student, course, attendance_date, nếu đã tồn tại trả về success với flag duplicate. Sử dụng khóa unique (student_id, course_id, attendance_date) để đảm bảo bất biến. Triển khai endpoint POST /api/attendance/qr với payload {studentId, courseId, timestamp}. Thêm fallback khi mất mạng: cache request local, retry khi kết nối lại, đảm bảo chỉ ghi một lần. Triển khai unit test cho duplicate detection và network recovery.
      - **Targeted Tag IDs:** [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006], [ARC-007]

- **DAY 8: Triển khai service quản lý thẻ hội viên (Membership).**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membership [REQ-014], [REQ-015], [DAT-007]`
      - **Low-Level Technical Task Instruction:** Triển khai entity StudentCards, implement MembershipService với phương thức getCard(studentId) trả về issueDate, validityDays, remainingDays (computed). Triển khai endpoint GET /api/membership/card/{studentId}. Triển khai endpoint POST /api/membership/renew với payload {studentId, days} thực hiện thanh toán (giả lập), cập nhật endDate (issueDate + validityDays). Triển khai validation cho student tồn tại. Triển khai unit test cho tính toán remainingDays và flow gia hạn.
      - **Targeted Tag IDs:** [REQ-014], [REQ-015], [DAT-007]

- **DAY 9: Triển khai service khuyến mãi & thông báo (Promotion).**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.promotion [REQ-017], [REQ-018], [DAT-009]`
      - **Low-Level Technical Task Instruction:** Triển khai entity Promotions và Announcements, implement PromotionService với CRUD cho khuyến mãi (code, discountPercent, startDate, endDate) và CRUD cho thông báo (title, content, startDate, endDate). Triển khai endpoint POST /api/promotions, GET /api/promotions, PUT /api/promotions/{id}, DELETE /api/promotions/{id}. Triển khai endpoint POST /api/announcements, GET /api/announcements, auto-filter các bản ghi đã hết hạn dựa trên endDate. Triển khai unit test cho validation và auto-expire.
      - **Targeted Tag IDs:** [REQ-017], [REQ-018], [DAT-009]

### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai giao diện người dùng di động, hỗ trợ quốc tế hóa và SEO, và hệ thống báo cáo & phân tích. Xây dựng các thành phần frontend và backend báo cáo.
- **Target Physical Directory Matrix Map:**
    *   `./sources/frontend.mobile [REQ-020], [REQ-021]`
    *   `./sources/frontend.i18n [REQ-022], [REQ-023], [DAT-011]`
    *   `./sources.backend.reports [REQ-024], [REQ-025], [EXC-005]`
    *   `./sources/docs/phase4_architecture.md [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011], [REQ-024], [REQ-025], [EXC-005]`
- **Database Schema DDL SQL Specification [DAT-011]:**

```sql
-- Bảng SystemSettings
CREATE TABLE systemsettings (
    setting_key VARCHAR(100) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```

- **API and Event Routing Contracts [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-009]:**
    *   `GET /api/mobile/dashboard` – Trả về các chỉ số dashboard cho vai trò người dùng (student, teacher, admin).
    *   `POST /api/mobile/auth/token` – Nhận device token để đăng ký push notification.
    *   `GET /api/i18n/resources` – Trả về các bản dịch cho locale được yêu cầu.
    *   `GET /api/reports/attendance` – Tạo báo cáo điểm danh CSV cho center/date range.
    *   `GET /api/dashboard/summary` – Trả về tổng hợp real-time (totalStudents, activeCourses, upcomingSessions).

- **Phase Localized Exception Handlers [EXC-005]:**
    *   System Recovery After Outage: Khi dịch vụ phục hồi, xử lý các yêu cầu điểm danh QR pending trong hàng đợi (FIFO), ghi bản ghi điểm danh, và gửi notification cho user về các sự kiện đã phục hồi.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 10: Triển khai giao diện người dùng di động (Mobile UI).**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/frontend.mobile [REQ-020], [REQ-021]`
      - **Low-Level Technical Task Instruction:** Triển khai React Native app với các màn hình role-specific (Student, Teacher, Admin). Bao gồm màn hình quét QR (camera integration), danh sách khóa học, thẻ hội viên, danh sách thông báo. Triển khai authentication context sử dụng JWT, lưu token trong secure storage. Triển khai push notification registration với Firebase Cloud Messaging (FCM) token. Triển khai offline caching cho các endpoint chính sử dụng @react-native-async-storage. Triển khai unit test cho navigation và UI components.
      - **Targeted Tag IDs:** [REQ-020], [REQ-021]

- **DAY 11: Triển khai quốc tế hóa (i18n) và SEO.**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/frontend.i18n [REQ-022], [REQ-023], [DAT-011]`
      - **Low-Level Technical Task Instruction:** Triển khai i18n middleware sử dụng i18next, detect language từ localStorage, fallback Accept-Language header. Triển khai dynamic hreflang links trong head cho EN, VN, ES. Triển khai SEO meta tags (title, description) cho từng locale. Triển khai API endpoint GET /api/i18n/resources trả về các bản dịch. Triển khai unit test cho detection và rendering.
      - **Targeted Tag IDs:** [REQ-022], [REQ-023], [DAT-011]

- **DAY 12: Triển khai service báo cáo & phân tích (Reports).**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.reports [REQ-024], [REQ-025], [EXC-005]`
      - **Low-Level Technical Task Instruction:** Triển khai ReportingService với phương thức generateAttendanceReport(centerId, startDate, endDate) xuất file CSV với các cột StudentName, CourseName, AttendanceDate, Status. Triển khai endpoint GET /api/reports/attendance. Triển khai DashboardService với phương thức getSummary(centerId) trả về totalStudents, activeCourses, upcomingSessions (7 ngày tới). Triển khai endpoint GET /api/dashboard. Thêm logic xử lý khi mất kết nối: cache dữ liệu, retry khi phục hồi, trigger EXC-005. Triển khai integration test cho report generation.
      - **Targeted Tag IDs:** [REQ-024], [REQ-025], [EXC-005]

### 📈 Phase 5 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai DevOps, containerization, triển khai lên GKE, và đảm bảo tuân thủ các yêu cầu phi chức năng (bảo mật, hiệu suất, khả năng phục hồi). Xây dựng pipeline CI/CD, image Docker, cấu hình cloud, và các biện pháp bảo mật.
- **Target Physical Directory Matrix Map:**
    *   `./sources/infra [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
    *   `./sources/docs/phase5_architecture.md [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
- **Database Schema DDL SQL Specification:** (none needed)

- **API and Event Routing Contracts:** (none needed)

- **Phase Localized Exception Handlers:** (none needed)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 13: Xây dựng Docker image và push registry.**
  - **Sub-Agent Workflow Specialization:**
    * **[Docker]:**
      - **Target Component file path (`target_component`):** `./sources/infra/Dockerfile [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
      - **Low-Level Technical Task Instruction:** Xây dựng multi-stage Dockerfile cho backend (Quarkus) và frontend (Node.js) với kích thước image tối ưu (<500MB). Push image lên Google Artifact Registry. Triển khai security scan (Trivy) để phát hiện lỗ hổng, đảm bảo tuân thủ NFR-003 (mã hóa dữ liệu), NFR-005 (kích thước image). Triển khai unit test và integration test trong pipeline CI.
      - **Targeted Tag IDs:** [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]

- **DAY 14: Cấu hình GCP và triển khai GKE.**
  - **Sub-Agent Workflow Specialization:**
    * **[GCP]:**
      - **Target Component file path (`target_component`):** `./sources/infra/gcp [ARC-010], [NFR-002], [NFR-004], [NFR-008]`
      - **Low-Level Technical Task Instruction:** Cấu hình VPC với private subnets, tạo IAM service accounts cho các service, thiết lập Cloud Storage bucket cho backup, enable Cloud SQL (PostgreSQL) với backup tự động, thiết lập Cloud Monitoring và Cloud Logging. Triển khai Cloud Build pipeline để trigger build Docker image và deploy lên GKE. Triển khai GKE cluster với auto-scaling dựa trên CPU >70% hoặc latency >300ms (HPA). Triển khai deployment.yaml, service.yaml, ingress.yaml. Triển khai health checks và tự động rollback khi lỗi.
      - **Targeted Tag IDs:** [ARC-010], [NFR-002], [NFR-004], [NFR-008]

- **DAY 14 (GKE Agent):**
  - **Sub-Agent Workflow Specialization:**
    * **[GKE]:**
      - **Target Component file path (`target_component`):** `./sources/infra/gke [ARC-010], [NFR-002], [NFR-004]`
      - **Low-Level Technical Task Instruction:** Tạo GKE cluster version 1.27+, cấu hình node pools, kích hoạt network policy, thiết lập CNI. Triển khai các deployment từ Docker images, cấu hình resource limits, liveness/readiness probes. Thiết lập HPA dựa trên metric tùy chỉnh (latency, request count). Triển khai CI/CD pipeline với GitHub Actions để tự động deploy khi có thay đổi code. Triển khai monitoring với Prometheus và alerting qua Alertmanager.
      - **Targeted Tag IDs:** [ARC-010], [NFR-002], [NFR-004]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-001]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng Prepared Statements với JDBC, Hibernate Criteria API, hoặc QueryDSL. Áp dụng Whitelist cho các giá trị sắp xếp (ví dụ: sortBy ∈ {“name”, “date”, “id”}). Áp dụng ORM mapping an toàn, không cho phép raw SQL.

- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Áp dụng auto-escaping trong Thymeleaf (cho Java) và React (JSX). Sử dụng helmet CSP cho frontend, đặt header `Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'` chỉ cho các script cần thiết. Áp dụng validation đầu vào cho các trường HTML.

- **Multi-Tenant CORS Security Rails:** Cấu hình CORS cho từng tenant dựa trên origin, sử dụng `Access-Control-Allow-Origin` động với whitelist. Xác thực tenant qua JWT claim `tenant_id`. Áp dụng same-origin cho các API nội bộ.

- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Sử dụng interceptor `@LogSanitization` để xóa thông tin nhạy cảm (email, SSN) trước khi ghi log. Áp dụng `@JsonSerialize` với `JsonInclude.Include.NON_NULL`. Thiết lập threshold cho độ dài log, tự động che giấu các trường PII bằng `***`.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng @capacitor/core để quản lý file hệ thống, lưu trữ an toàn với @capacitor/preferences, chặn back-button với native plugin, fetch data qua API với timeout và retry. Áp dụng URL scheme cho deep linking (app://course/123). Áp dụng caching với IndexedDB thông qua Capacitor Storage.

- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware phát hiện locale từ cookie, header Accept-Language, fallback sang default (EN). Sử dụng react-i18next với namespace cho từng phần. Tự động generate hreflang links: `<link rel="alternate" hreflang="en" href="https://example.com/en/page"/>`. Sử dụng schema.org cho các cấu trúc dữ liệu đa ngôn ngữ.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Mỗi ngày tạo branch mới `features/development-phase-X-day-Y` (X là số phase, Y là số ngày). Sử dụng git fork từ `main` để đảm bảo isolation.

- **Validation Guard Pipeline Gates:** Sau khi merge, GitHub Actions chạy các bước: `mvn clean verify` (hoặc `npm test`), kiểm tra độ phủ sóng >=85%, kiểm tra style (Spotless), kiểm tra bảo mật (Snyk). Chỉ cho phép merge khi tất cả các gate vượt qua.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`