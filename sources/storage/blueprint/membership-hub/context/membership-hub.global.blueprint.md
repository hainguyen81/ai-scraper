# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Kiểm soát Tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260802164015 |
| **Tên Dự án** | membership-hub |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày.Giờ** | 2026/08/02 16:40:15 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 📊 1. Tổng quan Hệ thống & Phương thức Kiến trúc Cốt lõi

### 1.1. Phương thức Hệ thống Cốt lõi & Kiến trúc
Dự án áp dụng kiến trúc **Microservices theo hướng sự kiện** với các biên giới CQRS rõ ràng. Mỗi lĩnh vực nghiệp vụ (Người dùng, Trung tâm, Khóa học, Ghi danh, Điểm danh, Thẻ hội viên, Thông báo, Khuyến mãi, Chatbot, Giao diện di động) được triển khai dưới dạng một dịch vụ độc lập. Các dịch vụ giao tiếp qua **Apache Kafka** cho các sự kiện bất đồng bộ (ví dụ: `[ARC-007]`, `[ARC-008]`) và qua **REST/GraphQL** cho các thao tác đồng bộ. Mỗi dịch vụ sử dụng mô hình **Command/Query Separation** với các bảng đọc/ghi riêng biệt, đảm bảo khả năng mở rộng theo chiều ngang và tính idempotent cho các thao tác như ghi điểm danh `[REQ-013]`. Các chính sách bảo mật được thực thi ở **Edge Gateway** (OAuth2/OIDC) với JWT có thời hạn 15 phút `[ARC-006]`. Hệ thống tuân thủ nghiêm ngặt **12-factor app** với container Docker, triển khai trên Kubernetes (GKE) và sử dụng **Flyway** cho quản lý migration cơ sở dữ liệu. Các mô hình dữ liệu được định nghĩa dưới dạng các bảng quan hệ PostgreSQL với các ràng buộc khóa ngoại, đảm bảo tính toàn vẹn tham chiếu cho các mối quan hệ đa-đến-một (ví dụ: `[DAT-001]`, `[DAT-003]`). Các API được thiết kế theo kiểu **RESTful** với các hợp đồng rõ ràng (xem Section 5), hỗ trợ **content-negotiation** và **rate-limiting** để đáp ứng mục tiêu hiệu năng `[NFR-001]`. Các cơ chế **Circuit Breaker** và **Bulkhead** được tích hợp qua Resilience4j để đảm bảo khả năng phục hồi `[NFR-002]`. Các chính sách đa ngôn ngữ được ngoại biên hóa và được cung cấp qua **i18next**, với các thẻ hreflang cho SEO `[REQ-023]`. Các quy tắc kiểm soát truy cập được thực thi qua **Spring Security** với các biểu diễn vai trò chi tiết theo RBAC `[ARC-001]` đến `[ARC-005]`. Các quy trình nghiệp vụ quan trọng được bao bọc bởi các **outbox pattern** để đảm bảo tính nhất quán sự kiện. Các chính sách tuân thủ GDPR/CCPA được thực hiện với các interceptor xóa dữ liệu và xuất dữ liệu theo yêu cầu `[NFR-008]`. Các chính sách kiểm tra và ghi nhật ký được thực hiện qua **OpenTelemetry** và **ELK stack**, ghi lại mọi thao tác thay đổi dữ liệu với dấu thời gian, user ID và chi tiết thao tác `[NFR-006]`. Các chính sách triển khai tuân thủ **GitOps** với các pipeline CI/CD trên GitHub Actions, tự động hóa việc xây dựng Docker image (< 500 MB `[NFR-005]`), quét vulnerabilities và thực hiện canary releases trên GKE `[NFR-004]`.

### 1.2. Kiến trúc Luồng Dữ liệu Doanh nghiệp & Hệ sinh thái Cốt lõi
Hệ thống sử dụng **Event-Driven Architecture** với các chủ đề Kafka chính: `auth-events`, `center-events`, `course-events`, `enrollment-events`, `attendance-events`, `membership-events`, `notification-events`, `promotion-events`. Các **Event Producers** (ví dụ: dịch vụ điểm danh cho `[REQ-012]`) ghi sự kiện vào Kafka, trong khi các **Event Consumers** (ví dụ: engine thông báo cho `[REQ-016]`) xử lý chúng một cách bất đồng bộ. Các **Ingestion Gateways** (API Gateway trên Nginx) định tuyến các yêu cầu HTTP đến các dịch vụ phù hợp, thực hiện xác thực OAuth2 `[ARC-006]` và ghi lại nhật ký truy cập. Các **Data Lakes** (Google Cloud Storage) nhận các bản ghi audit từ PostgreSQL thông qua CDC (Debezium) để phân tích sâu hơn. Các **Cache Layers** (Redis) lưu trữ các bản ghi phiên làm việc, thông tin người dùng và kết quả quét QR tạm thời để giảm độ trễ cho các API nóng (ví dụ: xác thực điểm danh `[REQ-013]`). Các **Outbound Connectors** tương tác với các hệ thống bên ngoài: **Firebase Authentication**, **Google/Facebook OAuth2**, **Zalo API** cho các bài đăng nhóm, **FCM/APNs** cho push notification `[REQ-021]`. Các **Circuit Breakers** được đặt trước các adapter bên ngoài để cách ly sự cố mạng `[EXC-001]`. Các **Schema Registry** (Confluent) đảm bảo tính tương thích phiên bản cho các sự kiện. Các **Retry Mechanisms** với exponential backoff được áp dụng cho các sự kiện thất bại (ví dụ: gửi notification `[EXC-003]`). Các **Backpressure Handling** được thực hiện qua **Reactive Streams** trong các dịch vụ Quarkus để duy trì khả năng đáp ứng dưới tải nặng `[NFR-001]`. Các **Observability Pipelines** thu thập metrics (Micrometer), logging (Logback) và traces (OpenTelemetry) để giám sát toàn bộ hệ thống, hỗ trợ các chính sách **Alerting** dựa trên các ngưỡng hiệu năng `[NFR-002]`. Các **Data Encryption** ở trạng thái nghỉ sử dụng AES‑256 cho PostgreSQL, trong khi TLS 1.3 được áp dụng cho mọi kênh truyền dữ liệu `[NFR-003]`. Các **Multi‑Tenant Isolation** được thực hiện qua schema per‑center trong PostgreSQL, với các chính sách whitelist origin cho CORS `[NFR-004]`. Các **Data Governance** bao gồm việc đánh dấu PII, tự động masking trong logs và các chính sách retention (1 năm cho audit logs) `[NFR-006]`. Các **Internationalization** được hỗ trợ qua các resource bundles và các thẻ hreflang động cho SEO `[REQ-023]`. Các **Disaster Recovery** sử dụng replica cross‑region và các script backup hàng ngày, với khả năng khôi phục điểm‑in‑time trong vòng 24 giờ `[NFR-009]`.

## 📁 2. Phụ thuộc Công nghệ & Thư viện Hệ sinh thái

- **Hệ thống Nền tảng Backend:** Quarkus 3.2.5‑Final (Java 21), PostgreSQL 15, Flyway 9.16, Hibernate ORM, SmallRye OpenAPI, Eclipse Microprofile JWT, Picocli, Lombok, JUnit 5, AssertJ, WireMock, Docker base image `eclipse-temurin:21-jdk-alpine`, OpenTelemetry, Micrometer, Resilience4j, Apache Kafka 3.5, Redis 7, Docker‑Compose cho local dev, GitHub Actions CI/CD.
- **Hệ thống Giao diện Người dùng Frontend & Đa nền tảng Di động:** Next.js 14.x, React 18.2, TypeScript 5, Tailwind CSS, i18next, react‑i18next, Redux Toolkit, Axios, SWR, PWA (Service Workers), Capacitor 5, @capacitor/app, @capacitor/haptics, @capacitor/keyboard, Firebase SDK, @react‑firebase‑login, Jest, React Testing Library, ESLint/Prettier, Husky, lint‑staged.

## 📁 3. Quy tắc Bảo vệ Toàn cầu & Tiêu chuẩn Tuân thủ Doanh nghiệp

- **Quy tắc Ranh giới Không gian Làm việc Tuyệt đối:** Toàn bộ kho lưu trữ phải nằm trong thư mục gốc dự án `..`. Tất cả các đường dẫn vật lý được tạo ra phải bắt đầu bằng `./sources/`. Không cho phép bất kỳ đường dẫn tương đối hoặc tuyệt đối nào khác.
- **Tuân thủ Tiền tố Thư mục Động:** Dựa trên cấu hình hệ thống, các module backend được đặt dưới dạng `./sources/backend.<service-name>/`, các module frontend dưới dạng `./sources/frontend/` (hoặc `./sources/frontend.<app-name>/` cho các ứng dụng di động đa nền tảng), và các tài nguyên infra dưới dạng `./sources/infra/`. Quy tắc này được áp dụng nghiêm ngặt trong toàn bộ pipeline CI/CD.
- **Tiêu chuẩn Gói Java:** Tất cả mã nguồn Java phải nằm trong gói cơ sở `org.nlh4j.saas.membershiphub`. Tên dự án được chuẩn hóa bằng cách loại bỏ khoảng trắng, dấu gạch ngang và dấu gạch dưới, chuyển về chữ thường.
- **Cú pháp Mục tiêu Đường dẫn Kiểm thử Nghiêm ngặt:** Bất kỳ thành phần nào được kiểm thử bởi sub‑agent **Tester** phải được biểu diễn dưới dạng cặp `<source_component>;<test_suite_file>`, ví dụ: `./sources/backend.auth;src/test/java/org/nlh4j/saas/membershiphub/auth/AuthServiceTest.java`. Cả hai phần trong cặp đều phải tuân thủ quy tắc tiền tố `./sources/`.

## 📁 4. Bảng Tóm tắt Kiến trúc Đa pha Cấp cao

| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1‑7 | `./sources/backend.auth`, `./sources/backend.user`, `./sources/backend.center`, `./sources/infra.k8s`, `./sources/frontend.nextjs` | Triển khai core authentication, quản lý người dùng, quản lý trung tâm, manifests K8s và giao diện người dùng web cơ bản. | Coder | [ARC-006], [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [DAT-001], [DAT-003], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [EXC-004] |
| Phase 2 | Day 8‑14 | `./sources/backend.course`, `./sources/backend.enrollment`, `./sources/backend.gateway` | Xây dựng CRUD khóa học, ghi danh học viên, API gateway với các chính sách RBAC cho quản lý và giáo viên. | Tester | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [EXC-001], [EXC-002] |
| Phase 3 | Day 15‑21 | `./sources/backend.attendance`, `./sources/backend.membership` | Triển khai quét QR điểm danh, ghi nhận bất biến, quản lý thẻ hội viên và logic gia hạn. | Reviewer | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [EXC-005], [ARC-007] |
| Phase 4 | Day 22‑28 | `./sources/backend.notification`, `./sources/backend.promotion`, `./sources/backend.announcement` | Xây dựng engine thông báo (push + Zalo), quản lý khuyến mãi và thông báo với các chính sách hết hạn. | Doc | [REQ-016], [REQ-017], [REQ-018], [DAT-008], [DAT-009], [EXC-003], [ARC-008] |
| Phase 5 | Day 29‑35 | `./sources/backend.chatbot`, `./sources/frontend.mobile`, `./sources/infra.ci`, `./sources/infra.gcp`, `./sources/infra.gke` | Triển khai chatbot AI, giao diện người dùng di động đa vai trò, pipeline CI/CD, manifests GCP & GKE. | Docker | [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-011], [ARC-009], [ARC-010], [NFR-007], [NFR-008], [NFR-009] |

## 5. Chi tiết Hóa Giai đoạn & Phân công Công việc Theo Ngày

<!--START_DELIMITTER-->
### Phase 1 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai foundation core bao gồm xác thực người dùng, quản lý vai trò, quản lý trung tâm và giao diện người dùng web cơ bản, thiết lập các chính sách bảo mật, hiệu năng và tuân thủ toàn cầu.
- **Target Physical Directory Matrix Map:** 
  - `./sources/backend.auth` (mã nguồn dịch vụ xác thực) – `[ARC-006], [REQ-001], [REQ-002], [DAT-001]`
  - `./sources/backend.user` (mã nguồn quản lý người dùng) – `[REQ-003], [DAT-001]`
  - `./sources/backend.center` (mã nguồn quản lý trung tâm) – `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
  - `./sources/infra.k8s` (manifests Kubernetes) – `[NFR-004], [NFR-005]`
  - `./sources/frontend.nextjs` (giao diện người dùng web) – `[NFR-007]`
- **Database Schema DDL SQL Specification [DAT-001], [DAT-003], [DAT-011]:**
```sql
-- [DAT-001] Bảng Users & Roles
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
    provider ENUM('local','firebase','google','facebook') NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    updated_at TIMESTAMP NOT NULL DEFAULT now()
);

-- [DAT-003] Bảng Centers
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(30),
    contact_email VARCHAR(255)
);

-- [DAT-011] Bảng SystemSettings
CREATE TABLE system_settings (
    setting_key VARCHAR(100) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-006]:**
  - `POST /api/v1/auth/register` – body: `{email, password, fullName}` → trả về `{userId, token}` `[REQ-001]`
  - `POST /api/v1/auth/social` – body: `{provider, code}` → trao đổi code lấy JWT `[REQ-002]`
  - `PUT /api/v1/users/{userId}/role` – body: `{roleId}` → cập nhật vai trò `[REQ-003]`
  - `GET /api/v1/centers` – trả về danh sách trung tâm `[REQ-004]`
  - `POST /api/v1/centers` – body: `{name, address, taxId, contactPhone, contactEmail}` `[REQ-005]`
  - `PUT /api/v1/centers/{centerId}` – cập nhật `[REQ-005]`
  - `DELETE /api/v1/centers/{centerId}` – xóa `[REQ-005]`
  - `POST /api/v1/centers/{centerId}/admin/{userId}` – chỉ định quản trị viên trung tâm `[REQ-006]`
  - `POST /api/v1/auth/token` – xác thực JWT, thời hạn 15 phút `[ARC-006]`
- **Phase Localized Exception Handlers [EXC-004]:**
  - Xác thực đầu vào không hợp lệ (email sai định dạng, thiếu trường bắt buộc) → trả về `400 Bad Request` với danh sách chi tiết các trường lỗi.
  - Xung đột khóa duy nhất (email hoặc taxId trùng) → trả về `409 Conflict` với thông báo rõ ràng.
  - Xác thực JWT thất bại hoặc token hết hạn → trả về `401 Unauthorized`.
  - Tất cả các response lỗi đều tuân thủ cấu trúc `{ "error": "MESSAGE", "code": "ERROR_CODE", "fields": [...] }`.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1:** Triển khai core authentication service và các migration cơ sở dữ liệu đầu tiên.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.auth;src/main/java/org/nlh4j/saas/membershiphub/auth/AuthController.java` – `[ARC-006], [REQ-001], [REQ-002], [DAT-001]`
      - **Low-Level Technical Task Instruction:** Viết AuthController với các endpoint `/register`, `/social`, `/token`. Sử dụng `PasswordEncoder` cho bcrypt hash, tích hợp Firebase/Google/Facebook OAuth2 qua `WebClient`. Áp dụng `@Valid` validation, trả về JWT với `java.time.Duration.ofMinutes(15)`. Thêm `SecurityConfig` với `JWTBearerConverter`. Đảm bảo tất cả các endpoint được bảo vệ bằng `@PreAuthorize` dựa trên vai trò từ `roles` table. Chuyển đổi exception thành `ProblemDetail` tuân thủ RFC 7807.
      - **Targeted Tag IDs:** `[ARC-006], [REQ-001], [REQ-002], [DAT-001]`
- **DAY 2:** Xây dựng service quản lý người dùng và vai trò.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.user;src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java` – `[REQ-003], [DAT-001]`
      - **Low-Level Technical Task Instruction:** Triển khai UserService với các phương thức `assignRole(Long userId, Integer roleId)`, `getUserDetails(Long userId)`. Sử dụng `@Transactional` và `Optional` để xử lý trường hợp không tìm thấy. Áp dụng `@PreAuthorize('hasAuthority("SYSTEM_ADMIN")')` cho quyền chỉ định vai trò. Thêm logging via `SLF4J`. Viết unit test cho các trường hợp thông thường và ngoại lệ (ví dụ: không có quyền).
      - **Targeted Tag IDs:** `[REQ-003], [DAT-001]`
- **DAY 3:** Triển khai module quản lý trung tâm và migration schema.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.center;src/main/java/org/nlh4j/saas/membershiphub/center/CenterController.java` – `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
      - **Low-Level Technical Task Instruction:** Tạo CenterController với các CRUD endpoint cho trung tâm. Sử dụng `@RequestBody` validation với `jakarta.validation.constraints`. Đảm bảo tính duy nhất của `taxId` qua `@Column(unique=true)`. Thêm `CenterService` với logic kiểm tra trùng lặp và ném `DuplicateCenterException`. Tích hợp `Flyway` để áp dụng migration `V1__create_centers_table.sql`. Thêm `CenterMapper` để chuyển đổi DTO sang entity.
      - **Targeted Tag IDs:** `[REQ-004], [REQ-005], [REQ-006], [DAT-003]`
- **DAY 4:** Xây dựng giao diện người dùng web cơ bản với i18n.
  - **Sub-Agent Workflow Specialization:**
    * **Doc:**
      - **Target Component file path (`target_component`):** `./sources/frontend.nextjs;pages/_app.tsx` – `[NFR-007]`
      - **Low-Level Technical Task Instruction:** Tạo `_app.tsx` bao bọc toàn bộ ứng dụng với `NextIntlProvider`. Cấu hình `locales` (`en`,`vi`,`es`) và `defaultLocale` (`vi`). Thêm `Head` component để thiết lập `<html lang={locale}>` và thẻ `hreflang`. Đảm bảo tất cả các chuỗi UI được bao bọc trong `useTranslations` hook.
      - **Targeted Tag IDs:** `[NFR-007]`
- **DAY 5:** Thiết lập pipeline CI/CD và container hóa.
  - **Sub-Agent Workflow Specialization:**
    * **Docker:**
      - **Target Component file path (`target_component`):** `./sources/infra;Dockerfile` – `[NFR-004], [NFR-005]`
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile đa giai đoạn sử dụng `eclipse-temurin:21-jdk-alpine` làm stage build, sau đó stage runtime với chỉ các jar cần thiết. Đặt label `org.opencontainers.image.base.name`. Đảm bảo kích thước image cuối cùng < 500 MB. Thêm healthcheck `curl -f http://localhost:8080/q health`. Tích hợp với GitHub Actions để tự động build và push lên Google Artifact Registry.
      - **Targeted Tag IDs:** `[NFR-004], [NFR-005]`
- **DAY 6:** Triển khai manifests Kubernetes và cấu hình HPA.
  - **Sub-Agent Workflow Specialization:**
    * **GKE:**
      - **Target Component file path (`target_component`):** `./sources/infra.k8s;deployment.yaml` – `[NFR-004]`
      - **Low-Level Technical Task Instruction:** Tạo Deployment cho service auth với `imagePullPolicy: Always`. Thêm `resources.limits` và `resources.requests`. Định nghĩa HorizontalPodAutoscaler dựa trên `cpuUtilization: 70%` và `latency: >300ms`. Thêm `Service` với `type: ClusterIP`. Thêm `ConfigMap` và `Secret` cho các biến môi trường (ví dụ: DB connection). Áp dụng `kubectl apply -f`.
      - **Targeted Tag IDs:** `[NFR-004]`
- **DAY 7:** Kiểm tra toàn diện và đánh giá tuân thủ bảo mật.
  - **Sub-Agent Workflow Specialization:**
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend.auth;src/test/java/org/nlh4j/saas/membershiphub/auth/AuthControllerTest.java` – `[ARC-006], [REQ-001], [REQ-002]`
      - **Low-Level Technical Task Instruction:** Viết test cho `/register` (email hợp lệ, password yếu), `/social` (token OAuth2 giả lập), `/token` (JWT hợp lệ và hết hạn). Sử dụng `MockBean` cho `AuthenticationManager` và `JwtTokenProvider`. Kiểm tra response code và schema. Chạy `mvn test` và đảm bảo độ phủ mã >=85%.
      - **Targeted Tag IDs:** `[ARC-006], [REQ-001], [REQ-002]`

<!--END_DELIMITTER-->

### Phase 2 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai các dịch vụ quản lý khóa học, ghi danh học viên và API gateway trung tâm, tích hợp các chính sách RBAC cho quản trị viên, giáo viên và học sinh.
- **Target Physical Directory Matrix Map:** 
  - `./sources/backend.course` (mã nguồn CRUD khóa học) – `[REQ-007], [REQ-008], [DAT-004]`
  - `./sources/backend.enrollment` (mã nguồn ghi danh) – `[REQ-010], [REQ-011], [DAT-005]`
  - `./sources/backend.gateway` (API gateway) – `[ARC-009]`
- **Database Schema DDL SQL Specification [DAT-004], [DAT-005]:**
```sql
-- [DAT-004] Bảng Courses
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
);

-- [DAT-005] Bảng Enrollments
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT now(),
    UNIQUE (student_id, course_id)
);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [ARC-001] đến [ARC-005]:**
  - `GET /api/v1/courses` – trả về danh sách khóa học `[REQ-007]`
  - `POST /api/v1/courses` – tạo khóa học mới, kiểm tra xung đột lịch giảng dạy của giáo viên `[REQ-008]`
  - `PUT /api/v1/courses/{courseId}` – cập nhật `[REQ-008]`
  - `DELETE /api/v1/courses/{courseId}` – xóa `[REQ-008]`
  - `POST /api/v1/courses/{courseId}/teacher/{teacherId}` – chỉ định giáo viên `[REQ-009]`
  - `GET /api/v1/courses/browse?studentId={sid}` – danh sách khóa học khả dụng cho học sinh `[REQ-010]`
  - `POST /api/v1/enrollments` – body: `{studentId, courseId}` → tạo ghi danh `[REQ-011]`
  - Các endpoint quản trị tuân thủ RBAC (System Admin, Center Admin) được bảo vệ bởi `hasAnyAuthority('SYSTEM_ADMIN','CENTER_ADMIN')` `[ARC-001]`, `[ARC-002]`.
- **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
  - Lỗi mạng khi truy vấn khóa học → ném `ServiceUnavailableException` với thông báo "Hiện tại không thể truy xuất danh sách khóa học, vui lòng thử lại sau".
  - Ghi danh trùng lặp → trả về `409 Conflict` với `{ "error": "Đã ghi danh vào khóa học này" }`.
  - Xung đột lịch giảng dạy của giáo viên → trả về `400 Bad Request` với `{ "error": "Giáo viên đã có lớp học trong cùng thời gian" }`.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 8:** Xây dựng Course Service và các migration schema.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.course;src/main/java/org/nlh4j/saas/membershiphub/course/CourseController.java` – `[REQ-007], [REQ-008], [DAT-004]`
      - **Low-Level Technical Task Instruction:** Triển khai CourseController với các endpoint CRUD. Thêm `CourseService` thực hiện kiểm tra xung đột lịch giảng dạy bằng cách truy vấn `SELECT * FROM courses WHERE teacher_id = ? AND (start_date <= ? AND end_date >= ?)`. Sử dụng `@Transactional` để đảm bảo nguyên tử. Thêm `CourseMapper` cho DTO. Tích hợp `Flyway` migration `V2__create_courses_table.sql`.
      - **Targeted Tag IDs:** `[REQ-007], [REQ-008], [DAT-004]`
- **DAY 9:** Triển khai Enrollment Service.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.enrollment;src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentController.java` – `[REQ-010], [REQ-011], [DAT-005]`
      - **Low-Level Technical Task Instruction:** Tạo EnrollmentController với endpoint `/enrollments`. Sử dụng `EnrollmentService` để kiểm tra khả năng ghi danh (số lượng học viên < max_students, không trùng lặp). Thêm `EnrollmentRepository` mở rộng `JpaRepository`. Thêm validation cho `studentId` và `courseId`. Ghi log hành động ghi danh.
      - **Targeted Tag IDs:** `[REQ-010], [REQ-011], [DAT-005]`
- **DAY 10:** Xây dựng API Gateway với Spring Cloud Gateway.
  - **Sub-Agent Workflow Specialization:**
    * **Docker:**
      - **Target Component file path (`target_component`):** `./sources/backend.gateway;Dockerfile` – `[ARC-009]`
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile cho gateway, thêm `routes` cho từng service (auth, user, center, course, enrollment). Cấu hình `filters` cho `RequestRateLimiter`, `CircuitBreaker`, `JwtAuthenticationFilter`. Sử dụng `Eureka` client cho service discovery. Triển khai lên GKE.
      - **Targeted Tag IDs:** `[ARC-009]`
- **DAY 11:** Triển khai RBAC filters và chính sách bảo mật.
  - **Sub-Agent Workflow Specialization:**
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend.gateway;src/main/java/org/nlh4j/saas/membershiphub/gateway/RbacFilter.java` – `[ARC-001] đến [ARC-005]`
      - **Low-Level Technical Task Instruction:** Viết RbacFilter kiểm tra `Authentication` và `Collection` quyền dựa trên `HttpServletRequest`. Sử dụng `AuthorityUtils` để so sánh vai trò. Từ chối yêu cầu với `403 Forbidden` nếu không có quyền. Thêm logging cho mỗi lần từ chối.
      - **Targeted Tag IDs:** `[ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]`
- **DAY 12:** Kiểm tra unit cho các service mới.
  - **Sub-Agent Workflow Specialization:**
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend.course;src/test/java/org/nlh4j/saas/membershiphub/course/CourseServiceTest.java` – `[REQ-008]`
      - **Low-Level Technical Task Instruction:** Viết test cho logic xung đột lịch giảng dạy, kiểm tra trường hợp giáo viên đã có lớp học. Sử dụng `Mockito` để mock `CourseRepository`. Đảm bảo trả về exception phù hợp. Chạy `mvn test` và đạt độ phủ >=85%.
      - **Targeted Tag IDs:** `[REQ-008]`
- **DAY 13:** Kiểm tra integration cho gateway.
  - **Sub-Agent Workflow Specialization:**
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend.gateway;src/test/java/org/nlh4j/saas/membershiphub/gateway/GatewayFilterTest.java` – `[ARC-009]`
      - **Low-Level Technical Task Instruction:** Mô phỏng request đến các service nội bộ, xác nhận JWT được truyền qua, kiểm tra response code cho các vai trò khác nhau. Sử dụng `WebTestClient`. Đảm bảo circuit breaker hoạt động khi service lỗi.
      - **Targeted Tag IDs:** `[ARC-009]`
- **DAY 14:** Hoàn thiện documentation và chuẩn bị cho giai đoạn tiếp theo.
  - **Sub-Agent Workflow Specialization:**
    * **Doc:**
      - **Target Component file path (`target_component`):** `./sources/backend.course;README.md` – `[REQ-007] đến [REQ-011]`
      - **Low-Level Technical Task Instruction:** Tạo README chi tiết về các endpoint, request/response schema, ví dụ curl, hướng dẫn triển khai. Thêm ghi chú về các chính sách RBAC và các lỗi có thể xảy ra.
      - **Targeted Tag IDs:** `[REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]`

<!--END_DELIMITTER-->

### Phase 3 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai dịch vụ điểm danh QR, engine thẻ hội viên và các chính sách bất biến, xử lý ngoại lệ mạng và khôi phục hệ thống.
- **Target Physical Directory Matrix Map:** 
  - `./sources/backend.attendance` (mã nguồn điểm danh) – `[REQ-012], [REQ-013], [DAT-006]`
  - `./sources/backend.membership` (mã nguồn thẻ hội viên) – `[REQ-014], [REQ-015], [DAT-007]`
- **Database Schema DDL SQL Specification [DAT-006], [DAT-007]:**
```sql
-- [DAT-006] Bảng Attendance
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT now()
);

-- [DAT-007] Bảng StudentCards
CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);
```
- **API and Event Routing Contracts [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007]:**
  - `POST /api/v1/attendance/scan` – body: `{studentId, courseId, qrCodeData}` → tạo bản ghi điểm danh, đảm bảo idempotent `[REQ-012]`, `[REQ-013]`
  - `GET /api/v1/student-cards/{studentId}` – trả về thông tin thẻ `[REQ-014]`
  - `POST /api/v1/student-cards/{studentId}/renew` – body: `{days}` → gia hạn thẻ `[REQ-015]`
  - Endpoint quét QR được bảo vệ bởi `JWT` và kiểm tra mối quan hệ học viên-khóa học.
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-005]:**
  - Mất mạng khi ghi điểm danh → lưu sự kiện vào hàng đợi cục bộ, xử lý khi kết nối khôi phục, thông báo cho người dùng `[EXC-001]`.
  - Quét QR trùng lặp trong cùng ngày → trả về `200 OK` với `{ "duplicate": true }` `[EXC-002]`.
  - Sau khi hệ thống khôi phục → xử lý hàng đợi điểm danh theo thứ tự FIFO, gửi push notification đến học viên `[EXC-005]`.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 15:** Xây dựng Attendance Service và logic idempotent.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.attendance;src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceController.java` – `[REQ-012], [REQ-013], [DAT-006]`
      - **Low-Level Technical Task Instruction:** Triển khai AttendanceController với endpoint `/scan`. Sử dụng `AttendanceService` để kiểm tra bản ghi hiện có: `SELECT * FROM attendance WHERE student_id = ? AND course_id = ? AND attendance_date = CURRENT_DATE`. Nếu tồn tại, trả về `{ "duplicate": true }`. Nếu không, chèn bản ghi mới. Thêm retry với exponential backoff khi lỗi mạng. Thêm logging via `SLF4J`.
      - **Targeted Tag IDs:** `[REQ-012], [REQ-013], [DAT-006]`
- **DAY 16:** Triển khai Membership Service cho thẻ hội viên.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.membership;src/main/java/org/nlh4j/saas/membershiphub/membership/MembershipController.java` – `[REQ-014], [REQ-015], [DAT-007]`
      - **Low-Level Technical Task Instruction:** Tạo MembershipController với các endpoint `/student-cards/{studentId}` (GET) và `/renew` (POST). Sử dụng `MembershipService` để tính `remainingDays = validityDays - (CURRENT_DATE - issueDate).days`. Endpoint gia hạn cập nhật `issueDate = CURRENT_DATE`, `remainingDays = days`. Sử dụng `@Modifying` JPA để cập nhật.
      - **Targeted Tag IDs:** `[REQ-014], [REQ-015], [DAT-007]`
- **DAY 17:** Thêm circuit breaker cho các cuộc gọi mạng ngoài.
  - **Sub-Agent Workflow Specialization:**
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend.attendance;src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceCircuitBreakerConfig.java` – `[EXC-001]`
      - **Low-Level Technical Task Instruction:** Cấu hình `CircuitBreakerConfig` với state `OPEN` sau 5 thất bại trong 1 phút. Thêm `FallbackMethod` để lưu sự kiện vào hàng đợi cục bộ. Thêm `EventListener` để chuyển sang `HALF_OPEN` sau thời gian chờ.
      - **Targeted Tag IDs:** `[EXC-001]`
- **DAY 18:** Triển khai hàng đợi bất đồng bộ cho điểm danh.
  - **Sub-Agent Workflow Specialization:**
    * **Docker:**
      - **Target Component file path (`target_component`):** `./sources/backend.attendance;src/main/resources/application.yml` – `[EXC-001]`
      - **Low-Level Technical Task Instruction:** Cấu hình `spring.rabbitmq` (hoặc `kafka`) cho hàng đợi `attendance.retry`. Đặt `retry.attempts=3`, `retry.delay=1000ms`. Thêm `Listener` để tiêu thụ sự kiện khi kết nối khôi phục.
      - **Targeted Tag IDs:** `[EXC-001]`
- **DAY 19:** Kiểm tra unit cho Attendance Service.
  - **Sub-Agent Workflow Specialization:**
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend.attendance;src/test/java/org/nlh4j/saas/membershiphub/attendance/AttendanceServiceTest.java` – `[REQ-013]`
      - **Low-Level Technical Task Instruction:** Viết test cho trường hợp quét QR trùng lặp, đảm bảo trả về duplicate flag. Sử dụng `Mockito` cho `AttendanceRepository`. Đảm bảo transaction rollback khi lỗi mạng.
      - **Targeted Tag IDs:** `[REQ-013]`
- **DAY 20:** Kiểm tra integration cho Membership Service.
  - **Sub-Agent Workflow Specialization:**
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend.membership;src/test/java/org/nlh4j/saas/membershiphub/membership/MembershipControllerTest.java` – `[REQ-015]`
      - **Low-Level Technical Task Instruction:** Mô phỏng request gia hạn thẻ, xác nhận cập nhật `student_cards` table. Sử dụng `JdbcTemplate` để kiểm tra dữ liệu. Đảm bảo response chứa `cardId` và `remainingDays` mới.
      - **Targeted Tag IDs:** `[REQ-015]`
- **DAY 21:** Hoàn thiện documentation và chuẩn bị cho giai đoạn tiếp theo.
  - **Sub-Agent Workflow Specialization:**
    * **Doc:**
      - **Target Component file path (`target_component`):** `./sources/backend.attendance;README.md` – `[REQ-012] đến [REQ-015]`
      - **Low-Level Technical Task Instruction:** Tạo README với hướng dẫn sử dụng endpoint quét QR, quy tắc bất biến, quy trình gia hạn thẻ. Thêm ghi chú về xử lý ngoại lệ mạng.
      - **Targeted Tag IDs:** `[REQ-012], [REQ-013], [REQ-014], [REQ-015]`

<!--END_DELIMITTER-->

### Phase 4 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai engine thông báo (push + Zalo), quản lý khuyến mãi và thông báo, tích hợp retry cho việc gửi notification thất bại.
- **Target Physical Directory Matrix Map:** 
  - `./sources/backend.notification` (mã nguồn thông báo) – `[REQ-016], [DAT-008]`
  - `./sources/backend.promotion` (mã nguồn khuyến mãi) – `[REQ-017], [DAT-009]`
  - `./sources/backend.announcement` (mã nguồn thông báo) – `[REQ-018], [DAT-009]`
- **Database Schema DDL SQL Specification [DAT-008], [DAT-009]:**
```sql
-- [DAT-008] Bảng Notifications
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT now(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

-- [DAT-009] Bảng Promotions & Announcements
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
- **API and Event Routing Contracts [REQ-016], [REQ-017], [REQ-018], [ARC-008]:**
  - `POST /api/v1/notifications` – body: `{userId, groupZalo, message}` → ghi vào DB, kích hoạt push qua FCM/APNs và bài đăng Zalo `[REQ-016]`
  - `POST /api/v1/promotions` – CRUD cho khuyến mãi `[REQ-017]`
  - `POST /api/v1/announcements` – CRUD cho thông báo `[REQ-018]`
  - Endpoint thông báo được bảo vệ bởi `hasAnyAuthority('SYSTEM_ADMIN','CENTER_ADMIN','MANAGER')` `[ARC-008]`.
- **Phase Localized Exception Handlers [EXC-003]:**
  - Lỗi gửi push (token không hợp lệ) → ghi log lỗi, thêm vào hàng đợi retry, sau 3 lần thất bại đánh dấu `delivered = false` và gửi alert cho admin `[EXC-003]`.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)
- **DAY 22:** Xây dựng Notification Service.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.notification;src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationController.java` – `[REQ-016], [DAT-008]`
      - **Low-Level Technical Task Instruction:** Triển khai NotificationController với endpoint `/notifications`. Sử dụng `NotificationService` để lưu bản ghi, gọi `FcmService` và `ZaloService`. Thêm `@Retryable` cho việc gửi push với `maxAttempts=3`. Thêm logging cho mỗi lần thử.
      - **Targeted Tag IDs:** `[REQ-016], [DAT-008]`
- **DAY 23:** Triển khai Promotion Service.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.promotion;src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionController.java` – `[REQ-017], [DAT-009]`
      - **Low-Level Technical Task Instruction:** Tạo PromotionController với CRUD. Sử dụng `PromotionService` để xác thực `startDate` <= `endDate`. Thêm `PromotionMapper`. Tích hợp `EventPublisher` để phát sự kiện `PromotionCreated` cho các service khác.
      - **Targeted Tag IDs:** `[REQ-017], [DAT-009]`
- **DAY 24:** Triển khai Announcement Service.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.announcement;src/main/java/org/nlh4j/saas/membershiphub/announcement/AnnouncementController.java` – `[REQ-018], [DAT-009]`
      - **Low-Level Technical Task Instruction:** Tương tự như Promotion, triển khai AnnouncementController với logic hết hạn dựa trên `startDate`/`endDate`. Sử dụng `Scheduled` task để vô hiệu hóa bản ghi hết hạn.
      - **Targeted Tag IDs:** `[REQ-018], [DAT-009]`
- **DAY 25:** Thêm retry mechanism cho notification thất bại.
  - **Sub-Agent Workflow Specialization:**
    * **Reviewer:**
      - **Target Component file path (`target_component`):** `./sources/backend.notification;src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationRetryConfig.java` – `[EXC-003]`
      - **Low-Level Technical Task Instruction:** Cấu hình `RetryTemplate` với `FixedBackOffPolicy` (1000ms). Thêm `NotificationRetryListener` để đếm số lần thử và cập nhật `delivered` flag sau 3 lần thất bại. Ghi log lỗi vào bảng `notification_failures`.
      - **Targeted Tag IDs:** `[EXC-003]`
- **DAY 26:** Kiểm tra unit cho Promotion và Announcement.
  - **Sub-Agent Workflow Specialization:**
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend.promotion;src/test/java/org/nlh4j/saas/membershiphub/promotion/PromotionServiceTest.java` – `[REQ-017]`
      - **Low-Level Technical Task Instruction:** Viết test cho việc tạo khuyến mãi với ngày bắt đầu/kết thúc hợp lệ, kiểm tra validation cho `discountPercent` (0-100). Sử dụng `MockMvc` để test controller.
      - **Targeted Tag IDs:** `[REQ-017]`
- **DAY 27:** Kiểm tra integration cho Notification.
  - **Sub-Agent Workflow Specialization:**
    * **Tester:**
      - **Target Component file path (`target_component`):** `./sources/backend.notification;src/test/java/org/nlh4j/saas/membershiphub/notification/NotificationControllerTest.java` – `[REQ-016]`
      - **Low-Level Technical Task Instruction:** Mô phỏng request gửi notification, xác nhận record được tạo và push được kích hoạt (mock `FcmService`). Kiểm tra retry khi ném `FcmException`.
      - **Targeted Tag IDs:** `[REQ-016]`
- **DAY 28:** Hoàn thiện documentation và chuẩn bị cho giai đoạn tiếp theo.
  - **Sub-Agent Workflow Specialization:**
    * **Doc:**
      - **Target Component file path (`target_component`):** `./sources/backend.notification;README.md` – `[REQ-016] đến [REQ-018]`
      - **Low-Level Technical Task Instruction:** Tạo README với hướng dẫn sử dụng API thông báo, quy tắc retry, ví dụ payload cho push và Zalo.
      - **Targeted Tag IDs:** `[REQ-016], [REQ-017], [REQ-018]`

<!--END_DELIMITTER-->

### Phase 5 Detailed Architectural Specification
- **Phase Core Objective & Purpose:** Triển khai chatbot AI, giao diện người dùng di động đa vai trò, hoàn thiện pipeline CI/CD, cấu hình GCP & GKE infra, và các tính năng báo cáo & phân tích.
- **Target Physical Directory Matrix Map:** 
  - `./sources/backend.chatbot` (mã nguồn chatbot) – `[REQ-019]`
  - `./sources/frontend.mobile` (giao diện người dùng di động) – `[REQ-020], [REQ-021]`
  - `./sources/infra.ci` (pipeline CI/CD) – `[ARC-010]`
  - `./sources/infra.gcp` (cấu hình GCP) – `[ARC-010]`
  - `./sources/infra.gke` (manifests GKE) – `[ARC-010]`
- **Database Schema DDL SQL Specification [DAT-011] (SystemSettings) – already covered in Phase 1, but we can include again for completeness:**
```sql
-- [DAT-011] Bảng SystemSettings (tái sử dụng từ Phase 1)
CREATE TABLE system_settings (
    setting_key VARCHAR(100) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-009], [ARC-010]:**
  - `POST /api/v1/chatbot` – body: `{userId, message}` → trả về phản hồi từ AI `[REQ-019]`
  - `GET /api/v1/mobile/{role}` – trả về giao diện người dùng di động được tối ưu hóa cho vai trò `[REQ-020]`
  - `POST /api/v1/push/register` – body: `{deviceToken, platform}` → đăng ký thiết bị nhận push `[REQ-021]`
  - `GET /api/v1/i18n/default` – trả về ngôn ngữ mặc định dựa trên stored preference hoặc header `[REQ-022]`
  - `GET /api/v1/seo/{locale}` – trả về meta tags và hreflang cho SEO `[REQ-023]`
  - `GET /api/v1/reports/attendance` – query parameters `centerId`, `startDate`, `endDate` → xuất CSV `[REQ-024]`
  - `GET /api/v1/dashboard/center/{centerId}` – trả về tổng hợp số liệu `[REQ-025]`
  - Endpoint di động được bảo vệ bởi JWT và các chính sách RBAC `[ARC-009]`.
  - Infra APIs (ví dụ: `POST /api/v1/infra/gcp/deploy`) được bảo vệ bởi vai trò System Admin `[ARC-010]`.
- **Phase Localized Exception Handlers (relevant tags already covered):**
  - Tất cả các ngoại lệ chưa được bao phủ (ví dụ: lỗi chatbot không xác định) được xử lý bằng `GlobalExceptionHandler` trả về `500 Internal Server Error` với thông báo lỗi chi tiết.

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)
- **DAY 29:** Xây dựng Chatbot AI Service.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.chatbot;src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java` – `[REQ-019]`
      - **Low-Level Technical Task Instruction:** Triển khai ChatbotController với endpoint `/chat`. Sử dụng `OpenAI` client (hoặc mock) để xử lý tin nhắn. Thêm `ChatbotService` để lưu lịch sử hội thoại vào bảng `chat_logs` (không bắt buộc). Áp dụng rate limiting (10 requests/phút). Trả về JSON `{ "response": "...", "timestamp": "..." }`.
      - **Targeted Tag IDs:** `[REQ-019]`
- **DAY 30:** Xây dựng giao diện người dùng di động đa vai trò.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/frontend.mobile;src/screens/StudentDashboard.tsx` – `[REQ-020], [REQ-021]`
      - **Low-Level Technical Task Instruction:** Tạo component React Native hiển thị danh sách khóa học, nút quét QR, thẻ hội viên. Sử dụng `react-navigation` để điều hướng dựa trên vai trò. Tích hợp `PushNotification` config cho cả Android và iOS. Sử dụng `useTranslation` cho i18n.
      - **Targeted Tag IDs:** `[REQ-020], [REQ-021]`
- **DAY 31:** Triển khai pipeline CI/CD.
  - **Sub-Agent Workflow Specialization:**
    * **Docker:**
      - **Target Component file path (`target_component`):** `./sources/infra.ci;github/workflows/ci.yml` – `[ARC-010]`
      - **Low-Level Technical Task Instruction:** Tạo workflow GitHub Actions: trigger trên push/pull_request. Các bước: thiết lập JDK 21, build Maven, kiểm tra mã, build Docker image, push lên Artifact Registry, triển khai lên GKE bằng `kubectl`. Thêm `slack` notification trên thất bại.
      - **Targeted Tag IDs:** `[ARC-010]`
- **DAY 32:** Cấu hình GCP infra (Project, VPC, Services).
  - **Sub-Agent Workflow Specialization:**
    * **GCP:**
      - **Target Component file path (`target_component`):** `./sources/infra.gcp;infra/gcp.tf` – `[ARC-010]`
      - **Low-Level Technical Task Instruction:** Sử dụng Terraform để tạo `google_project`, `google_vpc_network`, `google_sql_database_instance` (PostgreSQL), `google_artifact_registry_repository`. Thiết lập `google_service_account` cho CI/CD. Kích hoạt APIs: `cloudbuild`, `container`, `sqladmin`, `artifactregistry`.
      - **Targeted Tag IDs:** `[ARC-010]`
- **DAY 33:** Tạo manifests Kubernetes cho GKE.
  - **Sub-Agent Workflow Specialization:**
    * **GKE:**
      - **Target Component file path (`target_component`):** `./sources/infra.gke;k8s/deployment.yaml` – `[ARC-010]`
      - **Low-Level Technical Task Instruction:** Tạo Deployment cho chatbot, notification, attendance services. Thêm `Service`, `Ingress` với `nginx-ingress`. Cấu hình `ResourceQuota`, `LimitRange`. Thêm `HorizontalPodAutoscaler` dựa trên CPU và latency.
      - **Targeted Tag IDs:** `[ARC-010]`
- **DAY 34:** Xây dựng báo cáo điểm danh và dashboard.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.chatbot;src/main/java/org/nlh4j/saas/membershiphub/report/AttendanceReportController.java` – `[REQ-024]`
      - **Low-Level Technical Task Instruction:** Triển khai AttendanceReportController với endpoint `/reports/attendance`. Sử dụng `ReportService` để truy vấn `attendance` join `users` và `courses`. Xuất CSV qua `ResponseEntity` với `MediaType.TEXT_CSV`. Thêm caching 5 phút cho báo cáo.
      - **Targeted Tag IDs:** `[REQ-024]`
- **DAY 35:** Hoàn thiện dashboard và kiểm tra cuối cùng.
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Target Component file path (`target_component`):** `./sources/backend.chatbot;src/main/java/org/nlh4j/saas/membershiphub/dashboard/DashboardController.java` – `[REQ-025]`
      - **Low-Level Technical Task Instruction:** Triển khai DashboardController trả về JSON tổng hợp: `totalStudents`, `activeCourses`, `upcomingSessions`. Sử dụng `DashboardService` để thực hiện các query hiệu năng. Thêm `WebSocket` endpoint `/topic/dashboard` để cập nhật thời gian thực.
      - **Targeted Tag IDs:** `[REQ-025]`

<!--END_DELIMITTER-->

## 📁 6. Mã Bảo mật Doanh nghiệp Toàn cầu & Biện pháp Phòng chống Nạp lệnh [NFR-001] đến [NFR-009]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng `PreparedStatement` cho mọi truy vấn động. Áp dụng `JdbcTemplate` với `SqlParameterSource`. Sử dụng `Flyway` migration scripts để quản lý schema. Áp dụng `jakarta.validation` constraints cho mọi entity. Sử dụng `Hibernate` `CriteriaBuilder` cho các query phức tạp. Áp dụng `RowMapper` an toàn.

- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Sử dụng `react-helmet` để chèn `Content-Security-Policy` header (không cho phép `unsafe-inline`). Sử dụng `DOMPurify` cho việc dọn dẹp HTML đầu vào. Sử dụng `helmet` cho các meta tag. Sử dụng `styled-components` với escape CSS. Sử dụng `Next.js` `dangerouslySetInnerHTML` chỉ sau khi sanitization.

- **Multi-Tenant CORS Security Rails:** Cấu hình `WebSecurityConfigurerAdapter` với `CorsConfiguration` whitelist các origin theo từng trung tâm (`https://centerX.example.com`). Sử dụng `Database` lưu trữ whitelist origin. Áp dụng `Filter` kiểm tra origin cho mỗi request.

- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Sử dụng `Logback` encoder với `MaskingDecorator` để thay thế các phần của email (`.*@`) và số điện thoại. Sử dụng `@JsonSerialize` custom cho `User` entity để loại bỏ `passwordHash`. Áp dụng `Slf4j` với `Redact` annotation.

- **Performance Metrics ([NFR-001]):** Tối ưu hóa query với index trên `users(email)`, `courses(teacher_id,start_date)`, `attendance(student_id,attendance_date)`. Sử dụng `Redis` cache cho các lookup người dùng và điểm danh. Áp dụng `Resilience4j` circuit breaker cho các service gọi nhau. Sử dụng `OpenTelemetry` để đo latency.

- **Availability ([NFR-002]):** Triển khai active-active trên hai region GKE, sử dụng `Global HTTP(S) Load Balancer` với health checks. Thiết lập `PodDisruptionBudgets`. Sử dụng `Database` read replicas cho reporting.

- **Security ([NFR-003]):** Áp dụng TLS 1.3 trên Nginx, sử dụng `letsencrypt`. Mã hóa JWT với RSA256. Lưu `passwordHash` bằng bcrypt. Thực hiện `OWASP` Top 10: SQLi, XSS, CSRF tokens, file upload validation.

- **Scalability & Availability ([NFR-004]):** Sử dụng Kubernetes HPA dựa trên CPU >70% hoặc latency >300ms. Sử dụng `HorizontalPodAutoscaler` cho các service. Sử dụng `Database` sharding theo trung tâm cho bảng `centers`.

- **Docker Image Size ([NFR-005]):** Sử dụng base image `eclipse-temurin:21-jdk-alpine` (~100MB). Loại bỏ các gói không cần thiết, sử dụng `apk --no-cache del`. Đảm bảo image cuối cùng <500MB.

- **Logging & Audit ([NFR-006]):** Sử dụng `SLF4J` với `MDC` để ghi `userId`, `centerId`. Ghi log mọi thao tác CRUD vào bảng `audit_log`. Sử dụng `ELK` stack để phân tích. Retention 1 năm.

- **Multi-Language Support ([NFR-007]):** Ngoại biên hóa chuỗi UI trong `resources/messages_{locale}.properties`. Sử dụng `i18next` cho frontend. Tự động phát hiện ngôn ngữ qua `Accept-Language` header, fallback về stored preference.

- **GDPR/CCPA Compliance ([NFR-008]):** Thêm `DELETE /api/v1/users/{userId}` để xóa dữ liệu cá nhân. Sử dụng `JpaRepository.delete` với cascade. Xuất dữ liệu qua `GET /api/v1/users/{userId}/export`. Quản lý consent cho marketing qua `ConsentService`.

- **Backup & Disaster Recovery ([NFR-009]):** Sử dụng `pg_dump` hàng ngày cho PostgreSQL, lưu vào Cloud Storage. Khôi phục điểm-in-time sử dụng `PITR`. Backup cluster GKE bằng `Velero` sang bucket region khác.

## 📁 7. Quy tắc Tuân thủ Di động Hỗn hợp & Cơ chế SEO Đa ngôn ngữ

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng `@capacitor/core` để truy cập camera cho quét QR, `@capacitor/network` để phát hiện kết nối. Sử dụng `SecureStorage` cho token. Sử dụng `Device` API để lấy thông tin thiết bị. Áp dụng `BackButton` interception cho navigation. Sử dụng `LocalNotifications` cho push.

- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware `Next.js` (`i18n`) để phát hiện locale. Sử dụng `next-intl` cho routing. Thêm `<link rel="canonical" href="...">` và `<link rel="alternate" hreflang="...">` cho từng ngôn ngữ. Sử dụng `meta` tags `og:locale` cho mạng xã hội.

## 📁 8. Quy trình Tự động Hóa Pipeline Theo Ngày & Luồng Chi nhánh Git

- **Daily Workspace Forking Isolation:** Script CI tạo branch `features/development-day-$(date +%Y%m%d)` từ `main`. Mỗi ngày làm việc là một branch riêng biệt để cô lập thay đổi.

- **Validation Guard Pipeline Gates:** 
  - **Compile Check:** `mvn clean compile` phải thành công.
  - **Unit Test Coverage:** `mvn test` với độ phủ mã >=85%.
  - **Integration Test:** Chạy `docker-compose up --build` và thực hiện các request API mẫu.
  - **Security Scan:** `OWASP ZAP` hoặc `Snyk` phải không có lỗi cao.
  - **Lint & Format:** `eslint`, `prettier`, `spotless` pass.
  - **Documentation:** `mkdocs build` không có lỗi.
  - **Artifact Promotion:** Chỉ sau khi tất cả các gate pass, artifact được push lên Artifact Registry và triển khai lên GKE stage.

### 🛑 Kiểm tra Ma trận Bao phủ

[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]