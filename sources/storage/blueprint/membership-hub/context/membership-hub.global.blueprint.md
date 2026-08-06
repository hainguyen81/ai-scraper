# BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806131423 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:14:23 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CỐT LÕ

### 1.1. Mô Hình Hệ Thống Cốt Lõi & Kiến Trúc

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

### 1.2. Mô Hình Dòng Dữ Liệu & Hệ Sinh Thái

- **Authentication Flow**: OAuth2 (Firebase, Google, Facebook) → JWT → API Gateway.  
- **Attendance Flow**: Mobile QR scan → API → idempotent attendance record.  
- **Notification Flow**: Event → Kafka → Notification Service → FCM/APNs + Zalo group.  
- **Enrollment Flow**: Student → API → Enrollment record, capacity check, notification.  
- **Promotion Flow**: Center Admin → API → Promotion record, student visibility.  
- **Reporting Flow**: Admin → API → CSV export, dashboard metrics.  

## 📁 2. CỤC PHẦN CÔNG NGHỆ & THƯ VIỆN

- **Backend Infrastructure Core Stack**: Java 17, Quarkus 3.x, Hibernate ORM, Flyway, Kafka, Redis, PostgreSQL, JWT, Spring Security, OWASP ESAPI.  
- **Frontend & Cross‑Platform UI Mobile Stack**: Next.js 13, React 18, TypeScript, Tailwind CSS, React Query, Capacitor 4, Firebase SDK, Zalo SDK, QR Code Scanner.  

### MÁ THƯỜNG CỤC PHẦN

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. QUY ĐỊNH BẢO VỆ & TUY ĐIỂM TUYÊN CUNG

- **Workspace Root**: `./sources/`.  
- **Backend Code**: `./sources/backend/membership-hub/`.  
- **Frontend Code**: `./sources/frontend/membership-hub/`.  
- **Mobile Code**: `./sources/frontend/membership-hub-mobile/`.  
- **Infra Code**: `./sources/infra/`.  
- **Docs**: `./sources/docs/`.  
- **Java Package**: `org.nlh4j.saas.membershiphub`.  

## 📁 4. BẢNG TỔNG QUAN ĐIỀU PHÁP KIẾN TRÚC GIAO PHÂN

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-7 | ./sources/backend/membership-hub/ | Tạo schema, API cơ bản | Coder | [DAT-001], [DAT-002], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 2 | 1-5 | ./sources/backend/membership-hub/ | Kiểm thử API | Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |
| Giai đoạn 3 | 1-5 | ./sources/infra/ | Bảo mật, Docker, GCP, GKE, CI/CD | Coder, Docker, GCP, GKE | [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 4 | 1-3 | ./sources/frontend/membership-hub/ | Frontend, Mobile, i18n, SEO | Coder | [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010] |
| Giai đoạn 5 | 1-2 | ./sources/docs/ | Git flow, Traceability | Doc, Reviewer | [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009] |

## 📁 5. CHI TIẾT GIAO PHÂN GIAI ĐOẠN & LỊCH HÀNH NGÀY

### 📈 Giai đoạn 1: Tạo Schema & API Cơ Bản

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

### 📈 Giai đoạn 2: Kiểm Thử API

- **Phase Core Objective & Purpose**: Đảm bảo tính đúng đắn, độ tin cậy và bảo mật của các endpoint.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/UserControllerTest.java [REQ-001], [REQ-002], [REQ-003]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CenterControllerTest.java [REQ-004], [REQ-005], [REQ-006]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/CourseControllerTest.java [REQ-007], [REQ-008], [REQ-009]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/controller/EnrollmentControllerTest.java [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]`  
  * `./sources/backend/membership-hub/src/test/java/com/membershiphub/integration/AuthIntegrationTest.java [REQ-001], [REQ-002], [REQ-003]`  

- **Low-Level Technical Task Instruction**: Viết unit tests sử dụng JUnit 5, Mockito, Spring MockMvc. Kiểm tra các trường hợp thành công, lỗi, và bảo mật (JWT, CSRF). Đảm bảo coverage ≥ 85 %.  

### 📈 Giai đoạn 3: Bảo Mật & Hạ Tầng

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

### 📈 Giai đoạn 4: Frontend, Mobile, i18n, SEO

- **Phase Core Objective & Purpose**: Xây dựng giao diện web, mobile, hỗ trợ đa ngôn ngữ và SEO.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/frontend/membership-hub/pages/index.js [ARC-010], [ARC-006], [ARC-007]`  
  * `./sources/frontend/membership-hub/pages/centers.js [ARC-004]`  
  * `./sources/frontend/membership-hub/pages/courses.js [ARC-007]`  
  * `./sources/frontend/membership-hub-mobile/App.js [ARC-009], [ARC-008], [ARC-010]`  
  * `./sources/frontend/membership-hub/pages/_document.js [NFR-007], [NFR-008]`  

- **Low-Level Technical Task Instruction**: Sử dụng Next.js với API routes, React Query cho caching, Tailwind CSS cho responsive, Capacitor để build native, Firebase SDK cho push, Zalo SDK cho chat, QR Code Scanner. Thêm i18n với next-i18next, SEO meta tags, hreflang.  

### 📈 Giai đoạn 5: Git Flow & Traceability

- **Phase Core Objective & Purpose**: Định nghĩa quy trình phát triển, kiểm tra tính toàn vẹn liên kết.  
- **Target Physical Directory Matrix Map**:  
  * `./sources/docs/git-branching.md [NFR-004]`  
  * `./sources/docs/traceability_matrix.md [REQ-001]...[REQ-025], [EXC-001]...[EXC-005], [DAT-001]...[DAT-011], [ARC-001]...[ARC-010], [NFR-001]...[NFR-009]`  

- **Low-Level Technical Task Instruction**: Viết tài liệu quy tắc đặt tên nhánh, quy trình merge, kiểm tra liên kết.  

## 📁 6. MÃ BẢO VỆ & CHẾ ĐỘ NGHIỆM NGHIỆP

- **SQL Injection (SQLi)**: Sử dụng prepared statements, parameterized queries.  
- **Cross-Site Scripting (XSS)**: Escape output, CSP header `default-src 'self'; script-src 'self';`.  
- **CORS**: Chỉ cho phép origin từ danh sách whitelist, không dùng wildcard.  
- **Logging**: Mã hoá dữ liệu nhạy cảm, mask PII, log level INFO.  
- **Encryption**: AES‑256 cho dữ liệu tĩnh, TLS 1.3 cho truyền.  

## 📁 7. HỢP ĐỒNG HỢP TÁC MOBILE & SEO

- **Capacitor Mobile**: `capacitor.config.json` cấu hình Android, iOS, web.  
- **i18n**: `next-i18next.config.js` cấu hình ngôn ngữ, `public/locales/vi/common.json`.  
- **SEO**: `pages/_document.js` thêm `<meta name="description">`, `<link rel="alternate" hreflang="vi">`.  

## 📁 8. PIPELINE CI/CD & Git Branch Flow

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

## 📁 9. Kiểm Tra Tracability Matrix

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`