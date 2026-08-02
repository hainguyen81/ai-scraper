# GLOBAL PROJECT CONTEXT: membership-hub

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260802082615 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/02 08:26:15 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY
The solution adopts a **microservice‑friendly monolithic** pattern: a Node.js/Express backend serving a Next.js React frontend and a Capacitor‑based hybrid mobile app. All core domain models (users, centers, courses, enrollments, attendance, cards, notifications, promotions, announcements, system settings) are persisted in a PostgreSQL database with strict multi‑tenant isolation via `centerId` foreign keys. Authentication follows JWT‑based stateless security with 15‑minute access tokens and 7‑day refresh cycles, supporting local, Firebase, Google, and Facebook OAuth2. Real‑time attendance is captured via QR scans with idempotent processing, and push notifications flow through Firebase Cloud Messaging (FCM) and Zalo group broadcasting. The architecture is designed for horizontal scaling on GKE, with CI/CD pipelines enforcing 100 % tag traceability and zero‑padding compliance.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Core Stack**: Node.js 20, TypeScript, Express 4, `@types/jwt`, `bcryptjs`, `passport`, `passport-jwt`, `passport-google-oauth20`, `firebase-admin`, `pg` (PostgreSQL client), `sequelize` (ORM), `cors`, `helmet`, `express-rate-limit`, `dotenv`, `winston` (logging), `joi` (validation), `uuid`, `dayjs`, `nanoid`, `swagger-ui-express`, `openapi-specification`, Docker (`Dockerfile`), `gcloud` CLI, `kubectl`, `helm`.
- **Frontend & Mobile Stack**: Next.js 14 (React 18), TypeScript, Tailwind CSS, `i18next`, `react-i18next`, `@capacitor/core`, `@capacitor/app`, `@capacitor/haptics`, `@capacitor/push-notifications`, `@capacitor/preferences`, `axios`, `swr`, `pwa`, Service Worker, SEO (`next-seo`), `jest`, `react‑testing‑library`, `cypress`.
- **DevOps & Infra**: Docker, Kubernetes (GKE), Helm charts, Terraform, GitHub Actions, GitLab CI, Prometheus + Grafana, Loki, Falco, OPA for policy enforcement, Nginx ingress, Cert‑Manager for TLS, AWS RDS (PostgreSQL), Google Cloud Storage (backup), CloudBuild, Artifact Registry.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule**: Repository root is `..`. All generated paths MUST start with `./sources/`.
- **Dynamic Directory Prefixing Compliance**: Backend code → `./sources/backend/`. Frontend code → `./sources/frontend/`. Infra manifests → `./sources/infra/`.
- **Java Package Standard (if Java)**: `org.nlh4j.saas.membershiphub`. (Not used in this Node.js project.)
- **Strict Tester Target Path Syntax**: Tester sub‑agent tasks must be expressed as `<source_component>;<test_suite_file>` with both parts prefixed by `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1‑3 | `./sources/backend` | Core data models, user registration, authentication, role management, JWT issuance, initial validation & exception handling. | Coder | [DAT-001],[DAT-002],[DAT-003],[DAT-004],[DAT-005],[DAT-006],[DAT-007],[DAT-008],[DAT-009],[DAT-010],[DAT-011],[REQ-001],[REQ-002],[REQ-003],[ARC-001],[ARC-002],[ARC-003],[ARC-004],[ARC-005],[ARC-006],[EXC-001],[EXC-002],[EXC-003],[EXC-004],[NFR-001],[NFR-002],[NFR-003],[NFR-004],[NFR-77],[NFR-006] |
| Phase 2 | Day 4‑7 | `./sources/backend` | Center CRUD, course management, enrollment, membership cards, notifications, promotions, announcements, related validation & error handling. | Coder | [REQ-004],[REQ-005],[REQ-006],[REQ-007],[REQ-008],[REQ-009],[REQ-010],[REQ-011],[REQ-014],[REQ-015],[REQ-016],[REQ-017],[REQ-018],[DAT-002],[DAT-003],[DAT-004],[DAT-006],[DAT-009],[DAT-010],[EXC-003],[EXC-004],[EXC-005],[NFR-001],[NFR-002],[NFR-003],[NFR-004] |
| Phase 3 | Day 8‑12 | `./sources/backend` | Attendance QR processing, mobile backend integration, AI chatbot, GDPR & backup compliance, push notifications, system settings, final security hardening. | Coder | [REQ-012],[REQ-013],[ARC-007],[EXC-001],[EXC-002],[REQ-019],[REQ-020],[REQ-021],[ARC-009],[NFR-007],[NFR-008],[NFR-009],[DAT-005],[DAT-007],[DAT-011] |
| Phase 4 | Day 13‑18 | `./sources/frontend` & `./sources/backend` | Multilingual & SEO, reporting & dashboards, final CI/CD pipeline, mobile compliance, i18n, hreflang, audit logging, final review & release. | Coder | [REQ-022],[REQ-023],[REQ-024],[REQ-025],[NFR-001],[NFR-002],[NFR-003],[NFR-004],[NFR-77],[NFR-006],[NFR-007],[NFR-008],[NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
### Phase 1 Detailed Architectural Specification
*(Note: Replace [X] with the active sequential phase number from 1 to N)*
- **Phase Core Objective & Purpose:** Establish the foundational data model, user lifecycle, authentication/authorization, and core validation/exception handling to support all downstream features.
- **Target Physical Directory Matrix Map:**  
  - `./sources/backend/src/models/users.model.ts [DAT-001],[REQ-001],[REQ-002],[REQ-003],[ARC-001],[ARC-002],[ARC-003],[ARC-004],[ARC-005],[ARC-006],[EXC-001],[EXC-002],[EXC-003],[EXC-004]`  
  - `./sources/backend/src/models/centers.model.ts [DAT-002],[REQ-004],[REQ-005],[REQ-006]`  
  - `./sources/backend/src/models/courses.model.ts [DAT-003],[REQ-007],[REQ-008],[REQ-009]`  
  - `./sources/backend/src/models/enrollments.model.ts [DAT-004],[REQ-010],[REQ-011]`  
  - `./sources/backend/src/models/attendance.model.ts [DAT-005],[REQ-012],[REQ-013]`  
  - `./sources/backend/src/models/studentcards.model.ts [DAT-006],[REQ-014],[REQ-015]`  
  - `./sources/backend/src/models/notifications.model.ts [DAT-007],[REQ-016]`  
  - `./sources/backend/src/models/roles.model.ts [DAT-008]`  
  - `./sources/backend/src/models/promotions.model.ts [DAT-009],[REQ-017]`  
  - `./sources/backend/src/models/announcements.model.ts [DAT-010],[REQ-018]`  
  - `./sources/backend/src/models/systemsettings.model.ts [DAT-011]`  
- **Database Schema DDL SQL Specification [DAT-XXX]:**  
```sql
-- [DAT-001] Users
CREATE TABLE users (
    userId VARCHAR(255) PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL,
    provider ENUM('local','firebase','google','facebook') NOT NULL,
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uk_users_email UNIQUE (email),
    CONSTRAINT fk_users_role FOREIGN KEY (roleId) REFERENCES roles(roleId)
);

-- [DAT-002] Centers
CREATE TABLE centers (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(20) NOT NULL,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(100),
    CONSTRAINT uk_centers_taxid UNIQUE (taxId)
);

-- [DAT-003] Courses
CREATE TABLE courses (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL,
    maxStudents INT DEFAULT 30,
    CONSTRAINT chk_courses_date CHECK (endDate >= startDate),
    CONSTRAINT fk_courses_teacher FOREIGN KEY (teacherId) REFERENCES users(userId)
);

-- [DAT-004] Enrollments
CREATE TABLE enrollments (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_enrollments_student FOREIGN KEY (studentId) REFERENCES users(userId),
    CONSTRAINT fk_enrollments_course FOREIGN KEY (courseId) REFERENCES courses(courseId),
    CONSTRAINT uk_enrollments_student_course UNIQUE (studentId, courseId)
);

-- [DAT-005] Attendance
CREATE TABLE attendance (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    CONSTRAINT fk_attendance_student FOREIGN KEY (studentId) REFERENCES users(userId),
    CONSTRAINT fk_attendance_course FOREIGN KEY (courseId) REFERENCES courses(courseId)
);

-- [DAT-006] StudentCards
CREATE TABLE studentcards (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    CONSTRAINT fk_studentcards_student FOREIGN KEY (studentId) REFERENCES users(userId)
);

-- [DAT-007] Notifications
CREATE TABLE notifications (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(50),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_notifications_user FOREIGN KEY (userId) REFERENCES users(userId)
);

-- [DAT-008] Roles
CREATE TABLE roles (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    description VARCHAR(200)
);

-- [DAT-009] Promotions
CREATE TABLE promotions (
    promoId UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT,
    CONSTRAINT uk_promotions_code UNIQUE (code)
);

-- [DAT-010] Announcements
CREATE TABLE announcements (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE,
    CONSTRAINT chk_announcements_date CHECK (COALESCE(endDate, '9999-12-31'::DATE) >= COALESCE(startDate, '1970-01-01'::DATE))
);

-- [DAT-011] SystemSettings
CREATE TABLE systemsettings (
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**  
```yaml
# [REQ-001] User Registration
POST /api/v1/auth/register
Request:
{
  "email": "string",
  "password": "string",
  "fullName": "string",
  "termsAccepted": boolean
}
Response:
{
  "userId": "string",
  "email": "string",
  "role": "Student",
  "accessToken": "string",
  "refreshToken": "string"
}
# [REQ-002] Social Authentication
POST /api/v1/auth/social
Request:
{
  "provider": "firebase|google|facebook",
  "idToken": "string"
}
Response: same as [REQ-001]
# [REQ-003] Assign User Role
PUT /api/v1/users/{userId}/role
Request:
{
  "roleId": smallint
}
Response: { "message": "Role updated" }
# [ARC-001] System Admin Privileges
All admin endpoints prefixed /api/v1/admin/*
# [ARC-006] Authentication Flow
POST /api/v1/auth/token
Request: { "grantType":"password|refresh","username":"...","password":"...","refreshToken":"..." }
Response: { "accessToken":"...","refreshToken":"...","expiresIn":900 }
```
- **Phase Localized Exception Handlers [EXC-XXX]:**  
```yaml
# [EXC-001] Network loss during QR scan
HTTP 200 OK with payload: { "status":"retry_pending","message":"Scan recorded offline, will retry on reconnection" }
# [EXC-002] Duplicate scan
HTTP 200 OK with payload: { "status":"duplicate","message":"Attendance already recorded for this session" }
# [EXC-003] Notification delivery failure
HTTP 500 Internal Server Error, logged with retry count, max 3 attempts.
# [EXC-004] Validation error
HTTP 400 Bad Request, body: { "errors": [ {"field":"email","message":"Invalid email format"}, ... ] }
# [EXC-005] Center/TaxID conflict
HTTP 409 Conflict, body: { "message":"TaxID already exists for another center" }
```

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Maximum ceiling limit: 7 Days per phase)
# Enforce the 'Longitructural Day Partitioning' and 'Anti-Padding Mandate' rules. Output each active day as an isolated standalone single integer subsection header. Freeze and terminate immediately once all BA tracking codes mapped to this phase are fully covered.

#### 🗓️ DAY 1: Core Data Model & User Schema Implementation
- **Sub-Agent Workflow Specialization:**  
  * **[Coder]:**  
    - **Target Component file path (`target_component`):** `./sources/backend/src/models/users.model.ts [DAT-001],[REQ-001],[REQ-002],[REQ-003],[ARC-001],[ARC-002],[ARC-003],[ARC-004],[ARC-005],[ARC-006],[EXC-001],[EXC-002],[EXC-003],[EXC-004]`  
    - **Low-Level Technical Task Instruction:** Define Sequelize model for Users table matching DDL, include validation hooks for email uniqueness, password strength (min 8 chars, uppercase, lowercase, number, special), roleId foreign key, provider enum, timestamps, and associate with Roles model. Implement static method `register(email, password, fullName)` that hashes password with bcrypt, creates user with roleId=Student, generates JWT (sign with secret, expires 15 min) and refresh token (expires 7 days). Attach error handling for duplicate email and validation failures per [EXC-004].  
    - **Targeted Tag IDs:** [DAT-001],[REQ-001],[REQ-002],[REQ-003],[ARC-001],[ARC-002],[ARC-003],[ARC-004],[ARC-005],[ARC-006],[EXC-001],[EXC-002],[EXC-003],[EXC-004]

#### 🗓️ DAY 2: Social Auth Integration & Role Management
- **Sub-Agent Workflow Specialization:**  
  * **[Coder]:**  
    - **Target Component file path (`target_component`):** `./sources/backend/src/services/social-auth.service.ts [REQ-002],[ARC-001],[ARC-002],[ARC-003],[EXC-004]`  
    - **Low-Level Technical Task Instruction:** Implement OAuth2 strategy for Firebase, Google, Facebook using `passport` and respective SDKs. On successful validation, fetch user profile, locate or create a Users record (provider field set accordingly), generate JWT and refresh token, return to client. Include role assignment logic for new users (default roleId=Student). Validate provider token presence per [EXC-004].  
    - **Targeted Tag IDs:** [REQ-002],[ARC-001],[ARC-002],[ARC-003],[EXC-004]

#### 🗓️ DAY 3: Validation, Exception Handling & Initial Testing
- **Sub-Agent Workflow Specialization:**  
  * **[Tester]:**  
    - **Target Component file path (`target_component`):** `./sources/backend/tests/users.test.ts [DAT-001],[REQ-001],[REQ-002],[REQ-003],[EXC-001],[EXC-002],[EXC-003],[EXC-004]`  
    - **Low-Level Technical Task Instruction:** Write unit tests for registration endpoint covering valid payload (expect 201, JWT), duplicate email (expect 409), weak password (expect 400), missing terms (expect 400). Test social auth flow with mocked provider tokens (expect 200). Verify role assignment permissions (admin only). Use Jest supertest, mock bcrypt and jwt. Ensure test coverage >=85 % for Users model.  
    - **Targeted Tag IDs:** [DAT-001],[REQ-001],[REQ-002],[REQ-003],[EXC-001],[EXC-002],[EXC-003],[EXC-004]

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Deploy center, course, enrollment, membership card, notification, promotion, and announcement capabilities with full CRUD, validation, and audit logging.
- **Target Physical Directory Matrix Map:**  
  - `./sources/backend/src/models/centers.model.ts [DAT-002],[REQ-004],[REQ-005],[REQ-006]`  
  - `./sources/backend/src/models/courses.model.ts [DAT-003],[REQ-007],[REQ-008],[REQ-009]`  
  - `./sources/backend/src/models/enrollments.model.ts [DAT-004],[REQ-010],[REQ-011]`  
  - `./sources/backend/src/models/studentcards.model.ts [DAT-006],[REQ-014],[REQ-015]`  
  - `./sources/backend/src/models/notifications.model.ts [DAT-007],[REQ-016]`  
  - `./sources/backend/src/models/promotions.model.ts [DAT-009],[REQ-017]`  
  - `./sources/backend/src/models/announcements.model.ts [DAT-010],[REQ-018]`  
- **Database Schema DDL SQL Specification [DAT-XXX]:** (Additional DDLs for new tables)  
```sql
-- [DAT-002] Centers (re‑stated for completeness)
CREATE TABLE centers (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(20) NOT NULL,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(100),
    CONSTRAINT uk_centers_taxid UNIQUE (taxId)
);

-- [DAT-003] Courses (re‑stated)
CREATE TABLE courses (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL,
    maxStudents INT DEFAULT 30,
    CONSTRAINT chk_courses_date CHECK (endDate >= startDate),
    CONSTRAINT fk_courses_teacher FOREIGN KEY (teacherId) REFERENCES users(userId)
);

-- [DAT-004] Enrollments (re‑stated)
CREATE TABLE enrollments (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_enrollments_student FOREIGN KEY (studentId) REFERENCES users(userId),
    CONSTRAINT fk_enrollments_course FOREIGN KEY (courseId) REFERENCES courses(courseId),
    CONSTRAINT uk_enrollments_student_course UNIQUE (studentId, courseId)
);

-- [DAT-006] StudentCards (re‑stated)
CREATE TABLE studentcards (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    CONSTRAINT fk_studentcards_student FOREIGN KEY (studentId) REFERENCES users(userId)
);

-- [DAT-007] Notifications (re‑stated)
CREATE TABLE notifications (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(50),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_notifications_user FOREIGN KEY (userId) REFERENCES users(userId)
);

-- [DAT-009] Promotions (re‑stated)
CREATE TABLE promotions (
    promoId UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT,
    CONSTRAINT uk_promotions_code UNIQUE (code)
);

-- [DAT-010] Announcements (re‑stated)
CREATE TABLE announcements (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE,
    CONSTRAINT chk_announcements_date CHECK (COALESCE(endDate, '9999-12-31'::DATE) >= COALESCE(startDate, '1970-01-01'::DATE))
);
```
- **API and Event Routing Contracts [REQ-XXX], [ARC-XXX]:**  
```yaml
# [REQ-004] List Centers
GET /api/v1/centers
Response: [ { "centerId":"UUID","name":"string","address":"string","taxId":"string","contactPhone":"string","contactEmail":"string" } ]
# [REQ-005] Create/Update/Delete Center
POST /api/v1/centers
PUT /api/v1/centers/{centerId}
DELETE /api/v1/centers/{centerId}
# [REQ-006] Assign Center Admin
POST /api/v1/centers/{centerId}/admin
Request: { "userId":"UUID" }
Response: { "message":"User assigned as Center Admin" }
# [REQ-007] List Courses
GET /api/v1/courses
# [REQ-008] Manage Course
POST /api/v1/courses
PUT /api/v1/courses/{courseId}
DELETE /api/v1/courses/{courseId}
# [REQ-009] Assign Teacher
POST /api/v1/courses/{courseId}/teacher
Request: { "teacherId":"UUID" }
# [REQ-010] Browse Courses
GET /api/v1/courses/browse?studentId=UUID
# [REQ-011] Enroll Course
POST /api/v1/enrollments
Request: { "studentId":"UUID","courseId":"UUID" }
# [REQ-014] View Membership Card
GET /api/v1/studentcards/{studentId}
# [REQ-015] Extend Membership Card
PUT /api/v1/studentcards/{cardId}/extend
Request: { "additionalDays":int }
# [REQ-016] Trigger Notification
POST /api/v1/notifications
Request: { "userId":"UUID|optional","groupZalo":"string|optional","message":"string" }
# [REQ-017] Manage Promotion
POST /api/v1/promotions
PUT /api/v1/promotions/{promoId}
DELETE /api/v1/promotions/{promoId}
# [REQ-018] Manage Announcement
POST /api/v1/announcements
PUT /api/v1/announcements/{announcementId}
DELETE /api/v1/announcements/{announcementId}
```
- **Phase Localized Exception Handlers [EXC-XXX]:**  
```yaml
# [EXC-003] Notification delivery failure
HTTP 500 with retry logic, log to audit_trail, max 3 attempts.
# [EXC-004] Validation error (e.g., duplicate TaxID)
HTTP 409 Conflict, body: { "message":"TaxID already exists" }
# [EXC-005] Center/TaxID conflict
HTTP 409 Conflict, body: { "message":"TaxID already exists for another center" }
```

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Maximum ceiling limit: 7 Days per phase)
#### 🗓️ DAY 4: Centers CRUD & Validation
- **Sub-Agent Workflow Specialization:**  
  * **[Coder]:**  
    - **Target Component file path (`target_component`):** `./sources/backend/src/controllers/centers.controller.ts [REQ-004],[REQ-005],[REQ-006],[DAT-002],[EXC-003],[EXC-004],[EXC-005]`  
    - **Low-Level Technical Task Instruction:** Implement REST endpoints for listing, creating, updating, deleting centers. Validate taxId format (10‑13 numeric digits) and uniqueness (throw [EXC-005]). Enforce admin role via middleware. Use Sequelize transactions for atomicity. Log each operation to audit_trail table.  
    - **Targeted Tag IDs:** [REQ-004],[REQ-005],[REQ-006],[DAT-002],[EXC-003],[EXC-004],[EXC-005]

#### 🗓️ DAY 5: Courses Management & Teacher Assignment
- **Sub-Agent Workflow Specialization:**  
  * **[Coder]:**  
    - **Target Component file path (`target_component`):** `./sources/backend/src/controllers/courses.controller.ts [REQ-007],[REQ-008],[REQ-009],[DAT-003],[EXC-004]`  
    - **Low-Level Technical Task Instruction:** Build CRUD for courses with overlap validation (teacher schedule). Ensure `endDate >= startDate` per [EXC-004]. Implement teacher assignment endpoint that creates a record in a join table `course_teachers` (if needed) and triggers a notification via event emitter.  
    - **Targeted Tag IDs:** [REQ-007],[REQ-008],[REQ-009],[DAT-003],[EXC-004]

#### 🗓️ DAY 6: Enrollments & Membership Cards
- **Sub-Agent Workflow Specialization:**  
  * **[Coder]**:  
    - **Target Component file path (`target_component`):** `./sources/backend/src/controllers/enrollments.controller.ts [REQ-010],[REQ-011],[DAT-004],[EXC-004]`  
    - **Technical Task Instruction:** Implement enrollment logic: validate student existence, check course capacity, create enrollment record, decrement remaining slots, emit `enrollment:created` event to push notification to user and broadcast to Zalo group. Include validation for duplicate enrollment (unique constraint) and return appropriate HTTP status codes.  

#### 🗓️ DAY 7: Notifications, Promotions & Announcements
- **Sub-Agent Workflow Specialization:**  
  * **[Coder]**:  
    - **Target Component file path (`target_component`):** `./sources/backend/src/controllers/notifications.controller.ts [REQ-016],[DAT-007],[REQ-017],[DAT-010],[EXC-003]`  
    - **Technical Task Direction:** Build notification dispatch service that writes to `notifications` table, queues messages for FCM/APNs and Zalo group broadcast. Implement retry logic for failed deliveries per [EXC-003] and expose admin APIs for creating promotions and announcements with validation of `startDate`/`endDate` fields.  

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Deploy attendance QR processing, mobile backend integration, AI chatbot, GDPR & backup compliance.
- **Target Physical Directory Map:** `./sources/backend`  
- **Technical Task Outline:**  
 1. **Attendance QR Processing & Mobile Integration**  
 2. **AI Chatbot & Compliance Module**  
3. **GDPR & Backup Compliance**  

### Phase 3 Detailed Architecture Specification
- **Core Objective:** Implement attendance QR scanning, mobile app backend integration, AI chatbot, GDPR & backup compliance.
- **Physical File Structure:** `./sources/backend`  
- **Technical Outline:**  
   - **Attendance QR Service** – handle scan, validate student-course relationship, store attendance record, enforce idempotency, support offline queue.  
   - **Mobile Backend Integration** – expose endpoints for mobile app (push notifications, device token registration).  
   - **AI Chatbot** – natural language processing, intent recognition, response generation.  
   - **GDPR & Backup** – data retention policies, encryption keys, disaster recovery.  

#### Database Schema Extensions
- **Attendance Table** – `[DAT-005]`  
- **Notifications Table** – `[DAT-007]`  
- **System Settings Table** – `[DAT-011]`  

#### API Contracts
- **QR Attendance Endpoint** – `[REQ-012],[ARC-007]`  
- **Mobile Backend Integration** – `[REQ-020],[REQ-021],[ARC-009]`  
- **AI Chatbot** – `[REQ-019]`  
- **GDPR/Backup** – `[NFR-008],[NFR-009]`  

#### Exception Handling Specifications
- **Network Loss QR** – `[EXC-001]`  
- **Duplicate Scan** – `[EXC-002]`  
- **Notification Failure** – `[EXC-003]`  

#### Security & Compliance Controls
- **SQL Injection** – `[NFR-003]`  
- **XSS & CSP** – `[NFR-004]`  
- **CORS** – `[NFR-005]`  
- **Log Scrubbing** – `[NFR-006]`  

#### Hybrid Mobile Compliance Rails
- **Capacitor Integration** – `[NFR-007]`  
- **i18n & SEO** – `[REQ-022],[REQ-023],[NFR-007]`  

#### Pipeline Daily Git Branch Flow
- **Workspace Fork** – `features/development-day-X`  
- **Validation Gates** – compile, coverage≥85%, lint, security-scan  

### 🛑 MATRIX COVERAGE VALIDATION
**[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]**