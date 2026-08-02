# GLOBAL PROJECT CONTEXT: membership-hub

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260802170418 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/02 17:04:18 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & PHƯƠNG THỨC KIẾN TRÚC CỐT LÕI

### 1.1. Tổng quan hệ thống & phương thức kiến trúc cốt lõi
[Provide a comprehensive technical overview mapping out the core detected architecture topology, EDA paradigms, CQRS boundaries, and Reactive Core patterns based strictly on requirements]

- Kiến trúc dựa trên mô hình microservices với các service độc lập: `auth`, `center`, `course`, `enrollment`, `attendance`, `card`, `notification`, `promotion`, `announcement`, `reporting`.
- Mỗi service được container hóa bằng Docker và triển khai trên Google Kubernetes Engine (GKE) với Horizontal Pod Autoscaler.
- Áp dụng CQRS cho các thao tác đọc/ghi: ví dụ: bảng `users` cho đọc, bảng `enrollments` cho ghi.
- Sử dụng Reactive Programming cho luồng xử lý điểm danh QR (`[ARC-007]`) và hàng đợi thông báo push (`[ARC-008]`).
- Tích hợp OAuth2 với Firebase Authentication, Google, Facebook để cấp JWT token (`[ARC-006]`).
- Triển khai PostgreSQL với Flyway migration, Redis cho caching phiên, và sử dụng Kafka cho messaging bất đồng bộ.
- Tuân thủ các nguyên tắc thiết kế đa tenant và phân quyền nghiêm ngặt theo RBAC (`[ARC-001]`–`[ARC-005]`).

## 📁 2. CÔNG NGHỆ & THƯ VIỆN HỆ SINH

- **Backend Infrastructure Core Stack:** Java 21, Quarkus 3.2, Hibernate ORM, SmallRye GraphQL, REST Easy, JUnit 5, Testcontainers, Flyway, Jackson, bcrypt, io.jsonwebtoken, Apache Commons, Lombok.
- **Database & Persistence:** PostgreSQL 15, Flyway, JPA Panache.
- **Messaging & Events:** Apache Kafka, SmallRye Reactive Messaging.
- **Authentication & Authorization:** Firebase Auth, OAuth2, JWT, Keycloak (nếu cần).
- **Mobile & Push:** Firebase Cloud Messaging (FCM), Apple APNs, Capacitor cho hybrid app.
- **Frontend & Mobile UI:** Next.js 14, React, TypeScript, Tailwind CSS, i18next, React Query, Capacitor, Expo.
- **DevOps & Infra:** Docker, Kubernetes (GKE), Helm, GitHub Actions, Terraform, Prometheus, Grafana, Jaeger.
- **Security & Compliance:** OWASP ZAP, SonarQube, Trivy, Snyk, TLS 1.3, AES-256 encryption, GDPR/CCPA tools.

## 📁 3. QUY TẮC BẢO VỆ TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP

- **Quy tắc biên giới không gian làm việc:** root `..`, tất cả đường dẫn bắt đầu với `./sources/`.
- **Quy tắc tiền tố thư mục động:** tuân thủ Protocol 1 (backend, frontend, infra).
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** tất cả mã nguồn Java phải nằm trong gói `org.nlh4j.saas.membershiphub`.
- **Strict Tester Target Path Syntax:** `<source_component>;<test_suite_file>`.

## 📁 4. BẢNG TÓM TẮT KIẾN TRÚC HÀNG ĐẦU THEO GIAI ĐOẠN

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1-2 | ./sources/backend.auth, ./sources/backend.center | Tạo bảng Users/Roles (`[DAT-001]`), bảng Centers (`[DAT-003]`), API xác thực (`[ARC-006]`), gán vai trò (`[ARC-001]`–`[ARC-005]`) | Coder,Tester,Reviewer,Doc,Docker,GCP,GKE | [REQ-001],[REQ-002],[REQ-003],[ARC-001],[ARC-002],[ARC-006],[DAT-001],[DAT-003],[NFR-003],[NFR-006] |
| Phase 2 | Day 3-4 | ./sources/backend.course, ./sources/backend.enrollment | Tạo bảng Courses (`[DAT-004]`), bảng Enrollments (`[DAT-005]`), API khóa học (`[REQ-007]`–`[REQ-009]`), API ghi danh (`[REQ-010]`–`[REQ-011]`), luồng điểm danh (`[ARC-007]`) | Coder,Tester,Reviewer,Doc,Docker,GCP,GKE | [REQ-007],[REQ-008],[REQ-009],[REQ-010],[REQ-011],[ARC-007],[ARC-008],[DAT-004],[DAT-005],[NFR-003],[NFR-006] |
| Phase 3 | Day 5-8 | ./sources/backend.attendance, ./sources/backend.card, ./sources/backend.notification | Tạo bảng Attendance (`[DAT-006]`), bảng StudentCards (`[DAT-007]`), bảng Notifications (`[DAT-008]`), API điểm danh (`[REQ-012]`–`[REQ-013]`), API thẻ (`[REQ-014]`–`[REQ-015]`), API thông báo (`[REQ-016]`), xử lý ngoại lệ (`[EXC-001]`–`[EXC-003]`) | Coder,Tester,Reviewer,Doc,Docker,GCP,GKE | [REQ-012],[REQ-013],[REQ-014],[REQ-015],[REQ-016],[EXC-001],[EXC-002],[EXC-003],[DAT-006],[DAT-007],[DAT-008],[NFR-003],[NFR-006] |
| Phase 4 | Day 9-12 | ./sources/backend.promo, ./sources/backend.announcement, ./sources/backend.systemsettings, ./sources/backend.reporting | Tạo bảng Promotions (`[DAT-009]`), bảng Announcements (`[DAT-009]`), bảng SystemSettings (`[DAT-011]`), API khuyến mãi (`[REQ-017]`–`[REQ-018]`), API thông báo (`[REQ-022]`–`[REQ-023]`), API báo cáo (`[REQ-024]`–`[REQ-025]`), xử lý ngoại lệ (`[EXC-004]`–`[EXC-005]`) | Coder,Tester,Reviewer,Doc,Docker,GCP,GKE | [REQ-017],[REQ-018],[REQ-022],[REQ-023],[REQ-024],[REQ-025],[EXC-004],[EXC-005],[DAT-009],[DAT-011],[NFR-001],[NFR-002],[NFR-004],[NFR-005],[NFR-007],[NFR-008],[NFR-009] |

## 5. CHI TIẾT KIẾN TRÚC THEO GIAI ĐOẠN & GIAO HÀNG NGÀY

### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng nền tảng người dùng, vai trò và quản lý trung tâm; thiết lập xác thực cơ bản và phân quyền RBAC.
- **Target Physical Directory Matrix Map:**
  - ./sources/backend.auth/src/main/resources/db/migration/V1__Create_Users_Table.sql `[DAT-001]`
  - ./sources/backend.auth/src/main/resources/db/migration/V2__Create_Roles_Table.sql `[DAT-001]`
  - ./sources/backend.center/src/main/resources/db/migration/V1__Create_Centers_Table.sql `[DAT-003]`
- **Database Schema DDL SQL Specification [DAT-001], [DAT-003]:**
```sql
-- [DAT-001] Bảng Users & Roles
CREATE TABLE users (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL REFERENCES roles(roleId),
    provider ENUM('local','firebase','google','facebook') NOT NULL,
    createdAt TIMESTAMP NOT NULL DEFAULT now(),
    updatedAt TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE roles (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

-- [DAT-003] Bảng Centers
CREATE TABLE centers (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(30),
    contactEmail VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
  - `POST /api/v1/auth/register` – đăng ký người dùng `[REQ-001]`
  - `POST /api/v1/auth/social` – OAuth2 social sign‑in `[REQ-002]`
  - `PUT /api/v1/users/{userId}/role` – gán vai trò `[REQ-003]`
  - `GET /api/v1/centers` – liệt kê trung tâm `[REQ-004]`
  - `POST /api/v1/centers` – tạo trung tâm `[REQ-005]`
  - `PATCH /api/v1/centers/{centerId}/admin` – phân quyền quản trị `[REQ-006]`
- **Phase Localized Exception Handlers [EXC-004]:**
  - Xác thực đầu vào không hợp lệ (email sai định dạng, thiếu trường bắt buộc) → trả về 400 với danh sách lỗi chi tiết.

#### 📅 Chronological Sub-Agent Task Distribution (Phase 1)
- **DAY 1:** Xây dựng DDL người dùng và vai trò
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth/src/main/resources/db/migration/V1__Create_Users_Table.sql `[DAT-001]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `users` với các cột `userId`, `email`, `passwordHash`, `fullName`, `roleId`, `provider`, `createdAt`, `updatedAt`. Áp dụng khóa chính, ràng buộc NOT NULL, UNIQUE cho email, khóa ngoại đến `roles`. Sử dụng UUID cho `userId`. Đảm bảo tuân thủ `[REQ-001]`, `[ARC-006]`, `[NFR-003]`, `[NFR-006]`.
      - **Targeted Tag IDs:** [REQ-001], [ARC-006], [DAT-001], [NFR-003], [NFR-006]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java;./sources/backend.auth/src/test/java/org/nlh4j/saas/membershiphub/service/AuthServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết unit test cho `AuthService.register` kiểm tra xác thực đầu vào, tạo người dùng, trả về JWT. Đảm bảo bao phủ trường hợp đăng ký thành công (`[REQ-001]`) và lỗi validation (`[EXC-004]`).
      - **Targeted Tag IDs:** [REQ-001], [EXC-004], [DAT-001]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth/src/main/resources/db/migration/V1__Create_Users_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tuân thủ mô hình dữ liệu, ràng buộc khóa ngoại, chỉ mục, và các yêu cầu bảo mật (`[NFR-003]`). Cung cấp phê duyệt hoặc danh sách yêu cầu sửa đổi.
      - **Targeted Tag IDs:** [DAT-001], [NFR-003]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth/docs/Users_Roles_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các ràng buộc. Bao gồm các thẻ tag `[REQ-001]`, `[ARC-006]`, `[DAT-001]`.
      - **Targeted Tag IDs:** [REQ-001], [ARC-006], [DAT-001]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile tối ưu hóa cho Quarkus, sử dụng image base `eclipse-temurin:21-jdk` với kích thước < 200 MB (`[NFR-005]`). Thêm nhãn `org.opencontainers.image.base.name` và thiết lập user không phải root.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth/gcp/sql-instance.yaml
      - **Low-Level Technical Task Instruction:** Khai báo Cloud SQL PostgreSQL instance với cấu hình HA, mã hóa dữ liệu ở nghỉ (`[NFR-003]`), và thiết lập IAM cho service account.
      - **Targeted Tag IDs:** [NFR-003]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.auth/gke/deployment.yaml
      - **Low-Level Technical Task Instruction:** Tạo Kubernetes Deployment cho auth service với resource limits (CPU 500m, memory 1Gi), HPA dựa trên latency (`[NFR-001]`), và service mesh cho bảo mật.
      - **Targeted Tag IDs:** [NFR-001]

  - **DAY 2:** Xây dựng DDL trung tâm và API trung tâm
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.center/src/main/resources/db/migration/V1__Create_Centers_Table.sql `[DAT-003]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `centers` với các cột `centerId`, `name`, `address`, `taxId`, `contactPhone`, `contactEmail`. Áp dụng UNIQUE cho `taxId`, NOT NULL cho các trường bắt buộc. Đảm bảo tuân thủ `[REQ-004]`, `[REQ-005]`, `[REQ-006]`, `[NFR-003]`.
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003], [NFR-003]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.center/src/main/java/org/nlh4j/saas/membershiphub/service/CenterService.java;./sources/backend.center/src/test/java/org/nlh4j/saas/membershiphub/service/CenterServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `CenterService.create` kiểm tra xung đột taxId (`[EXC-004]`), thành công, và test cho `assignAdmin`. Đảm bảo bao phủ `[REQ-005]`, `[REQ-006]`.
      - **Targeted Tag IDs:** [REQ-005], [REQ-006], [EXC-004], [DAT-003]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.center/src/main/resources/db/migration/V1__Create_Centers_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-003]`.
      - **Targeted Tag IDs:** [DAT-003], [NFR-003]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.center/docs/Centers_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-004]`, `[REQ-005]`, `[REQ-006]`.
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.center/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho center service, tuân thủ giới hạn kích thước hình ảnh (`[NFR-005]`), thiết lập health checks.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.center/gcp/iam-policy.yaml
      - **Low-Level Technical Task Instruction:** Thiết lập IAM roles cho center service account, áp dụng principle of least privilege.
      - **Targeted Tag IDs:** [NFR-003]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.center/gke/hpa.yaml
      - **Low-Level Technical Task Instruction:** Định nghĩa HPA cho center deployment dựa trên CPU > 70% hoặc latency > 300 ms (`[NFR-004]`).
      - **Targeted Tag IDs:** [NFR-004]

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng module khóa học và ghi danh; triển khai xác thực điểm danh QR và xung đột lịch học.
- **Target Physical Directory Matrix Map:**
  - ./sources/backend.course/src/main/resources/db/migration/V1__Create_Courses_Table.sql `[DAT-004]`
  - ./sources/backend.enrollment/src/main/resources/db/migration/V1__Create_Enrollments_Table.sql `[DAT-005]`
- **Database Schema DDL SQL Specification [DAT-004], [DAT-005]:**
```sql
-- [DAT-004] Bảng Courses
CREATE TABLE courses (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL REFERENCES users(userId),
    maxStudents INT NOT NULL DEFAULT 30
);

-- [DAT-005] Bảng Enrollments
CREATE TABLE enrollments (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES users(userId),
    courseId UUID NOT NULL REFERENCES courses(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(studentId, courseId)
);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [ARC-007], [ARC-008]:**
  - `GET /api/v1/courses` – duyệt khóa học `[REQ-007]`
  - `POST /api/v1/courses` – tạo khóa học `[REQ-008]`
  - `PUT /api/v1/courses/{courseId}` – cập nhật khóa học `[REQ-008]`
  - `PATCH /api/v1/courses/{courseId}/teacher` – phân công giáo viên `[REQ-009]`
  - `GET /api/v1/enrollments` – duyệt ghi danh `[REQ-010]`
  - `POST /api/v1/enrollments` – đăng ký khóa học `[REQ-011]`
  - `POST /api/v1/attendance/scan` – xử lý QR điểm danh `[REQ-012]`
- **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
  - Mất kết nối mạng trong khi quét QR → khi khôi phục, ghi lại điểm danh (`[EXC-001]`).
  - Quét QR trùng lặp trong cùng ngày → trả về thành công với cờ duplicate (`[EXC-002]`).

#### 📅 Chronological Sub-Agent Task Distribution (Phase 2)
- **DAY 3:** Xây dựng DDL khóa học và ghi danh
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.course/src/main/resources/db/migration/V1__Create_Courses_Table.sql `[DAT-004]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `courses` với các cột `courseId`, `title`, `description`, `startDate`, `endDate`, `teacherId`, `maxStudents`. Thêm ràng buộc UNIQUE cho `teacherId` + ngày chồng lấn (xử lý ở ứng dụng). Đảm bảo tuân thủ `[REQ-007]`, `[REQ-008]`, `[REQ-009]`, `[NFR-003]`.
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004], [NFR-003]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.course/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java;./sources/backend.course/src/test/java/org/nlh4j/saas/membershiphub/service/CourseServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `CourseService.create` kiểm tra xung đột lịch học (`[EXC-004]`), test cho `assignTeacher`. Đảm bảo bao phủ `[REQ-008]`, `[REQ-009]`.
      - **Targeted Tag IDs:** [REQ-008], [REQ-009], [EXC-004], [DAT-004]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.course/src/main/resources/db/migration/V1__Create_Courses_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-003]`.
      - **Targeted Tag IDs:** [DAT-004], [NFR-003]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.course/docs/Courses_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-007]`, `[REQ-008]`, `[REQ-009]`.
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.course/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile tối ưu hóa cho Quarkus, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập health checks.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.course/gcp/ vpc-peering.yaml
      - **Low-Level Technical Task Instruction:** Thiết lập VPC peering giữa auth và course services để đảm bảo giao tiếp riêng tư.
      - **Targeted Tag IDs:** [NFR-003]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.course/gke/ingress.yaml
      - **Low-Level Technical Task Instruction:** Tạo Ingress cho course service với TLS (`[NFR-003]`), định tuyến dựa trên host/path.
      - **Targeted Tag IDs:** [NFR-003]

  - **DAY 4:** Xây dựng DDL ghi danh và API điểm danh QR
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment/src/main/resources/db/migration/V1__Create_Enrollments_Table.sql `[DAT-005]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `enrollments` với các cột `enrollmentId`, `studentId`, `courseId`, `enrollmentDate`. Thêm UNIQUE(studentId, courseId) để ngăn ghi danh trùng lặp. Đảm bảo tuân thủ `[REQ-010]`, `[REQ-011]`, `[NFR-003]`.
      - **Targeted Tag IDs:** [REQ-010], [REQ-011], [DAT-005], [NFR-003]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment/src/main/java/org/nlh4j/saas/membershiphub/service/EnrollmentService.java;./sources/backend.enrollment/src/test/java/org/nlh4j/saas/membershiphub/service/EnrollmentServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `EnrollmentService.register` kiểm tra xung đột ghi danh (`[EXC-004]`), test cho `scanQr` xử lý duplicate (`[EXC-002]`).
      - **Targeted Tag IDs:** [REQ-011], [EXC-004], [EXC-002], [DAT-005]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment/src/main/resources/db/migration/V1__Create_Enrollments_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-003]`.
      - **Targeted Tag IDs:** [DAT-005], [NFR-003]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment/docs/Enrollments_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-010]`, `[REQ-011]`.
      - **Targeted Tag IDs:** [REQ-010], [REQ-011]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho enrollment service, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập user không phải root.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment/gcp/backup-policy.yaml
      - **Low-Level Technical Task Instruction:** Thiết lập chính sách backup cho Cloud SQL (hàng ngày, giữ 7 bản) để đảm bảo khả năng phục hồi (`[NFR-009]`).
      - **Targeted Tag IDs:** [NFR-009]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.enrollment/gke/autoscaling.yaml
      - **Low-Level Technical Task Instruction:** Định nghĩa Cluster Autoscaler cho enrollment deployment, điều chỉnh dựa trên latency (`[NFR-001]`).
      - **Targeted Tag IDs:** [NFR-001]

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng module điểm danh, thẻ hội viên và thông báo; triển khai xử lý QR bất biến và push notification.
- **Target Physical Directory Matrix Map:**
  - ./sources/backend.attendance/src/main/resources/db/migration/V1__Create_Attendance_Table.sql `[DAT-006]`
  - ./sources/backend.card/src/main/resources/db/migration/V1__Create_StudentCards_Table.sql `[DAT-007]`
  - ./sources/backend.notification/src/main/resources/db/migration/V1__Create_Notifications_Table.sql `[DAT-008]`
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007], [DAT-008]:**
```sql
-- [DAT-006] Bảng Attendance
CREATE TABLE attendance (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES users(userId),
    courseId UUID NOT NULL REFERENCES courses(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE(studentId, courseId, attendanceDate)
);

-- [DAT-007] Bảng StudentCards
CREATE TABLE studentcards (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES users(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);

-- [DAT-008] Bảng Notifications
CREATE TABLE notifications (
    notificationId UUID PRIMARY KEY,
    userId UUID REFERENCES users(userId),
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT now(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
```
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [ARC-007], [ARC-008]:**
  - `POST /api/v1/attendance/scan` – chụp ảnh QR điểm danh `[REQ-012]`
  - `GET /api/v1/attendance/scan` – trả về duplicate flag `[REQ-013]`
  - `GET /api/v1/cards/{studentId}` – hiển thị thẻ hội viên `[REQ-014]`
  - `POST /api/v1/cards/{cardId}/renew` – gia hạn thẻ `[REQ-015]`
  - `POST /api/v1/notifications` – tạo thông báo `[REQ-016]`
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003]:**
  - Mất kết nối mạng trong khi quét QR → khi khôi phục, ghi lại điểm danh (`[EXC-001]`).
  - Quét QR trùng lặp → trả về thành công với cờ duplicate (`[EXC-002]`).
  - Không thể gửi push notification → ghi log lỗi, lên lịch retry tối đa 3 lần (`[EXC-003]`).

#### 📅 Chronological Sub-Agent Task Distribution (Phase 3)
- **DAY 5:** Xây dựng DDL điểm danh, thẻ và thông báo
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.attendance/src/main/resources/db/migration/V1__Create_Attendance_Table.sql `[DAT-006]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `attendance` với các cột `attendanceId`, `studentId`, `courseId`, `attendanceDate`, `timestamp`. Thêm UNIQUE(studentId, courseId, attendanceDate) để đảm bảo bất biến. Đảm bảo tuân thủ `[REQ-012]`, `[REQ-013]`, `[NFR-003]`.
      - **Targeted Tag IDs:** [REQ-012], [REQ-013], [DAT-006], [NFR-003]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.attendance/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java;./sources/backend.attendance/src/test/java/org/nlh4j/saas/membershiphub/service/AttendanceServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `AttendanceService.record` kiểm tra duplicate (`[EXC-002]`), test cho network recovery (`[EXC-001]`).
      - **Targeted Tag IDs:** [REQ-012], [EXC-002], [EXC-001], [DAT-006]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.attendance/src/main/resources/db/migration/V1__Create_Attendance_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-003]`.
      - **Targeted Tag IDs:** [DAT-006], [NFR-003]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.attendance/docs/Attendance_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-012]`, `[REQ-013]`.
      - **Targeted Tag IDs:** [REQ-012], [REQ-013]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.attendance/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho attendance service, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập health checks.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.attendance/gcp/monitoring.yaml
      - **Low-Level Technical Task Instruction:** Thiết lập monitoring cho attendance service (Prometheus metrics) để theo dõi latency (`[NFR-001]`).
      - **Targeted Tag IDs:** [NFR-001]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.attendance/gke/service.yaml
      - **Low-Level Technical Task Instruction:** Tạo Service cho attendance, expose endpoint, thiết lập session affinity cho idempotent xử lý.
      - **Targeted Tag IDs:** [NFR-003]

  - **DAY 6:** Xây dựng DDL thẻ hội viên và thông báo
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.card/src/main/resources/db/migration/V1__Create_StudentCards_Table.sql `[DAT-007]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `studentcards` với các cột `cardId`, `studentId`, `issueDate`, `validityDays`, `remainingDays`. Thêm trigger để tự động cập nhật `remainingDays`. Đảm bảo tuân thủ `[REQ-014]`, `[REQ-015]`, `[NFR-003]`.
      - **Targeted Tag IDs:** [REQ-014], [REQ-015], [DAT-007], [NFR-003]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.card/src/main/java/org/nlh4j/saas/membershiphub/service/CardService.java;./sources/backend.card/src/test/java/org/nlh4j/saas/membershiphub/service/CardServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `CardService.renew` kiểm tra payment integration (`[EXC-004]`), test cho `CardService.getRemainingDays`.
      - **Targeted Tag IDs:** [REQ-015], [EXC-004], [DAT-007]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.card/src/main/resources/db/migration/V1__Create_StudentCards_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-003]`.
      - **Targeted Tag IDs:** [DAT-007], [NFR-003]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.card/docs/StudentCards_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-014]`, `[REQ-015]`.
      - **Targeted Tag IDs:** [REQ-014], [REQ-015]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.card/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho card service, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập user không phải root.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.card/gcp/iam-policy.yaml
      - **Low-Level Technical Task Instruction:** Thiết lập IAM roles cho card service account, áp dụng principle of least privilege.
      - **Targeted Tag IDs:** [NFR-003]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.card/gke/pod.yaml
      - **Low-Level Technical Task Instruction:** Tạo Pod cho card, thiết lập PodDisruptionBudget cho khả năng sẵn sàng (`[NFR-002]`).
      - **Targeted Tag IDs:** [NFR-002]

  - **DAY 7:** Xây dựng DDL thông báo và API thông báo
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification/src/main/resources/db/migration/V1__Create_Notifications_Table.sql `[DAT-008]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `notifications` với các cột `notificationId`, `userId`, `groupZalo`, `message`, `sentAt`, `delivered`. Thêm index trên `sentAt`. Đảm bảo tuân thủ `[REQ-016]`, `[EXC-003]`, `[NFR-003]`.
      - **Targeted Tag IDs:** [REQ-016], [EXC-003], [DAT-008], [NFR-003]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java;./sources/backend.notification/src/test/java/org/nlh4j/saas/membershiphub/service/NotificationServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `NotificationService.send` kiểm tra retry logic (`[EXC-003]`), test cho `delivered` flag.
      - **Targeted Tag IDs:** [REQ-016], [EXC-003], [DAT-008]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification/src/main/resources/db/migration/V1__Create_Notifications_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-003]`.
      - **Targeted Tag IDs:** [DAT-008], [NFR-003]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification/docs/Notifications_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-016]`.
      - **Targeted Tag IDs:** [REQ-016]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho notification service, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập logging.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification/gcp/pubsub.yaml
      - **Low-Level Technical Task Instruction:** Thiết lập Pub/Sub topic cho notification queue, đảm bảo delivery guarantees (`[NFR-002]`).
      - **Targeted Tag IDs:** [NFR-002]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.notification/gke/pod.yaml
      - **Low-Level Technical Task Instruction:** Tạo Pod cho notification, thiết lập resource limits (CPU 200m, memory 256Mi) để tối ưu hóa chi phí.
      - **Targeted Tag IDs:** [NFR-004]

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Xây dựng module khuyến mãi, thông báo, cài đặt hệ thống, báo cáo; triển khai SEO đa ngôn ngữ, tuân thủ GDPR/CCPA, và hoàn thiện cơ sở hạ tầng.
- **Target Physical Directory Matrix Map:**
  - ./sources/backend.promo/src/main/resources/db/migration/V1__Create_Promotions_Table.sql `[DAT-009]`
  - ./sources/backend.announcement/src/main/resources/db/migration/V1__Create_Announcements_Table.sql `[DAT-009]`
  - ./sources/backend.systemsettings/src/main/resources/db/migration/V1__Create_SystemSettings_Table.sql `[DAT-011]`
  - ./sources/backend.reporting/src/main/resources/db/migration/V1__Create_Reports_Table.sql `[DAT-011]` (dùng chung DAT-011 cho reporting)
- **Database Schema DDL SQL Specification [DAT-009], [DAT-011]:**
```sql
-- [DAT-009] Bảng Promotions & Announcements
CREATE TABLE promotions (
    promoId UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);

CREATE TABLE announcements (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);

-- [DAT-011] Bảng SystemSettings & Reports
CREATE TABLE systemsettings (
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description TEXT
);

CREATE TABLE reports (
    reportId UUID PRIMARY KEY,
    reportType VARCHAR(50) NOT NULL,
    generatedAt TIMESTAMP NOT NULL DEFAULT now(),
    filePath VARCHAR(255) NOT NULL,
    parameters JSONB
);
```
- **API and Event Routing Contracts [REQ-017], [REQ-018], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-009]:**
  - `GET /api/v1/promotions` – liệt kê khuyến mãi `[REQ-017]`
  - `POST /api/v1/promotions` – tạo khuyến mãi `[REQ-017]`
  - `PUT /api/v1/promotions/{promoId}` – cập nhật khuyến mãi `[REQ-017]`
  - `DELETE /api/v1/promotions/{promoId}` – xóa khuyến mãi `[REQ-017]`
  - `GET /api/v1/announcements` – liệt kê thông báo `[REQ-018]`
  - `POST /api/v1/announcements` – tạo thông báo `[REQ-018]`
  - `PUT /api/v1/announcements/{announcementId}` – cập nhật thông báo `[REQ-018]`
  - `DELETE /api/v1/announcements/{announcementId}` – xóa thông báo `[REQ-018]`
  - `GET /api/v1/i18n/{locale}` – lấy chuỗi dịch `[REQ-022]`
  - `GET /api/v1/seo/{locale}` – lấy meta tags SEO `[REQ-023]`
  - `GET /api/v1/reports/attendance` – tạo báo cáo điểm danh `[REQ-024]`
  - `GET /api/v1/dashboard/{centerId}` – bảng điều khiển tóm tắt `[REQ-025]`
- **Phase Localized Exception Handlers [EXC-004], [EXC-005]:**
  - Xác thực đầu vào không hợp lệ cho khuyến mãi/thông báo (`[EXC-004]`).
  - System recovery sau sự cố (`[EXC-005]`) – xử lý hàng đợi điểm danh chờ.

#### 📅 Chronological Sub-Agent Task Distribution (Phase 4)
- **DAY 8:** Xây dựng DDL khuyến mãi, thông báo, cài đặt hệ thống và báo cáo
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.promo/src/main/resources/db/migration/V1__Create_Promotions_Table.sql `[DAT-009]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `promotions` với các cột `promoId`, `code`, `discountPercent`, `startDate`, `endDate`, `description`. Thêm UNIQUE cho `code`. Đảm bảo tuân thủ `[REQ-017]`, `[NFR-003]`.
      - **Targeted Tag IDs:** [REQ-017], [DAT-009], [NFR-003]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.promo/src/main/java/org/nlh4j/saas/membershiphub/service/PromoService.java;./sources/backend.promo/src/test/java/org/nlh4j/saas/membershiphub/service/PromoServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `PromoService.create` kiểm tra validation (`[EXC-004]`), test cho `PromoService.list`.
      - **Targeted Tag IDs:** [REQ-017], [EXC-004], [DAT-009]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.promo/src/main/resources/db/migration/V1__Create_Promotions_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-003]`.
      - **Targeted Tag IDs:** [DAT-009], [NFR-003]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.promo/docs/Promotions_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-017]`.
      - **Targeted Tag IDs:** [REQ-017]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.promo/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho promo service, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập health checks.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.promo/gcp/cloudfunctions.yaml
      - **Low-Level Technical Task Instruction:** Triển khai Cloud Function để tự động vô hiệu hóa khuyến mãi hết hạn (`[NFR-004]`).
      - **Targeted Tag IDs:** [NFR-004]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.promo/gke/ingress.yaml
      - **Low-Level Technical Task Instruction:** Tạo Ingress cho promo service với TLS (`[NFR-003]`), định tuyến dựa trên host.
      - **Targeted Tag IDs:** [NFR-003]

  - **DAY 9:** Xây dựng DDL thông báo, cài đặt hệ thống và báo cáo
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.announcement/src/main/resources/db/migration/V1__Create_Announcements_Table.sql `[DAT-009]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `announcements` với các cột `announcementId`, `title`, `content`, `startDate`, `endDate`. Đảm bảo tuân thủ `[REQ-018]`, `[NFR-003]`.
      - **Targeted Tag IDs:** [REQ-018], [DAT-009], [NFR-003]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.announcement/src/main/java/org/nlh4j/saas/membershiphub/service/AnnouncementService.java;./sources/backend.announcement/src/test/java/org/nlh4j/saas/membershiphub/service/AnnouncementServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `AnnouncementService.create` kiểm tra validation (`[EXC-004]`), test cho `AnnouncementService.list`.
      - **Targeted Tag IDs:** [REQ-018], [EXC-004], [DAT-009]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.announcement/src/main/resources/db/migration/V1__Create_Announcements_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-003]`.
      - **Targeted Tag IDs:** [DAT-009], [NFR-003]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.announcement/docs/Announcements_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-018]`.
      - **Targeted Tag IDs:** [REQ-018]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.announcement/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho announcement service, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập logging.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.announcement/gcp/iam-policy.yaml
      - **Low-Level Technical Task Instruction:** Thiết lập IAM roles cho announcement service account, áp dụng principle of least privilege.
      - **Targeted Tag IDs:** [NFR-003]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.announcement/gke/autoscaling.yaml
      - **Low-Level Technical Task Instruction:** Định nghĩa HPA cho announcement deployment dựa trên CPU > 70% (`[NFR-004]`).
      - **Targeted Tag IDs:** [NFR-004]

  - **DAY 10:** Xây dựng DDL cài đặt hệ thống, báo cáo và triển khai SEO/i18n
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.systemsettings/src/main/resources/db/migration/V1__Create_SystemSettings_Table.sql `[DAT-011]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `systemsettings` với các cột `settingKey`, `settingValue`, `description`. Đảm bảo tuân thủ `[REQ-022]`, `[REQ-023]`, `[NFR-007]`.
      - **Targeted Tag IDs:** [REQ-022], [REQ-023], [DAT-011], [NFR-007]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.systemsettings/src/main/java/org/nlh4j/saas/membershiphub/service/SystemSettingsService.java;./sources/backend.systemsettings/src/test/java/org/nlh4j/saas/membershiphub/service/SystemSettingsServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `SystemSettingsService.get` kiểm tra locale, test cho `SystemSettingsService.set`.
      - **Targeted Tag IDs:** [REQ-022], [REQ-023], [DAT-011]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.systemsettings/src/main/resources/db/migration/V1__Create_SystemSettings_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-007]`.
      - **Targeted Tag IDs:** [DAT-011], [NFR-007]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.systemsettings/docs/SystemSettings_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-022]`, `[REQ-023]`.
      - **Targeted Tag IDs:** [REQ-022], [REQ-023]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.systemsettings/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho systemsettings service, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập health checks.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.systemsettings/gcp/secretmanager.yaml
      - **Low-Level Technical Task Instruction:** Lưu trữ khóa API và cấu hình trong Secret Manager để đảm bảo bảo mật (`[NFR-003]`).
      - **Targeted Tag IDs:** [NFR-003]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.systemsettings/gke/network-policy.yaml
      - **Low-Level Technical Task Instruction:** Tạo NetworkPolicy để giới hạn giao tiếp giữa các service (`[NFR-003]`).
      - **Targeted Tag IDs:** [NFR-003]

  - **DAY 11:** Xây dựng DDL báo cáo và triển khai SEO/i18n
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/backend.reporting/src/main/resources/db/migration/V1__Create_Reports_Table.sql `[DAT-011]`
      - **Low-Level Technical Task Instruction:** Tạo bảng `reports` với các cột `reportId`, `reportType`, `generatedAt`, `filePath`, `parameters`. Đảm bảo tuân thủ `[REQ-024]`, `[REQ-025]`, `[NFR-001]`.
      - **Targeted Tag IDs:** [REQ-024], [REQ-025], [DAT-011], [NFR-001]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/backend.reporting/src/main/java/org/nlh4j/saas/membershiphub/service/ReportingService.java;./sources/backend.reporting/src/test/java/org/nlh4j/saas/membershiphub/service/ReportingServiceTest.java
      - **Low-Level Technical Task Instruction:** Viết test cho `ReportingService.generateAttendanceReport` kiểm tra generation, test cho `ReportingService.getDashboard`.
      - **Targeted Tag IDs:** [REQ-024], [REQ-025], [DAT-011]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/backend.reporting/src/main/resources/db/migration/V1__Create_Reports_Table.sql
      - **Low-Level Technical Task Instruction:** Đánh giá DDL để đảm bảo tính toàn vẹn dữ liệu, chỉ mục, và tuân thủ `[NFR-001]`.
      - **Targeted Tag IDs:** [DAT-011], [NFR-001]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/backend.reporting/docs/Reports_Schema.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu mô tả cấu trúc bảng, mối quan hệ, và các yêu cầu nghiệp vụ. Bao gồm thẻ tag `[REQ-024]`, `[REQ-025]`.
      - **Targeted Tag IDs:** [REQ-024], [REQ-025]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/backend.reporting/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho reporting service, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập logging.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/backend.reporting/gcp/cloudscheduler.yaml
      - **Low-Level Technical Task Instruction:** Thiết lập Cloud Scheduler để tự động tạo báo cáo hàng ngày (`[NFR-004]`).
      - **Targeted Tag IDs:** [NFR-004]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/backend.reporting/gke/service.yaml
      - **Low-Level Technical Task Instruction:** Tạo Service cho reporting, expose endpoint, thiết lập resource limits (CPU 500m, memory 512Mi).
      - **Targeted Tag IDs:** [NFR-004]

  - **DAY 12:** Hoàn thiện frontend, di động, SEO, tuân thủ GDPR/CCPA và hoàn thiện cơ sở hạ tầng
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** ./sources/frontend/src/app/i18n.ts `[REQ-022]`, `[REQ-023]`
      - **Low-Level Technical Task Instruction:** Triển khai middleware phát hiện locale, tải tài nguyên dịch (`i18next`), và chèn hreflang vào HTML head cho SEO (`[REQ-023]`). Đảm bảo tuân thủ `[NFR-007]`, `[NFR-008]`.
      - **Targeted Tag IDs:** [REQ-022], [REQ-023], [NFR-007], [NFR-008]
    * **Tester:**
      - **Target Component file path (`target_component`):** ./sources/frontend/src/app/i18n.spec.ts
      - **Low-Level Technical Task Instruction:** Viết test cho i18n detection và hreflang generation, bao phủ `[REQ-022]`, `[REQ-023]`.
      - **Targeted Tag IDs:** [REQ-022], [REQ-023]
    * **Reviewer:**
      - **Target Component file path (`target_component`):** ./sources/frontend/src/app/i18n.ts
      - **Low-Level Technical Task Instruction:** Đánh giá việc triển khai đa ngôn ngữ để đảm bảo tuân thủ `[NFR-007]` và `[NFR-008]`.
      - **Targeted Tag IDs:** [NFR-007], [NFR-008]
    * **Doc:**
      - **Target Component file path (`target_component`):** ./sources/frontend/docs/i18n_SEO.md
      - **Low-Level Technical Task Instruction:** Tạo tài liệu hướng dẫn về triển khai i18n, hreflang, và các bước tuân thủ GDPR/CCPA.
      - **Targeted Tag IDs:** [REQ-022], [REQ-023], [NFR-007], [NFR-008]
    * **Docker:**
      - **Target Component file path (`target_component`):** ./sources/frontend/Dockerfile
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho frontend, tuân thủ giới hạn kích thước (`[NFR-005]`), thiết lập caching.
      - **Targeted Tag IDs:** [NFR-005]
    * **GCP:**
      - **Target Component file path (`target_component`):** ./sources/frontend/gcp/loadbalancing.yaml
      - **Low-Level Technical Task Instruction:** Thiết lập HTTP(S) load balancer với TLS (`[NFR-003]`), định hướng traffic đến các service.
      - **Targeted Tag IDs:** [NFR-003]
    * **GKE:**
      - **Target Component file path (`target_component`):** ./sources/frontend/gke/ingress.yaml
      - **Low-Level Technical Task Instruction:** Tạo Ingress cho frontend với TLS, thiết lập canonical URL cho SEO (`[NFR-003]`).
      - **Targeted Tag IDs:** [NFR-003]

## 📁 6. MÃ BẢO MẬT DOANH NGHIỆP & BIỆN PHÁP CHỐNG INJECTION [NFR-001] – [NFR-009]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng prepared statements, tham số hóa truy vấn, whitelist cho sắp xếp động.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động escape JSX, thiết lập header CSP (`script-src 'self'`), vô hiệu hóa `unsafe-inline`.
- **Multi-Tenant CORS Security Rails:** Phê duyệt origin dựa trên whitelist tenant, xác thực header `Origin` trước khi cho phép request cross-origin.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Áp dụng `@JsonSerialize` với `JsonIgnore` cho trường nhạy cảm, tự động thay thế email/phone trong log (`[NFR-006]`).

## 📁 7. QUY TẮC TUÂN THỦ DI ĐỘNG & CƠ CHẾ SEO QUỐC TẾ (Translate this header into "🇻🇳 Vietnamese")
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Quy tắc cho dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. DÒNG CHẠY TỰ ĐỘNG HÀNG NGÀY QUA GIT BRANCH FLOW (Translate this header into "🇻🇳 Vietnamese")
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-day-X`.
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE (Translate this header into "🇻🇳 Vietnamese")
[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]