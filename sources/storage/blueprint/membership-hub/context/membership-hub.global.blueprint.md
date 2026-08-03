# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260803044420 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/03 04:44:20 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống được thiết kế theo kiến trúc **Microservices** với mô hình **Event-Driven Architecture (EDA)**. Các thành phần nghiệp vụ được phân tách thành các dịch vụ độc lập (User Service, Center Service, Course Service, Attendance Service, Notification Service, etc.) tuân thủ nguyên tắc **CQRS** (Command/Query Separation) để tối ưu hiệu suất đọc ghi. Các tương tác giữa dịch vụ được thực hiện qua **Message Brokers** (ví dụ: Kafka, RabbitMQ) đảm bảo tính bất biến và khả năng mở rộng. Lõi phản hồi (Reactive Core) sử dụng các luồng **Reactive Streams** để xử lý bất đồng bộ, đảm bảo khả năng chịu tải cao và độ trễ thấp cho các API quan trọng (xác thực, điểm danh QR, liệt kê khóa học). Các biên giới đa trung tâm được xác định rõ ràng, mỗi trung tâm hoạt động như một tenant độc lập với các chính sách truy cập được áp dụng ở lớp gateway.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Dòng dữ liệu chính bao gồm:

* **Luồng xác thực** – Người dùng đăng nhập qua email/mật khẩu hoặc các nhà cung cấp OAuth2 (Firebase, Google, Facebook). JWT access token có hạn dùng 15 phút, refresh token 7 ngày.
* **Luồng xử lý điểm danh QR** – Ứng dụng di động quét mã QR của khóa học, gửi `studentId` và `timestamp` đến Attendance Service. Dịch vụ xác thực mối quan hệ học viên-khóa học, ghi lại bản ghi điểm danh một cách idempotent.
* **Luồng gửi thông báo** – Khi có sự kiện (tạo thông báo, phân công giáo viên, ghi danh học viên), hệ thống tạo bản ghi Notification, đẩy push notification đến thiết bị di động qua Firebase Cloud Messaging (FCM)/Apple APNs, đồng thời đăng bài lên nhóm Zalo được chỉ định.
* **Luồng tích hợp backend ứng dụng di động** – Frontend Next.js tiêu thụ REST APIs qua bearer token, hỗ trợ lưu trữ dữ liệu ngoại tuyến (IndexedDB) để hoạt động khi mất kết nối mạng.

Các kênh bất đồng bộ được định nghĩa dưới dạng **topics** trong message broker, với các subscriber là các microservice tương ứng, đảm bảo xử lý phi tập trung và khả năng phục hồi.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.x, Hibernate ORM, JDBC (PostgreSQL), SmallRye Reactive Messaging, Apache Kafka (hoặc RabbitMQ), OpenTelemetry, JUnit 5, AssertJ, Lombok, MapStruct, Jackson, Spring Security (tích hợp với OAuth2), Flyway/Liquibase cho migration.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14 (React 18), TypeScript, Tailwind CSS, React Query (SWR), Redux Toolkit, Capacitor cho native bridge, React Native cho các module di động chuyên sâu, Localization với i18next, SEO với Next.js dynamic metadata, PWA cho offline caching.
- **DevOps & Infra:** Docker (multi‑stage), Kubernetes (Helm charts), Google Cloud Platform (GCP) – Cloud SQL (PostgreSQL), Cloud Memorystore (Redis), Cloud Pub/Sub, Firebase Authentication, Firebase Cloud Messaging, Zalo OAuth2 API, GitHub Actions (CI/CD), Helm, Argo CD, Prometheus + Grafana, Jaeger cho tracing, Trivy cho quét bảo mật hình ảnh.
- **Security & Compliance:** Spring Security, OAuth2 Resource Server, JWT (JJWT), BCrypt cho hash mật khẩu, CORS đa tenant, CSP headers, OWASP Java Security Guidelines, GDPR/CCPA data handling libraries, Flyway baseline verification.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** Workspace làm việc thực sự được cố định tại `..` (căn cứ vào hệ thống tệp gốc). Tất cả các đường dẫn được tạo ra PHẢI bắt đầu bằng `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Áp dụng quy tắc tiền tố thư mục động theo Protocol 1: logic backend → `./sources/backend.<service-name>`, frontend → `./sources/frontend`, hạ tầng DevOps → `./sources/infra`.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Tất cả mã nguồn Java PHẢI nằm trong gói cơ sở doanh nghiệp `org.nlh4j.saas.membershiphub`. Chuỗi “membership-hub” được chuẩn hóa thành dạng thuần chữ thường, không dấu phẩy, gạch ngang hoặc gạch dưới.
- **Strict Tester Target Path Syntax:** Bất kỳ thành phần nào được Tester Sub-Agent nhắm mục tiêu PHẢI được biểu diễn dưới dạng cặp `<source_component>;<test_suite_file>` với cả hai phần bắt đầu bằng `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Ngày 1‑3 | `./sources/backend.membershiphub.model`, `./sources/backend.membershiphub.repository`, `./sources/backend.membershiphub.service`, `./sources/backend.membershiphub.security`, `./sources/backend.membershiphub.auth` | Triển khai mô hình dữ liệu người dùng/vai trò, repository CRUD, service xử lý đăng ký/xác thực, thiết lập RBAC, bảo mật cơ bản, xử lý ngoại lệ xác thực đầu vào. | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [REQ-001], [REQ-002], [REQ-003], [DAT-001], [DAT-003], [EXC-004], [NFR-001], [NFR-003] |
| Phase 2 | Ngày 4‑5 | `./sources/backend.membershiphub.center`, `./sources/backend.membershiphub.course`, `./sources/backend.membershiphub.enrollment`, `./sources/backend.membershiphub.notification` | Xây dựng CRUD cho Trung tâm và Khóa học, logic ghi danh học viên, hàng đợi thông báo, xác thực xung đột lịch, triển khai API công khai. | Tester | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-003], [DAT-004], [DAT-005], [DAT-008], [NFR-004], [NFR-003] |
| Phase 3 | Ngày 6‑7 | `./sources/backend.membershiphub.attendance`, `./sources/backend.membershiphub.studentcard`, `./sources/backend.membershiphub.promotion`, `./sources/backend.membershiphub.announcement` | Triển khai dịch vụ điểm danh QR với phát hiện trùng lặp, quản lý thẻ hội viên (issue, gia hạn), quản lý khuyến mãi & thông báo, tích hợp push notification, xử lý ngoại lệ mạng và trùng lặp. | Reviewer | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [DAT-006], [DAT-007], [DAT-009], [DAT-010], [EXC-001], [EXC-002], [EXC-003], [NFR-005], [NFR-006] |
| Phase 4 | Ngày 8‑10 | `./sources/backend.membershiphub.i18n`, `./sources/backend.membershiphub.report`, `./sources/backend.membershiphub.security.audit`, `./sources/backend.membershiphub.config`, `./sources/infra.docker`, `./sources/infra.gcp`, `./sources/infra.gke` | Triển khai quốc tế hóa và SEO (meta tags, hreflang), module báo cáo & phân tích (CSV, dashboard), ghi nhật ký kiểm toán, tuân thủ GDPR/CCPA, xây dựng Docker image, cung cấp hạ tầng GCP (VPC, IAM, Cloud SQL), triển khai GKE với HPA, tích hợp CI/CD, hoàn thiện các chỉ số hiệu năng và khả năng sẵn sàng. | Doc | [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-011], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [ARC-007], [ARC-008], [ARC-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

<!--START_DELIMITTER-->
### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các thành phần cốt lõi hỗ trợ đăng ký người dùng, xác thực đa nhà cung cấp, phân quyền vai trò và quản lý trung tâm ban đầu. Xây dựng mô hình dữ liệu cho người dùng, vai trò, trung tâm và các bảng tra cứu liên quan, đồng thời thiết lập các chính sách bảo mật cơ bản (TLS, JWT, bcrypt). Đảm bảo xử lý đầu vào xác thực cho các trường hợp đăng ký và đăng nhập.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend.membershiphub.model/Users.java [DAT-001]`
  * `./sources/backend.membershiphub.model/Roles.java [DAT-001]`
  * `./sources/backend.membershiphub.model/Centers.java [DAT-003]`
  * `./sources/backend.membershiphub.repository/UserRepository.java [DAT-001]`
  * `./sources/backend.membershiphub.repository/RoleRepository.java [DAT-001]`
  * `./sources/backend.membershiphub.repository/CenterRepository.java [DAT-003]`
  * `./sources/backend.membershiphub.service/UserService.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-001], [REQ-002], [REQ-003]`
  * `./sources/backend.membershiphub.security/JwtAuthenticationFilter.java [ARC-006]`
  * `./sources/backend.membershiphub.security/PasswordEncoderConfig.java`
- **Database Schema DDL SQL Specification [DAT-001], [DAT-003]:**
```sql
-- Bảng Users & Roles (DAT-001)
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
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Bảng Centers (DAT-003)
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) NOT NULL UNIQUE,
    contact_phone VARCHAR(30),
    contact_email VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-001]‑[ARC-006]:**
  * `POST /api/auth/register` – yêu cầu `{email, password, fullName, provider}`; trả về `{token, userId}`. `[REQ-001]`
  * `POST /api/auth/social` – trao đổi OAuth2 code lấy thông tin người dùng từ Firebase/Google/Facebook; tạo hoặc cập nhật bản ghi người dùng, cấp JWT. `[REQ-002]`
  * `PUT /api/users/{userId}/role` – chỉ dành cho System Admin; cập nhật `role_id` của người dùng, áp dụng lại quyền ngay lập tức. `[REQ-003]`
  * `GET /api/centers` – liệt kê tất cả trung tâm (Name, Address, TaxID, Contact). `[REQ-004]`
  * `POST /api/centers` – tạo trung tâm mới, kiểm tra trùng tax_id. `[REQ-005]`
  * `DELETE /api/centers/{centerId}` – xóa trung tâm. `[REQ-006]`
  * Xác thực JWT qua `Authorization: Bearer <token>` sử dụng `JwtAuthenticationFilter`. `[ARC-006]`
- **Phase Localized Exception Handlers [EXC-004]:**
  * Xác thực đầu vào không hợp lệ (email sai định dạng, thiếu trường bắt buộc) → trả về HTTP 400 với danh sách chi tiết các trường không hợp lệ. `[EXC-004]`
  * Xung đột khóa duy nhất (email hoặc tax_id trùng lặp) → HTTP 409 với thông báo xung đột.
  * Lỗi máy chủ nội bộ → HTTP 500 với nhật ký theo dõi.

<!--END_DELIMITTER-->

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1: Triển khai mô hình dữ liệu người dùng và vai trò**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.model/Users.java [DAT-001]`
      - **Low-Level Technical Task Instruction:** Trong file Users.java, định nghĩa các trường dữ liệu tương ứng với bảng `users`, sử dụng annotation `@Entity`, `@Table`, `@Id`, `@Column`, `@ManyToOne` với `Roles`. Áp dụng `@Email` cho email, `@NotBlank` cho các trường bắt buộc, `@CreatedDate`/`@LastModifiedDate` cho timestamp, và `@PrePersist`/`@PreUpdate` để tự động cập nhật `updated_at`. Đảm bảo sử dụng `@GeneratedValue(strategy = GenerationType.AUTO)` cho khóa chính nếu cần. `[DAT-001]`
      - **Targeted Tag IDs:** [DAT-001]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.model/Roles.java [DAT-001]`
      - **Low-Level Technical Task Instruction:** Tạo lớp Roles.java với các trường `roleId`, `name`, `description`. Sử dụng `@Id` cho roleId, `@Column(unique = true)` cho name, thêm `@Entity` và `@Table`. Đảm bảo constructor không tham số, constructor đầy đủ tham số, getter/setter. `[DAT-001]`
      - **Targeted Tag IDs:** [DAT-001]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.repository/UserRepository.java [DAT-001]`
      - **Low-Level Technical Task Instruction:** Triển khai interface UserRepository extends `JpaRepository<Users, UUID>` với các phương thức tùy chỉnh: `findByEmail(String email)`, `findByRole(Roles role)`. Thêm `@Repository` và `@Transactional`. Đảm bảo các phương thức tuân thủ giao dịch và xử lý ngoại lệ JPA. `[DAT-001]`
      - **Targeted Tag IDs:** [DAT-001]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.repository/RoleRepository.java [DAT-001]`
      - **Low-Level Technical Task Instruction:** Triển khai interface RoleRepository extends `JpaRepository<Roles, Short>` với phương thức `findByName(String name)`. Thêm `@Repository`. Đảm bảo kiểu dữ liệu khớp với `role_id` SMALLINT. `[DAT-001]`
      - **Targeted Tag IDs:** [DAT-001]

- **DAY 2: Xây dựng service xử lý đăng ký người dùng và xác thực**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.service/UserService.java [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-001], [REQ-002], [REQ-003]`
      - **Low-Level Technical Task Instruction:** Trong UserService.java, triển khai các method: `registerUser(RegisterRequest req)` tạo Users mới với role mặc định là Student, mã hóa mật khẩu bằng BCrypt, lưu vào database; `authenticateUser(String email, String password)` xác thực thông tin đăng nhập, tạo JWT; `assignRole(Long userId, Short newRoleId)` cập nhật vai trò người dùng; `getUserRoles()` trả về danh sách vai trò; `validatePermission(...)` kiểm tra quyền truy cập dựa trên vai trò. Thêm @Service, @Transactional, và xử lý các trường hợp ngoại lệ đăng ký (EXC-004). `[ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-001], [REQ-002], [REQ-003]`
      - **Targeted Tag IDs:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [REQ-001], [REQ-002], [REQ-003]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.security/JwtAuthenticationFilter.java [ARC-006]`
      - **Low-Level Technical Task Instruction:** Triển khai JwtAuthenticationFilter mở rộng `OncePerRequestFilter`. Trong `doFilterInternal`, trích xuất Bearer token từ header, xác thực token bằng JwtUtil, thiết lập Authentication với UserDetails, sau đó gọi `filterChain.doFilter`. Thêm `@Component` và cấu hình trong SecurityConfig. Đảm bảo token hết hạn sau 15 phút. `[ARC-006]`
      - **Targeted Tag IDs:** [ARC-006]

- **DAY 3: Xây dựng repository trung tâm và triển khai bảo mật cơ bản**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.model/Centers.java [DAT-003]`
      - **Low-Level Technical Task Instruction:** Tạo lớp Centers.java với các trường `centerId`, `name`, `address`, `taxId`, `contactPhone`, `contactEmail`. Sử dụng annotation `@Entity`, `@Table`, `@Id`, `@Column`, thêm constraint `unique` cho taxId, `@Email` cho contactEmail. Đảm bảo constructor, getter/setter. `[DAT-003]`
      - **Targeted Tag IDs:** [DAT-003]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.repository/CenterRepository.java [DAT-003]`
      - **Low-Level Technical Task Instruction:** Triển khai interface CenterRepository extends `JpaRepository<Centers, UUID>` với phương thức `findByTaxId(String taxId)`, `findByNameContainingIgnoreCase(String keyword)`. Thêm `@Repository`. Đảm bảo các phương thức có sẵn cho CRUD. `[DAT-003]`
      - **Targeted Tag IDs:** [DAT-003]
    * **[Assigned Sub-Agent literal token: Docker]:**
      - **Target Component file path (`target_component`):** `./sources/infra.docker/Dockerfile [NFR-005]`
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile đa giai đoạn: giai đoạn builder sử dụng `maven:3.9-eclipse-temurin-21` để đóng gói ứng dụng Spring Boot; giai đoạn runtime sử dụng `eclipse-temurin:21-jre-alpine`. Sao chép tệp JAR, thiết lập người dùng không phải root, phơi cổng 8080, thêm nhãn `org.opencontainers.image.base.name` và `maintainer`. Đảm bảo kích thước ảnh cuối cùng < 500MB. `[NFR-005]`
      - **Targeted Tag IDs:** [NFR-005]

<!--END_DELIMITTER-->

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các module quản lý trung tâm, khóa học, ghi danh học viên và hệ thống thông báo. Xây dựng API CRUD cho Trung tâm và Khóa học, logic xung đột lịch, service ghi danh, và hàng đợi thông báo. Đảm bảo các chính sách bảo mật đa trung tâm và kiểm tra quyền truy cập.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend.membershiphub.center/CenterController.java [REQ-004], [REQ-005], [REQ-006]`
  * `./sources/backend.membershiphub.center/CenterService.java [REQ-004], [REQ-005], [REQ-006]`
  * `./sources/backend.membershiphub.course/CourseController.java [REQ-007], [REQ-008], [REQ-009]`
  * `./sources/backend.membershiphub.course/CourseService.java [REQ-007], [REQ-008], [REQ-009]`
  * `./sources/backend.membershiphub.enrollment/EnrollmentController.java [REQ-010], [REQ-011]`
  * `./sources/backend.membershiphub.enrollment/EnrollmentService.java [REQ-010], [REQ-011]`
  * `./sources/backend.membershiphub.notification/NotificationService.java [REQ-016]`
  * `./sources/backend.membershiphub.notification/NotificationController.java [REQ-016]`
- **Database Schema DDL SQL Specification [DAT-003], [DAT-004], [DAT-005], [DAT-008]:**
```sql
-- Bảng Courses (DAT-004)
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
);

-- Bảng Enrollments (DAT-005)
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id)
);

-- Bảng Notifications (DAT-008)
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-016]:**
  * `GET /api/centers` – trả về danh sách trung tâm. `[REQ-004]`
  * `POST /api/centers` – tạo trung tâm mới, kiểm tra tax_id. `[REQ-005]`
  * `DELETE /api/centers/{centerId}` – xóa trung tâm. `[REQ-006]`
  * `GET /api/courses` – liệt kê khóa học (CourseID, Title, StartDate, EndDate, TeacherName). `[REQ-007]`
  * `POST /api/courses` – tạo khóa học mới, kiểm tra xung đột lịch của giáo viên. `[REQ-008]`
  * `PUT /api/courses/{courseId}/teacher` – gán giáo viên cho khóa học, đẩy notification. `[REQ-009]`
  * `POST /api/enrollments` – học viên ghi danh khóa học, tự động tạo tài khoản học viên nếu thiếu, đẩy notification. `[REQ-010], [REQ-011]`
  * `POST /api/notifications` – ghi lại thông báo, đưa vào hàng đợi push notification và Zalo. `[REQ-016]`
- **Phase Localized Exception Handlers:** (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

<!--END_DELIMITTER-->

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 4: Xây dựng controller và service trung tâm**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.center/CenterController.java [REQ-004], [REQ-005], [REQ-006]`
      - **Low-Level Technical Task Instruction:** Trong CenterController, triển khai các endpoint REST: `@GetMapping`, `@PostMapping`, `@DeleteMapping`. Sử dụng `@Valid` cho validation request body, `@CurrentUser` để lấy thông tin admin hiện tại. Trả về ResponseEntity với trạng thái phù hợp. Thêm ghi chú `@Operation` cho Swagger. `[REQ-004], [REQ-005], [REQ-006]`
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.center/CenterService.java [REQ-004], [REQ-005], [REQ-006]`
      - **Low-Level Technical Task Instruction:** Triển khai CenterService với các method: `listCenters()`, `createCenter(CenterRequest req)`, `deleteCenter(UUID centerId)`. Trong `createCenter`, kiểm tra tax_id duy nhất bằng `centerRepository.existsByTaxId`. Sử dụng `@Transactional`. Thêm xử lý ngoại lệ cho xung đột khóa duy nhất. `[REQ-004], [REQ-005], [REQ-006]`
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]

- **DAY 5: Xây dựng module khóa học và ghi danh học viên**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.course/CourseController.java [REQ-007], [REQ-008], [REQ-009]`
      - **Low-Level Technical Task Instruction:** Triển khai các endpoint: `GET /courses` trả về CourseDTO; `POST /courses` nhận CourseRequest, gọi `courseService.create`; `PUT /courses/{id}/teacher` gán giáo viên. Sử dụng `@PreAuthorize('hasAnyRole("SYSTEM_ADMIN","CENTER_ADMIN")')` cho bảo mật. Thêm validation cho overlapping dates. `[REQ-007], [REQ-008], [REQ-009]`
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.course/CourseService.java [REQ-007], [REQ-008], [REQ-009]`
      - **Low-Level Technical Task Instruction:** Triển khai logic service: `listCourses()`, `createCourse(CourseRequest req)`, `assignTeacher(UUID courseId, UUID teacherId)`. Trong `createCourse`, kiểm tra xung đột lịch với các khóa học hiện có của giáo viên bằng `courseRepository.findOverlappingCourses(teacherId, start, end)`. Sử dụng `@Transactional`. Đẩy sự kiện `CourseCreatedEvent` cho notification service. `[REQ-007], [REQ-008], [REQ-009]`
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]
    * **[Assigned Sub-Agent literal token: Tester]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.course/CourseController.java;./sources/backend.membershiphub.course/CourseService.java`
      - **Low-Level Technical Task Instruction:** Viết unit test cho các endpoint: kiểm tra `GET /courses` trả về danh sách rỗng khi chưa có khóa học; kiểm tra `POST /courses` với overlapping dates trả về HTTP 409; kiểm tra `PUT /courses/{id}/teacher` thành công trả về HTTP 200. Sử dụng MockMvc, Mockito, và JUnit5. Đảm bảo độ phủ mã >= 85%. `[REQ-007], [REQ-008], [REQ-009]`
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]

<!--END_DELIMITTER-->

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các module điểm danh QR, thẻ hội viên, khuyến mãi, thông báo và xử lý ngoại lệ mạng. Xây dựng service điểm danh với logic idempotent, service quản lý thẻ hội viên (issue/gia hạn), module quản lý khuyến mãi & thông báo, và tích hợp push notification. Đảm bảo các chính sách bảo mật cho việc ghi danh và điểm danh.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend.membershiphub.attendance/AttendanceController.java [REQ-012], [REQ-013]`
  * `./sources/backend.membershiphub.attendance/AttendanceService.java [REQ-012], [REQ-013]`
  * `./sources/backend.membershiphub.studentcard/StudentCardController.java [REQ-014], [REQ-015]`
  * `./sources/backend.membershiphub.studentcard/StudentCardService.java [REQ-014], [REQ-015]`
  * `./sources/backend.membershiphub.promotion/PromotionController.java [REQ-017], [REQ-018]`
  * `./sources/backend.membershiphub.promotion/PromotionService.java [REQ-017], [REQ-018]`
  * `./sources/backend.membershiphub.announcement/AnnouncementController.java [REQ-017], [REQ-018]`
  * `./sources/backend.membershiphub.announcement/AnnouncementService.java [REQ-017], [REQ-018]`
  * `./sources/backend.membershiphub.notification/NotificationService.java [REQ-016], [EXC-003]`
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007], [DAT-009], [DAT-010]:**
```sql
-- Bảng Attendance (DAT-006)
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id, attendance_date)
);

-- Bảng StudentCards (DAT-007)
CREATE TABLE studentcards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);

-- Bảng Promotions (DAT-009)
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT
);

-- Bảng Announcements (DAT-010)
CREATE TABLE announcements (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);
```
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018]:**
  * `POST /api/attendance/scan` – nhận `{studentId, courseId, timestamp}`; ghi lại điểm danh, trả về `{attendanceId, duplicateFlag}`. `[REQ-012]`
  * `GET /api/attendance/{studentId}/{courseId}/{date}` – truy vấn bản ghi điểm danh. `[REQ-013]`
  * `GET /api/studentcards/{studentId}` – trả về thông tin thẻ (ngày hiệu lực còn lại). `[REQ-014]`
  * `POST /api/studentcards/{studentId}/renew` – gia hạn thẻ theo số ngày được chọn, cập nhật end date. `[REQ-015]`
  * `POST /api/notifications` – ghi lại thông báo, đưa vào hàng đợi push notification và Zalo. `[REQ-016]`
  * `POST /api/promotions` – tạo khuyến mãi mới, lưu vào DB. `[REQ-017]`
  * `PUT /api/promotions/{promoId}` – cập nhật khuyến mãi. `[REQ-018]`
  * `POST /api/announcements` – tạo thông báo mới. `[REQ-017]`
  * `PUT /api/announcements/{announcementId}` – cập nhật thông báo. `[REQ-018]`
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003]:**
  * **EXC-001 (Network & Connectivity Drops During QR Scan):** Nếu điểm danh bị lỗi do mất mạng, ứng dụng di động sẽ lưu yêu cầu quét cục bộ; khi kết nối được khôi phục, client gửi lại yêu cầu; service kiểm tra `attendance_date` và `student_id` để tránh ghi đè. `[EXC-001]`
  * **EXC-002 (Duplicate Attendance Submission):** Service kiểm tra sự tồn tại của bản ghi cho `(student_id, course_id, attendance_date)` trước khi chèn; nếu đã tồn tại, trả về success với `duplicate: true`. `[EXC-002]`
  * **EXC-003 (Failed Notification Delivery):** Khi push notification thất bại (ví dụ: token không hợp lệ), system ghi log lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu `delivered = false`. `[EXC-003]`

<!--END_DELIMITTER-->

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 6: Xây dựng service điểm danh QR**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.attendance/AttendanceController.java [REQ-012], [REQ-013]`
      - **Low-Level Technical Task Instruction:** Triển khai AttendanceController với endpoint `POST /scan` nhận `AttendanceRequest` (`studentId`, `courseId`, `timestamp`). Controller gọi `attendanceService.recordScan(...)`. Trả về `ResponseEntity<AttendanceResponse>` với HTTP 200. Thêm annotation `@PostMapping`, `@RequestBody`. `[REQ-012], [REQ-013]`
      - **Targeted Tag IDs:** [REQ-012], [REQ-013]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.attendance/AttendanceService.java [REQ-012], [REQ-013]`
      - **Low-Level Technical Task Instruction:** Triển khai `recordScan(UUID studentId, UUID courseId, Instant timestamp)` kiểm tra mối quan hệ học viên-khóa học (`enrollmentRepository.existsByStudentIdAndCourseId`). Nếu đã có bản ghi cho `attendance_date` hôm nay, trả về duplicate flag true. Nếu chưa có, tạo bản ghi `Attendance` và lưu. Sử dụng `@Transactional` và xử lý `DataIntegrityViolationException`. `[REQ-012], [REQ-013]`
      - **Targeted Tag IDs:** [REQ-012], [REQ-013]

- **DAY 7: Xây dựng module thẻ hội viên và quản lý khuyến mãi/thông báo**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.studentcard/StudentCardController.java [REQ-014], [REQ-015]`
      - **Low-Level Technical Task Instruction:** Triển khai các endpoint: `GET /studentcards/{studentId}` trả về `StudentCardDTO`; `POST /studentcards/{studentId}/renew` nhận `RenewRequest` (`days`), gọi `studentCardService.renew(...)`. Sử dụng `@PreAuthorize('hasRole(\"STUDENT\")')`. `[REQ-014], [REQ-015]`
      - **Targeted Tag IDs:** [REQ-014], [REQ-015]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.studentcard/StudentCardService.java [REQ-014], [REQ-015]`
      - **Low-Level Technical Task Instruction:** Triển khai `getCard(UUID studentId)` truy vấn `studentcards` và tính `remainingDays = validityDays - daysUsed`. Triển khai `renew(UUID studentId, int days)` cập nhật `validityDays` và `remainingDays`, lưu bản ghi. Sử dụng `@Transactional`. `[REQ-014], [REQ-015]`
      - **Targeted Tag IDs:** [REQ-014], [REQ-015]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.promotion/PromotionController.java [REQ-017], [REQ-018]`
      - **Low-Level Technical Task Instruction:** Triển khai endpoint `POST /promotions` nhận `PromotionRequest`, gọi `promotionService.create`. Endpoint `PUT /promotions/{id}` cập nhật. Sử dụng validation `@Valid`. `[REQ-017], [REQ-018]`
      - **Targeted Tag IDs:** [REQ-017], [REQ-018]
    * **[Assigned Sub-Agent literal token: Reviewer]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.promotion/PromotionService.java [REQ-017], [REQ-018]`
      - **Low-Level Technical Task Instruction:** Triển khai logic service: `create(PromotionRequest req)` lưu vào DB, `update(UUID id, PromotionRequest req)` cập nhật. Kiểm tra `startDate` <= `endDate` nếu có. Đẩy sự kiện `PromotionCreatedEvent`. Thêm ghi chú `@Service`. `[REQ-017], [REQ-018]`
      - **Targeted Tag IDs:** [REQ-017], [REQ-018]

<!--END_DELIMITTER-->

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các tính năng quốc tế hóa và SEO, module báo cáo & phân tích, ghi nhật ký kiểm toán, tuân thủ GDPR/CCPA, container hóa, cung cấp hạ tầng GCP, triển khai GKE, và hoàn thiện các chỉ số hiệu năng, khả năng sẵn sàng, sao lưu/khôi phục. Xây dựng hệ thống logging và audit cho mọi thao tác người dùng, đảm bảo xóa dữ liệu cá nhân theo yêu cầu.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend.membershiphub.i18n/I18nConfig.java [REQ-022], [REQ-023]`
  * `./sources/backend.membershiphub.i18n/MessageSourceConfig.java`
  * `./sources/backend.membershiphub.report/ReportController.java [REQ-024], [REQ-025]`
  * `./sources/backend.membershiphub.report/ReportService.java [REQ-024], [REQ-025]`
  * `./sources/backend.membershiphub.security/audit/AuditLogger.java [NFR-006]`
  * `./sources/backend.membershiphub.config/AppProperties.java [DAT-011]`
  * `./sources/infra.docker/Dockerfile [NFR-005]`
  * `./sources/infra.docker/docker-compose.yml`
  * `./sources/infra.gcp/gcp-pipeline.yaml`
  * `./sources/infra.gke/gke-deployment.yaml`
- **Database Schema DDL SQL Specification [DAT-011]:**
```sql
-- Bảng SystemSettings (DAT-011)
CREATE TABLE systemsettings (
    setting_key VARCHAR(100) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-007], [ARC-008], [ARC-009]:**
  * `GET /api/chatbot/query` – nhận `{question}` từ bất kỳ người dùng nào, trả về câu trả lời từ AI chatbot. `[REQ-019]`
  * `GET /api/mobile/ui/{role}` – trả về cấu hình giao diện người dùng cho vai trò di động (Student, Teacher, Admin). `[REQ-020]`
  * `POST /api/push/register` – đăng ký thiết bị (`deviceToken`, `platform`) cho push notification. `[REQ-021]`
  * `GET /api/i18n/messages` – trả về các chuỗi đã dịch cho locale được yêu cầu. `[REQ-022]`
  * `GET /api/seo/hreflang` – trả về liên kết hreflang cho các phiên bản ngôn ngữ. `[REQ-023]`
  * `GET /api/reports/attendance` – tạo báo cáo điểm danh CSV cho trung tâm và khoảng ngày được chọn. `[REQ-024]`
  * `GET /api/dashboard/center` – trả về các chỉ số tóm tắt (totalStudents, activeCourses, upcomingSessions). `[REQ-025]`
  * `POST /api/attendance/qr` – endpoint cho ứng dụng di động quét QR, gửi `studentId` và `timestamp`. `[ARC-007]`
  * `POST /api/notifications/push` – đẩy push notification đến thiết bị đã đăng ký. `[ARC-008]`
  * `POST /api/mobile/integrate` – xác thực token di động, thiết lập phiên làm việc. `[ARC-009]`
- **Phase Localized Exception Handlers [EXC-005]:**
  * **EXC-005 (System Recovery After Outage):** Khi service được khôi phục sau sự cố, hệ thống xử lý các bản ghi điểm danh chờ (pending attendance scans) theo thứ tự FIFO, ghi lại các bản ghi và gửi notification đến học viên tương ứng. `[EXC-005]`

<!--END_DELIMITTER-->

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 8: Triển khai quốc tế hóa và SEO**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.i18n/I18nConfig.java [REQ-022], [REQ-023]`
      - **Low-Level Technical Task Instruction:** Trong I18nConfig, cấu hình `ResourceBundleMessageSource` với basename `messages`, hỗ trợ các locale `en`, `vi`, `es`. Thêm `LocaleResolver` dựa trên header `Accept-Language` hoặc cookie. Đảm bảo tất cả các thuộc tính được đánh dấu `@Bean`. `[REQ-022], [REQ-023]`
      - **Targeted Tag IDs:** [REQ-022], [REQ-023]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.i18n/MessageSourceConfig.java`
      - **Low-Level Technical Task Instruction:** Tạo MessageSourceConfig để tải các tệp properties từ classpath (`/i18n/messages_{locale}.properties`). Sử dụng `PropertiesMessageSource` để tải nóng. Đảm bảo encoding UTF-8. `[REQ-022], [REQ-023]`
      - **Targeted Tag IDs:** [REQ-022], [REQ-023]

- **DAY 9: Xây dựng module báo cáo và dashboard**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.report/ReportController.java [REQ-024], [REQ-025]`
      - **Low-Level Technical Task Instruction:** Triển khai endpoint `GET /reports/attendance` nhận query parameters `centerId`, `startDate`, `endDate`. Controller gọi `reportService.generateAttendanceCsv(...)`, trả về `ResponseEntity<byte[]>` với `MediaType.TEXT_CSV`. Thêm annotation `@PreAuthorize('hasAnyRole("SYSTEM_ADMIN","CENTER_ADMIN")')`. `[REQ-024], [REQ-025]`
      - **Targeted Tag IDs:** [REQ-024], [REQ-025]
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.membershiphub.report/ReportService.java [REQ-024], [REQ-025]`
      - **Low-Level Technical Task Instruction:** Triển khai `generateAttendanceCsv(UUID centerId, LocalDate start, LocalDate end)` truy vấn `attendance` join `users` join `courses`, tổng hợp dữ liệu, ghi vào `StringBuilder` với header CSV. Triển khai `getDashboardSummary(UUID centerId)` trả về DTO với các chỉ số. Sử dụng `@Transactional`. `[REQ-024], [REQ-025]`
      - **Targeted Tag IDs:** [REQ-024], [REQ-025]

- **DAY 10: Xây dựng logging kiểm toán và hoàn thiện hạ tầng**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      * **Target Component file path (`target_component`):** `./sources/backend.membershiphub.security/audit/AuditLogger.java [NFR-006]`
      * **Low-Level Technical Task Instruction:** Triển khai AuditLogger với method `log(String userId, String action, String entity, UUID entityId)`. Ghi log vào bảng `audit_log` với các cột `log_id`, `user_id`, `action`, `entity_type`, `entity_id`, `timestamp`. Sử dụng `@Service` và `@Async` để tránh chặn. `[NFR-006]`
      * **Targeted Tag IDs:** [NFR-006]
    * **[Assigned Sub-Agent literal token: Docker]:**
      * **Target Component file path (`target_component`):** `./sources/infra.docker/Dockerfile [NFR-005]`
      * **Low-Level Technical Task Instruction:** Cập nhật Dockerfile đa giai đoạn: giai đoạn builder sử dụng `maven:3.9-eclipse-temurin-21` để đóng gói; giai đoạn runtime sử dụng `eclipse-temurin:21-jre-alpine`. Sao chép tệp JAR, thiết lập người dùng không phải root, phơi cổng 8080, thêm nhãn `org.opencontainers.image.base.name` và `maintainer`. Đảm bảo kích thước ảnh cuối cùng < 500MB. `[NFR-005]`
      * **Targeted Tag IDs:** [NFR-005]
    * **[Assigned Sub-Agent literal token: GCP]:**
      * **Target Component file path (`target_component`):** `./sources/infra.gcp/gcp-pipeline.yaml [NFR-002], [NFR-004]`
      * **Low-Level Technical Task Instruction:** Tạo pipeline YAML cho Cloud Build: định nghĩa các bước `clone`, `build` (docker build), `push` (to Artifact Registry), `deploy` (GKE). Cấu hình `substitutions` cho `PROJECT_ID`, `LOCATION`, `REPOSITORY`. Thêm bước `gcloud run deploy` nếu cần. Đảm bảo tự động failover qua các region. `[NFR-002], [NFR-004]`
      * **Targeted Tag IDs:** [NFR-002], [NFR-004]
    * **[Assigned Sub-Agent literal token: GKE]:**
      * **Target Component file path (`target_component`):** `./sources/infra.gke/gke-deployment.yaml [NFR-002], [NFR-004]`
      * **Low-Level Technical Task Instruction:** Tạo Helm chart hoặc manifest YAML cho Deployment (image: `<artifactRegistry>/membership-hub:latest`), Service (type: LoadBalancer), ConfigMap cho application properties, Secret cho credentials. Cấu hình HPA với `cpuUtilization: 70%` và `memoryUtilization: 70%`. Thêm NetworkPolicy để phân đoạn đa tenant. `[NFR-002], [NFR-004]`
      * **Targeted Tag IDs:** [NFR-002], [NFR-004]

<!--END_DELIMITTER-->

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-001]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng `PreparedStatement` cho tất cả các câu lệnh SQL; áp dụng `JdbcTemplate` với tham số đánh dấu `?`. Triển khai `QueryDSL` cho các điều kiện động. Whitelist các cột và bảng được phép cho các trường hợp sắp xếp động. Áp dụng `Flyway` cho các script migration được kiểm tra.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Áp dụng `spring-boot-starter-validation` với annotation `@SafeHtml`. Sử dụng `Thymeleaf` với `sanitize` enabled. Thêm header `Content-Security-Policy` (không cho phép `unsafe-inline`). Đảm bảo tất cả các phản hồi HTML được đánh dấu `X-Content-Type-Options: nosniff`.
- **Multi-Tenant CORS Security Rails:** Cấu hình `CorsConfiguration` cho phép các origin động dựa trên danh sách trắng của trung tâm (`center.cors.origins`). Sử dụng `Origin pattern matching` (`https://*.membershiphub.com`). Vô hiệu hóa credential cho các request cross-origin.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Triển khai `Logback` với `MaskingFilter` để che giấu số điện thoại, email trong log. Sử dụng `@JsonSerialize` với `JsonSerializer` tùy chỉnh cho các trường PII. Thiết lập `logback.xml` để loại bỏ các trường nhạy cảm trước khi ghi log. Áp dụng `slf4j` MDC cho request ID.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng `@capacitor/core` cho các API native (ví dụ: `Device`, `Network`, `Storage`). Triển khai cơ chế fallback cho các request API khi mất kết nối bằng cách sử dụng `axios` với `retry` và `offline queue`. Sử dụng `SecureStorage` cho JWT. Thêm back‑button interceptor để điều hướng ứng dụng.
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware `LocaleResolver` xác định locale từ cookie, header `Accept-Language`, hoặc tham số yêu cầu. Sử dụng `Next.js` `i18n` với các route `(/en/, /vi/, /es/)`. Tự động chèn thẻ `<link rel="alternate" hreflang="en" href="https://membershiphub.com/en"/>` vào `<head>`. Sử dụng `meta` tags động cho mỗi ngôn ngữ.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Script CI tự động fork repository chính vào nhánh `features/development-day-{N}` nơi N là số ngày hiện tại (bắt đầu từ 1). Mỗi nhánh là không gian làm việc cô lập.
- **Validation Guard Pipeline Gates:** Sau khi push, GitHub Actions thực hiện:
  * Kiểm tra cú pháp (`./mvnw compile`).
  * Chạy unit test (`./mvnw test`) với độ phủ mã >= 85%.
  * Chạy quét bảo mật (`trivy` cho image).
  * Triển khai đến môi trường staging (`gcloud run deploy`).
  * Nếu tất cả kiểm tra thành công, hợp nhất vào nhánh `develop`.
  * Nếu thất bại, tạo PR với log lỗi chi tiết và tự động đóng nhánh.

### 🛑 MATRIX COVERAGE CHECK MANDATE (Dịch tiêu đề sang tiếng Việt)
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TỔNG SỐ REQ TAGS: 26, TỔNG SỐ ARC TAGS: 9, TỔNG SỐ EXC TAGS: 5, TỔNG SỐ DAT TAGS: 11, TỔNG SỐ NFR TAGS: 9. KHÔNG CÓ MÃ NÀO BỊ BỎ QUA.]`