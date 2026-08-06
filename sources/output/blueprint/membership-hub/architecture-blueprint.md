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
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
###### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
## BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`##`, `####`, `######`, `########`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into 🇻🇳 Vietnamese, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling all workloads into early phases to lazily terminate early. The generation must only freeze and terminate when the final phase (up to the computed total, capped strictly at 5) is completely engineered. You are strictly prohibited from creating dummy/placeholder requirements, empty reviews, or hollow tasks. Every phase and day generated must contain unique, actionable technical implementation details.

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

Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Requested 16173, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}: ['Traceback (most recent call last):
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
', "openai.APIStatusError: Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Requested 16173, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
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
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
###### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
## BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`##`, `####`, `######`, `########`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into 🇻🇳 Vietnamese, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling all workloads into early phases to lazily terminate early. The generation must only freeze and terminate when the final phase (up to the computed total, capped strictly at 5) is completely engineered. You are strictly prohibited from creating dummy/placeholder requirements, empty reviews, or hollow tasks. Every phase and day generated must contain unique, actionable technical implementation details.

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
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
###### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
## BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`##`, `####`, `######`, `########`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into 🇻🇳 Vietnamese, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling all workloads into early phases to lazily terminate early. The generation must only freeze and terminate when the final phase (up to the computed total, capped strictly at 5) is completely engineered. You are strictly prohibited from creating dummy/placeholder requirements, empty reviews, or hollow tasks. Every phase and day generated must contain unique, actionable technical implementation details.

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

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 6481 tokens, but can only afford 167. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 1177. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 477. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 2048 tokens, but can only afford 362. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 8192 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 3072 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 530. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
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
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 6481 tokens, but can only afford 167. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 1177. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 477. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 2048 tokens, but can only afford 362. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 8192 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 3072 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 530. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
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
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
###### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
## BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`##`, `####`, `######`, `########`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into 🇻🇳 Vietnamese, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling all workloads into early phases to lazily terminate early. The generation must only freeze and terminate when the final phase (up to the computed total, capped strictly at 5) is completely engineered. You are strictly prohibited from creating dummy/placeholder requirements, empty reviews, or hollow tasks. Every phase and day generated must contain unique, actionable technical implementation details.

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
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
###### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
## BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`##`, `####`, `######`, `########`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into 🇻🇳 Vietnamese, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling all workloads into early phases to lazily terminate early. The generation must only freeze and terminate when the final phase (up to the computed total, capped strictly at 5) is completely engineered. You are strictly prohibited from creating dummy/placeholder requirements, empty reviews, or hollow tasks. Every phase and day generated must contain unique, actionable technical implementation details.

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
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
###### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
## BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`##`, `####`, `######`, `########`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into 🇻🇳 Vietnamese, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling all workloads into early phases to lazily terminate early. The generation must only freeze and terminate when the final phase (up to the computed total, capped strictly at 5) is completely engineered. You are strictly prohibited from creating dummy/placeholder requirements, empty reviews, or hollow tasks. Every phase and day generated must contain unique, actionable technical implementation details.

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
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
###### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
## BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`##`, `####`, `######`, `########`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into 🇻🇳 Vietnamese, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling all workloads into early phases to lazily terminate early. The generation must only freeze and terminate when the final phase (up to the computed total, capped strictly at 5) is completely engineered. You are strictly prohibited from creating dummy/placeholder requirements, empty reviews, or hollow tasks. Every phase and day generated must contain unique, actionable technical implementation details.

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

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 392. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
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
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 392. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
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
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
###### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
## BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`##`, `####`, `######`, `########`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into 🇻🇳 Vietnamese, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling all workloads into early phases to lazily terminate early. The generation must only freeze and terminate when the final phase (up to the computed total, capped strictly at 5) is completely engineered. You are strictly prohibited from creating dummy/placeholder requirements, empty reviews, or hollow tasks. Every phase and day generated must contain unique, actionable technical implementation details.

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
- You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements. Do NOT emit relative paths that assume a sub-module directory is the root:
  * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend.` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend.<service-name>.`).
  * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend.` (or `./sources/frontend.<app-name>.` if multiple client applications exist. Skip entirely if project is Backend-only).
  * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra.`.
  * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.

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

## GLOBAL PROJECT CONTEXT: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=[true/false based on project context]
BACKEND_LAYER_REQUIRED=[true/false based on project context]
FRONTEND_LAYER_REQUIRED=[true/false based on project context]
MOBILE_LAYER_REQUIRED=[true/false based on project context]
DEVOPS_LAYER_REQUIRED=[true/false based on project context]
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
<COMMAND>
## STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

## DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of 7 days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to 7 is completely banned.
</COMMAND>

<!--START_DELIMITTER-->
###### 📈 Phase [X] DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into 🇻🇳 Vietnamese]
- **Target Physical Directory Matrix Map:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **Database Schema DDL SQL Specification [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **Phase Localized Exception Handlers [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase [X])
## BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`##`, `####`, `######`, `########`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Target Component file path (`target_component`):** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax in Technical English. Append its corresponding Tag IDs inline here, e.g., `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Low-Level Technical Task Instruction:** [Exhaustive, high-density engineering instruction, framework conventions, API contract layouts, data fields validation, or unit test case parameters translated completely into 🇻🇳 Vietnamese, attaching Tag IDs]
      - **Targeted Tag IDs:** [Write each tag out individually separated by commas, e.g., `[REQ-001], [DAT-002], [EXC-001]`.]

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
- 🚨 **UNIVERSAL LAYOUT & HEADER LOCALIZATION PARADIGM (FORCED OVERRIDE)**: 
    * When generating any standardized structural output template, document layout layout, table keys, markdown headers (`#`, `##`, `###`), or static metadata labels defined inside the instruction manuals (including but not limited to: literal tokens like "GLOBAL PROJECT CONTEXT", "Document Control", "Item", "Details", "Blueprint ID", "Project Name", "Version", "Date.Time", "Author", "Approval", "SYSTEM OVERVIEW", "Core System Modality"), you are ABSOLUTELY AND CRITICALLY FORBIDDEN from outputting them in raw English to the user interface.
    * You MUST treat these literal string titles not as static technical keywords, but as "Dynamic Layout Placeholders". You MUST contextually translate 100% of these structural labels, header titles, and table dictionary columns directly into the designated Target Output Language: "🇻🇳 Vietnamese" before committing them to the final output buffer.
    * Only the internal technical runtime system variable values passed by the engine backend (e.g., ``, `ARCH-`, ``) MUST be preserved natively in pure Technical English. Any model that emits a structural text title or a table key parameter in raw English triggers an immediate compliance pipeline crash.
- 🚨 **INLINE ISOLATION & FAULT-TOLERANT CIRCUIT-BREAKER LAW (ANTI-CASCADING FAILURE PROTOCOL):**
    * You MUST rigorously enforce a compartmentalized, fault-tolerant execution strategy during token parsing. You are STRICTLY PROHIBITED from allowing a syntax anomaly, character malformation, or structural parsing breakdown in one specific scope (e.g., inside a malformed `<COMMAND>` tag or accidental stray backticks) to trigger an attention bleed or cascade into an application-wide rule failure across clean blocks.
    * If any independent block, custom anchor tag, or operational layout section contains a malformed technical syntax that compromises hidden parsing or pruning, you MUST instantly trigger an isolated Fallback Mechanism: Completely isolate, skip, and drop that exact failing block from your cognitive token constraints, rendering it completely inert as if it were omitted.
    * You MUST dynamically resume linear execution immediately and continue enforcing 100% of all other active global system guardrails with absolute fidelity (specifically safeguarding the `CRITICAL SQUARE BRACKET DESTRUCTION LAW` for standard AI prompt markers `[...]`, header localization paradigms, and code purity mandates on all other clean blocks). Any failure to compartmentalize errors that leads to secondary rule dropouts triggers a fatal pipeline contract breach.
- 🚨 **UNIVERSAL DYNAMIC LAYOUT & TABLE HEADER LOCALIZATION LAW (PROJECT-AGNOSTIC PARADIGM):**
    * **Header Structural Parsing Filter:** Any text string accompanying markdown structural header syntax operators (`#`, `##`, `###`, `####`)—regardless of full uppercase formatting or specialized character components—MUST be dynamically parsed, isolated from the syntax tokens, and fully translated into the requested Target Output Language: "🇻🇳 Vietnamese". You are STRICTLY AND PERMANENTLY FORBIDDEN from freezing a whole header line in raw English to evade translation gates.
    * **Table Grid Column Header Filter:** When constructing, replicating, or emitting any markdown table structures (`| Column | Column |`), you MUST comprehensively intercept 100% of the textual column parameter headers located strictly in the very first row (the specific text row residing immediately above the table divider alignment row `| :--- | :--- |`). You MUST execute contextual dynamic translation on each column key parameter before committing the stream to the print buffer.
    * **Core Tech Protection Constraints:** Only the native formatting operators (`#`, `##`, `|`, `:`, `-`), internal technical system variable values passed by the engine backend (e.g., ``, ``), and literal tracking Tag IDs (e.g., `[REQ-XXX]`) MUST be strictly protected and preserved natively in pure unaccented Technical English. Any model execution that leaks raw layout titles or structural table dictionary headers in English triggers an immediate compliance pipeline failure.

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
- 🚨 **CRITICAL SQUARE BRACKET DESTRUCTION LAW**: Any text segment enclosed within square brackets `[...]` inside the structural report templates (e.g., `[Provide a comprehensive...]`, `[Detail...]`) MUST be treated strictly as an internal operational directive, NEVER as static text payload. You MUST completely destruct, prune, and delete the square brackets and all text inside them from the output buffer. You MUST dynamically replace that exact position with real-world technical data generated in the target language. Emitting raw or translated square brackets to the user interface triggers a fatal contract breach.
    * **INFERENCE RULES FOR TECH STACK PLACEHOLDERS:** Specifically for technology stack, library, or library dependency indicators inside square brackets `[...]` (such as in Section 2): If the exact technical version numbers, dependency injection engines, frameworks, or database ORMs are not explicitly detailed in the source BA documentation, you are STRICTLY FORBIDDEN from leaving the section blank or skipping it. You MUST act as an Enterprise Principal Architect to automatically infer, select, and dynamically output the most stable, industry-standard enterprise production stack configurations compatible with the business flows described in Section 1.2 (e.g., dynamically specify exact latest enterprise versions for Quarkus, Next.js, React Native, PostgreSQL, Apache Kafka, and Firebase Hosting based on the architecture context). Output this data as a clean, high-density bulleted technical checklist inside the target component placeholder.

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

2. **Absolute Anti-Padding & Uniform Chronological Distribution Rule:** You MUST naturally distribute the core functional requirements and Tag IDs across the calculated architectural phases without artificial compaction. You are ABSOLUTELY BANNED from bundling all workloads into early phases to lazily terminate early. The generation must only freeze and terminate when the final phase (up to the computed total, capped strictly at 5) is completely engineered. You are strictly prohibited from creating dummy/placeholder requirements, empty reviews, or hollow tasks. Every phase and day generated must contain unique, actionable technical implementation details.

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

## BỐ CỤC DỰ ÁN TOÀN CẦU: membership-hub

#### 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806083133 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 08:31:33 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

###### 1.1. Core System Modality & Architecture Modality
Mô tả kỹ thuật chi tiết về kiến trúc hệ thống được phát hiện: hệ thống tuân thủ kiến trúc đa trung tâm (multi-center) với mô hình dịch vụ vi mô (microservices) được container hóa, sử dụng mẫu thiết kế Event-Driven (EDA) cho các luồng bất đồng bộ như điểm danh QR, thông báo, và tích hợp Zalo. Hệ thống áp dụng CQRS cho các thao tác ghi (nhật ký điểm danh, thông báo) và truy vấn (báo cáo, danh sách khóa học). Các biên giới lệnh (command) và truy vấn (query) được phân tách rõ ràng để đảm bảo khả năng mở rộng và hiệu suất. Các thành phần cốt lõi hoạt động theo kiểu phản ứng (reactive) với RxJava/Vert.x, tích hợp với Redis để cache phiên làm việc và hàng đợi tin nhắn. RBAC được thực hiện ở tầng bảo mật, với các service bảo vệ endpoint dựa trên vai trò người dùng. Các API được định nghĩa dưới dạng REST với Swagger, hỗ trợ JWT cho xác thực và OAuth2 cho các nhà cung cấp bên ngoài. Các sự kiện được phát qua Apache Kafka (hoặc RabbitMQ) để đảm bảo tính bất biến và khả năng mở rộng của các luồng điểm danh và thông báo. Các schema cơ sở dữ liệu được thiết kế theo mô hình ER với các ràng buộc khóa ngoại và chỉ mục để đảm bảo truy vấn dưới 200ms cho các trường hợp sử dụng chính. Hệ thống được triển khai trên Kubernetes (GKE) với auto-scaling dựa trên CPU và độ trễ yêu cầu, sử dụng Flyway cho quản lý migration. Các chính sách bảo mật tuân thủ OWASP Top 10, mã hóa dữ liệu ở nghỉ bằng AES-256, và TLS 1.3 cho mọi giao tiếp. Hệ thống hỗ trợ đa ngôn ngữ (EN, VN, ES) với i18n middleware và hreflang cho SEO. Các quy trình CI/CD được tự động hóa qua GitHub Actions, với các giai đoạn build, test, container image push, và triển khai lên GKE.

###### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
Mô tả chi tiết về các kênh bất đồng bộ, cổng nhập liệu (ingestion gateway), topology chủ đề, và kiến trúc fan-out cho các hệ thống ngoại vi. Hệ thống sử dụng Apache Kafka làm backbone cho các luồng sự kiện bất đồng bộ: chủ đề `qr-attendance` ghi nhận sự kiện quét mã QR từ ứng dụng di động; chủ đề `notifications` truyền tải thông báo push và tin nhắn Zalo; chủ đề `enrollments` ghi lại các đăng ký khóa học. Các cổng nhập liệu (ingestion gateway) tại lớp API biên (edge) nhận yêu cầu từ client, xác thực JWT, sau đó ghi vào Kafka chủ đề tương ứng. Các consumer xử lý song song: service điểm danh xử lý `qr-attendance` để ghi vào PostgreSQL với tính chất idempotent; service thông báo đẩy vào FCM/APNs và gửi tin nhắn Zalo dựa trên chủ đề `notifications`. Các hệ thống phân tích (analytics) đọc từ Kafka để tạo báo cáo điểm danh hàng ngày và cập nhật dashboard. Các tích hợp bên ngoài (Zalo API, Firebase Auth) được thực hiện qua HTTP client bất đồng bộ, với retry circuit-breaker để đảm bảo độ tin cậy. Cache Redis được sử dụng cho session user và token blacklist, với TTL phù hợp. Các luồng này được giám sát bởi hệ thống logging tập trung (ELK) và alerting qua Prometheus/Grafana.

#### 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21 (LTS), Quarkus 3.2.0, Hibernate ORM, PostgreSQL 15, Docker 23.x, Kubernetes 1.27+, Firebase Authentication SDK, Google Cloud Messaging (FCM) SDK, Apple APNs SDK, Zalo API v2, Redis 7, Flyway, GitHub Actions, Maven 3.9.

- **Frontend & Cross-Platform UI Mobile Stack:** Node.js 20, npm 9, Next.js 14 (React 18), TypeScript, Tailwind CSS, React Native 0.73, Expo, Capacitor, i18next, react-i18next, Jest, React Testing Library, Docker (cho môi trường phát triển).

###### ARCHITECTURAL STACK MATRIX

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

#### 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** Toàn bộ mã nguồn và cấu hình phải nằm dưới thư mục gốc dự án `.`. Tất cả các đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Áp dụng quy tắc tiền tố thư mục linh hoạt: `./sources/backend.<service-name>` cho logic backend, `./sources/frontend` cho giao diện web, `./sources/frontend.<app-name>` cho ứng dụng di động, `./sources/infra` cho cấu hình DevOps.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** Tất cả mã Java phải được đóng gói trong `org.nlh4j.saas.membershiphub`. Tên dự án được chuẩn hóa thành dạng chữ thường, không dấu, không gạch ngang.
- **Strict Tester Target Path Syntax:** Bất kỳ thành phần nào được Tester nhắm đến phải được biểu diễn dưới dạng cặp bán phẩy `<source_component>;<test_suite_file>`, ví dụ: `./sources/backend.user-management;src/test/java/org/nlh4j/saas/membershiphub/user/RegistrationTest.java`.

#### 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

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

#### 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

###### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
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

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
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

###### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
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

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
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

###### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
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

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
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

###### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
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

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
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

###### 📈 Phase 5 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai DevOps, containerization, triển khai lên GKE, và đảm bảo tuân thủ các yêu cầu phi chức năng (bảo mật, hiệu suất, khả năng phục hồi). Xây dựng pipeline CI/CD, image Docker, cấu hình cloud, và các biện pháp bảo mật.
- **Target Physical Directory Matrix Map:**
    *   `./sources/infra [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
    *   `./sources/docs/phase5_architecture.md [ARC-010], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
- **Database Schema DDL SQL Specification:** (none needed)

- **API and Event Routing Contracts:** (none needed)

- **Phase Localized Exception Handlers:** (none needed)

######## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
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

#### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-001]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng Prepared Statements với JDBC, Hibernate Criteria API, hoặc QueryDSL. Áp dụng Whitelist cho các giá trị sắp xếp (ví dụ: sortBy ∈ {“name”, “date”, “id”}). Áp dụng ORM mapping an toàn, không cho phép raw SQL.

- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Áp dụng auto-escaping trong Thymeleaf (cho Java) và React (JSX). Sử dụng helmet CSP cho frontend, đặt header `Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'` chỉ cho các script cần thiết. Áp dụng validation đầu vào cho các trường HTML.

- **Multi-Tenant CORS Security Rails:** Cấu hình CORS cho từng tenant dựa trên origin, sử dụng `Access-Control-Allow-Origin` động với whitelist. Xác thực tenant qua JWT claim `tenant_id`. Áp dụng same-origin cho các API nội bộ.

- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Sử dụng interceptor `@LogSanitization` để xóa thông tin nhạy cảm (email, SSN) trước khi ghi log. Áp dụng `@JsonSerialize` với `JsonInclude.Include.NON_NULL`. Thiết lập threshold cho độ dài log, tự động che giấu các trường PII bằng `***`.

#### 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng @capacitor/core để quản lý file hệ thống, lưu trữ an toàn với @capacitor/preferences, chặn back-button với native plugin, fetch data qua API với timeout và retry. Áp dụng URL scheme cho deep linking (app://course/123). Áp dụng caching với IndexedDB thông qua Capacitor Storage.

- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware phát hiện locale từ cookie, header Accept-Language, fallback sang default (EN). Sử dụng react-i18next với namespace cho từng phần. Tự động generate hreflang links: `<link rel="alternate" hreflang="en" href="https://example.com/en/page"/>`. Sử dụng schema.org cho các cấu trúc dữ liệu đa ngôn ngữ.

#### 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Mỗi ngày tạo branch mới `features/development-phase-X-day-Y` (X là số phase, Y là số ngày). Sử dụng git fork từ `main` để đảm bảo isolation.

- **Validation Guard Pipeline Gates:** Sau khi merge, GitHub Actions chạy các bước: `mvn clean verify` (hoặc `npm test`), kiểm tra độ phủ sóng >=85%, kiểm tra style (Spotless), kiểm tra bảo mật (Snyk). Chỉ cho phép merge khi tất cả các gate vượt qua.

###### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`

