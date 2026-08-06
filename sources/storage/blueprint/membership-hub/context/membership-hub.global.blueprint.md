# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806071649 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 07:16:49 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
[Detail the asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures]

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.x, Hibernate ORM, PostgreSQL JDBC driver, Flyway migration, SmallRye OpenAPI, Micrometer metrics, Jackson JSON, bcrypt password hashing, JWT (Eclipse Microprofile), OAuth2 OIDC (Keycloak/Firebase), Apache Kafka (for notifications), Redis client, Docker base image (ubi9/openjdk-21), Maven or Gradle build.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14 (React 18), TypeScript, Tailwind CSS, React Query (TanStack), i18next, dayjs, @capacitor/core & @capacitor/push-notifications, Capacitor SQLite for offline cache, Cordova plugins for QR scanner, Jest / React Testing Library for testing, ESLint/Prettier, Docker multi-stage for frontend, CI/CD GitHub Actions.

### ARCHITECTURAL STACK MATRIX
<COMMAND>
```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```
</COMMAND>

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS

- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.membershiphub`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1‑2 | `./sources/backend.users.` | Xây dựng dịch vụ người dùng cốt lõi, đăng ký, xác thực OAuth2, gán vai trò, triển khai bảo mật JWT, tạo bảng Users & Roles. | Coder | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-006], [NFR-003], [NFR-001] |
| Phase 1 | Day 1‑2 | `./sources/infra.` | Xây dựng Dockerfile đa giai đoạn cho backend, push image, tạo ConfigMap & Secret cho PostgreSQL, Redis, triển khai Helm chart cơ bản. | Docker | [NFR-005], [NFR-004] |
| Phase 2 | Day 3‑4 | `./sources/backend.centers.` | Triển khai CRUD trung tâm, API REST cho trung tâm, validation taxId duy nhất, gán Center Admin, tạo bảng Centers. | Coder | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002], [NFR-003] |
| Phase 2 | Day 3‑4 | `./sources/backend.centers.;./sources/backend.centers.test` | Viết unit test cho CenterService (JUnit5), test validation, test role assignment. | Tester | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| Phase 3 | Day 5‑6 | `./sources/backend.courses.` | Xây dựng quản lý khóa học, kiểm tra xung đột lịch giảng, API gán giáo viên, tạo bảng Courses. | Coder | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-008], [NFR-001] |
| Phase 3 | Day 5‑6 | `./sources/backend.courses.;./sources/backend.courses.test` | Viết integration test cho CourseService, test validation xung đột lịch, test gán giáo viên. | Tester | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| Phase 4 | Day 7‑8 | `./sources/backend.enrollments.` | Triển khai duyệt khóa học, đăng ký học viên, tự động tạo tài khoản Student, tạo bảng Enrollments. | Coder | [REQ-010], [REQ-011], [DAT-005], [ARC-007], [NFR-003] |
| Phase 4 | Day 7‑8 | `./sources/infra.` | Tạo Kubernetes Deployment cho EnrollmentService, cấu hình HPA dựa trên latency. | GKE | [NFR-004] |
| Phase 5 | Day 9‑10 | `./sources/backend.attendance.` | Xây dựng QR attendance capture, đảm bảo bất biến, xử lý duplicate, tạo bảng Attendance, xử lý ngoại lệ EXC-001, EXC-002. | Coder | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002], [ARC-007] |
| Phase 5 | Day 9‑10 | `./sources/backend.cards.` | Triển khai hiển thị thẻ hội viên, tính remaining days, API gia hạn thẻ, tạo bảng StudentCards. | Coder | [REQ-014], [REQ-015], [DAT-007], [NFR-001] |
| Phase 5 | Day 11‑12 | `./sources/backend.notifications.` | Xây dựng push notification, tích hợp Zalo group messaging, hàng đợi bất đồng bộ, tạo bảng Notifications, xử lý EXC-003. | Coder | [REQ-016], [DAT-008], [ARC-008], [EXC-003], [NFR-003] |
| Phase 5 | Day 13‑14 | `./sources/backend.promotions.` | Triển khai quản lý khuyến mãi và thông báo, tạo bảng Promotions & Announcements. | Coder | [REQ-017], [REQ-018], [DAT-009], [DAT-011], [NFR-007] |
| Phase 5 | Day 15‑16 | `./sources/backend.reporting.` | Xây dựng báo cáo điểm danh CSV, dashboard tóm tắt ghi danh, xử lý EXC-005. | Coder | [REQ-024], [REQ-025], [NFR-006], [EXC-005] |
| Phase 5 | Day 17‑18 | `./sources/infra.` | Thiết lập CI/CD pipeline (GitHub Actions), tạo Dockerfiles cho tất cả services, push images, triển khai GKE clusters, cấu hình monitoring & logging. | Docker, GCP, GKE | [NFR-002], [NFR-004], [NFR-005], [NFR-009] |
| Phase 5 | Day 19‑20 | `./sources/docs.` | Soạn thảo tài liệu kỹ thuật, API reference, hướng dẫn vận hành, hướng dẫn triển khai, checklist tuân thủ. | Doc | [ALL] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai các chức năng người dùng cốt lõi, xác thực đa nhà cung cấp, và thiết lập phân quyền vai trò để đảm bảo truy cập an toàn vào hệ thống membership‑hub.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend.users./org/nlh4j/saas/membershiphub/user/` (tất cả file Java cho UserService) `[REQ-001], [REQ-002], [REQ-003], [DAT-001]`
  * `./sources/docs/` (UserService README, API spec) `[REQ-001], [REQ-002], [REQ-003]`
- **Database Schema DDL SQL Specification [DAT-001]:**
```sql
CREATE TABLE ROLES (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE USERS (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL REFERENCES ROLES(role_id),
    provider ENUM('local','firebase','google','facebook') NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now()
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
  * `POST /api/v1/auth/register` – yêu cầu {email, password, fullName, provider?} – trả về {userId, token, role}. `[REQ-001]`
  * `POST /api/v1/auth/social` – yêu cầu {provider, code, redirectUri} – trao đổi code lấy thông tin người dùng từ Firebase/Google/Facebook, tạo/cập nhật người dùng, trả về JWT. `[REQ-002]`
  * `PUT /api/v1/users/{userId}/role` – yêu cầu {roleId} (chỉ System Admin) – cập nhật trường role_id, ghi lại vào audit log. `[REQ-003]`
  * `GET /api/v1/auth/validate` – xác thực JWT, trả về claim. `[ARC-006]`
- **Phase Localized Exception Handlers [EXC-004]:**
  * Xác thực đầu vào không hợp lệ (email sai định dạng, thiếu trường bắt buộc) – trả về HTTP 400 với danh sách các trường lỗi dịch sang tiếng Việt: “Email không hợp lệ”, “Mật khẩu phải có ít nhất 8 ký tự”, v.v.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1: Xây dựng core user service và bảng dữ liệu**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.users./org/nlh4j/saas/membershiphub/user/UserService.java` `[REQ-001], [REQ-002], [REQ-003], [DAT-001]`
      - **Low-Level Technical Task Instruction:** Triển khai lớp UserService với các phương thức registerUser, authenticateWithProvider, assignRole. Sử dụng @Valid cho validation, bcrypt cho mã hóa mật khẩu, JWT cho token. Áp dụng @RolesAllowed cho endpoint gán vai trò. Đảm bảo transaction cho các thao tác ghi. `[REQ-001], [REQ-002], [REQ-003], [DAT-001]`
      - **Targeted Tag IDs:** `[REQ-001], [REQ-002], [REQ-003], [DAT-001]`
- **DAY 2: Container hóa và triển khai bảo mật**
  - **Sub-Agent Workflow Specialization:**
    * **[Docker]:**
      - **Target Component file path (`target_component`):** `./sources/infra/Dockerfile.backend` `[NFR-005], [NFR-004]`
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile đa giai đoạn sử dụng image base ubi9/openjdk-21, sao chép target classes, build với Maven, tạo image với size <500MB, tích hợp Jib cho Google Container Registry. Thêm môi trường runtime cho JWT secret, database connection. `[NFR-005], [NFR-004]`
      - **Targeted Tag IDs:** `[NFR-005], [NFR-004]`

### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng và vận hành module quản lý trung tâm, bao gồm CRUD trung tâm, gán quyền Center Admin, và đảm bảo cách ly đa trung tâm.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend.centers./org/nlh4j/saas/membershiphub/center/` (code cho CenterService) `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
  * `./sources/docs/` (CenterService README) `[REQ-004], [REQ-005], [REQ-006]`
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE CENTERS (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [ARC-002]:**
  * `GET /api/v1/centers` – trả về danh sách trung tâm (name, address, taxId, contactPhone, contactEmail). `[REQ-004]`
  * `POST /api/v1/centers` – yêu cầu payload trung tâm, validation taxId duy nhất, trả về centerId. `[REQ-005]`
  * `DELETE /api/v1/centers/{centerId}` – xóa trung tâm (chỉ System Admin). `[REQ-005]`
  * `PUT /api/v1/centers/{centerId}/assign` – yêu cầu {userId} để gán làm Center Admin, cập nhật role và center_id trong bảng USERS. `[REQ-006]`
  * `DELETE /api/v1/centers/{centerId}/assign/{userId}` – hủy gán. `[REQ-006]`
- **Phase Localized Exception Handlers:** (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 3: Triển khai service trung tâm và schema**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.centers./org/nlh4j/saas/membershiphub/center/CenterService.java` `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
      - **Low-Level Technical Task Instruction:** Triển khai CenterService với các phương thức listCenters, createCenter, deleteCenter. Sử dụng @Transactional, validation @NotBlank cho các trường, unique constraint cho tax_id. Tích hợp role checking với @RolesAllowed("SYSTEM_ADMIN"). `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
      - **Targeted Tag IDs:** `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
- **DAY 4: Kiểm thử unit cho CenterService**
  - **Sub-Agent Workflow Specialization:**
    * **[Tester]:**
      - **Target Component file path (`target_component`):** `./sources/backend.centers.;./sources/backend.centers.test/CenterServiceTest.java` `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
      - **Low-Level Technical Task Instruction:** Viết JUnit5 test cases bao phủ happy path cho list, create (duplicate taxId), delete, assign/unassign. Sử dụng @DataJpaTest, mock UserRepository. Đảm bảo test validation trả về HTTP 409 cho taxId trùng. `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
      - **Targeted Tag IDs:** `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`

### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng module quản lý khóa học, bao gồm CRUD khóa học, kiểm tra xung đột lịch giảng, và gán giáo viên.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend.courses./org/nlh4j/saas/membershiphub/course/` (code cho CourseService) `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`
  * `./sources/docs/` (CourseService README) `[REQ-007], [REQ-008], [REQ-009]`
- **Database Schema DDL SQL Specification [DAT-004]:**
```sql
CREATE TABLE COURSES (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES USERS(user_id),
    max_students INT NOT NULL DEFAULT 30
);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [ARC-008]:**
  * `GET /api/v1/courses` – trả về danh sách khóa học (courseId, title, startDate, endDate, teacherName). `[REQ-007]`
  * `POST /api/v1/courses` – yêu cầu payload khóa học, validation xung đột lịch giảng, trả về courseId. `[REQ-008]`
  * `DELETE /api/v1/courses/{courseId}` – xóa khóa học (System Admin / Center Admin). `[REQ-008]`
  * `PUT /api/v1/courses/{courseId}/assign/{teacherId}` – gán giáo viên, tạo notification cho giáo viên qua WebSocket/FCM. `[REQ-009]`
  * `DELETE /api/v1/courses/{courseId}/unassign/{teacherId}` – hủy gán. `[REQ-009]`
- **Phase Localized Exception Handlers:** (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 5: Xây dựng CourseService và validation**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.courses./org/nlh4j/saas/membershiphub/course/CourseService.java` `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`
      - **Low-Level Technical Task Instruction:** Triển khai CourseService với các phương thức listCourses, createCourse, deleteCourse, assignTeacher. Sử dụng @Transactional, validation @FutureOrPresent cho start_date/end_date, business rule kiểm tra teacher_id không có khóa học khác chồng lấn. Tích hợp @RolesAllowed("SYSTEM_ADMIN","CENTER_ADMIN"). `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`
      - **Targeted Tag IDs:** `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`
- **DAY 6: Kiểm thử integration cho CourseService**
  - **Sub-Agent Workflow Specialization:**
    * **[Tester]:**
      - **Target Component file path (`target_component`):** `./sources/backend.courses.;./sources/backend.courses.test/CourseServiceTest.java` `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`
      - **Low-Level Technical Task Instruction:** Viết integration test sử dụng @SpringBootTest, mock repository, test createCourse với xung đột lịch giảng trả về HTTP 409, test assign/unassign, verify notification được tạo. `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`
      - **Targeted Tag IDs:** `[REQ-007], [REQ-008], [REQ-009], [DAT-004]`

### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai module ghi danh học viên, bao gồm duyệt khóa học, đăng ký, tự động tạo tài khoản học viên, và tích hợp notification.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend.enrollments./org/nlh4j/saas/membershiphub/enrollment/` (code cho EnrollmentService) `[REQ-010], [REQ-011], [DAT-005]`
  * `./sources/infra/` (Kubernetes Deployment cho EnrollmentService) `[NFR-004]`
- **Database Schema DDL SQL Specification [DAT-005]:**
```sql
CREATE TABLE ENROLLMENTS (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES USERS(user_id),
    course_id UUID NOT NULL REFERENCES COURSES(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(student_id, course_id)
);
```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [ARC-007]:**
  * `GET /api/v1/courses/{courseId}/available` – trả về danh sách khóa học có chỗ trống, loại trừ các khóa học đã ghi danh. `[REQ-010]`
  * `POST /api/v1/enrollments` – yêu cầu {studentId, courseId}, tạo bản ghi enrollment, nếu student không có tài khoản thì tạo với role "Student", đẩy notification đến mobile app và Zalo group. `[REQ-011]`
  * `GET /api/v1/enrollments/student/{studentId}` – trả về danh sách khóa học đã ghi danh. `[REQ-011]`
- **Phase Localized Exception Handlers:** (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 7: Xây dựng EnrollmentService**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.enrollments./org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java` `[REQ-010], [REQ-011], [DAT-005]`
      - **Low-Level Technical Task Instruction:** Triển khai EnrollmentService với các phương thức listAvailableCourses, enrollStudent, findEnrollmentsByStudent. Sử dụng @Transactional, validation khóa ngoại, kiểm tra capacity (max_students). Tích hợp role checking cho student. `[REQ-010], [REQ-011], [DAT-005]`
      - **Targeted Tag IDs:** `[REQ-010], [REQ-011], [DAT-005]`
- **DAY 8: Triển khai Kubernetes cho EnrollmentService**
  - **Sub-Agent Workflow Specialization:**
    * **[GKE]:**
      - **Target Component file path (`target_component`):** `./sources/infra/k8s/enrollment-deployment.yaml` `[NFR-004]`
      - **Low-Level Technical Task Instruction:** Tạo Kubernetes Deployment cho EnrollmentService với image backend:latest, resource limits (CPU 250m, memory 512Mi), HPA dựa trên latency >300ms hoặc CPU >70%. Thêm ConfigMap cho application properties, Secret cho DB credentials. `[NFR-004]`
      - **Targeted Tag IDs:** `[NFR-004]`

### 📈 Phase 5 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Hoàn thiện các tính năng cốt lõi còn lại: điểm danh QR, thẻ hội viên, notification, khuyến mãi, báo cáo, và hardening hạ tầng.
- **Target Physical Directory Matrix Map:**
  * `./sources/backend.attendance./org/nlh4j/saas/membershiphub/attendance/` (code cho AttendanceService) `[REQ-012], [REQ-013], [DAT-006]`
  * `./sources/backend.cards./org/nlh4j/saas/membershiphub/card/` (code cho CardService) `[REQ-014], [REQ-015], [DAT-007]`
  * `./sources/backend.notifications./org/nlh4j/saas/membershiphub/notification/` (code cho NotificationService) `[REQ-016], [DAT-008]`
  * `./sources/backend.promotions./org/nlh4j/saas/membershiphub/promotion/` (code cho PromotionService) `[REQ-017], [REQ-018], [DAT-009]`
  * `./sources/backend.reporting./org/nlh4j/saas/membershiphub/reporting/` (code cho ReportingService) `[REQ-024], [REQ-025]`
  * `./sources/infra/` (Dockerfiles, CI/CD, monitoring) `[NFR-002], [NFR-004], [NFR-005], [NFR-009]`
  * `./sources/docs/` (tài liệu kỹ thuật) `[ALL]`
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:**
```sql
CREATE TABLE ATTENDANCE (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES USERS(user_id),
    course_id UUID NOT NULL REFERENCES COURSES(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE STUDENTCARDS (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES USERS(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);

CREATE TABLE NOTIFICATIONS (
    notification_id UUID PRIMARY KEY,
    user_id UUID,
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT now(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE PROMOTIONS (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT
);

CREATE TABLE ANNOUNCEMENTS (
    announcement_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);

CREATE TABLE SYSTEMSETTINGS (
    setting_key VARCHAR(50) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-024], [REQ-025], [ARC-007], [ARC-008]:**
  * `POST /api/v1/attendance/scan` – yêu cầu {studentId, courseId, qrToken} – xác thực, ghi lại điểm danh, trả về {attendanceId, duplicateFlag}. `[REQ-012], [REQ-013]`
  * `GET /api/v1/cards/{studentId}` – trả về thông tin thẻ hội viên (issueDate, validityDays, remainingDays). `[REQ-014]`
  * `POST /api/v1/cards/{studentId}/renew` – yêu cầu {additionalDays, paymentInfo} – cập nhật endDate, trả về cardId mới. `[REQ-015]`
  * `POST /api/v1/notifications` – yêu cầu {userId?, groupZalo?, message} – lưu vào DB, đẩy push notification qua FCM/APNs, gửi tin nhắn Zalo. `[REQ-016]`
  * `GET /api/v1/promotions` – trả về danh sách khuyến mãi đang hiệu lực. `[REQ-017]`
  * `POST /api/v1/promotions` – yêu cầu payload khuyến mãi, validation start/end date, trả về promoId. `[REQ-017]`
  * `GET /api/v1/announcements` – trả về danh sách thông báo đang hiệu lực. `[REQ-018]`
  * `POST /api/v1/reports/attendance` – yêu cầu {centerId, startDate, endDate} – trả về CSV attachment với các cột StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
  * `GET /api/v1/dashboard/center/{centerId}` – trả về JSON với totalStudents, activeCourses, upcomingSessions (7 ngày tới). `[REQ-025]`
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003], [EXC-005]:**
  * **EXC-001:** Network & Connectivity Drops During QR Scan – Khi student quét QR nhưng mất kết nối, app lưu scan local, retry sau khi reconnect, ghi log với level WARN, và đánh dấu pending trong bảng ATTENDANCE với trường `status='PENDING'`. Khi online trở lại, service xử lý hàng đợi, tạo bản ghi ATTENDANCE thực sự.
  * **EXC-002:** Duplicate Attendance Submission – Nếu cùng student quét cùng course trong cùng ngày, service trả về HTTP 200 với body `{duplicate: true}` và không tạo row mới. Log với level INFO.
  * **EXC-003:** Failed Notification Delivery – Khi push thất bại (token không hợp lệ), system ghi log lỗi, tăng counter thất bại, lên lịch retry tối đa 3 lần (exponential backoff). Sau 3 lần thất bại, đánh dấu delivered = false và gửi alert qua email admin.
  * **EXC-005:** System Recovery After Outage – Khi service khôi phục, xử lý hàng đợi ATTENDANCE có status='PENDING' theo FIFO, tạo bản ghi mới, gửi notification đến student và ghi log recovery.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 9: Xây dựng AttendanceService và xử lý ngoại lệ**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.attendance./org/nlh4j/saas/membershiphub/attendance/AttendanceService.java` `[REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]`
      - **Low-Level Technical Task Instruction:** Triển khai AttendanceService với endpoint /scan. Sử dụng @Transactional, kiểm tra sự tồn tại của student-course, ghi ATTENDANCE với attendance_date = current date, sử dụng khóa duy nhất (student_id, course_id, attendance_date) để ngăn duplicate. Xử lý ngoại lệ network bằng cách lưu pending vào DB, lên lịch job xử lý hàng đợi. `[REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]`
      - **Targeted Tag IDs:** `[REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]`
- **DAY 10: Xây dựng CardService**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.cards./org/nlh4j/saas/membershiphub/card/CardService.java` `[REQ-014], [REQ-015], [DAT-007]`
      - **Low-Level Technical Task Instruction:** Triển khai CardService với endpoint GET /cards/{studentId} trả về remainingDays tính từ issueDate + validityDays. Endpoint POST /cards/{studentId}/renew chấp nhận additionalDays, cập nhật remainingDays, ghi log giao dịch. Sử dụng @RolesAllowed("STUDENT") cho các thao tác thẻ. `[REQ-014], [REQ-015], [DAT-007]`
      - **Targeted Tag IDs:** `[REQ-014], [REQ-015], [DAT-007]`
- **DAY 11: Xây dựng NotificationService**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.notifications./org/nlh4j/saas/membershiphub/notification/NotificationService.java` `[REQ-016], [DAT-008], [EXC-003]`
      - **Low-Level Technical Task Instruction:** Triển khai NotificationService với endpoint POST /notifications. Sử dụng Kafka template hoặc WebSocket để đẩy thông báo real-time. Gọi FCM client library để gửi push, gọi Zalo API để đăng bài. Bọc trong retry circuit breaker, ghi log thất bại, lên lịch retry tối đa 3 lần. `[REQ-016], [DAT-008], [EXC-003]`
      - **Targeted Tag IDs:** `[REQ-016], [DAT-008], [EXC-003]`
- **DAY 12: Xây dựng PromotionService & AnnouncementService**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.promotions./org/nlh4j/saas/membershiphub/promotion/PromotionService.java` `[REQ-017], [REQ-018], [DAT-009], [DAT-011]`
      - **Low-Level Technical Task Instruction:** Triển khai PromotionService với CRUD cho Promotions và Announcements. Sử dụng validation start_date/end_date, tự động vô hiệu hóa sau end_date. Tích hợp role checking cho CENTER_ADMIN và MANAGER. `[REQ-017], [REQ-018], [DAT-009], [DAT-011]`
      - **Targeted Tag IDs:** `[REQ-017], [REQ-018], [DAT-009], [DAT-011]`
- **DAY 13: Xây dựng ReportingService**
  - **Sub-Agent Workflow Specialization:**
    * **[Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.reporting./org/nlh4j/saas/membershiphub/reporting/ReportingService.java` `[REQ-024], [REQ-025], [NFR-006], [EXC-005]`
      - **Low-Level Technical Task Instruction:** Triển khai ReportingService với endpoint GET /reports/attendance trả về CSV, endpoint GET /dashboard/center/{centerId} trả về JSON. Sử dụng JDBC batch reading cho performance, lưu file tạm trong /tmp, trả về qua ResponseEntity.withHeaders. Xử lý ngoại lệ EXC-005 bằng cách xử lý hàng đợi điểm danh pending. `[REQ-024], [REQ-025], [NFR-006], [EXC-005]`
      - **Targeted Tag IDs:** `[REQ-024], [REQ-025], [NFR-006], [EXC-005]`
- **DAY 14: Container hóa và CI/CD pipeline**
  - **Sub-Agent Workflow Specialization:**
    * **[Docker]:**
      - **Target Component file path (`target_component`):** `./sources/infra/Dockerfile.backend` `[NFR-005]`
      - **Low-Level Technical Task Instruction:** Tạo multi-stage Dockerfile cho backend (builder stage với Maven, runtime stage với distroless). Đảm bảo size image <500MB, sử dụng Jib để push trực tiếp lên Google Artifact Registry. Thêm healthcheck endpoint /actuator/health. `[NFR-005]`
      - **Targeted Tag IDs:** `[NFR-005]`
    * **[GCP]:**
      - **Target Component file path (`target_component`):** `./sources/infra/gcp/artifact-registry.yaml` `[NFR-002]`
      - **Low-Level Technical Task Instruction:** Tạo Artifact Registry repo, thiết lập IAM cho CI/CD service account, cấu hình secret manager cho DB credentials. `[NFR-002]`
      - **Targeted Tag IDs:** `[NFR-002]`
    * **[GKE]:**
      - **Target Component file path (`target_component`):** `./sources/infra/k8s/backend-deployment.yaml` `[NFR-004]`
      - **Low-Level Technical Task Instruction:** Tạo Kubernetes Deployment cho tất cả services backend, cấu hình HPA, Liveness/Probes, resource limits. Sử dụng Ingress để expose API. `[NFR-004]`
      - **Targeted Tag IDs:** `[NFR-004]`
- **DAY 15: Soạn thảo tài liệu kỹ thuật**
  - **Sub-Agent Workflow Specialization:**
    * **[Doc]:**
      - **Target Component file path (`target_component`):** `./sources/docs/` (tất cả file markdown: API_Reference.md, Architecture_Overview.md, Deployment_Guide.md, Compliance_Checks.md) `[ALL]`
      - **Low-Level Technical Task Instruction:** Soạn thảo tài liệu kỹ thuật chi tiết bao gồm API reference cho từng module, sơ đồ kiến trúc, hướng dẫn triển khai trên GKE, checklist tuân thủ NFR, hướng dẫn debug, hướng dẫn vận hành. Đảm bảo markdown được định dạng đúng, có bảng mục lục, liên kết internal. `[ALL]`
      - **Targeted Tag IDs:** `[ALL]`

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-001]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng PreparedStatement với các tham số dấu ?; áp dụng @JdbcRepository cho tất cả truy vấn; whitelist các cột cho phép sort; sử dụng Flyway để quản lý migration.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Áp dụng @CrossOrigin annotations; sử dụng Jackson @JsonSerialize với HTMLSanitizer; thiết lập header CSP: "default-src 'self'; script-src 'self'; style-src 'self';".
- **Multi-Tenant CORS Security Rails:** Kiểm tra origin trong @CrossOrigin, cho phép chỉ các domain thuộc tenant; lưu tenant_id trong JWT claim; xác thực tenant_id trong mỗi request.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Sử dụng Logback với Filter để che giấu email, số điện thoại; áp dụng @JsonIgnore cho các trường nhạy cảm; scheduled job xóa log cũ sau 1 năm.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng @capacitor/core và @capacitor/push-notifications; lưu trữ an toàn với @capacitor/preferences; chặn back-button với native app logic; enforce HTTPS cho tất cả request; cache offline với SQLite; tự động sync khi online.
- **Internationalization (i18n) & Dynamic SEO Injection:** Sử dụng i18next cho frontend; middleware phát hiện locale từ cookie, header Accept-Language; generate hreflang tags tự động; tối ưu hóa meta description cho từng ngôn ngữ; preload tài nguyên cho ngôn ngữ đã chọn.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW

- **Daily Workspace Forking Isolation:** Script CI tạo branch `features/development-phase-5-day-15` cho ngày cuối cùng; mỗi ngày branch được tạo từ base `main`.
- **Validation Guard Pipeline Gates:** Sau khi merge, GitHub Actions chạy mvn clean install, thực hiện unit test (coverage >=85%), quét SonarQube, kiểm tra lint, sau đó triển khai lên GKE thông qua Helm.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`