## 1. PROJECT OVERVIEW
- **Product Objectives & Core Values**
  - Provide a unified platform for multi‑center membership management.
  - Enable real‑time attendance tracking via QR code scanning.
  - Offer digital membership cards with validity counting.
  - Facilitate multi‑channel communication (web, mobile, Zalo groups).
  - Core values: reliability, scalability, security, user‑friendliness, multilingual support.
- **Target User Personas**
  - System Admin (global super‑user)
  - Center Admin (center‑level manager)
  - Manager (sub‑admin, limited rights)
  - Teacher (read‑only course schedule)
  - Student (course browsing, enrollment, card view)
  - Mobile App User (same personas, responsive UI)
- **Role‑Based Access Control (RBAC) Matrix**
  - [ARC-001] System Admin: full permissions across all centers.
  - [ARC-002] Center Admin: full permissions within own center, cannot affect other centers.
  - [ARC-003] Manager: can create announcements, manage students, assign existing students to courses, view course list, cannot edit courses or assign teachers.
  - [ARC-004] Teacher: view own courses, student lists, schedule; read‑only.
  - [ARC-005] Student: browse courses, register for new courses, view own membership card (remaining days), renew card days.
- **Architecture & Data Flow (key flows)**
  - [ARC-006] Authentication Flow: supports email/password, Firebase, Google, Facebook via OAuth2; issues JWT tokens with 15‑minute expiry and refresh tokens.
  - [ARC-007] Attendance QR Processing Flow: mobile app scans QR, sends student ID and timestamp to backend; service validates and records attendance idempotently.
  - [ARC-008] Notification Delivery Flow: system triggers push notifications to mobile apps and posts to designated Zalo groups for announcements, course assignments, and attendance alerts.
  - [ARC-009] Mobile App Backend Integration Flow: Next.js frontend consumes REST APIs; authentication via bearer tokens; supports offline caching for limited connectivity.

## 2. FUNCTIONAL REQUIREMENTS

### 2.1 User Management
- **[REQ-001]** User Registration: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
  - **Acceptance Criteria**:
    - Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. *[REQ-001]*
  - **Data Inputs & Field Validations**:
    - Email: required, max 255 chars, must contain a single ‘@’ and a domain part (e.g., user@example.com). Must be unique.
    - Password: required, min 8 chars, at least one uppercase, one lowercase, one digit, one special character.
    - Terms: required checkbox.
- **[REQ-002]** Social Authentication: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
  - **Acceptance Criteria**:
    - Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. *[REQ-002]*
  - **Data Inputs & Field Validations**: provider token, optional profile picture.
- **[REQ-003]** User Role Assignment: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.
  - **Acceptance Criteria**:
    - Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. *[REQ-003]*
  - **Data Inputs & Field Validations**: Role dropdown, audit log entry required.

### 2.2 Center Management
- **[REQ-004]** Center List View: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
  - **Acceptance Criteria**:
    - Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. *[REQ-004]*
  - **Data Inputs & Field Validations**: None (read‑only).
- **[REQ-005]** Center Create/Update/Delete: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
  - **Acceptance Criteria**:
    - Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. *[REQ-005]*
  - **Data Inputs & Field Validations**:
    - Name: required, max 100 chars.
    - Address: required, max 255 chars.
    - TaxID: required, numeric, 10‑13 digits, unique.
    - Contact Phone: optional, may include +, digits, spaces, hyphens, parentheses.
    - Contact Email: optional, must be valid email format.
- **[REQ-006]** Center Admin Assignment: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.
  - **Acceptance Criteria**:
    - Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. *[REQ-006]*
  - **Data Inputs & Field Validations**: User ID, Center ID.

### 2.3 Course Management
- **[REQ-007]** Course List View: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
  - **Acceptance Criteria**:
    - Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. *[REQ-007]*
  - **Data Inputs & Field Validations**: None.
- **[REQ-008]** Course Create/Update/Delete (Conflict Avoidance): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
  - **Acceptance Criteria**:
    - Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. *[REQ-008]*
  - **Data Inputs & Field Validations**:
    - Title: required, max 150 chars.
    - StartDate/EndDate: required, EndDate >= StartDate.
    - TeacherID: required, foreign key.
    - Overlap check logic enforced at DB/trigger level.
- **[REQ-009]** Teacher Assignment to Course: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.
  - **Acceptance Criteria**:
    - Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. *[REQ-009]*
  - **Data Inputs & Field Validations**: CourseID, TeacherID (must exist).

### 2.4 Student Enrollment & Registration
- **[REQ-010]** Course Browse: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
  - **Acceptance Criteria**:
    - Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. *[REQ-010]*
  - **Data Inputs & Field Validations**: None.
- **[REQ-011]** Student Course Registration: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.
  - **Acceptance Criteria**:
    - Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. *[REQ-011]*
  - **Data Inputs & Field Validations**:
    - CourseID: required, must be active.
    - StudentID: derived from authentication token (or created on‑the‑fly).

### 2.5 Attendance & QR Scanning
- **[REQ-012]** QR Attendance Capture: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
  - **Acceptance Criteria**:
    - Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. *[REQ-012]*
  - **Data Inputs & Field Validations**:
    - QR payload: base64 encoded string containing studentID and courseID.
    - Validation: student must be enrolled in the course for the day.
- **[REQ-013]** Attendance Idempotency: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.
  - **Acceptance Criteria**:
    - Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. *[REQ-013]*
  - **Data Inputs & Field Validations**: Unique composite key (StudentID, CourseID, Date).

### 2.6 Student Card Management
- **[REQ-014]** Card Validity Display: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
  - **Acceptance Criteria**:
    - Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. *[REQ-014]*
  - **Data Inputs & Field Validations**: None (read‑only).
- **[REQ-015]** Card Renewal: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.
  - **Acceptance Criteria**:
    - Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. *[REQ-015]*
  - **Data Inputs & Field Validations**:
    - RenewalDays: integer, 1‑365.
    - Payment gateway integration required (outside scope).

### 2.7 Notifications & Communications
- **[REQ-016]** Notification Trigger: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.
  - **Acceptance Criteria**:
    - Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. *[REQ-016]*
  - **Data Inputs & Field Validations**: Target audience (student, teacher, group), message content, optional media.

### 2.8 Promotions & Announcements Management
- **[REQ-017]** Promotion Management: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
  - **Acceptance Criteria**:
    - Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. *[REQ-017]*
  - **Data Inputs & Field Validations**:
    - Name: required, max 100 chars.
    - StartDate/EndDate: optional, date format YYYY‑MM‑DD.
    - Description: max 500 chars.
- **[REQ-018]** Announcement Management: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.
  - **Acceptance Criteria**:
    - Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. *[REQ-018]*
  - **Data Inputs & Field Validations**:
    - Title: required, max 150 chars.
    - Content: required, max 2000 chars.

### 2.9 AI Customer Service Chatbot
- **[REQ-019]** AI Chatbot Integration: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.
  - **Acceptance Criteria**:
    - Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. *[REQ-019]*
  - **Data Inputs & Field Validations**: Input text, session timeout.

### 2.10 Mobile App Core Features
- **[REQ-020]** Mobile App Role‑Specific UI: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
  - **Acceptance Criteria**:
    - Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. *[REQ-020]*
  - **Data Inputs & Field Validations**: None.
- **[REQ-021]** Mobile Push Notifications: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.
  - **Acceptance Criteria**:
    - Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. *[REQ-021]*
  - **Data Inputs & Field Validations**: DeviceToken, Platform (iOS/Android).

### 2.11 Localization & SEO
- **[REQ-022]** Default Locale Detection: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
  - **Acceptance Criteria**:
    - Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. *[REQ-022]*
  - **Data Inputs & Field Validations**: None.
- **[REQ-023]** Multi‑Language SEO: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.
  - **Acceptance Criteria**:
    - Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. *[REQ-023]*
  - **Data Inputs & Field Validations**: Language codes (en, vi, es).

### 2.12 Reporting & Analytics
- **[REQ-024]** Attendance Report Generation: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
  - **Acceptance Criteria**:
    - Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. *[REQ-024]*
  - **Data Inputs & Field Validations**:
    - Date range: start ≤ end, max 30 days.
- **[REQ-025]** Enrollment Summary Dashboard: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.
  - **Acceptance Criteria**:
    - Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). *[REQ-025]*
  - **Data Inputs & Field Validations**: Refresh interval configurable (default 15 minutes).

## 3. EXCEPTION FLOWS & EDGE CASES
- **[EXC-001]** Network & Connectivity Drops During QR Scan:
  - If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- **[EXC-002]** Duplicate Attendance Submission:
  - If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.
- **[EXC-003]** Failed Notification Delivery:
  - When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.
- **[EXC-004]** Invalid Input Validation (e.g., malformed email, missing required fields):
  - If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.
- **[EXC-005]** System Recovery After Outage:
  - If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

## 4. NON-FUNCTIONAL REQUIREMENTS
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

## 5. PRELIMINARY DATA DICTIONARY
| Entity | Field | Data Type | Constraints | Description |
|--------|-------|-----------|-------------|-------------|
| Users | user_id | UUID | PK, not null | Unique identifier |
| | email | VARCHAR(255) | not null, unique | Primary login identifier |
| | password_hash | CHAR(60) | not null | bcrypt hash |
| | full_name | VARCHAR(100) | not null | Real name |
| | role_id | SMALLINT | FK → Roles.role_id | Assigned role |
| | provider | ENUM('local','firebase','google','facebook') | default 'local' | Auth provider |
| | created_at | TIMESTAMP | not null, default now() | Account creation |
| | updated_at | TIMESTAMP | not null, default now() | Last update |
| Centers | center_id | UUID | PK, not null | Unique identifier |
| | name | VARCHAR(100) | not null | Center name |
| | address | VARCHAR(255) | not null | Physical address |
| | tax_id | VARCHAR(20) | unique, not null | Tax identification number |
| | contact_phone | VARCHAR(20) | optional | Contact telephone |
| | contact_email | VARCHAR(100) | optional | Contact email |
| Courses | course_id | UUID | PK, not null | Unique identifier |
| | title | VARCHAR(150) | not null | Course name |
| | description | TEXT | optional | Detailed description |
| | start_date | DATE | not null | Course start |
| | end_date | DATE | not null | Course end |
| | teacher_id | UUID | FK → Users.user_id | Assigned teacher |
| | max_students | INT | default 30 | Capacity |
| Enrollments | enrollment_id | UUID | PK, not null | Unique identifier |
| | student_id | UUID | FK → Users.user_id | Enrolled student |
| | course_id | UUID | FK → Courses.course_id | Course |
| | enrollment_date | TIMESTAMP | default now() | When enrolled |
| Attendance | attendance_id | UUID | PK, not null | Unique identifier |
| | student_id | UUID | FK → Users.user_id | Student present |
| | course_id | UUID | FK → Courses.course_id | Course attended |
| | attendance_date | DATE | not null | Date of attendance |
| | timestamp | TIMESTAMP | default now() | Exact time recorded |
| StudentCards | card_id | UUID | PK, not null | Unique identifier |
| | student_id | UUID | FK → Users.user_id | Owner |
| | issue_date | DATE | not null | Card issue date |
| | validity_days | INT | not null | Total validity days |
| | remaining_days | INT | computed | Days left until expiry |
| Notifications | notification_id | UUID | PK, not null | Unique identifier |
| | user_id | UUID | FK → Users.user_id (optional) | Target user |
| | group_zalo | VARCHAR(50) | optional | Target Zalo group |
| | message | TEXT | not null | Notification content |
| | sent_at | TIMESTAMP | default now() | When sent |
| | delivered | BOOLEAN | default false | Delivery status |
| Roles | role_id | SMALLINT | PK | Role identifier |
| | name | VARCHAR(30) | unique, not null | Role name |
| | description | VARCHAR(200) | optional | Role description |
| Promotions | promo_id | UUID | PK, not null | Unique identifier |
| | code | VARCHAR(30) | unique | Discount code |
| | discount_percent | SMALLINT | not null | Discount percentage |
| | start_date | DATE | optional | Promotion start |
| | end_date | DATE | optional | Promotion end |
| | description | TEXT | optional | Promo details |
| Announcements | announcement_id | UUID | PK, not null | Unique identifier |
| | title | VARCHAR(150) | not null | Title |
| | content | TEXT | not null | Content |
| | start_date | DATE | optional | Effective start |
| | end_date | DATE | optional | Effective end |
| SystemSettings | setting_key | VARCHAR(50) | PK | Configuration key |
| | setting_value | TEXT | not null | Configuration value |
| | description | VARCHAR(200) | optional | Meaning of setting |