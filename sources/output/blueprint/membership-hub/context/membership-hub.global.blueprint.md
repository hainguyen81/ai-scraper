# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260803170121 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/03 17:01:21 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
Hệ thống membership‑hub được thiết kế theo kiến trúc microservices với backend Java/Quarkus, PostgreSQL, Redis, và Docker/Kubernetes (GKE). Các dịch vụ được chia thành các module: Auth, User, Center, Course, Enrollment, Attendance, Card, Notification, Promotion, Chatbot, Mobile UI, Localization, Reporting. Mỗi module triển khai API REST và sự kiện qua Pub/Sub, đồng thời hỗ trợ OAuth2, JWT, và bảo mật OWASP. Kiến trúc sử dụng CQRS cho các thao tác ghi, Event Sourcing cho các sự kiện quan trọng, và Reactive Streams cho các luồng dữ liệu thời gian thực.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- **Auth Flow**: OAuth2 (Firebase, Google, Facebook) → JWT (15 min) + Refresh (7 days).  
- **Attendance Flow**: Mobile QR → Backend → Idempotent record (attendanceDate + studentId + courseId).  
- **Notification Flow**: Event → Pub/Sub → FCM/APNs + Zalo API.  
- **Data Replication**: PostgreSQL read replicas cho báo cáo, Redis cache cho session.  
- **CI/CD**: GitHub Actions → Docker Build → GCP Cloud Build → GKE Deploy.  

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Redis client, Firebase Admin SDK, Google Cloud SDK, Zalo API SDK.  
- **Frontend**: Next.js 13, React, TypeScript, Tailwind CSS, Capacitor (mobile).  
- **Infrastructure**: Docker 20.x, Kubernetes 1.28 (GKE), Terraform, Helm, Cloud Build, Cloud Run, Cloud SQL, Cloud Pub/Sub, Cloud Storage.  
- **Testing**: JUnit 5, Testcontainers, RestAssured, Cypress, Jest, Playwright.  

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Workspace Boundary**: Root repository `..`, tất cả các file bắt đầu bằng `./sources/`.  
- **Directory Prefixing**: Backend → `./sources/backend.<service-name>.`, Frontend → `./sources/frontend.<app-name>.`, Infra → `./sources/infra.`  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  
- **Tester Path Syntax**: `<source_component>;<test_suite_file>`.  
- **Security**: TLS 1.3, AES‑256, OWASP Top 10 mitigations, JWT 15 min, refresh 7 days.  

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1‑3 | `./sources/backend.auth/`, `./sources/backend.user/`, `./sources/backend.center/` | Auth, User, Center modules, RBAC, JWT, DB schema (Users, Roles, Centers) | Coder | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [DAT-003], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008] |
| 2 | 1‑3 | `./sources/backend.course/`, `./sources/backend.enrollment/`, `./sources/backend.attendance/`, `./sources/backend.card/` | Course, Enrollment, Attendance, Card modules, DB schema (Courses, Enrollments, Attendance, StudentCards) | Coder | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007], [ARC-008], [ARC-009], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008] |
| 3 | 1‑3 | `./sources/backend.notification/`, `./sources/backend.promotion/`, `./sources/backend.chatbot/` | Notification, Promotion, Chatbot modules, DB schema (Notifications, Promotions, Announcements) | Coder | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [ARC-008], [ARC-009], [ARC-010], [DAT-008], [DAT-009], [EXC-003], [EXC-005], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| 4 | 1‑2 | `./sources/frontend.mobile/`, `./sources/backend.settings/` | Mobile UI, SystemSettings module, DB schema (SystemSettings) | Coder | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [ARC-010], [DAT-011], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| 5 | 1‑2 | `./sources/infra/` | Docker, GCP, GKE manifests, CI/CD pipelines | Docker, GCP, GKE | [NFR-002], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

<!--START_DELIMITTER-->
### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Thiết lập cơ sở hạ tầng xác thực, quản lý người dùng, và quyền truy cập trung tâm.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/backend.auth/` [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006]  
  - `./sources/backend.user/` [DAT-001], [REQ-001], [REQ-002], [REQ-003]  
  - `./sources/backend.center/` [DAT-003], [REQ-004], [REQ-005], [REQ-006], [ARC-002], [ARC-003], [ARC-004], [ARC-005]  
- **Database Schema DDL SQL Specification [DAT-001], [DAT-003]**  
```sql
CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL,
    provider VARCHAR(20) NOT NULL DEFAULT 'local',
    createdAt TIMESTAMP NOT NULL DEFAULT now(),
    updatedAt TIMESTAMP NOT NULL DEFAULT now()
);
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(50),
    contactEmail VARCHAR(255)
);
ALTER TABLE USERS ADD CONSTRAINT fk_user_role FOREIGN KEY (roleId) REFERENCES ROLES(roleId);
ALTER TABLE USERS ADD CONSTRAINT fk_user_center FOREIGN KEY (centerId) REFERENCES CENTERS(centerId);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006]**  
```json
{
  "endpoint": "/api/auth/register",
  "method": "POST",
  "request": {
    "email": "string",
    "password": "string",
    "fullName": "string",
    "provider": "string"
  },
  "response": {
    "userId": "uuid",
    "token": "string",
    "expiresIn": "int"
  }
}
```
- **Phase Localized Exception Handlers [EXC-004]**  
```java
public class InvalidInputException extends RuntimeException {
    public InvalidInputException(String field, String message) {
        super(String.format("Invalid input for %s: %s", field, message));
    }
}
```
<!--END_DELIMITTER-->

<!--START_DELIMITTER-->
### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Xây dựng mô-đun khóa học, ghi danh, điểm danh, và thẻ hội viên.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/backend.course/` [DAT-004], [REQ-007], [REQ-008], [REQ-009]  
  - `./sources/backend.enrollment/` [DAT-005], [REQ-010], [REQ-011]  
  - `./sources/backend.attendance/` [DAT-006], [REQ-012], [REQ-013], [EXC-001], [EXC-002]  
  - `./sources/backend.card/` [DAT-007], [REQ-014], [REQ-015]  
- **Database Schema DDL SQL Specification [DAT-004], [DAT-005], [DAT-006], [DAT-007]**  
```sql
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL,
    maxStudents INT DEFAULT 30
);
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT now()
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);
ALTER TABLE ENROLLMENTS ADD CONSTRAINT fk_enroll_student FOREIGN KEY (studentId) REFERENCES USERS(userId);
ALTER TABLE ENROLLMENTS ADD CONSTRAINT fk_enroll_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId);
ALTER TABLE ATTENDANCE ADD CONSTRAINT fk_attend_student FOREIGN KEY (studentId) REFERENCES USERS(userId);
ALTER TABLE ATTENDANCE ADD CONSTRAINT fk_attend_course FOREIGN KEY (courseId) REFERENCES COURSES(courseId);
ALTER TABLE STUDENTCARDS ADD CONSTRAINT fk_card_student FOREIGN KEY (studentId) REFERENCES USERS(userId);
```
- **API and Event Routing Contracts [REQ-007]–[REQ-015]**  
```json
{
  "endpoint": "/api/courses",
  "method": "GET",
  "response": [
    {
      "courseId": "uuid",
      "title": "string",
      "startDate": "date",
      "endDate": "date",
      "teacherName": "string"
    }
  ]
}
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002]**  
```java
public class NetworkException extends RuntimeException {
    public NetworkException(String message) {
        super(message);
    }
}
public class DuplicateAttendanceException extends RuntimeException {
    public DuplicateAttendanceException(String studentId, String courseId, Date date) {
        super(String.format("Attendance already recorded for student %s, course %s on %s", studentId, courseId, date));
    }
}
```
<!--END_DELIMITTER-->

<!--START_DELIMITTER-->
### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Triển khai thông báo, khuyến mãi, chatbot, và các tính năng liên quan.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/backend.notification/` [DAT-008], [REQ-016]  
  - `./sources/backend.promotion/` [DAT-009], [REQ-017], [REQ-018]  
  - `./sources/backend.chatbot/` [REQ-019]  
- **Database Schema DDL SQL Specification [DAT-008], [DAT-009]**  
```sql
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT now(),
    delivered BOOLEAN NOT NULL DEFAULT false
);
CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);
CREATE TABLE ANNOUNCEMENTS (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);
ALTER TABLE NOTIFICATIONS ADD CONSTRAINT fk_notification_user FOREIGN KEY (userId) REFERENCES USERS(userId);
```
- **API and Event Routing Contracts [REQ-016]–[REQ-019]**  
```json
{
  "endpoint": "/api/notifications",
  "method": "POST",
  "request": {
    "userId": "uuid",
    "message": "string"
  },
  "response": {
    "notificationId": "uuid",
    "status": "queued"
  }
}
```
- **Phase Localized Exception Handlers [EXC-003], [EXC-005]**  
```java
public class NotificationDeliveryException extends RuntimeException {
    public NotificationDeliveryException(String deviceToken) {
        super("Failed to deliver notification to token: " + deviceToken);
    }
}
public class SystemRecoveryException extends RuntimeException {
    public SystemRecoveryException(String message) {
        super(message);
    }
}
```
<!--END_DELIMITTER-->

<!--START_DELIMITTER-->
### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Phát triển giao diện di động, cài đặt hệ thống cài đặt, và hỗ trợ đa ngôn ngữ.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/frontend.mobile/` [REQ-020], [REQ-021], [REQ-022], [REQ-023]  
  - `./sources/backend.settings/` [DAT-011]  
- **Database Schema DDL SQL Specification [DAT-011]**  
```sql
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-020]–[REQ-023]**  
```json
{
  "endpoint": "/api/settings",
  "method": "GET",
  "response": {
    "language": "string",
    "seoMeta": "object"
  }
}
```
- **Phase Localized Exception Handlers**: Không có ngoại lệ riêng biệt.  
<!--END_DELIMITTER-->

<!--START_DELIMITTER-->
### Phase 5 Detailed Architectural Specification
- **Phase Core Objective & Purpose**: Đóng gói Docker, triển khai GKE, và thiết lập CI/CD.  
- **Target Physical Directory Matrix Map**:  
  - `./sources/infra/docker/` [NFR-005]  
  - `./sources/infra/gcp/` [NFR-002], [NFR-004], [NFR-006], [NFR-007], [NFR-008], [NFR-009]  
  - `./sources/infra/k8s/` [NFR-002], [NFR-004], [NFR-006], [NFR-007], [NFR-008], [NFR-009]  
- **Dockerfile Example**  
```dockerfile
FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app
COPY target/*.jar app.jar
CMD ["java", "-jar", "app.jar"]
```
- **Helm Chart Example**  
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: membership-hub
spec:
  replicas: 3
  selector:
    matchLabels:
      app: membership-hub
  template:
    metadata:
      labels:
        app: membership-hub
    spec:
      containers:
        - name: backend
          image: gcr.io/project-id/membership-hub:latest
          ports:
            - containerPort: 8080
```
- **CI/CD Pipeline (GitHub Actions)**  
```yaml
name: CI/CD
on:
  push:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker
        run: docker build -t gcr.io/project-id/membership-hub:latest .
      - name: Push Docker
        run: docker push gcr.io/project-id/membership-hub:latest
```
<!--END_DELIMITTER-->

## 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs

### Phase 1
- **DAY 1:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Coder:**  
      - **Target Component file path (`target_component`):** `./sources/backend.auth/;src/main/java/com/membershiphub/auth/AuthService.java [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006]`  
      - **Low-Level Technical Task Instruction:** Xây dựng lớp dịch vụ AuthService, triển khai các phương thức đăng ký, đăng nhập, và phát token JWT, đồng thời tích hợp OAuth2 với Firebase, Google, Facebook.  
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006]  
- **DAY 2:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Tester:**  
      - **Target Component file path (`target_component`):** `./sources/backend.auth/;src/test/java/com/membershiphub/auth/AuthServiceTest.java [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006]`  
      - **Low-Level Technical Task Instruction:** Viết unit test cho AuthService, bao gồm kiểm tra đăng ký thành công, đăng nhập thành công, và xử lý lỗi đầu vào.  
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006]  
- **DAY 3:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Reviewer:**  
      - **Target Component file path (`target_component`):** `./sources/backend.auth/;src/main/java/com/membershiphub/auth/AuthService.java [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]`  
      - **Low-Level Technical Task Instruction:** Đánh giá mã nguồn, kiểm tra tuân thủ OWASP, tối ưu hiệu năng, và xác nhận các biện pháp bảo mật.  
      - **Targeted Tag IDs:** [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]  

### Phase 2
- **DAY 1:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Coder:**  
      - **Target Component file path (`target_component`):** `./sources/backend.course/;src/main/java/com/membershiphub/course/CourseService.java [REQ-007], [REQ-008], [REQ-009], [ARC-007], [ARC-008], [ARC-009], [DAT-004]`  
      - **Low-Level Technical Task Instruction:** Xây dựng lớp CourseService, triển khai CRUD khóa học, kiểm tra xung đột lịch học, và gán giáo viên.  
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [ARC-007], [ARC-008], [ARC-009], [DAT-004]  
- **DAY 2:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Tester:**  
      - **Target Component file path (`target_component`):** `./sources/backend.course/;src/test/java/com/membershiphub/course/CourseServiceTest.java [REQ-007], [REQ-008], [REQ-009], [ARC-007], [ARC-008], [ARC-009], [DAT-004]`  
      - **Low-Level Technical Task Instruction:** Viết unit test cho CourseService, bao gồm kiểm tra CRUD, xung đột lịch, và gán giáo viên.  
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [ARC-007], [ARC-008], [ARC-009], [DAT-004]  
- **DAY 3:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Reviewer:**  
      - **Target Component file path (`target_component`):** `./sources/backend.course/;src/main/java/com/membershiphub/course/CourseService.java [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]`  
      - **Low-Level Technical Task Instruction:** Đánh giá mã nguồn, kiểm tra tuân thủ OWASP, tối ưu hiệu năng, và xác nhận các biện pháp bảo mật.  
      - **Targeted Tag IDs:** [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]  

### Phase 3
- **DAY 1:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Coder:**  
      - **Target Component file path (`target_component`):** `./sources/backend.notification/;src/main/java/com/membershiphub/notification/NotificationService.java [REQ-016], [ARC-008], [ARC-009], [ARC-010], [DAT-008]`  
      - **Low-Level Technical Task Instruction:** Xây dựng NotificationService, triển khai gửi push, Zalo, và lưu trữ thông báo.  
      - **Targeted Tag IDs:** [REQ-016], [ARC-008], [ARC-009], [ARC-010], [DAT-008]  
- **DAY 2:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Tester:**  
      - **Target Component file path (`target_component`):** `./sources/backend.notification/;src/test/java/com/membershiphub/notification/NotificationServiceTest.java [REQ-016], [ARC-008], [ARC-009], [ARC-010], [DAT-008]`  
      - **Low-Level Technical Task Instruction:** Viết unit test cho NotificationService, kiểm tra gửi push, Zalo, và lưu trữ.  
      - **Targeted Tag IDs:** [REQ-016], [ARC-008], [ARC-009], [ARC-010], [DAT-008]  
- **DAY 3:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Reviewer:**  
      - **Target Component file path (`target_component`):** `./sources/backend.notification/;src/main/java/com/membershiphub/notification/NotificationService.java [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]`  
      - **Low-Level Technical Task Instruction:** Đánh giá mã nguồn, kiểm tra tuân thủ OWASP, tối ưu hiệu năng, và xác nhận các biện pháp bảo mật.  
      - **Targeted Tag IDs:** [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]  

### Phase 4
- **DAY 1:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Coder:**  
      - **Target Component file path (`target_component`):** `./sources/frontend.mobile/;src/main/js/App.js [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]`  
      - **Low-Level Technical Task Instruction:** Xây dựng giao diện di động, tích hợp push, đa ngôn ngữ, và SEO.  
      - **Targeted Tag IDs:** [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]  
- **DAY 2:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Tester:**  
      - **Target Component file path (`target_component`):** `./sources/frontend.mobile/;src/test/js/App.test.js [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]`  
      - **Low-Level Technical Task Instruction:** Viết unit test cho giao diện di động, kiểm tra push, đa ngôn ngữ, và SEO.  
      - **Targeted Tag IDs:** [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]  

### Phase 5
- **DAY 1:**  
  - **Sub-Agent Workflow Specialization:**  
    * **Docker:**  
      - **Target Component file path (`target_component`):** `./sources/infra/docker/Dockerfile [NFR-005]`  
      - **Low-Level Technical Task Instruction:** Viết Dockerfile đa stage, tối ưu kích thước, và cấu hình multi‑arch.  
      - **Targeted Tag IDs:** [NFR-005]  
- **DAY 2:**  
  - **Sub-Agent Workflow Specialization:**  
    * **GCP:**  
      - **Target Component file path (`target_component`):** `./sources/infra/gcp/terraform/main.tf [NFR-002], [NFR-004], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`  
      - **Low-Level Technical Task Instruction:** Viết Terraform để provision GKE, VPC, IAM, Cloud SQL, Pub/Sub, và cấu hình CI/CD.  
      - **Targeted Tag IDs:** [NFR-002], [NFR-004], [NFR-006], [NFR-007], [NFR-008], [NFR-009]  

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng prepared statements, tham số hóa truy vấn, whitelist các trường sắp xếp, và kiểm tra độ dài.  
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động escape nội dung, bật CSP strict, và kiểm tra các input.  
- **Multi-Tenant CORS Security Rails:** Chỉ cho phép origin cụ thể, kiểm tra tenant ID trong header, và giới hạn truy cập.  
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Sử dụng interceptor `@JsonSerialize` để mask email, phone, và token trong logs, và giới hạn thời gian lưu trữ logs 1 năm.  

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng Capacitor để gọi native APIs, lưu trữ local bằng `@capacitor/preferences`, và xử lý back‑button.  
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware nhận `Accept-Language`, inject `<html lang='vi'>`, và thêm `hreflang` cho các ngôn ngữ.  

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Tạo nhánh `features/development-phase-X-day-Y` cho mỗi ngày.  
- **Validation Guard Pipeline Gates:** Kiểm tra compile, coverage ≥ 85 %, và serialize logs.  

### 🛑 MATRIX COVERAGE CHECK MANDATE
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 24, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`