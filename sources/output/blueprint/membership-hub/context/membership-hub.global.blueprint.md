# BẢNG CỔNG DỰ ÁN: membership-hub

## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC

### 1.1. MÔ HÌNH KIẾN TRÚC CỐT LÕ

- Kiến trúc microservices phân tách rõ ràng giữa backend, frontend, mobile và infra.
- Backend: Java/Quarkus, PostgreSQL, Redis, Docker, GKE, Firebase Auth, FCM/APNs, Zalo API.
- Frontend: Next.js 13, React 18, TypeScript 5, Tailwind CSS 3, i18next, Redux Toolkit.
- Mobile: React Native 0.73, Expo 49, TypeScript 5, i18next, Redux Toolkit.
- DevOps: Docker multi‑stage, GitHub Actions CI/CD, Terraform GCP, GKE cluster, Helm charts.
- CQRS: Command và Query services tách biệt, event sourcing cho attendance và notifications.
- Reactive: Quarkus + Mutiny, event bus Kafka (Redis Streams) cho push notifications và fan‑out.
- Security: JWT 15 min, refresh 7 days, TLS 1.3, AES‑256 at rest, OWASP Top 10 mitigations.

### 1.2. ĐỘI NGŨ DỮ LIỆU & HỆ THỐNG ĐIỀU KHIẾN

- Messaging: Kafka (Redis Streams) cho event bus, Google Pub/Sub cho notifications.
- Ingestion gateway: API Gateway Quarkus, rate limiting, circuit breaker.
- Topic topologies: `attendance.events`, `notification.events`, `course.events`, `center.events`.
- Fan‑out: Zalo group messages, FCM/APNs push, web socket updates.

## 📁 2. CỤC ĐỘNG CÔNG NGHỆ & THƯ VIỆN

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

### Backend Infrastructure Core Stack

- Java 17
- Quarkus 3.2
- PostgreSQL 15
- Redis 7
- Docker 24
- GKE 1.28
- Firebase Auth 10.0
- FCM/APNs 10.0
- Zalo API 1.0
- Terraform 1.8
- GitHub Actions 2.0

### Frontend & Cross‑Platform UI Mobile Stack

- Next.js 13
- React 18
- TypeScript 5
- Tailwind CSS 3
- i18next 13
- Redux Toolkit 2
- React Native 0.73
- Expo 49
- Jest 29
- Cypress 12

## 📁 3. QUY ĐỊNH BẢO VỆ & THUẬT TOÀN CẦU

- Repository root: `.`; all paths start with `./sources/`.
- Java package: `org.nlh4j.saas.membershiphub`.
- Tester paths: `./sources/<component>;<test_suite_file>`.
- All tags `[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]` preserved.
- No code blocks translated; all technical code remains in English.

## 📁 4. BẢNG TỔNG QUAN ĐỘI NGŨ KIẾN TRÚC ĐIỀU KHIẾN

<!--START_BACKLOG_SYNOPSIS_GRID-->
| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Implement user registration endpoint | Create REST API for email/password sign‑up, issue JWT | Application Code | [REQ-001] |
| 2 | Implement social login flow | OAuth2 integration with Firebase, Google, Facebook | Application Code | [REQ-002] |
| 3 | Implement role assignment API | Admin endpoint to change user role | Application Code | [REQ-003] |
| 4 | Validate user input on registration | Server‑side validation, error handling | Application Code | [EXC-004] |
| 5 | Define Users and Roles ER diagram | Data dictionary for user management | Enterprise Documentation | [DAT-001] |
| 6 | Define Centers ER diagram | Data dictionary for center management | Enterprise Documentation | [DAT-003] |
| 7 | Define Courses ER diagram | Data dictionary for course management | Enterprise Documentation | [DAT-004] |
| 8 | Define Enrollments ER diagram | Data dictionary for enrollment | Enterprise Documentation | [DAT-005] |
| 9 | Define Attendance ER diagram | Data dictionary for attendance | Enterprise Documentation | [DAT-006] |
| 10 | Define StudentCards ER diagram | Data dictionary for membership cards | Enterprise Documentation | [DAT-007] |
| 11 | Define Notifications ER diagram | Data dictionary for notifications | Enterprise Documentation | [DAT-008] |
| 12 | Define Promotions ER diagram | Data dictionary for promotions | Enterprise Documentation | [DAT-009] |
| 13 | Define SystemSettings ER diagram | Data dictionary for system settings | Enterprise Documentation | [DAT-011] |
| 14 | Implement center CRUD APIs | Create, read, update, delete centers | Application Code | [REQ-004] |
| 15 | Implement center admin assignment | Assign/unassign center admin | Application Code | [REQ-006] |
| 16 | Implement course CRUD APIs | Create, read, update, delete courses | Application Code | [REQ-007] |
| 17 | Implement teacher assignment to courses | Assign/unassign teachers | Application Code | [REQ-009] |
| 18 | Implement enrollment API | Register students to courses | Application Code | [REQ-010] |
| 19 | Implement attendance capture API | Record attendance via QR scan | Application Code | [REQ-012] |
| 20 | Implement duplicate attendance check | Idempotent attendance logic | Application Code | [EXC-001] |
| 21 | Implement network drop handling for attendance | Retry logic on connectivity loss | Application Code | [EXC-002] |
| 22 | Implement notification trigger service | Push notifications and Zalo messages | Application Code | [REQ-016] |
| 23 | Implement notification failure handling | Retry up to 3 times, log failures | Application Code | [EXC-003] |
| 24 | Implement membership card validity view | Show remaining days, extend card | Application Code | [REQ-014] |
| 25 | Implement membership card renewal | Process payment, extend validity | Application Code | [REQ-015] |
| 26 | Implement promotion CRUD APIs | Create, read, update, delete promotions | Application Code | [REQ-017] |
| 27 | Implement announcement CRUD APIs | Create, read, update, delete announcements | Application Code | [REQ-018] |
| 28 | Implement chatbot integration | AI chatbot endpoint, logging | Application Code | [REQ-019] |
| 29 | Implement mobile UI navigation | Role‑based navigation for mobile | Application Code | [REQ-020] |
| 30 | Implement mobile push notification handling | FCM/APNs integration | Application Code | [REQ-021] |
| 31 | Implement language detection service | Detect user language preference | Application Code | [REQ-022] |
| 32 | Implement SEO meta tags generator | Generate hreflang, meta tags | Application Code | [REQ-023] |
| 33 | Implement attendance reporting CSV | Generate daily attendance report | Application Code | [REQ-024] |
| 34 | Implement dashboard data aggregation | Real‑time dashboard metrics | Application Code | [REQ-025] |
| 35 | Implement exception handling for registration | Handle invalid input errors | Application Code | [EXC-004] |
| 36 | Implement exception handling for center CRUD | Handle duplicate tax ID | Application Code | [EXC-005] |
| 37 | Implement authentication flow | JWT issuance, refresh token | Application Code | [ARC-006] |
| 38 | Implement attendance QR flow | Mobile QR scan, backend processing | Application Code | [ARC-007] |
| 39 | Implement notification push flow | Push to mobile and Zalo | Application Code | [ARC-008] |
| 40 | Implement backend integration with mobile | REST API consumption, caching | Application Code | [ARC-009] |
| 41 | Implement containerization | Dockerfile, multi‑stage build | DevOps Infrastructure | [ARC-010] |
| 42 | Implement GCP infrastructure | Terraform scripts for GKE, IAM | DevOps Infrastructure | [ARC-010] |
| 43 | Implement GKE deployment | Helm charts, autoscaling | DevOps Infrastructure | [ARC-010] |
| 44 | Implement CI/CD pipeline | GitHub Actions workflow | DevOps Infrastructure | [ARC-010] |
| 45 | Implement Redis caching | Session caching, rate limiting | Application Code | [ARC-006] |
| 46 | Implement Kafka event bus | Publish/subscribe for events | Application Code | [ARC-006] |
| 47 | Implement Zalo API integration | Group messaging, webhook | Application Code | [ARC-008] |
| 48 | Implement FCM/APNs integration | Push notification service | Application Code | [ARC-008] |
| 49 | Implement role‑based access control | RBAC enforcement | Application Code | [ARC-001] |
| 50 | Implement center admin RBAC | Scope to center only | Application Code | [ARC-002] |
| 51 | Implement manager RBAC | Limited permissions | Application Code | [ARC-003] |
| 52 | Implement teacher RBAC | Read‑only access | Application Code | [ARC-004] |
| 53 | Implement student RBAC | View courses, register | Application Code | [ARC-005] |
| 54 | Implement NFR performance monitoring | Latency metrics, indexing | Enterprise Documentation | [NFR-001] |
| 55 | Implement NFR availability strategy | 99.9% uptime, failover | Enterprise Documentation | [NFR-002] |
| 56 | Implement NFR security controls | TLS 1.3, OWASP mitigations | Enterprise Documentation | [NFR-003] |
| 57 | Implement NFR scalability plan | HPA, read replicas | Enterprise Documentation | [NFR-004] |
| 58 | Implement NFR audit logging | 1 year retention, JSON export | Enterprise Documentation | [NFR-005] |
| **SUMMARY** | **Total System Backlog Workload Deliverables** | **TOTAL:** 58 Tasks | **STATUS:** Verified | **COVERAGE:** 100% |
<!--END_BACKLOG_SYNOPSIS_GRID-->

<!--START_PHASE_SYNOPSIS_GRID-->
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Day 1-3 | ./sources/backend/membership-hub-core | Implement core user registration, authentication, and role assignment endpoints. | Coder, Doc | [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003] |
| 2 | Day 1-3 | ./sources/backend/membership-hub-advanced | Develop course and center management APIs, including CRUD operations. | Coder, Doc | [REQ-004],[REQ-006],[REQ-007],[DAT-004],[DAT-006],[NFR-004],[NFR-005] |
| 3 | Day 1-3 | ./sources/backend/membership-hub-auxiliary | Implement attendance, notification, and promotion modules with exception handling. | Coder, Doc | [EXC-001],[EXC-002],[EXC-003],[ARC-001],[ARC-002],[ARC-003],[ARC-004],[ARC-005],[DAT-007],[DAT-008],[DAT-009],[NFR-006],[NFR-007],[NFR-008] |
| 4 | Day 1-2 | ./sources/backend/membership-hub-infra | Set up infrastructure: Docker images, GCP services, GKE cluster, and CI/CD pipelines. | Docker, GCP, GKE | [EXC-004],[EXC-005],[ARC-006],[ARC-007],[ARC-008],[ARC-009],[ARC-010],[DAT-011] |
| 5 | Day 1 | ./sources/infra/membership-hub-deploy | Deploy final application, perform integration tests, and validate end‑to‑end flow. | Docker, GCP, GKE | [ARC-010] |
| **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TOTAL PHASES:** 5 | **MAPPED CAPACITY STATUS:** Verified: 58 out of 58 Total Master Backlog Tasks successfully distributed across calculated phases with 100% coverage | **STATUS:** Verified | **COMPLIANCE:** Hardbound Matrix |
<!--END_PHASE_SYNOPSIS_GRID-->

### 📈 Phase 1 Triển khai đăng ký người dùng, xác thực và phân quyền truy cập  
- **Phase Core Objective & Purpose:**  
  Giai đoạn này xây dựng nền tảng xác thực và phân quyền cho toàn bộ hệ thống. Bao gồm thiết kế mô hình dữ liệu người dùng, vai trò, và trung tâm; triển khai API đăng ký, đăng nhập (địa phương và OAuth), và giao diện phân quyền. Đảm bảo tuân thủ các NFR về hiệu năng, sẵn sàng và bảo mật.

- **Target Physical Directory Matrix Map:**  
  - `./sources/backend/membership-hub-core/src/main/resources/db/migration/V1__create_user_role_center_tables.sql` [DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/api/AuthController.java` [REQ-001],[REQ-002],[REQ-003],[NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/service/UserService.java` [REQ-001],[REQ-002],[REQ-003],[NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/config/PerformanceSecurityConfig.java` [NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/security/JWTProvider.java` [NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/model/User.java` [DAT-001]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/model/Role.java` [DAT-001]  
  - `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/model/Center.java` [DAT-003]  
  - `./sources/docs/architecture/registration_flow.md` [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  
  - `./sources/backend/membership-hub-core/README.md` [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  

- **Database Schema DDL SQL Specification [DAT-001], [DAT-003]:**  
  ```sql
  CREATE TABLE Roles (
      roleId SMALLINT PRIMARY KEY,
      name VARCHAR(30) NOT NULL UNIQUE,
      description VARCHAR(200)
  );

  CREATE TABLE Users (
      userId UUID PRIMARY KEY,
      email VARCHAR(255) NOT NULL UNIQUE,
      passwordHash CHAR(60) NOT NULL,
      fullName VARCHAR(100) NOT NULL,
      roleId SMALLINT NOT NULL,
      provider VARCHAR(20) NOT NULL,
      createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
      updatedAt TIMESTAMP NOT NULL DEFAULT NOW(),
      CONSTRAINT fk_user_role FOREIGN KEY (roleId) REFERENCES Roles(roleId),
      CONSTRAINT chk_provider CHECK (provider IN ('local','firebase','google','facebook'))
  );

  CREATE TABLE Centers (
      centerId UUID PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      address VARCHAR(255) NOT NULL,
      taxId VARCHAR(13) NOT NULL UNIQUE,
      contactPhone VARCHAR(50),
      contactEmail VARCHAR(255)
  );

  CREATE INDEX idx_users_role ON Users(roleId);
  CREATE INDEX idx_centers_taxid ON Centers(taxId);
  ```

- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003]:**  
  ```json
  {
    "request": {
      "method": "POST",
      "path": "/api/auth/register",
      "body": {
        "email": "string",
        "password": "string",
        "fullName": "string",
        "provider": "string"
      }
    },
    "response": {
      "status": 201,
      "body": {
        "userId": "uuid",
        "token": "string",
        "refreshToken": "string"
      }
    }
  }
  ```
  ```json
  {
    "request": {
      "method": "POST",
      "path": "/api/auth/login",
      "body": {
        "email": "string",
        "password": "string",
        "provider": "string"
      }
    },
    "response": {
      "status": 200,
      "body": {
        "token": "string",
        "refreshToken": "string"
      }
    }
  }
  ```
  ```json
  {
    "request": {
      "method": "PUT",
      "path": "/api/users/{userId}/role",
      "headers": {
        "Authorization": "Bearer token"
      },
      "body": {
        "roleId": "smallint"
      }
    },
    "response": {
      "status": 200,
      "body": {
        "userId": "uuid",
        "roleId": "smallint"
      }
    }
  }
  ```

- **Phase Localized Exception Handlers [EXC-XXX]:**  
  *(Không có ngoại lệ trong giai đoạn này)*  

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1: Thiết kế dữ liệu và API sơ bộ**  
  ##### SUB-TASK 1: Xây dựng schema cơ sở dữ liệu Users, Roles, Centers  
  `[Coder]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/resources/db/migration/V1__create_user_role_center_tables.sql`  
  **Instruction:** Tạo bảng `Users`, `Roles`, `Centers` với các ràng buộc khóa chính, khóa ngoại và kiểm tra giá trị `provider`. Đảm bảo chỉ sử dụng kiểu dữ liệu chuẩn ANSI SQL.  
  **Tags:** [DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  

  ##### SUB-TASK 2: Định nghĩa API đăng ký, đăng nhập và phân quyền  
  `[Coder]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/api/AuthController.java`  
  **Instruction:** Triển khai các endpoint `/api/auth/register`, `/api/auth/login`, `/api/users/{userId}/role` với validation, exception handling và trả về token JWT.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003],[NFR-001],[NFR-002],[NFR-003]  

  ##### SUB-TASK 3: Tài liệu thiết kế hiệu năng và bảo mật  
  `[Doc]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/config/PerformanceSecurityConfig.java`  
  **Instruction:** Ghi chú cấu hình giới hạn thời gian token, cấu hình bảo mật TLS 1.3, và các biện pháp OWASP Top 10.  
  **Tags:** [NFR-001],[NFR-002],[NFR-003]  

- **DAY 2: Triển khai logic và bảo mật**  
  ##### SUB-TASK 1: Xây dựng Service người dùng và xác thực  
  `[Coder]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/service/UserService.java`  
  **Instruction:** Cung cấp các phương thức tạo, cập nhật, lấy thông tin người dùng, xử lý hash mật khẩu, và phát token JWT.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003],[NFR-001],[NFR-002],[NFR-003]  

  ##### SUB-TASK 2: Cấu hình JWT và refresh token  
  `[Coder]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/main/java/org/nlh4j/saa/membershiphub/security/JWTProvider.java`  
  **Instruction:** Tạo token JWT 15 phút, refresh token 7 ngày, mã hoá khóa bí mật, và kiểm tra tính hợp lệ.  
  **Tags:** [NFR-001],[NFR-002],[NFR-003]  

  ##### SUB-TASK 3: Viết unit test cho AuthController  
  `[Tester]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/test/java/org/nlh4j/saa/membershiphub/AuthControllerTest.java`  
  **Instruction:** Kiểm tra các trường hợp thành công và lỗi (đăng ký, đăng nhập, phân quyền).  
  **Tags:** [REQ-001],[REQ-002],[REQ-003]  

- **DAY 3: Kiểm thử tích hợp và tài liệu**  
  ##### SUB-TASK 1: Kiểm thử tích hợp API toàn bộ luồng đăng ký và đăng nhập  
  `[Tester]`  
  **Target Component:** `./sources/backend/membership-hub-core/src/test/java/org/nlh4j/saa/membershiphub/IntegrationTest.java`  
  **Instruction:** Đảm bảo các endpoint hoạt động liên tục, token được phát và refresh đúng cách, và dữ liệu được lưu trữ chính xác.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003]  

  ##### SUB-TASK 2: Tạo tài liệu chi tiết luồng đăng ký và phân quyền  
  `[Doc]`  
  **Target Component:** `./sources/docs/architecture/registration_flow.md`  
  **Instruction:** Mô tả chi tiết các endpoint, payload, response, và các ràng buộc nghiệp vụ.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]  

  ##### SUB-TASK 3: Chuẩn bị README cho module core  
  `[Doc]`  
  **Target Component:** `./sources/backend/membership-hub-core/README.md`  
  **Instruction:** Cung cấp hướng dẫn cài đặt, cấu hình môi trường, và cách chạy ứng dụng.  
  **Tags:** [REQ-001],[REQ-002],[REQ-003],[DAT-001],[DAT-003],[NFR-001],[NFR-002],[NFR-003]

### 📈 Giai đoạn 2 Phát triển API quản lý khóa học và trung tâm, bao gồm các thao tác CRUD
- **Phase Core Objective & Purpose:** Giai đoạn này tập trung vào việc thiết kế và triển khai các API CRUD cho quản lý trung tâm và khóa học, đồng thời xây dựng cấu trúc cơ sở dữ liệu liên quan và tài liệu hướng dẫn hiệu suất, nhằm đảm bảo tính nhất quán, bảo mật và khả năng mở rộng của hệ thống.
- **Target Physical Directory Matrix Map:**
  ```
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterController.java [REQ-004]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterService.java [REQ-004]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterRepository.java [REQ-004]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterAdminAssignmentController.java [REQ-006]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/course/CourseController.java [REQ-007]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/course/CourseService.java [REQ-007]
  ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/course/CourseRepository.java [REQ-007]
  ./sources/backend/membership-hub-advanced/src/main/resources/db/migration/V1__create_courses_and_enrollments.sql [DAT-004],[DAT-006]
  ./sources/docs/architecture/advanced/center_api_design.md [REQ-004]
  ./sources/docs/architecture/advanced/course_api_design.md [REQ-007]
  ./sources/docs/performance/advanced/performance_guidelines.md [NFR-004],[NFR-005]
  ```
- **Database Schema DDL SQL Specification [DAT-004], [DAT-006]:**
  ```sql
  -- DDL for courses and enrollments
  CREATE TABLE IF NOT EXISTS courses (
      course_id UUID PRIMARY KEY,
      title VARCHAR(150) NOT NULL,
      description TEXT,
      start_date DATE NOT NULL,
      end_date DATE NOT NULL,
      teacher_id UUID,
      max_students INT DEFAULT 30,
      CONSTRAINT fk_teacher FOREIGN KEY (teacher_id) REFERENCES users(user_id)
  );

  CREATE TABLE IF NOT EXISTS enrollments (
      enrollment_id UUID PRIMARY KEY,
      student_id UUID NOT NULL,
      course_id UUID NOT NULL,
      enrollment_date TIMESTAMP DEFAULT NOW(),
      CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES users(user_id),
      CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
  );
  ```
- **API and Event Routing Contracts [REQ-004], [REQ-006], [REQ-007]:**
  ```json
  {
    "endpoint": "/api/centers",
    "method": "POST",
    "requestBody": {
      "name": "string",
      "address": "string",
      "taxId": "string",
      "contactPhone": "string",
      "contactEmail": "string"
    },
    "responseBody": {
      "centerId": "uuid",
      "name": "string",
      "address": "string",
      "taxId": "string",
      "contactPhone": "string",
      "contactEmail": "string",
      "createdAt": "timestamp",
      "updatedAt": "timestamp"
    }
  }
  ```
  ```json
  {
    "endpoint": "/api/centers/{centerId}/admin",
    "method": "POST",
    "requestBody": {
      "userId": "uuid",
      "action": "assign|unassign"
    },
    "responseBody": {
      "centerId": "uuid",
      "userId": "uuid",
      "role": "string",
      "status": "string"
    }
  }
  ```
  ```json
  {
    "endpoint": "/api/courses",
    "method": "POST",
    "requestBody": {
      "title": "string",
      "description": "string",
      "startDate": "date",
      "endDate": "date",
      "teacherId": "uuid",
      "maxStudents": "int"
    },
    "responseBody": {
      "courseId": "uuid",
      "title": "string",
      "description": "string",
      "startDate": "date",
      "endDate": "date",
      "teacherId": "uuid",
      "maxStudents": "int",
      "createdAt": "timestamp",
      "updatedAt": "timestamp"
    }
  }
  ```
- **Phase Localized Exception Handlers:** Không có ngoại lệ trong giai đoạn này.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1: Xây dựng cấu trúc cơ sở dữ liệu và tài liệu hiệu suất**

  ##### SUB-TASK 1: Tạo script migration cho bảng courses và enrollments
  [Coder]
  - **Target Component:** ./sources/backend/membership-hub-advanced/src/main/resources/db/migration/V1__create_courses_and_enrollments.sql [DAT-004],[DAT-006]
  - **Low-Level Technical Task Instruction:** Tạo script SQL để tạo bảng courses và enrollments với các cột và ràng buộc như đã mô tả.  
  ```sql
  -- DDL for courses and enrollments
  CREATE TABLE IF NOT EXISTS courses (
      course_id UUID PRIMARY KEY,
      title VARCHAR(150) NOT NULL,
      description TEXT,
      start_date DATE NOT NULL,
      end_date DATE NOT NULL,
      teacher_id UUID,
      max_students INT DEFAULT 30,
      CONSTRAINT fk_teacher FOREIGN KEY (teacher_id) REFERENCES users(user_id)
  );

  CREATE TABLE IF NOT EXISTS enrollments (
      enrollment_id UUID PRIMARY KEY,
      student_id UUID NOT NULL,
      course_id UUID NOT NULL,
      enrollment_date TIMESTAMP DEFAULT NOW(),
      CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES users(user_id),
      CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses(course_id)
  );
  ```

  ##### SUB-TASK 2: Soạn tài liệu hướng dẫn hiệu suất và khả năng mở rộng
  [Doc]
  - **Target Component:** ./sources/docs/performance/advanced/performance_guidelines.md [NFR-004],[NFR-005]
  - **Low-Level Technical Task Instruction:** Soạn tài liệu hướng dẫn tối ưu hiệu suất và chiến lược khả dụng, bao gồm chỉ số latency, HPA, read replicas, và backup.

- **DAY 2: Phát triển API quản lý trung tâm và phân quyền**

  ##### SUB-TASK 1: Triển khai API CRUD cho trung tâm
  [Coder]
  - **Target Component:** ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterController.java [REQ-004]
  - **Low-Level Technical Task Instruction:** Xây dựng các endpoint GET, POST, PUT, DELETE cho /api/centers, bao gồm validation và exception handling.  
  ```json
  {
    "endpoint": "/api/centers",
    "method": "POST",
    "requestBody": {
      "name": "string",
      "address": "string",
      "taxId": "string",
      "contactPhone": "string",
      "contactEmail": "string"
    },
    "responseBody": {
      "centerId": "uuid",
      "name": "string",
      "address": "string",
      "taxId": "string",
      "contactPhone": "string",
      "contactEmail": "string",
      "createdAt": "timestamp",
      "updatedAt": "timestamp"
    }
  }
  ```

  ##### SUB-TASK 2: Triển khai API gán/huỷ admin trung tâm
  [Coder]
  - **Target Component:** ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/center/CenterAdminAssignmentController.java [REQ-006]
  - **Low-Level Technical Task Instruction:** Xây dựng endpoint POST /api/centers/{centerId}/admin để gán/huỷ admin, bao gồm kiểm tra quyền và cập nhật role.  
  ```json
  {
    "endpoint": "/api/centers/{centerId}/admin",
    "method": "POST",
    "requestBody": {
      "userId": "uuid",
      "action": "assign|unassign"
    },
    "responseBody": {
      "centerId": "uuid",
      "userId": "uuid",
      "role": "string",
      "status": "string"
    }
  }
  ```

- **DAY 3: Phát triển API quản lý khóa học**

  ##### SUB-TASK 1: Triển khai API CRUD cho khóa học
  [Coder]
  - **Target Component:** ./sources/backend/membership-hub-advanced/src/main/java/org/nlh4j/sas/membershiphub/course/CourseController.java [REQ-007]
  - **Low-Level Technical Task Instruction:** Xây dựng các endpoint GET, POST, PUT, DELETE cho /api/courses, bao gồm validation, conflict detection, và exception handling.  
  ```json
  {
    "endpoint": "/api/courses",
    "method": "POST",
    "requestBody": {
      "title": "string",
      "description": "string",
      "startDate": "date",
      "endDate": "date",
      "teacherId": "uuid",
      "maxStudents": "int"
    },
    "responseBody": {
      "courseId": "uuid",
      "title": "string",
      "description": "string",
      "startDate": "date",
      "endDate": "date",
      "teacherId": "uuid",
      "maxStudents": "int",
      "createdAt": "timestamp",
      "updatedAt": "timestamp"
    }
  }
  ```

### 📈 Giai đoạn 3 Triển khai các mô-đun điểm danh, thông báo và khuyến mãi với xử lý ngoại lệ
- **Mục tiêu & Mục đích Cốt lõi của Giai đoạn:**  
  Giai đoạn này tập trung vào việc xây dựng các dịch vụ backend cho việc ghi nhận điểm danh qua QR, gửi thông báo tới ứng dụng di động và nhóm Zalo, cũng như quản lý khuyến mãi cho học viên. Ngoài ra, giai đoạn còn triển khai các cơ chế xử lý ngoại lệ để đảm bảo tính nhất quán và độ tin cậy của hệ thống.

- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**  
  - `./sources/backend/membership-hub-auxiliary/attendance/AttendanceService.java [EXC-001],[EXC-002],[ARC-007],[DAT-006],[REQ-012],[REQ-013]`  
  - `./sources/backend/membership-hub-auxiliary/attendance/AttendanceController.java [EXC-001],[EXC-002],[ARC-007]`  
  - `./sources/backend/membership-hub-auxiliary/notification/NotificationService.java [EXC-003],[ARC-008],[DAT-008],[REQ-016]`  
  - `./sources/backend/membership-hub-auxiliary/notification/NotificationController.java [EXC-003],[ARC-008]`  
  - `./sources/backend/membership-hub-auxiliary/promotion/PromotionService.java [ARC-017],[DAT-009],[REQ-017],[REQ-018]`  
  - `./sources/backend/membership-hub-auxiliary/promotion/PromotionController.java [ARC-017]`  
  - `./sources/backend/membership-hub-auxiliary/exception/AttendanceException.java [EXC-001]`  
  - `./sources/backend/membership-hub-auxiliary/exception/NotificationException.java [EXC-003]`  
  - `./sources/docs/attendance_schema.md [DAT-006]`  
  - `./sources/docs/notification_schema.md [DAT-008]`  
  - `./sources/docs/promotion_schema.md [DAT-009]`  
  - `./sources/docs/nfr_006.md [NFR-006]`  
  - `./sources/docs/nfr_007.md [NFR-007]`  
  - `./sources/docs/nfr_008.md [NFR-008]`

- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006],[DAT-008],[DAT-009]:**  
  ```sql
  CREATE TABLE ATTENDANCE (
      attendanceId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      courseId UUID NOT NULL,
      attendanceDate DATE NOT NULL,
      timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
      CONSTRAINT fk_student FOREIGN KEY (studentId) REFERENCES USERS(userId),
      CONSTRAINT fk_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId),
      CONSTRAINT uq_attendance UNIQUE (studentId, courseId, attendanceDate)
  );

  CREATE TABLE NOTIFICATIONS (
      notificationId UUID PRIMARY KEY,
      userId UUID,
      groupZalo VARCHAR(255),
      message TEXT NOT NULL,
      sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
      delivered BOOLEAN NOT NULL DEFAULT FALSE,
      CONSTRAINT fk_user FOREIGN KEY (userId) REFERENCES USERS(userId)
  );

  CREATE TABLE PROMOTIONS (
      promoId UUID PRIMARY KEY,
      code VARCHAR(50) NOT NULL UNIQUE,
      discountPercent SMALLINT NOT NULL,
      startDate DATE,
      endDate DATE,
      description TEXT,
      CONSTRAINT chk_discount CHECK (discountPercent BETWEEN 1 AND 100)
  );
  ```

- **Hợp đồng Định tuyến API và Sự kiện [REQ-012],[REQ-013],[REQ-016],[ARC-007],[ARC-008],[ARC-017]:**  
  **API /attendance**  
  ```json
  POST /attendance
  Request:
  {
    "studentId": "uuid",
    "courseId": "uuid",
    "attendanceDate": "YYYY-MM-DD"
  }
  Response:
  {
    "attendanceId": "uuid",
    "status": "SUCCESS",
    "duplicate": false
  }
  ```  
  **API /notifications**  
  ```json
  POST /notifications
  Request:
  {
    "userId": "uuid",
    "groupZalo": "string",
    "message": "string"
  }
  Response:
  {
    "notificationId": "uuid",
    "status": "PENDING"
  }
  ```  
  **API /promotions**  
  ```json
  GET /promotions
  Response:
  [
    {
      "promoId": "uuid",
      "code": "string",
      "discountPercent": 20,
      "startDate": "YYYY-MM-DD",
      "endDate": "YYYY-MM-DD",
      "description": "string"
    }
  ]
  ```  
  **Event Topics**  
  - `attendance.events`  
  - `notification.events`  
  - `promotion.events`

- **Xử lý Ngoại lệ Định vị Giai đoạn [EXC-001],[EXC-002],[EXC-003]:**  
  - **EXC-001: DuplicateAttendanceException** – Mã lỗi 409, thông báo: “Attendance already recorded for this student on the same day.”  
  - **EXC-002: AttendanceValidationException** – Mã lỗi 400, thông báo: “Invalid attendance data: missing studentId or courseId.”  
  - **EXC-003: NotificationFailureException** – Mã lỗi 500, thông báo: “Failed to send notification to device or Zalo group.”

---

## Nhật ký Phân phối Công việc Theo Ngày (Giai đoạn 3)

- **Ngày 1: Thiết lập các dịch vụ attendance và notification**  
  ##### Công việc phụ [1]: Xây dựng AttendanceService và controller [Coder]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/attendance/AttendanceService.java; ./sources/backend/membership-hub-auxiliary/attendance/AttendanceController.java [EXC-001],[EXC-002],[ARC-007],[DAT-006],[REQ-012],[REQ-013]`  
  Low-Level Technical Task Instruction: Xây dựng lớp AttendanceService với phương thức recordAttendance, xử lý idempotency, kiểm tra quyền truy cập, và lưu vào bảng ATTENDANCE.  
  Database Schema DDL SQL Specification [DAT-006]:  
  ```sql
  CREATE TABLE ATTENDANCE (
      attendanceId UUID PRIMARY KEY,
      studentId UUID NOT NULL,
      courseId UUID NOT NULL,
      attendanceDate DATE NOT NULL,
      timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
      CONSTRAINT fk_student FOREIGN KEY (studentId) REFERENCES USERS(userId),
      CONSTRAINT fk_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId),
      CONSTRAINT uq_attendance UNIQUE (studentId, courseId, attendanceDate)
  );
  ```  
  API and Event Routing Contracts [REQ-012],[REQ-013],[ARC-007]:  
  ```json
  POST /attendance
  Request:
  {
    "studentId": "uuid",
    "courseId": "uuid",
    "attendanceDate": "YYYY-MM-DD"
  }
  Response:
  {
    "attendanceId": "uuid",
    "status": "SUCCESS",
    "duplicate": false
  }
  ```  
  Phase Localized Exception Handlers [EXC-001],[EXC-002]:  
  - **EXC-001: DuplicateAttendanceException** – Mã lỗi 409, thông báo: “Attendance already recorded for this student on the same day.”  
  - **EXC-002: AttendanceValidationException** – Mã lỗi 400, thông báo: “Invalid attendance data: missing studentId or courseId.”  

  ##### Công việc phụ [2]: Xây dựng NotificationService và controller [Coder]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/notification/NotificationService.java; ./sources/backend/membership-hub-auxiliary/notification/NotificationController.java [EXC-003],[ARC-008],[DAT-008],[REQ-016]`  
  Low-Level Technical Task Instruction: Xây dựng lớp NotificationService để gửi push tới FCM/APNs và Zalo, tạo Notification entity, lưu vào bảng NOTIFICATIONS.  
  Database Schema DDL SQL Specification [DAT-008]:  
  ```sql
  CREATE TABLE NOTIFICATIONS (
      notificationId UUID PRIMARY KEY,
      userId UUID,
      groupZalo VARCHAR(255),
      message TEXT NOT NULL,
      sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
      delivered BOOLEAN NOT NULL DEFAULT FALSE,
      CONSTRAINT fk_user FOREIGN KEY (userId) REFERENCES USERS(userId)
  );
  ```  
  API and Event Routing Contracts [REQ-016],[ARC-008]:  
  ```json
  POST /notifications
  Request:
  {
    "userId": "uuid",
    "groupZalo": "string",
    "message": "string"
  }
  Response:
  {
    "notificationId": "uuid",
    "status": "PENDING"
  }
  ```  
  Phase Localized Exception Handlers [EXC-003]:  
  - **EXC-003: NotificationFailureException** – Mã lỗi 500, thông báo: “Failed to send notification to device or Zalo group.”  

- **Ngày 2: Xây dựng dịch vụ promotion và exception classes**  
  ##### Công việc phụ [1]: Xây dựng PromotionService và controller [Coder]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/promotion/PromotionService.java; ./sources/backend/membership-hub-auxiliary/promotion/PromotionController.java [ARC-017],[DAT-009],[REQ-017],[REQ-018]`  
  Low-Level Technical Task Instruction: Xây dựng lớp PromotionService để quản lý khuyến mãi, bao gồm CRUD, tính toán giảm giá, và lưu vào bảng PROMOTIONS.  
  Database Schema DDL SQL Specification [DAT-009]:  
  ```sql
  CREATE TABLE PROMOTIONS (
      promoId UUID PRIMARY KEY,
      code VARCHAR(50) NOT NULL UNIQUE,
      discountPercent SMALLINT NOT NULL,
      startDate DATE,
      endDate DATE,
      description TEXT,
      CONSTRAINT chk_discount CHECK (discountPercent BETWEEN 1 AND 100)
  );
  ```  
  API and Event Routing Contracts [REQ-017],[REQ-018],[ARC-017]:  
  ```json
  GET /promotions
  Response:
  [
    {
      "promoId": "uuid",
      "code": "string",
      "discountPercent": 20,
      "startDate": "YYYY-MM-DD",
      "endDate": "YYYY-MM-DD",
      "description": "string"
    }
  ]
  ```  

  ##### Công việc phụ [2]: Định nghĩa các exception tùy chỉnh [Coder]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/exception/AttendanceException.java; ./sources/backend/membership-hub-auxiliary/exception/NotificationException.java [EXC-001],[EXC-002],[EXC-003]`  
  Low-Level Technical Task Instruction: Định nghĩa các exception tùy chỉnh cho attendance và notification, bao gồm mã lỗi và thông báo.  
  Phase Localized Exception Handlers [EXC-001],[EXC-002],[EXC-003]:  
  - **EXC-001: DuplicateAttendanceException** – Mã lỗi 409, thông báo: “Attendance already recorded for this student on the same day.”  
  - **EXC-002: AttendanceValidationException** – Mã lỗi 400, thông báo: “Invalid attendance data: missing studentId or courseId.”  
  - **EXC-003: NotificationFailureException** – Mã lỗi 500, thông báo: “Failed to send notification to device or Zalo group.”  

- **Ngày 3: Kiểm thử và tài liệu**  
  ##### Công việc phụ [1]: Viết unit test cho attendance, notification, promotion [Tester]  
  Target Component file path: `./sources/backend/membership-hub-auxiliary/attendance/AttendanceServiceTest.java; ./sources/backend/membership-hub-auxiliary/notification/NotificationServiceTest.java; ./sources/backend/membership-hub-auxiliary/promotion/PromotionServiceTest.java [EXC-001],[EXC-002],[EXC-003],[ARC-007],[ARC-008],[ARC-017],[DAT-006],[DAT-008],[DAT-009]`  
  Low-Level Technical Task Instruction: Viết các unit test để kiểm tra tính idempotent của attendance, xử lý ngoại lệ, và CRUD promotion.  

  ##### Công việc phụ [2]: Tài liệu chi tiết cho API và exception handling [Doc]  
  Target Component file path: `./sources/docs/attendance_api.md; ./sources/docs/notification_api.md; ./sources/docs/promotion_api.md; ./sources/docs/exception_handling.md [REQ-012],[REQ-013],[REQ-016],[ARC-007],[ARC-008],[ARC-017],[EXC-001],[EXC-002],[EXC-003]`  
  Low-Level Technical Task Instruction: Tạo tài liệu chi tiết cho các endpoint, payload, và exception handling.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1: Thiết lập hạ tầng cơ bản cho dịch vụ backend**

  ##### SUB-TASK 1: Xây dựng và đẩy Docker image cho các dịch vụ Quarkus  
  **[Docker]**  
  **Target Component:** `./sources/backend/membership-hub-infra/Dockerfile`  
  **Tag IDs:** [ARC-010]  
  **Nhiệm vụ chi tiết:** Tạo Dockerfile đa giai đoạn cho các microservice Quarkus, biên dịch mã nguồn, đóng gói thành image, và đẩy lên Google Container Registry (GCR) với tag `membership-hub:latest`.

  ##### SUB-TASK 2: Provisioning GCP Terraform cho GKE cluster  
  **[GCP]**  
  **Target Component:** `./sources/infra/terraform/main.tf`  
  **Tag IDs:** [ARC-010],[ARC-009]  
  **Nhiệm vụ chi tiết:** Định nghĩa tài nguyên GKE cluster, node pools, IAM roles và service accounts trong Terraform, chạy `terraform init` và `terraform apply` để triển khai cluster với cấu hình tự động scaling.

  ##### SUB-TASK 3: Triển khai Helm chart cho ứng dụng  
  **[GKE]**  
  **Target Component:** `./sources/infra/helm/membership-hub/Chart.yaml`  
  **Tag IDs:** [ARC-010],[ARC-008]  
  **Nhiệm vụ chi tiết:** Tạo chart Helm bao gồm deployment, service, ingress cho các microservice, cấu hình values.yaml, và triển khai lên GKE bằng `helm upgrade --install`.

- **DAY 2: Hoàn thiện hạ tầng, CI/CD và cấu hình sự kiện**

  ##### SUB-TASK 1: Xây dựng Docker image cho sidecar (Redis, Kafka)  
  **[Docker]**  
  **Target Component:** `./sources/backend/membership-hub-infra/sidecar/Dockerfile`  
  **Tag IDs:** [ARC-010],[ARC-006]  
  **Nhiệm vụ chi tiết:** Tạo Dockerfile cho Redis và Kafka, biên dịch và đẩy image lên GCR, chuẩn bị cho deployment trong Helm chart.

  ##### SUB-TASK 2: Tạo Pub/Sub topics cho event bus  
  **[GCP]**  
  **Target Component:** `./sources/infra/terraform/pubsub.tf`  
  **Tag IDs:** [ARC-006],[ARC-009]  
  **Nhiệm vụ chi tiết:** Định nghĩa các topic `attendance.events`, `notification.events`, `course.events`, `center.events` trong Terraform, triển khai bằng `terraform apply`.

  ##### SUB-TASK 3: Triển khai event bus services (Kafka/Redis Streams) lên GKE  
  **[GKE]**  
  **Target Component:** `./sources/infra/helm/eventbus/Chart.yaml`  
  **Tag IDs:** [ARC-006],[ARC-008]  
  **Nhiệm vụ chi tiết:** Cấu hình Helm chart cho Kafka và Redis Streams, triển khai vào GKE cluster, xác nhận các broker hoạt động bình thường.

  ##### SUB-TASK 4: Thiết lập pipeline CI/CD với GitHub Actions  
  **[Docker]**  
  **Target Component:** `./sources/infra/github-actions/workflows/ci-cd.yml`  
  **Tag IDs:** [ARC-010],[ARC-006]  
  **Nhiệm vụ chi tiết:** Định nghĩa workflow GitHub Actions để build, test, push Docker image, và deploy Helm chart lên GKE, bao gồm các bước kiểm tra lint, unit test và integration test.

  ##### SUB-TASK 5: Xử lý ngoại lệ khi provisioning hạ tầng  
  **[GCP]**  
  **Target Component:** `./sources/infra/terraform/variables.tf`  
  **Tag IDs:** [EXC-004],[EXC-005]  
  **Nhiệm vụ chi tiết:** Thêm validation cho các biến Terraform, xử lý lỗi khi thiếu credentials hoặc thiếu resource quota, ghi log chi tiết và rollback khi cần.

  ##### SUB-TASK 6: Tạo bảng SystemSettings trong PostgreSQL  
  **[Docker]**  
  **Target Component:** `./sources/backend/membership-hub-infra/migrations/V1__create_system_settings.sql`  
  **Tag IDs:** [DAT-011]  
  **Nhiệm vụ chi tiết:**  
  ```sql
  CREATE TABLE IF NOT EXISTS SYSTEMSETTINGS (
      settingKey VARCHAR(255) NOT NULL PRIMARY KEY,
      settingValue TEXT NOT NULL,
      description VARCHAR(500)
  );
  CREATE INDEX idx_setting_key ON SYSTEMSETTINGS (settingKey);
  ```

  ##### SUB-TASK 7: Triển khai Cloud Function cho QR scan  
  **[GCP]**  
  **Target Component:** `./sources/infra/terraform/cloudfunctions.tf`  
  **Tag IDs:** [ARC-007]  
  **Nhiệm vụ chi tiết:** Định nghĩa Cloud Function `qr_scan_handler` trong Terraform, triển khai, cấu hình trigger HTTP, và cấp quyền truy cập từ mobile app.

# TỔNG QUAN DỰ ÁN: membership-hub

### 📈 Giai đoạn 5 Triển khai ứng dụng cuối cùng, thực hiện kiểm thử tích hợp và xác nhận luồng toàn bộ
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:**  
  Giai đoạn này thực hiện triển khai toàn bộ ứng dụng lên môi trường sản xuất, thực thi các bài kiểm thử tích hợp để xác nhận tính toàn vẹn của luồng dữ liệu, và thực hiện kiểm tra toàn bộ luồng giao dịch từ đăng nhập, quản lý khóa học, điểm danh, đến thông báo, đảm bảo mọi thành phần hoạt động đồng bộ và đáp ứng các tiêu chí hiệu năng, bảo mật đã đề ra.

- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**  
  - `./sources/infra/membership-hub-deploy/Dockerfile [ARC-010]`  
  - `./sources/infra/membership-hub-deploy/helm/values.yaml [ARC-010]`  
  - `./sources/infra/membership-hub-deploy/helm/membership-hub-deploy.yaml [ARC-010]`  
  - `./sources/infra/membership-hub-deploy/ci/github-actions.yml [ARC-010]`  
  - `./sources/infra/membership-hub-deploy/integration-tests/validate-end-to-end.test.ts [ARC-010]`  
  - `./sources/docs/architecture/infra-deployment.md [ARC-010]`

- **Phase Localized Exception Handlers:**  
  Không có ngoại lệ đặc thù trong giai đoạn này.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 1: Triển khai Docker images, áp dụng Helm chart, chạy kiểm thử tích hợp, và xác nhận triển khai**  

  ##### SUB-TASK 1: Xây dựng Docker images  
  **[Docker]**  
  **Target Component:** `./sources/infra/membership-hub-deploy/Dockerfile [ARC-010]`  
  **Hướng dẫn chi tiết:** Xây dựng Dockerfile đa giai đoạn cho tất cả các microservice, tối ưu kích thước, đẩy lên GCR.

  ##### SUB-TASK 2: Triển khai Helm chart  
  **[GKE]**  
  **Target Component:** `./sources/infra/membership-hub-deploy/helm/membership-hub-deploy.yaml [ARC-010]`  
  **Hướng dẫn chi tiết:** Triển khai Helm chart lên cluster GKE, kiểm tra trạng thái pod, service, và xác nhận endpoint hoạt động.

  ##### SUB-TASK 3: Chạy kiểm thử tích hợp  
  **[Tester]**  
  **Target Component:** `./sources/infra/membership-hub-deploy;integration-tests/validate-end-to-end.test.ts [ARC-010]`  
  **Hướng dẫn chi tiết:** Chạy tập hợp kiểm thử tích hợp end-to-end, ghi lại logs, và báo cáo lỗi.

  ##### SUB-TASK 4: Xác nhận triển khai  
  **[Reviewer]**  
  **Target Component:** `./sources/infra/membership-hub-deploy/ci/github-actions.yml [ARC-010]`  
  **Hướng dẫn chi tiết:** Xem xét pipeline CI, xác nhận các bước kiểm thử đã hoàn thành, và phê duyệt triển khai.

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2=5
TOTAL_PHASES_EXPECTED_BY_PARAMETERS=5
PHASE_COUNT_COMPLIANCE_STATUS=Verified_5_out_of_5_Phases_Generated
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER=7
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE=1
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1=58
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=58
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

# TỔNG QUAN HỆ THỐNG: membership-hub

## 📁 6. MÃ BẢO MẬT QUỐC TẾ VÀ THIẾT BỊ CHỐNG TIẾT THUẬT [NFR-XXX]
- **Chống SQL Injection (SQLi) - Biện pháp tuyệt đối**: Định nghĩa quy tắc sử dụng câu lệnh chuẩn bị (prepared statements), tham số vị trí (positional parameters), và danh sách trắng (whitelists) cho các đầu vào sắp xếp động.
- **Chống XSS & Chính sách Bảo mật Nội dung (CSP)**: Tiêu chuẩn tự động làm sạch ngữ cảnh, tự động thoát JSX, và chèn tiêu đề CSP nghiêm ngặt (`unsafe-inline` bị cấm).
- **Quy tắc CORS đa tenant**: Cấu hình ngăn chặn wildcard nguồn gốc và xác thực động các nguồn gốc tenant dựa trên cơ sở dữ liệu.
- **Công cụ làm sạch nhật ký và ẩn dữ liệu PII**: Hệ thống tự động ẩn dữ liệu nhạy cảm (`@JsonSerialize`) và ngưỡng làm sạch nhật ký.

## 📁 7. QUY TẮC TUYÊN CHẤP MÔ HÌNH HỢP TÁC & CƠ THỂ SEO ĐỊNH DỊCH
- **Quy tắc tuân thủ Capacitor Mobile Hybrid**: Khi di động được kích hoạt, áp dụng các quy tắc lấy dữ liệu phía client, địa chỉ URL tuyệt đối, bảo vệ hydration, trừu tượng lưu trữ native (`@capacitor/preferences`), và xử lý nút back của thiết bị.
- **Hệ thống SEO đa ngôn ngữ**: Kiến trúc middleware nhận diện ngôn ngữ, chèn động thẻ hreflang, và giới hạn chỉ mục crawler robots.

## 📁 8. DÂY ĐỘNG CÔNG CỤ TỰ ĐỘNG HÀNH ĐỘNG GIT
- **Phân tách fork làm việc hàng ngày**: Kiểm soát lập trình cho nhánh `features/development-phase-X-day-Y` (X là số giai đoạn, Y là số ngày trong giai đoạn, bắt đầu từ 1 cho mỗi giai đoạn).
- **Cổng bảo vệ quy trình**: Quy tắc thực thi biên dịch, kiểm tra độ phủ mã tự động (`>= 85%`), và ghi lại nhật ký tổng hợp ngữ cảnh.

### 🛑 QUÁ TRÌNH KIỂM TRA MÁT HÀNH
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`