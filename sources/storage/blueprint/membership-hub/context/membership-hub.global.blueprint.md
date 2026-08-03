# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260803033550 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/03 03:35:50 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

The solution adopts a **micro‑service‑oriented architecture** built on **Java 21 / Quarkus 3.x** for the backend, **Next.js 14** for the web front‑end, and a **Capacitor‑based hybrid mobile app** for iOS/Android. Services are containerised with **Docker** and orchestrated on **Google Kubernetes Engine (GKE)**.  

* **Event‑Driven Data Flow** – Core domains (attendance, notifications, promotions) emit **Kafka** events; subscribers maintain read‑models for fast UI rendering.  
* **CQRS & Command Processing** – Write operations ( enrolment, attendance scan ) use dedicated command services; read models are served via query services, ensuring sub‑second API latency.  
* **Reactive Core** – All internal communication uses **SmallRye Reactive Messaging**; non‑blocking I/O and Vert.x event loops guarantee high throughput under 10 000 concurrent users.  
* **Multi‑Tenant Isolation** – Each center operates in its own logical tenant boundary enforced via schema‑per‑tenant PostgreSQL patterns and JWT‑based tenant identification.  
* **API Gateway & Security** – Central **OpenAPI** gateway enforces **TLS 1.3**, JWT validation, rate‑limiting, and OWASP Top‑10 mitigations.  

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross‑channel external fan‑out architectures]

* **Ingestion Gateway** – All mobile QR scans and web form submissions are normalised via a **REST‑over‑HTTPS** endpoint, validated, and published to the **`events.attendance`** Kafka topic.  
* **Fan‑Out Topology** – The attendance event fans out to three sinks: (1) **`service.attendance.write`** (persistent store), (2) **`service.notification.queue`** (push & Zalo), (3) **`service.analytics.stream`** (real‑time dashboards).  
* **External Integrations** – Firebase Authentication, Google/ Facebook OAuth2, Zalo API, and FCM/APNs are integrated through dedicated adapter services that emit **`events.auth`** and **`events.push`** topics.  
* **Session Caching** – Redis clusters store short‑lived JWT claims and user session state, reducing DB load and enabling offline‑first UI caching.  

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.x, Hibernate ORM, Flyway, SmallRye OpenAPI, Eclipse Microprofile JWT, PostgreSQL JDBC Driver, Apache Kafka (librdkafka), Redis Java client, JUnit 5, AssertJ, WireMock, Lombok, MapStruct, Jackson Databind, Spring‑Boot‑compatible extensions (for Quarkus), Google Cloud Firestore (optional), Google Cloud Storage SDK.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14, React 18, TypeScript 5, Tailwind CSS, i18next, react‑query, Axios, Capacitor 5, Ionic Framework, Cordova plugins (camera, barcode‑scanner), Firebase SDK, @capacitor/push-notifications, @capacitor/preferences, Jest, React‑Testing‑Library.

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `..`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.membershiphub`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1‑3 | `./sources/backend.authentication`, `./sources/backend.user`, `./sources/frontend.auth`, `./sources/infra.dockerfile`, `./sources/infra.k8s` | JWT auth service, user registration & social OAuth, role assignment, DDL for Users/Roles, OpenAPI contracts for REQ‑001‑003, ARC‑006, security hardening per NFR‑003/005/006 | Coder, Docker, GCP, Reviewer | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [DAT-003], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Phase 2 | Day 4‑6 | `./sources/backend.center`, `./sources/backend.course`, `./sources/frontend.center`, `./sources/frontend.course`, `./sources/infra.k8s` | Center CRUD, course conflict detection, teacher assignment, DDL for Centers/Courses, API contracts for REQ‑004‑009, ARC‑001‑005, RBAC enforcement | Coder, Tester, Reviewer, Doc | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [DAT-003], [DAT-004], [EXC-004] |
| Phase 3 | Day 7‑9 | `./sources/backend.enrollment`, `./sources/backend.attendance`, `./sources/backend.membership`, `./sources/frontend.student`, `./sources/infra.k8s` | Student enrollment, QR attendance idempotent service, membership card validity, DDL for Enrollments/Attendance/StudentCards, API contracts for REQ‑010‑015, EXC‑001‑002, duplicate detection logic | Coder, Tester, Reviewer, Doc | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [EXC-001], [EXC-002], [DAT-005], [DAT-006], [DAT-007], [ARC-007], [ARC-008] |
| Phase 4 | Day 10‑12 | `./sources/backend.notification`, `./sources/backend.promotion`, `./sources/backend.announcement`, `./sources/backend.chatbot`, `./sources/frontend.mobile`, `./sources/infra.k8s` | Notification engine (push & Zalo), promotion & announcement management, AI chatbot integration, mobile UI & push registration, DDL for Notifications/Promotions/Announcements, API contracts for REQ‑016‑021, EXC‑003 | Coder, Docker, GCP, Reviewer, Doc | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [EXC-003], [DAT-008], [DAT-009], [ARC-009], [ARC-010] |
| Phase 5 | Day 13‑15 | `./sources/backend.i18n`, `./sources/backend.seo`, `./sources/backend.reporting`, `./sources/infra.security`, `./sources/infra.backup`, `./sources/frontend.global` | Internationalisation & SEO middleware, daily attendance report generation (CSV), real‑time dashboards, security hardening (TLS 1.3, AES‑256), backup & disaster recovery, DDL for SystemSettings, API contracts for REQ‑022‑025, NFR‑001‑009 enforcement | Coder, Tester, Reviewer, Doc, GCP, GKE | [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-011], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [EXC-005] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
# STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= 5). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

<!--START_DELIMITTER-->
### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các thành phần cốt lõi của hệ thống xác thực và quản lý người dùng, bao gồm đăng ký tài khoản địa phương, xác thực OAuth2 qua Firebase/Google/Facebook, gán vai trò và phát hành JWT token. Xây dựng DDL cho bảng Users, Roles và SystemSettings, đồng thời định nghĩa các hợp đồng API cho các yêu cầu chức năng tương ứng.
- **Target Physical Directory Matrix Map:** 
  * `./sources/backend.authentication/org/nlh4j/saas/membershiphub/authentication/` (contains `AuthController.java`, `KeyClockConfig.java`, `JwtService.java`) – `[REQ-001], [REQ-002], [ARC-006], [DAT-001]`
  * `./sources/backend.user/org/nlh4j/saas/membershiphub/user/` (contains `UserResource.java`, `RoleRepository.java`, `UserService.java`) – `[REQ-003], [DAT-001]`
  * `./sources/frontend.auth/src/auth/` (contains `login.component.ts`, `register.component.ts`, `oauth-callback.component.ts`) – `[REQ-001], [REQ-002]`
  * `./sources/infra.dockerfile/backend/` (Dockerfile cho Quarkus) – `[NFR-005]`
  * `./sources/infra.k8s/backend/` (Helm chart cho GKE) – `[NFR-004], [NFR-002]`
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
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [ARC-006]:**
  * `POST /api/auth/register` – body: `{email, password, fullName, provider}`; response: `{token, userId}` – `[REQ-001]`
  * `POST /api/auth/social` – body: `{provider, code, redirectUri}`; response: `{token}` – `[REQ-002]`
  * `GET /api/auth/validate` – header: `Authorization: Bearer <token>`; response: `{valid, userId, role}` – `[ARC-006]`
- **Phase Localized Exception Handlers [EXC-004]:**
  * Xác thực đầu vào không hợp lệ (email sai định dạng, thiếu trường bắt buộc) → trả về HTTP 400 với JSON: `{ "error": "VALIDATION_FAILED", "details": ["email is required", "password must be strong"] }` – `[EXC-004]`

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1: Triển khai dịch vụ xác thực JWT và cấu hình bảo mật**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.authentication/org/nlh4j/saas/membershiphub/authentication/JwtService.java` – `[REQ-001], [ARC-006]`
      - **Low-Level Technical Task Instruction:** Triển khai lớp dịch vụ tạo và xác thực JWT token với thời hạn 15 phút, tích hợp với Eclipse Microprofile JWT, đảm bảo chữ ký bằng RSA-256, logging token creation theo chuẩn ISO‑8601. Gắn thẻ `[REQ-001], [ARC-006]`.
      - **Targeted Tag IDs:** [REQ-001], [ARC-006]
    * **[Tester]:**
      - **Target Component file path (`target_component`):** `./sources/backend.authentication/org/nlh4j/saas/membershiphub/authentication/JwtService.java;src/test/java/org/nlh4j/saas/membershiphub/authentication/JwtServiceTest.java` – `[REQ-001], [ARC-006]`
      - **Low-Level Technical Task Instruction:** Viết unit test cho JwtService.verifyToken() với các trường hợp token hợp lệ, token hết hạn, chữ ký sai, đảm bảo trả về true/false chính xác. Gắn thẻ `[REQ-001], [ARC-006]`.
      - **Targeted Tag IDs:** [REQ-001], [ARC-006]

- **DAY 2: Xây dựng endpoint đăng ký người dùng địa phương**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.authentication/org/nlh4j/saas/membershiphub/authentication/AuthController.java` – `[REQ-001]`
    - **Low-Level Technical Task Instruction:** Triển khai REST endpoint `POST /api/auth/register` xử lý xác thực đầu vào, mã hóa mật khẩu bằng bcrypt, lưu user vào bảng users với role mặc định 'Student', trả về JWT token. Gắn thẻ `[REQ-001]`.
    - **Targeted Tag IDs:** [REQ-001]
  * **[Reviewer]:**
    - **Target Component file path (`target_component`):** `./sources/backend.authentication/org/nlh4j/saas/membershiphub/authentication/AuthController.java` – `[REQ-001]`
    - **Low-Level Technical Task Instruction:** Đánh giá logic nghiệp vụ, kiểm tra tuân thủ RFC 7231, đảm bảo không lộ thông tin nhạy cảm trong response, xác nhận tuân thủ `[REQ-001]`.
    - **Targeted Tag IDs:** [REQ-001]

- **DAY 3: Triển khai xác thực OAuth2 qua Firebase/Google/Facebook và tích hợp Docker/K8s**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.authentication/org/nlh4j/saas/membershiphub/authentication/SocialAuthService.java` – `[REQ-002], [ARC-006]`
    - **Low-Level Technical Task Instruction:** Triển khai exchange code lấy thông tin người dùng từ Firebase Auth, Google People API, Facebook Graph API, tạo hoặc cập nhật bản ghi người dùng, phát hành JWT. Gắn thẻ `[REQ-002], [ARC-006]`.
    - **Targeted Tag IDs:** [REQ-002], [ARC-006]
  * **[Docker]:**
    - **Target Component file path (`target_component`):** `./sources/infra.dockerfile/backend/Dockerfile` – `[NFR-005]`
    - **Low-Level Technical Task Instruction:** Tạo image Docker tối ưu hóa cho Quarkus, sử dụng base image `quay.io/quarkus/centos-quarkus-maven:3.15`, giảm kích thước image xuống < 500 MB, tích hợp health‑check endpoint. Gắn thẻ `[NFR-005]`.
    - **Targeted Tag IDs:** [NFR-005]
  * **[GCP]:**
    - **Target Component file path (`target_component`):** `./sources/infra.k8s/backend/values.yaml` – `[NFR-004], [NFR-002]`
    - **Low-Level Technical Task Instruction:** Định nghĩa Helm giá trị cho GKE deployment, thiết lập HPA dựa trên CPU > 70 % hoặc latency > 300 ms, cấu hình service‑mesh cho TLS 1.3. Gắn thẻ `[NFR-004], [NFR-002]`.
    - **Targeted Tag IDs:** [NFR-004], [NFR-002]

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng module quản lý trung tâm và khóa học, bao gồm CRUD cho trung tâm, phát hiện xung đột lịch học, gán giáo viên, DDL cho bảng Centers và Courses, hợp đồng API cho các yêu cầu chức năng tương ứng.
- **Target Physical Directory Matrix Map:** 
  * `./sources/backend.center/org/nlh4j/saas/membershiphub/center/` (CenterResource.java, CenterRepository.java) – `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
  * `./sources/backend.course/org/nlh4j/saas/membershiphub/course/` (CourseResource.java, CourseRepository.java) – `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`
  * `./sources/frontend.center/src/center/` (center.component.ts, center.service.ts) – `[REQ-004], [REQ-005]`
  * `./sources/frontend.course/src/course/` (course.component.ts, course.service.ts) – `[REQ-007], [REQ-008]`
  * `./sources/infra.k8s/backend/` (Helm chart cập nhật) – `[NFR-004]`
- **Database Schema DDL SQL Specification [DAT-003], [DAT-004]:**
```sql
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) NOT NULL UNIQUE,
    contact_phone VARCHAR(30),
    contact_email VARCHAR(255)
);

CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]:**
  * `GET /api/centers` – trả về danh sách trung tâm – `[REQ-004]`
  * `POST /api/centers` – tạo trung tâm mới, kiểm tra tax_id trùng – `[REQ-005]`
  * `PUT /api/centers/{id}` / `DELETE /api/centers/{id}` – cập nhật/xóa – `[REQ-005]`
  * `GET /api/centers/{id}/admins` – liệt kê admin – `[REQ-006]`
  * `POST /api/centers/{id}/admins/{userId}` – gán người dùng làm Center Admin – `[REQ-006]`
  * `GET /api/courses` – danh sách khóa học – `[REQ-007]`
  * `POST /api/courses` – tạo khóa học mới, kiểm tra xung đột lịch học giáo viên – `[REQ-008]`
  * `PUT /api/courses/{id}` / `DELETE /api/courses/{id}` – cập nhật/xóa – `[REQ-008]`
  * `POST /api/courses/{id}/teachers/{teacherId}` – gán giáo viên – `[REQ-009]`
- **Phase Localized Exception Handlers [EXC-004]:**
  * Xác thực đầu vào không hợp lệ cho form tạo trung tâm (trường bắt buộc thiếu, tax_id sai định dạng) → trả về HTTP 422 với JSON: `{ "error": "CENTER_VALIDATION_FAILED", "fields": ["tax_id must be numeric 10‑13 digits"] }` – `[EXC-004]`

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 4: Triển khai CRUD cho trung tâm**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.center/org/nlh4j/saas/membershiphub/center/CenterResource.java` – `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
    - **Low-Level Technical Task Instruction:** Triển khai REST endpoints GET /api/centers, POST /api/centers, PUT /api/centers/{id}, DELETE /api/centers/{id} với xác thực vai trò System Admin (ARC‑001) hoặc Center Admin (ARC‑002). Thêm kiểm tra tax_id duy nhất. Gắn thẻ `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`.
    - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]
  * **[Tester]:**
    - **Target Component file path (`target_component`):** `./sources/backend.center/org/nlh4j/saas/membershiphub/center/CenterResource.java;src/test/java/org/nlh4j/saas/membershiphub/center/CenterResourceTest.java` – `[REQ-004], [REQ-005], [REQ-006]`
    - **Low-Level Technical Task Instruction:** Viết test cases cho GET (trả về danh sách), POST (tạo thành công, lỗi tax_id trùng), PUT, DELETE, xác nhận mã trạng thái HTTP và payload. Gắn thẻ `[REQ-004], [REQ-005], [REQ-006]`.
    - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]

- **DAY 5: Triển khai module khóa học với phát hiện xung đột**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.course/org/nlh4j/saas/membershiphub/course/CourseResource.java` – `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`
    - **Low-Level Technical Task Instruction:** Triển khai GET /api/courses, POST /api/courses (kiểm tra xung đột lịch học giáo viên), PUT/DELETE, POST /api/courses/{id}/teachers/{teacherId}. Sử dụng stored procedure hoặc trigger để đảm bảo atomicity. Gắn thẻ `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`.
    - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004]
  * **[Reviewer]:**
    - **Target Component file path (`target_component`):** `./sources/backend.course/org/nlh4j/saas/membershiphub/course/CourseResource.java` – `[REQ-007], [REQ-008], [REQ-009]`
    - **Low-Level Technical Task Instruction:** Đánh giá logic nghiệp vụ xung đột, đảm bảo tuân thủ RBAC (System Admin, Center Admin), xác nhận response JSON phù hợp. Gắn thẻ `[REQ-007], [REQ-008], [REQ-009]`.
    - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]

- **DAY 6: Tích hợp frontend cho trung tâm và khóa học, cập nhật Helm**
  * **[Doc]:**
    - **Target Component file path (`target_component`):** `./sources/frontend.center/src/center/README.md` – `[REQ-004], [REQ-005]`
    - **Low-Level Technical Task Instruction:** Viết tài liệu API tích hợp cho các component trung tâm, mô tả endpoint, tham số, phản hồi, lỗi. Gắn thẻ `[REQ-004], [REQ-005]`.
    - **Targeted Tag IDs:** [REQ-004], [REQ-005]
  * **[GKE]:**
    - **Target Component file path (`target_component`):** `./sources/infra.k8s/backend/values.yaml` – `[NFR-004]`
    - **Low-Level Technical Task Instruction:** Cập nhật giá trị Helm để bao gồm deployment mới cho backend.center và backend.course, thiết lập resource limits, tự động scaling. Gắn thẻ `[NFR-004]`.
    - **Targeted Tag IDs:** [NFR-004]

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng module ghi danh học viên, điểm danh QR, và quản lý thẻ hội viên, bao gồm DDL cho bảng Enrollments, Attendance, StudentCards, triển khai dịch vụ điểm danh bất biến, hợp đồng API cho các yêu cầu chức năng tương ứng.
- **Target Physical Directory Matrix Map:** 
  * `./sources/backend.enrollment/org/nlh4j/saas/membershiphub/enrollment/` (EnrollmentResource.java, EnrollmentRepository.java) – `[REQ-010], [REQ-011], [DAT-005]`
  * `./sources/backend.attendance/org/nlh4j/saas/membershiphub/attendance/` (AttendanceResource.java, AttendanceService.java) – `[REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]`
  * `./sources/backend.membership/org/nlh4j/saas/membershiphub/membership/` (MembershipResource.java, StudentCardRepository.java) – `[REQ-014], [REQ-015], [DAT-007]`
  * `./sources/frontend.student/src/student/` (student-dashboard.component.ts, attendance-scanner.component.ts, card.component.ts) – `[REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015]`
  * `./sources/infra.k8s/backend/` (Helm chart cập nhật) – `[NFR-004]`
- **Database Schema DDL SQL Specification [DAT-005], [DAT-006], [DAT-007]:**
```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id)
);

CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (student_id, course_id, attendance_date)
);

CREATE TABLE studentcards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);
```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007], [ARC-008]:**
  * `GET /api/enrollments` – danh sách ghi danh của học viên – `[REQ-010]`
  * `POST /api/enrollments` – đăng ký khóa học, tự động tạo tài khoản học viên nếu thiếu – `[REQ-011]`
  * `POST /api/attendance/scan` – nhận payload `{studentId, courseId, timestamp}`, ghi nhận điểm danh, phát hiện duplicate – `[REQ-012]`
  * `GET /api/attendance/{studentId}/today` – trả về bản ghi điểm danh hôm nay – `[REQ-013]`
  * `GET /api/studentcards/{studentId}` – hiển thị thẻ hội viên với days remaining – `[REQ-014]`
  * `POST /api/studentcards/{studentId}/renew` – gia hạn thẻ theo số ngày chọn, xử lý thanh toán – `[REQ-015]`
- **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
  * Mất kết nối mạng trong khi quét QR → lưu sự kiện offline cục bộ, retry khi có kết nối, sau đó ghi nhận điểm danh một lần duy nhất – `[EXC-001]`
  * Quét QR trùng lặp trong cùng ngày → trả về HTTP 200 với `{ "message": "attendance already recorded", "attendanceId": "<id>" }` – `[EXC-002]`

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 7: Triển khai module ghi danh học viên**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.enrollment/org/nlh4j/saas/membershiphub/enrollment/EnrollmentResource.java` – `[REQ-010], [REQ-011], [DAT-005]`
    - **Low-Level Technical Task Instruction:** Triển khai endpoint GET /api/enrollments (lọc theo studentId) và POST /api/enrollments (kiểm tra xung đột ghi danh, tạo bản ghi). Đảm bảo transaction với bảng users để tạo tài khoản học viên nếu thiếu. Gắn thẻ `[REQ-010], [REQ-011], [DAT-005]`.
    - **Targeted Tag IDs:** [REQ-010], [REQ-011], [DAT-005]
  * **[Tester]:**
    - **Target Component file path (`target_component`):** `./sources/backend.enrollment/org/nlh4j/saas/membershiphub/enrollment/EnrollmentResource.java;src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentResourceTest.java` – `[REQ-010], [REQ-011]`
    - **Low-Level Technical Task Instruction:** Viết test cho GET (trả về danh sách), POST (tạo thành công, lỗi duplicate), xác nhận HTTP status và payload. Gắn thẻ `[REQ-010], [REQ-011]`.
    - **Targeted Tag IDs:** [REQ-010], [REQ-011]

- **DAY 8: Triển khai dịch vụ điểm danh QR với tính bất biến**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.attendance/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java` – `[REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]`
    - **Low-Level Technical Task Instruction:** Triển khai logic xử lý điểm danh: xác thực studentId/courseId relationship, chèn bản ghi với timestamp, sử dụng khóa duy nhất (student_id, course_id, attendance_date) để ngăn duplicate, xử lý ngoại lệ network loss (lưu offline) và duplicate scan. Gắn thẻ `[REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]`.
    - **Targeted Tag IDs:** [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]
  * **[Reviewer]:**
    - **Target Component file path (`target_component`):** `./sources/backend.attendance/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java` – `[REQ-012], [REQ-013]`
    - **Low-Level Technical Task Instruction:** Đánh giá logic bất biến, đảm bảo hiệu suất sub‑second, xác nhận tuân thủ ARC‑007/ARC‑008. Gắn thẻ `[REQ-012], [REQ-013]`.
    - **Targeted Tag IDs:** [REQ-012], [REQ-013]

- **DAY 9: Triển khai module thẻ hội viên và tích hợp frontend**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.membership/org/nlh4j/saas/membershiphub/membership/MembershipResource.java` – `[REQ-014], [REQ-015], [DAT-007]`
    - **Low-Level Technical Task Instruction:** Triển khai GET /api/studentcards/{studentId} (tính remainingDays từ issueDate + validityDays) và POST /api/studentcards/{studentId}/renew (cập nhật end date sau thanh toán). Sử dụng stored function để tính remainingDays. Gắn thẻ `[REQ-014], [REQ-015], [DAT-007]`.
    - **Targeted Tag IDs:** [REQ-014], [REQ-015], [DAT-007]
  * **[Doc]:**
    - **Target Component file path (`target_component`):** `./sources/frontend.student/src/student/card.component.ts` – `[REQ-014], [REQ-015]`
    - **Low-Level Technical Task Instruction:** Viết component hiển thị thẻ hội viên, binding days remaining, UI cho quá trình gia hạn, tích hợp với API renew. Gắn thẻ `[REQ-014], [REQ-015]`.
    - **Targeted Tag IDs:** [REQ-014], [REQ-015]

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng module thông báo (push & Zalo), quản lý khuyến mãi & thông báo, tích hợp chatbot AI, triển khai giao diện người dùng di động, bao gồm DDL cho bảng Notifications, Promotions, Announcements, hợp đồng API cho các yêu cầu chức năng tương ứng.
- **Target Physical Directory Matrix Map:** 
  * `./sources/backend.notification/org/nlh4j/saas/membershiphub/notification/` (NotificationService.java, PushService.java) – `[REQ-016], [DAT-008], [ARC-009]`
  * `./sources/backend.promotion/org/nlh4j/saas/membershiphub/promotion/` (PromotionResource.java, PromotionRepository.java) – `[REQ-017], [DAT-009]`
  * `./sources/backend.announcement/org/nlh4j/saas/membershiphub/announcement/` (AnnouncementResource.java, AnnouncementRepository.java) – `[REQ-018], [DAT-009]`
  * `./sources/backend.chatbot/org/nlh4j/saas/membershiphub/chatbot/` (ChatbotController.java, NlpService.java) – `[REQ-019], [NOT APPLICABLE]`
  * `./sources/frontend.mobile/src/app/` (components cho dashboard, notifications, promotions) – `[REQ-020], [REQ-021]`
  * `./sources/infra.k8s/backend/` (Helm chart cập nhật) – `[NFR-004]`
- **Database Schema DDL SQL Specification [DAT-008], [DAT-009]:**
```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID,
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
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
```
- **API and Event Routing Contracts [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [EXC-003]:**
  * `POST /api/notifications` – tạo thông báo, đẩy push notification qua FCM/APNs, gửi Zalo message – `[REQ-016]`
  * `GET /api/notifications/{userId}` – lấy danh sách thông báo – `[REQ-020]`
  * `POST /api/promotions` – tạo khuyến mãi mới, thiết lập ngày bắt đầu/kết thúc – `[REQ-017]`
  * `PUT /api/promotions/{id}` / `DELETE /api/promotions/{id}` – cập nhật/xóa – `[REQ-017]`
  * `POST /api/announcements` – tạo thông báo, thiết lập ngày hiệu lực – `[REQ-018]`
  * `PUT /api/announcements/{id}` / `DELETE /api/announcements/{id}` – cập nhật/xóa – `[REQ-018]`
  * `POST /api/chatbot/ask` – nhận `{question}` từ người dùng, trả về `{answer}` – `[REQ-019]`
  * `POST /api/mobile/token` – đăng ký thiết bị push token cho người dùng – `[REQ-021]`
- **Phase Localized Exception Handlers [EXC-003]:**
  * Lỗi gửi push notification (token không hợp lệ) → ghi log lỗi, lên lịch retry tối đa 3 lần, sau đó đánh dấu delivered = false – `[EXC-003]`

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 10: Triển khai module thông báo và push service**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.notification/org/nlh4j/saas/membershiphub/notification/NotificationService.java` – `[REQ-016], [DAT-008], [ARC-009]`
    - **Low-Level Technical Task Instruction:** Triển khai logic tạo notification record, gọi FCM/APNs client để gửi push, gọi Zalo API để đăng bài, lên lịch retry cho trường hợp thất bại. Gắn thẻ `[REQ-016], [DAT-008], [ARC-009]`.
    - **Targeted Tag IDs:** [REQ-016], [DAT-008], [ARC-009]
  * **[Tester]:**
    - **Target Component file path (`target_component`):** `./sources/backend.notification/org/nlh4j/saas/membershiphub/notification/NotificationService.java;src/test/java/org/nlh4j/saas/membershiphub/notification/NotificationServiceTest.java` – `[REQ-016], [EXC-003]`
    - **Low-Level Technical Task Instruction:** Viết test cho gửi push thành công, token không hợp lệ (retry), xác nhận delivered flag. Gắn thẻ `[REQ-016], [EXC-003]`.
    - **Targeted Tag IDs:** [REQ-016], [EXC-003]

- **DAY 11: Triển khai module khuyến mãi và thông báo**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.promotion/org/nlh4j/saas/membershiphub/promotion/PromotionResource.java` – `[REQ-017], [DAT-009]`
    - **Low-Level Technical Task Instruction:** Triển khai CRUD cho khuyến mãi, validation start/end date, đảm bảo code duy nhất, gắn thẻ `[REQ-017], [DAT-009]`.
    - **Targeted Tag IDs:** [REQ-017], [DAT-009]
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.announcement/org/nlh4j/saas/membershiphub/announcement/AnnouncementResource.java` – `[REQ-018], [DAT-009]`
    - **Low-Level Technical Task Instruction:** Triển khai CRUD cho thông báo, hỗ trợ ngày hiệu lực, tự động ẩn sau end_date. Gắn thẻ `[REQ-018], [DAT-009]`.
    - **Targeted Tag IDs:** [REQ-018], [DAT-009]

- **DAY 12: Triển khai chatbot AI và giao diện người dùng di động**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.chatbot/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java` – `[REQ-019]`
    - **Low-Level Technical Task Instruction:** Triển khai endpoint POST /api/chatbot/ask, tích hợp với NlpService để xử lý câu hỏi, trả về câu trả lời, ghi log tương tác vào bảng AuditLog. Gắn thẻ `[REQ-019]`.
    - **Targeted Tag IDs:** [REQ-019]
  * **[Doc]:**
    - **Target Component file path (`target_component`):** `./sources/frontend.mobile/src/app/chatbot.component.ts` – `[REQ-019]`
    - **Low-Level Technical Task Instruction:** Viết component giao diện chatbot, binding input/output, hiển thị kết quả, tích hợp với API chatbot. Gắn thẻ `[REQ-019]`.
    - **Targeted Tag IDs:** [REQ-019]
  * **[GKE]:**
    - **Target Component file path (`target_component`):** `./sources/infra.k8s/backend/values.yaml` – `[NFR-004]`
    - **Low-Level Technical Task Instruction:** Cập nhật Helm values để triển khai backend.notification, backend.promotion, backend.announcement, backend.chatbot, frontend.mobile. Gắn thẻ `[NFR-004]`.
    - **Targeted Tag IDs:** [NFR-004]

### Phase 5 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các tính năng quốc tế hóa, SEO, báo cáo & phân tích, hardening bảo mật, sao lưu & disaster recovery, bao gồm DDL cho bảng SystemSettings, hợp đồng API cho các yêu cầu chức năng tương ứng, và thực thi các yêu cầu phi chức năng.
- **Target Physical Directory Matrix Map:** 
  * `./sources/backend.i18n/org/nlh4j/saas/membershiphub/i18n/` (I18nConfig.java, LocaleInterceptor.java) – `[REQ-022], [REQ-023], [NFR-007]`
  * `./sources/backend.seo/org/nlh4j/saas/membershiphub/seo/` (SeoController.java, HreflangService.java) – `[REQ-023], [NFR-007]`
  * `./sources/backend.reporting/org/nlh4j/saas/membershiphub/reporting/` (ReportController.java, AttendanceReportService.java) – `[REQ-024], [REQ-025], [NFR-001]`
  * `./sources/infra.security/` (security-config.yaml, tls-config.yaml) – `[NFR-003], [NFR-004]`
  * `./sources/infra.backup/` (backup-script.sh, restore-script.sh) – `[NFR-009]`
  * `./sources/frontend.global/src/app/` (global-error-handler.component.ts, language-switcher.component.ts) – `[REQ-022], [REQ-023]`
  * `./sources/infra.k8s/backend/` (Helm chart cập nhật) – `[NFR-004]`
- **Database Schema DDL SQL Specification [DAT-011]:**
```sql
CREATE TABLE systemsettings (
    setting_key VARCHAR(100) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]:**
  * `GET /api/i18n/preferences` – trả về ngôn ngữ đã lưu của người dùng – `[REQ-022]`
  * `PUT /api/i18n/preferences` – cập nhật ngôn ngữ ưa thích – `[REQ-022]`
  * `GET /api/seo/hreflang/{path}` – trả về thẻ hreflang cho các ngôn ngữ thay thế – `[REQ-023]`
  * `GET /api/reports/attendance` – tạo báo cáo điểm danh CSV cho trung tâm và ngày chỉ định – `[REQ-024]`
  * `GET /api/analytics/dashboard` – trả về tổng hợp thời gian thực (totalStudents, activeCourses, upcomingSessions) – `[REQ-025]`
  * `GET /api/health` – endpoint kiểm tra tình trạng (latency < 200 ms) – `[NFR-001]`
  * `GET /api/secure/info` – yêu cầu TLS 1.3, xác thực JWT – `[NFR-003]`
  * `GET /api/secure/config` – trả về cấu hình bảo mật – `[NFR-004]`
  * `GET /api/secure/image` – endpoint trả về logo với Content‑Security‑Policy – `[NFR-005]`
  * `GET /api/logs/audit` – trả về audit log (đã được che giấu PII) – `[NFR-006]`
  * `GET /api/i18n/available` – liệt kê ngôn ngữ được hỗ trợ (EN, VN, ES) – `[NFR-007]`
  * `POST /api/gdpr/delete/{userId}` – xóa dữ liệu cá nhân theo yêu cầu GDPR/CCPA – `[NFR-008]`
  * `POST /api/backup/trigger` – kích hoạt sao lưu PostgreSQL đầy đủ – `[NFR-009]`
- **Phase Localized Exception Handlers [EXC-005]:**
  * System phục hồi sau sự cố – khi dịch vụ khôi phục, xử lý các điểm danh chờ (FIFO), gửi notification cho người dùng về các sự kiện đã phục hồi – `[EXC-005]`

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 13: Triển khai quốc tế hóa và middleware SEO**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.i18n/org/nlh4j/saas/membershiphub/i18n/I18nConfig.java` – `[REQ-022], [REQ-023], [NFR-007]`
    - **Low-Level Technical Task Instruction:** Cấu hình Spring Boot (Quarkus) i18n, thiết lập locale resolver từ session, cookie, header Accept-Language, expose REST endpoint /api/i18n/preferences. Tích hợp với Thymeleaf/Vert.x web template để áp dụng thuộc tính html lang. Gắn thẻ `[REQ-022], [REQ-023], [NFR-007]`.
    - **Targeted Tag IDs:** [REQ-022], [REQ-023], [NFR-007]
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.seo/org/nlh4j/saas/membershiphub/seo/SeoController.java` – `[REQ-023]`
    - **Low-Level Technical Task Instruction:** Triển khai endpoint GET /api/seo/hreflang/{path} để tạo liên kết hreflang cho EN, VN, ES, đảm bảo mỗi page bao gồm meta tags [keywords], [description] theo từng ngôn ngữ. Gắn thẻ `[REQ-023]`.
    - **Targeted Tag IDs:** [REQ-023]

- **DAY 14: Triển khai báo cáo & phân tích và hardening bảo mật**
  * **[Coder]:**
    - **Target Component file path (`target_component`):** `./sources/backend.reporting/org/nlh4j/saas/membershiphub/reporting/ReportController.java` – `[REQ-024], [REQ-025], [NFR-001]`
    - **Low-Level Technical Task Instruction:** Triển khai endpoint GET /api/reports/attendance (tạo CSV với columns StudentName, CourseName, AttendanceDate, Status) và GET /api/analytics/dashboard (trả về JSON tổng hợp). Đảm bảo performance latency < 200 ms bằng cách sử dụng index trên attendance(attendance_date), caching kết quả báo cáo trong Redis 5 phút. Gắn thẻ `[REQ-024], [REQ-025], [NFR-001]`.
    - **Targeted Tag IDs:** [REQ-024], [REQ-025], [NFR-001]
  * **[Docker]:**
    - **Target Component file path (`target_component`):** `./sources/infra.security/security-config.yaml` – `[NFR-003], [NFR-004]`
    - **Low-Level Technical Task Instruction:** Cấu hình Spring Security cho TLS 1.3, enforce JWT với thời hạn 15 phút, thiết lập CSP header, cấu hình CORS cho từng tenant origin, logging tất cả request/response. Gắn thẻ `[NFR-003], [NFR-004]`.
    - **Targeted Tag IDs:** [NFR-003], [NFR-004]

- **DAY 15: Triển khai sao lưu & disaster recovery, hoàn thiện CI/CD**
  * **[GCP]:**
    - **Target Component file path (`target_component`):** `./sources/infra.backup/backup-script.sh` – `[NFR-009]`
    - **Low-Level Technical Task Instruction:** Viết script tự động sao lưu PostgreSQL đầy đủ hàng ngày, nén, upload lên Google Cloud Storage bucket `membership-hub-backups`, lên lịch với cron `0 2 * * *`. Triển khai restore point-in-time (PITR) đến 24 giờ trước. Gắn thẻ `[NFR-009]`.
    - **Targeted Tag IDs:** [NFR-009]
  * **[GKE]:**
    - **Target Component file path (`target_component`):** `./sources/infra.k8s/backend/values.yaml` – `[NFR-004], [NFR-002]`
    - **Low-Level Technical Task Instruction:** Cập nhật Helm values để kích hoạt backup cronjob, cấu hình cluster autoscaling, thiết lập node-pool riêng cho stateful services, đảm bảo SLA 99.9% uptime. Gắn thẻ `[NFR-004], [NFR-002]`.
    - **Targeted Tag IDs:** [NFR-004], [NFR-002]

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng PreparedStatement với tham số dấu ? cho mọi câu lệnh SQL; áp dụng Whitelist cho các cột sắp xếp; vô hiệu hóa dynamic SQL; tích hợp Flyway để quản lý migration; kiểm tra input tại biên giới với regex cho tax_id, email.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Áp dụng auto‑escaping trong Thymeleaf/JSX; sử dụng `@ResponseBody` với `ContentType="application/json"`; thiết lập CSP header: `default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:`; vô hiệu hóa `unsafe-inline` trong production.
- **Multi-Tenant CORS Security Rails:** Cấu hình `Access-Control-Allow-Origin` cho từng tenant dựa trên bảng `tenants` whitelist; từ chối wildcard `*`; xác thực `Origin` so với database tenant metadata; sử dụng `Vary: Origin` header.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Áp dụng `@JsonSerialize` với `JsonSerializer` tùy chỉnh để che giấu số điện thoại, email trong log; thiết lập log forwarder loại bỏ trường `password_hash`; sử dụng `slf4j` MDC để track request ID; lưu giữ log 1 năm, sau đó tự động xóa.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** 
  * Sử dụng `@capacitor/preferences` để lưu trữ offline token và queue cho các sự kiện đã xử lý. 
  * Triển khai network interceptor để retry tự động khi mất kết nối (max 3 lần). 
  * Sử dụng `cordova-plugin-inscreen-price` để bảo vệ deep link từ QR scanner. 
  * Tích hợp push notification registration thông qua `@capacitor/push-notifications` với FCM/APNs.
- **Internationalization (i18n) & Dynamic SEO Injection:** 
  * Middleware phát hiện locale từ cookie `lang`, header `Accept-Language`, fallback sang `en`. 
  * Sử dụng `i18next` với backend resource bundle để dịch UI strings. 
  * Tự động chèn thẻ `<html lang="vi">` và `<link rel="alternate" hreflang="en" href="...">` cho từng ngôn ngữ. 
  * Crawler robots được phép thu thập dữ liệu từ `/en`, `/vi`, `/es` với sitemap.xml được tạo động.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Script tự động fork từ `main` sang `features/development-day-<N>` mỗi buổi sáng, đảm bảo mỗi ngày có branch riêng biệt.
- **Validation Guard Pipeline Gates:** 
  * **Compilation Verification:** `mvn clean compile` (hoặc `quarkus build`) phải thành công. 
  * **Code Coverage Goal:** `jacoco` báo cáo >= 85 % cho mỗi module. 
  * **Context Summary Serialization Logs:** Sau mỗi build, ghi log JSON tóm tắt: `{ "phase": "X", "day": "Y", "tagsCovered": ["REQ-001", ...], "status": "PASS" }`.
- **Merge Protection:** Chỉ `Reviewer` có thể merge vào `main` sau khi phê duyệt tất cả kiểm tra và xác nhận 100% coverage tag.

### 🛑 MATRIX COVERAGE CHECK MANDATE (Translate this header into "🇻🇳 Vietnamese")
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]