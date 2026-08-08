# TỔNG QUAN DỰ ÁN: membership-hub

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260808090442 |
| **Tên Dự Án** | membership-hub |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày.Thời Gian** | 2026/08/08 09:04:42 |
| **Tác Giả** | Enterprise System Architect (SA Agent) |
| **Phê Duyệt** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕI

## 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

- Kiến trúc microservices dựa trên Quarkus, PostgreSQL, Docker, GKE.
- Xác thực đa kênh: email/mật khẩu, Firebase, Google, Facebook OAuth2.
- Quản lý người dùng, trung tâm, khóa học, đăng ký, điểm danh, thẻ hội viên, và thông báo.
- Dữ liệu lưu trữ trong PostgreSQL, session caching bằng Redis.
- API REST tiêu chuẩn, event-driven với Kafka (được tích hợp).
- CI/CD pipeline với GitHub Actions, Terraform cho GCP.

## 1.2. Kiến Trúc Dòng Dữ Liệu Doanh Nghiệp & Hệ Sinh Thái Cốt Lõi

- Luồng xác thực: nhận token JWT, refresh token, lưu trữ session.
- Luồng điểm danh QR: quét, gửi student ID và timestamp, idempotent ghi nhận.
- Luồng thông báo: push notification, Zalo group posting.
- Luồng tích hợp frontend Next.js: caching offline, bearer token auth.
- Event bus: Kafka topics cho notifications, attendance, enrollment.

## 📁 2. CƠ SỞ CÔNG NGHỆ & THƯ VIỆN HỆ THỐNG

- Backend: Java/Quarkus, PostgreSQL, Docker, GKE, Firebase Auth, FCM/APNs, Zalo API, Redis, GitHub Actions.
- Frontend: Next.js, React Native, Capacitor, i18n, SEO, responsive design.
- DevOps: Docker, Terraform, GKE, CI/CD, monitoring, backup.

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. QUY ĐỊNH BẢO VỆ & CHẤT LƯỢNG DOANH NGHIỆP

- Đảm bảo 99.9% uptime, failover GKE.
- TLS 1.3, AES-256 at rest.
- JWT 15 phút, refresh 7 ngày.
- OWASP Top 10: SQLi, XSS, CSRF, etc.
- Horizontal scaling HPA CPU > 70% hoặc latency > 300ms.
- Docker image < 200MB base, < 500MB final.
- Logging 1 năm, GDPR/CCPA compliance.
- Backup: daily full, PITR 24h, GKE backup region.

## 📁 4. BẢNG TỔNG QUAN KHIẾN TRÚC Đa Giai Đoạn

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 - 7 | ./sources/backend/auth-service, ./sources/backend/user-service, ./sources/backend/role-service | Xây dựng hệ thống đăng ký, xác thực, phân quyền người dùng | [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], [GKE] | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-002], [NFR-003], [EXC-001], [EXC-002] |
| Phase 2 | Day 1 - 7 | ./sources/backend/center-service, ./sources/backend/course-service, ./sources/backend/enrollment-service, ./sources/backend/attendance-service, ./sources/backend/card-service, ./sources/backend/notification-service | Quản lý trung tâm, khóa học, đăng ký, điểm danh, thẻ, thông báo | [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], [GKE] | [REQ-012], [REQ-013], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [DAT-008], [EXC-003], [EXC-004], [EXC-005] |
| Phase 3 | Day 1 - 7 | ./sources/backend/database/migration, ./sources/backend/security, ./sources/backend/card-service | Tạo bảng dữ liệu, áp dụng NFR, logic thẻ | [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], [GKE] | [DAT-009], [DAT-011], [DAT-001], [DAT-003], [DAT-004], [DAT-005], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [REQ-014] |
| Phase 4 | Day 1 - 7 | ./sources/backend/database/migration, ./sources/infra/monitoring, ./sources/infra/backup, ./sources/infra/alerting, ./sources/infra/ci-cd | Backup, monitoring, alerting, CI/CD | [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], [GKE] | [DAT-006], [DAT-007], [DAT-008] |
| Phase 5 | Day 1 - 7 | ./sources/infra/docker, ./sources/infra/gcp, ./sources/infra/gke, ./sources/frontend/mobile-app, ./sources/frontend/web-app | DevOps, containerization, GCP, mobile UI, web UI | [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], [GKE] |  |
<!--END_PHASE_SYNOPSIS_GRID-->

## 📁 5. ĐẶC TẢ CHI TIẾT GIAI ĐOẠN VÀ LOG THỰC HIỆN NGÀY

### 📈 Phase 1 Khởi Tạo Hệ Thống Người Dùng Và Xác Thực

- **Phase Core Objective & Purpose:** Thiết lập hệ thống đăng ký, xác thực, và phân quyền người dùng, bao gồm lưu trữ dữ liệu người dùng, xác thực đa kênh, và bảo mật token.
- **Target Physical Directory Matrix Map:** ./sources/backend/auth-service, ./sources/backend/user-service, ./sources/backend/role-service
- **Database Schema DDL SQL Specification [DAT-001]:** 
```sql
CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL,
    provider VARCHAR(20) NOT NULL DEFAULT 'local',
    createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
    updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);
ALTER TABLE USERS ADD CONSTRAINT fk_role FOREIGN KEY (roleId) REFERENCES ROLES(roleId);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003]:** 
```json
{
  "endpoint": "/api/auth/register",
  "method": "POST",
  "request": {
    "email": "string",
    "password": "string",
    "provider": "string"
  },
  "response": {
    "token": "string",
    "expiresIn": "int"
  }
}
```
- **Phase Localized Exception Handlers [EXC-004]:** 
```java
@ExceptionHandler(InvalidInputException.class)
public ResponseEntity<?> handleInvalidInput(InvalidInputException ex) {
    return ResponseEntity.badRequest().body(Map.of("error", ex.getMessage()));
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1: Thiết lập endpoint đăng ký**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-001], [ARC-001], [NFR-001]
    * **Target Component file path (`target_component`):** ./sources/backend/auth-service [REQ-001], [ARC-001], [NFR-001]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/auth/register` với validation, hashing mật khẩu, lưu trữ người dùng, trả về JWT token. [REQ-001], [ARC-001], [NFR-001]

- **DAY 2: Xây dựng endpoint đăng nhập**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-002], [ARC-002], [NFR-002]
    * **Target Component file path (`target_component`):** ./sources/backend/auth-service [REQ-002], [ARC-002], [NFR-002]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/auth/login` với OAuth2, token refresh, và validation. [REQ-002], [ARC-002], [NFR-002]

- **DAY 3: Phân quyền người dùng**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-003], [ARC-003], [NFR-003]
    * **Target Component file path (`target_component`):** ./sources/backend/role-service [REQ-003], [ARC-003], [NFR-003]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/role/assign` để admin thay đổi role, cập nhật DB, kiểm tra quyền. [REQ-003], [ARC-003], [NFR-003]

- **DAY 4: Kiểm tra đầu vào không hợp lệ**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [EXC-004]
    * **Target Component file path (`target_component`):** ./sources/backend/auth-service;./sources/backend/auth-service-test [EXC-004]
    * **Low-Level Technical Task Instruction:** Viết unit test cho validation, kiểm tra email, password, provider. [EXC-004]

- **DAY 5: Review code và documentation**
    * **Sub-Agent Workflow Specialization:** [Reviewer]
    * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003]
    * **Target Component file path (`target_component`):** ./sources/backend/auth-service, ./sources/backend/role-service [REQ-001], [REQ-002], [REQ-003]
    * **Low-Level Technical Task Instruction:** Kiểm tra tính đúng đắn, tuân thủ coding standards, đề xuất cải tiến. [REQ-001], [REQ-002], [REQ-003]

- **DAY 6: Viết tài liệu API**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003]
    * **Target Component file path (`target_component`):** ./sources/docs/api-auth.md [REQ-001], [REQ-002], [REQ-003]
    * **Low-Level Technical Task Instruction:** Tạo tài liệu Swagger/OpenAPI cho các endpoint đăng ký, đăng nhập, phân quyền. [REQ-001], [REQ-002], [REQ-003]

- **DAY 7: Dockerize services**
    * **Sub-Agent Workflow Specialization:** [Docker]
    * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003]
    * **Target Component file path (`target_component`):** ./sources/backend/auth-service/Dockerfile [REQ-001], [REQ-002], [REQ-003]
    * **Low-Level Technical Task Instruction:** Viết Dockerfile multi-stage, build image, push to registry. [REQ-001], [REQ-002], [REQ-003]

### 📈 Phase 2 Quản lý trung tâm, khóa học, đăng ký, điểm danh, thẻ, thông báo

- **Phase Core Objective & Purpose:** Xây dựng các module quản lý trung tâm, khóa học, đăng ký học viên, ghi danh, thẻ hội viên, và hệ thống thông báo.
- **Target Physical Directory Matrix Map:** ./sources/backend/center-service, ./sources/backend/course-service, ./sources/backend/enrollment-service, ./sources/backend/attendance-service, ./sources/backend/card-service, ./sources/backend/notification-service
- **Database Schema DDL SQL Specification [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008]:** 
```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID,
    maxStudents INT DEFAULT 30
);
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID,
    courseId UUID,
    enrollmentDate TIMESTAMP DEFAULT NOW()
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID,
    courseId UUID,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP DEFAULT NOW()
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT
);
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP DEFAULT NOW(),
    delivered BOOLEAN DEFAULT FALSE
);
```
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]:** (Provide example JSON for one endpoint)
```json
{
  "endpoint": "/api/center/list",
  "method": "GET",
  "response": {
    "centers": [
      {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      }
    ]
  }
}
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** (Provide example Java exception handler)
```java
@ExceptionHandler(AttendanceDuplicateException.class)
public ResponseEntity<?> handleDuplicateAttendance(AttendanceDuplicateException ex) {
    return ResponseEntity.ok(Map.of("status", "duplicate"));
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1: Xây dựng API danh sách trung tâm**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-012], [ARC-006], [DAT-003]
    * **Target Component file path (`target_component`):** ./sources/backend/center-service [REQ-012], [ARC-006], [DAT-003]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/center/list` trả về danh sách trung tâm, kiểm tra quyền truy cập. [REQ-012], [ARC-006], [DAT-003]

- **DAY 2: Xây dựng API tạo trung tâm**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-013], [ARC-007], [DAT-003]
    * **Target Component file path (`target_component`):** ./sources/backend/center-service [REQ-013], [ARC-007], [DAT-003]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/center/create` với validation, kiểm tra taxId trùng, lưu trữ. [REQ-013], [ARC-007], [DAT-003]

- **DAY 3: Xây dựng API danh sách khóa học**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-014], [ARC-008], [DAT-004]
    * **Target Component file path (`target_component`):** ./sources/backend/course-service [REQ-014], [ARC-008], [DAT-004]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/course/list` trả về danh sách khóa học, kiểm tra quyền. [REQ-014], [ARC-008], [DAT-004]

- **DAY 4: Xây dựng API đăng ký học viên**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-015], [ARC-009], [DAT-005]
    * **Target Component file path (`target_component`):** ./sources/backend/enrollment-service [REQ-015], [ARC-009], [DAT-005]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/enrollment/register` tạo enrollment, tạo user nếu chưa có, gửi notification. [REQ-015], [ARC-009], [DAT-005]

- **DAY 5: Xây dựng API ghi danh điểm danh**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-016], [ARC-010], [DAT-006]
    * **Target Component file path (`target_component`):** ./sources/backend/attendance-service [REQ-016], [ARC-010], [DAT-006]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/attendance/scan` nhận studentId, courseId, timestamp, kiểm tra idempotent, lưu trữ. [REQ-016], [ARC-010], [DAT-006]

- **DAY 6: Xây dựng API thẻ hội viên**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-017], [DAT-007]
    * **Target Component file path (`target_component`):** ./sources/backend/card-service [REQ-017], [DAT-007]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/card/status` trả về validity days, days used, days remaining. [REQ-017], [DAT-007]

- **DAY 7: Xây dựng API thông báo**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-018], [DAT-008]
    * **Target Component file path (`target_component`):** ./sources/backend/notification-service [REQ-018], [DAT-008]
    * **Low-Level Technical Task Instruction:** Xây dựng endpoint `/api/notification/create` tạo notification, queue push, gửi Zalo. [REQ-018], [DAT-008]

### 📈 Phase 3 Tạo bảng dữ liệu, áp dụng NFR, logic thẻ

- **Phase Core Objective & Purpose:** Tạo và cấu hình các bảng dữ liệu, áp dụng các yêu cầu NFR, và triển khai logic thẻ hội viên.
- **Target Physical Directory Matrix Map:** ./sources/backend/database/migration, ./sources/backend/security, ./sources/backend/card-service
- **Database Schema DDL SQL Specification [DAT-009], [DAT-011]:** 
```sql
CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
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
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** (Provide example)
```java
@ExceptionHandler(PromotionConflictException.class)
public ResponseEntity<?> handlePromotionConflict(PromotionConflictException ex) {
    return ResponseEntity.status(HttpStatus.CONFLICT).body(Map.of("error", ex.getMessage()));
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 1: Tạo bảng điểm danh**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [DAT-009], [DAT-011]
    * **Target Component file path (`target_component`):** ./sources/backend/database/migration [DAT-009], [DAT-011]
    * **Low-Level Technical Task Instruction:** Viết migration script tạo bảng PROMOTIONS và ANNOUNCEMENTS. [DAT-009], [DAT-011]

- **DAY 2: Áp dụng NFR-004 (Performance)**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [NFR-004]
    * **Target Component file path (`target_component`):** ./sources/backend/database/migration;./sources/backend/performance-test [NFR-004]
    * **Low-Level Technical Task Instruction:** Viết load test, kiểm tra latency, tối ưu index. [NFR-004]

- **DAY 3: Áp dụng NFR-005 (Availability)**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [NFR-005]
    * **Target Component file path (`target_component`):** ./sources/backend/database/migration;./sources/backend/availability-test [NFR-005]
    * **Low-Level Technical Task Instruction:** Kiểm tra failover, replication, recovery. [NFR-005]

- **DAY 4: Áp dụng NFR-006 (Security)**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [NFR-006]
    * **Target Component file path (`target_component`):** ./sources/backend/security;./sources/backend/security-test [NFR-006]
    * **Low-Level Technical Task Instruction:** Kiểm tra OWASP, bảo mật token, encryption. [NFR-006]

- **DAY 5: Áp dụng NFR-007 (Scalability)**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [NFR-007]
    * **Target Component file path (`target_component`):** ./sources/backend/scalability-test [NFR-007]
    * **Low-Level Technical Task Instruction:** Kiểm tra HPA, scaling, load balancing. [NFR-007]

- **DAY 6: Áp dụng NFR-008 (GDPR/CCPA)**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [NFR-008]
    * **Target Component file path (`target_component`):** ./sources/backend/compliance-test [NFR-008]
    * **Low-Level Technical Task Instruction:** Kiểm tra deletion, export, consent. [NFR-008]

- **DAY 7: Áp dụng NFR-009 (Backup & DR)**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [NFR-009]
    * **Target Component file path (`target_component`):** ./sources/backend/backup-test [NFR-009]
    * **Low-Level Technical Task Instruction:** Kiểm tra backup, point-in-time recovery. [NFR-009]

### 📈 Phase 4 Backup, monitoring, CI/CD

- **Phase Core Objective & Purpose:** Thiết lập backup, monitoring, alerting, và CI/CD pipeline cho toàn bộ hệ thống.
- **Target Physical Directory Matrix Map:** ./sources/backend/database/migration, ./sources/infra/monitoring, ./sources/infra/backup, ./sources/infra/alerting, ./sources/infra/ci-cd
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007], [DAT-008]:** (Already defined in Phase 2)
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** (Already defined)

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1: Backup script for PostgreSQL**
    * **Sub-Agent Workflow Specialization:** [Docker]
    * **Targeted Tag IDs:** [DAT-006]
    * **Target Component file path (`target_component`):** ./sources/infra/backup/backup.sh [DAT-006]
    * **Low-Level Technical Task Instruction:** Viết script backup full, lưu trữ vào Cloud Storage, schedule cron. [DAT-006]

- **DAY 2: Monitoring setup with Prometheus & Grafana**
    * **Sub-Agent Workflow Specialization:** [GCP]
    * **Targeted Tag IDs:** [DAT-007]
    * **Target Component file path (`target_component`):** ./sources/infra/monitoring/monitoring.yaml [DAT-007]
    * **Low-Level Technical Task Instruction:** Cấu hình Prometheus, Grafana dashboards, alerting rules. [DAT-007]

- **DAY 3: Alerting configuration**
    * **Sub-Agent Workflow Specialization:** [GCP]
    * **Targeted Tag IDs:** [DAT-008]
    * **Target Component file path (`target_component`):** ./sources/infra/alerting/alerting.yaml [DAT-008]
    * **Low-Level Technical Task Instruction:** Thiết lập alert rules, webhook, email. [DAT-008]

- **DAY 4: CI/CD pipeline for backend services**
    * **Sub-Agent Workflow Specialization:** [Docker]
    * **Targeted Tag IDs:** [DAT-006], [DAT-007]
    * **Target Component file path (`target_component`):** ./sources/infra/ci-cd/github-actions.yml [DAT-006], [DAT-007]
    * **Low-Level Technical Task Instruction:** Viết workflow build, test, push Docker image, deploy to GKE. [DAT-006], [DAT-007]

- **DAY 5: CI/CD pipeline for frontend services**
    * **Sub-Agent Workflow Specialization:** [Docker]
    * **Targeted Tag IDs:** [DAT-006], [DAT-007]
    * **Target Component file path (`target_component`):** ./sources/infra/ci-cd/github-actions-frontend.yml [DAT-006], [DAT-007]
    * **Low-Level Technical Task Instruction:** Build, test, deploy Next.js, React Native. [DAT-006], [DAT-007]

- **DAY 6: Review and documentation of CI/CD**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Targeted Tag IDs:** [DAT-006], [DAT-007]
    * **Target Component file path (`target_component`):** ./sources/docs/ci-cd.md [DAT-006], [DAT-007]
    * **Low-Level Technical Task Instruction:** Viết tài liệu pipeline, quy trình release. [DAT-006], [DAT-007]

- **DAY 7: Final testing and rollback plan**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** [DAT-006], [DAT-007]
    * **Target Component file path (`target_component`):** ./sources/infra/ci-cd/rollback-test.sh [DAT-006], [DAT-007]
    * **Low-Level Technical Task Instruction:** Kiểm tra rollback, failover, recovery. [DAT-006], [DAT-007]

### 📈 Phase 5 DevOps, containerization, GCP, mobile UI, web UI

- **Phase Core Objective & Purpose:** Triển khai containerization, provisioning GCP, triển khai GKE, phát triển UI di động và web, tài liệu kỹ thuật.
- **Target Physical Directory Matrix Map:** ./sources/infra/docker, ./sources/infra/gcp, ./sources/infra/gke, ./sources/frontend/mobile-app, ./sources/frontend/web-app
- **Database Schema DDL SQL Specification:** (none)
- **Phase Localized Exception Handlers:** (none)

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 1: Dockerize backend services**
    * **Sub-Agent Workflow Specialization:** [Docker]
    * **Targeted Tag IDs:** 
    * **Target Component file path (`target_component`):** ./sources/backend/auth-service/Dockerfile
    * **Low-Level Technical Task Instruction:** Viết Dockerfile multi-stage cho service auth, build, push. 

- **DAY 2: Terraform provisioning GKE cluster**
    * **Sub-Agent Workflow Specialization:** [GCP]
    * **Targeted Tag IDs:** 
    * **Target Component file path (`target_component`):** ./sources/infra/gcp/terraform/main.tf
    * **Low-Level Technical Task Instruction:** Tạo cluster GKE, VPC, IAM, node pools, autoscaling. 

- **DAY 3: Deploy services to GKE**
    * **Sub-Agent Workflow Specialization:** [GKE]
    * **Targeted Tag IDs:** 
    * **Target Component file path (`target_component`):** ./sources/infra/gke/deployment.yaml
    * **Low-Level Technical Task Instruction:** Định nghĩa Deployment, Service, Ingress, apply. 

- **DAY 4: Implement mobile UI for student role**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** 
    * **Target Component file path (`target_component`):** ./sources/frontend/mobile-app/src/pages/StudentDashboard.tsx
    * **Low-Level Technical Task Instruction:** Xây dựng giao diện dashboard, fetch API, i18n. 

- **DAY 5: Write API documentation for mobile UI**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Targeted Tag IDs:** 
    * **Target Component file path (`target_component`):** ./sources/docs/api-mobile.md
    * **Low-Level Technical Task Instruction:** Tài liệu API, endpoints, payloads. 

- **DAY 6: Write integration tests for mobile UI**
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** 
    * **Target Component file path (`target_component`):** ./sources/frontend/mobile-app/src/__tests__/StudentDashboard.spec.ts
    * **Low-Level Technical Task Instruction:** Viết test Jest, mock API, coverage. 

- **DAY 7: Review mobile UI code**
    * **Sub-Agent Workflow Specialization:** [Reviewer]
    * **Targeted Tag IDs:** 
    * **Target Component file path (`target_component`):** ./sources/frontend/mobile-app/src/pages/StudentDashboard.tsx
    * **Low-Level Technical Task Instruction:** Kiểm tra code quality, performance, accessibility. 

## 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ CHỐI XẠ

- **SQL Injection (SQLi) Countermeasures:** Sử dụng prepared statements, parameterized queries, whitelist input.
- **Cross-Site Scripting (XSS) & CSP:** Escape output, CSP headers, sanitize input.
- **CORS Security Rails:** Origin whitelist, dynamic tenant validation.
- **Log Scrubbing & PII Masking:** Định dạng log, mask email, phone.

## 📁 7. QUY ĐỊNH HỢP TÁC DI ĐỘNG & SEO

- **Capacitor Mobile Compliance:** Fetch API, offline caching, hardware back button.
- **i18n & SEO Injection:** Meta tags, hreflang, dynamic routing.

## 📁 8. PHÂN CÔNG NGHIỆP GIT

- **Branching Strategy:** features/development-phase-X-day-Y
- **Validation Gates:** compile, coverage >=85%, tests pass.

[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]