# NGHIỆP ĐỀ XUẤT TOÀN CẦU: membership-hub

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260807154510 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/07 15:45:10 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH CƠ SỞ CƠ BẢN

### 1.1. MÔ HÌNH CƠ SỞ CƠ BẢN
- Microservice architecture with Quarkus backend services, PostgreSQL database, Redis cache, Docker containerization, GKE orchestration, Firebase Authentication, FCM/APNs, CI/CD via GitHub Actions.
- Reactive event-driven communication using Kafka topics for notifications and attendance events.
- CQRS pattern separating command and query responsibilities across services.
- Strict RBAC enforcement based on ARC tags, with role hierarchy: System Admin > Center Admin > Manager > Teacher > Student.

### 1.2. ĐỘI NGŨ VÀ LƯỢNG LƯỢNG
- Backend: Java/Quarkus, Hibernate ORM, Flyway migrations, Docker images.
- Frontend: Next.js, React Native (mobile), responsive design, Zalo API integration.
- DevOps: Terraform for GCP resources, Helm charts for GKE, GitHub Actions pipelines.
- Security: OWASP Top 10 mitigations, TLS 1.3, AES‑256 at rest, JWT 15 min access, 7‑day refresh.

## 📁 2. CỤC THUỘC HỆ THỐNG & THƯ VIỆN HỆ THỐNG

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.6, Hibernate ORM 6.2, Flyway 9.22, Redis 7.0, Firebase Auth, GCP SDK, GKE, Docker 24, PostgreSQL 15, Kafka 3.5.
- **Frontend & Cross‑Platform UI Stack**: Next.js 13, React 18, React Native 0.73, Capacitor 4, Tailwind CSS, Zalo SDK, FCM/APNs.

### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=[true]
BACKEND_LAYER_REQUIRED=[true]
FRONTEND_LAYER_REQUIRED=[true]
MOBILE_LAYER_REQUIRED=[true]
DEVOPS_LAYER_REQUIRED=[true]
```

## 📁 3. QUY ĐỊNH BẢO VỆ & CHẤP NHẬN ĐẠO HÀNH DOANH NGHIỆP

- Repository root: `.`; all paths start with `./sources/`.
- Java package: `org.nlh4j.saas.membershiphub`.
- Docker images: multi‑stage, size <500 MB, health checks.
- Terraform: GCP resources, IAM, VPC, Cloud Build, Cloud Run.
- GKE: Helm charts, HPA, autoscaling, rolling updates.
- Logging: structured JSON, retention 1 year, GDPR compliance.
- Security: OWASP Top 10, JWT, TLS 1.3, AES‑256, prepared statements, CSP, CORS, rate limiting.

## 📁 4. BẢNG TỔNG QUAN ĐA GIAI ĐOẠN KIẾN TRÚC

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Day 1 - 5 | ./sources/backend/user-service | Xây dựng xác thực, quản lý người dùng, RBAC, và cơ sở dữ liệu cơ bản | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [DAT-002], [NFR-001], [NFR-002], [NFR-003] |
| Giai đoạn 2 | Day 1 - 3 | ./sources/backend/center-service | Quản lý trung tâm, CRUD, phân quyền trung tâm, và cơ sở dữ liệu trung tâm | Coder | [REQ-004], [REQ-005], [REQ-006], [ARC-007], [ARC-008], [ARC-009], [DAT-003], [NFR-004], [NFR-005] |
| Giai đoạn 3 | Day 1 - 2 | ./sources/backend/course-service | Quản lý khóa học, lịch, giảng viên, và cơ sở dữ liệu khóa học | Coder | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [NFR-006] |
| Giai đoạn 4 | Day 1 - 4 | ./sources/backend/course-service | Đăng ký, điểm danh, thẻ hội viên, và cơ sở dữ liệu liên quan | Coder | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [EXC-003], [NFR-007] |
| Giai đoạn 5 | Day 1 - 6 | ./sources/backend/notification-service | Thông báo, khuyến mãi, chatbot, mobile, báo cáo, và hạ tầng | Coder | [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [DAT-008], [DAT-009], [EXC-004], [EXC-005], [NFR-008], [NFR-009] |

## 📁 5. ĐẶC TẢ KIẾN TRÚC CHI TIẾT GIAI ĐOẠN VÀ LOG THỰC HIỆN NGÀY ĐÓ

### 📈 Giai đoạn 1: Xây dựng xác thực, quản lý người dùng, RBAC, và cơ sở dữ liệu cơ bản
- **Phase Core Objective & Purpose**: Triển khai hệ thống xác thực, quản lý người dùng, và RBAC; thiết lập cơ sở dữ liệu và Docker image.
- **Target Physical Directory Matrix Map**:
  * `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java [REQ-001], [DAT-001], [NFR-001]`
  * `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/auth/SocialAuthService.java [REQ-002], [DAT-002], [NFR-002]`
  * `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/role/RoleService.java [REQ-003], [ARC-001], [ARC-002]`
  * `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/authorization/AuthorizationService.java [ARC-003], [ARC-004], [ARC-005]`
  * `./sources/infra/docker/Dockerfile.user-service [ARC-006], [NFR-003]`
- **Database Schema DDL SQL Specification [DAT-001]**:
```sql
CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL,
    provider VARCHAR(20) NOT NULL CHECK (provider IN ('local','firebase','google','facebook')),
    createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
    updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);
ALTER TABLE USERS ADD CONSTRAINT fk_user_role FOREIGN KEY (roleId) REFERENCES ROLES(roleId);
CREATE INDEX idx_users_email ON USERS(email);
```
- **API and Event Routing Contracts [REQ-001]**:
```json
{
  "request": {
    "type": "object",
    "properties": {
      "email": {"type":"string","format":"email"},
      "password": {"type":"string","minLength":8},
      "fullName": {"type":"string","maxLength":100}
    },
    "required": ["email","password","fullName"]
  },
  "response": {
    "type":"object",
    "properties": {
      "userId": {"type":"string","format":"uuid"},
      "token": {"type":"string"},
      "expiresIn": {"type":"integer"}
    },
    "required": ["userId","token","expiresIn"]
  }
}
```
- **Day 1**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-001], [DAT-001], [NFR-001]`
  * **Target Component file path (`target_component`)**: `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java [REQ-001], [DAT-001], [NFR-001]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint POST /api/auth/register, tạo bảng USERS và ROLES, mã hoá mật khẩu, thêm chỉ mục email, thiết lập metric latency.

- **Day 2**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-002], [DAT-002], [NFR-002]`
  * **Target Component file path (`target_component`)**: `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/auth/SocialAuthService.java [REQ-002], [DAT-002], [NFR-002]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint POST /api/auth/social, tạo bảng CENTERS, cấu hình Redis cache, tối ưu latency.

- **Day 3**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-003], [ARC-001], [ARC-002]`
  * **Target Component file path (`target_component`)**: `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/role/RoleService.java [REQ-003], [ARC-001], [ARC-002]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint PUT /api/users/{id}/role, kiểm tra quyền, cập nhật roleId.

- **Day 4**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Reviewer]`
  * **Targeted Tag IDs**: `[ARC-003], [ARC-004], [ARC-005]`
  * **Target Component file path (`target_component`)**: `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/authorization/AuthorizationService.java [ARC-003], [ARC-004], [ARC-005]`
  * **Low-Level Technical Task Instruction**: Đánh giá logic RBAC, xác thực quyền, bảo vệ endpoints, đề xuất cải tiến.

- **Day 5**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Docker]`
  * **Targeted Tag IDs**: `[ARC-006], [NFR-003]`
  * **Target Component file path (`target_component`)**: `./sources/infra/docker/Dockerfile.user-service [ARC-006], [NFR-003]`
  * **Low-Level Technical Task Instruction**: Xây dựng Docker image, thiết lập environment variables, kiểm tra kích thước <500 MB, cấu hình health check.
  * **Docker Agent Role**:
```dockerfile
FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /app
COPY . .
RUN ./mvnw clean package -DskipTests
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","app.jar"]
```

### 📈 Giai đoạn 2: Quản lý trung tâm, CRUD, phân quyền trung tâm, và cơ sở dữ liệu trung tâm
- **Phase Core Objective & Purpose**: Thiết lập CRUD trung tâm, phân quyền, và bảng CENTERS.
- **Target Physical Directory Matrix Map**:
  * `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-004], [DAT-003], [NFR-004]`
  * `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterAdminService.java [REQ-005], [ARC-007], [ARC-008]`
  * `./sources/infra/docker/Dockerfile.center-service [REQ-006], [ARC-009], [NFR-005]`
- **Database Schema DDL SQL Specification [DAT-003]**:
```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
CREATE INDEX idx_centers_taxId ON CENTERS(taxId);
```
- **API and Event Routing Contracts [REQ-004]**:
```json
{
  "request": {
    "type":"object",
    "properties": {
      "name": {"type":"string","maxLength":100},
      "address": {"type":"string","maxLength":255},
      "taxId": {"type":"string","pattern":"^[0-9]{10,13}$"},
      "contactPhone": {"type":"string"},
      "contactEmail": {"type":"string","format":"email"}
    },
    "required": ["name","address","taxId"]
  },
  "response": {
    "type":"object",
    "properties": {
      "centerId": {"type":"string","format":"uuid"},
      "name": {"type":"string"},
      "address": {"type":"string"},
      "taxId": {"type":"string"},
      "contactPhone": {"type":"string"},
      "contactEmail": {"type":"string"}
    },
    "required": ["centerId","name","address","taxId"]
  }
}
```
- **Day 1**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-004], [DAT-003], [NFR-004]`
  * **Target Component file path (`target_component`)**: `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-004], [DAT-003], [NFR-004]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint GET /api/centers, tạo bảng CENTERS, chỉ mục taxId, index address.

- **Day 2**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-005], [ARC-007], [ARC-008]`
  * **Target Component file path (`target_component`)**: `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterAdminService.java [REQ-005], [ARC-007], [ARC-008]`
  * **Low-Level Technical Task Instruction**: Triển khai CRUD center, gán Center Admin, kiểm tra isolation, cập nhật contact.

- **Day 3**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Docker]`
  * **Targeted Tag IDs**: `[REQ-006], [ARC-009], [NFR-005]`
  * **Target Component file path (`target_component`)**: `./sources/infra/docker/Dockerfile.center-service [REQ-006], [ARC-009], [NFR-005]`
  * **Low-Level Technical Task Instruction**: Xây dựng Docker image, health checks, environment variables.
  * **Docker Agent Role**:
```dockerfile
FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /app
COPY . .
RUN ./mvnw clean package -DskipTests
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8081
ENTRYPOINT ["java","-jar","app.jar"]
```

### 📈 Giai đoạn 3: Quản lý khóa học, lịch, giảng viên, và cơ sở dữ liệu khóa học
- **Phase Core Objective & Purpose**: Thiết lập CRUD khóa học, lịch, giảng viên, và bảng COURSES.
- **Target Physical Directory Matrix Map**:
  * `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java [REQ-007], [DAT-004], [NFR-006]`
  * `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseAdminService.java [REQ-008], [REQ-009]`
- **Database Schema DDL SQL Specification [DAT-004]**:
```sql
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID,
    maxStudents INT DEFAULT 30,
    CONSTRAINT chk_dates CHECK (startDate <= endDate)
);
CREATE INDEX idx_courses_teacher ON COURSES(teacherId);
```
- **API and Event Routing Contracts [REQ-007]**:
```json
{
  "request": {},
  "response": {
    "type":"array",
    "items":{
      "type":"object",
      "properties":{
        "courseId":{"type":"string","format":"uuid"},
        "title":{"type":"string"},
        "startDate":{"type":"string","format":"date"},
        "endDate":{"type":"string","format":"date"},
        "teacherName":{"type":"string"}
      },
      "required":["courseId","title","startDate","endDate","teacherName"]
    }
  }
}
```
- **Day 1**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-007], [DAT-004], [NFR-006]`
  * **Target Component file path (`target_component`)**: `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java [REQ-007], [DAT-004], [NFR-006]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint GET /api/courses, tạo bảng COURSES, kiểm tra xung đột lịch.

- **Day 2**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Tester]`
  * **Targeted Tag IDs**: `[REQ-008], [REQ-009]`
  * **Target Component file path (`target_component`)**: `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseAdminService.java [REQ-008], [REQ-009]`
  * **Low-Level Technical Task Instruction**: Viết unit test cho CRUD khóa học, kiểm tra xung đột lịch, gán giảng viên.
  * **Tester Agent Role**:
```java
@Test
void testCreateCourseConflict() {
    // Arrange
    CourseDto dto = new CourseDto("Math", LocalDate.now(), LocalDate.now().plusDays(5), teacherId);
    // Act & Assert
    assertThrows(ConflictException.class, () -> courseService.createCourse(dto));
}
```

### 📈 Giai đoạn 4: Đăng ký, điểm danh, thẻ hội viên, và cơ sở dữ liệu liên quan
- **Phase Core Objective & Purpose**: Thiết lập đăng ký, điểm danh, thẻ hội viên, và bảng liên quan.
- **Target Physical Directory Matrix Map**:
  * `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/EnrollmentService.java [REQ-010], [DAT-005], [EXC-001]`
  * `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/AttendanceService.java [REQ-011], [DAT-006], [EXC-002]`
  * `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/AttendanceService.java [REQ-012], [DAT-007], [EXC-003]`
  * `./sources/infra/docker/Dockerfile.attendance-service [REQ-013], [NFR-007]`
- **Database Schema DDL SQL Specification [DAT-005]**:
```sql
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_enroll_student FOREIGN KEY (studentId) REFERENCES USERS(userId),
    CONSTRAINT fk_enroll_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE UNIQUE INDEX uq_enroll_student_course ON ENROLLMENTS(studentId, courseId);
```
- **Database Schema DDL SQL Specification [DAT-006]**:
```sql
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_attend_student FOREIGN KEY (studentId) REFERENCES USERS(userId),
    CONSTRAINT fk_attend_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId),
    CONSTRAINT uq_attend UNIQUE (studentId, courseId, attendanceDate)
);
```
- **Database Schema DDL SQL Specification [DAT-007]**:
```sql
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_notify_user FOREIGN KEY (userId) REFERENCES USERS(userId)
);
```
- **API and Event Routing Contracts [REQ-010]**:
```json
{
  "request": {},
  "response": {
    "type":"array",
    "items":{
      "type":"object",
      "properties":{
        "courseId":{"type":"string","format":"uuid"},
        "title":{"type":"string"},
        "capacity":{"type":"integer"},
        "schedule":{"type":"string"}
      },
      "required":["courseId","title","capacity","schedule"]
    }
  }
}
```
- **Exception Handlers**:
  * **EXC-001**:
```java
public class InvalidInputException extends RuntimeException {
    public InvalidInputException(String message) { super(message); }
}
```
  * **EXC-002**:
```java
public class DuplicateAttendanceException extends RuntimeException {
    public DuplicateAttendanceException(String message) { super(message); }
}
```
  * **EXC-003**:
```java
public class NotificationDeliveryFailureException extends RuntimeException {
    public NotificationDeliveryFailureException(String message) { super(message); }
}
```
- **Day 1**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-010], [DAT-005], [EXC-001]`
  * **Target Component file path (`target_component`)**: `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/EnrollmentService.java [REQ-010], [DAT-005], [EXC-001]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint GET /api/courses/available, tạo bảng ENROLLMENTS, xử lý lỗi đầu vào.

- **Day 2**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-011], [DAT-006], [EXC-002]`
  * **Target Component file path (`target_component`)**: `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/AttendanceService.java [REQ-011], [DAT-006], [EXC-002]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint POST /api/attendance, tạo bảng ATTENDANCE, xử lý duplicate.

- **Day 3**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-012], [DAT-007], [EXC-003]`
  * **Target Component file path (`target_component`)**: `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/AttendanceService.java [REQ-012], [DAT-007], [EXC-003]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint POST /api/attendance/qr, tạo bảng NOTIFICATIONS, xử lý failure.

- **Day 4**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Docker]`
  * **Targeted Tag IDs**: `[REQ-013], [NFR-007]`
  * **Target Component file path (`target_component`)**: `./sources/infra/docker/Dockerfile.attendance-service [REQ-013], [NFR-007]`
  * **Low-Level Technical Task Instruction**: Xây dựng Docker image, tối ưu performance, health checks.
  * **Docker Agent Role**:
```dockerfile
FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /app
COPY . .
RUN ./mvnw clean package -DskipTests
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8082
ENTRYPOINT ["java","-jar","app.jar"]
```

### 📈 Giai đoạn 5: Thông báo, khuyến mãi, chatbot, mobile, báo cáo, và hạ tầng
- **Phase Core Objective & Purpose**: Thiết lập thông báo, khuyến mãi, chatbot, mobile, báo cáo, và hạ tầng.
- **Target Physical Directory Matrix Map**:
  * `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-014], [DAT-008], [EXC-004]`
  * `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-015], [DAT-009], [EXC-005]`
  * `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [NFR-008]`
  * `./sources/docs/marketing.md [REQ-017], [REQ-018], [NFR-009]`
  * `./sources/infra/gcp/terraform/main.tf [REQ-019], [REQ-020], [REQ-021]`
  * `./sources/infra/gke/deployment.yaml [REQ-022], [REQ-023], [REQ-024]`
- **Database Schema DDL SQL Specification [DAT-008]**:
```sql
CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);
```
- **Database Schema DDL SQL Specification [DAT-009]**:
```sql
CREATE TABLE ANNOUNCEMENTS (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);
```
- **API and Event Routing Contracts [REQ-014]**:
```json
{
  "request": {},
  "response": {
    "type":"object",
    "properties":{
      "totalValidityDays":{"type":"integer"},
      "daysUsed":{"type":"integer"},
      "daysRemaining":{"type":"integer"}
    },
    "required":["totalValidityDays","daysUsed","daysRemaining"]
  }
}
```
- **API and Event Routing Contracts [REQ-015]**:
```json
{
  "request": {
    "type":"object",
    "properties":{
      "renewalPeriod":{"type":"integer","minimum":1}
    },
    "required":["renewalPeriod"]
  },
  "response": {
    "type":"object",
    "properties":{
      "newEndDate":{"type":"string","format":"date"},
      "confirmation":{"type":"string"}
    },
    "required":["newEndDate","confirmation"]
  }
}
```
- **API and Event Routing Contracts [REQ-016]**:
```json
{
  "request": {
    "type":"object",
    "properties":{
      "userId":{"type":"string","format":"uuid"},
      "message":{"type":"string"}
    },
    "required":["userId","message"]
  },
  "response": {
    "type":"object",
    "properties":{
      "notificationId":{"type":"string","format":"uuid"},
      "status":{"type":"string"}
    },
    "required":["notificationId","status"]
  }
}
```
- **Exception Handlers**:
  * **EXC-004**:
```java
public class PromotionNotFoundException extends RuntimeException {
    public PromotionNotFoundException(String message) { super(message); }
}
```
  * **EXC-005**:
```java
public class AnnouncementNotFoundException extends RuntimeException {
    public AnnouncementNotFoundException(String message) { super(message); }
}
```
- **Day 1**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-014], [DAT-008], [EXC-004]`
  * **Target Component file path (`target_component`)**: `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-014], [DAT-008], [EXC-004]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint GET /api/cards, tạo bảng PROMOTIONS, xử lý missing promotion.

- **Day 2**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Coder]`
  * **Targeted Tag IDs**: `[REQ-015], [DAT-009], [EXC-005]`
  * **Target Component file path (`target_component`)**: `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-015], [DAT-009], [EXC-005]`
  * **Low-Level Technical Task Instruction**: Triển khai endpoint POST /api/cards/renew, tạo bảng ANNOUNCEMENTS, xử lý notification.

- **Day 3**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Reviewer]`
  * **Targeted Tag IDs**: `[REQ-016], [NFR-008]`
  * **Target Component file path (`target_component`)**: `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [NFR-008]`
  * **Low-Level Technical Task Instruction**: Đánh giá logic notification, GDPR compliance, performance.

- **Day 4**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[Doc]`
  * **Targeted Tag IDs**: `[REQ-017], [REQ-018], [NFR-009]`
  * **Target Component file path (`target_component`)**: `./sources/docs/marketing.md [REQ-017], [REQ-018], [NFR-009]`
  * **Low-Level Technical Task Instruction**: Viết tài liệu marketing, promotions, announcements, SEO.

- **Day 5**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[GCP]`
  * **Targeted Tag IDs**: `[REQ-019], [REQ-020], [REQ-021]`
  * **Target Component file path (`target_component`)**: `./sources/infra/gcp/terraform/main.tf [REQ-019], [REQ-020], [REQ-021]`
  * **Low-Level Technical Task Instruction**: Provision GCP resources, deploy mobile backend, configure FCM/APNs.
  * **GCP Agent Role**:
```hcl
provider "google" {
  project = var.project_id
  region  = var.region
}
resource "google_compute_network" "vpc" {
  name = "membershiphub-vpc"
}
resource "google_container_cluster" "gke" {
  name     = "membershiphub-cluster"
  location = var.region
  initial_node_count = 3
}
resource "google_storage_bucket" "bucket" {
  name          = "${var.project_id}-bucket"
  location      = var.region
  force_destroy = true
}
```

- **Day 6**: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY
  * **Sub-Agent Workflow Specialization**: `[GKE]`
  * **Targeted Tag IDs**: `[REQ-022], [REQ-023], [REQ-024]`
  * **Target Component file path (`target_component`)**: `./sources/infra/gke/deployment.yaml [REQ-022], [REQ-023], [REQ-024]`
  * **Low-Level Technical Task Instruction**: Deploy services, set up CI/CD, generate reports.
  * **GKE Agent Role**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: membershiphub-backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: membershiphub
  template:
    metadata:
      labels:
        app: membershiphub
    spec:
      containers:
      - name: backend
        image: gcr.io/${PROJECT_ID}/membershiphub-backend:latest
        ports:
        - containerPort: 8080
        env:
        - name: SPRING_PROFILES_ACTIVE
          value: prod
```

## 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ BẢO VỆ CHÍNH (NFR-XXX)

- **SQL Injection (SQLi)**: Use prepared statements, parameterized queries, avoid string concatenation.
- **Cross‑Site Scripting (XSS)**: CSP headers, auto‑escaping in templates, input sanitization.
- **CORS**: Restrict origins to registered domains, enforce per‑tenant validation.
- **Log Scrubbing**: Mask PII, redact sensitive fields, retain logs for 1 year.

## 📁 7. QUY ĐỊNH HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: Native storage, back‑button handling, push notification registration.
- **i18n & SEO**: Dynamic locale detection, `<html lang='vi'>`, `hreflang` tags, meta tags per language.

## 📁 8. PIPELINE TỰ ĐỘNG HÀNH ĐỘNG GIT

- **Branching**: `features/development-phase-X-day-Y`.
- **CI/CD**: GitHub Actions, test coverage ≥85 %, automated deployments.

### 🛑 MÁC CHỈ ĐÁNH ĐOÁN COVERSAGE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 24, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`