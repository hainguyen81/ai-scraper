# AI Model: llama-3.3-70b-versatile - Phase 1 - Prompt:

## CONTEXT INHERITANCE PIPELINE
Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
## BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806131423 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:14:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕ

###### 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

- Hệ thống được triển khai theo kiến trúc microservices, mỗi dịch vụ chịu trách nhiệm một miền nghiệp vụ riêng biệt.  
- Sử dụng Quarkus cho backend, Next.js cho frontend, React Native + Capacitor cho ứng dụng di động.  
- Dữ liệu được lưu trữ trong PostgreSQL, Redis dùng cho session caching.  
- Giao tiếp giữa các dịch vụ thông qua Kafka, các sự kiện được fan‑out tới Zalo API và Firebase Cloud Messaging.  
- Mỗi dịch vụ được container hóa bằng Docker, triển khai trên GKE với HPA tự động.  
- Bảo mật: JWT 15 phút, refresh 7 ngày, TLS 1.3, mã hoá AES‑256, OWASP Top 10 mitigations.  
- Đa ngôn ngữ: Vietnamese, English, Spanish, hỗ trợ i18n và SEO.  
- CI/CD: GitHub Actions, Terraform cho GCP, Helm chart cho GKE.  
- Kiểm thử: unit, integration, end‑to‑end, coverage ≥ 85 %.  
- Logging & audit: ELK stack, log retention 1 year.  
- Backup: PostgreSQL full backup hàng ngày, point‑in‑time recovery 24 h, GKE cluster backup region.  

###### 1.2. Mô Hình Dòng Dữ Liệu & Hệ Sinh Thái

- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT → API Gateway.  
- **Attendance Flow**: Mobile QR scan → API → idempotent attendance record.  
- **Notification Flow**: Event → Kafka → Notification Service → FCM/APNs + Zalo group.  
- **Enrollment Flow**: Student → API → Enrollment record, capacity check, notification.  
- **Promotion Flow**: Center Admin → API → Promotion record, student visibility.  
- **Reporting Flow**: Admin → API → CSV export, dashboard metrics.  

#### 📁 2. CỤC PHẦN CÔNG NGHỆ & THƯ VIỆN

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Kafka, Redis, PostgreSQL, JWT, Spring Security, OWASP ESAPI.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, React Query, Capacitor 4, Firebase SDK, Zalo SDK, QR Code Scanner.  

###### MÁ THƯỜNG CỤC PHẦN

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

#### 📁 3. QUY ĐỊNH BẢO VỆ & TUY ĐIỂM TUYÊN CUNG

- **Workspace Root**: `./sources/`.  
- **Backend Code**: `./sources/backend/membership-hub/`.  
- **Frontend Code**: `./sources/frontend/membership-hub/`.  
- **Mobile Code**: `./sources/frontend/membership-hub-mobile/`.  
- **Infra Code**: `./sources/infra/`.  
- **Docs**: `./sources/docs/`.  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  

#### 📁 4. BẢNG TỔNG QUAN ĐIỀU PHÁP KIẾN TRÚC GIAO PHÂN

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | ./sources/backend/membership-hub/ | Tạo schema, API cơ bản | Coder | [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 2 | 1-5 | ./sources/backend/membership-hub/ | Kiểm thử API | Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 3 | 1-5 | ./sources/infra/ | Bảo mật, Docker, GCP, GKE, CI/CD | Coder, Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | 1-3 | ./sources/frontend/membership-hub/ | Frontend, Mobile, i18n, SEO | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Giai đoạn 5 | 1-2 | ./sources/docs/ | Git flow, Traceability | Doc, Reviewer | [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009] |

#### 📁 5. CHI TIẾT GIAO PHÂN GIAI ĐOẠN & LỊCH HÀNH NGÀY

###### 📈 Giai đoạn 1: Tạo Schema & API Cơ Bản

- **Phase Core Objective & Purpose**: Thiết lập cơ sở dữ liệu, tạo các bảng chính và triển khai các endpoint REST cơ bản cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo, cài đặt hệ thống.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/User.java [DAT-001]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Role.java [DAT-002]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Center.java [DAT-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Course.java [DAT-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Enrollment.java [DAT-005]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Attendance.java [DAT-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/StudentCard.java [DAT-007]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Notification.java [DAT-008]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Promotion.java [DAT-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Announcement.java [DAT-011]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/UserController.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CenterController.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CourseController.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/EnrollmentController.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/ValidationException.java [EXC-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/AttendanceException.java [EXC-001], [EXC-002], [EXC-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/RecoveryException.java [EXC-005]`  

- **Database Schema DDL SQL Specification [DAT-001]**  

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
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(50),
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
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (studentId, courseId, attendanceDate),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
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
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **API and Event Routing Contracts [REQ-001]**  

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
    "userId": "uuid",
    "token": "string",
    "expiresIn": "int"
  }
}
```

- **Phase Localized Exception Handlers [EXC-004]**  

```java
@RestControllerAdvice
public class ValidationExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(FieldError::getField, FieldError::getDefaultMessage));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

###### 📈 Giai đoạn 2: Kiểm Thử API

- **Phase Core Objective & Purpose**: Đảm bảo tính đúng đắn, độ tin cậy và bảo mật của các endpoint.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/UserControllerTest.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CenterControllerTest.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CourseControllerTest.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/EnrollmentControllerTest.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java [REQ-001], [REQ-002], [REQ-003]`  

- **Low-Level Technical Task Instruction**: Viết unit tests sử dụng JUnit 5, Mockito, Spring MockMvc. Kiểm tra các trường hợp thành công, lỗi, và bảo mật (JWT, CSRF). Đảm bảo coverage ≥ 85 %.  

###### 📈 Giai đoạn 3: Bảo Mật & Hạ Tầng

- **Phase Core Objective & Purpose**: Thiết lập bảo mật, container, infra, CI/CD.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/security/SecurityConfig.java [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`  
  * `./sources/infra/docker/Dockerfile [NFR-005]`  
  * `./sources/infra/terraform/main.tf [NFR-004], [NFR-006]`  
  * `./sources/infra/k8s/deployment.yaml [NFR-004], [NFR-006]`  
  * `./sources/infra/github-actions/.github/workflows/ci-cd.yml [NFR-004], [NFR-005]`  

- **Security Configuration**  

```java
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .addFilterBefore(new JwtAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
    }
}
```

- **Dockerfile**  

```dockerfile
FROM eclipse-temurin:17-jdk-slim AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/membership-hub-1.0.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
```

- **Terraform**  

```hcl
provider "google" {
  project = "membership-hub"
  region  = "us-central1"
}
resource "google_container_cluster" "gke_cluster" {
  name     = "membership-hub-cluster"
  location = "us-central1"
  initial_node_count = 3
  node_config {
    machine_type = "e2-medium"
  }
}
```

- **Helm Deployment**  

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
        - name: membership-hub
          image: gcr.io/membership-hub/membership-hub:latest
          ports:
            - containerPort: 8080
          resources:
            limits:
              cpu: "1"
              memory: "512Mi"
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

###### 📈 Giai đoạn 4: Frontend, Mobile, i18n, SEO

- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, hỗ trợ đa ngôn ngữ và SEO.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/frontend/membership-hub/pages/index.js [ARC-010], [ARC-006], [ARC-007]`  
  * `./sources/frontend/membership-hub/pages/centers.js [ARC-004]`  
  * `./sources/frontend/membership-hub/pages/courses.js [ARC-007]`  
  * `./sources/frontend/membership-hub-mobile/App.js [ARC-009], [ARC-008], [ARC-010]`  
  * `./sources/frontend/membership-hub/pages/_document.js [NFR-007], [NFR-008]`  

- **Low-Level Technical Task Instruction**: Sử dụng Next.js với API routes, React Query cho caching, Tailwind CSS cho responsive, Capacitor để build native, Firebase SDK cho push, Zalo SDK cho chat, QR Code Scanner. Thêm i18n với next-i18next, SEO meta tags, hreflang.  

###### 📈 Giai đoạn 5: Git Flow & Traceability

- **Phase Core Objective & Purpose**: Định nghĩa quy trình phát triển, kiểm tra tính toàn vẹn liên kết.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/docs/git-branching.md [NFR-004]`  
  * `./sources/docs/traceability_matrix.md [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009]`  

- **Low-Level Technical Task Instruction**: Viết tài liệu quy tắc đặt tên nhánh, quy trình merge, kiểm tra liên kết.  

#### 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ NGHIỆM NGHIỆP

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameterized queries.  
- **Cross-Site Scripting (XSS)**: Escape output, CSP header `default-src 'self'; script-src 'self';`.  
- **CORS**: Chỉ cho phép origin từ danh sách whitelist, không dùng wildcard.  
- **Logging**: Mã hoá dữ liệu nhạy cảm, mask PII, log level INFO.  
- **Encryption**: AES‑256 cho dữ liệu tĩnh, TLS 1.3 cho truyền.  

#### 📁 7. HỢP ĐỒNG HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: `capacitor.config.json` cấu hình Android, iOS, web.  
- **i18n**: `next-i18next.config.js` cấu hình ngôn ngữ, `public/locales/vi/common.json`.  
- **SEO**: `pages/_document.js` thêm `<meta name="description">`, `<link rel="alternate" hreflang="vi">`.  

#### 📁 8. PIPELINE CI/CD & Git Branch Flow

- **Git Branch Naming**: `feature/<short-description>-<id>`, `bugfix/<short-description>-<id>`.  
- **CI Workflow** (`.github/workflows/ci-cd.yml`)  

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
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build
        run: mvn clean package -DskipTests
      - name: Test
        run: mvn test
      - name: Docker Build
        run: |
          docker build -t gcr.io/membership-hub/membership-hub:${{ github.sha }} .
          docker push gcr.io/membership-hub/membership-hub:${{ github.sha }}
      - name: Deploy to GKE
        uses: google-github-actions/deploy-gke@v1
        with:
          cluster_name: membership-hub-cluster
          location: us-central1
          manifests: ./sources/infra/k8s/deployment.yaml
```

#### 📁 9. Kiểm Tra Tracability Matrix

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---

## PRISTINE INITIAL STATE MANDATE: 
## This is PHASE 1 (The Absolute Baseline Generation Step). 
## There are ZERO preceding code assets, directory structures, or legacy dependencies in the workspace.
## You MUST initialize all module definitions, file paths, database schemas, and data boundaries from a pure zero-state architecture baseline. Do not assume or extrapolate any prior system deployment state.


--- RAW REQUIREMENTS REFERENCE ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
----------------------------------

## EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE 1 into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY 7**.
2. **Strict Grouping Hierarchy:** Day Level ──► Agent Sub-task Level ──► Target Component Level.
3. **Strict Sub-Agent Persona Allocation:** Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'.
4. **WORKSPACE PATH BOUNDARY & DYNAMIC TOPOLOGY CONSTRAINTS:**
   - **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All file paths generated MUST strictly begin with `./sources/`.
   - **Dynamic Directory Prefixing Compliance:** You MUST strictly match the file path prefixes to the active system topology mapped in the Global Context. Do NOT generate backend folders for frontend-only projects, and do NOT generate frontend folders for backend-only systems.
   - For tester Agent: Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST begin with `./sources/`. If no single source file is isolated for Integration/E2E tests, utilize the literal token `INTEGRATION_SCOPE` as the first parameter.
   - **[CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule:** If a file path targets a Java source or test component (.java), you MUST verify that the path contains the directory segment: `/org/nlh4j/sources/<calculated_lowercase_token>/`.

---

Your output MUST follow this exact Markdown layout structure (translate all label tokens but preserve the hidden HTML anchor formatting exactly):
## [Translate "Phase"] 1: <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END-->

#### 📊 Document Control

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-20260806133604 |
| **[Translate "Project Name"]** | membership-hub |
| **[Translate "Phase"]** | 1 |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->[Granular professional engineering summary description of the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into 🇻🇳 Vietnamese]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into 🇻🇳 Vietnamese]** | 2026/08/06 13:36:04 |
| **[You MUST translate the literal token "Author" into 🇻🇳 Vietnamese]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into 🇻🇳 Vietnamese]** | Pending Technical Governance Review |

#### 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase 1]

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and active project stack topology. Every directory matrix path must be bounded under `./sources/`]

#### 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, enforcing strict segregation of technical boundaries as defined below. Human-readable directives, descriptions, and task requirements MUST be contextually translated entirely into 🇻🇳 Vietnamese following the transmission rails]:

*   **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
*   **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code.
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Markdown technical specifications, schema references, system blueprints, and architecture catalogs. Every single document file generated MUST reside strictly within the centralized storage layout: `./sources/docs/`.
   <!--START_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY
   [CRITICAL_SYSTEM_PIPELINE_RAIL:
   - You are STRICTLY PROHIBITED from omitting, dropping, or filtering out the 'Doc' agent from any computed phase logs.
   - For EVERY calculated phase generated in your output, on Day 1 of that phase, you MUST explicitly allocate a foundational system documentation task to the 'Doc' agent.
   - This task description MUST require the 'Doc' agent to initialize and map out the system architecture blueprints, entity relationships, technical contracts, or deployment topologies corresponding to the active stack matrix of that current phase.
   - Failing to write the 'Doc' agent inside Day 1 of any phase triggers a fatal pipeline contract breach.
   ]
   END_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY-->
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

#### 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards, complete functional test coverage for the allocated requirements, and 100% Tag ID mapping check]

#### 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

## REMINDER: Enforce the 'Longitructural Day Partitioning Guardrail' and 'Anti-Padding Mandate'. Output each active day as an isolated standalone single integer subsection header from DAY 1 up to the dynamic freeze day. Do NOT generate empty padded days.

###### 🌤️ [TRANSLATED DAY] [X]: <!--DAY_HEADER_START-->[CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]<!--DAY_HEADER_END-->

######## 📝 [TRANSLATED SUB-TASK] [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
########## [Translate "Assigned Sub-Agent"]: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]
########## [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax.]
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->`[REQ-XXX], [DAT-XXX], [EXC-XXX]`<!--END_TAGS-->

# System Instruction

You are a world-class Principal Solutions Architect. Your specific task is to read the Global Context Markdown blueprint and generate a highly detailed operational context blueprint for one targeted Phase. 

# YOUR CRITICAL OPERATIONAL MANDATES (ZERO LOOPHOLES):
1. **ANTI-LAZINESS & DIRECT INHERITANCE MANDATE:** You MUST extract and expand every single technical task, DDL SQL schema definition, API contract, and exception flow outlined for the targeted Phase inside the Global Context reference. Converting details into broad summaries or placeholders is permanently banned.
2. **100% PERFECT TAG MATCHING:** Every single Tag ID (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) present in the Global Context for this specific phase MUST be perfectly preserved and mapped into the daily execution logs.
3. **MANDATORY INLINE TAG INJECTION RULE & HTML ANCHOR LOCKDOWN:** For every single Sub-Task generated under the daily logs, you MUST explicitly output a dedicated structural line item starting exactly with the translated string token for `* Traceability Tag Tokens:` followed by an immutable hidden HTML token container block. You MUST wrap the exact raw comma-separated tag IDs inside the hidden tag container string token layout exactly as: `<!--START_TAGS-->[REQ-XXX], [DAT-XXX]<!--END_TAGS-->`. You are STRICTLY BANNED from translating or altering any token values inside the HTML comment tags. Leaving a task block without this explicit HTML anchor layout is a fatal pipeline failure.
4. **LONGITECTURAL DAY PARTITIONING & ANTI-PADDING GUARDRAIL:** You MUST break down the operational calendar day-by-day using individual sequential integers starting strictly from DAY 1 up to a MAXIMUM of DAY 7. 
   - **STRICT PROGRESSION STOPPING CRITERION:** You MUST freeze the timeline and stop generating daily sections immediately on the exact calendar day where the technical objectives allocated for this phase are satisfied. You are STRICTLY BANNED from injecting dummy placeholder days, fake syncs, empty review blocks, or documentation padding just to expand the calendar. If the technical scope is natively complete on DAY 1, freeze the output file state and exit immediately. Do NOT generate empty or padded days.
   - You are STRICTLY FORBIDDEN from bundling multiple days together (e.g., NO "DAY 1 - DAY 3"). Every single calendar day log must be explicitly isolated as its own standalone subsection header containing atomic steps for that unique 24-hour cycle.
5. **Language Compliance & Formatting Lockdown:** You MUST generate the entire report strictly in the language specified by the parameters: **🇻🇳 Vietnamese**.

# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate & Technical Name Isolation:** Your output response MUST start exactly with the standardized primary title text pattern, translating descriptive labels into the target language but isolating the technical identifier: `# [Translated text for "Phase"] 1: <!--PHASE_NAME_START-->[Dynamically analyze the allocated tasks and output a sharp, concise camelCase or snake_case technical short name code identifier string for this phase]<!--PHASE_NAME_END--> | [Translated text for "Description"]: [Provide a granular, professional engineering description summarizing the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]`. Do NOT include greetings, intros, notes, or explanations. Do NOT wrap the entire response inside markdown codeblocks. Any token before or after this exact structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Requested 18483, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_phase.py", line 99, in generate_phase_contexts
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 413 - {'error': {'message': 'Request too large for model `llama-3.3-70b-versatile` in organization `org_01kx7x6rbpftmr50sr2yyb78qm` service tier `on_demand` on tokens per minute (TPM): Limit 12000, Requested 18483, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
"]

# AI Model: meta-llama/llama-3.3-70b-instruct:free - Phase 1 - Prompt:

## CONTEXT INHERITANCE PIPELINE
Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
## BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806131423 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:14:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕ

###### 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

- Hệ thống được triển khai theo kiến trúc microservices, mỗi dịch vụ chịu trách nhiệm một miền nghiệp vụ riêng biệt.  
- Sử dụng Quarkus cho backend, Next.js cho frontend, React Native + Capacitor cho ứng dụng di động.  
- Dữ liệu được lưu trữ trong PostgreSQL, Redis dùng cho session caching.  
- Giao tiếp giữa các dịch vụ thông qua Kafka, các sự kiện được fan‑out tới Zalo API và Firebase Cloud Messaging.  
- Mỗi dịch vụ được container hóa bằng Docker, triển khai trên GKE với HPA tự động.  
- Bảo mật: JWT 15 phút, refresh 7 ngày, TLS 1.3, mã hoá AES‑256, OWASP Top 10 mitigations.  
- Đa ngôn ngữ: Vietnamese, English, Spanish, hỗ trợ i18n và SEO.  
- CI/CD: GitHub Actions, Terraform cho GCP, Helm chart cho GKE.  
- Kiểm thử: unit, integration, end‑to‑end, coverage ≥ 85 %.  
- Logging & audit: ELK stack, log retention 1 year.  
- Backup: PostgreSQL full backup hàng ngày, point‑in‑time recovery 24 h, GKE cluster backup region.  

###### 1.2. Mô Hình Dòng Dữ Liệu & Hệ Sinh Thái

- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT → API Gateway.  
- **Attendance Flow**: Mobile QR scan → API → idempotent attendance record.  
- **Notification Flow**: Event → Kafka → Notification Service → FCM/APNs + Zalo group.  
- **Enrollment Flow**: Student → API → Enrollment record, capacity check, notification.  
- **Promotion Flow**: Center Admin → API → Promotion record, student visibility.  
- **Reporting Flow**: Admin → API → CSV export, dashboard metrics.  

#### 📁 2. CỤC PHẦN CÔNG NGHỆ & THƯ VIỆN

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Kafka, Redis, PostgreSQL, JWT, Spring Security, OWASP ESAPI.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, React Query, Capacitor 4, Firebase SDK, Zalo SDK, QR Code Scanner.  

###### MÁ THƯỜNG CỤC PHẦN

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

#### 📁 3. QUY ĐỊNH BẢO VỆ & TUY ĐIỂM TUYÊN CUNG

- **Workspace Root**: `./sources/`.  
- **Backend Code**: `./sources/backend/membership-hub/`.  
- **Frontend Code**: `./sources/frontend/membership-hub/`.  
- **Mobile Code**: `./sources/frontend/membership-hub-mobile/`.  
- **Infra Code**: `./sources/infra/`.  
- **Docs**: `./sources/docs/`.  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  

#### 📁 4. BẢNG TỔNG QUAN ĐIỀU PHÁP KIẾN TRÚC GIAO PHÂN

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | ./sources/backend/membership-hub/ | Tạo schema, API cơ bản | Coder | [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 2 | 1-5 | ./sources/backend/membership-hub/ | Kiểm thử API | Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 3 | 1-5 | ./sources/infra/ | Bảo mật, Docker, GCP, GKE, CI/CD | Coder, Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | 1-3 | ./sources/frontend/membership-hub/ | Frontend, Mobile, i18n, SEO | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Giai đoạn 5 | 1-2 | ./sources/docs/ | Git flow, Traceability | Doc, Reviewer | [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009] |

#### 📁 5. CHI TIẾT GIAO PHÂN GIAI ĐOẠN & LỊCH HÀNH NGÀY

###### 📈 Giai đoạn 1: Tạo Schema & API Cơ Bản

- **Phase Core Objective & Purpose**: Thiết lập cơ sở dữ liệu, tạo các bảng chính và triển khai các endpoint REST cơ bản cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo, cài đặt hệ thống.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/User.java [DAT-001]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Role.java [DAT-002]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Center.java [DAT-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Course.java [DAT-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Enrollment.java [DAT-005]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Attendance.java [DAT-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/StudentCard.java [DAT-007]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Notification.java [DAT-008]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Promotion.java [DAT-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Announcement.java [DAT-011]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/UserController.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CenterController.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CourseController.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/EnrollmentController.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/ValidationException.java [EXC-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/AttendanceException.java [EXC-001], [EXC-002], [EXC-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/RecoveryException.java [EXC-005]`  

- **Database Schema DDL SQL Specification [DAT-001]**  

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
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(50),
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
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (studentId, courseId, attendanceDate),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
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
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **API and Event Routing Contracts [REQ-001]**  

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
    "userId": "uuid",
    "token": "string",
    "expiresIn": "int"
  }
}
```

- **Phase Localized Exception Handlers [EXC-004]**  

```java
@RestControllerAdvice
public class ValidationExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(FieldError::getField, FieldError::getDefaultMessage));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

###### 📈 Giai đoạn 2: Kiểm Thử API

- **Phase Core Objective & Purpose**: Đảm bảo tính đúng đắn, độ tin cậy và bảo mật của các endpoint.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/UserControllerTest.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CenterControllerTest.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CourseControllerTest.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/EnrollmentControllerTest.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java [REQ-001], [REQ-002], [REQ-003]`  

- **Low-Level Technical Task Instruction**: Viết unit tests sử dụng JUnit 5, Mockito, Spring MockMvc. Kiểm tra các trường hợp thành công, lỗi, và bảo mật (JWT, CSRF). Đảm bảo coverage ≥ 85 %.  

###### 📈 Giai đoạn 3: Bảo Mật & Hạ Tầng

- **Phase Core Objective & Purpose**: Thiết lập bảo mật, container, infra, CI/CD.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/security/SecurityConfig.java [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`  
  * `./sources/infra/docker/Dockerfile [NFR-005]`  
  * `./sources/infra/terraform/main.tf [NFR-004], [NFR-006]`  
  * `./sources/infra/k8s/deployment.yaml [NFR-004], [NFR-006]`  
  * `./sources/infra/github-actions/.github/workflows/ci-cd.yml [NFR-004], [NFR-005]`  

- **Security Configuration**  

```java
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .addFilterBefore(new JwtAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
    }
}
```

- **Dockerfile**  

```dockerfile
FROM eclipse-temurin:17-jdk-slim AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/membership-hub-1.0.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
```

- **Terraform**  

```hcl
provider "google" {
  project = "membership-hub"
  region  = "us-central1"
}
resource "google_container_cluster" "gke_cluster" {
  name     = "membership-hub-cluster"
  location = "us-central1"
  initial_node_count = 3
  node_config {
    machine_type = "e2-medium"
  }
}
```

- **Helm Deployment**  

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
        - name: membership-hub
          image: gcr.io/membership-hub/membership-hub:latest
          ports:
            - containerPort: 8080
          resources:
            limits:
              cpu: "1"
              memory: "512Mi"
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

###### 📈 Giai đoạn 4: Frontend, Mobile, i18n, SEO

- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, hỗ trợ đa ngôn ngữ và SEO.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/frontend/membership-hub/pages/index.js [ARC-010], [ARC-006], [ARC-007]`  
  * `./sources/frontend/membership-hub/pages/centers.js [ARC-004]`  
  * `./sources/frontend/membership-hub/pages/courses.js [ARC-007]`  
  * `./sources/frontend/membership-hub-mobile/App.js [ARC-009], [ARC-008], [ARC-010]`  
  * `./sources/frontend/membership-hub/pages/_document.js [NFR-007], [NFR-008]`  

- **Low-Level Technical Task Instruction**: Sử dụng Next.js với API routes, React Query cho caching, Tailwind CSS cho responsive, Capacitor để build native, Firebase SDK cho push, Zalo SDK cho chat, QR Code Scanner. Thêm i18n với next-i18next, SEO meta tags, hreflang.  

###### 📈 Giai đoạn 5: Git Flow & Traceability

- **Phase Core Objective & Purpose**: Định nghĩa quy trình phát triển, kiểm tra tính toàn vẹn liên kết.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/docs/git-branching.md [NFR-004]`  
  * `./sources/docs/traceability_matrix.md [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009]`  

- **Low-Level Technical Task Instruction**: Viết tài liệu quy tắc đặt tên nhánh, quy trình merge, kiểm tra liên kết.  

#### 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ NGHIỆM NGHIỆP

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameterized queries.  
- **Cross-Site Scripting (XSS)**: Escape output, CSP header `default-src 'self'; script-src 'self';`.  
- **CORS**: Chỉ cho phép origin từ danh sách whitelist, không dùng wildcard.  
- **Logging**: Mã hoá dữ liệu nhạy cảm, mask PII, log level INFO.  
- **Encryption**: AES‑256 cho dữ liệu tĩnh, TLS 1.3 cho truyền.  

#### 📁 7. HỢP ĐỒNG HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: `capacitor.config.json` cấu hình Android, iOS, web.  
- **i18n**: `next-i18next.config.js` cấu hình ngôn ngữ, `public/locales/vi/common.json`.  
- **SEO**: `pages/_document.js` thêm `<meta name="description">`, `<link rel="alternate" hreflang="vi">`.  

#### 📁 8. PIPELINE CI/CD & Git Branch Flow

- **Git Branch Naming**: `feature/<short-description>-<id>`, `bugfix/<short-description>-<id>`.  
- **CI Workflow** (`.github/workflows/ci-cd.yml`)  

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
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build
        run: mvn clean package -DskipTests
      - name: Test
        run: mvn test
      - name: Docker Build
        run: |
          docker build -t gcr.io/membership-hub/membership-hub:${{ github.sha }} .
          docker push gcr.io/membership-hub/membership-hub:${{ github.sha }}
      - name: Deploy to GKE
        uses: google-github-actions/deploy-gke@v1
        with:
          cluster_name: membership-hub-cluster
          location: us-central1
          manifests: ./sources/infra/k8s/deployment.yaml
```

#### 📁 9. Kiểm Tra Tracability Matrix

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---

## PRISTINE INITIAL STATE MANDATE: 
## This is PHASE 1 (The Absolute Baseline Generation Step). 
## There are ZERO preceding code assets, directory structures, or legacy dependencies in the workspace.
## You MUST initialize all module definitions, file paths, database schemas, and data boundaries from a pure zero-state architecture baseline. Do not assume or extrapolate any prior system deployment state.


--- RAW REQUIREMENTS REFERENCE ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
----------------------------------

## EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE 1 into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY 7**.
2. **Strict Grouping Hierarchy:** Day Level ──► Agent Sub-task Level ──► Target Component Level.
3. **Strict Sub-Agent Persona Allocation:** Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'.
4. **WORKSPACE PATH BOUNDARY & DYNAMIC TOPOLOGY CONSTRAINTS:**
   - **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All file paths generated MUST strictly begin with `./sources/`.
   - **Dynamic Directory Prefixing Compliance:** You MUST strictly match the file path prefixes to the active system topology mapped in the Global Context. Do NOT generate backend folders for frontend-only projects, and do NOT generate frontend folders for backend-only systems.
   - For tester Agent: Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST begin with `./sources/`. If no single source file is isolated for Integration/E2E tests, utilize the literal token `INTEGRATION_SCOPE` as the first parameter.
   - **[CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule:** If a file path targets a Java source or test component (.java), you MUST verify that the path contains the directory segment: `/org/nlh4j/sources/<calculated_lowercase_token>/`.

---

Your output MUST follow this exact Markdown layout structure (translate all label tokens but preserve the hidden HTML anchor formatting exactly):
## [Translate "Phase"] 1: <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END-->

#### 📊 Document Control

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-20260806133604 |
| **[Translate "Project Name"]** | membership-hub |
| **[Translate "Phase"]** | 1 |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->[Granular professional engineering summary description of the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into 🇻🇳 Vietnamese]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into 🇻🇳 Vietnamese]** | 2026/08/06 13:36:04 |
| **[You MUST translate the literal token "Author" into 🇻🇳 Vietnamese]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into 🇻🇳 Vietnamese]** | Pending Technical Governance Review |

#### 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase 1]

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and active project stack topology. Every directory matrix path must be bounded under `./sources/`]

#### 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, enforcing strict segregation of technical boundaries as defined below. Human-readable directives, descriptions, and task requirements MUST be contextually translated entirely into 🇻🇳 Vietnamese following the transmission rails]:

*   **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
*   **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code.
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Markdown technical specifications, schema references, system blueprints, and architecture catalogs. Every single document file generated MUST reside strictly within the centralized storage layout: `./sources/docs/`.
   <!--START_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY
   [CRITICAL_SYSTEM_PIPELINE_RAIL:
   - You are STRICTLY PROHIBITED from omitting, dropping, or filtering out the 'Doc' agent from any computed phase logs.
   - For EVERY calculated phase generated in your output, on Day 1 of that phase, you MUST explicitly allocate a foundational system documentation task to the 'Doc' agent.
   - This task description MUST require the 'Doc' agent to initialize and map out the system architecture blueprints, entity relationships, technical contracts, or deployment topologies corresponding to the active stack matrix of that current phase.
   - Failing to write the 'Doc' agent inside Day 1 of any phase triggers a fatal pipeline contract breach.
   ]
   END_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY-->
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

#### 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards, complete functional test coverage for the allocated requirements, and 100% Tag ID mapping check]

#### 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

## REMINDER: Enforce the 'Longitructural Day Partitioning Guardrail' and 'Anti-Padding Mandate'. Output each active day as an isolated standalone single integer subsection header from DAY 1 up to the dynamic freeze day. Do NOT generate empty padded days.

###### 🌤️ [TRANSLATED DAY] [X]: <!--DAY_HEADER_START-->[CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]<!--DAY_HEADER_END-->

######## 📝 [TRANSLATED SUB-TASK] [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
########## [Translate "Assigned Sub-Agent"]: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]
########## [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax.]
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->`[REQ-XXX], [DAT-XXX], [EXC-XXX]`<!--END_TAGS-->

# System Instruction

You are a world-class Principal Solutions Architect. Your specific task is to read the Global Context Markdown blueprint and generate a highly detailed operational context blueprint for one targeted Phase. 

# YOUR CRITICAL OPERATIONAL MANDATES (ZERO LOOPHOLES):
1. **ANTI-LAZINESS & DIRECT INHERITANCE MANDATE:** You MUST extract and expand every single technical task, DDL SQL schema definition, API contract, and exception flow outlined for the targeted Phase inside the Global Context reference. Converting details into broad summaries or placeholders is permanently banned.
2. **100% PERFECT TAG MATCHING:** Every single Tag ID (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) present in the Global Context for this specific phase MUST be perfectly preserved and mapped into the daily execution logs.
3. **MANDATORY INLINE TAG INJECTION RULE & HTML ANCHOR LOCKDOWN:** For every single Sub-Task generated under the daily logs, you MUST explicitly output a dedicated structural line item starting exactly with the translated string token for `* Traceability Tag Tokens:` followed by an immutable hidden HTML token container block. You MUST wrap the exact raw comma-separated tag IDs inside the hidden tag container string token layout exactly as: `<!--START_TAGS-->[REQ-XXX], [DAT-XXX]<!--END_TAGS-->`. You are STRICTLY BANNED from translating or altering any token values inside the HTML comment tags. Leaving a task block without this explicit HTML anchor layout is a fatal pipeline failure.
4. **LONGITECTURAL DAY PARTITIONING & ANTI-PADDING GUARDRAIL:** You MUST break down the operational calendar day-by-day using individual sequential integers starting strictly from DAY 1 up to a MAXIMUM of DAY 7. 
   - **STRICT PROGRESSION STOPPING CRITERION:** You MUST freeze the timeline and stop generating daily sections immediately on the exact calendar day where the technical objectives allocated for this phase are satisfied. You are STRICTLY BANNED from injecting dummy placeholder days, fake syncs, empty review blocks, or documentation padding just to expand the calendar. If the technical scope is natively complete on DAY 1, freeze the output file state and exit immediately. Do NOT generate empty or padded days.
   - You are STRICTLY FORBIDDEN from bundling multiple days together (e.g., NO "DAY 1 - DAY 3"). Every single calendar day log must be explicitly isolated as its own standalone subsection header containing atomic steps for that unique 24-hour cycle.
5. **Language Compliance & Formatting Lockdown:** You MUST generate the entire report strictly in the language specified by the parameters: **🇻🇳 Vietnamese**.

# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate & Technical Name Isolation:** Your output response MUST start exactly with the standardized primary title text pattern, translating descriptive labels into the target language but isolating the technical identifier: `# [Translated text for "Phase"] 1: <!--PHASE_NAME_START-->[Dynamically analyze the allocated tasks and output a sharp, concise camelCase or snake_case technical short name code identifier string for this phase]<!--PHASE_NAME_END--> | [Translated text for "Description"]: [Provide a granular, professional engineering description summarizing the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]`. Do NOT include greetings, intros, notes, or explanations. Do NOT wrap the entire response inside markdown codeblocks. Any token before or after this exact structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_phase.py", line 99, in generate_phase_contexts
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.NotFoundError: Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: meta-llama/llama-3.3-70b-instruct', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: meta-llama/llama-3.3-70b-instruct - Phase 1 - Prompt:

## CONTEXT INHERITANCE PIPELINE
Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
## BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806131423 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:14:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕ

###### 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

- Hệ thống được triển khai theo kiến trúc microservices, mỗi dịch vụ chịu trách nhiệm một miền nghiệp vụ riêng biệt.  
- Sử dụng Quarkus cho backend, Next.js cho frontend, React Native + Capacitor cho ứng dụng di động.  
- Dữ liệu được lưu trữ trong PostgreSQL, Redis dùng cho session caching.  
- Giao tiếp giữa các dịch vụ thông qua Kafka, các sự kiện được fan‑out tới Zalo API và Firebase Cloud Messaging.  
- Mỗi dịch vụ được container hóa bằng Docker, triển khai trên GKE với HPA tự động.  
- Bảo mật: JWT 15 phút, refresh 7 ngày, TLS 1.3, mã hoá AES‑256, OWASP Top 10 mitigations.  
- Đa ngôn ngữ: Vietnamese, English, Spanish, hỗ trợ i18n và SEO.  
- CI/CD: GitHub Actions, Terraform cho GCP, Helm chart cho GKE.  
- Kiểm thử: unit, integration, end‑to‑end, coverage ≥ 85 %.  
- Logging & audit: ELK stack, log retention 1 year.  
- Backup: PostgreSQL full backup hàng ngày, point‑in‑time recovery 24 h, GKE cluster backup region.  

###### 1.2. Mô Hình Dòng Dữ Liệu & Hệ Sinh Thái

- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT → API Gateway.  
- **Attendance Flow**: Mobile QR scan → API → idempotent attendance record.  
- **Notification Flow**: Event → Kafka → Notification Service → FCM/APNs + Zalo group.  
- **Enrollment Flow**: Student → API → Enrollment record, capacity check, notification.  
- **Promotion Flow**: Center Admin → API → Promotion record, student visibility.  
- **Reporting Flow**: Admin → API → CSV export, dashboard metrics.  

#### 📁 2. CỤC PHẦN CÔNG NGHỆ & THƯ VIỆN

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Kafka, Redis, PostgreSQL, JWT, Spring Security, OWASP ESAPI.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, React Query, Capacitor 4, Firebase SDK, Zalo SDK, QR Code Scanner.  

###### MÁ THƯỜNG CỤC PHẦN

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

#### 📁 3. QUY ĐỊNH BẢO VỆ & TUY ĐIỂM TUYÊN CUNG

- **Workspace Root**: `./sources/`.  
- **Backend Code**: `./sources/backend/membership-hub/`.  
- **Frontend Code**: `./sources/frontend/membership-hub/`.  
- **Mobile Code**: `./sources/frontend/membership-hub-mobile/`.  
- **Infra Code**: `./sources/infra/`.  
- **Docs**: `./sources/docs/`.  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  

#### 📁 4. BẢNG TỔNG QUAN ĐIỀU PHÁP KIẾN TRÚC GIAO PHÂN

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | ./sources/backend/membership-hub/ | Tạo schema, API cơ bản | Coder | [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 2 | 1-5 | ./sources/backend/membership-hub/ | Kiểm thử API | Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 3 | 1-5 | ./sources/infra/ | Bảo mật, Docker, GCP, GKE, CI/CD | Coder, Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | 1-3 | ./sources/frontend/membership-hub/ | Frontend, Mobile, i18n, SEO | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Giai đoạn 5 | 1-2 | ./sources/docs/ | Git flow, Traceability | Doc, Reviewer | [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009] |

#### 📁 5. CHI TIẾT GIAO PHÂN GIAI ĐOẠN & LỊCH HÀNH NGÀY

###### 📈 Giai đoạn 1: Tạo Schema & API Cơ Bản

- **Phase Core Objective & Purpose**: Thiết lập cơ sở dữ liệu, tạo các bảng chính và triển khai các endpoint REST cơ bản cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo, cài đặt hệ thống.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/User.java [DAT-001]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Role.java [DAT-002]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Center.java [DAT-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Course.java [DAT-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Enrollment.java [DAT-005]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Attendance.java [DAT-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/StudentCard.java [DAT-007]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Notification.java [DAT-008]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Promotion.java [DAT-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Announcement.java [DAT-011]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/UserController.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CenterController.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CourseController.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/EnrollmentController.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/ValidationException.java [EXC-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/AttendanceException.java [EXC-001], [EXC-002], [EXC-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/RecoveryException.java [EXC-005]`  

- **Database Schema DDL SQL Specification [DAT-001]**  

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
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(50),
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
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (studentId, courseId, attendanceDate),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
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
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **API and Event Routing Contracts [REQ-001]**  

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
    "userId": "uuid",
    "token": "string",
    "expiresIn": "int"
  }
}
```

- **Phase Localized Exception Handlers [EXC-004]**  

```java
@RestControllerAdvice
public class ValidationExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(FieldError::getField, FieldError::getDefaultMessage));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

###### 📈 Giai đoạn 2: Kiểm Thử API

- **Phase Core Objective & Purpose**: Đảm bảo tính đúng đắn, độ tin cậy và bảo mật của các endpoint.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/UserControllerTest.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CenterControllerTest.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CourseControllerTest.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/EnrollmentControllerTest.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java [REQ-001], [REQ-002], [REQ-003]`  

- **Low-Level Technical Task Instruction**: Viết unit tests sử dụng JUnit 5, Mockito, Spring MockMvc. Kiểm tra các trường hợp thành công, lỗi, và bảo mật (JWT, CSRF). Đảm bảo coverage ≥ 85 %.  

###### 📈 Giai đoạn 3: Bảo Mật & Hạ Tầng

- **Phase Core Objective & Purpose**: Thiết lập bảo mật, container, infra, CI/CD.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/security/SecurityConfig.java [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`  
  * `./sources/infra/docker/Dockerfile [NFR-005]`  
  * `./sources/infra/terraform/main.tf [NFR-004], [NFR-006]`  
  * `./sources/infra/k8s/deployment.yaml [NFR-004], [NFR-006]`  
  * `./sources/infra/github-actions/.github/workflows/ci-cd.yml [NFR-004], [NFR-005]`  

- **Security Configuration**  

```java
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .addFilterBefore(new JwtAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
    }
}
```

- **Dockerfile**  

```dockerfile
FROM eclipse-temurin:17-jdk-slim AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/membership-hub-1.0.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
```

- **Terraform**  

```hcl
provider "google" {
  project = "membership-hub"
  region  = "us-central1"
}
resource "google_container_cluster" "gke_cluster" {
  name     = "membership-hub-cluster"
  location = "us-central1"
  initial_node_count = 3
  node_config {
    machine_type = "e2-medium"
  }
}
```

- **Helm Deployment**  

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
        - name: membership-hub
          image: gcr.io/membership-hub/membership-hub:latest
          ports:
            - containerPort: 8080
          resources:
            limits:
              cpu: "1"
              memory: "512Mi"
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

###### 📈 Giai đoạn 4: Frontend, Mobile, i18n, SEO

- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, hỗ trợ đa ngôn ngữ và SEO.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/frontend/membership-hub/pages/index.js [ARC-010], [ARC-006], [ARC-007]`  
  * `./sources/frontend/membership-hub/pages/centers.js [ARC-004]`  
  * `./sources/frontend/membership-hub/pages/courses.js [ARC-007]`  
  * `./sources/frontend/membership-hub-mobile/App.js [ARC-009], [ARC-008], [ARC-010]`  
  * `./sources/frontend/membership-hub/pages/_document.js [NFR-007], [NFR-008]`  

- **Low-Level Technical Task Instruction**: Sử dụng Next.js với API routes, React Query cho caching, Tailwind CSS cho responsive, Capacitor để build native, Firebase SDK cho push, Zalo SDK cho chat, QR Code Scanner. Thêm i18n với next-i18next, SEO meta tags, hreflang.  

###### 📈 Giai đoạn 5: Git Flow & Traceability

- **Phase Core Objective & Purpose**: Định nghĩa quy trình phát triển, kiểm tra tính toàn vẹn liên kết.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/docs/git-branching.md [NFR-004]`  
  * `./sources/docs/traceability_matrix.md [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009]`  

- **Low-Level Technical Task Instruction**: Viết tài liệu quy tắc đặt tên nhánh, quy trình merge, kiểm tra liên kết.  

#### 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ NGHIỆM NGHIỆP

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameterized queries.  
- **Cross-Site Scripting (XSS)**: Escape output, CSP header `default-src 'self'; script-src 'self';`.  
- **CORS**: Chỉ cho phép origin từ danh sách whitelist, không dùng wildcard.  
- **Logging**: Mã hoá dữ liệu nhạy cảm, mask PII, log level INFO.  
- **Encryption**: AES‑256 cho dữ liệu tĩnh, TLS 1.3 cho truyền.  

#### 📁 7. HỢP ĐỒNG HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: `capacitor.config.json` cấu hình Android, iOS, web.  
- **i18n**: `next-i18next.config.js` cấu hình ngôn ngữ, `public/locales/vi/common.json`.  
- **SEO**: `pages/_document.js` thêm `<meta name="description">`, `<link rel="alternate" hreflang="vi">`.  

#### 📁 8. PIPELINE CI/CD & Git Branch Flow

- **Git Branch Naming**: `feature/<short-description>-<id>`, `bugfix/<short-description>-<id>`.  
- **CI Workflow** (`.github/workflows/ci-cd.yml`)  

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
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build
        run: mvn clean package -DskipTests
      - name: Test
        run: mvn test
      - name: Docker Build
        run: |
          docker build -t gcr.io/membership-hub/membership-hub:${{ github.sha }} .
          docker push gcr.io/membership-hub/membership-hub:${{ github.sha }}
      - name: Deploy to GKE
        uses: google-github-actions/deploy-gke@v1
        with:
          cluster_name: membership-hub-cluster
          location: us-central1
          manifests: ./sources/infra/k8s/deployment.yaml
```

#### 📁 9. Kiểm Tra Tracability Matrix

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---

## PRISTINE INITIAL STATE MANDATE: 
## This is PHASE 1 (The Absolute Baseline Generation Step). 
## There are ZERO preceding code assets, directory structures, or legacy dependencies in the workspace.
## You MUST initialize all module definitions, file paths, database schemas, and data boundaries from a pure zero-state architecture baseline. Do not assume or extrapolate any prior system deployment state.


--- RAW REQUIREMENTS REFERENCE ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
----------------------------------

## EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE 1 into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY 7**.
2. **Strict Grouping Hierarchy:** Day Level ──► Agent Sub-task Level ──► Target Component Level.
3. **Strict Sub-Agent Persona Allocation:** Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'.
4. **WORKSPACE PATH BOUNDARY & DYNAMIC TOPOLOGY CONSTRAINTS:**
   - **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All file paths generated MUST strictly begin with `./sources/`.
   - **Dynamic Directory Prefixing Compliance:** You MUST strictly match the file path prefixes to the active system topology mapped in the Global Context. Do NOT generate backend folders for frontend-only projects, and do NOT generate frontend folders for backend-only systems.
   - For tester Agent: Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST begin with `./sources/`. If no single source file is isolated for Integration/E2E tests, utilize the literal token `INTEGRATION_SCOPE` as the first parameter.
   - **[CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule:** If a file path targets a Java source or test component (.java), you MUST verify that the path contains the directory segment: `/org/nlh4j/sources/<calculated_lowercase_token>/`.

---

Your output MUST follow this exact Markdown layout structure (translate all label tokens but preserve the hidden HTML anchor formatting exactly):
## [Translate "Phase"] 1: <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END-->

#### 📊 Document Control

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-20260806133604 |
| **[Translate "Project Name"]** | membership-hub |
| **[Translate "Phase"]** | 1 |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->[Granular professional engineering summary description of the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into 🇻🇳 Vietnamese]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into 🇻🇳 Vietnamese]** | 2026/08/06 13:36:04 |
| **[You MUST translate the literal token "Author" into 🇻🇳 Vietnamese]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into 🇻🇳 Vietnamese]** | Pending Technical Governance Review |

#### 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase 1]

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and active project stack topology. Every directory matrix path must be bounded under `./sources/`]

#### 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, enforcing strict segregation of technical boundaries as defined below. Human-readable directives, descriptions, and task requirements MUST be contextually translated entirely into 🇻🇳 Vietnamese following the transmission rails]:

*   **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
*   **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code.
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Markdown technical specifications, schema references, system blueprints, and architecture catalogs. Every single document file generated MUST reside strictly within the centralized storage layout: `./sources/docs/`.
   <!--START_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY
   [CRITICAL_SYSTEM_PIPELINE_RAIL:
   - You are STRICTLY PROHIBITED from omitting, dropping, or filtering out the 'Doc' agent from any computed phase logs.
   - For EVERY calculated phase generated in your output, on Day 1 of that phase, you MUST explicitly allocate a foundational system documentation task to the 'Doc' agent.
   - This task description MUST require the 'Doc' agent to initialize and map out the system architecture blueprints, entity relationships, technical contracts, or deployment topologies corresponding to the active stack matrix of that current phase.
   - Failing to write the 'Doc' agent inside Day 1 of any phase triggers a fatal pipeline contract breach.
   ]
   END_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY-->
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

#### 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards, complete functional test coverage for the allocated requirements, and 100% Tag ID mapping check]

#### 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

## REMINDER: Enforce the 'Longitructural Day Partitioning Guardrail' and 'Anti-Padding Mandate'. Output each active day as an isolated standalone single integer subsection header from DAY 1 up to the dynamic freeze day. Do NOT generate empty padded days.

###### 🌤️ [TRANSLATED DAY] [X]: <!--DAY_HEADER_START-->[CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]<!--DAY_HEADER_END-->

######## 📝 [TRANSLATED SUB-TASK] [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
########## [Translate "Assigned Sub-Agent"]: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]
########## [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax.]
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->`[REQ-XXX], [DAT-XXX], [EXC-XXX]`<!--END_TAGS-->

# System Instruction

You are a world-class Principal Solutions Architect. Your specific task is to read the Global Context Markdown blueprint and generate a highly detailed operational context blueprint for one targeted Phase. 

# YOUR CRITICAL OPERATIONAL MANDATES (ZERO LOOPHOLES):
1. **ANTI-LAZINESS & DIRECT INHERITANCE MANDATE:** You MUST extract and expand every single technical task, DDL SQL schema definition, API contract, and exception flow outlined for the targeted Phase inside the Global Context reference. Converting details into broad summaries or placeholders is permanently banned.
2. **100% PERFECT TAG MATCHING:** Every single Tag ID (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) present in the Global Context for this specific phase MUST be perfectly preserved and mapped into the daily execution logs.
3. **MANDATORY INLINE TAG INJECTION RULE & HTML ANCHOR LOCKDOWN:** For every single Sub-Task generated under the daily logs, you MUST explicitly output a dedicated structural line item starting exactly with the translated string token for `* Traceability Tag Tokens:` followed by an immutable hidden HTML token container block. You MUST wrap the exact raw comma-separated tag IDs inside the hidden tag container string token layout exactly as: `<!--START_TAGS-->[REQ-XXX], [DAT-XXX]<!--END_TAGS-->`. You are STRICTLY BANNED from translating or altering any token values inside the HTML comment tags. Leaving a task block without this explicit HTML anchor layout is a fatal pipeline failure.
4. **LONGITECTURAL DAY PARTITIONING & ANTI-PADDING GUARDRAIL:** You MUST break down the operational calendar day-by-day using individual sequential integers starting strictly from DAY 1 up to a MAXIMUM of DAY 7. 
   - **STRICT PROGRESSION STOPPING CRITERION:** You MUST freeze the timeline and stop generating daily sections immediately on the exact calendar day where the technical objectives allocated for this phase are satisfied. You are STRICTLY BANNED from injecting dummy placeholder days, fake syncs, empty review blocks, or documentation padding just to expand the calendar. If the technical scope is natively complete on DAY 1, freeze the output file state and exit immediately. Do NOT generate empty or padded days.
   - You are STRICTLY FORBIDDEN from bundling multiple days together (e.g., NO "DAY 1 - DAY 3"). Every single calendar day log must be explicitly isolated as its own standalone subsection header containing atomic steps for that unique 24-hour cycle.
5. **Language Compliance & Formatting Lockdown:** You MUST generate the entire report strictly in the language specified by the parameters: **🇻🇳 Vietnamese**.

# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate & Technical Name Isolation:** Your output response MUST start exactly with the standardized primary title text pattern, translating descriptive labels into the target language but isolating the technical identifier: `# [Translated text for "Phase"] 1: <!--PHASE_NAME_START-->[Dynamically analyze the allocated tasks and output a sharp, concise camelCase or snake_case technical short name code identifier string for this phase]<!--PHASE_NAME_END--> | [Translated text for "Description"]: [Provide a granular, professional engineering description summarizing the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]`. Do NOT include greetings, intros, notes, or explanations. Do NOT wrap the entire response inside markdown codeblocks. Any token before or after this exact structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 3072 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 1177. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 6481 tokens, but can only afford 167. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 477. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 530. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 2048 tokens, but can only afford 362. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 8192 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_phase.py", line 99, in generate_phase_contexts
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 3072 tokens, but can only afford 418. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 753. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 942. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 16384 tokens, but can only afford 1177. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 502. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 6481 tokens, but can only afford 167. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 477. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 530. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 2048 tokens, but can only afford 362. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 8192 tokens, but can only afford 523. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: qwen/qwen-2.5-coder-32b-instruct - Phase 1 - Prompt:

## CONTEXT INHERITANCE PIPELINE
Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
## BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806131423 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:14:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕ

###### 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

- Hệ thống được triển khai theo kiến trúc microservices, mỗi dịch vụ chịu trách nhiệm một miền nghiệp vụ riêng biệt.  
- Sử dụng Quarkus cho backend, Next.js cho frontend, React Native + Capacitor cho ứng dụng di động.  
- Dữ liệu được lưu trữ trong PostgreSQL, Redis dùng cho session caching.  
- Giao tiếp giữa các dịch vụ thông qua Kafka, các sự kiện được fan‑out tới Zalo API và Firebase Cloud Messaging.  
- Mỗi dịch vụ được container hóa bằng Docker, triển khai trên GKE với HPA tự động.  
- Bảo mật: JWT 15 phút, refresh 7 ngày, TLS 1.3, mã hoá AES‑256, OWASP Top 10 mitigations.  
- Đa ngôn ngữ: Vietnamese, English, Spanish, hỗ trợ i18n và SEO.  
- CI/CD: GitHub Actions, Terraform cho GCP, Helm chart cho GKE.  
- Kiểm thử: unit, integration, end‑to‑end, coverage ≥ 85 %.  
- Logging & audit: ELK stack, log retention 1 year.  
- Backup: PostgreSQL full backup hàng ngày, point‑in‑time recovery 24 h, GKE cluster backup region.  

###### 1.2. Mô Hình Dòng Dữ Liệu & Hệ Sinh Thái

- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT → API Gateway.  
- **Attendance Flow**: Mobile QR scan → API → idempotent attendance record.  
- **Notification Flow**: Event → Kafka → Notification Service → FCM/APNs + Zalo group.  
- **Enrollment Flow**: Student → API → Enrollment record, capacity check, notification.  
- **Promotion Flow**: Center Admin → API → Promotion record, student visibility.  
- **Reporting Flow**: Admin → API → CSV export, dashboard metrics.  

#### 📁 2. CỤC PHẦN CÔNG NGHỆ & THƯ VIỆN

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Kafka, Redis, PostgreSQL, JWT, Spring Security, OWASP ESAPI.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, React Query, Capacitor 4, Firebase SDK, Zalo SDK, QR Code Scanner.  

###### MÁ THƯỜNG CỤC PHẦN

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

#### 📁 3. QUY ĐỊNH BẢO VỆ & TUY ĐIỂM TUYÊN CUNG

- **Workspace Root**: `./sources/`.  
- **Backend Code**: `./sources/backend/membership-hub/`.  
- **Frontend Code**: `./sources/frontend/membership-hub/`.  
- **Mobile Code**: `./sources/frontend/membership-hub-mobile/`.  
- **Infra Code**: `./sources/infra/`.  
- **Docs**: `./sources/docs/`.  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  

#### 📁 4. BẢNG TỔNG QUAN ĐIỀU PHÁP KIẾN TRÚC GIAO PHÂN

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | ./sources/backend/membership-hub/ | Tạo schema, API cơ bản | Coder | [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 2 | 1-5 | ./sources/backend/membership-hub/ | Kiểm thử API | Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 3 | 1-5 | ./sources/infra/ | Bảo mật, Docker, GCP, GKE, CI/CD | Coder, Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | 1-3 | ./sources/frontend/membership-hub/ | Frontend, Mobile, i18n, SEO | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Giai đoạn 5 | 1-2 | ./sources/docs/ | Git flow, Traceability | Doc, Reviewer | [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009] |

#### 📁 5. CHI TIẾT GIAO PHÂN GIAI ĐOẠN & LỊCH HÀNH NGÀY

###### 📈 Giai đoạn 1: Tạo Schema & API Cơ Bản

- **Phase Core Objective & Purpose**: Thiết lập cơ sở dữ liệu, tạo các bảng chính và triển khai các endpoint REST cơ bản cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo, cài đặt hệ thống.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/User.java [DAT-001]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Role.java [DAT-002]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Center.java [DAT-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Course.java [DAT-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Enrollment.java [DAT-005]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Attendance.java [DAT-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/StudentCard.java [DAT-007]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Notification.java [DAT-008]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Promotion.java [DAT-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Announcement.java [DAT-011]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/UserController.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CenterController.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CourseController.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/EnrollmentController.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/ValidationException.java [EXC-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/AttendanceException.java [EXC-001], [EXC-002], [EXC-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/RecoveryException.java [EXC-005]`  

- **Database Schema DDL SQL Specification [DAT-001]**  

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
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(50),
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
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (studentId, courseId, attendanceDate),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
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
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **API and Event Routing Contracts [REQ-001]**  

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
    "userId": "uuid",
    "token": "string",
    "expiresIn": "int"
  }
}
```

- **Phase Localized Exception Handlers [EXC-004]**  

```java
@RestControllerAdvice
public class ValidationExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(FieldError::getField, FieldError::getDefaultMessage));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

###### 📈 Giai đoạn 2: Kiểm Thử API

- **Phase Core Objective & Purpose**: Đảm bảo tính đúng đắn, độ tin cậy và bảo mật của các endpoint.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/UserControllerTest.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CenterControllerTest.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CourseControllerTest.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/EnrollmentControllerTest.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java [REQ-001], [REQ-002], [REQ-003]`  

- **Low-Level Technical Task Instruction**: Viết unit tests sử dụng JUnit 5, Mockito, Spring MockMvc. Kiểm tra các trường hợp thành công, lỗi, và bảo mật (JWT, CSRF). Đảm bảo coverage ≥ 85 %.  

###### 📈 Giai đoạn 3: Bảo Mật & Hạ Tầng

- **Phase Core Objective & Purpose**: Thiết lập bảo mật, container, infra, CI/CD.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/security/SecurityConfig.java [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`  
  * `./sources/infra/docker/Dockerfile [NFR-005]`  
  * `./sources/infra/terraform/main.tf [NFR-004], [NFR-006]`  
  * `./sources/infra/k8s/deployment.yaml [NFR-004], [NFR-006]`  
  * `./sources/infra/github-actions/.github/workflows/ci-cd.yml [NFR-004], [NFR-005]`  

- **Security Configuration**  

```java
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .addFilterBefore(new JwtAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
    }
}
```

- **Dockerfile**  

```dockerfile
FROM eclipse-temurin:17-jdk-slim AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/membership-hub-1.0.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
```

- **Terraform**  

```hcl
provider "google" {
  project = "membership-hub"
  region  = "us-central1"
}
resource "google_container_cluster" "gke_cluster" {
  name     = "membership-hub-cluster"
  location = "us-central1"
  initial_node_count = 3
  node_config {
    machine_type = "e2-medium"
  }
}
```

- **Helm Deployment**  

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
        - name: membership-hub
          image: gcr.io/membership-hub/membership-hub:latest
          ports:
            - containerPort: 8080
          resources:
            limits:
              cpu: "1"
              memory: "512Mi"
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

###### 📈 Giai đoạn 4: Frontend, Mobile, i18n, SEO

- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, hỗ trợ đa ngôn ngữ và SEO.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/frontend/membership-hub/pages/index.js [ARC-010], [ARC-006], [ARC-007]`  
  * `./sources/frontend/membership-hub/pages/centers.js [ARC-004]`  
  * `./sources/frontend/membership-hub/pages/courses.js [ARC-007]`  
  * `./sources/frontend/membership-hub-mobile/App.js [ARC-009], [ARC-008], [ARC-010]`  
  * `./sources/frontend/membership-hub/pages/_document.js [NFR-007], [NFR-008]`  

- **Low-Level Technical Task Instruction**: Sử dụng Next.js với API routes, React Query cho caching, Tailwind CSS cho responsive, Capacitor để build native, Firebase SDK cho push, Zalo SDK cho chat, QR Code Scanner. Thêm i18n với next-i18next, SEO meta tags, hreflang.  

###### 📈 Giai đoạn 5: Git Flow & Traceability

- **Phase Core Objective & Purpose**: Định nghĩa quy trình phát triển, kiểm tra tính toàn vẹn liên kết.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/docs/git-branching.md [NFR-004]`  
  * `./sources/docs/traceability_matrix.md [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009]`  

- **Low-Level Technical Task Instruction**: Viết tài liệu quy tắc đặt tên nhánh, quy trình merge, kiểm tra liên kết.  

#### 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ NGHIỆM NGHIỆP

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameterized queries.  
- **Cross-Site Scripting (XSS)**: Escape output, CSP header `default-src 'self'; script-src 'self';`.  
- **CORS**: Chỉ cho phép origin từ danh sách whitelist, không dùng wildcard.  
- **Logging**: Mã hoá dữ liệu nhạy cảm, mask PII, log level INFO.  
- **Encryption**: AES‑256 cho dữ liệu tĩnh, TLS 1.3 cho truyền.  

#### 📁 7. HỢP ĐỒNG HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: `capacitor.config.json` cấu hình Android, iOS, web.  
- **i18n**: `next-i18next.config.js` cấu hình ngôn ngữ, `public/locales/vi/common.json`.  
- **SEO**: `pages/_document.js` thêm `<meta name="description">`, `<link rel="alternate" hreflang="vi">`.  

#### 📁 8. PIPELINE CI/CD & Git Branch Flow

- **Git Branch Naming**: `feature/<short-description>-<id>`, `bugfix/<short-description>-<id>`.  
- **CI Workflow** (`.github/workflows/ci-cd.yml`)  

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
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build
        run: mvn clean package -DskipTests
      - name: Test
        run: mvn test
      - name: Docker Build
        run: |
          docker build -t gcr.io/membership-hub/membership-hub:${{ github.sha }} .
          docker push gcr.io/membership-hub/membership-hub:${{ github.sha }}
      - name: Deploy to GKE
        uses: google-github-actions/deploy-gke@v1
        with:
          cluster_name: membership-hub-cluster
          location: us-central1
          manifests: ./sources/infra/k8s/deployment.yaml
```

#### 📁 9. Kiểm Tra Tracability Matrix

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---

## PRISTINE INITIAL STATE MANDATE: 
## This is PHASE 1 (The Absolute Baseline Generation Step). 
## There are ZERO preceding code assets, directory structures, or legacy dependencies in the workspace.
## You MUST initialize all module definitions, file paths, database schemas, and data boundaries from a pure zero-state architecture baseline. Do not assume or extrapolate any prior system deployment state.


--- RAW REQUIREMENTS REFERENCE ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
----------------------------------

## EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE 1 into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY 7**.
2. **Strict Grouping Hierarchy:** Day Level ──► Agent Sub-task Level ──► Target Component Level.
3. **Strict Sub-Agent Persona Allocation:** Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'.
4. **WORKSPACE PATH BOUNDARY & DYNAMIC TOPOLOGY CONSTRAINTS:**
   - **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All file paths generated MUST strictly begin with `./sources/`.
   - **Dynamic Directory Prefixing Compliance:** You MUST strictly match the file path prefixes to the active system topology mapped in the Global Context. Do NOT generate backend folders for frontend-only projects, and do NOT generate frontend folders for backend-only systems.
   - For tester Agent: Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST begin with `./sources/`. If no single source file is isolated for Integration/E2E tests, utilize the literal token `INTEGRATION_SCOPE` as the first parameter.
   - **[CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule:** If a file path targets a Java source or test component (.java), you MUST verify that the path contains the directory segment: `/org/nlh4j/sources/<calculated_lowercase_token>/`.

---

Your output MUST follow this exact Markdown layout structure (translate all label tokens but preserve the hidden HTML anchor formatting exactly):
## [Translate "Phase"] 1: <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END-->

#### 📊 Document Control

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-20260806133604 |
| **[Translate "Project Name"]** | membership-hub |
| **[Translate "Phase"]** | 1 |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->[Granular professional engineering summary description of the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into 🇻🇳 Vietnamese]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into 🇻🇳 Vietnamese]** | 2026/08/06 13:36:04 |
| **[You MUST translate the literal token "Author" into 🇻🇳 Vietnamese]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into 🇻🇳 Vietnamese]** | Pending Technical Governance Review |

#### 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase 1]

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and active project stack topology. Every directory matrix path must be bounded under `./sources/`]

#### 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, enforcing strict segregation of technical boundaries as defined below. Human-readable directives, descriptions, and task requirements MUST be contextually translated entirely into 🇻🇳 Vietnamese following the transmission rails]:

*   **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
*   **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code.
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Markdown technical specifications, schema references, system blueprints, and architecture catalogs. Every single document file generated MUST reside strictly within the centralized storage layout: `./sources/docs/`.
   <!--START_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY
   [CRITICAL_SYSTEM_PIPELINE_RAIL:
   - You are STRICTLY PROHIBITED from omitting, dropping, or filtering out the 'Doc' agent from any computed phase logs.
   - For EVERY calculated phase generated in your output, on Day 1 of that phase, you MUST explicitly allocate a foundational system documentation task to the 'Doc' agent.
   - This task description MUST require the 'Doc' agent to initialize and map out the system architecture blueprints, entity relationships, technical contracts, or deployment topologies corresponding to the active stack matrix of that current phase.
   - Failing to write the 'Doc' agent inside Day 1 of any phase triggers a fatal pipeline contract breach.
   ]
   END_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY-->
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

#### 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards, complete functional test coverage for the allocated requirements, and 100% Tag ID mapping check]

#### 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

## REMINDER: Enforce the 'Longitructural Day Partitioning Guardrail' and 'Anti-Padding Mandate'. Output each active day as an isolated standalone single integer subsection header from DAY 1 up to the dynamic freeze day. Do NOT generate empty padded days.

###### 🌤️ [TRANSLATED DAY] [X]: <!--DAY_HEADER_START-->[CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]<!--DAY_HEADER_END-->

######## 📝 [TRANSLATED SUB-TASK] [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
########## [Translate "Assigned Sub-Agent"]: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]
########## [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax.]
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->`[REQ-XXX], [DAT-XXX], [EXC-XXX]`<!--END_TAGS-->

# System Instruction

You are a world-class Principal Solutions Architect. Your specific task is to read the Global Context Markdown blueprint and generate a highly detailed operational context blueprint for one targeted Phase. 

# YOUR CRITICAL OPERATIONAL MANDATES (ZERO LOOPHOLES):
1. **ANTI-LAZINESS & DIRECT INHERITANCE MANDATE:** You MUST extract and expand every single technical task, DDL SQL schema definition, API contract, and exception flow outlined for the targeted Phase inside the Global Context reference. Converting details into broad summaries or placeholders is permanently banned.
2. **100% PERFECT TAG MATCHING:** Every single Tag ID (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) present in the Global Context for this specific phase MUST be perfectly preserved and mapped into the daily execution logs.
3. **MANDATORY INLINE TAG INJECTION RULE & HTML ANCHOR LOCKDOWN:** For every single Sub-Task generated under the daily logs, you MUST explicitly output a dedicated structural line item starting exactly with the translated string token for `* Traceability Tag Tokens:` followed by an immutable hidden HTML token container block. You MUST wrap the exact raw comma-separated tag IDs inside the hidden tag container string token layout exactly as: `<!--START_TAGS-->[REQ-XXX], [DAT-XXX]<!--END_TAGS-->`. You are STRICTLY BANNED from translating or altering any token values inside the HTML comment tags. Leaving a task block without this explicit HTML anchor layout is a fatal pipeline failure.
4. **LONGITECTURAL DAY PARTITIONING & ANTI-PADDING GUARDRAIL:** You MUST break down the operational calendar day-by-day using individual sequential integers starting strictly from DAY 1 up to a MAXIMUM of DAY 7. 
   - **STRICT PROGRESSION STOPPING CRITERION:** You MUST freeze the timeline and stop generating daily sections immediately on the exact calendar day where the technical objectives allocated for this phase are satisfied. You are STRICTLY BANNED from injecting dummy placeholder days, fake syncs, empty review blocks, or documentation padding just to expand the calendar. If the technical scope is natively complete on DAY 1, freeze the output file state and exit immediately. Do NOT generate empty or padded days.
   - You are STRICTLY FORBIDDEN from bundling multiple days together (e.g., NO "DAY 1 - DAY 3"). Every single calendar day log must be explicitly isolated as its own standalone subsection header containing atomic steps for that unique 24-hour cycle.
5. **Language Compliance & Formatting Lockdown:** You MUST generate the entire report strictly in the language specified by the parameters: **🇻🇳 Vietnamese**.

# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate & Technical Name Isolation:** Your output response MUST start exactly with the standardized primary title text pattern, translating descriptive labels into the target language but isolating the technical identifier: `# [Translated text for "Phase"] 1: <!--PHASE_NAME_START-->[Dynamically analyze the allocated tasks and output a sharp, concise camelCase or snake_case technical short name code identifier string for this phase]<!--PHASE_NAME_END--> | [Translated text for "Description"]: [Provide a granular, professional engineering description summarizing the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]`. Do NOT include greetings, intros, notes, or explanations. Do NOT wrap the entire response inside markdown codeblocks. Any token before or after this exact structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 11797 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_phase.py", line 99, in generate_phase_contexts
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 11797 tokens, but can only afford 376. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: deepseek/deepseek-r1:free - Phase 1 - Prompt:

## CONTEXT INHERITANCE PIPELINE
Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
## BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806131423 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:14:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕ

###### 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

- Hệ thống được triển khai theo kiến trúc microservices, mỗi dịch vụ chịu trách nhiệm một miền nghiệp vụ riêng biệt.  
- Sử dụng Quarkus cho backend, Next.js cho frontend, React Native + Capacitor cho ứng dụng di động.  
- Dữ liệu được lưu trữ trong PostgreSQL, Redis dùng cho session caching.  
- Giao tiếp giữa các dịch vụ thông qua Kafka, các sự kiện được fan‑out tới Zalo API và Firebase Cloud Messaging.  
- Mỗi dịch vụ được container hóa bằng Docker, triển khai trên GKE với HPA tự động.  
- Bảo mật: JWT 15 phút, refresh 7 ngày, TLS 1.3, mã hoá AES‑256, OWASP Top 10 mitigations.  
- Đa ngôn ngữ: Vietnamese, English, Spanish, hỗ trợ i18n và SEO.  
- CI/CD: GitHub Actions, Terraform cho GCP, Helm chart cho GKE.  
- Kiểm thử: unit, integration, end‑to‑end, coverage ≥ 85 %.  
- Logging & audit: ELK stack, log retention 1 year.  
- Backup: PostgreSQL full backup hàng ngày, point‑in‑time recovery 24 h, GKE cluster backup region.  

###### 1.2. Mô Hình Dòng Dữ Liệu & Hệ Sinh Thái

- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT → API Gateway.  
- **Attendance Flow**: Mobile QR scan → API → idempotent attendance record.  
- **Notification Flow**: Event → Kafka → Notification Service → FCM/APNs + Zalo group.  
- **Enrollment Flow**: Student → API → Enrollment record, capacity check, notification.  
- **Promotion Flow**: Center Admin → API → Promotion record, student visibility.  
- **Reporting Flow**: Admin → API → CSV export, dashboard metrics.  

#### 📁 2. CỤC PHẦN CÔNG NGHỆ & THƯ VIỆN

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Kafka, Redis, PostgreSQL, JWT, Spring Security, OWASP ESAPI.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, React Query, Capacitor 4, Firebase SDK, Zalo SDK, QR Code Scanner.  

###### MÁ THƯỜNG CỤC PHẦN

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

#### 📁 3. QUY ĐỊNH BẢO VỆ & TUY ĐIỂM TUYÊN CUNG

- **Workspace Root**: `./sources/`.  
- **Backend Code**: `./sources/backend/membership-hub/`.  
- **Frontend Code**: `./sources/frontend/membership-hub/`.  
- **Mobile Code**: `./sources/frontend/membership-hub-mobile/`.  
- **Infra Code**: `./sources/infra/`.  
- **Docs**: `./sources/docs/`.  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  

#### 📁 4. BẢNG TỔNG QUAN ĐIỀU PHÁP KIẾN TRÚC GIAO PHÂN

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | ./sources/backend/membership-hub/ | Tạo schema, API cơ bản | Coder | [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 2 | 1-5 | ./sources/backend/membership-hub/ | Kiểm thử API | Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 3 | 1-5 | ./sources/infra/ | Bảo mật, Docker, GCP, GKE, CI/CD | Coder, Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | 1-3 | ./sources/frontend/membership-hub/ | Frontend, Mobile, i18n, SEO | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Giai đoạn 5 | 1-2 | ./sources/docs/ | Git flow, Traceability | Doc, Reviewer | [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009] |

#### 📁 5. CHI TIẾT GIAO PHÂN GIAI ĐOẠN & LỊCH HÀNH NGÀY

###### 📈 Giai đoạn 1: Tạo Schema & API Cơ Bản

- **Phase Core Objective & Purpose**: Thiết lập cơ sở dữ liệu, tạo các bảng chính và triển khai các endpoint REST cơ bản cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo, cài đặt hệ thống.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/User.java [DAT-001]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Role.java [DAT-002]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Center.java [DAT-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Course.java [DAT-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Enrollment.java [DAT-005]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Attendance.java [DAT-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/StudentCard.java [DAT-007]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Notification.java [DAT-008]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Promotion.java [DAT-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Announcement.java [DAT-011]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/UserController.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CenterController.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CourseController.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/EnrollmentController.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/ValidationException.java [EXC-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/AttendanceException.java [EXC-001], [EXC-002], [EXC-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/RecoveryException.java [EXC-005]`  

- **Database Schema DDL SQL Specification [DAT-001]**  

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
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(50),
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
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (studentId, courseId, attendanceDate),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
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
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **API and Event Routing Contracts [REQ-001]**  

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
    "userId": "uuid",
    "token": "string",
    "expiresIn": "int"
  }
}
```

- **Phase Localized Exception Handlers [EXC-004]**  

```java
@RestControllerAdvice
public class ValidationExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(FieldError::getField, FieldError::getDefaultMessage));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

###### 📈 Giai đoạn 2: Kiểm Thử API

- **Phase Core Objective & Purpose**: Đảm bảo tính đúng đắn, độ tin cậy và bảo mật của các endpoint.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/UserControllerTest.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CenterControllerTest.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CourseControllerTest.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/EnrollmentControllerTest.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java [REQ-001], [REQ-002], [REQ-003]`  

- **Low-Level Technical Task Instruction**: Viết unit tests sử dụng JUnit 5, Mockito, Spring MockMvc. Kiểm tra các trường hợp thành công, lỗi, và bảo mật (JWT, CSRF). Đảm bảo coverage ≥ 85 %.  

###### 📈 Giai đoạn 3: Bảo Mật & Hạ Tầng

- **Phase Core Objective & Purpose**: Thiết lập bảo mật, container, infra, CI/CD.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/security/SecurityConfig.java [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`  
  * `./sources/infra/docker/Dockerfile [NFR-005]`  
  * `./sources/infra/terraform/main.tf [NFR-004], [NFR-006]`  
  * `./sources/infra/k8s/deployment.yaml [NFR-004], [NFR-006]`  
  * `./sources/infra/github-actions/.github/workflows/ci-cd.yml [NFR-004], [NFR-005]`  

- **Security Configuration**  

```java
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .addFilterBefore(new JwtAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
    }
}
```

- **Dockerfile**  

```dockerfile
FROM eclipse-temurin:17-jdk-slim AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/membership-hub-1.0.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
```

- **Terraform**  

```hcl
provider "google" {
  project = "membership-hub"
  region  = "us-central1"
}
resource "google_container_cluster" "gke_cluster" {
  name     = "membership-hub-cluster"
  location = "us-central1"
  initial_node_count = 3
  node_config {
    machine_type = "e2-medium"
  }
}
```

- **Helm Deployment**  

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
        - name: membership-hub
          image: gcr.io/membership-hub/membership-hub:latest
          ports:
            - containerPort: 8080
          resources:
            limits:
              cpu: "1"
              memory: "512Mi"
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

###### 📈 Giai đoạn 4: Frontend, Mobile, i18n, SEO

- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, hỗ trợ đa ngôn ngữ và SEO.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/frontend/membership-hub/pages/index.js [ARC-010], [ARC-006], [ARC-007]`  
  * `./sources/frontend/membership-hub/pages/centers.js [ARC-004]`  
  * `./sources/frontend/membership-hub/pages/courses.js [ARC-007]`  
  * `./sources/frontend/membership-hub-mobile/App.js [ARC-009], [ARC-008], [ARC-010]`  
  * `./sources/frontend/membership-hub/pages/_document.js [NFR-007], [NFR-008]`  

- **Low-Level Technical Task Instruction**: Sử dụng Next.js với API routes, React Query cho caching, Tailwind CSS cho responsive, Capacitor để build native, Firebase SDK cho push, Zalo SDK cho chat, QR Code Scanner. Thêm i18n với next-i18next, SEO meta tags, hreflang.  

###### 📈 Giai đoạn 5: Git Flow & Traceability

- **Phase Core Objective & Purpose**: Định nghĩa quy trình phát triển, kiểm tra tính toàn vẹn liên kết.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/docs/git-branching.md [NFR-004]`  
  * `./sources/docs/traceability_matrix.md [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009]`  

- **Low-Level Technical Task Instruction**: Viết tài liệu quy tắc đặt tên nhánh, quy trình merge, kiểm tra liên kết.  

#### 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ NGHIỆM NGHIỆP

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameterized queries.  
- **Cross-Site Scripting (XSS)**: Escape output, CSP header `default-src 'self'; script-src 'self';`.  
- **CORS**: Chỉ cho phép origin từ danh sách whitelist, không dùng wildcard.  
- **Logging**: Mã hoá dữ liệu nhạy cảm, mask PII, log level INFO.  
- **Encryption**: AES‑256 cho dữ liệu tĩnh, TLS 1.3 cho truyền.  

#### 📁 7. HỢP ĐỒNG HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: `capacitor.config.json` cấu hình Android, iOS, web.  
- **i18n**: `next-i18next.config.js` cấu hình ngôn ngữ, `public/locales/vi/common.json`.  
- **SEO**: `pages/_document.js` thêm `<meta name="description">`, `<link rel="alternate" hreflang="vi">`.  

#### 📁 8. PIPELINE CI/CD & Git Branch Flow

- **Git Branch Naming**: `feature/<short-description>-<id>`, `bugfix/<short-description>-<id>`.  
- **CI Workflow** (`.github/workflows/ci-cd.yml`)  

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
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build
        run: mvn clean package -DskipTests
      - name: Test
        run: mvn test
      - name: Docker Build
        run: |
          docker build -t gcr.io/membership-hub/membership-hub:${{ github.sha }} .
          docker push gcr.io/membership-hub/membership-hub:${{ github.sha }}
      - name: Deploy to GKE
        uses: google-github-actions/deploy-gke@v1
        with:
          cluster_name: membership-hub-cluster
          location: us-central1
          manifests: ./sources/infra/k8s/deployment.yaml
```

#### 📁 9. Kiểm Tra Tracability Matrix

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---

## PRISTINE INITIAL STATE MANDATE: 
## This is PHASE 1 (The Absolute Baseline Generation Step). 
## There are ZERO preceding code assets, directory structures, or legacy dependencies in the workspace.
## You MUST initialize all module definitions, file paths, database schemas, and data boundaries from a pure zero-state architecture baseline. Do not assume or extrapolate any prior system deployment state.


--- RAW REQUIREMENTS REFERENCE ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
----------------------------------

## EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE 1 into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY 7**.
2. **Strict Grouping Hierarchy:** Day Level ──► Agent Sub-task Level ──► Target Component Level.
3. **Strict Sub-Agent Persona Allocation:** Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'.
4. **WORKSPACE PATH BOUNDARY & DYNAMIC TOPOLOGY CONSTRAINTS:**
   - **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All file paths generated MUST strictly begin with `./sources/`.
   - **Dynamic Directory Prefixing Compliance:** You MUST strictly match the file path prefixes to the active system topology mapped in the Global Context. Do NOT generate backend folders for frontend-only projects, and do NOT generate frontend folders for backend-only systems.
   - For tester Agent: Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST begin with `./sources/`. If no single source file is isolated for Integration/E2E tests, utilize the literal token `INTEGRATION_SCOPE` as the first parameter.
   - **[CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule:** If a file path targets a Java source or test component (.java), you MUST verify that the path contains the directory segment: `/org/nlh4j/sources/<calculated_lowercase_token>/`.

---

Your output MUST follow this exact Markdown layout structure (translate all label tokens but preserve the hidden HTML anchor formatting exactly):
## [Translate "Phase"] 1: <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END-->

#### 📊 Document Control

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-20260806133604 |
| **[Translate "Project Name"]** | membership-hub |
| **[Translate "Phase"]** | 1 |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->[Granular professional engineering summary description of the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into 🇻🇳 Vietnamese]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into 🇻🇳 Vietnamese]** | 2026/08/06 13:36:04 |
| **[You MUST translate the literal token "Author" into 🇻🇳 Vietnamese]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into 🇻🇳 Vietnamese]** | Pending Technical Governance Review |

#### 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase 1]

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and active project stack topology. Every directory matrix path must be bounded under `./sources/`]

#### 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, enforcing strict segregation of technical boundaries as defined below. Human-readable directives, descriptions, and task requirements MUST be contextually translated entirely into 🇻🇳 Vietnamese following the transmission rails]:

*   **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
*   **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code.
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Markdown technical specifications, schema references, system blueprints, and architecture catalogs. Every single document file generated MUST reside strictly within the centralized storage layout: `./sources/docs/`.
   <!--START_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY
   [CRITICAL_SYSTEM_PIPELINE_RAIL:
   - You are STRICTLY PROHIBITED from omitting, dropping, or filtering out the 'Doc' agent from any computed phase logs.
   - For EVERY calculated phase generated in your output, on Day 1 of that phase, you MUST explicitly allocate a foundational system documentation task to the 'Doc' agent.
   - This task description MUST require the 'Doc' agent to initialize and map out the system architecture blueprints, entity relationships, technical contracts, or deployment topologies corresponding to the active stack matrix of that current phase.
   - Failing to write the 'Doc' agent inside Day 1 of any phase triggers a fatal pipeline contract breach.
   ]
   END_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY-->
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

#### 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards, complete functional test coverage for the allocated requirements, and 100% Tag ID mapping check]

#### 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

## REMINDER: Enforce the 'Longitructural Day Partitioning Guardrail' and 'Anti-Padding Mandate'. Output each active day as an isolated standalone single integer subsection header from DAY 1 up to the dynamic freeze day. Do NOT generate empty padded days.

###### 🌤️ [TRANSLATED DAY] [X]: <!--DAY_HEADER_START-->[CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]<!--DAY_HEADER_END-->

######## 📝 [TRANSLATED SUB-TASK] [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
########## [Translate "Assigned Sub-Agent"]: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]
########## [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax.]
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->`[REQ-XXX], [DAT-XXX], [EXC-XXX]`<!--END_TAGS-->

# System Instruction

You are a world-class Principal Solutions Architect. Your specific task is to read the Global Context Markdown blueprint and generate a highly detailed operational context blueprint for one targeted Phase. 

# YOUR CRITICAL OPERATIONAL MANDATES (ZERO LOOPHOLES):
1. **ANTI-LAZINESS & DIRECT INHERITANCE MANDATE:** You MUST extract and expand every single technical task, DDL SQL schema definition, API contract, and exception flow outlined for the targeted Phase inside the Global Context reference. Converting details into broad summaries or placeholders is permanently banned.
2. **100% PERFECT TAG MATCHING:** Every single Tag ID (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) present in the Global Context for this specific phase MUST be perfectly preserved and mapped into the daily execution logs.
3. **MANDATORY INLINE TAG INJECTION RULE & HTML ANCHOR LOCKDOWN:** For every single Sub-Task generated under the daily logs, you MUST explicitly output a dedicated structural line item starting exactly with the translated string token for `* Traceability Tag Tokens:` followed by an immutable hidden HTML token container block. You MUST wrap the exact raw comma-separated tag IDs inside the hidden tag container string token layout exactly as: `<!--START_TAGS-->[REQ-XXX], [DAT-XXX]<!--END_TAGS-->`. You are STRICTLY BANNED from translating or altering any token values inside the HTML comment tags. Leaving a task block without this explicit HTML anchor layout is a fatal pipeline failure.
4. **LONGITECTURAL DAY PARTITIONING & ANTI-PADDING GUARDRAIL:** You MUST break down the operational calendar day-by-day using individual sequential integers starting strictly from DAY 1 up to a MAXIMUM of DAY 7. 
   - **STRICT PROGRESSION STOPPING CRITERION:** You MUST freeze the timeline and stop generating daily sections immediately on the exact calendar day where the technical objectives allocated for this phase are satisfied. You are STRICTLY BANNED from injecting dummy placeholder days, fake syncs, empty review blocks, or documentation padding just to expand the calendar. If the technical scope is natively complete on DAY 1, freeze the output file state and exit immediately. Do NOT generate empty or padded days.
   - You are STRICTLY FORBIDDEN from bundling multiple days together (e.g., NO "DAY 1 - DAY 3"). Every single calendar day log must be explicitly isolated as its own standalone subsection header containing atomic steps for that unique 24-hour cycle.
5. **Language Compliance & Formatting Lockdown:** You MUST generate the entire report strictly in the language specified by the parameters: **🇻🇳 Vietnamese**.

# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate & Technical Name Isolation:** Your output response MUST start exactly with the standardized primary title text pattern, translating descriptive labels into the target language but isolating the technical identifier: `# [Translated text for "Phase"] 1: <!--PHASE_NAME_START-->[Dynamically analyze the allocated tasks and output a sharp, concise camelCase or snake_case technical short name code identifier string for this phase]<!--PHASE_NAME_END--> | [Translated text for "Description"]: [Provide a granular, professional engineering description summarizing the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]`. Do NOT include greetings, intros, notes, or explanations. Do NOT wrap the entire response inside markdown codeblocks. Any token before or after this exact structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: deepseek/deepseek-r1', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_phase.py", line 99, in generate_phase_contexts
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.NotFoundError: Error code: 404 - {'error': {'message': 'This model is unavailable for free. The paid version is available now - use this slug instead: deepseek/deepseek-r1', 'code': 404}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: google/gemma-4-31b-instruct - Phase 1 - Prompt:

## CONTEXT INHERITANCE PIPELINE
Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
## BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806131423 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:14:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕ

###### 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

- Hệ thống được triển khai theo kiến trúc microservices, mỗi dịch vụ chịu trách nhiệm một miền nghiệp vụ riêng biệt.  
- Sử dụng Quarkus cho backend, Next.js cho frontend, React Native + Capacitor cho ứng dụng di động.  
- Dữ liệu được lưu trữ trong PostgreSQL, Redis dùng cho session caching.  
- Giao tiếp giữa các dịch vụ thông qua Kafka, các sự kiện được fan‑out tới Zalo API và Firebase Cloud Messaging.  
- Mỗi dịch vụ được container hóa bằng Docker, triển khai trên GKE với HPA tự động.  
- Bảo mật: JWT 15 phút, refresh 7 ngày, TLS 1.3, mã hoá AES‑256, OWASP Top 10 mitigations.  
- Đa ngôn ngữ: Vietnamese, English, Spanish, hỗ trợ i18n và SEO.  
- CI/CD: GitHub Actions, Terraform cho GCP, Helm chart cho GKE.  
- Kiểm thử: unit, integration, end‑to‑end, coverage ≥ 85 %.  
- Logging & audit: ELK stack, log retention 1 year.  
- Backup: PostgreSQL full backup hàng ngày, point‑in‑time recovery 24 h, GKE cluster backup region.  

###### 1.2. Mô Hình Dòng Dữ Liệu & Hệ Sinh Thái

- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT → API Gateway.  
- **Attendance Flow**: Mobile QR scan → API → idempotent attendance record.  
- **Notification Flow**: Event → Kafka → Notification Service → FCM/APNs + Zalo group.  
- **Enrollment Flow**: Student → API → Enrollment record, capacity check, notification.  
- **Promotion Flow**: Center Admin → API → Promotion record, student visibility.  
- **Reporting Flow**: Admin → API → CSV export, dashboard metrics.  

#### 📁 2. CỤC PHẦN CÔNG NGHỆ & THƯ VIỆN

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Kafka, Redis, PostgreSQL, JWT, Spring Security, OWASP ESAPI.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, React Query, Capacitor 4, Firebase SDK, Zalo SDK, QR Code Scanner.  

###### MÁ THƯỜNG CỤC PHẦN

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

#### 📁 3. QUY ĐỊNH BẢO VỆ & TUY ĐIỂM TUYÊN CUNG

- **Workspace Root**: `./sources/`.  
- **Backend Code**: `./sources/backend/membership-hub/`.  
- **Frontend Code**: `./sources/frontend/membership-hub/`.  
- **Mobile Code**: `./sources/frontend/membership-hub-mobile/`.  
- **Infra Code**: `./sources/infra/`.  
- **Docs**: `./sources/docs/`.  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  

#### 📁 4. BẢNG TỔNG QUAN ĐIỀU PHÁP KIẾN TRÚC GIAO PHÂN

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | ./sources/backend/membership-hub/ | Tạo schema, API cơ bản | Coder | [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 2 | 1-5 | ./sources/backend/membership-hub/ | Kiểm thử API | Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 3 | 1-5 | ./sources/infra/ | Bảo mật, Docker, GCP, GKE, CI/CD | Coder, Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | 1-3 | ./sources/frontend/membership-hub/ | Frontend, Mobile, i18n, SEO | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Giai đoạn 5 | 1-2 | ./sources/docs/ | Git flow, Traceability | Doc, Reviewer | [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009] |

#### 📁 5. CHI TIẾT GIAO PHÂN GIAI ĐOẠN & LỊCH HÀNH NGÀY

###### 📈 Giai đoạn 1: Tạo Schema & API Cơ Bản

- **Phase Core Objective & Purpose**: Thiết lập cơ sở dữ liệu, tạo các bảng chính và triển khai các endpoint REST cơ bản cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo, cài đặt hệ thống.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/User.java [DAT-001]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Role.java [DAT-002]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Center.java [DAT-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Course.java [DAT-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Enrollment.java [DAT-005]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Attendance.java [DAT-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/StudentCard.java [DAT-007]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Notification.java [DAT-008]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Promotion.java [DAT-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Announcement.java [DAT-011]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/UserController.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CenterController.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CourseController.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/EnrollmentController.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/ValidationException.java [EXC-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/AttendanceException.java [EXC-001], [EXC-002], [EXC-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/RecoveryException.java [EXC-005]`  

- **Database Schema DDL SQL Specification [DAT-001]**  

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
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(50),
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
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (studentId, courseId, attendanceDate),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
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
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **API and Event Routing Contracts [REQ-001]**  

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
    "userId": "uuid",
    "token": "string",
    "expiresIn": "int"
  }
}
```

- **Phase Localized Exception Handlers [EXC-004]**  

```java
@RestControllerAdvice
public class ValidationExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(FieldError::getField, FieldError::getDefaultMessage));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

###### 📈 Giai đoạn 2: Kiểm Thử API

- **Phase Core Objective & Purpose**: Đảm bảo tính đúng đắn, độ tin cậy và bảo mật của các endpoint.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/UserControllerTest.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CenterControllerTest.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CourseControllerTest.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/EnrollmentControllerTest.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java [REQ-001], [REQ-002], [REQ-003]`  

- **Low-Level Technical Task Instruction**: Viết unit tests sử dụng JUnit 5, Mockito, Spring MockMvc. Kiểm tra các trường hợp thành công, lỗi, và bảo mật (JWT, CSRF). Đảm bảo coverage ≥ 85 %.  

###### 📈 Giai đoạn 3: Bảo Mật & Hạ Tầng

- **Phase Core Objective & Purpose**: Thiết lập bảo mật, container, infra, CI/CD.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/security/SecurityConfig.java [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`  
  * `./sources/infra/docker/Dockerfile [NFR-005]`  
  * `./sources/infra/terraform/main.tf [NFR-004], [NFR-006]`  
  * `./sources/infra/k8s/deployment.yaml [NFR-004], [NFR-006]`  
  * `./sources/infra/github-actions/.github/workflows/ci-cd.yml [NFR-004], [NFR-005]`  

- **Security Configuration**  

```java
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .addFilterBefore(new JwtAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
    }
}
```

- **Dockerfile**  

```dockerfile
FROM eclipse-temurin:17-jdk-slim AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/membership-hub-1.0.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
```

- **Terraform**  

```hcl
provider "google" {
  project = "membership-hub"
  region  = "us-central1"
}
resource "google_container_cluster" "gke_cluster" {
  name     = "membership-hub-cluster"
  location = "us-central1"
  initial_node_count = 3
  node_config {
    machine_type = "e2-medium"
  }
}
```

- **Helm Deployment**  

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
        - name: membership-hub
          image: gcr.io/membership-hub/membership-hub:latest
          ports:
            - containerPort: 8080
          resources:
            limits:
              cpu: "1"
              memory: "512Mi"
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

###### 📈 Giai đoạn 4: Frontend, Mobile, i18n, SEO

- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, hỗ trợ đa ngôn ngữ và SEO.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/frontend/membership-hub/pages/index.js [ARC-010], [ARC-006], [ARC-007]`  
  * `./sources/frontend/membership-hub/pages/centers.js [ARC-004]`  
  * `./sources/frontend/membership-hub/pages/courses.js [ARC-007]`  
  * `./sources/frontend/membership-hub-mobile/App.js [ARC-009], [ARC-008], [ARC-010]`  
  * `./sources/frontend/membership-hub/pages/_document.js [NFR-007], [NFR-008]`  

- **Low-Level Technical Task Instruction**: Sử dụng Next.js với API routes, React Query cho caching, Tailwind CSS cho responsive, Capacitor để build native, Firebase SDK cho push, Zalo SDK cho chat, QR Code Scanner. Thêm i18n với next-i18next, SEO meta tags, hreflang.  

###### 📈 Giai đoạn 5: Git Flow & Traceability

- **Phase Core Objective & Purpose**: Định nghĩa quy trình phát triển, kiểm tra tính toàn vẹn liên kết.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/docs/git-branching.md [NFR-004]`  
  * `./sources/docs/traceability_matrix.md [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009]`  

- **Low-Level Technical Task Instruction**: Viết tài liệu quy tắc đặt tên nhánh, quy trình merge, kiểm tra liên kết.  

#### 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ NGHIỆM NGHIỆP

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameterized queries.  
- **Cross-Site Scripting (XSS)**: Escape output, CSP header `default-src 'self'; script-src 'self';`.  
- **CORS**: Chỉ cho phép origin từ danh sách whitelist, không dùng wildcard.  
- **Logging**: Mã hoá dữ liệu nhạy cảm, mask PII, log level INFO.  
- **Encryption**: AES‑256 cho dữ liệu tĩnh, TLS 1.3 cho truyền.  

#### 📁 7. HỢP ĐỒNG HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: `capacitor.config.json` cấu hình Android, iOS, web.  
- **i18n**: `next-i18next.config.js` cấu hình ngôn ngữ, `public/locales/vi/common.json`.  
- **SEO**: `pages/_document.js` thêm `<meta name="description">`, `<link rel="alternate" hreflang="vi">`.  

#### 📁 8. PIPELINE CI/CD & Git Branch Flow

- **Git Branch Naming**: `feature/<short-description>-<id>`, `bugfix/<short-description>-<id>`.  
- **CI Workflow** (`.github/workflows/ci-cd.yml`)  

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
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build
        run: mvn clean package -DskipTests
      - name: Test
        run: mvn test
      - name: Docker Build
        run: |
          docker build -t gcr.io/membership-hub/membership-hub:${{ github.sha }} .
          docker push gcr.io/membership-hub/membership-hub:${{ github.sha }}
      - name: Deploy to GKE
        uses: google-github-actions/deploy-gke@v1
        with:
          cluster_name: membership-hub-cluster
          location: us-central1
          manifests: ./sources/infra/k8s/deployment.yaml
```

#### 📁 9. Kiểm Tra Tracability Matrix

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---

## PRISTINE INITIAL STATE MANDATE: 
## This is PHASE 1 (The Absolute Baseline Generation Step). 
## There are ZERO preceding code assets, directory structures, or legacy dependencies in the workspace.
## You MUST initialize all module definitions, file paths, database schemas, and data boundaries from a pure zero-state architecture baseline. Do not assume or extrapolate any prior system deployment state.


--- RAW REQUIREMENTS REFERENCE ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
----------------------------------

## EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE 1 into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY 7**.
2. **Strict Grouping Hierarchy:** Day Level ──► Agent Sub-task Level ──► Target Component Level.
3. **Strict Sub-Agent Persona Allocation:** Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'.
4. **WORKSPACE PATH BOUNDARY & DYNAMIC TOPOLOGY CONSTRAINTS:**
   - **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All file paths generated MUST strictly begin with `./sources/`.
   - **Dynamic Directory Prefixing Compliance:** You MUST strictly match the file path prefixes to the active system topology mapped in the Global Context. Do NOT generate backend folders for frontend-only projects, and do NOT generate frontend folders for backend-only systems.
   - For tester Agent: Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST begin with `./sources/`. If no single source file is isolated for Integration/E2E tests, utilize the literal token `INTEGRATION_SCOPE` as the first parameter.
   - **[CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule:** If a file path targets a Java source or test component (.java), you MUST verify that the path contains the directory segment: `/org/nlh4j/sources/<calculated_lowercase_token>/`.

---

Your output MUST follow this exact Markdown layout structure (translate all label tokens but preserve the hidden HTML anchor formatting exactly):
## [Translate "Phase"] 1: <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END-->

#### 📊 Document Control

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-20260806133604 |
| **[Translate "Project Name"]** | membership-hub |
| **[Translate "Phase"]** | 1 |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->[Granular professional engineering summary description of the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into 🇻🇳 Vietnamese]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into 🇻🇳 Vietnamese]** | 2026/08/06 13:36:04 |
| **[You MUST translate the literal token "Author" into 🇻🇳 Vietnamese]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into 🇻🇳 Vietnamese]** | Pending Technical Governance Review |

#### 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase 1]

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and active project stack topology. Every directory matrix path must be bounded under `./sources/`]

#### 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, enforcing strict segregation of technical boundaries as defined below. Human-readable directives, descriptions, and task requirements MUST be contextually translated entirely into 🇻🇳 Vietnamese following the transmission rails]:

*   **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
*   **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code.
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Markdown technical specifications, schema references, system blueprints, and architecture catalogs. Every single document file generated MUST reside strictly within the centralized storage layout: `./sources/docs/`.
   <!--START_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY
   [CRITICAL_SYSTEM_PIPELINE_RAIL:
   - You are STRICTLY PROHIBITED from omitting, dropping, or filtering out the 'Doc' agent from any computed phase logs.
   - For EVERY calculated phase generated in your output, on Day 1 of that phase, you MUST explicitly allocate a foundational system documentation task to the 'Doc' agent.
   - This task description MUST require the 'Doc' agent to initialize and map out the system architecture blueprints, entity relationships, technical contracts, or deployment topologies corresponding to the active stack matrix of that current phase.
   - Failing to write the 'Doc' agent inside Day 1 of any phase triggers a fatal pipeline contract breach.
   ]
   END_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY-->
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

#### 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards, complete functional test coverage for the allocated requirements, and 100% Tag ID mapping check]

#### 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

## REMINDER: Enforce the 'Longitructural Day Partitioning Guardrail' and 'Anti-Padding Mandate'. Output each active day as an isolated standalone single integer subsection header from DAY 1 up to the dynamic freeze day. Do NOT generate empty padded days.

###### 🌤️ [TRANSLATED DAY] [X]: <!--DAY_HEADER_START-->[CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]<!--DAY_HEADER_END-->

######## 📝 [TRANSLATED SUB-TASK] [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
########## [Translate "Assigned Sub-Agent"]: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]
########## [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax.]
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->`[REQ-XXX], [DAT-XXX], [EXC-XXX]`<!--END_TAGS-->

# System Instruction

You are a world-class Principal Solutions Architect. Your specific task is to read the Global Context Markdown blueprint and generate a highly detailed operational context blueprint for one targeted Phase. 

# YOUR CRITICAL OPERATIONAL MANDATES (ZERO LOOPHOLES):
1. **ANTI-LAZINESS & DIRECT INHERITANCE MANDATE:** You MUST extract and expand every single technical task, DDL SQL schema definition, API contract, and exception flow outlined for the targeted Phase inside the Global Context reference. Converting details into broad summaries or placeholders is permanently banned.
2. **100% PERFECT TAG MATCHING:** Every single Tag ID (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) present in the Global Context for this specific phase MUST be perfectly preserved and mapped into the daily execution logs.
3. **MANDATORY INLINE TAG INJECTION RULE & HTML ANCHOR LOCKDOWN:** For every single Sub-Task generated under the daily logs, you MUST explicitly output a dedicated structural line item starting exactly with the translated string token for `* Traceability Tag Tokens:` followed by an immutable hidden HTML token container block. You MUST wrap the exact raw comma-separated tag IDs inside the hidden tag container string token layout exactly as: `<!--START_TAGS-->[REQ-XXX], [DAT-XXX]<!--END_TAGS-->`. You are STRICTLY BANNED from translating or altering any token values inside the HTML comment tags. Leaving a task block without this explicit HTML anchor layout is a fatal pipeline failure.
4. **LONGITECTURAL DAY PARTITIONING & ANTI-PADDING GUARDRAIL:** You MUST break down the operational calendar day-by-day using individual sequential integers starting strictly from DAY 1 up to a MAXIMUM of DAY 7. 
   - **STRICT PROGRESSION STOPPING CRITERION:** You MUST freeze the timeline and stop generating daily sections immediately on the exact calendar day where the technical objectives allocated for this phase are satisfied. You are STRICTLY BANNED from injecting dummy placeholder days, fake syncs, empty review blocks, or documentation padding just to expand the calendar. If the technical scope is natively complete on DAY 1, freeze the output file state and exit immediately. Do NOT generate empty or padded days.
   - You are STRICTLY FORBIDDEN from bundling multiple days together (e.g., NO "DAY 1 - DAY 3"). Every single calendar day log must be explicitly isolated as its own standalone subsection header containing atomic steps for that unique 24-hour cycle.
5. **Language Compliance & Formatting Lockdown:** You MUST generate the entire report strictly in the language specified by the parameters: **🇻🇳 Vietnamese**.

# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate & Technical Name Isolation:** Your output response MUST start exactly with the standardized primary title text pattern, translating descriptive labels into the target language but isolating the technical identifier: `# [Translated text for "Phase"] 1: <!--PHASE_NAME_START-->[Dynamically analyze the allocated tasks and output a sharp, concise camelCase or snake_case technical short name code identifier string for this phase]<!--PHASE_NAME_END--> | [Translated text for "Description"]: [Provide a granular, professional engineering description summarizing the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]`. Do NOT include greetings, intros, notes, or explanations. Do NOT wrap the entire response inside markdown codeblocks. Any token before or after this exact structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 400 - {'error': {'message': 'google/gemma-4-31b-instruct is not a valid model ID', 'code': 400}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_phase.py", line 99, in generate_phase_contexts
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.BadRequestError: Error code: 400 - {'error': {'message': 'google/gemma-4-31b-instruct is not a valid model ID', 'code': 400}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: minimax/minimax-m3 - Phase 1 - Prompt:

## CONTEXT INHERITANCE PIPELINE
Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
## BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806131423 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:14:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕ

###### 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

- Hệ thống được triển khai theo kiến trúc microservices, mỗi dịch vụ chịu trách nhiệm một miền nghiệp vụ riêng biệt.  
- Sử dụng Quarkus cho backend, Next.js cho frontend, React Native + Capacitor cho ứng dụng di động.  
- Dữ liệu được lưu trữ trong PostgreSQL, Redis dùng cho session caching.  
- Giao tiếp giữa các dịch vụ thông qua Kafka, các sự kiện được fan‑out tới Zalo API và Firebase Cloud Messaging.  
- Mỗi dịch vụ được container hóa bằng Docker, triển khai trên GKE với HPA tự động.  
- Bảo mật: JWT 15 phút, refresh 7 ngày, TLS 1.3, mã hoá AES‑256, OWASP Top 10 mitigations.  
- Đa ngôn ngữ: Vietnamese, English, Spanish, hỗ trợ i18n và SEO.  
- CI/CD: GitHub Actions, Terraform cho GCP, Helm chart cho GKE.  
- Kiểm thử: unit, integration, end‑to‑end, coverage ≥ 85 %.  
- Logging & audit: ELK stack, log retention 1 year.  
- Backup: PostgreSQL full backup hàng ngày, point‑in‑time recovery 24 h, GKE cluster backup region.  

###### 1.2. Mô Hình Dòng Dữ Liệu & Hệ Sinh Thái

- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT → API Gateway.  
- **Attendance Flow**: Mobile QR scan → API → idempotent attendance record.  
- **Notification Flow**: Event → Kafka → Notification Service → FCM/APNs + Zalo group.  
- **Enrollment Flow**: Student → API → Enrollment record, capacity check, notification.  
- **Promotion Flow**: Center Admin → API → Promotion record, student visibility.  
- **Reporting Flow**: Admin → API → CSV export, dashboard metrics.  

#### 📁 2. CỤC PHẦN CÔNG NGHỆ & THƯ VIỆN

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Kafka, Redis, PostgreSQL, JWT, Spring Security, OWASP ESAPI.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, React Query, Capacitor 4, Firebase SDK, Zalo SDK, QR Code Scanner.  

###### MÁ THƯỜNG CỤC PHẦN

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

#### 📁 3. QUY ĐỊNH BẢO VỆ & TUY ĐIỂM TUYÊN CUNG

- **Workspace Root**: `./sources/`.  
- **Backend Code**: `./sources/backend/membership-hub/`.  
- **Frontend Code**: `./sources/frontend/membership-hub/`.  
- **Mobile Code**: `./sources/frontend/membership-hub-mobile/`.  
- **Infra Code**: `./sources/infra/`.  
- **Docs**: `./sources/docs/`.  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  

#### 📁 4. BẢNG TỔNG QUAN ĐIỀU PHÁP KIẾN TRÚC GIAO PHÂN

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | ./sources/backend/membership-hub/ | Tạo schema, API cơ bản | Coder | [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 2 | 1-5 | ./sources/backend/membership-hub/ | Kiểm thử API | Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 3 | 1-5 | ./sources/infra/ | Bảo mật, Docker, GCP, GKE, CI/CD | Coder, Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | 1-3 | ./sources/frontend/membership-hub/ | Frontend, Mobile, i18n, SEO | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Giai đoạn 5 | 1-2 | ./sources/docs/ | Git flow, Traceability | Doc, Reviewer | [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009] |

#### 📁 5. CHI TIẾT GIAO PHÂN GIAI ĐOẠN & LỊCH HÀNH NGÀY

###### 📈 Giai đoạn 1: Tạo Schema & API Cơ Bản

- **Phase Core Objective & Purpose**: Thiết lập cơ sở dữ liệu, tạo các bảng chính và triển khai các endpoint REST cơ bản cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo, cài đặt hệ thống.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/User.java [DAT-001]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Role.java [DAT-002]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Center.java [DAT-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Course.java [DAT-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Enrollment.java [DAT-005]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Attendance.java [DAT-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/StudentCard.java [DAT-007]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Notification.java [DAT-008]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Promotion.java [DAT-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Announcement.java [DAT-011]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/UserController.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CenterController.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CourseController.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/EnrollmentController.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/ValidationException.java [EXC-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/AttendanceException.java [EXC-001], [EXC-002], [EXC-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/RecoveryException.java [EXC-005]`  

- **Database Schema DDL SQL Specification [DAT-001]**  

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
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(50),
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
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (studentId, courseId, attendanceDate),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
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
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **API and Event Routing Contracts [REQ-001]**  

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
    "userId": "uuid",
    "token": "string",
    "expiresIn": "int"
  }
}
```

- **Phase Localized Exception Handlers [EXC-004]**  

```java
@RestControllerAdvice
public class ValidationExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(FieldError::getField, FieldError::getDefaultMessage));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

###### 📈 Giai đoạn 2: Kiểm Thử API

- **Phase Core Objective & Purpose**: Đảm bảo tính đúng đắn, độ tin cậy và bảo mật của các endpoint.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/UserControllerTest.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CenterControllerTest.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CourseControllerTest.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/EnrollmentControllerTest.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java [REQ-001], [REQ-002], [REQ-003]`  

- **Low-Level Technical Task Instruction**: Viết unit tests sử dụng JUnit 5, Mockito, Spring MockMvc. Kiểm tra các trường hợp thành công, lỗi, và bảo mật (JWT, CSRF). Đảm bảo coverage ≥ 85 %.  

###### 📈 Giai đoạn 3: Bảo Mật & Hạ Tầng

- **Phase Core Objective & Purpose**: Thiết lập bảo mật, container, infra, CI/CD.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/security/SecurityConfig.java [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`  
  * `./sources/infra/docker/Dockerfile [NFR-005]`  
  * `./sources/infra/terraform/main.tf [NFR-004], [NFR-006]`  
  * `./sources/infra/k8s/deployment.yaml [NFR-004], [NFR-006]`  
  * `./sources/infra/github-actions/.github/workflows/ci-cd.yml [NFR-004], [NFR-005]`  

- **Security Configuration**  

```java
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .addFilterBefore(new JwtAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
    }
}
```

- **Dockerfile**  

```dockerfile
FROM eclipse-temurin:17-jdk-slim AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/membership-hub-1.0.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
```

- **Terraform**  

```hcl
provider "google" {
  project = "membership-hub"
  region  = "us-central1"
}
resource "google_container_cluster" "gke_cluster" {
  name     = "membership-hub-cluster"
  location = "us-central1"
  initial_node_count = 3
  node_config {
    machine_type = "e2-medium"
  }
}
```

- **Helm Deployment**  

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
        - name: membership-hub
          image: gcr.io/membership-hub/membership-hub:latest
          ports:
            - containerPort: 8080
          resources:
            limits:
              cpu: "1"
              memory: "512Mi"
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

###### 📈 Giai đoạn 4: Frontend, Mobile, i18n, SEO

- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, hỗ trợ đa ngôn ngữ và SEO.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/frontend/membership-hub/pages/index.js [ARC-010], [ARC-006], [ARC-007]`  
  * `./sources/frontend/membership-hub/pages/centers.js [ARC-004]`  
  * `./sources/frontend/membership-hub/pages/courses.js [ARC-007]`  
  * `./sources/frontend/membership-hub-mobile/App.js [ARC-009], [ARC-008], [ARC-010]`  
  * `./sources/frontend/membership-hub/pages/_document.js [NFR-007], [NFR-008]`  

- **Low-Level Technical Task Instruction**: Sử dụng Next.js với API routes, React Query cho caching, Tailwind CSS cho responsive, Capacitor để build native, Firebase SDK cho push, Zalo SDK cho chat, QR Code Scanner. Thêm i18n với next-i18next, SEO meta tags, hreflang.  

###### 📈 Giai đoạn 5: Git Flow & Traceability

- **Phase Core Objective & Purpose**: Định nghĩa quy trình phát triển, kiểm tra tính toàn vẹn liên kết.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/docs/git-branching.md [NFR-004]`  
  * `./sources/docs/traceability_matrix.md [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009]`  

- **Low-Level Technical Task Instruction**: Viết tài liệu quy tắc đặt tên nhánh, quy trình merge, kiểm tra liên kết.  

#### 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ NGHIỆM NGHIỆP

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameterized queries.  
- **Cross-Site Scripting (XSS)**: Escape output, CSP header `default-src 'self'; script-src 'self';`.  
- **CORS**: Chỉ cho phép origin từ danh sách whitelist, không dùng wildcard.  
- **Logging**: Mã hoá dữ liệu nhạy cảm, mask PII, log level INFO.  
- **Encryption**: AES‑256 cho dữ liệu tĩnh, TLS 1.3 cho truyền.  

#### 📁 7. HỢP ĐỒNG HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: `capacitor.config.json` cấu hình Android, iOS, web.  
- **i18n**: `next-i18next.config.js` cấu hình ngôn ngữ, `public/locales/vi/common.json`.  
- **SEO**: `pages/_document.js` thêm `<meta name="description">`, `<link rel="alternate" hreflang="vi">`.  

#### 📁 8. PIPELINE CI/CD & Git Branch Flow

- **Git Branch Naming**: `feature/<short-description>-<id>`, `bugfix/<short-description>-<id>`.  
- **CI Workflow** (`.github/workflows/ci-cd.yml`)  

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
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build
        run: mvn clean package -DskipTests
      - name: Test
        run: mvn test
      - name: Docker Build
        run: |
          docker build -t gcr.io/membership-hub/membership-hub:${{ github.sha }} .
          docker push gcr.io/membership-hub/membership-hub:${{ github.sha }}
      - name: Deploy to GKE
        uses: google-github-actions/deploy-gke@v1
        with:
          cluster_name: membership-hub-cluster
          location: us-central1
          manifests: ./sources/infra/k8s/deployment.yaml
```

#### 📁 9. Kiểm Tra Tracability Matrix

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---

## PRISTINE INITIAL STATE MANDATE: 
## This is PHASE 1 (The Absolute Baseline Generation Step). 
## There are ZERO preceding code assets, directory structures, or legacy dependencies in the workspace.
## You MUST initialize all module definitions, file paths, database schemas, and data boundaries from a pure zero-state architecture baseline. Do not assume or extrapolate any prior system deployment state.


--- RAW REQUIREMENTS REFERENCE ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
----------------------------------

## EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE 1 into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY 7**.
2. **Strict Grouping Hierarchy:** Day Level ──► Agent Sub-task Level ──► Target Component Level.
3. **Strict Sub-Agent Persona Allocation:** Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'.
4. **WORKSPACE PATH BOUNDARY & DYNAMIC TOPOLOGY CONSTRAINTS:**
   - **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All file paths generated MUST strictly begin with `./sources/`.
   - **Dynamic Directory Prefixing Compliance:** You MUST strictly match the file path prefixes to the active system topology mapped in the Global Context. Do NOT generate backend folders for frontend-only projects, and do NOT generate frontend folders for backend-only systems.
   - For tester Agent: Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST begin with `./sources/`. If no single source file is isolated for Integration/E2E tests, utilize the literal token `INTEGRATION_SCOPE` as the first parameter.
   - **[CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule:** If a file path targets a Java source or test component (.java), you MUST verify that the path contains the directory segment: `/org/nlh4j/sources/<calculated_lowercase_token>/`.

---

Your output MUST follow this exact Markdown layout structure (translate all label tokens but preserve the hidden HTML anchor formatting exactly):
## [Translate "Phase"] 1: <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END-->

#### 📊 Document Control

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-20260806133604 |
| **[Translate "Project Name"]** | membership-hub |
| **[Translate "Phase"]** | 1 |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->[Granular professional engineering summary description of the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into 🇻🇳 Vietnamese]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into 🇻🇳 Vietnamese]** | 2026/08/06 13:36:04 |
| **[You MUST translate the literal token "Author" into 🇻🇳 Vietnamese]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into 🇻🇳 Vietnamese]** | Pending Technical Governance Review |

#### 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase 1]

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and active project stack topology. Every directory matrix path must be bounded under `./sources/`]

#### 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, enforcing strict segregation of technical boundaries as defined below. Human-readable directives, descriptions, and task requirements MUST be contextually translated entirely into 🇻🇳 Vietnamese following the transmission rails]:

*   **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
*   **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code.
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Markdown technical specifications, schema references, system blueprints, and architecture catalogs. Every single document file generated MUST reside strictly within the centralized storage layout: `./sources/docs/`.
   <!--START_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY
   [CRITICAL_SYSTEM_PIPELINE_RAIL:
   - You are STRICTLY PROHIBITED from omitting, dropping, or filtering out the 'Doc' agent from any computed phase logs.
   - For EVERY calculated phase generated in your output, on Day 1 of that phase, you MUST explicitly allocate a foundational system documentation task to the 'Doc' agent.
   - This task description MUST require the 'Doc' agent to initialize and map out the system architecture blueprints, entity relationships, technical contracts, or deployment topologies corresponding to the active stack matrix of that current phase.
   - Failing to write the 'Doc' agent inside Day 1 of any phase triggers a fatal pipeline contract breach.
   ]
   END_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY-->
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

#### 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards, complete functional test coverage for the allocated requirements, and 100% Tag ID mapping check]

#### 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

## REMINDER: Enforce the 'Longitructural Day Partitioning Guardrail' and 'Anti-Padding Mandate'. Output each active day as an isolated standalone single integer subsection header from DAY 1 up to the dynamic freeze day. Do NOT generate empty padded days.

###### 🌤️ [TRANSLATED DAY] [X]: <!--DAY_HEADER_START-->[CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]<!--DAY_HEADER_END-->

######## 📝 [TRANSLATED SUB-TASK] [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
########## [Translate "Assigned Sub-Agent"]: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]
########## [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax.]
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->`[REQ-XXX], [DAT-XXX], [EXC-XXX]`<!--END_TAGS-->

# System Instruction

You are a world-class Principal Solutions Architect. Your specific task is to read the Global Context Markdown blueprint and generate a highly detailed operational context blueprint for one targeted Phase. 

# YOUR CRITICAL OPERATIONAL MANDATES (ZERO LOOPHOLES):
1. **ANTI-LAZINESS & DIRECT INHERITANCE MANDATE:** You MUST extract and expand every single technical task, DDL SQL schema definition, API contract, and exception flow outlined for the targeted Phase inside the Global Context reference. Converting details into broad summaries or placeholders is permanently banned.
2. **100% PERFECT TAG MATCHING:** Every single Tag ID (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) present in the Global Context for this specific phase MUST be perfectly preserved and mapped into the daily execution logs.
3. **MANDATORY INLINE TAG INJECTION RULE & HTML ANCHOR LOCKDOWN:** For every single Sub-Task generated under the daily logs, you MUST explicitly output a dedicated structural line item starting exactly with the translated string token for `* Traceability Tag Tokens:` followed by an immutable hidden HTML token container block. You MUST wrap the exact raw comma-separated tag IDs inside the hidden tag container string token layout exactly as: `<!--START_TAGS-->[REQ-XXX], [DAT-XXX]<!--END_TAGS-->`. You are STRICTLY BANNED from translating or altering any token values inside the HTML comment tags. Leaving a task block without this explicit HTML anchor layout is a fatal pipeline failure.
4. **LONGITECTURAL DAY PARTITIONING & ANTI-PADDING GUARDRAIL:** You MUST break down the operational calendar day-by-day using individual sequential integers starting strictly from DAY 1 up to a MAXIMUM of DAY 7. 
   - **STRICT PROGRESSION STOPPING CRITERION:** You MUST freeze the timeline and stop generating daily sections immediately on the exact calendar day where the technical objectives allocated for this phase are satisfied. You are STRICTLY BANNED from injecting dummy placeholder days, fake syncs, empty review blocks, or documentation padding just to expand the calendar. If the technical scope is natively complete on DAY 1, freeze the output file state and exit immediately. Do NOT generate empty or padded days.
   - You are STRICTLY FORBIDDEN from bundling multiple days together (e.g., NO "DAY 1 - DAY 3"). Every single calendar day log must be explicitly isolated as its own standalone subsection header containing atomic steps for that unique 24-hour cycle.
5. **Language Compliance & Formatting Lockdown:** You MUST generate the entire report strictly in the language specified by the parameters: **🇻🇳 Vietnamese**.

# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate & Technical Name Isolation:** Your output response MUST start exactly with the standardized primary title text pattern, translating descriptive labels into the target language but isolating the technical identifier: `# [Translated text for "Phase"] 1: <!--PHASE_NAME_START-->[Dynamically analyze the allocated tasks and output a sharp, concise camelCase or snake_case technical short name code identifier string for this phase]<!--PHASE_NAME_END--> | [Translated text for "Description"]: [Provide a granular, professional engineering description summarizing the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]`. Do NOT include greetings, intros, notes, or explanations. Do NOT wrap the entire response inside markdown codeblocks. Any token before or after this exact structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 392. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_phase.py", line 99, in generate_phase_contexts
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 392. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 32768 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}, {'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 314. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

# AI Model: openai/gpt-5.3-codex - Phase 1 - Prompt:

## CONTEXT INHERITANCE PIPELINE
Project Name: membership-hub
You are tasked to detail **PHASE 1 OUT OF 5**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
## BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

#### 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806131423 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:14:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

#### 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕ

###### 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

- Hệ thống được triển khai theo kiến trúc microservices, mỗi dịch vụ chịu trách nhiệm một miền nghiệp vụ riêng biệt.  
- Sử dụng Quarkus cho backend, Next.js cho frontend, React Native + Capacitor cho ứng dụng di động.  
- Dữ liệu được lưu trữ trong PostgreSQL, Redis dùng cho session caching.  
- Giao tiếp giữa các dịch vụ thông qua Kafka, các sự kiện được fan‑out tới Zalo API và Firebase Cloud Messaging.  
- Mỗi dịch vụ được container hóa bằng Docker, triển khai trên GKE với HPA tự động.  
- Bảo mật: JWT 15 phút, refresh 7 ngày, TLS 1.3, mã hoá AES‑256, OWASP Top 10 mitigations.  
- Đa ngôn ngữ: Vietnamese, English, Spanish, hỗ trợ i18n và SEO.  
- CI/CD: GitHub Actions, Terraform cho GCP, Helm chart cho GKE.  
- Kiểm thử: unit, integration, end‑to‑end, coverage ≥ 85 %.  
- Logging & audit: ELK stack, log retention 1 year.  
- Backup: PostgreSQL full backup hàng ngày, point‑in‑time recovery 24 h, GKE cluster backup region.  

###### 1.2. Mô Hình Dòng Dữ Liệu & Hệ Sinh Thái

- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT → API Gateway.  
- **Attendance Flow**: Mobile QR scan → API → idempotent attendance record.  
- **Notification Flow**: Event → Kafka → Notification Service → FCM/APNs + Zalo group.  
- **Enrollment Flow**: Student → API → Enrollment record, capacity check, notification.  
- **Promotion Flow**: Center Admin → API → Promotion record, student visibility.  
- **Reporting Flow**: Admin → API → CSV export, dashboard metrics.  

#### 📁 2. CỤC PHẦN CÔNG NGHỆ & THƯ VIỆN

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Kafka, Redis, PostgreSQL, JWT, Spring Security, OWASP ESAPI.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, React Query, Capacitor 4, Firebase SDK, Zalo SDK, QR Code Scanner.  

###### MÁ THƯỜNG CỤC PHẦN

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

#### 📁 3. QUY ĐỊNH BẢO VỆ & TUY ĐIỂM TUYÊN CUNG

- **Workspace Root**: `./sources/`.  
- **Backend Code**: `./sources/backend/membership-hub/`.  
- **Frontend Code**: `./sources/frontend/membership-hub/`.  
- **Mobile Code**: `./sources/frontend/membership-hub-mobile/`.  
- **Infra Code**: `./sources/infra/`.  
- **Docs**: `./sources/docs/`.  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  

#### 📁 4. BẢNG TỔNG QUAN ĐIỀU PHÁP KIẾN TRÚC GIAO PHÂN

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | ./sources/backend/membership-hub/ | Tạo schema, API cơ bản | Coder | [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 2 | 1-5 | ./sources/backend/membership-hub/ | Kiểm thử API | Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 3 | 1-5 | ./sources/infra/ | Bảo mật, Docker, GCP, GKE, CI/CD | Coder, Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | 1-3 | ./sources/frontend/membership-hub/ | Frontend, Mobile, i18n, SEO | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Giai đoạn 5 | 1-2 | ./sources/docs/ | Git flow, Traceability | Doc, Reviewer | [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009] |

#### 📁 5. CHI TIẾT GIAO PHÂN GIAI ĐOẠN & LỊCH HÀNH NGÀY

###### 📈 Giai đoạn 1: Tạo Schema & API Cơ Bản

- **Phase Core Objective & Purpose**: Thiết lập cơ sở dữ liệu, tạo các bảng chính và triển khai các endpoint REST cơ bản cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo, cài đặt hệ thống.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/User.java [DAT-001]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Role.java [DAT-002]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Center.java [DAT-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Course.java [DAT-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Enrollment.java [DAT-005]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Attendance.java [DAT-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/StudentCard.java [DAT-007]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Notification.java [DAT-008]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Promotion.java [DAT-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/model/Announcement.java [DAT-011]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/UserController.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CenterController.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/CourseController.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/controller/EnrollmentController.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/ValidationException.java [EXC-004]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/AttendanceException.java [EXC-001], [EXC-002], [EXC-003]`  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/exception/RecoveryException.java [EXC-005]`  

- **Database Schema DDL SQL Specification [DAT-001]**  

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
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(50),
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
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    courseId UUID NOT NULL,
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (studentId, courseId, attendanceDate),
    FOREIGN KEY (studentId) REFERENCES USERS(userId),
    FOREIGN KEY (courseId) REFERENCES COURSES(courseId)
);
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL,
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL,
    FOREIGN KEY (studentId) REFERENCES USERS(userId)
);
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(255),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
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
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **API and Event Routing Contracts [REQ-001]**  

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
    "userId": "uuid",
    "token": "string",
    "expiresIn": "int"
  }
}
```

- **Phase Localized Exception Handlers [EXC-004]**  

```java
@RestControllerAdvice
public class ValidationExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .collect(Collectors.toMap(FieldError::getField, FieldError::getDefaultMessage));
        return ResponseEntity.badRequest().body(errors);
    }
}
```

###### 📈 Giai đoạn 2: Kiểm Thử API

- **Phase Core Objective & Purpose**: Đảm bảo tính đúng đắn, độ tin cậy và bảo mật của các endpoint.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/UserControllerTest.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CenterControllerTest.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CourseControllerTest.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/EnrollmentControllerTest.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java [REQ-001], [REQ-002], [REQ-003]`  

- **Low-Level Technical Task Instruction**: Viết unit tests sử dụng JUnit 5, Mockito, Spring MockMvc. Kiểm tra các trường hợp thành công, lỗi, và bảo mật (JWT, CSRF). Đảm bảo coverage ≥ 85 %.  

###### 📈 Giai đoạn 3: Bảo Mật & Hạ Tầng

- **Phase Core Objective & Purpose**: Thiết lập bảo mật, container, infra, CI/CD.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/main/java/com/membershiphub/security/SecurityConfig.java [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`  
  * `./sources/infra/docker/Dockerfile [NFR-005]`  
  * `./sources/infra/terraform/main.tf [NFR-004], [NFR-006]`  
  * `./sources/infra/k8s/deployment.yaml [NFR-004], [NFR-006]`  
  * `./sources/infra/github-actions/.github/workflows/ci-cd.yml [NFR-004], [NFR-005]`  

- **Security Configuration**  

```java
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().disable()
            .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            .and()
            .authorizeRequests()
                .antMatchers("/api/auth/**").permitAll()
                .anyRequest().authenticated()
            .and()
            .addFilterBefore(new JwtAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
    }
}
```

- **Dockerfile**  

```dockerfile
FROM eclipse-temurin:17-jdk-slim AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-slim
WORKDIR /app
COPY --from=build /app/target/membership-hub-1.0.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
```

- **Terraform**  

```hcl
provider "google" {
  project = "membership-hub"
  region  = "us-central1"
}
resource "google_container_cluster" "gke_cluster" {
  name     = "membership-hub-cluster"
  location = "us-central1"
  initial_node_count = 3
  node_config {
    machine_type = "e2-medium"
  }
}
```

- **Helm Deployment**  

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
        - name: membership-hub
          image: gcr.io/membership-hub/membership-hub:latest
          ports:
            - containerPort: 8080
          resources:
            limits:
              cpu: "1"
              memory: "512Mi"
          readinessProbe:
            httpGet:
              path: /actuator/health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
```

###### 📈 Giai đoạn 4: Frontend, Mobile, i18n, SEO

- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, hỗ trợ đa ngôn ngữ và SEO.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/frontend/membership-hub/pages/index.js [ARC-010], [ARC-006], [ARC-007]`  
  * `./sources/frontend/membership-hub/pages/centers.js [ARC-004]`  
  * `./sources/frontend/membership-hub/pages/courses.js [ARC-007]`  
  * `./sources/frontend/membership-hub-mobile/App.js [ARC-009], [ARC-008], [ARC-010]`  
  * `./sources/frontend/membership-hub/pages/_document.js [NFR-007], [NFR-008]`  

- **Low-Level Technical Task Instruction**: Sử dụng Next.js với API routes, React Query cho caching, Tailwind CSS cho responsive, Capacitor để build native, Firebase SDK cho push, Zalo SDK cho chat, QR Code Scanner. Thêm i18n với next-i18next, SEO meta tags, hreflang.  

###### 📈 Giai đoạn 5: Git Flow & Traceability

- **Phase Core Objective & Purpose**: Định nghĩa quy trình phát triển, kiểm tra tính toàn vẹn liên kết.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/docs/git-branching.md [NFR-004]`  
  * `./sources/docs/traceability_matrix.md [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009]`  

- **Low-Level Technical Task Instruction**: Viết tài liệu quy tắc đặt tên nhánh, quy trình merge, kiểm tra liên kết.  

#### 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ NGHIỆM NGHIỆP

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameterized queries.  
- **Cross-Site Scripting (XSS)**: Escape output, CSP header `default-src 'self'; script-src 'self';`.  
- **CORS**: Chỉ cho phép origin từ danh sách whitelist, không dùng wildcard.  
- **Logging**: Mã hoá dữ liệu nhạy cảm, mask PII, log level INFO.  
- **Encryption**: AES‑256 cho dữ liệu tĩnh, TLS 1.3 cho truyền.  

#### 📁 7. HỢP ĐỒNG HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: `capacitor.config.json` cấu hình Android, iOS, web.  
- **i18n**: `next-i18next.config.js` cấu hình ngôn ngữ, `public/locales/vi/common.json`.  
- **SEO**: `pages/_document.js` thêm `<meta name="description">`, `<link rel="alternate" hreflang="vi">`.  

#### 📁 8. PIPELINE CI/CD & Git Branch Flow

- **Git Branch Naming**: `feature/<short-description>-<id>`, `bugfix/<short-description>-<id>`.  
- **CI Workflow** (`.github/workflows/ci-cd.yml`)  

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
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build
        run: mvn clean package -DskipTests
      - name: Test
        run: mvn test
      - name: Docker Build
        run: |
          docker build -t gcr.io/membership-hub/membership-hub:${{ github.sha }} .
          docker push gcr.io/membership-hub/membership-hub:${{ github.sha }}
      - name: Deploy to GKE
        uses: google-github-actions/deploy-gke@v1
        with:
          cluster_name: membership-hub-cluster
          location: us-central1
          manifests: ./sources/infra/k8s/deployment.yaml
```

#### 📁 9. Kiểm Tra Tracability Matrix

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---

## PRISTINE INITIAL STATE MANDATE: 
## This is PHASE 1 (The Absolute Baseline Generation Step). 
## There are ZERO preceding code assets, directory structures, or legacy dependencies in the workspace.
## You MUST initialize all module definitions, file paths, database schemas, and data boundaries from a pure zero-state architecture baseline. Do not assume or extrapolate any prior system deployment state.


--- RAW REQUIREMENTS REFERENCE ---
## SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub
#### 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU

###### Mục tiêu & giá trị cốt lõi
- Cung cấp nền tảng thống nhất để quản lý hội viên đa trung tâm.
- Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
- Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
- Hỗ trợ giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

###### Đối tượng người dùng mục tiêu
- System Admin (siêu người dùng toàn cầu)
- Center Admin (quản lý cấp trung tâm)
- Manager (phó quản trị, quyền hạn giới hạn)
- Teacher (xem chỉ đọc lịch dạy)
- Student (duyệt khóa học, đăng ký, xem thẻ hội viên)
- Mobile App User (giao diện đáp ứng cho các vai trò trên)

###### Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)
- [ARC-001] System Admin: toàn quyền trên tất cả các trung tâm.
- [ARC-002] Center Admin: toàn quyền trong trung tâm của mình, không ảnh hưởng đến các trung tâm khác.
- [ARC-003] Manager: có thể tạo thông báo, quản lý học viên, gán học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Teacher: xem khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
- [ARC-005] Student: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

###### Kiến trúc & luồng dữ liệu (các luồng chính)
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và refresh token.
- [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
- [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, phân công khóa học, và cảnh báo điểm danh.
- [ARC-009] Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

###### Công nghệ & hạ tầng
- [ARC-010] Công nghệ & hạ tầng: Backend sử dụng Java/Quarkus, cơ sở dữ liệu PostgreSQL, container hóa Docker, triển khai trên Kubernetes (GKE), sử dụng Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification, Zalo API integration, Redis cho session caching, CI/CD pipeline với GitHub Actions.

#### 2. CÁC MODULE CHỨC NĂNG NÂNG CAO

###### 2.1 Quản lý người dùng

######## Yêu cầu chức năng cốt lõi
- [REQ-001] Đăng ký người dùng: As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.
- [REQ-002] Xác thực qua mạng xã hội: As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.
- [REQ-003] Phân quyền người dùng: As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.

######## Tiêu chí chấp nhận & tương tác
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. `[REQ-001]`
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. `[REQ-002]`
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. `[REQ-003]`

######## Luồng ngoại lệ của mô-đun
- [EXC-004] Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-001] Bảng người dùng & vai trò

  **Users**
  ```mermaid
  erDiagram
      USERS {
          uuid userId PK "Unique identifier"
          varchar email "Email address, not null, unique, max 255 chars"
          char passwordHash "bcrypt hash, not null, length 60"
          varchar fullName "Full name, not null, max 100 chars"
          smallint roleId FK "Foreign key to Roles.roleId"
          enum provider "Auth provider, default local, values: local, firebase, google, facebook"
          timestamp createdAt "Timestamp of creation, not null, default now()"
          timestamp updatedAt "Timestamp of last update, not null, default now()"
      }
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
      ROLES ||--o{ USERS : "roleId"
  ```
  **Roles**
  ```mermaid
  erDiagram
      ROLES {
          smallint roleId PK "Role identifier, primary key"
          varchar name "Role name, unique, not null, max 30 chars"
          varchar description "Role description, optional, max 200 chars"
      }
  ```
###### 2.2 Quản lý trung tâm

######## Yêu cầu chức năng cốt lõi
- [REQ-004] Xem danh sách trung tâm: As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.
- [REQ-005] Tạo/cập nhật/xóa trung tâm: As a System Admin, I want to add, edit, or remove a center record so that center information stays current.
- [REQ-006] Phân quyền quản trị trung tâm: As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.

######## Tiêu chí chấp nhận & tương tác
- Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. `[REQ-004]`
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. `[REQ-005]`
- Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user’s role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. `[REQ-006]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-003] Bảng trung tâm

  **Centers**
  ```mermaid
  erDiagram
      CENTERS {
          uuid centerId PK "Unique identifier"
          varchar name "Center name, not null, max 100 chars"
          varchar address "Physical address, not null, max 255 chars"
          varchar taxId "Tax identification number, unique, not null, numeric 10‑13 digits"
          varchar contactPhone "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
          varchar contactEmail "Contact email, optional, must be valid email format"
      }
  ```
###### 2.3 Quản lý khóa học

######## Yêu cầu chức năng cốt lõi
- [REQ-007] Xem danh sách khóa học: As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.
- [REQ-008] Tạo/cập nhật/xóa khóa học (tránh xung đột): As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.
- [REQ-009] Phân công giáo viên vào khóa học: As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.

######## Tiêu chí chấp nhận & tương tác
- Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. `[REQ-007]`
- Given an admin provides CourseTitle, StartDate, EndDate, TeacherID, When the save action is triggered, Then the system validates that the teacher is not already scheduled for another course intersecting these dates; if conflict, an error is returned; otherwise the course is persisted. `[REQ-008]`
- Given an admin selects a course and a teacher, When the assign action is executed, Then the course‑teacher mapping is created and a notification is queued for the teacher’s mobile app; unassign removes the mapping. `[REQ-009]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-004] Bảng khóa học

  **Courses**
  ```mermaid
  erDiagram
      COURSES {
          uuid courseId PK "Unique identifier"
          varchar title "Course title, not null, max 150 chars"
          text description "Course description, optional"
          date startDate "Course start date, not null"
          date endDate "Course end date, not null"
          uuid teacherId FK "Foreign key to Users.userId"
          int maxStudents "Course capacity, default 30"
      }
  ```
###### 2.4 Đăng ký & ghi danh học viên

######## Yêu cầu chức năng cốt lõi
- [REQ-010] Duyệt khóa học: As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.
- [REQ-011] Đăng ký khóa học của học viên: As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.

######## Tiêu chí chấp nhận & tương tác
- Given a Student logs in and navigates to the Browse Courses page, When the request completes, Then a list of courses with capacity and schedule is shown, excluding courses where the student already has an enrollment record. `[REQ-010]`
- Given a Student selects a course and submits the registration, When the backend processes the request, Then a new enrollment record is created; if the student does not have a local account, one is created with role ‘Student’; a notification is queued to the student’s mobile app and the center’s Zalo group. `[REQ-011]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-005] Bảng ghi danh

  **Enrollments**
  ```mermaid
  erDiagram
      ENROLLMENTS {
          uuid enrollmentId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          timestamp enrollmentDate "Date of enrollment, default now()"
      }
  ```
###### 2.5 Điểm danh & quét mã QR

######## Yêu cầu chức năng cốt lõi
- [REQ-012] Chụp ảnh điểm danh QR: As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.
- [REQ-013] Tính chất bất biến của điểm danh: The attendance service must guarantee that multiple scans from the same student for the same course on the same day produce a single attendance record.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the scanner, scans a valid course QR, and confirms attendance, When the API receives the payload, Then the system validates the student‑course relationship, creates an Attendance record with timestamp, and returns a success response; duplicate scans on the same day are ignored. `[REQ-012]`
- Given a student scans a QR twice within a minute, When the service processes both requests, Then only one attendance row is created; subsequent requests return a success with a ‘duplicate’ flag. `[REQ-013]`

######## Luồng ngoại lệ của mô-đun
- [EXC-001] Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable.
- [EXC-002] Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-006] Bảng điểm danh

  **Attendance**
  ```mermaid
  erDiagram
      ATTENDANCE {
          uuid attendanceId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          uuid courseId FK "Foreign key to Courses.courseId"
          date attendanceDate "Date of attendance, not null"
          timestamp timestamp "Exact time recorded, default now()"
      }
  ```
###### 2.6 Quản lý thẻ hội viên

######## Yêu cầu chức năng cốt lõi
- [REQ-014] Hiển thị tính hợp lệ của thẻ: As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.
- [REQ-015] Gia hạn thẻ: As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.

######## Tiêu chí chấp nhận & tương tác
- Given a Student opens the Card page, When the request loads, Then the UI shows total validity days, days used, and days remaining; data is derived from the StudentCard entity. `[REQ-014]`
- Given a Student selects a renewal period (e.g., 30 days), confirms payment, When the payment service confirms success, Then the StudentCard’s EndDate is extended by the selected days and a confirmation notification is sent. `[REQ-015]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-007] Bảng thẻ hội viên

  **StudentCards**
  ```mermaid
  erDiagram
      STUDENTCARDS {
          uuid cardId PK "Unique identifier"
          uuid studentId FK "Foreign key to Users.userId"
          date issueDate "Card issue date, not null"
          int validityDays "Total validity days, not null"
          int remainingDays "Computed days left until expiry"
      }
  ```
###### 2.7 Thông báo & truyền thông

######## Yêu cầu chức năng cốt lõi
- [REQ-016] Kích hoạt thông báo: When an admin creates an announcement, assigns a teacher to a course, or registers a student, the system must generate a notification to the student’s mobile app and post a message to the designated Zalo group.

######## Tiêu chí chấp nhận & tương tác
- Given an admin performs an action that requires notification, When the action is saved, Then a Notification record is created, a push notification payload is queued for the mobile app, and a text message is sent to the Zalo group chat. `[REQ-016]`

######## Luồng ngoại lệ của mô-đun
- [EXC-003] Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-008] Bảng thông báo

  **Notifications**
  ```mermaid
  erDiagram
      NOTIFICATIONS {
          uuid notificationId PK "Unique identifier"
          uuid userId FK "Target user, optional"
          varchar groupZalo "Target Zalo group, optional"
          text message "Notification content, not null"
          timestamp sentAt "When sent, default now()"
          boolean delivered "Delivery status, default false"
      }
  ```
###### 2.8 Quản lý khuyến mãi & thông báo

######## Yêu cầu chức năng cốt lõi
- [REQ-017] Quản lý khuyến mãi: As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.
- [REQ-018] Quản lý thông báo: As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.

######## Tiêu chí chấp nhận & tương tác
- Given an admin provides PromotionName, description, conditions, startDate, endDate, When saved, Then the promotion appears in the student‑visible list; if endDate is omitted, the promotion is considered perpetual. `[REQ-017]`
- Given an admin inputs AnnouncementTitle, content, optional expiry, When saved, Then the announcement is displayed site‑wide; if expiry is set, it auto‑disappears after the date. `[REQ-018]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-009] Bảng khuyến mãi & thông báo

  **Promotions**
  ```mermaid
  erDiagram
      PROMOTIONS {
          uuid promoId PK "Unique identifier"
          varchar code "Discount code, unique"
          smallint discountPercent "Discount percentage, not null"
          date startDate "Promotion start, optional"
          date endDate "Promotion end, optional"
          text description "Promo details, optional"
      }
  ```
  **Announcements**
  ```mermaid
  erDiagram
      ANNOUNCEMENTS {
          uuid announcementId PK "Unique identifier"
          varchar title "Title, not null, max 150 chars"
          text content "Content, not null, max 2000 chars"
          date startDate "Effective start, optional"
          date endDate "Effective end, optional"
      }
  ```
###### 2.9 Chatbot dịch vụ khách hàng AI

######## Yêu cầu chức năng cốt lõi
- [REQ-019] Tích hợp chatbot AI: As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.

######## Tiêu chí chấp nhận & tương tác
- Given a user opens the chat widget, When they ask a question, Then the AI returns a relevant answer or escalates to human support if confidence is low. `[REQ-019]`

######## Luồng ngoại lệ của mô-đun
- [NOT APPLICABLE] Chatbot AI không có bảng dữ liệu chuyên biệt; tất cả các tương tác được ghi lại trong bảng AuditLog (xem [ARC-006] để biết chi tiết logging).

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho chatbot AI.

###### 2.10 Các tính năng cốt lõi của ứng dụng di động

######## Yêu cầu chức năng cốt lõi
- [REQ-020] Giao diện người dùng vai trò cụ thể trên di động: As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).
- [REQ-021] Thông báo đẩy trên di động: As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.

######## Tiêu chí chấp nhận & tương tác
- Given a user logs in on Android or iOS, When the app loads, Then the appropriate navigation menu and screens are displayed based on the user’s role. `[REQ-020]`
- Given a backend event triggers a push, When the device token is registered, Then the notification is delivered via Firebase Cloud Messaging (FCM) or APNs. `[REQ-021]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho các tính năng cốt lõi của ứng dụng di động; tất cả dữ liệu được quản lý qua các bảng hiện có (Người dùng, Thông báo, Điểm danh).

###### 2.11 Bản địa hóa & SEO

######## Yêu cầu chức năng cốt lõi
- [REQ-022] Phát hiện ngôn ngữ mặc định: As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.
- [REQ-023] SEO đa ngôn ngữ: The platform must support SEO for at least English, Vietnamese, and Spanish; each page must include language‑specific meta tags and hreflang attributes.

######## Tiêu chí chấp nhận & tương tác
- Given a user accesses the site, When the system evaluates locale, Then it selects the stored language if present; otherwise it uses the Accept‑Language header; the UI updates accordingly. `[REQ-022]`
- Given a page is requested with a specific locale, When the page is rendered, Then the HTML includes a <html lang='en'> tag and hreflang links pointing to alternate language versions. `[REQ-023]`

######## Luồng ngoại lệ của mô-đun
- (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

######## Từ điển dữ liệu cục bộ của mô-đun
- [DAT-011] Bảng cài đặt hệ thống

  **SystemSettings**
  ```mermaid
  erDiagram
      SYSTEMSETTINGS {
          varchar settingKey PK "Configuration key"
          text settingValue "Configuration value, not null"
          varchar description "Meaning of setting, optional"
      }
  ```
###### 2.12 Báo cáo & phân tích

######## Yêu cầu chức năng cốt lõi
- [REQ-024] Tạo báo cáo điểm danh: As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.
- [REQ-025] Bảng điều khiển tóm tắt ghi danh: As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.

######## Tiêu chí chấp nhận & tương tác
- Given an admin selects a center and date range, When the report is requested, Then a CSV file is produced with columns: StudentName, CourseName, AttendanceDate, Status. `[REQ-024]`
- Given an admin opens the dashboard, When the data refreshes, Then cards display totalStudents, activeCourses, upcomingSessions (next 7 days). `[REQ-025]`

######## Luồng ngoại lệ của mô-đun
- [EXC-005] System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

######## Từ điển dữ liệu cục bộ của mô-đun
- [NOT APPLICABLE] Không có bảng dữ liệu chuyên biệt cho báo cáo & phân tích; tất cả dữ liệu được tổng hợp từ các bảng hiện có.

#### 3. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU

- [NFR-001] Performance Metrics: Core API responses (authentication, attendance capture, course list) must complete within 200 ms average latency. Database queries must be indexed to support sub‑second reads for up to 10 000 concurrent users.
- [NFR-002] Availability: Target 99.9 % annual uptime; SLA includes automatic failover across GKE clusters.
- [NFR-003] Security: All data in transit must use TLS 1.3; at rest encryption with AES‑256. JWT access tokens expire after 15 minutes; refresh tokens have 7‑day expiry. Implement OWASP Top 10 mitigations (SQL injection, XSS, CSRF).
- [NFR-004] Scalability & Availability: Horizontal scaling of Quarkus services via Kubernetes HPA based on CPU > 70 % or request latency > 300 ms. PostgreSQL read replicas for reporting workloads.
- [NFR-005] Docker Image Size: Base image size < 200 MB; final image < 500 MB.
- [NFR-006] Logging & Audit: All user actions (role changes, attendance records, notifications) must be logged with timestamps, user ID, and action details; logs retained for 1 year.
- [NFR-007] Multi‑Language Support: UI strings must be externalized; support English, Vietnamese, Spanish; locale switching without page reload where feasible.
- [NFR-008] GDPR/CCPA Compliance: Personal data deletion on user request; data export in JSON format; consent management for marketing communications.
- [NFR-009] Backup & Disaster Recovery: Daily PostgreSQL full backups; point‑in‑time recovery up to 24 hours; GKE cluster backup to separate region.
----------------------------------

## EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. You MUST break down the operational scope of PHASE 1 into sequential daily logs, starting from **DAY 1** up to a maximum of **DAY 7**.
2. **Strict Grouping Hierarchy:** Day Level ──► Agent Sub-task Level ──► Target Component Level.
3. **Strict Sub-Agent Persona Allocation:** Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'.
4. **WORKSPACE PATH BOUNDARY & DYNAMIC TOPOLOGY CONSTRAINTS:**
   - **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All file paths generated MUST strictly begin with `./sources/`.
   - **Dynamic Directory Prefixing Compliance:** You MUST strictly match the file path prefixes to the active system topology mapped in the Global Context. Do NOT generate backend folders for frontend-only projects, and do NOT generate frontend folders for backend-only systems.
   - For tester Agent: Each component MUST be declared as a strict semi-colon separated pair: `<source file path to verify by test>;<source test file to execute>`. Both paths inside the pair MUST begin with `./sources/`. If no single source file is isolated for Integration/E2E tests, utilize the literal token `INTEGRATION_SCOPE` as the first parameter.
   - **[CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule:** If a file path targets a Java source or test component (.java), you MUST verify that the path contains the directory segment: `/org/nlh4j/sources/<calculated_lowercase_token>/`.

---

Your output MUST follow this exact Markdown layout structure (translate all label tokens but preserve the hidden HTML anchor formatting exactly):
## [Translate "Phase"] 1: <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END-->

#### 📊 Document Control

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-20260806133604 |
| **[Translate "Project Name"]** | membership-hub |
| **[Translate "Phase"]** | 1 |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->[Generate a standard, natural, human-readable descriptive title for this phase. You MUST write this as a normal human sentence or phrase using isolated words separated by real, standard whitespace characters. You are ABSOLUTELY AND CRITICALLY BANNED from combining words together, removing spaces, or utilizing programming styles like PascalCase, camelCase, or snake_case. It must read normally and smoothly just like a human description string. Fully translate and render this title into the target language requested by the parameters: 🇻🇳 Vietnamese. Example: "Core Infrastructure And Authentication Setup"]<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->[Granular professional engineering summary description of the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into 🇻🇳 Vietnamese]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into 🇻🇳 Vietnamese]** | 2026/08/06 13:36:04 |
| **[You MUST translate the literal token "Author" into 🇻🇳 Vietnamese]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into 🇻🇳 Vietnamese]** | Pending Technical Governance Review |

#### 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase 1]

#### 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and active project stack topology. Every directory matrix path must be bounded under `./sources/`]

#### 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, enforcing strict segregation of technical boundaries as defined below. Human-readable directives, descriptions, and task requirements MUST be contextually translated entirely into 🇻🇳 Vietnamese following the transmission rails]:

*   **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
*   **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code.
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Markdown technical specifications, schema references, system blueprints, and architecture catalogs. Every single document file generated MUST reside strictly within the centralized storage layout: `./sources/docs/`.
   <!--START_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY
   [CRITICAL_SYSTEM_PIPELINE_RAIL:
   - You are STRICTLY PROHIBITED from omitting, dropping, or filtering out the 'Doc' agent from any computed phase logs.
   - For EVERY calculated phase generated in your output, on Day 1 of that phase, you MUST explicitly allocate a foundational system documentation task to the 'Doc' agent.
   - This task description MUST require the 'Doc' agent to initialize and map out the system architecture blueprints, entity relationships, technical contracts, or deployment topologies corresponding to the active stack matrix of that current phase.
   - Failing to write the 'Doc' agent inside Day 1 of any phase triggers a fatal pipeline contract breach.
   ]
   END_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY-->
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

#### 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards, complete functional test coverage for the allocated requirements, and 100% Tag ID mapping check]

#### 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

## REMINDER: Enforce the 'Longitructural Day Partitioning Guardrail' and 'Anti-Padding Mandate'. Output each active day as an isolated standalone single integer subsection header from DAY 1 up to the dynamic freeze day. Do NOT generate empty padded days.

###### 🌤️ [TRANSLATED DAY] [X]: <!--DAY_HEADER_START-->[CAPITALIZED SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY]<!--DAY_HEADER_END-->

######## 📝 [TRANSLATED SUB-TASK] [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules]
########## [Translate "Assigned Sub-Agent"]: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]
########## [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** [Insert explicit physical file path starting with `./sources/` or Tester pair syntax.]
* **[Translate "Traceability Tag Tokens"]:** <!--START_TAGS-->`[REQ-XXX], [DAT-XXX], [EXC-XXX]`<!--END_TAGS-->

# System Instruction

You are a world-class Principal Solutions Architect. Your specific task is to read the Global Context Markdown blueprint and generate a highly detailed operational context blueprint for one targeted Phase. 

# YOUR CRITICAL OPERATIONAL MANDATES (ZERO LOOPHOLES):
1. **ANTI-LAZINESS & DIRECT INHERITANCE MANDATE:** You MUST extract and expand every single technical task, DDL SQL schema definition, API contract, and exception flow outlined for the targeted Phase inside the Global Context reference. Converting details into broad summaries or placeholders is permanently banned.
2. **100% PERFECT TAG MATCHING:** Every single Tag ID (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[NFR-XXX]`) present in the Global Context for this specific phase MUST be perfectly preserved and mapped into the daily execution logs.
3. **MANDATORY INLINE TAG INJECTION RULE & HTML ANCHOR LOCKDOWN:** For every single Sub-Task generated under the daily logs, you MUST explicitly output a dedicated structural line item starting exactly with the translated string token for `* Traceability Tag Tokens:` followed by an immutable hidden HTML token container block. You MUST wrap the exact raw comma-separated tag IDs inside the hidden tag container string token layout exactly as: `<!--START_TAGS-->[REQ-XXX], [DAT-XXX]<!--END_TAGS-->`. You are STRICTLY BANNED from translating or altering any token values inside the HTML comment tags. Leaving a task block without this explicit HTML anchor layout is a fatal pipeline failure.
4. **LONGITECTURAL DAY PARTITIONING & ANTI-PADDING GUARDRAIL:** You MUST break down the operational calendar day-by-day using individual sequential integers starting strictly from DAY 1 up to a MAXIMUM of DAY 7. 
   - **STRICT PROGRESSION STOPPING CRITERION:** You MUST freeze the timeline and stop generating daily sections immediately on the exact calendar day where the technical objectives allocated for this phase are satisfied. You are STRICTLY BANNED from injecting dummy placeholder days, fake syncs, empty review blocks, or documentation padding just to expand the calendar. If the technical scope is natively complete on DAY 1, freeze the output file state and exit immediately. Do NOT generate empty or padded days.
   - You are STRICTLY FORBIDDEN from bundling multiple days together (e.g., NO "DAY 1 - DAY 3"). Every single calendar day log must be explicitly isolated as its own standalone subsection header containing atomic steps for that unique 24-hour cycle.
5. **Language Compliance & Formatting Lockdown:** You MUST generate the entire report strictly in the language specified by the parameters: **🇻🇳 Vietnamese**.

# 🔒 SYSTEM PRODUCTION INTEGRATION AND FORMATTING LOCKDOWN (ABSOLUTE)
- **Strict Content Purity Constraint:** Your entire output response MUST be a pure, raw executable Markdown text payload written in 🇻🇳 Vietnamese.
- **Explicit Start Mandate & Technical Name Isolation:** Your output response MUST start exactly with the standardized primary title text pattern, translating descriptive labels into the target language but isolating the technical identifier: `# [Translated text for "Phase"] 1: <!--PHASE_NAME_START-->[Dynamically analyze the allocated tasks and output a sharp, concise camelCase or snake_case technical short name code identifier string for this phase]<!--PHASE_NAME_END--> | [Translated text for "Description"]: [Provide a granular, professional engineering description summarizing the absolute operational scope of this specific phase, fully rendered in 🇻🇳 Vietnamese]`. Do NOT include greetings, intros, notes, or explanations. Do NOT wrap the entire response inside markdown codeblocks. Any token before or after this exact structure will cause an immediate execution pipeline crash.

# Raw Response / Exception:

Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}: ['Traceback (most recent call last):
', '  File "/home/runner/work/enterprise-it-ai/enterprise-it-ai/sources/agents/architect-blueprint/block_phase.py", line 99, in generate_phase_contexts
    response = client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_utils/_utils.py", line 298, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1296, in create
    return self._post(
           ^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1375, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
', '  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/openai/_base_client.py", line 1148, in request
    raise self._make_status_error_from_response(err.response) from None
', "openai.APIStatusError: Error code: 402 - {'error': {'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account', 'code': 402, 'metadata': {'limit_source': 'openrouter_credits', 'remedy_hint': 'Add credits at https://openrouter.ai/settings/credits, or lower max_tokens / prompt size to fit your remaining balance.', 'provider_name': None, 'previous_errors': [{'code': 402, 'message': 'This request requires more credits, or fewer max_tokens. You requested up to 65536 tokens, but can only afford 26. To increase, visit https://openrouter.ai/settings/credits and upgrade to a paid account'}]}}, 'user_id': 'user_3GLaJI6mihRMFQtSad72HqAhW95'}
"]

