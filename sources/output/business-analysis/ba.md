# SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub

## 1. PROJECT OVERVIEW & GLOBAL ARCHITECTURE

### 1.1 Mục tiêu sản phẩm & Giá trị cốt lõi
- Cung cấp một nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực thông qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, mobile, nhóm Zalo).
- Các giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### 1.2 Nhóm người dùng mục tiêu
- Quản trị viên hệ thống (super‑user toàn cầu)
- Quản trị viên trung tâm (quản lý cấp trung tâm)
- Quản lý (phụ trách, quyền hạn giới hạn)
- Giáo viên (chỉ đọc lịch học)
- Học viên (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Người dùng ứng dụng di động (cùng các vai trò trên, giao diện đáp ứng)

### 1.3 Ma trận RBAC toàn cầu
- [ARC-001] Quản trị viên hệ thống: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Quản trị viên trung tâm: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Quản lý: có thể tạo thông báo, quản lý học viên, chỉ định học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Giáo viên: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Học viên: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày hiệu lực còn lại), gia hạn thẻ.

### 1.4 Kiến trúc công nghệ & hạ tầng [ARC-010]
- Frontend web: Next.js (React) với SSR, hỗ trợ đa ngôn ngữ (i18n).
- Frontend di động: React Native (iOS/Android) tích hợp với Firebase Authentication, FCM, máy quét QR.
- Backend services: Quarkus (Java) exposing RESTful APIs, tích hợp JWT, OAuth2.
- Message broker: RabbitMQ / Apache Kafka cho hàng đợi thông báo.
- Database: PostgreSQL với read replicas, sharding theo trung tâm để đảm bảo cô lập đa租.
- Containerization: Docker với image size < 500 MB, base image < 200 MB.
- Orchestration: Kubernetes (GKE) với HPA dựa trên CPU > 70% hoặc độ trễ > 300 ms.
- API Gateway: Kong / AWS API GW với rate limiting, throttling.
- Security: TLS 1.3, mã hóa AES‑256 tại chỗ, JWT access token 15 phút, refresh token 7 ngày.
- CI/CD: GitLab CI, triển khai blue‑green, kiểm tra tự động, quét bảo mật (OWASP).
- Giám sát: Prometheus + Grafana, Loki cho logging, distributed tracing (Jaeger).

## 2. MODULES CHỨC NĂNG NÂNG CAO

### 2.1 Quản lý người dùng

#### 2.1.1 [REQ-001] Đăng ký người dùng
**Mô tả:** As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.

**Tiêu chí chấp nhận:**
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. *[REQ-001]*

**Xác thực dữ liệu đầu vào:**
- Email: bắt buộc, tối đa 255 ký tự, phải chứa đúng một ký tự ‘@’ và phần miền hợp lệ (ví dụ: user@example.com). Phải là duy nhất.
- Password: bắt buộc, tối thiểu 8 ký tự, ít nhất một chữ hoa, một chữ thường, một chữ số, một ký tự đặc biệt.
- Terms: bắt buộc checkbox đồng ý.

#### 2.1.2 [REQ-002] Xác thực xã hội
**Mô tả:** As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.

**Tiêu chí chấp nhận:**
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. *[REQ-002]*

**Xác thực dữ liệu đầu vào:**
- Token nhà cung cấp, tùy chọn ảnh đại diện.

#### 2.1.3 [REQ-003] Phân quyền người dùng
**Mô tả:** As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

**Tiêu chí chấp nhận:**
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. *[REQ-003]*

**Xác thực dữ liệu đầu vào:**
- Dropdown vai trò, yêu cầu ghi log kiểm toán.

#### 2.1.4 Từ điển dữ liệu mô-đun (người dùng)
- **[DAT-001] Bảng USERS**
  - `uuid user_id` PK "Primary key"
  - `varchar email` "NOT NULL, UNIQUE"
  - `char password_hash` "NOT NULL"
  - `varchar full_name` "NOT NULL"
  - `smallint role_id` FK "FK → ROLES.role_id"
  - `varchar provider` "DEFAULT 'local'"
  - `timestamp created_at` "NOT NULL, DEFAULT now()"
  - `timestamp updated_at` "NOT NULL, DEFAULT now()"

  **Mermaid erDiagram:**
  ```
  erDiagram
      USERS {
          uuid user_id PK "Primary key"
          varchar email "NOT NULL, UNIQUE"
          char password_hash "NOT NULL"
          varchar full_name "NOT NULL"
          smallint role_id "FK → ROLES.role_id"
          varchar provider "DEFAULT 'local'"
          timestamp created_at "NOT NULL, DEFAULT now()"
          timestamp updated_at "NOT NULL, DEFAULT now()"
      }
  ```

- **[DAT-008] Bảng ROLES**
  - `smallint role_id` PK "Primary key"
  - `varchar name` "UNIQUE, NOT NULL"
  - `varchar description` "Optional"

  **Mermaid erDiagram:**
  ```
  erDiagram
      ROLES {
          smallint role_id PK "Primary key"
          varchar name "UNIQUE, NOT NULL"
          varchar description "Optional"
      }
  ```

### 2.2 Quản lý trung tâm

#### 2.2.1 [REQ-004] Xem danh sách trung tâm
**Mô tả:** As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.

**Tiêu chí chấp nhận:**
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. *[REQ-004]*

**Xác thực dữ liệu đầu vào:** Không (chỉ đọc).

#### 2.2.2 [REQ-005] Tạo/Cập nhật/Xóa trung tâm
**Mô tả:** As a System Admin, I want to add, edit, or remove a center record so that center information stays current.

**Tiêu chí chấp nhận:**
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. *[REQ-005]*

**Xác thực dữ liệu đầu vào:**
- Name: bắt buộc, tối đa 100 ký tự.
- Address: bắt buộc, tối đa 255 ký tự.
- TaxID: bắt buộc, numeric, 10‑13 chữ số, duy nhất.
- Contact Phone: tùy chọn, cho phép +, chữ số, khoảng trắng, dấu gạch ngang, dấu ngoặc.
- Contact Email: tùy chọn, phải là định dạng email hợp lệ.

#### 2.2.3 [REQ-006] Chỉ định quản trị viên trung tâm
**Mô tả:** As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

**Tiêu chí chấp nhận:**
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. *[REQ-006]*

**Xác thực dữ liệu đầu vào:** User ID, Center ID.

#### 2.2.4 Từ điển dữ liệu mô-đun (trung tâm)
- **[DAT-002] Bảng CENTERS**
  - `uuid center_id` PK "Primary key"
  - `varchar name` "NOT NULL"
  - `varchar address` "NOT NULL"
  - `varchar tax_id` "UNIQUE, NOT NULL"
  - `varchar contact_phone` "Optional"
  - `varchar contact_email` "Optional"

  **Mermaid erDiagram:**
  ```
  erDiagram
      CENTERS {
          uuid center_id PK "Primary key"
          varchar name "NOT NULL"
          varchar address "NOT NULL"
          varchar tax_id "UNIQUE, NOT NULL"
          varchar contact_phone "Optional"
          varchar contact_email "Optional"
      }
  ```

### 2.3 Quản lý khóa học

#### 2.3.1 [REQ-007] Xem danh sách khóa học
**Mô tả:** As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.

**Tiêu chí chấp nhận:**
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. *[REQ-007]*

**Xác thực dữ liệu đầu vào:** Không.

#### 2.3.2 [REQ-008] Tạo/Cập nhật/Xóa khóa học (tránh xung đột)
**Mô tả:** As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.

**Tiêu chí chấp nhận:**
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. *[REQ-008]*

**Xác thực dữ liệu đầu vào:**
- Title: bắt buộc, tối đa 150 ký tự.
- StartDate/EndDate: bắt buộc, EndDate >= StartDate.
- TeacherID: bắt buộc, khóa ngoại.
- Logic kiểm tra chồng chéo được thực hiện ở DB/trigger level.

#### 2.3.3 [REQ-009] Chỉ định giáo viên vào khóa học
**Mô tả:** As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

**Tiêu chí chấp nhận:**
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. *[REQ-009]*

**Xác thực dữ liệu đầu vào:** CourseID, TeacherID (phải tồn tại).

#### 2.3.4 Từ điển dữ liệu mô-đun (khóa học)
- **[DAT-003] Bảng COURSES**
  - `uuid course_id` PK "Primary key"
  - `varchar title` "NOT NULL"
  - `text description` "Optional"
  - `date start_date` "NOT NULL"
  - `date end_date` "NOT NULL"
  - `uuid teacher_id` FK "FK → USERS.user_id"
  - `int max_students` "DEFAULT 30"

  **Mermaid erDiagram:**
  ```
  erDiagram
      COURSES {
          uuid course_id PK "Primary key"
          varchar title "NOT NULL"
          text description "Optional"
          date start_date "NOT NULL"
          date end_date "NOT NULL"
          uuid teacher_id "FK → USERS.user_id"
          int max_students "DEFAULT 30"
      }
  ```

### 2.4 Đăng ký & Ghi danh học viên

#### 2.4.1 [REQ-010] Duyệt khóa học
**Mô tả:** As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.

**Tiêu chí chấp nhận:**
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. *[REQ-010]*

**Xác thực dữ liệu đầu vào:** Không.

#### 2.4.2 [REQ-011] Đăng ký khóa học
**Mô tả:** As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

**Tiêu chí chấp nhận:**
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. *[REQ-011]*

**Xác thực dữ liệu đầu vào:**
- CourseID: bắt buộc, phải là khóa học đang hoạt động.
- StudentID: được suy ra từ token xác thực (hoặc tạo trên‑the‑fly).

#### 2.4.3 Từ điển dữ liệu mô-đun (ghi danh)
- **[DAT-004] Bảng ENROLLMENTS**
  - `uuid enrollment_id` PK "Primary key"
  - `uuid student_id` FK "FK → USERS.user_id"
  - `uuid course_id` FK "FK → COURSES.course_id"
  - `timestamp enrollment_date` "DEFAULT now()"

  **Mermaid erDiagram:**
  ```
  erDiagram
      ENROLLMENTS {
          uuid enrollment_id PK "Primary key"
          uuid student_id "FK → USERS.user_id"
          uuid course_id "FK → COURSES.course_id"
          timestamp enrollment_date "DEFAULT now()"
      }
  USERS ||--o{ ENROLLMENTS : student_id
  COURSES ||--o{ ENROLLMENTS : course_id
  ```

### 2.5 Điểm danh & Quét QR

#### 2.5.1 [REQ-012] Chụp điểm danh QR
**Mô tả:** As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.

**Tiêu chí chấp nhận:**
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. *[REQ-012]*

**Xác thực dữ liệu đầu vào:**
- QR payload: chuỗi base64 chứa studentID và courseID.
- Validation: học viên phải ghi danh vào khóa học trong ngày.

#### 2.5.2 [REQ-013] Tính chất không lặp lại của điểm danh
**Mô tả:** The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

**Tiêu chí chấp nhận:**
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. *[REQ-013]*

**Xác thực dữ liệu đầu vào:** Khóa chính tổng hợp (StudentID, CourseID, Date).

#### 2.5.3 Từ điển dữ liệu mô-đun (điểm danh)
- **[DAT-005] Bảng ATTENDANCE**
  - `uuid attendance_id` PK "Primary key"
  - `uuid student_id` FK "FK → USERS.user_id"
  - `uuid course_id` FK "FK → COURSES.course_id"
  - `date attendance_date` "NOT NULL"
  - `timestamp timestamp` "DEFAULT now()"

  **Mermaid erDiagram:**
  ```
  erDiagram
      ATTENDANCE {
          uuid attendance_id PK "Primary key"
          uuid student_id "FK → USERS.user_id"
          uuid course_id "FK → COURSES.course_id"
          date attendance_date "NOT NULL"
          timestamp timestamp "DEFAULT now()"
      }
  USERS ||--o{ ATTENDANCE : student_id
  COURSES ||--o{ ATTENDANCE : course_id
  ```

#### 2.5.4 Luồng ngoại lệ mô-đun (QR điểm danh)
- **[EXC-001]** Network & Connectivity Drops During QR Scan:
  - If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.

- **[EXC-002]** Duplicate Attendance Submission:
  - If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

### 2.6 Quản lý thẻ hội viên

#### 2.6.1 [REQ-014] Hiển thị hiệu lực thẻ
**Mô tả:** As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.

**Tiêu chí chấp nhận:**
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. *[REQ-014]*

**Xác thực dữ liệu đầu vào:** Không (chỉ đọc).

#### 2.6.2 [REQ-015] Gia hạn thẻ
**Mô tả:** As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

**Tiêu chí chấp nhận:**
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. *[REQ-015]*

**Xác thực dữ liệu đầu vào:**
- RenewalDays: integer, 1‑365.
- Tích hợp cổng thanh toán (ngoài phạm vi).

#### 2.6.3 Từ điển dữ liệu mô-đun (thẻ hội viên)
- **[DAT-006] Bảng STUDENTCARDS**
  - `uuid card_id` PK "Primary key"
  - `uuid student_id` FK "FK → USERS.user_id"
  - `date issue_date` "NOT NULL"
  - `int validity_days` "NOT NULL"
  - `int remaining_days` "computed"

  **Mermaid erDiagram:**
  ```
  erDiagram
      STUDENTCARDS {
          uuid card_id PK "Primary key"
          uuid student_id "FK → USERS.user_id"
          date issue_date "NOT NULL"
          int validity_days "NOT NULL"
          int remaining_days "computed"
      }
  USERS ||--o{ STUDENTCARDS : student_id
  ```

### 2.7 Thông báo & Truyền thông

#### 2.7.1 [REQ-016] Kích hoạt thông báo
**Mô tả:** When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

**Tiêu chí chấp nhận:**
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. *[REQ-016]*

**Xác thực dữ liệu đầu vào:** Đối tượng mục tiêu (học viên, giáo viên, nhóm), nội dung tin nhắn, tùy chọn media.

#### 2.7.2 Từ điển dữ liệu mô-đun (thông báo)
- **[DAT-007] Bảng NOTIFICATIONS**
  - `uuid notification_id` PK "Primary key"
  - `uuid user_id` FK "FK → USERS.user_id (optional)"
  - `varchar group_zalo` "optional"
  - `text message` "NOT NULL"
  - `timestamp sent_at` "DEFAULT now()"
  - `boolean delivered` "DEFAULT false"

  **Mermaid erDiagram:**
  ```
  erDiagram
      NOTIFICATIONS {
          uuid notification_id PK "Primary key"
          uuid user_id "FK → USERS.user_id (optional)"
          varchar group_zalo "optional"
          text message "NOT NULL"
          timestamp sent_at "DEFAULT now()"
          boolean delivered "DEFAULT false"
      }
  USERS ||--o{ NOTIFICATIONS : user_id
  ```

#### 2.7.3 Ngoại lệ mô-đun (thông báo)
- **[EXC-003]** Failed Notification Delivery:
  - When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

### 2.8 Quản lý khuyến mãi & thông báo

#### 2.8.1 [REQ-017] Quản lý khuyến mãi
**Mô tả:** As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.

**Tiêu chí chấp nhận:**
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. *[REQ-017]*

**Xác thực dữ liệu đầu vào:**
- Name: bắt buộc, tối đa 100 ký tự.
- StartDate/EndDate: tùy chọn, định dạng YYYY‑MM‑DD.
- Description: tối đa 500 ký tự.

#### 2.8.2 [REQ-018] Quản lý thông báo
**Mô tả:** As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

**Tiêu chí chấp nhận:**
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. *[REQ-018]*

**Xác thực dữ liệu đầu vào:**
- Title: bắt buộc, tối đa 150 ký tự.
- Content: bắt buộc, tối đa 2000 ký tự.

#### 2.8.3 Từ điển dữ liệu mô-đun (khuyến mãi)
- **[DAT-009] Bảng PROMOTIONS**
  - `uuid promo_id` PK "Primary key"
  - `varchar code` "UNIQUE"
  - `smallint discount_percent` "NOT NULL"
  - `date start_date` "optional"
  - `date end_date` "optional"
  - `text description` "optional"

  **Mermaid erDiagram:**
  ```
  erDiagram
      PROMOTIONS {
          uuid promo_id PK "Primary key"
          varchar code "UNIQUE"
          smallint discount_percent "NOT NULL"
          date start_date "optional"
          date end_date "optional"
          text description "optional"
      }
  ```

#### 2.8.4 Từ điển dữ liệu mô-đun (thông báo)
- **[DAT-010] BẢNG ANNOUNCEMENTS**
  - `uuid announcement_id` PK "Primary key"
  - `varchar title` "NOT NULL"
  - `text content` "NOT NULL"
  - `date start_date` "optional"
  - `date end_date` "optional"

  **Mermaid erDiagram:**
  ```
  erDiagram
      ANNOUNCEMENTS {
          uuid announcement_id PK "Primary key"
          varchar title "NOT NULL"
          text content "NOT NULL"
          date start_date "optional"
          date end_date "optional"
      }
  ```

### 2.9 Chatbot dịch vụ khách hàng AI

#### 2.9.1 [REQ-019] Tích hợp chatbot AI
**Mô tả:** As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

**Tiêu chí chấp nhận:**
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. *[REQ-019]*

**Xác thực dữ liệu đầu vào:** Văn bản đầu vào, timeout phiên.

### 2.10 Tính năng cốt lõi ứng dụng di động

#### 2.10.1 [REQ-020] Giao diện người dùng cụ thể theo vai trò trên di động
**Mô tả:** As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).

**Tiêu chí chấp nhận:**
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. *[REQ-020]*

**Xác thực dữ liệu đầu vào:** Không.

#### 2.10.2 [REQ-021] Đẩy thông báo trên di động
**Mô tả:** As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

**Tiêu chí chấp nhận:**
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. *[REQ-021]*

**Xác thực dữ liệu đầu vào:** DeviceToken, Platform (iOS/Android).

### 2.11 Bản địa hóa & SEO

#### 2.11.1 [REQ-022] Phát hiện ngôn ngữ mặc định
**Mô tả:** As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.

**Tiêu chí chấp nhận:**
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. *[REQ-022]*

**Xác thực dữ liệu đầu vào:** Không.

#### 2.11.2 [REQ-023] SEO đa ngôn ngữ
**Mô tả:** The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

**Tiêu chí chấp nhận:**
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. *[REQ-023]*

**Xác thực dữ liệu đầu vào:** Mã ngôn ngữ (en, vi, es).

### 2.12 Báo cáo & Phân tích

#### 2.12.1 [REQ-024] Tạo báo cáo điểm danh
**Mô tả:** As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.

**Tiêu chí chấp nhận:**
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. *[REQ-024]*

**Xác thực dữ liệu đầu vào:**
- Date range: start ≤ end, max 30 days.

#### 2.12.2 [REQ-025] Bảng điều khiển tóm tắt ghi danh
**Mô tả:** As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

**Tiêu chí chấp nhận:**
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). *[REQ-025]*

**Xác thực dữ liệu đầu vào:** Khoảng thời gian làm mới (mặc định 15 phút).

### 2.13 Ngoại lệ & Xử lý lỗi toàn cục

#### 2.13.1 [EXC-004] Xác thực đầu vào không hợp lệ
- If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.

#### 2.13.2 [EXC-005] Khôi phục hệ thống sau sự cố
- If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

## 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- **[NFR-001]** Performance Metrics:
  - Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency.
  - Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.

- **[NFR-002]** Availability:
  - Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.

- **[NFR-003]** Security:
  - All data in transit must use TLS 1.3; at rest encryption with AES‑256.
  - JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry.
  - Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).

- **[NFR-004]** Scalability & High Availability:
  - Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms.
  - PostgreSQL read replicas for reporting workloads.

- **[NFR-005]** Docker Image Size:
  - Base image size < 200 MB; final image < 500 MB.

- **[NFR-006]** Logging & Audit:
  - All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.

- **[NFR-007]** Hỗ trợ đa ngôn ngữ:
  - Chuỗi UI phải được ngoại hóa; hỗ trợ tiếng Anh, tiếng Việt, tiếng Tây Ban Nha; chuyển đổi ngôn ngữ mà không tải lại trang khi có thể.

- **[NFR-008]** Tuân thủ GDPR/CCPA:
  - Xóa dữ liệu cá nhân theo yêu cầu của người dùng; xuất dữ liệu ở định dạng JSON; quản lý sự đồng ý cho truyền thông tiếp thị.

- **[NFR-009]** Sao lưu & Khôi phục thảm họa:
  - Sao lưu PostgreSQL hàng ngày đầy đủ; khôi phục điểm trong thời gian lên đến 24 giờ; sao lưu cụm GKE sang khu vực riêng biệt.

## 4. LUỒNG KIẾN TRÚC TOÀN CẦU

- **[ARC-006]** Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token có hiệu lực 15 phút và refresh token.
- **[ARC-007]** Luồng xử lý QR điểm danh: ứng dụng di động quét QR, gửi studentID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách duy nhất.
- **[ARC-008]** Luồng truyền thông: hệ thống kích hoạt push notifications đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, chỉ định khóa học, cảnh báo điểm danh.
- **[ARC-009]** Luồng tích hợp ứng dụng di động: Frontend Next.js tiêu thụ các REST API; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối hạn chế.

---

[EXECUTION_REMEDIATION_PAYLOAD_START]
{
  "technical_codename": "membership-hub",
  "descriptive_name": "Membership Hub Platform",
  "brand_name": "EduHub",
  "requirement_tags": [
    "[REQ-001]",
    "[REQ-002]",
    "[REQ-003]",
    "[REQ-004]",
    "[REQ-005]",
    "[REQ-006]",
    "[REQ-007]",
    "[REQ-008]",
    "[REQ-009]",
    "[REQ-010]",
    "[REQ-011]",
    "[REQ-012]",
    "[REQ-013]",
    "[REQ-014]",
    "[REQ-015]",
    "[REQ-016]",
    "[REQ-017]",
    "[REQ-018]",
    "[REQ-019]",
    "[REQ-020]",
    "[REQ-021]",
    "[REQ-022]",
    "[REQ-023]",
    "[REQ-024]",
    "[REQ-025]",
    "[EXC-001]",
    "[EXC-002]",
    "[EXC-003]",
    "[EXC-004]",
    "[EXC-005]",
    "[ARC-001]",
    "[ARC-002]",
    "[ARC-003]",
    "[ARC-004]",
    "[ARC-005]",
    "[ARC-006]",
    "[ARC-007]",
    "[ARC-008]",
    "[ARC-009]",
    "[ARC-010]",
    "[NFR-001]",
    "[NFR-002]",
    "[NFR-003]",
    "[NFR-004]",
    "[NFR-005]",
    "[NFR-006]",
    "[NFR-007]",
    "[NFR-008]",
    "[NFR-009]",
    "[DAT-001]",
    "[DAT-002]",
    "[DAT-003]",
    "[DAT-004]",
    "[DAT-005]",
    "[DAT-006]",
    "[DAT-007]",
    "[DAT-008]",
    "[DAT-009]",
    "[DAT-010]",
    "[DAT-011]"
  ]
}