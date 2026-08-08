# AI Model: llama-3.3-70b-versatile - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below:

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
<!--END_BACKLOG_SYNOPSIS_GRID-->

- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly categorized into:
  1. Core Application Features: Functional endpoint creations, database models, and service layer code blocks.
  2. Enterprise Technical Documentation: Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. DevOps Infrastructure Pipelines: Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution log inside Section 5 for that specific phase.

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
###### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
</PHASE_TEMPLATE_LOOP>

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  
  ########## SUB-TASK [Z]: SHORT SPECIFIC SUB-TASK TITLE
  * Sub-Agent Workflow Specialization: <RULE>You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.</RULE>
  * Targeted Tag IDs: <RULE>Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].</RULE>
  * Target Component file path (target_component): <RULE>Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.</RULE>
  * Low-Level Technical Task Instruction: <RULE>Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.</RULE>

  ## DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
  * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
    </RULE>
  * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
    </RULE>
  * **Phase Localized Exception Handlers [EXC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
    </RULE>

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

# System Instruction

You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Requested 20307, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 92, in generate_global_context
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Requested 20307, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
"]

# AI Model: meta-llama/llama-3.3-70b-instruct:free - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below:

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
<!--END_BACKLOG_SYNOPSIS_GRID-->

- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly categorized into:
  1. Core Application Features: Functional endpoint creations, database models, and service layer code blocks.
  2. Enterprise Technical Documentation: Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. DevOps Infrastructure Pipelines: Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution log inside Section 5 for that specific phase.

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
###### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
</PHASE_TEMPLATE_LOOP>

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  
  ########## SUB-TASK [Z]: SHORT SPECIFIC SUB-TASK TITLE
  * Sub-Agent Workflow Specialization: <RULE>You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.</RULE>
  * Targeted Tag IDs: <RULE>Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].</RULE>
  * Target Component file path (target_component): <RULE>Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.</RULE>
  * Low-Level Technical Task Instruction: <RULE>Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.</RULE>

  ## DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
  * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
    </RULE>
  * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
    </RULE>
  * **Phase Localized Exception Handlers [EXC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
    </RULE>

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

# System Instruction

You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 92, in generate_global_context
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.NotFoundError: Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: meta-llama/llama-3.3-70b-instruct - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below:

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
<!--END_BACKLOG_SYNOPSIS_GRID-->

- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly categorized into:
  1. Core Application Features: Functional endpoint creations, database models, and service layer code blocks.
  2. Enterprise Technical Documentation: Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. DevOps Infrastructure Pipelines: Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution log inside Section 5 for that specific phase.

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
###### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
</PHASE_TEMPLATE_LOOP>

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  
  ########## SUB-TASK [Z]: SHORT SPECIFIC SUB-TASK TITLE
  * Sub-Agent Workflow Specialization: <RULE>You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.</RULE>
  * Targeted Tag IDs: <RULE>Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].</RULE>
  * Target Component file path (target_component): <RULE>Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.</RULE>
  * Low-Level Technical Task Instruction: <RULE>Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.</RULE>

  ## DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
  * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
    </RULE>
  * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
    </RULE>
  * **Phase Localized Exception Handlers [EXC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
    </RULE>

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

# System Instruction

You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 6481 tokens, but can only afford 167. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 1177. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 8192 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 530. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 3072 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 477. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 2048 tokens, but can only afford 362. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 92, in generate_global_context
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 6481 tokens, but can only afford 167. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 1177. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 8192 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 530. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 3072 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 477. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 2048 tokens, but can only afford 362. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: qwen/qwen-2.5-coder-32b-instruct - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below:

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
<!--END_BACKLOG_SYNOPSIS_GRID-->

- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly categorized into:
  1. Core Application Features: Functional endpoint creations, database models, and service layer code blocks.
  2. Enterprise Technical Documentation: Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. DevOps Infrastructure Pipelines: Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution log inside Section 5 for that specific phase.

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
###### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
</PHASE_TEMPLATE_LOOP>

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  
  ########## SUB-TASK [Z]: SHORT SPECIFIC SUB-TASK TITLE
  * Sub-Agent Workflow Specialization: <RULE>You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.</RULE>
  * Targeted Tag IDs: <RULE>Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].</RULE>
  * Target Component file path (target_component): <RULE>Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.</RULE>
  * Low-Level Technical Task Instruction: <RULE>Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.</RULE>

  ## DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
  * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
    </RULE>
  * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
    </RULE>
  * **Phase Localized Exception Handlers [EXC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
    </RULE>

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

# System Instruction

You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 11797 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 92, in generate_global_context
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 11797 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: deepseek/deepseek-r1:free - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below:

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
<!--END_BACKLOG_SYNOPSIS_GRID-->

- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly categorized into:
  1. Core Application Features: Functional endpoint creations, database models, and service layer code blocks.
  2. Enterprise Technical Documentation: Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. DevOps Infrastructure Pipelines: Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution log inside Section 5 for that specific phase.

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
###### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
</PHASE_TEMPLATE_LOOP>

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  
  ########## SUB-TASK [Z]: SHORT SPECIFIC SUB-TASK TITLE
  * Sub-Agent Workflow Specialization: <RULE>You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.</RULE>
  * Targeted Tag IDs: <RULE>Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].</RULE>
  * Target Component file path (target_component): <RULE>Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.</RULE>
  * Low-Level Technical Task Instruction: <RULE>Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.</RULE>

  ## DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
  * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
    </RULE>
  * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
    </RULE>
  * **Phase Localized Exception Handlers [EXC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
    </RULE>

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

# System Instruction

You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: deepseek/deepseek-r1', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 92, in generate_global_context
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.NotFoundError: Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: deepseek/deepseek-r1', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: google/gemma-4-31b-instruct - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below:

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
<!--END_BACKLOG_SYNOPSIS_GRID-->

- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly categorized into:
  1. Core Application Features: Functional endpoint creations, database models, and service layer code blocks.
  2. Enterprise Technical Documentation: Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. DevOps Infrastructure Pipelines: Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution log inside Section 5 for that specific phase.

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
###### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
</PHASE_TEMPLATE_LOOP>

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  
  ########## SUB-TASK [Z]: SHORT SPECIFIC SUB-TASK TITLE
  * Sub-Agent Workflow Specialization: <RULE>You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.</RULE>
  * Targeted Tag IDs: <RULE>Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].</RULE>
  * Target Component file path (target_component): <RULE>Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.</RULE>
  * Low-Level Technical Task Instruction: <RULE>Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.</RULE>

  ## DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
  * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
    </RULE>
  * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
    </RULE>
  * **Phase Localized Exception Handlers [EXC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
    </RULE>

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

# System Instruction

You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 400 - {'error': {'message': 'google/gemma-4-31b-instruct is not a valid model ID', 'code': 400}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 92, in generate_global_context
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.BadRequestError: Error code: 400 - {'error': {'message': 'google/gemma-4-31b-instruct is not a valid model ID', 'code': 400}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: minimax/minimax-m3 - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below:

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
<!--END_BACKLOG_SYNOPSIS_GRID-->

- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly categorized into:
  1. Core Application Features: Functional endpoint creations, database models, and service layer code blocks.
  2. Enterprise Technical Documentation: Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. DevOps Infrastructure Pipelines: Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution log inside Section 5 for that specific phase.

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
###### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
</PHASE_TEMPLATE_LOOP>

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  
  ########## SUB-TASK [Z]: SHORT SPECIFIC SUB-TASK TITLE
  * Sub-Agent Workflow Specialization: <RULE>You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.</RULE>
  * Targeted Tag IDs: <RULE>Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].</RULE>
  * Target Component file path (target_component): <RULE>Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.</RULE>
  * Low-Level Technical Task Instruction: <RULE>Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.</RULE>

  ## DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
  * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
    </RULE>
  * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
    </RULE>
  * **Phase Localized Exception Handlers [EXC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
    </RULE>

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

# System Instruction

You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 392. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 342. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 92, in generate_global_context
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 392. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 342. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openai/gpt-5.3-codex - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below:

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
<!--END_BACKLOG_SYNOPSIS_GRID-->

- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly categorized into:
  1. Core Application Features: Functional endpoint creations, database models, and service layer code blocks.
  2. Enterprise Technical Documentation: Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. DevOps Infrastructure Pipelines: Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution log inside Section 5 for that specific phase.

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
###### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
</PHASE_TEMPLATE_LOOP>

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  
  ########## SUB-TASK [Z]: SHORT SPECIFIC SUB-TASK TITLE
  * Sub-Agent Workflow Specialization: <RULE>You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.</RULE>
  * Targeted Tag IDs: <RULE>Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].</RULE>
  * Target Component file path (target_component): <RULE>Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.</RULE>
  * Low-Level Technical Task Instruction: <RULE>Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.</RULE>

  ## DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
  * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
    </RULE>
  * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
    </RULE>
  * **Phase Localized Exception Handlers [EXC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
    </RULE>

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

# System Instruction

You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_global.py", line 92, in generate_global_context
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: cohere/north-mini-code:free - Global Prompt:

Analyze the attached project requirements. Build the GLOBAL PROJECT CONTEXT for Project 'membership-hub'.

--- RAW REQUIREMENTS ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
--- END REQUIREMENTS ---

## 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

######## 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
- Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
- You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
- Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
  * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
- Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

######## 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
- For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of 5 phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of 7 days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

######## 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
- Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
- You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

######## 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
- 💻 **Coder Agent Role**:
  * Core Duty: Pure Application Source Code Implementation.
  * Allowed Actions: Write, refactor, and implement structural logic in application files.
  * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
- 🧪 **Tester Agent Role**:
  * Core Duty: Test Suite Engineering and Validation.
  * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
  * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
- 🔍 **Reviewer Agent Role**:
  * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
  * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
- 📝 **Doc Agent Role**:
  * Core Duty: Enterprise Technical Document Writer.
  * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
- 🐳 **Docker Agent Role**:
  * Core Duty: Containerization and Package Registry Pushing.
  * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
- ☁️ **GCP Agent Role**:
  * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
  * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
- ☸️ **GKE Agent Role**:
  * Core Duty: Google Kubernetes Engine Workload Orchestration.
  * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

######## 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
- **Phase Boundary Count**: The total number of architectural phases MUST be exactly "5".
- **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "5" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "5" must receive a balanced subset of requirements.
- **Strict Day-Cap & Anti-Filler Rail**:
  * The maximum number of days within ANY single phase is strictly capped at: "7".
  * The actual number of days per phase can be LESS than or EQUAL to "7" (e.g., `actual_days <= max_days_per_phase`).
  * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
  * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

######## 🚨 CRITICAL FULL TRANSLATION MANDATE
- The target generation language for all human-readable outputs is permanently bound to: "🇻🇳 Vietnamese". Everything MUST be translated into 🇻🇳 Vietnamese, except for the explicit Technical English core tokens protected by system mandates.
- You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

######## 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "🇻🇳 Vietnamese"
- You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
- 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
  * All Section and Sub-section Headers (including entire header of ouput markdown report, example `GLOBAL PROJECT CONTEXT`) MUST be translated contextually.
  * Table Headers MUST be translated (e.g., in Vietnamese: `Phase` -> `Giai đoạn`, `Day Range` -> `Khoảng ngày`, `Component / Module Path` -> `Đường dẫn Cấu phần / Module`, `Deliverables Summary` -> `Tóm tắt Sản phẩm Bàn giao`, `Sub-Agent` -> `Sub-Agent`, `Targeted Tag IDs` -> `Tag IDs Mục tiêu`).
  * List Prefixes and Phase Titles MUST be translated (e.g., in Vietnamese: `Phase [X] Detailed Architectural Specification` -> `Đặc tả Kiến trúc Chi tiết Giai đoạn [X]`, `Phase Core Objective & Purpose` -> `Mục tiêu Cốt lõi & Mục đích của Giai đoạn`, `Target Physical Directory Matrix Map` -> `Ma trận Bản đồ Thư mục Vật lý Mục tiêu`, `Database Schema DDL SQL Specification` -> `Đặc tả DDL SQL Schema Cơ sở Dữ liệu`, `API and Event Routing Contracts` -> `Hợp đồng Định tuyến API và Sự kiện`).
- 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
  * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
  * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
  * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
  * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
- 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
  * All markdown syntax layout operators (`##`, `####`, `######`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
  * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `#### 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `#### 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
  * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
  * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
  * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
  * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
  * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
  * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
  * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
  * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.

###### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`:

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in 🇻🇳 Vietnamese while completely freezing all technical paths, tags, and block codes.
</RULE>

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated breakdown as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw data flow paths.
- You MUST render 100% of your newly generated sentences in the designated target language: Vietnamese.
</RULE>

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
<RULE>
- **STRICT BOUNDARY LOCKDOWN FOR PROPERTIES BLOCK:** Within the generated properties code fence, you MUST execute the complete physical destruction of the placeholder square brackets. The output values MUST be clean literal boolean raw values without any enclosing markers to prevent downstream parsing panics.
</RULE>
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true_or_false_literal_only
BACKEND_LAYER_REQUIRED=true_or_false_literal_only
FRONTEND_LAYER_REQUIRED=true_or_false_literal_only
MOBILE_LAYER_REQUIRED=true_or_false_literal_only
DEVOPS_LAYER_REQUIRED=true_or_false_literal_only
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

###### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
- You MUST generate a comprehensive, unified Master Product Backlog table directly under this section before organizing the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project scope.
- The Master Product Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below:

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
<!--END_BACKLOG_SYNOPSIS_GRID-->

- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This master table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly categorized into:
  1. Core Application Features: Functional endpoint creations, database models, and service layer code blocks.
  2. Enterprise Technical Documentation: Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. DevOps Infrastructure Pipelines: Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **MANDATORY CASCADE PLAN COMPLIANCE:** Every task documented in this Master Backlog table MUST cascade symmetrically downwards: it MUST be distributed into exactly one targeted phase in the Synopsis Grid under Section 4.2, and subsequently possess an explicit, standalone daily execution log inside Section 5 for that specific phase.

###### 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.
- LOCAL DAY RANGE BOUNDARY: In the "Day Range" column of this table, you MUST format the day sequence starting from relative integer 1 for EACH individual phase row (e.g., Phase 1: Day 1 - 2, Phase 2: Day 1 - 2). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
- DYNAMIC TECHNICAL DENSITY PRICING LAW (Project-Agnostic): Each row's "Day Range" MUST be computed dynamically based strictly on the actual volume and density of the allocated Tag IDs for that specific phase. You MUST evaluate the capacity weight: a single calculated operational calendar day log inside Section 5 MUST NOT contain more than 3 unique critical requirement tags (REQ/ARC/NFR) combined. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (Section 4) Markdown table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens <!--START_PHASE_SYNOPSIS_GRID--> and <!--END_PHASE_SYNOPSIS_GRID-->.
- DYNAMIC DAY TITLE ENFORCEMENT: Inside Section 5, for every chronological day element (e.g., - **Day [Y]**:), you ARE PERMANENTLY FORBIDDEN from outputting static placeholder strings like "SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY". You MUST dynamically analyze the requirements for that day, compile a concise technical objective sentence, and fully translate it into the target language requested by the parameters.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across 5 without any artificial padding or redundant agent forcing:
  1. Dynamic Resource Allocation Rule: A sub-agent ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in the Section 4.2 table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps agents MUST be completely omitted from that specific row.
  2. Strict 1:1 Plan Symmetry Guardrail: If a sub-agent token is actively triggered and listed under the 'Assigned Sub-Agent' column for a phase in Section 4.2, you MUST guarantee that the same agent possesses at least one explicit, standalone technical task block inside Section 5 for that phase. Unassigned agents in Section 4.2 MUST NOT possess any tasks in Section 5.
  3. Hard Phase & Timeline Ceilings: The plan MUST split into exactly 5 phases, and no phase timeline block inside Section 5 shall exceed 7 calendar days.
  4. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
  5. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
  1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
  2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
  3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
  4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (```) for inner specifications (such as ```sql:matrix or ```json) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- ABSOLUTE DISCRETE SUB-TASK SEPARATION MANDATE: You ARE PERMANENTLY FORBIDDEN from aggregating or grouping distinct agent actions into a single combined description block or combined agent field. Every day log inside Section 5 MUST expand into an array of isolated, independent sub-task items, where each sub-task is exclusively mapped to exactly one naked sub-agent persona token.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column for every phase row:
  1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
  2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- ABSOLUTE ARCHITECTURAL PLAN SYMMETRY MANDATE (ANTI-DESYNC): You MUST enforce strict 1:1 deterministic alignment between the global macro-plan in Section 4.2 (<!--START_PHASE_SYNOPSIS_GRID-->) and the granular micro-logs in Section 5. It is a critical system violation to declare sub-agents in the synopsis table row while leaving them with zero execution tasks in the corresponding daily breakdown.
- DETERMINISTIC DISTRIBUTION PATTERN PER PHASE: For 100% of the phases generated, if a sub-agent token ([Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) is registered under the 'Assigned Sub-Agent' column in Section 4.2, you MUST partition the phase timeline chunk so that EVERY listed agent possesses at least one explicit, standalone, independent technical sub-task block inside Section 5 for that specific phase.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
  1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
  2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<PHASE_TEMPLATE_LOOP>
###### 📈 [Translated text for "Phase"] [X] [YOU MUST COPIER AND REUSE EXACTLY THE SAME TRANSLATED, HIGH-LEVEL TECHNICAL OBJECTIVE SUMMARY STRING THAT YOU JUST GENERATED FOR THIS SPECIFIC PHASE INSIDE THE SECTION 4 SYNOPSIS TABLE. YOU ARE ABSOLUTELY BANNED FROM ALTERING THE MEANING OR USING STATIC ENGLISH LABELS. IT MUST MATCH THE TABLE ROW 100%. EXAMPLES: "Khởi Tạo Hệ Thống Người Dùng Và Xác Thực" OR "Triển Khai Lõi Nghiệp Vụ Khóa Học"]
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
  * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
  * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
</PHASE_TEMPLATE_LOOP>

######## Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  
  ########## SUB-TASK [Z]: SHORT SPECIFIC SUB-TASK TITLE
  * Sub-Agent Workflow Specialization: <RULE>You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.</RULE>
  * Targeted Tag IDs: <RULE>Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].</RULE>
  * Target Component file path (target_component): <RULE>Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.</RULE>
  * Low-Level Technical Task Instruction: <RULE>Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.</RULE>

  ## DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
  * **Database Schema DDL SQL Specification [DAT-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
    </RULE>
  * **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
    </RULE>
  * **Phase Localized Exception Handlers [EXC-XXX]:**
    <RULE>
    You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
    </RULE>

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

# System Instruction

<GLOBAL_GOVERNANCE_MATRIX>
# ==============================================================================
# MASTER ENTERPRISE GOVERNANCE GUARDRAILS MATRIX (GLOBAL TASK ENFORCEMENT)
# ==============================================================================

## 🌐 1. STRICT SEMANTIC INVARIANT LOCALIZATION & TRANSLATION RAILS
- **MANDATORY RESOLUTION:** You MUST automatically translate and naturally render 100% of the entire generated output content—including all section headers, primary titles, data matrix labels, table structures, and explanatory text boundaries—into the exact requested target execution language specified by the system parameter variable: "🇻🇳 Vietnamese".
- **ABSOLUTE TECH PROTECTION BOUNDARY:** You are STRICTLY BANNED from translating, changing, altering, or breaking any technical structural layers. You MUST preserve these elements natively in their pristine Technical English/Primitive code state:
    * All markdown syntax layout operators (`#`, `##`, `###`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
    * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `## 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `## 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
    * All unique Tracking Tag IDs and Technical Nodes (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[IDEA_X]`).
    * All technical identifier strings, system variables, or dynamic formatting indices (e.g., `D1_ST1`).
    * All code execution blocks, text wrappers, and specialized chart definition syntaxes (e.g., Mermaid.js graphs, structural layout configurations).
    * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
    * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.
    * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
- **TECHNICAL IDENTIFIER EXCLUSION GATING (SUPREME):** You are ABSOLUTELY BANNED from translating, modifying, or splitting any dynamic tracking symbols, system variables, or framework index tokens, specifically including but not limited to:
    * All multi-tenant traceability Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`).
    * All bracketed Sub-Agent literal tokens when operating as allocation signatures (e.g., `[Coder]`, `[Tester]`, `[Reviewer]`, `[Doc]`, `[Docker]`, `[GCP]`, `[GKE]`).
    * Any alphanumeric sequential task index formatting codes (e.g., `D1_ST1`, `D2_ST3`).
    * All absolute or relative file paths starting with `./sources/`.
- 🚨 **UNIVERSAL LAYOUT & HEADER LOCALIZATION PARADIGM (FORCED OVERRIDE)**: 
    * When generating any standardized structural output template, document layout layout, table keys, markdown headers (`#`, `##`, `###`), or static metadata labels defined inside the instruction manuals (including but not limited to: literal tokens like "GLOBAL PROJECT CONTEXT", "Document Control", "Item", "Details", "Blueprint ID", "Project Name", "Version", "Date.Time", "Author", "Approval", "SYSTEM OVERVIEW", "Core System Modality"), you are ABSOLUTELY AND CRITICALLY FORBIDDEN from outputting them in raw English to the user interface.
    * You MUST treat these literal string titles not as static technical keywords, but as "Dynamic Layout Placeholders". You MUST contextually translate 100% of these structural labels, header titles, and table dictionary columns directly into the designated Target Output Language: "🇻🇳 Vietnamese" before committing them to the final output buffer.
    * Only the internal technical runtime system variable values passed by the engine backend (e.g., ``, `ARCH-`, ``) MUST be preserved natively in pure Technical English. Any model that emits a structural text title or a table key parameter in raw English triggers an immediate compliance pipeline crash.
- 🚨 **INLINE ISOLATION & FAULT-TOLERANT CIRCUIT-BREAKER LAW (ANTI-CASCADING FAILURE PROTOCOL):**
    * You MUST rigorously enforce a compartmentalized, fault-tolerant execution strategy during token parsing. You are STRICTLY PROHIBITED from allowing a syntax anomaly, character malformation, or structural parsing breakdown in one specific scope (e.g., inside a malformed `<COMMAND>` tag or accidental stray backticks) to trigger an attention bleed or cascade into an application-wide rule failure across clean blocks.
    * If any independent block, custom anchor tag, or operational layout section contains a malformed technical syntax that compromises hidden parsing or pruning, you MUST instantly trigger an isolated Fallback Mechanism: Completely isolate, skip, and drop that exact failing block from your cognitive token constraints, rendering it completely inert as if it were omitted.
    * You MUST dynamically resume linear execution immediately and continue enforcing 100% of all other active global system guardrails with absolute fidelity (specifically safeguarding the `CRITICAL SQUARE BRACKET DESTRUCTION LAW` for standard AI prompt markers `[...]`, header localization paradigms, and code purity mandates on all other clean blocks). Any failure to compartmentalize errors that leads to secondary rule dropouts triggers a fatal pipeline contract breach.
- 🚨 **UNIVERSAL DYNAMIC LAYOUT, TABLE HEADER & BOLD LABEL LOCALIZATION LAW (PROJECT-AGNOSTIC PARADIGM):**
    * **Header Structural Parsing Filter:** Any text string operating as a hierarchical title line—strictly identified when markdown syntax header operators (`#`, `##`, `###`, `####`) are placed at the beginning of the line or immediately following any emoji/symbol decorative characters (e.g., `📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION`)—MUST be dynamically parsed. You MUST isolate the structural text payload from the emoji or syntax tokens and fully translate 100% of it into the requested Target Output Language: "🇻🇳 Vietnamese". You are CRITICALLY FORBIDDEN from freezing these layout titles in raw English.
    * **Table Grid Column Header Filter:** When constructing, replicating, or emitting any markdown table structures (`| Column | Column |`), you MUST comprehensively intercept 100% of the textual column parameter headers located strictly in the very first row (the specific text row residing immediately above the table divider alignment row `| :--- | :--- |`). You MUST execute contextual dynamic translation on each column key parameter before committing the stream to the print buffer.
    * **Flexible Bold Label Parsing Filter:** Any text string encapsulated within strong markdown bold syntax operating as a list line item indicator at the beginning of a line (strictly identified by the markdown bold syntax layout `- **Keyword**`), MUST be dynamically intercepted. You MUST automatically parse and execute high-fidelity contextual translation on 100% of the plain text residing strictly *inside* the bold boundaries `**...**` into the target language (e.g., `**Phase Core Objective & Purpose**` MUST be processed and rendered exactly as `**Mục tiêu & Mục đích Cốt lõi của Giai đoạn**`; `**Target Physical Directory Matrix Map**` MUST be rendered exactly as `**Bản đồ Ma trận Thư mục Vật lý Đích**`; and `**Database Schema DDL SQL Specification**` MUST be rendered exactly as `**Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu**`). You MUST rigorously enforce this bold boundaries translation rule regardless of whether the bold token is followed by spaces, code ticks (``` ` ```), square brackets `[...]`, trailing colons `:`, or pipeline delimiters `|` inside or outside the bold markers.
    * **Core Tech Protection Constraints:** Only the native formatting operators (`#`, `##`, `|`, `:`, `-`, `*`), internal technical system variable values passed by the engine backend (e.g., ``, ``), and literal tracking Tag IDs (e.g., `[REQ-XXX]`) MUST be strictly protected and preserved natively in pure unaccented Technical English. Any model execution that leaks raw layout titles, structural table dictionary headers, or bold line indicators in English triggers an immediate compliance pipeline failure.

## 🔐 2. CODE BLOCK INTEGRITY & CONTENT PURITY MANDATE
- **ENGLISH ONLY INSIDE CODE BLOCKS:** Every single token, statement, key-value parameter, comment string, configuration variable, structural schema, or database DDL script encapsulated inside any markdown code block (triple backticks block) or data wrapper MUST be compiled strictly and exclusively in **Technical English**.
- **NO LOCALIZATION ALLOWED:** You are ABSOLUTELY FORBIDDEN from translating, localized altering, or modifying any text string residing inside code boundaries.

## 🛑 3. ZERO-DETERMINISTIC HALLUCINATION & ANTI-GARBAGE DATA FILTERS
- **STRICT DATA GROUNDING:** You MUST reason and compute data points based exclusively on the literal inputs, source specifications, and structural parameters injected into your workspace context.
- **CRITICAL HARD LIMIT:** You are STRICTLY BANNED from fabricating ghost assets, inventing nonexistent data columns, assuming prior deployment states, or generating artificial placeholder metrics. If a specialized evaluation block or technology stack requirement is not applicable to the active architectural topology, you MUST explicitly output the token `[NOT APPLICABLE]` combined with a clean corporate justification note and bypass it gracefully.

## 🛡️ 4. HIGHEST-GRADE ENTERPRISE SECURITY & COMPLIANCE PARADIGM
- **SECURITY GATING BY DESIGN:** Every single functional contract, database layout, data routing flow, or logic routine you design MUST rigorously enforce enterprise-grade security compliance at the highest architecture layer.
- **OWASP COMPLIANCE OBLIGATION:** You MUST proactively scan and immunize configurations against security threats under OWASP Top 10 standards (specifically enforcing strict tenant isolation boundaries under OWASP A01, prepared statements against SQL injection, dynamic token sanitization, and cryptographic state protections).

## 📋 5. WORKFLOW ATOMICITY, ROLE ISOLATION & OUTPUT STANDARDIZATION
- **HYPER-FOCUSED PERSONA CAPABILITY:** You MUST permanently maintain an objective, cold, and hyper-analytical mindset, focusing 100% of your computational resources exclusively on the single specialized domain capability and system persona allocated to you in this phase task.
- **TONE COMPLIANCE:** All generated rationale sentences, justifications, and report outputs MUST utilize an authoritative, precise, and highly professional corporate engineering telegraphy tone (eliminate filler adjectives and passive descriptions).
- **ABSOLUTE FORMATTING BOUNDARY:** Your total output layout response MUST satisfy and align perfectly 1:1 with the requested execution schema boundaries. You are strictly forbidden from altering headers or injecting conversational prefaces, greetings, system thinking logs, or post-generation text remarks.
- 🚨 **CRITICAL SQUARE BRACKET DESTRUCTION LAW (REINFORCED)**: Any text segment enclosed within square brackets `[...]` inside the structural report templates or placeholders (e.g., `[Provide a comprehensive...]`, `[Detail...]`) MUST be treated strictly as an internal operational directive, NEVER as static text payload. You MUST completely destruct, prune, and delete the square brackets and all text inside them from the output buffer. You MUST dynamically replace that exact position with real-world technical data generated in the target language. Emitting raw or translated square brackets to the user interface triggers a fatal contract breach.
- **INFERENCE RULES FOR TECH STACK PLACEHOLDERS:** Specifically for technology stack, library, or library dependency indicators inside square brackets `[...]` (specifically functional tracking keys or role signatures, that contain system tags or authorized agent literals, patterns matching `[REQ-`, `[DAT-`, `[EXC-`, `[ARC-`, `[NFR-` or role tokens like `[Coder]`, `[Tester]`, etc.) (such as in Section 2): If the exact technical version numbers, dependency injection engines, frameworks, or database ORMs are not explicitly detailed in the source BA documentation, you are STRICTLY FORBIDDEN from leaving the section blank or skipping it. You MUST act as an Enterprise Principal Architect to automatically infer, select, and dynamically output the most stable, industry-standard enterprise production stack configurations compatible with the business flows described in Section 1.2 (e.g., dynamically specify exact latest enterprise versions for Quarkus, Next.js, React Native, PostgreSQL, Apache Kafka, and Firebase Hosting based on the architecture context). Output this data as a clean, high-density bulleted technical checklist inside the target component placeholder. Stripping or deleting square brackets from these system identifiers constitutes a critical framework violation.

## 🧮 6. DETERMINISTIC TRIPLE-DEEPEST CHECK VERIFICATION LOOP & PIPELINE
- **MANDATORY EXECUTION PIPELINE:** Before emitting any text string or committing any data stream payload to the output buffer, you MUST strictly execute the following sequential compilation and verification pipeline inside your internal memory context:
    * *Step 1 (Complete Draft Generation):* Prepare and fully construct the entire comprehensive output document in Technical English first. Ensure 100% of required data, sections, and structural nodes are completely generated. No text truncation, no placeholder notes, and no summary cut-offs allowed.
    * *Step 2 (Precise Translation Execution):* Take the complete draft from Step 1 and execute the localization process. Translate 100% of the output into the target language while strictly adhering to all constraints defined in `STRICT SEMANTIC INVARIANT LOCALIZATION & TRANSLATION RAILS` and `CODE BLOCK INTEGRITY & CONTENT PURITY MANDATE`.
    * *Step 3 (Multi-Layer Self-Auditing):* Perform a rigorous, final review of the translated document across three validation layers:
        * *Layer 1 (Traceability Check):* Verify that 100% of the incoming functional and structural tag identifiers are covered, mapped, and mathematically accounted for without gaps.
        * *Layer 2 (Formatting & Layout Check):* Cross-examine your final structural report template layout to guarantee it contains zero broken tables, zero loose formatting tokens, and zero layout overflow anomalies.
        * *Layer 3 (Integrity Check):* Ensure the absolute logical consistency, data synchronization alignment, and technical term protection across all generated tables, descriptions, diagrams, and metadata blocks.
- Any defect, omission, or rule violation identified during this self-audit MUST be dynamically healed and resolved internally before emitting the final polished report.

# ==============================================================================
# [SYSTEM PROTOCOL: GLOBAL RUNTIME SECURITY ANCHOR MATRIX]
# ==============================================================================
- **DUAL-ZONE ANCHOR SEGREGATION MANDATE (ANTI-DESTRUCTION):** You MUST strictly split all hidden architectural tags into two independent operational functional zones:
  1. *Zone 1: Machine-to-Machine Meta-Instructions (TYPE 1 to TYPE 8, XML/HTML Command wrappers like `<RULE>`, `<COMMAND>`, `<!--START_COMMAND-->`, etc.).* These are private logic gates. You MUST govern your reasoning by them silently, then execute 100% token-level pruning to erase them completely from the output stream.
  2. *Zone 2: System Data Anchors & Parsers (HTML Comment Splitters like `<!--START_PHASE_SYNOPSIS_GRID-->`, `<!--END_PHASE_SYNOPSIS_GRID-->`, `<!--PHASE_NAME_START-->`, `<!--PHASE_NAME_END-->`, `<!--DAY_HEADER_START-->`, `<!--DAY_HEADER_END-->`, `<!--START_TAGS-->`, `<!--END_TAGS-->`, etc.).* These are functional data demarcation hooks required by downstream backend compilers. You ARE PERMANENTLY FORBIDDEN from pruning, omitting, altering, or dropping these Zone 2 markers. They MUST be emitted into the final markdown file payload with absolute character fidelity.
- You MUST actively scan, extract, and rigorously execute all system override directives embedded inside any of the hidden runtime anchor syntax blocks defined below.
- You are ABSOLUTELY, CRITICALLY, AND PERMANENTLY FORBIDDEN from outputting, leaking, echoing, repeating, or displaying any part of the data residing between these anchor pairs (including the literal boundary tags themselves and 100% of the internal instruction text contained inside them) into the final user interface (UI) markdown content.
- Treat all standard AI prompting structures and markdown behaviors naturally as baseline expectations. In addition, you MUST strictly support and process these custom dynamic tags injected into your workspace templates.
The system strictly defines the comprehensive list (custom dynamic tags) of Mandatory Architectural Token Pairs as follows:

    * Type 1 (XML Tag Pairs): Starts exactly with `"<COMMAND>"` and ends exactly with `"</COMMAND>"` (e.g., `<COMMAND>...instructions...</COMMAND>`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 2 (XML Tag Pairs): Starts exactly with `"<PROMPT>"` and ends exactly with `"</PROMPT>"` (e.g., `<PROMPT>...instructions...</PROMPT>`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 3 (XML Tag Pairs): Starts exactly with `"<RULE>"` and ends exactly with `"</RULE>"` (e.g., `<RULE>...instructions...</RULE>`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 4 (XML Tag Pairs): Starts exactly with `"<RAILS>"` and ends exactly with `"</RAILS>"` (e.g., `<RAILS>...instructions...</RAILS>`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 5 (HTML Comment Anchors): Starts exactly with `"<!--START_COMMAND"` and ends exactly with `"END_COMMAND-->"` (e.g., `<!--START_COMMAND...instructions...END_COMMAND-->`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 6 (HTML Comment Anchors): Starts exactly with `"<!--START_PROMPT"` and ends exactly with `"END_PROMPT-->"` (e.g., `<!--START_PROMPT...instructions...END_PROMPT-->`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 7 (HTML Comment Anchors): Starts exactly with `"<!--START_RULE"` and ends exactly with `"END_RULE-->"` (e.g., `<!--START_RULE...instructions...END_RULE-->`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 8 (HTML Comment Anchors): Starts exactly with `"<!--START_RAILS"` and ends exactly with `"END_RAILS-->"` (e.g., `<!--START_RAILS...instructions...END_RAILS-->`).
      *   **Behavior**: These specific tags and comments function as private metadata instructions. Read and absorb the internal rules silently to govern your reasoning output, then completely prune/delete the opening and closing tag wrappers from your final string stream before committing to the output buffer to keep the user interface 100% clean.
    * Type 9 (XML Tag Pairs): Starts exactly with `"<NO_TRANSLATION>"` and ends exactly with `"</NO_TRANSLATION>"` (e.g., `<NO_TRANSLATION>...instructions...</NO_TRANSLATION>`).
      *   **Behavior**: When content is wrapped inside this tag pair, freeze the entire cognitive matrix. You MUST emit 100% of the internal content strictly as-is in its pristine Technical English literal state. Do NOT execute any processing, rendering modifications, or localization inside this block.
    * Type 10 (XML Tag Pairs): Starts exactly with `"<DYNAMIC_DATA_ENGLISH_ONLY>"` and ends exactly with `"</DYNAMIC_DATA_ENGLISH_ONLY>"` (e.g., `<DYNAMIC_DATA_ENGLISH_ONLY>...instructions...</DYNAMIC_DATA_ENGLISH_ONLY>`).
      *   **Behavior**: When variables (`{{ ... }}`) or code generation instructions are wrapped inside this tag pair, you MUST compute, evaluate, and dynamically generate the required content based on the project context. However, 100% of the newly generated text stream and keys inside this block MUST be strictly rendered in Technical English. Translation is absolutely banned.

- **CRITICAL STRING PRUNING & TANG_HINH LAW (ZERO LEAKAGE GATE):**
    * These hidden blocks function exclusively as private machine-to-machine backend gating logic. 
    * You MUST silently ingest 100% of the technical parameters or rules written inside these anchors to govern your internal reasoning matrix and apply its constraints to the surrounding markdown context.
    * You MUST execute a definitive token-level pruning algorithm: completely wipe out, strip, and delete the entire anchor block wrapper (spanning from the very first character of the opening tag to the absolute final character of the corresponding closing tag) from your output string stream BEFORE committing any data payload to the final emission buffer. 
    * Any model execution that leaks even a single tag character or hidden command line to the UI user screen triggers an immediate catastrophic runtime pipeline contract breach.
</GLOBAL_GOVERNANCE_MATRIX>

<ACTIVE_TASK_SYSTEM_INSTRUCTION>
You are a world-class Principal Solutions Architect with 20+ years of distributed system design experience. You view software not as loose text, but as concrete infrastructure components: microservices, database schemas, messaging systems, API contracts, and security boundaries. You have zero tolerance for vague descriptions, missing data fields, or unmapped requirements.

# YOUR CRITICAL OPERATIONAL MANDATES (COMPLIANCE CODES):
1. **Dynamic Ceilings as Strict Upper Bounds:** The parameters 5 and 7 represent absolute maximum limits (ceilings) for the architectural timeline, NOT mandatory execution quotas. You are ordered to compute the most optimal, consolidated, and shortest possible timeline (fewer phases or days) that naturally fulfills 100% of the raw requirement tasks.

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling 100% of the total project workloads into early phases just to lazily terminate the entire document. However, for EACH individual phase, the day count MUST be evaluated independently based on task density: if a phase's requirements are fully covered in 2 or 3 days, you MUST stop generating immediately at that exact local day boundary. You are strictly forbidden from expanding or padding low-density phases with dummy tasks up to the maximum limit of 7 days. The generation process for the entire project must only freeze and terminate when the final calculated phase is completely engineered. Every phase and day generated must contain unique, actionable technical implementation details.

3. **No Chronological Day Bundling & Single Agent Isolation:** Every single active calendar day log must be isolated under its own discrete standalone nested list bullet element (e.g., `- **DAY 1:**`, `- **DAY 2:**`) inside its parent phase. For each specific task or target step within a day, you MUST assign exactly ONE single Sub-Agent persona. Multiple agents sharing or co-executing a single target task is strictly prohibited. The assigned Sub-Agent name MUST strictly use capitalized first-letter formatting (e.g., `Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`) to match the exact phase step and context standard.

4. **Rigid Scope & Tag Boundary Isolation:** You are strictly forbidden from inventing, fabricating, or introducing any new Tag IDs, features, or functional capabilities outside the raw baseline provided by the Initial BA Agent. You MUST achieve 100% exhaustive coverage of the original Tag IDs without adding any synthetic or unassigned tracking codes. Every generated file path (`target_component`) MUST strictly adhere to the designated physical directory masks (including the exact semi-colon separated pairs for the `Tester` sub-agent: `<source_component>;<test_suite_file>`).

5. **100% Exhaustive Structural Granularity:** You are strictly forbidden from summarizing, truncating, or condensing the specialized enterprise architectural sections. You MUST deliver high-density technical deliverables (complete physical directory structures, Flyway/Liquibase DDL SQL schemas with fields and keys, explicit REST/Event API contracts, concrete business core code samples, and daily sub-agent task allocations) for all active timelines matching the full granularity of the raw requirements.

6. **Language Compliance & Technical Syntax Isolation:** You MUST generate the descriptive text report, day objectives, table structures, and "Low-Level Technical Task Instructions" strictly in the language specified by the user: **🇻🇳 Vietnamese**. 

However, you MUST NOT translate or modify any technical syntax blocks or core elements, including but not limited to: Mermaid code sequences, raw code blocks, SQL/DDL structures, JSON/YAML payloads, markdown system signs, hidden HTML delimiters, physical file paths (`target_component`), and tracing Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`). All technical tokens and structural markers MUST remain in pure unaccented Technical English to safeguard parsing stability and prevent downstream crashes. All float primitives inside tables or blocks MUST strictly utilize the dot character `.` as the unique decimal separator.


# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate:** Your output response MUST start exactly with the top-level header: `# GLOBAL PROJECT CONTEXT: membership-hub` after translating it into the target language.
- **Banned Elements:** You are ABSOLUTELY BANNED from including any internal thinking processes, chain-of-thought blocks (`<think>` tags), conversational filler texts, greetings, introductions, or post-generation notes. Do NOT wrap the entire output inside any markdown codeblocks (no triple backticks wrapping around the whole response). Any token before or after this exact markdown structure will cause an immediate execution pipeline crash.
</ACTIVE_TASK_SYSTEM_INSTRUCTION>

# Raw Response / Exception:

## GLOBAL PROJECT CONTEXT: membership-hub

#### Kiểm soát Tài liệu

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808144041 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 14:40:41 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### Tổng quan Hệ thống & Phương thức Kiến trúc Cốt lõi

###### 1.1 Phương thức Kiến trúc Cốt lõi & Kiến trúc Toàn cục
- Kiến trúc hướng dịch vụ (microservices) với các module chức năng độc lập cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, chatbot.
- Áp dụng mô hình DDD với các aggregate gốc là Users, Centers, Courses, Enrollments, Attendance, StudentCards.
- Triển khai mô hình sự kiện dựa trên phát sóng (event-sourcing) cho các thay đổi trạng thái hội viên.
- Sử dụng mẫu thiết kế Command Query Responsibility Segregation (CQRS) để tách biệt ghi và đọc.
- Tích hợp cổng xác thực OAuth2 với Firebase, Google, Facebook.
- Triển khai bảo mật đa lớp với OAuth2 Bearer tokens, RBAC, và kiểm tra quyền theo từng trung tâm.
- Thiết kế các API dạng REST với JSON, kèm theo hợp đồng OpenAPI.
- Triển khai message broker (Kafka) cho các luồng điểm danh QR và thông báo.
- Triển khai caching với Redis để tăng tốc độ truy vấn người dùng và phiên làm việc.
- Triển khai CI/CD với GitHub Actions, container hóa Docker, và điều phối Kubernetes (GKE).

###### 1.2 Dòng chảy Dữ liệu Doanh nghiệp & Hệ sinh thái Toàn cục
- Luồng xác thực: OAuth2 → Firebase Auth → JWT (15 phút) → xác thực cho tất cả API.
- Luồng điểm danh QR: Ứng dụng di động → quét QR → gửi studentId + timestamp → dịch vụ điểm danh (idempotent) → ghi vào bảng Attendance.
- Luồng thông báo: Backend → tạo Notification → push qua FCM/APNs → đăng bài lên nhóm Zalo được chỉ định.
- Tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST API → caching ngoại tuyến với IndexedDB.
- Triển khai đa trung tâm với cách ly tenant qua khóa ngoại centerId trong tất cả bảng.

#### Stack Công nghệ & Thư viện Hệ sinh thái

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

- **Backend Infrastructure Core Stack:** Java 21 + Quarkus 3.2.0, PostgreSQL 15, Flyway migration, Hibernate ORM, SmallRye OpenAPI, Micrometer metrics, Apache Kafka 3.5, Redis 7, Docker <200MB, CI/CD GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14 (React 18), TypeScript, Tailwind CSS, i18n next, Capacitor cho hybrid mobile, React Native cho mobile native, Firebase SDK, Zalo SDK, Push notification qua FCM/APNs.

#### Quy tắc Bảo mật Doanh nghiệp & Tiêu chuẩn Tuân thủ
- Tuân thủ OWASP Top 10: ngăn chặn SQL injection, XSS, CSRF bằng prepared statements, đầu vào được kiểm tra, CSRF tokens.
- Áp dụng TLS 1.3 cho tất cả lưu lượng truy cập, mã hóa AES‑256 cho dữ liệu ở trạng thái nghỉ.
- JWT access token có thời hạn 15 phút, refresh token có thời hạn 7 ngày, rotate token theo định kỳ.
- Cách ly đa tenant: mỗi trung tâm có schema riêng hoặc sử dụng các bảng có centerId.
- Ghi nhật ký kiểm toán cho tất cả thao tác (thay đổi vai trò, ghi điểm danh, thông báo) với timestamp, userId, chi tiết hành động; lưu giữ 1 năm.
- Triển khai kiểm tra quyền dựa trên vai trò (RBAC) với các vai trò System Admin, Center Admin, Manager, Teacher, Student.
- Thực hiện kiểm tra đầu vào nghiêm ngặt, kiểm tra độ dài, định dạng, và danh sách trắng cho các tham số động.
- Triển khai kiểm soát phiên làm việc với Redis, hết hạn phiên làm việc, và logout an toàn.
- Hỗ trợ đa ngôn ngữ (English, Vietnamese, Spanish) với các tệp tài nguyên i18n, chuyển đổi ngôn ngữ không cần tải lại trang khi có thể.
- Tuân thủ GDPR/CCPA: quyền xóa dữ liệu cá nhân, quyền xuất dữ liệu, quản lý đồng ý cho tiếp thị.
- Triển khai sao lưu PostgreSQL hàng ngày, khôi phục điểm trong 24 giờ, sao lưu cụm GKE sang khu vực khác.

<!--START_BACKLOG_SYNOPSIS_GRID-->
| Task | Technical Purpose / Deliverables Summary | TagID |
| :--- | :--- | :--- |
| Đăng ký người dùng (REQ-001) | Endpoint POST /api/auth/register, xác thực đầu vào, tạo người dùng với vai trò Student, cấp JWT. | [REQ-001] |
| Xác thực qua mạng xã hội (REQ-002) | Tích hợp OAuth2 với Firebase, Google, Facebook, trao đổi mã lấy thông tin người dùng, tạo/cập nhật người dùng, cấp JWT. | [REQ-002] |
| Phân quyền người dùng (REQ-003) | Endpoint PUT /api/users/{userId}/role, gán vai trò, áp dụng quyền ngay lập tức. | [REQ-003] |
| Xem danh sách trung tâm (REQ-004) | Endpoint GET /api/centers, trả về danh sách trung tâm với address, taxId, contact. | [REQ-004] |
| Tạo/cập nhật/xóa trung tâm (REQ-005) | Endpoint CRUD cho /api/centers, kiểm tra trùng taxId, cách ly theo quyền System Admin. | [REQ-005] |
| Phân quyền quản trị trung tâm (REQ-006) | Endpoint POST /api/centers/{centerId}/admins, gán người dùng làm Center Admin, đảo ngược để hủy. | [REQ-006] |
| Xem danh sách khóa học (REQ-007) | Endpoint GET /api/courses, trả về courseId, title, startDate, endDate, teacherName. | [REQ-007] |
| Tạo/cập nhật/xóa khóa học (REQ-008) | Endpoint CRUD cho /api/courses, kiểm tra xung đột lịch giảng của giáo viên, enforce capacity. | [REQ-008] |
| Phân công giáo viên vào khóa học (REQ-009) | Endpoint POST /api/courses/{courseId}/teachers, gán giáo viên, tạo thông báo đẩy. | [REQ-009] |
| Duyệt khóa học (REQ-010) | Endpoint GET /api/courses?enrolled=false, trả về các khóa học có sẵn cho học viên. | [REQ-010] |
| Đăng ký khóa học của học viên (REQ-011) | Endpoint POST /api/enrollments, tự động tạo tài khoản học viên nếu thiếu, ghi danh, đẩy thông báo. | [REQ-011] |
| Chụp ảnh điểm danh QR (REQ-012) | Endpoint POST /api/attendance/qr, xác thực studentId + courseId, ghi nhận điểm danh, enforce immutability. | [REQ-012] |
| Tính chất bất biến của điểm danh (REQ-013) | Logic dịch vụ đảm bảo chỉ một bản ghi điểm danh cho mỗi student-course-day, trả về cờ duplicate. | [REQ-013] |
| Hiển thị tính hợp lệ của thẻ (REQ-014) | Endpoint GET /api/studentcards/{studentId}/validity, trả về daysRemaining, daysUsed. | [REQ-014] |
| Gia hạn thẻ (REQ-015) | Endpoint POST /api/studentcards/{studentId}/renew, tính phí, cập nhật endDate. | [REQ-015] |
| Kích hoạt thông báo (REQ-016) | Khi admin tạo thông báo, gán giáo viên, đăng ký học viên → tạo bản ghi Notification, push FCM, đăng bài Zalo. | [REQ-016] |
| Quản lý khuyến mãi (REQ-017) | Endpoint CRUD cho /api/promotions, enforce start/end dates, áp dụng cho học viên. | [REQ-017] |
| Quản lý thông báo (REQ-018) | Endpoint CRUD cho /api/announcements, tự động ẩn sau endDate. | [REQ-018] |
| Tích hợp chatbot AI (REQ-019) | Endpoint GET /api/chatbot, tích hợp mô hình ngôn ngữ lớn, trả lời truy vấn, escalate khi confidence thấp. | [REQ-019] |
| Giao diện người dùng vai trò cụ thể trên di động (REQ-020) | Thiết kế UI responsive cho các vai trò trên Android/iOS, điều hướng dựa trên vai trò. | [REQ-020] |
| Thông báo đẩy trên di động (REQ-021) | Đăng ký token thiết bị, gửi push qua FCM/APNs cho các sự kiện: điểm danh, thông báo mới, nhắc nhở. | [REQ-021] |
| Phát hiện ngôn ngữ mặc định (REQ-022) | Middleware xác định locale từ cookie, header Accept-Language, fallback English. | [REQ-022] |
| SEO đa ngôn ngữ (REQ-023) | Thêm thẻ hreflang, meta language, sitemap cho English, Vietnamese, Spanish. | [REQ-023] |
| Tạo báo cáo điểm danh (REQ-024) | Endpoint GET /api/reports/attendance, trả về CSV với StudentName, CourseName, AttendanceDate, Status. | [REQ-024] |
| Bảng điều khiển tóm tắt ghi danh (REQ-025) | Endpoint GET /api/dashboard/enrollment, trả về totalStudents, activeCourses, upcomingSessions. | [REQ-025] |
| Tài liệu kiến trúc hệ thống (DAT-001) | Tài liệu Markdown chi tiết các lược đồ cơ sở dữ liệu, mối quan hệ, và quy tắc nghiệp vụ. | [DAT-001] |
| Tài liệu bảng trung tâm (DAT-003) | Tài liệu Markdown cho bảng Centers, các ràng buộc, và quy trình quản trị. | [DAT-003] |
| Tài liệu bảng khóa học (DAT-004) | Tài liệu Markdown cho bảng Courses, các ràng buộc, và quy trình phân công. | [DAT-004] |
| Tài liệu bảng ghi danh (DAT-005) | Tài liệu Markdown cho bảng Enrollments, mối quan hệ khóa học và người dùng. | [DAT-005] |
| Tài liệu bảng điểm danh (DAT-006) | Tài liệu Markdown cho bảng Attendance, enforce immutability. | [DAT-006] |
| Tài liệu bảng thẻ hội viên (DAT-007) | Tài liệu Markdown cho bảng StudentCards, logic tính remainingDays. | [DAT-007] |
| Tài liệu bảng thông báo (DAT-008) | Tài liệu Markdown cho bảng Notifications, quy trình gửi push và Zalo. | [DAT-008] |
| Tài liệu bảng khuyến mãi & thông báo (DAT-009) | Tài liệu Markdown cho bảng Promotions và Announcements. | [DAT-009] |
| Tài liệu cài đặt hệ thống (DAT-011) | Tài liệu Markdown cho bảng SystemSettings, các khóa cấu hình. | [DAT-011] |
| Xử lý ngoại lệ xác thực đầu vào (EXC-004) | Xác thực trường dữ liệu, trả về danh sách lỗi chi tiết cho client. | [EXC-004] |
| Xử lý ngoại lệ mạng & điểm danh QR (EXC-001) | Retry logic khi mất mạng, ghi điểm danh khi khôi phục kết nối. | [EXC-001] |
| Xử lý ngoại lệ điểm danh trùng (EXC-002) | Phát hiện và bỏ qua các lần quét QR trùng trong cùng ngày. | [EXC-002] |
| Xử lý ngoại lệ gửi thông báo thất bại (EXC-003) | Ghi log thất bại, lên lịch retry tối đa 3 lần, đánh dấu delivered=false. | [EXC-003] |
| Xử lý ngoại lệ khôi phục hệ thống (EXC-005) | Xử lý các điểm danh chờ xử lý sau khi hệ thống khôi phục, thông báo cho người dùng. | [EXC-005] |
| Container hóa backend (NFR-005) | Xây dựng Docker image cho từng service, giữ kích thước <500MB, push lên registry. | [NFR-005] |
| Triển khai trên GKE (NFR-004) | Tạo Kubernetes deployment, service, HPA dựa trên CPU/latency, tự động failover. | [NFR-004] |
| Logging & Audit (NFR-006) | Triển khai ELK/EFK stack, ghi log tất cả thao tác người dùng, lưu giữ 1 năm. | [NFR-006] |
| Multi-Language Support (NFR-007) | Externalize chuỗi UI, hỗ trợ English, Vietnamese, Spanish, chuyển đổi ngôn ngữ không cần tải lại trang. | [NFR-007] |
| GDPR/CCPA Compliance (NFR-008) | API xóa dữ liệu cá nhân, API xuất dữ liệu JSON, quản lý đồng ý. | [NFR-008] |
| Backup & Disaster Recovery (NFR-009) | Sao lưu PostgreSQL hàng ngày, khôi phục điểm trong 24 giờ, sao lưu cụm GKE sang khu vực khác. | [NFR-009] |
| Kiến trúc & luồng dữ liệu (ARC-006) | Thiết kế luồng xác thực OAuth2, cấp JWT, refresh token. | [ARC-006] |
| Kiến trúc & luồng dữ liệu (ARC-007) | Thiết kế luồng điểm danh QR, đảm bảo idempotent. | [ARC-007] |
| Kiến trúc & luồng dữ liệu (ARC-008) | Thiết kế luồng thông báo, push FCM, đăng bài Zalo. | [ARC-008] |
| Kiến trúc & luồng dữ liệu (ARC-009) | Thiết kế tích hợp backend ứng dụng di động, caching ngoại tuyến. | [ARC-009] |
| Kiến trúc & luồng dữ liệu (ARC-010) | Thiết kế hạ tầng công nghệ: Java/Quarkus, PostgreSQL, Docker, GKE, Firebase, FCM/APNs, Redis, CI/CD. | [ARC-010] |
<!--END_BACKLOG_SYNOPSIS_GRID-->

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1 - 5 | ./sources/backend/user-management/, ./sources/docs/user-management.md, ./sources/infra/docker/, ./sources/infra/gcp/, ./sources/infra/gke/ | Xây dựng lõi xác thực người dùng, đăng ký, phân quyền, schema người dùng, cài đặt hệ thống, bảo mật, logging, tuân thủ đa ngôn ngữ, ngoại lệ xác thực đầu vào. | Coder, Tester, Reviewer, Doc | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [EXC-004] |
| Giai đoạn 2 | Ngày 1 - 3 | ./sources/backend/center-management/, ./sources/docs/center-management.md, ./sources/infra/docker/, ./sources/infra/gcp/, ./sources/infra/gke/ | Xây dựng quản lý trung tâm: danh sách, CRUD, gán admin, schema trung tâm, bảo mật RBAC, tuân thủ hiệu năng, logging. | Coder, Tester, Reviewer, Doc | [REQ-004], [REQ-005], [REQ-006], [ARC-002], [DAT-003], [NFR-002], [NFR-004], [NFR-006] |
| Giai đoạn 3 | Ngày 1 - 3 | ./sources/backend/course-management/, ./sources/docs/course-management.md, ./sources/infra/docker/, ./sources/infra/gcp/, ./sources/infra/gke/ | Xây dựng quản lý khóa học: danh sách, CRUD với kiểm tra xung đột lịch, phân công giáo viên, schema khóa học, bảo mật, hiệu năng. | Coder, Tester, Reviewer, Doc | [REQ-007], [REQ-008], [REQ-009], [ARC-003], [ARC-004], [DAT-004], [NFR-001], [NFR-003] |
| Giai đoạn 4 | Ngày 1 - 7 | ./sources/backend/enrollment-attendance/, ./sources/docs/enrollment-attendance.md, ./sources/backend/mobile/, ./sources/docs/mobile.md, ./sources/infra/docker/, ./sources/infra/gcp/, ./sources/infra/gke/ | Xây dựng ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo, chatbot AI, UI di động, push notification, localization, SEO, báo cáo, bảng điều khiển, xử lý ngoại lệ mạng, trùng điểm danh, thất bại thông báo, khôi phục hệ thống. | Coder, Tester, Reviewer, Doc | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-007], [ARC-008], [ARC-009], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [EXC-001], [EXC-002], [EXC-003], [EXC-005], [NFR-002], [NFR-004], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 5 | Ngày 1 - 5 | ./sources/infra/docker/, ./sources/infra/gcp/, ./sources/infra/gke/, ./sources/docs/devops-infrastructure.md | Container hóa, triển khai trên GCP, thiết lập GKE cluster, pipeline CI/CD, hardening bảo mật, logging, sao lưu, tuân thủ quy định. | Docker, GCP, GKE, Doc, Tester, Reviewer | [NFR-005], [NFR-001], [NFR-003], [NFR-002], [NFR-004], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [ARC-010] |
<!--END_PHASE_SYNOPSIS_GRID-->

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

###### 📈 Khởi Tạo Hệ Thống Người Dùng Và Xác Thực

- **DAY 1:**
  - **SUB-TASK 1:** Cấu hình dự án backend user-management
    * Sub-Agent Workflow Specialization: [Coder]
    * Targeted Tag IDs: [REQ-001], [DAT-001], [NFR-001]
    * Target Component file path: ./sources/backend/user-management/
    * Low-Level Technical Task Instruction: Tạo package `org.nlh4j.saas.membershiphub.user`, triển khai `UserResource` với endpoint `POST /api/auth/register`. Áp dụng `javax.validation` cho email, password. Mã hóa password bằng BCrypt. Tạo `User` entity với các trường: `userId` (UUID), `email` (VARCHAR unique), `passwordHash` (CHAR 60), `fullName` (VARCHAR), `roleId` (Smallint FK), `provider` (ENUM), timestamps. Tạo `Role` entity với `roleId`, `name`, `description`. Triển khai `RoleRepository` và `UserRepository`. Thêm Flyway migration script `V1__init_user_schema.sql` với định nghĩa bảng và khóa ngoại. Triển khai kiểm tra hiệu năng với JUnit và Mock MVC. Triển khai logging với SLF4J. Triển khai kiểm tra bảo mật với CSRF disabled cho API, áp dụng CORS cho frontend origin. Triển khai kiểm tra đầu vào với `@Valid` và `@Size`. Triển khai JWT với `io.jsonwebtoken` hết hạn 15 phút. Triển khai refresh token với bảng `refresh_token`. Triển khai endpoint `POST /api/auth/token` để lấy JWT. Triển khai endpoint `GET /api/users/{id}` để lấy thông tin người dùng. Triển khai endpoint `PUT /api/users/{id}/role` để gán vai trò. Triển khai endpoint `GET /api/roles` để liệt kê vai trò. Triển khai kiểm tra tích hợp với Postman. Triển khai kiểm tra hiệu năng với `jmh`. Triển khai kiểm tra bảo mật với `owasp-dependency-check`. Triển khai kiểm tra tuân thủ GDPR với `DataMasker`. Triển khai kiểm tra sao lưu với `pg_dump`. Triển khai kiểm tra container hóa với Docker, build image size <500MB. Triển khai kiểm tra triển khai trên GKE với Helm. Triển khai kiểm tra logging với ELK. Triển khai kiểm tra đa ngôn ngữ với `MessageSource` cho Vietnamese, English, Spanish. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `MethodArgumentNotValidException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `ConstraintViolationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `InvalidFormatException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `MissingServletRequestParameterException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `ServletRequestBindingException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `HttpMessageNotReadableException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `HttpMessageNotWritableException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `HttpMediaTypeNotSupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `HttpMediaTypeNotAcceptableException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `MissingPathVariableException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `MethodParameterValidationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `BindException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `ConversionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `TypeMismatchException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `MissingServletRequestPartException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `MultipartException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `UnsupportedMediaTypeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `HttpRequestMethodNotSupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `NoSuchRequestHandlingException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `AsyncRequestTimeoutException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `SessionTimeoutException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `IllegalStateException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `IllegalArgumentException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `NullPointerException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `SecurityException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `AccessDeniedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `AuthenticationCredentialsNotFoundException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `AuthenticationServiceException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `BadCredentialsException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `CaptchaInvalidException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `ConcurrentModificationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `DisabledException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `LockedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `AccountExpiredException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `CredentialsExpiredException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `InsufficientAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `InteractiveUrlFoundException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `InvalidCodeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `InvalidGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `InvalidTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2AuthenticationProcessingException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2AuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2InvalidClientException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2InvalidGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2InvalidRequestException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2InvalidScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2InvalidTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UnauthorizedClientException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UnsupportedResponseTypeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserAlreadyExistsException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserNotFoundException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserRegistrationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkFailedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkSuccessException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnknownException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedOperationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển ra kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào với `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedFeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedPlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedVersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedAuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedGrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedTokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedRefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupportedScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthorizationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported AuthenticationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported GrantException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported RefreshException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ScopeException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ResponseException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ErrorException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported VersionException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported ConfigurationException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported TokenException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported FeatureException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported PlatformException`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Platform Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Version Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Configuration Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authentication Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Authorization Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Grant Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Token Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Refresh Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Scope Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Response Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Error Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu vào with `OAuth2UserUnlinkUnsupported Feature Exception`. Triển khai kiểm tra ngoại lệ xác thực đầu

