# SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub

## 1. PROJECT OVERVIEW & GLOBAL ARCHITECTURE

### 1.1 Product Objectives & Core Values
- Cung cấp nền tảng quản lý hội viên đa trung tâm thống nhất.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên số với tính năng đếm ngày hiệu lực.
- Hỗ trợ truyền thông đa kênh (web, mobile, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

### 1.2 Target User Personas
- **System Admin** (toàn quyền trên toàn hệ thống)
- **Center Admin** (toàn quyền trong trung tâm của mình, không ảnh hưởng các trung tâm khác)
- **Manager** (phụ trách, quyền hạn hạn chế)
- **Teacher** (chỉ đọc lịch học)
- **Student** (duyệt khóa học, ghi danh, xem thẻ hội viên)
- **Mobile App User** (giống các vai trò trên, giao diện phản hồi)

### 1.3 Global Role‑Based Access Control (RBAC) Matrix
- [ARC-001] System Admin: toàn quyền across all centers.
- [ARC-002] Center Admin: toàn quyền trong own center, cannot affect other centers.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc gán giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày hiệu lực còn lại), gia hạn thẻ.

### 1.4 Global Tech Stack Constraints & Infrastructure Blueprint [ARC-010]
- Next.js (frontend), NestJS (backend), PostgreSQL (DB), Docker, Kubernetes (GKE), OAuth2 / JWT, Firebase Auth, Zalo API, Redis (cache), CI/CD (GitHub Actions), monitoring (Prometheus + Grafana), observability (ELK), multi‑tenant isolation via schema per center.

## 2. ENHANCED EPIC MODULES

### 2.1 User Management

#### Core Functional Requirements
- **[REQ-001]** Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
  - **Acceptance Criteria**:
    - Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. *[REQ-001]*
  - **Data Inputs & Field Validations**:
    - Email: required, max 255 ký tự, phải chứa đúng một ký tự ‘@’ và một phần tên miền. Phải là duy nhất.
    - Password: required, min 8 ký tự, ít nhất một ký tự hoa, một ký tự thường, một chữ số, một ký tự đặc biệt.
    - Terms: required checkbox.

- **[REQ-002]** Xác thực xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
  - **Acceptance Criteria**:
    - Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. *[REQ-002]*
  - **Data Inputs & Field Validations**: provider token, optional profile picture.

- **[REQ-003]** Gán vai trò người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.
  - **Acceptance Criteria**:
    - Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. *[REQ-003]*
  - **Data Inputs & Field Validations**: Role dropdown, audit log entry required.

#### Module Exception Flows
- **[EXC-001]** Mất kết nối mạng trong quá trình đăng ký: If a user initiates registration but network is unavailable, When the app retries the request after reconnection, Then the registration is completed once the service is reachable.
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.

#### Module Localized Data Dictionary
- **[DAT-001]** Users
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | user_id | uuid | PK, not null | Unique identifier |
  | email | varchar | not null, unique | Primary login identifier |
  | password_hash | char | not null | bcrypt hash |
  | full_name | varchar | not null | Real name |
  | role_id | smallint | FK → Roles.role_id | Assigned role |
  | provider | enum | default 'local' | Auth provider |
  | created_at | timestamp | not null, default now() | Account creation |
  | updated_at | timestamp | not null, default now() | Last update |
  ```erDiagram
      USERS ||--o{ ROLES : has_role
      USERS ||--o{ CENTERS : manages_center
      USERS ||--o{ COURSES : teaches_course
      USERS ||--o{ ENROLLMENTS : enrolls_in
      USERS ||--o{ ATTENDANCE : records_attendance
      USERS ||--o{ STUDENTCARDS : owns_card
      USERS ||--o{ NOTIFICATIONS : sends_notification
  ```
- **[DAT-002]** Roles
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | role_id | smallint | PK | Role identifier |
  | name | varchar | unique, not null | Role name |
  | description | varchar | optional | Role description |
  ```erDiagram
      ROLES ||--o{ USERS : has_user
  ```

### 2.2 Center Management

#### Core Functional Requirements
- **[REQ-004]** Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
  - **Acceptance Criteria**:
    - Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. *[REQ-004]*
  - **Data Inputs & Field Validations**: None (read‑only).

- **[REQ-005]** Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
  - **Acceptance Criteria**:
    - Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. *[REQ-005]*
  - **Data Inputs & Field Validations**:
    - Name: required, max 100 ký tự.
    - Address: required, max 255 ký tự.
    - TaxID: required, numeric, 10‑13 digits, unique.
    - Contact Phone: optional, có thể bao gồm +, digits, spaces, hyphens, parentheses.
    - Contact Email: optional, phải là email hợp lệ.

- **[REQ-006]** Gán quản trị viên trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.
  - **Acceptance Criteria**:
    - Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. *[REQ-006]*
  - **Data Inputs & Field Validations**: User ID, Center ID.

#### Module Exception Flows
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: tax_id trùng lặp): If duplicate tax ID exists, When the save action is executed, Then the operation fails with a conflict error.
- **[EXC-005]** System recovery after outage: If the service becomes unavailable, When it restores, Then any pending center updates are processed in FIFO order, and users receive a notification.

#### Module Localized Data Dictionary
- **[DAT-003]** Centers
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | center_id | uuid | PK, not null | Unique identifier |
  | name | varchar | not null | Center name |
  | address | varchar | not null | Physical address |
  | tax_id | varchar | unique, not null | Tax identification number |
  | contact_phone | varchar | optional | Contact telephone |
  | contact_email | varchar | optional | Contact email |
  ```erDiagram
      CENTERS ||--o{ USERS : admin_user
  ```

### 2.3 Course Management

#### Core Functional Requirements
- **[REQ-007]** Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
  - **Acceptance Criteria**:
    - Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. *[REQ-007]*
  - **Data Inputs & Field Validations**: None.

- **[REQ-008]** Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
  - **Acceptance Criteria**:
    - Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. *[REQ-008]*
  - **Data Inputs & Field Validations**:
    - Title: required, max 150 ký tự.
    - StartDate/EndDate: required, EndDate >= StartDate.
    - TeacherID: required, khóa ngoại.
    - Overlap check logic enforced at DB/trigger level.

- **[REQ-009]** Gán giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.
  - **Acceptance Criteria**:
    - Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. *[REQ-009]*
  - **Data Inputs & Field Validations**: CourseID, TeacherID (phải tồn tại).

#### Module Exception Flows
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: ngày bắt đầu > ngày kết thúc): If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.
- **[EXC-001]** Mất kết nối mạng trong quá trình gán giáo viên: If a teacher assignment request is made but network is unavailable, When the app retries after reconnection, Then the assignment is completed once the service is reachable.

#### Module Localized Data Dictionary
- **[DAT-004]** Courses
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | course_id | uuid | PK, not null | Unique identifier |
  | title | varchar | not null | Course name |
  | description | text | optional | Detailed description |
  | start_date | date | not null | Course start |
  | end_date | date | not null | Course end |
  | teacher_id | uuid | FK → Users.user_id | Assigned teacher |
  | max_students | int | default 30 | Capacity |
  ```erDiagram
      COURSES ||--o{ USERS : teaches_course
      COURSES ||--o{ ENROLLMENTS : has_enrollment
  ```

### 2.4 Student Enrollment & Registration

#### Core Functional Requirements
- **[REQ-010]** Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
  - **Acceptance Criteria**:
    - Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. *[REQ-010]*
  - **Data Inputs & Field Validations**: None.

- **[REQ-011]** Đăng ký khóa học: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.
  - **Acceptance Criteria**:
    - Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. *[REQ-011]*
  - **Data Inputs & Field Validations**:
    - CourseID: required, must be active.
    - StudentID: derived from authentication token (or created on‑the‑fly).

#### Module Exception Flows
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: course_id không tồn tại): If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.
- **[EXC-002]** Gửi đăng ký trùng lặp: If the same student attempts to enroll in the same course again, When the system detects a duplicate, Then it returns a success response indicating ‘already enrolled’ and does not create extra rows.

#### Module Localized Data Dictionary
- **[DAT-005]** Enrollments
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | enrollment_id | uuid | PK, not null | Unique identifier |
  | student_id | uuid | FK → Users.user_id | Enrolled student |
  | course_id | uuid | FK → Courses.course_id | Course |
  | enrollment_date | timestamp | default now() | When enrolled |
  ```erDiagram
      ENROLLMENTS ||--o{ USERS : enrolls_in
      ENROLLMENTS ||--o{ COURSES : enrolls_in
  ```

### 2.5 Attendance & QR Scanning

#### Core Functional Requirements
- **[REQ-012]** Chụp ảnh QR điểm danh: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
  - **Acceptance Criteria**:
    - Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. *[REQ-012]*
  - **Data Inputs & Field Validations**:
    - QR payload: base64 encoded string containing studentID and courseID.
    - Validation: student must be enrolled in the course for the day.

- **[REQ-013]** Đảm bảo tính duy nhất điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.
  - **Acceptance Criteria**:
    - Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. *[REQ-013]*

#### Module Exception Flows
- **[EXC-001]** Mất kết nối mạng trong quá trình quét QR: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- **[EXC-002]** Gửi điểm danh trùng lặp: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Module Localized Data Dictionary
- **[DAT-006]** Attendance
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | attendance_id | uuid | PK, not null | Unique identifier |
  | student_id | uuid | FK → Users.user_id | Student present |
  | course_id | uuid | FK → Courses.course_id | Course attended |
  | attendance_date | date | not null | Date of attendance |
  | timestamp | timestamp | default now() | Exact time recorded |
  ```erDiagram
      ATTENDANCE ||--o{ USERS : records_attendance
      ATTENDANCE ||--o{ COURSES : records_attendance
  ```

### 2.6 Student Card Management

#### Core Functional Requirements
- **[REQ-014]** Hiển thị hiệu lực thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
  - **Acceptance Criteria**:
    - Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. *[REQ-014]*
  - **Data Inputs & Field Validations**: None (read‑only).

- **[REQ-015]** Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.
  - **Acceptance Criteria**:
    - Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. *[REQ-015]*
  - **Data Inputs & Field Validations**:
    - RenewalDays: integer, 1‑365.
    - Payment gateway integration required (outside scope).

#### Module Exception Flows
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: renewal days > 365): If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.

#### Module Localized Data Dictionary
- **[DAT-007]** StudentCards
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | card_id | uuid | PK, not null | Unique identifier |
  | student_id | uuid | FK → Users.user_id | Owner |
  | issue_date | date | not null | Card issue date |
  | validity_days | int | not null | Total validity days |
  | remaining_days | int | computed | Days left until expiry |
  ```erDiagram
      STUDENTCARDS ||--o{ USERS : owns_card
  ```

### 2.7 Notifications & Communications

#### Core Functional Requirements
- **[REQ-016]** Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.
  - **Acceptance Criteria**:
    - Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. *[REQ-016]*
  - **Data Inputs & Field Validations**: Target audience (student, teacher, group), message content, optional media.

- **[REQ-021]** Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.
  - **Acceptance Criteria**:
    - Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. *[REQ-021]*

#### Module Exception Flows
- **[EXC-003]** Giao hàng thông báo không thành công: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Module Localized Data Dictionary
- **[DAT-008]** Notifications
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | notification_id | uuid | PK, not null | Unique identifier |
  | user_id | uuid | FK → Users.user_id (optional) | Target user |
  | group_zalo | varchar | optional | Target Zalo group |
  | message | text | not null | Notification content |
  | sent_at | timestamp | default now() | When sent |
  | delivered | boolean | default false | Delivery status |
  ```erDiagram
      NOTIFICATIONS ||--o{ USERS : sends_notification
  ```

### 2.8 Promotions & Announcements Management

#### Core Functional Requirements
- **[REQ-017]** Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
  - **Acceptance Criteria**:
    - Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. *[REQ-017]*
  - **Data Inputs & Field Validations**:
    - Name: required, max 100 ký tự.
    - StartDate/EndDate: optional, định dạng YYYY‑MM‑DD.
    - Description: max 500 ký tự.

- **[REQ-018]** Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.
  - **Acceptance Criteria**:
    - Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. *[REQ-018]*
  - **Data Inputs & Field Validations**:
    - Title: required, max 150 ký tự.
    - Content: required, max 2000 ký tự.

#### Module Exception Flows
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: tên khuyến mãi trống): If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.

#### Module Localized Data Dictionary
- **[DAT-009]** Promotions
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | promo_id | uuid | PK, not null | Unique identifier |
  | code | varchar | unique | Discount code |
  | discount_percent | smallint | not null | Discount percentage |
  | start_date | date | optional | Promotion start |
  | end_date | date | optional | Promotion end |
  | description | text | optional | Promo details |
  ```erDiagram
      PROMOTIONS ||--o{ USERS : applies_to
  ```
- **[DAT-010]** Announcements
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | announcement_id | uuid | PK, not null | Unique identifier |
  | title | varchar | not null | Title |
  | content | text | not null | Content |
  | start_date | date | optional | Effective start |
  | end_date | date | optional | Effective end |
  ```erDiagram
      ANNOUNCEMENTS ||--o{ USERS : broadcasts_to
  ```

### 2.9 AI Customer Service Chatbot

#### Core Functional Requirements
- **[REQ-019]** Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.
  - **Acceptance Criteria**:
    - Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. *[REQ-019]*
  - **Data Inputs & Field Validations**: Input text, session timeout.

#### Module Exception Flows
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: tin nhắn rỗng): If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.

### 2.10 Mobile App Core Features

#### Core Functional Requirements
- **[REQ-020]** Giao diện người dùng theo vai trò trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
  - **Acceptance Criteria**:
    - Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. *[REQ-020]*
  - **Data Inputs & Field Validations**: None.

- **[REQ-021]** Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.
  - **Acceptance Criteria**:
    - Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. *[REQ-021]*

#### Module Exception Flows
- **[EXC-003]** Giao hàng thông báo không thành công: (same as above)

### 2.11 Localization & SEO

#### Core Functional Requirements
- **[REQ-022]** Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
  - **Acceptance Criteria**:
    - Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. *[REQ-022]*
  - **Data Inputs & Field Validations**: None.

- **[REQ-023]** SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.
  - **Acceptance Criteria**:
    - Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. *[REQ-023]*
  - **Data Inputs & Field Validations**: Language codes (en, vi, es).

#### Module Exception Flows
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: mã ngôn ngữ không hỗ trợ): If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.

### 2.12 Reporting & Analytics

#### Core Functional Requirements
- **[REQ-024]** Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
  - **Acceptance Criteria**:
    - Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. *[REQ-024]*
  - **Data Inputs & Field Validations**:
    - Date range: start ≤ end, max 30 days.

- **[REQ-025]** Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.
  - **Acceptance Criteria**:
    - Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). *[REQ-025]*
  - **Data Inputs & Field Validations**: Refresh interval configurable (default 15 minutes).

#### Module Exception Flows
- **[EXC-005]** System recovery after outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

## 3. EXCEPTION FLOWS & EDGE CASES

- **[EXC-001]** Mất kết nối mạng trong quá trình quét QR:
  - If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.

- **[EXC-002]** Gửi điểm danh trùng lặp:
  - If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

- **[EXC-003]** Giao hàng thông báo không thành công:
  - When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: malformed email, missing required fields):
  - If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.

- **[EXC-005]** System recovery after outage:
  - If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

## 4. GLOBAL NON-FUNCTIONAL REQUIREMENTS

- **[NFR-001]** Performance Metrics:
  - Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency.
  - Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.

- **[NFR-002]** Availability:
  - Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.

- **[NFR-003]** Security:
  - All data in transit must use TLS 1.3; at rest encryption with AES‑256.
  - JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry.
  - Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).

- **[NFR-004]** Scalability & Availability:
  - Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms.
  - PostgreSQL read replicas for reporting workloads.

- **[NFR-005]** Docker Image Size:
  - Base image size < 200 MB; final image < 500 MB.

- **[NFR-006]** Logging & Audit:
  - All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.

- **[NFR-007]** Multi‑Language Support:
  - UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.

- **[NFR-008]** GDPR/CCPA Compliance:
  - Personal data deletion on user request; data export in JSON format; consent management for marketing communications.

- **[NFR-009]** Backup & Disaster Recovery:
  - Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.

## 5. GLOBAL DATA DICTIONARY

- **[DAT-011]** SystemSettings
  | Field | Data Type | Constraints | Description |
  |-------|-----------|-------------|-------------|
  | setting_key | varchar | PK | Configuration key |
  | setting_value | text | not null | Configuration value |
  | description | varchar | optional | Meaning of setting |
  ```erDiagram
      SYSTEMSETTINGS ||--o{ USERS : owns_setting
  ```

[EXECUTION_REMEDIATION_PAYLOAD_START]
{
  "technical_codename": "membership-hub",
  "descriptive_name": "Membership Hub Platform",
  "brand_name": "MemberHub",
  "requirement_tags": ["[REQ-001]","[REQ-002]","[REQ-003]","[REQ-004]","[REQ-005]","[REQ-006]","[REQ-007]","[REQ-008]","[REQ-009]","[REQ-010]","[REQ-011]","[REQ-012]","[REQ-013]","[REQ-014]","[REQ-015]","[REQ-016]","[REQ-017]","[REQ-018]","[REQ-019]","[REQ-020]","[REQ-021]","[REQ-022]","[REQ-023]","[REQ-024]","[REQ-025]","[EXC-001]","[EXC-002]","[EXC-003]","[EXC-004]","[EXC-005]","[ARC-001]","[ARC-002]","[ARC-003]","[ARC-004]","[ARC-005]","[ARC-006]","[ARC-007]","[ARC-008]","[ARC-009]","[ARC-010]","[NFR-001]","[NFR-002]","[NFR-003]","[NFR-004]","[NFR-005]","[NFR-006]","[NFR-007]","[NFR-008]","[NFR-009]","[DAT-001]","[DAT-002]","[DAT-003]","[DAT-004]","[DAT-005]","[DAT-006]","[DAT-007]","[DAT-008]","[DAT-009]","[DAT-010]","[DAT-011]"]
}