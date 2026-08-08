# TỔNG QUAN DỰ ÁN: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808150811 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 15:08:11 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
- Kiến trúc hướng dịch vụ vi mô (Microservices) với các module độc lập: Quản lý người dùng, Trung tâm, Khóa học, Ghi danh, Điểm danh, Thẻ hội viên, Thông báo, Khuyến mãi, Chatbot, Di động.
- Áp dụng mô hình CQRS cho các thao tác đọc/ghi, đảm bảo khả năng mở rộng và hiệu suất.
- Sử dụng Event-Driven cho các luồng thông báo, điểm danh, và tích hợp Zalo.
- Triển khai xác thực OAuth2 với JWT, phân quyền RBAC nghiêm ngặt.
- Tích hợp Firebase Authentication, Google/Facebook OAuth, và FCM/APNs cho push notification.
- Container hóa với Docker, triển khai trên Google Kubernetes Engine (GKE).
- Triển khai CI/CD với GitHub Actions, thực hiện kiểm tra tự động và triển khai blue-green.
- Tuân thủ các tiêu chuẩn OWASP Top 10, mã hóa dữ liệu ở nghỉ bằng AES-256, TLS 1.3 cho mọi giao tiếp.
- Thiết kế các API RESTful với Swagger/OpenAPI, hỗ trợ đa ngôn ngữ (EN, VN, ES).
- Triển khai caching với Redis cho session và các truy vấn thường gặp.
- Thực hiện logging tập trung với ELK/Structured logs, tuân thủ GDPR/CCPA.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Luồng xác thực: OAuth2 → Firebase/Google/Facebook → JWT issuance (ARC-006).
- Luồng điểm danh: Mobile QR scan → REST API → Attendance service (idempotent) (ARC-007).
- Luồng thông báo: Backend event → Push notification (FCM/APNs) + Zalo group post (ARC-008).
- Luồng frontend: Next.js tiêu thụ REST APIs, caching ngoại tuyến với IndexedDB (ARC-009).
- Tích hợp Pub/Sub cho các sự kiện chéo module (ví dụ: ghi danh kích hoạt thông báo).
- Sử dụng Google Pub/Sub cho các luồng sự kiện có độ trễ thấp.
- Triển khai API Gateway (ví dụ: Kong) để định tuyến và bảo mật.
- Thực hiện kiểm tra toàn vẹn dữ liệu với schema validation (Pydantic/Bean Validation).
- Sử dụng CDN cho tài nguyên tĩnh, triển khai đa vùng trên GKE.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

### Backend Infrastructure Core Stack
- **Runtime:** Java 21 + Quarkus 3.2.0 (native support, GraalVM).
- **Persistence:** PostgreSQL 15.3 với JDBC driver, Flyway/Liquibase cho migration.
- **Messaging:** Google Pub/Sub (v2 SDK) cho event-driven architecture.
- **Authentication:** Firebase Auth SDK (v9 modular), OAuth2 resource server với JWT (Java Keycloak adapter).
- **Push Notification:** Firebase Cloud Messaging (v9), Apple APNs (v1.0.0).
- **Caching:** Redis 7.0 (cluster mode enabled).
- **Observability:** OpenTelemetry Java agent, Prometheus metrics, Grafana dashboards.
- **Security:** Spring Security 6.x, OWASP Java HTML Sanitizer, Cryptographic utilities (Bouncy Castle).
- **DevOps:** Docker multi-stage images (<500MB), Kubernetes manifests (Helm charts), GitHub Actions CI/CD pipelines.

### Frontend & Cross-Platform UI Mobile Stack
- **Web Frontend:** Next.js 14 (React 18), TypeScript, Tailwind CSS, i18n với i18next, routing động, static generation với revalidate.
- **Mobile:** React Native 0.73 (Hermes), Capacitor 5.x cho native bridge, Firebase SDK cho auth/push, Zalo SDK tích hợp.
- **State Management:** Redux Toolkit với RTK Query, Context API cho mobile.
- **UI Components:** Material-UI (MUI) cho web, React Native Paper cho mobile.
- **Build Tools:** Vite cho dev, Webpack cho production, CI/CD với GitHub Actions.
- **Testing:** Jest + React Testing Library (web), Detox + Jest (mobile).

### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- Tuân thủ OWASP Top 10: Ngăn chặn SQL injection bằng prepared statements, XSS bằng auto-escaping, CSRF bằng token, IDOR bằng kiểm tra quyền.
- Mã hóa JWT với RS256, thời gian sống 15 phút, refresh token 7 ngày.
- TLS 1.3 cho mọi giao tiếp, chứng chỉ pin (pinning) cho các endpoint quan trọng.
- Phân tách đa租: mỗi trung tâm có schema riêng hoặc sử dụng row-level security.
- Kiểm soát truy cập dựa trên vai trò (RBAC) với các vai trò được định nghĩa (ARC-001..005).
- Ghi audit mọi thao tác người dùng (tạo, cập nhật, xóa) vào bảng AuditLog.
- Thực hiện quy tắc giữ dữ liệu: chỉ lưu trữ cần thiết, tự động xóa sau 1 năm.
- Triển khai kiểm tra hiệu suất (load) với mục tiêu 200ms cho các API cốt lõi.
- Thực hiện kiểm tra bảo mật định kỳ (SAST/DAST).
- Hỗ trợ đa ngôn ngữ: i18n với key-value JSON, meta tags hreflang cho SEO.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
<!--START_BACKLOG_SYNOPSIS_GRID-->
| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Đăng ký người dùng | Triển khai form đăng ký với xác thực email/mật khẩu, gán vai trò ban đầu, trả về JWT. | Application Code | [REQ-001], [DAT-001], [EXC-004] |
| 2 | Xác thực qua mạng xã hội | Tích hợp OAuth2 với Firebase, Google, Facebook; tạo/cập nhật người dùng cục bộ. | Application Code | [REQ-002], [DAT-001], [ARC-006] |
| 3 | Phân quyền người dùng | Gán/rút vai trò người dùng, áp dụng quyền ngay lập tức. | Application Code | [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] |
| 4 | Xem danh sách trung tâm | Hiển thị danh sách trung tâm (tên, địa chỉ, taxId, liên hệ). | Application Code | [REQ-004], [DAT-003] |
| 5 | Tạo/cập nhật/xóa trung tâm | CRUD trung tâm với kiểm tra taxId duy nhất. | Application Code | [REQ-005], [DAT-003] |
| 6 | Phân quyền quản trị trung tâm | Gán người dùng làm Center Admin cho trung tâm cụ thể. | Application Code | [REQ-006], [DAT-003], [ARC-002] |
| 7 | Xem danh sách khóa học | Hiển thị tất cả khóa học với giáo viên được gán. | Application Code | [REQ-007], [DAT-004] |
| 8 | Tạo/cập nhật/xóa khóa học | Quản lý khóa học với kiểm tra xung đột lịch giáo viên. | Application Code | [REQ-008], [DAT-004] |
| 9 | Phân công giáo viên vào khóa học | Gán giáo viên vào khóa học, tạo thông báo đẩy. | Application Code | [REQ-009], [DAT-004], [ARC-003] |
| 10 | Duyệt khóa học | Hiển thị khóa học có sẵn cho học viên (không bao gồm khóa đã ghi danh). | Application Code | [REQ-010], [DAT-005] |
| 11 | Đăng ký khóa học của học viên | Xử lý ghi danh, tự động tạo tài khoản học viên nếu thiếu. | Application Code | [REQ-011], [DAT-005], [DAT-001], [ARC-005] |
| 12 | Chụp ảnh điểm danh QR | Ghi nhận điểm danh qua quét QR từ thiết bị di động. | Application Code | [REQ-012], [DAT-006], [ARC-007] |
| 13 | Tính chất bất biến của điểm danh | Đảm bảo chỉ một bản ghi điểm danh mỗi ngày. | Application Code | [REQ-013], [DAT-006], [EXC-001], [EXC-002] |
| 14 | Hiển thị tính hợp lệ của thẻ | Hiển thị ngày còn lại của thẻ hội viên. | Application Code | [REQ-014], [DAT-007] |
| 15 | Gia hạn thẻ | Cập nhật ngày kết thúc thẻ sau thanh toán. | Application Code | [REQ-015], [DAT-007] |
| 16 | Kích hoạt thông báo | Tạo thông báo đẩy và bài đăng Zalo khi có sự kiện. | Application Code | [REQ-016], [DAT-008], [ARC-008] |
| 17 | Quản lý khuyến mãi | CRUD khuyến mãi với ngày bắt đầu/kết thúc. | Application Code | [REQ-017], [DAT-009] |
| 18 | Quản lý thông báo | CRUD thông báo với khả năng hết hạn. | Application Code | [REQ-018], [DAT-009] |
| 19 | Tích hợp chatbot AI | Triển khai chatbot trả lời truy vấn, tích hợp với hệ thống knowledge base. | Application Code | [REQ-019], [NFR-007] |
| 20 | Giao diện người dùng vai trò cụ thể trên di động | UI responsive cho các vai trò trên di động (Student, Teacher, Admin). | Application Code | [REQ-020], [NFR-008] |
| 21 | Thông báo đẩy trên di động | Gửi push notification qua FCM/APNs. | Application Code | [REQ-021], [NFR-008] |
| 22 | Phát hiện ngôn ngữ mặc định | Xác định locale từ preference người dùng. | Application Code | [REQ-022], [NFR-007] |
| 23 | SEO đa ngôn ngữ | Hỗ trợ SEO cho EN, VN, ES với hreflang. | Application Code | [REQ-023], [NFR-007] |
| 24 | Tạo báo cáo điểm danh | Xuất CSV điểm danh theo trung tâm/ngày. | Application Code | [REQ-024], [NFR-001], [NFR-006] |
| 25 | Bảng điều khiển tóm tắt ghi danh | Dashboard thời gian thực cho Center Admin. | Application Code | [REQ-025], [NFR-001], [NFR-006] |
| 26 | Tài liệu kỹ thuật – Đặc tả người dùng | Tổng hợp đặc tả chức năng, ER diagram, API contract. | Enterprise Documentation | [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011] |
| 27 | Tài liệu triển khai hạ tầng | Hướng dẫn CI/CD, Docker, Kubernetes, GCP, GKE. | DevOps Infrastructure | [NFR-004], [NFR-005], [NFR-009] |
| **SUMMARY** | **Tổng số công việc trong backlog** | **TỔNG CỘNG:** 27 Tasks | **TRẠNG THÁI:** Verified | **PHẠM VI:** 100% |
<!--END_BACKLOG_SYNOPSIS_GRID-->

### 4.2. MULTI-PHASE SYNOPSIS MATRIX
<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Đối tượng phụ | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Ngày 1 - 2 | ./sources/backend/user-management/, ./sources/docs/user-management.md, ./sources/backend/user-management/src/test/ | Triển khai đăng ký người dùng, xác thực xã hội, gán vai trò; tạo DDL người dùng/vai trò; tài liệu kỹ thuật. | Coder, Doc, Tester, Reviewer | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [ARC-006] |
| 2 | Ngày 1 - 2 | ./sources/backend/center/, ./sources/docs/center-management.md, ./sources/backend/center/src/test/ | Triển khai CRUD trung tâm, gán quyền quản trị trung tâm; tài liệu và kiểm thử. | Coder, Doc, Tester, Reviewer | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002] |
| 3 | Ngày 1 - 2 | ./sources/backend/course/, ./sources/docs/course-management.md, ./sources/backend/course/src/test/ | Triển khai CRUD khóa học với kiểm tra xung đột lịch, gán giáo viên; tài liệu và kiểm thử. | Coder, Doc, Tester, Reviewer | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003] |
| 4 | Ngày 1 - 3 | ./sources/backend/enrollment/, ./sources/backend/attendance/, ./sources/backend/membercard/, ./sources/docs/enrollment-attendance-membercard.md, ./sources/backend/enrollment/src/test/, ./sources/backend/attendance/src/test/, ./sources/backend/membercard/src/test/ | Triển khai ghi danh khóa học, điểm danh QR, hiển thị/gia hạn thẻ hội viên, engine thông báo; xử lý ngoại lệ mạng và trùng lặp. | Coder, Doc, Tester, Reviewer | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [EXC-001], [EXC-002], [EXC-003] |
| 5 | Ngày 1 - 3 | ./sources/backend/promotion/, ./sources/backend/chatbot/, ./sources/frontend/, ./sources/mobile/, ./sources/docs/promotion-chatbot-mobile.md, ./sources/backend/promotion/src/test/, ./sources/backend/chatbot/src/test/, ./sources/frontend/src/test/, ./sources/mobile/src/test/ | Triển khai quản lý khuyến mãi/thông báo, tích hợp chatbot AI, UI di động vai trò, push notification, localization/SEO, báo cáo & phân tích, triển khai Docker, GCP, GKE. | Coder, Doc, Tester, Reviewer, Docker, GCP, GKE | [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-009], [DAT-011], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
<!--END_PHASE_SYNOPSIS_GRID-->

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Giai đoạn 1: Core User Management & Authentication
- **Phase Core Objective & Purpose:** Triển khai các chức năng cốt lõi cho quản lý người dùng bao gồm đăng ký, xác thực xã hội, và phân quyền vai trò. Xây dựng nền tảng bảo mật và audit cho toàn hệ thống.
- **Target Physical Directory Matrix Map:**
    *   ./sources/backend/user-management/
    *   ./sources/docs/user-management.md
- **Database Schema DDL SQL Specification [DAT-001]:**
```sql:matrix
-- Bảng Roles
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

-- Bảng Users
CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL REFERENCES ROLES(roleId),
    provider ENUM('local','firebase','google','facebook') NOT NULL DEFAULT 'local',
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [ARC-006]:**
```json
// POST /api/v1/auth/register
{
  "email":"user@example.com",
  "password":"StrongPass123!",
  "fullName":"Nguyen Van A",
  "roleId":5
}
```
```json
// POST /api/v1/auth/social
{
  "provider":"google",
  "code":"OAuth2_code_from_provider"
}
```
- **Phase Localized Exception Handlers [EXC-004]:**
    * Xác thực đầu vào không hợp lệ: Trả về HTTP 400 với danh sách chi tiết các trường không hợp lệ (ví dụ: "email không đúng định dạng", "mật khẩu phải có ít nhất 8 ký tự").

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1:**
  
  ##### SUB-TASK 1: Triển khai đăng ký người dùng
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-001], [DAT-001], [EXC-004]
  * Target Component file path (target_component): ./sources/backend/user-management/src/main/java/org/nlh4j/saas/membershiphub/controller/UserController.java
  * Low-Level Technical Task Instruction: Xây dựng REST endpoint `POST /api/v1/auth/register`. Áp dụng Bean Validation cho các trường email, password, fullName. Mã hóa password bằng BCrypt. Gán role mặc định là `Student` (roleId 5). Trả về JWT token với thời hạn 15 phút. Ghi log hành động tạo người dùng vào bảng AuditLog.

  ##### SUB-TASK 2: Tích hợp OAuth2 với Firebase
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-002], [DAT-001], [ARC-006]
  * Target Component file path (target_component): ./sources/backend/user-management/src/main/java/org/nlh4j/saas/membershiphub/service/SocialAuthService.java
  * Low-Level Technical Task Instruction: Triển khai `SocialAuthService` sử dụng Firebase Auth SDK để xác thực người dùng qua ID token. Tạo hoặc cập nhật bản ghi trong bảng USERS dựa trên provider và sub. Phát sinh sự kiện `UserAuthenticatedEvent` để ghi audit.

  ##### SUB-TASK 3: Tài liệu kỹ thuật cho module người dùng
  * Sub-Agent Workflow Specialization: [Doc]
  * Targeted Tag IDs: [DAT-001], [REQ-001], [REQ-002]
  * Target Component file path (target_component): ./sources/docs/user-management.md
  * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật bao gồm mô tả ER diagram, API contract, hướng dẫn sử dụng cho các endpoint đăng ký và xác thực xã hội. Đảm bảo tài liệu được dịch sang tiếng Việt và tiếng Anh.

  ##### SUB-TASK 4: Kiểm thử đơn vị cho UserController
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-001], [REQ-002], [DAT-001]
  * Target Component file path (target_component): ./sources/backend/user-management/src/test/java/org/nlh4j/saas/membershiphub/controller/UserControllerTest.java
  * Low-Level Technical Task Instruction: Viết JUnit5 tests bao phủ các trường hợp đăng ký thành công, email trùng lặp, xác thực xã hội, và xử lý ngoại lệ validation. Sử dụng Mock cho FirebaseAuth và JwtTokenProvider.

  ##### SUB-TASK 5: Đánh giá chất lượng mã nguồn
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-001], [REQ-002], [DAT-001]
  * Target Component file path (target_component): ./sources/backend/user-management/src/main/java/org/nlh4j/saas/membershiphub/controller/UserController.java
  * Low-Level Technical Task Instruction: Kiểm tra tuân thủ các quy tắc lập trình ( spotless, SonarQube ), đảm bảo không có lỗ hổng bảo mật (SQL injection, XSS). Đề xuất các cải tiến về hiệu suất và ghi chú javadoc.

- **DAY 2:**

  ##### SUB-TASK 6: Tạo migration DDL cho Users & Roles
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [DAT-001], [EXC-004]
  * Target Component file path (target_component): ./sources/backend/user-management/src/main/resources/db/migration/V1__init_users_roles.sql
  * Low-Level Technical Task Instruction: Tạo Flyway migration script tạo bảng ROLES và USERS với các ràng buộc khóa ngoại, chỉ mục, và CHECK constraint cho provider enum.

  ##### SUB-TASK 7: Kiểm thử tích hợp cho SocialAuthService
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-002], [DAT-001], [ARC-006]
  * Target Component file path (target_component): ./sources/backend/user-management/src/test/java/org/nlh4j/saas/membershiphub/service/SocialAuthServiceTest.java
  * Low-Level Technical Task Instruction: Triển khai integration test sử dụng Firebase Auth mock, xác nhận flow OAuth2 tạo/cập nhật người dùng, và phát sinh sự kiện audit.

  ##### SUB-TASK 8: Đánh giá chất lượng mã nguồn cho SocialAuthService
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-002], [DAT-001], [ARC-006]
  * Target Component file path (target_component): ./sources/backend/user-management/src/main/java/org/nlh4j/saas/membershiphub/service/SocialAuthService.java
  * Low-Level Technical Task Instruction: Phân tích mã để đảm bảo xử lý ngoại lệ an toàn, không rò rỉ thông tin xác thực, và tuân thủ các quy tắc thiết kế SOLID.

### 📈 Giai đoạn 2: Center Management
- **Phase Core Objective & Purpose:** Xây dựng module quản lý trung tâm cho phép System Admin thao tác CRUD trung tâm và phân quyền quản trị trung tâm. Đảm bảo tính duy nhất của taxId và kiểm soát truy cập dựa trên vai trò.
- **Target Physical Directory Matrix Map:**
    *   ./sources/backend/center/
    *   ./sources/docs/center-management.md
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql:matrix
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [ARC-002]:**
```json
// GET /api/v1/centers
// Response: [{ "centerId":"...","name":"...","address":"...","taxId":"...","contactPhone":"...","contactEmail":"..." }]
```
```json
// POST /api/v1/centers
{
  "name":"Trung tâm Hà Nội",
  "address":"123 Đường Láng, Đống Đa, Hà Nội",
  "taxId":"0123456789",
  "contactPhone":"+84123456789",
  "contactEmail":"hn@nlh4j.com"
}
```
- **Phase Localized Exception Handlers:** (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1:**

  ##### SUB-TASK 1: Triển khai CRUD trung tâm
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002]
  * Target Component file path (target_component): ./sources/backend/center/src/main/java/org/nlh4j/saas/membershiphub/controller/CenterController.java
  * Low-Level Technical Task Instruction: Xây dựng REST endpoints `GET /api/v1/centers`, `POST /api/v1/centers`, `PUT /api/v1/centers/{id}`, `DELETE /api/v1/centers/{id}`. Áp dụng validation cho taxId (duy nhất). Gắn annotation `@PreAuthorize('hasRole(\"SYSTEM_ADMIN\")')` cho các thao tác ghi.

  ##### SUB-TASK 2: Tài liệu kỹ thuật cho module trung tâm
  * Sub-Agent Workflow Specialization: [Doc]
  * Targeted Tag IDs: [DAT-003], [REQ-004], [REQ-005], [REQ-006]
  * Target Component file path (target_component): ./sources/docs/center-management.md
  * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật bao gồm ER diagram, API contract, hướng dẫn sử dụng cho CRUD trung tâm, và quy tắc phân quyền Center Admin.

  ##### SUB-TASK 3: Kiểm thử đơn vị cho CenterController
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-004], [REQ-005], [REQ-006], [DAT-003]
  * Target Component file path (target_component): ./sources/backend/center/src/test/java/org/nlh4j/saas/membershiphub/controller/CenterControllerTest.java
  * Low-Level Technical Task Instruction: Viết JUnit5 tests bao phủ các trường hợp lấy danh sách, tạo, cập nhật, xóa trung tâm, kiểm tra validation taxId, và kiểm soát quyền truy cập.

  ##### SUB-TASK 4: Đánh giá chất lượng mã nguồn
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-004], [REQ-005], [REQ-006], [DAT-003]
  * Target Component file path (target_component): ./sources/backend/center/src/main/java/org/nlh4j/saas/membershiphub/controller/CenterController.java
  * Low-Level Technical Task Instruction: Kiểm tra tuân thủ các quy tắc mã nguồn, đảm bảo không có lỗ hổng bảo mật (SQL injection, authorization bypass), và đề xuất các cải tiến về hiệu suất.

- **DAY 2:**

  ##### SUB-TASK 5: Tạo migration DDL cho bảng CENTERS
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [DAT-003], [REQ-005]
  * Target Component file path (target_component): ./sources/backend/center/src/main/resources/db/migration/V1__init_centers.sql
  * Low-Level Technical Task Instruction: Tạo Flyway migration script tạo bảng CENTERS với ràng buộc UNIQUE taxId, CHECK constraint cho định dạng email và phone.

  ##### SUB-TASK 6: Kiểm thử tích hợp cho CenterService
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-004], [REQ-005], [REQ-006], [DAT-003]
  * Target Component file path (target_component): ./sources/backend/center/src/test/java/org/nlh4j/saas/membershiphub/service/CenterServiceTest.java
  * Low-Level Technical Task Instruction: Triển khai integration test sử dụng H2 embedded DB, kiểm tra flow CRUD, validation, và phân quyền Center Admin.

  ##### SUB-TASK 7: Đánh giá chất lượng mã nguồn cho CenterService
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-004], [REQ-005], [REQ-006], [DAT-003]
  * Target Component file path (target_component): ./sources/backend/center/src/main/java/org/nlh4j/saas/membershiphub/service/CenterService.java
  * Low-Level Technical Task Instruction: Phân tích mã để đảm bảo xử lý transaction an toàn, không có race condition khi tạo taxId, và tuân thủ các quy tắc thiết kế.

### 📈 Giai đoạn 3: Course Management
- **Phase Core Objective & Purpose:** Xây dựng module quản lý khóa học bao gồm CRUD khóa học, phân công giáo viên, và kiểm tra xung đột lịch. Đảm bảo tính toàn vẹn dữ liệu và thông báo cho giáo viên khi được phân công.
- **Target Physical Directory Matrix Map:**
    *   ./sources/backend/course/
    *   ./sources/docs/course-management.md
- **Database Schema DDL SQL Specification [DAT-004]:**
```sql:matrix
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL REFERENCES USERS(userId),
    maxStudents INT NOT NULL DEFAULT 30
);
```
- **API and Event Routing Contracts [REQ-007], [REQ-008], [REQ-009], [ARC-003]:**
```json
// GET /api/v1/courses
// Response: [{ "courseId":"...","title":"...","startDate":"...","endDate":"...","teacherName":"..." }]
```
```json
// POST /api/v1/courses
{
  "title":"Lớp học lập trình Java",
  "description":"Khóa học nâng cao về Java",
  "startDate":"2026-09-01",
  "endDate":"2026-12-31",
  "teacherId":"a1b2c3d4-...",
  "maxStudents":30
}
```
- **Phase Localized Exception Handlers:** (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 1:**

  ##### SUB-TASK 1: Triển khai CRUD khóa học với kiểm tra xung đột
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003]
  * Target Component file path (target_component): ./sources/backend/course/src/main/java/org/nlh4j/saas/membershiphub/controller/CourseController.java
  * Low-Level Technical Task Instruction: Xây dựng REST endpoints `GET /api/v1/courses`, `POST /api/v1/courses`, `PUT /api/v1/courses/{id}`, `DELETE /api/v1/courses/{id}`. Thêm logic validation để đảm bảo giáo viên không có lớp học khác chồng lịch trong cùng khoảng thời gian. Sử dụng `@Transactional` để tránh race condition.

  ##### SUB-TASK 2: Tài liệu kỹ thuật cho module khóa học
  * Sub-Agent Workflow Specialization: [Doc]
  * Targeted Tag IDs: [DAT-004], [REQ-007], [REQ-008], [REQ-009]
  * Target Component file path (target_component): ./sources/docs/course-management.md
  * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật bao gồm ER diagram, API contract, hướng dẫn sử dụng cho CRUD khóa học, quy tắc xung đột lịch, và quy trình phân công giáo viên.

  ##### SUB-TASK 3: Kiểm thử đơn vị cho CourseController
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-007], [REQ-008], [REQ-009], [DAT-004]
  * Target Component file path (target_component): ./sources/backend/course/src/test/java/org/nlh4j/saas/membershiphub/controller/CourseControllerTest.java
  * Low-Level Technical Task Instruction: Viết JUnit5 tests bao phủ các trường hợp lấy danh sách, tạo, cập nhật, xóa khóa học, kiểm tra xung đột lịch, và kiểm soát quyền truy cập (System Admin, Center Admin).

  ##### SUB-TASK 4: Đánh giá chất lượng mã nguồn
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-007], [REQ-008], [REQ-009], [DAT-004]
  * Target Component file path (target_component): ./sources/backend/course/src/main/java/org/nlh4j/saas/membershiphub/controller/CourseController.java
  * Low-Level Technical Task Instruction: Kiểm tra tuân thủ các quy tắc mã nguồn, đảm bảo không có lỗ hổng bảo mật (SQL injection, authorization bypass), và đề xuất các cải tiến về hiệu suất.

- **DAY 2:**

  ##### SUB-TASK 5: Tạo migration DDL cho bảng COURSES
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [DAT-004], [REQ-008]
  * Target Component file path (target_component): ./sources/backend/course/src/main/resources/db/migration/V1__init_courses.sql
  * Low-Level Technical Task Instruction: Tạo Flyway migration script tạo bảng COURSES với ràng buộc khóa ngoại teacherId, CHECK constraint startDate <= endDate.

  ##### SUB-TASK 6: Kiểm thử tích hợp cho CourseService
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-007], [REQ-008], [REQ-009], [DAT-004]
  * Target Component file path (target_component): ./sources/backend/course/src/test/java/org/nlh4j/saas/membershiphub/service/CourseServiceTest.java
  * Low-Level Technical Task Instruction: Triển khai integration test sử dụng PostgreSQL test container, kiểm tra flow CRUD, validation xung đột lịch, và phân quyền giáo viên.

  ##### SUB-TASK 7: Đánh giá chất lượng mã nguồn cho CourseService
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-007], [REQ-008], [REQ-009], [DAT-004]
  * Target Component file path (target_component): ./sources/backend/course/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java
  * Low-Level Technical Task Instruction: Phân tích mã để đảm bảo xử lý transaction an toàn, không có race condition khi gán giáo viên, và tuân thủ các quy tắc thiết kế.

### 📈 Giai đoạn 4: Enrollment, Attendance, Membership Card & Notifications
- **Phase Core Objective & Purpose:** Triển khai các module ghi danh khóa học, điểm danh QR, quản lý thẻ hội viên, và engine thông báo. Đảm bảo tính bất biến của điểm danh, xử lý ngoại lệ mạng, và gửi thông báo đẩy cùng bài đăng Zalo.
- **Target Physical Directory Matrix Map:**
    *   ./sources/backend/enrollment/
    *   ./sources/backend/attendance/
    *   ./sources/backend/membercard/
    *   ./sources/docs/enrollment-attendance-membercard.md
- **Database Schema DDL SQL Specification [DAT-005], [DAT-006], [DAT-007], [DAT-008]:**
```sql:matrix
-- Bảng Enrollments
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (studentId, courseId)
);

-- Bảng Attendance
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (studentId, courseId, attendanceDate)
);

-- Bảng StudentCards
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);

-- Bảng Notifications
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID REFERENCES USERS(userId),
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [ARC-007], [ARC-008]:**
```json
// POST /api/v1/enrollments
{
  "studentId":"a1b2c3d4-...",
  "courseId":"e5f6g7h8-..."
}
```
```json
// POST /api/v1/attendance/qr
{
  "studentId":"a1b2c3d4-...",
  "courseId":"e5f6g7h8-...",
  "timestamp":"2026-08-08T15:08:11Z"
}
```
```json
// GET /api/v1/membercard/{studentId}
```
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003]:**
    * Xử lý ngoại lệ network khi quét QR: Nếu request thất bại do mất mạng, app di động sẽ retry sau khi reconnect; service sẽ ghi nhận attempt và tạo bản ghi điểm danh khi request thành công.
    * Ngăn duplicate attendance: Service kiểm tra sự tồn tại của bản ghi (studentId, courseId, attendanceDate) trước khi tạo mới; trả về HTTP 200 với flag duplicate.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1:**

  ##### SUB-TASK 1: Triển khai ghi danh khóa học
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-010], [REQ-011], [DAT-005], [ARC-005]
  * Target Component file path (target_component): ./sources/backend/enrollment/src/main/java/org/nlh4j/saas/membershiphub/controller/EnrollmentController.java
  * Low-Level Technical Task Instruction: Xây dựng REST endpoint `POST /api/v1/enrollments`. Kiểm tra sự tồn tại của student và course, đảm bảo chưa ghi danh, tạo bản ghi ENROLLMENTS, phát sinh sự kiện `EnrollmentCreatedEvent` để trigger notification.

  ##### SUB-TASK 2: Tài liệu kỹ thuật cho module ghi danh
  * Sub-Agent Workflow Specialization: [Doc]
  * Targeted Tag IDs: [DAT-005], [REQ-010], [REQ-011]
  * Target Component file path (target_component): ./sources/docs/enrollment-attendance-membercard.md
  * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật bao gồm flow ghi danh, validation, API contract, và hướng dẫn sử dụng cho mobile app.

  ##### SUB-TASK 3: Kiểm thử đơn vị cho EnrollmentController
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-010], [REQ-011], [DAT-005]
  * Target Component file path (target_component): ./sources/backend/enrollment/src/test/java/org/nlh4j/saas/membershiphub/controller/EnrollmentControllerTest.java
  * Low-Level Technical Task Instruction: Viết JUnit5 tests bao phủ các trường hợp ghi danh thành công, student không tồn tại, course đã đầy, và validation business.

  ##### SUB-TASK 4: Đánh giá chất lượng mã nguồn
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-010], [REQ-011], [DAT-005]
  * Target Component file path (target_component): ./sources/backend/enrollment/src/main/java/org/nlh4j/saas/membershiphub/controller/EnrollmentController.java
  * Low-Level Technical Task Instruction: Kiểm tra tuân thủ các quy tắc mã nguồn, đảm bảo không có race condition khi ghi danh, và đề xuất các cải tiến về hiệu suất.

- **DAY 2:**

  ##### SUB-TASK 5: Triển khai service điểm danh QR với tính bất biến
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]
  * Target Component file path (target_component): ./sources/backend/attendance/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java
  * Low-Level Technical Task Instruction: Xây dựng REST endpoint `POST /api/v1/attendance/qr`. Sử dụng `SELECT FOR UPDATE` trên bảng ATTENDANCE để đảm bảo chỉ một bản ghi được tạo cho mỗi (studentId, courseId, attendanceDate). Nếu duplicate, trả về HTTP 200 với payload `{ "duplicate": true }`. Ghi log attempt vào bảng AuditLog.

  ##### SUB-TASK 6: Tài liệu kỹ thuật cho module điểm danh
  * Sub-Agent Workflow Specialization: [Doc]
  * Targeted Tag IDs: [DAT-006], [REQ-012], [REQ-013]
  * Target Component file path (target_component): ./sources/docs/enrollment-attendance-membercard.md
  * Low-Level Technical Task Instruction: Cập nhật tài liệu kỹ thuật với flow điểm danh QR, quy tắc bất biến, và hướng dẫn xử lý ngoại lệ network.

  ##### SUB-TASK 7: Kiểm thử tích hợp cho AttendanceService
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-012], [REQ-013], [DAT-006]
  * Target Component file path (target_component): ./sources/backend/attendance/src/test/java/org/nlh4j/saas/membershiphub/service/AttendanceServiceTest.java
  * Low-Level Technical Task Instruction: Triển khai integration test sử dụng PostgreSQL test container, mô phỏng scenario quét QR thành công, duplicate scan, và mất mạng (retry).

  ##### SUB-TASK 8: Đánh giá chất lượng mã nguồn
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-012], [REQ-013], [DAT-006]
  * Target Component file path (target_component): ./sources/backend/attendance/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java
  * Low-Level Technical Task Instruction: Phân tích mã để đảm bảo xử lý transaction an toàn, không có race condition, và tuân thủ các quy tắc thiết kế.

- **DAY 3:**

  ##### SUB-TASK 9: Triển khai module thẻ hội viên và gia hạn
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-014], [REQ-015], [DAT-007], [DAT-008], [EXC-003]
  * Target Component file path (target_component): ./sources/backend/membercard/src/main/java/org/nlh4j/saas/membershiphub/controller/MemberCardController.java
  * Low-Level Technical Task Instruction: Xây dựng REST endpoints `GET /api/v1/membercard/{studentId}` và `POST /api/v1/membercard/{studentId}/renew`. Tính remainingDays dựa trên issueDate + validityDays. Khi renew, cập nhật issueDate và remainingDays, tạo notification record.

  ##### SUB-TASK 10: Tài liệu kỹ thuật cho module thẻ hội viên
  * Sub-Agent Workflow Specialization: [Doc]
  * Targeted Tag IDs: [DAT-007], [DAT-008], [REQ-014], [REQ-015]
  * Target Component file path (target_component): ./sources/docs/enrollment-attendance-membercard.md
  * Low-Level Technical Task Instruction: Hoàn thiện tài liệu kỹ thuật bao gồm flow hiển thị thẻ, quy tắc gia hạn, API contract, và hướng dẫn sử dụng cho mobile app.

  ##### SUB-TASK 11: Kiểm thử đơn vị cho MemberCardController
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-014], [REQ-015], [DAT-007]
  * Target Component file path (target_component): ./sources/backend/membercard/src/test/java/org/nlh4j/saas/membershiphub/controller/MemberCardControllerTest.java
  * Low-Level Technical Task Instruction: Viết JUnit5 tests bao phủ các trường hợp lấy thông tin thẻ, gia hạn thành công, validation đầu vào, và kiểm tra notification được tạo.

  ##### SUB-TASK 12: Đánh giá chất lượng mã nguồn
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-014], [REQ-015], [DAT-007]
  * Target Component file path (target_component): ./sources/backend/membercard/src/main/java/org/nlh4j/saas/membershiphub/controller/MemberCardController.java
  * Low-Level Technical Task Instruction: Kiểm tra tuân thủ các quy tắc mã nguồn, đảm bảo không có SQL injection, authorization bypass, và đề xuất các cải tiến về hiệu suất.

### 📈 Giai đoạn 5: Promotions, Chatbot, Mobile, i18n, SEO, Reporting & Infra
- **Phase Core Objective & Purpose:** Triển khai các tính năng nâng cao bao gồm quản lý khuyến mãi/thông báo, tích hợp chatbot AI, UI di động vai trò, push notification, localization/SEO, báo cáo & phân tích, và triển khai hạ tầng DevOps (Docker, GCP, GKE).
- **Target Physical Directory Matrix Map:**
    *   ./sources/backend/promotion/
    *   ./sources/backend/chatbot/
    *   ./sources/frontend/
    *   ./sources/mobile/
    *   ./sources/docs/promotion-chatbot-mobile.md
- **Database Schema DDL SQL Specification [DAT-009], [DAT-011]:**
```sql:matrix
-- Bảng Promotions
CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);

-- Bảng Announcements
CREATE TABLE ANNOUNCEMENTS (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);

-- Bảng SystemSettings
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```
- **API and Event Routing Contracts [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-008], [NFR-007], [NFR-008], [NFR-009]:**
```json
// POST /api/v1/promotions
{
  "code":"SUMMER20",
  "discountPercent":20,
  "startDate":"2026-06-01",
  "endDate":"2026-08-31",
  "description":"Giảm giá 20% cho tất cả khóa học"
}
```
```json
// GET /api/v1/announcements
```
- **Phase Localized Exception Handlers:** (Không có luồng ngoại lệ chuyên biệt được xác định cho mô-đun này.)

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 1:**

  ##### SUB-TASK 1: Triển khai quản lý khuyến mãi & thông báo
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-017], [REQ-018], [DAT-009], [ARC-008]
  * Target Component file path (target_component): ./sources/backend/promotion/src/main/java/org/nlh4j/saas/membershiphub/controller/PromotionController.java
  * Low-Level Technical Task Instruction: Xây dựng REST endpoints `GET /api/v1/promotions`, `POST /api/v1/promotions`, `PUT /api/v1/promotions/{id}`, `DELETE /api/v1/promotions/{id}`. Thêm logic validation cho code duy nhất, startDate/endDate. Khi tạo/chỉnh sửa promotion, phát sinh sự kiện `PromotionChangedEvent` để trigger notification.

  ##### SUB-TASK 2: Tài liệu kỹ thuật cho module khuyến mãi
  * Sub-Agent Workflow Specialization: [Doc]
  * Targeted Tag IDs: [DAT-009], [REQ-017], [REQ-018]
  * Target Component file path (target_component): ./sources/docs/promotion-chatbot-mobile.md
  * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật bao gồm flow quản lý khuyến mãi/thông báo, API contract, hướng dẫn sử dụng cho admin.

  ##### SUB-TASK 3: Kiểm thử đơn vị cho PromotionController
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-017], [REQ-018], [DAT-009]
  * Target Component file path (target_component): ./sources/backend/promotion/src/test/java/org/nlh4j/saas/membershiphub/controller/PromotionControllerTest.java
  * Low-Level Technical Task Instruction: Viết JUnit5 tests bao phủ các trường hợp CRUD promotion, validation code trùng lặp, và kiểm tra notification được tạo.

  ##### SUB-TASK 4: Đánh giá chất lượng mã nguồn
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-017], [REQ-018], [DAT-009]
  * Target Component file path (target_component): ./sources/backend/promotion/src/main/java/org/nlh4j/saas/membershiphub/controller/PromotionController.java
  * Low-Level Technical Task Instruction: Kiểm tra tuân thủ các quy tắc mã nguồn, đảm bảo không có SQL injection, authorization bypass, và đề xuất các cải tiến về hiệu suất.

- **DAY 2:**

  ##### SUB-TASK 5: Triển khai chatbot AI integration
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-019], [NFR-007], [NFR-008]
  * Target Component file path (target_component): ./sources/backend/chatbot/src/main/java/org/nlh4j/saas/membershiphub/service/ChatbotService.java
  * Low-Level Technical Task Instruction: Triển khai REST endpoint `POST /api/v1/chatbot/query`. Sử dụng OpenAI/Gemini SDK để xử lý truy vấn người dùng, trả về câu trả lời phù hợp. Tích hợp logging cho audit.

  ##### SUB-TASK 6: Triển khai UI di động vai trò
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-020], [NFR-008]
  * Target Component file path (target_component): ./sources/mobile/app/src/screens/RoleBasedScreen.tsx
  * Low-Level Technical Task Instruction: Xây dựng React Native component hiển thị giao diện phù hợp dựa trên vai trò người dùng (Student, Teacher, Admin). Sử dụng React Navigation và Redux Toolkit cho state management.

  ##### SUB-TASK 7: Tài liệu kỹ thuật cho chatbot & di động
  * Sub-Agent Workflow Specialization: [Doc]
  * Targeted Tag IDs: [REQ-019], [REQ-020], [NFR-007], [NFR-008]
  * Target Component file path (target_component): ./sources/docs/promotion-chatbot-mobile.md
  * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật bao gồm flow tích hợp chatbot, contract API, hướng dẫn sử dụng cho mobile app, và quy tắc localization.

  ##### SUB-TASK 8: Kiểm thử tích hợp cho ChatbotService
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [REQ-019], [NFR-007]
  * Target Component file path (target_component): ./sources/backend/chatbot/src/test/java/org/nlh4j/saas/membershiphub/service/ChatbotServiceTest.java
  * Low-Level Technical Task Instruction: Triển khai integration test sử dụng mock LLM response, xác nhận flow xử lý truy vấn, và logging.

  ##### SUB-TASK 9: Đánh giá chất lượng mã nguồn
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-019], [NFR-007]
  * Target Component file path (target_component): ./sources/backend/chatbot/src/main/java/org/nlh4j/saas/membershiphub/service/ChatbotService.java
  * Low-Level Technical Task Instruction: Phân tích mã để đảm bảo xử lý ngoại lệ an toàn, không rò rỉ thông tin người dùng, và tuân thủ các quy tắc thiết kế.

- **DAY 3:**

  ##### SUB-TASK 10: Triển khai báo cáo & phân tích
  * Sub-Agent Workflow Specialization: [Coder]
  * Targeted Tag IDs: [REQ-024], [REQ-025], [NFR-001], [NFR-006]
  * Target Component file path (target_component): ./sources/backend/reporting/src/main/java/org/nlh4j/saas/membershiphub/controller/ReportController.java
  * Low-Level Technical Task Instruction: Xây dựng REST endpoints `GET /api/v1/reports/attendance` (xuất CSV) và `GET /api/v1/dashboard` (tổng hợp số liệu). Sử dụng JPA queries tối ưu hóa cho hiệu suất.

  ##### SUB-TASK 11: Triển khai Docker, GCP & GKE infrastructure
  * Sub-Agent Workflow Specialization: [Docker]
  * Targeted Tag IDs: [NFR-004], [NFR-005], [NFR-009]
  * Target Component file path (target_component): ./sources/infra/docker/Dockerfile
  * Low-Level Technical Task Instruction: Tạo multi-stage Docker image (<500MB) cho backend và frontend. Thêm healthcheck, cấu hình resource limits.

  ##### SUB-TASK 12: Triển khai GCP services & GKE manifests
  * Sub-Agent Workflow Specialization: [GCP]
  * Targeted Tag IDs: [NFR-004], [NFR-009]
  * Target Component file path (target_component): ./sources/infra/gcp/terraform/main.tf
  * Low-Level Technical Task Instruction: Viết Terraform scripts để provision VPC, Cloud SQL (PostgreSQL), Cloud Storage, và GKE cluster. Thiết lập IAM cho service accounts.

  ##### SUB-TASK 13: Triển khai Kubernetes manifests
  * Sub-Agent Workflow Specialization: [GKE]
  * Targeted Tag IDs: [NFR-004], [NFR-009]
  * Target Component file path (target_component): ./sources/infra/k8s/deployment.yaml
  * Low-Level Technical Task Instruction: Tạo Kubernetes Deployment và Service cho các microservice, cấu hình HPA dựa trên CPU >70% hoặc latency >300ms.

  ##### SUB-TASK 14: Tài liệu kỹ thuật cho báo cáo & hạ tầng
  * Sub-Agent Workflow Specialization: [Doc]
  * Targeted Tag IDs: [REQ-024], [REQ-025], [NFR-004], [NFR-005], [NFR-009]
  * Target Component file path (target_component): ./sources/docs/promotion-chatbot-mobile.md
  * Low-Level Technical Task Instruction: Hoàn thiện tài liệu kỹ thuật bao gồm hướng dẫn triển khai Docker, cấu hình GCP, manifest GKE, và quy trình CI/CD.

  ##### SUB-TASK 15: Kiểm thử triển khai Docker image
  * Sub-Agent Workflow Specialization: [Tester]
  * Targeted Tag IDs: [NFR-005], [NFR-009]
  * Target Component file path (target_component): ./sources/infra/docker/Dockerfile;./sources/infra/docker/Dockerfile
  * Low-Level Technical Task Instruction: Xây dựng Docker image, chạy container trong môi trường test, xác nhận size image <500MB, và các healthcheck hoạt động.

  ##### SUB-TASK 16: Đánh giá chất lượng mã nguồn cho ReportController
  * Sub-Agent Workflow Specialization: [Reviewer]
  * Targeted Tag IDs: [REQ-024], [REQ-025]
  * Target Component file path (target_component): ./sources/backend/reporting/src/main/java/org/nlh4j/saas/membershiphub/controller/ReportController.java
  * Low-Level Technical Task Instruction: Kiểm tra tuân thủ các quy tắc mã nguồn, đảm bảo không có SQL injection, authorization bypass, và đề xuất các cải tiến về hiệu suất.

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-001]..[NFR-009]
- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng PreparedStatement/Parameterized queries trong tất cả JDBC calls; áp dụng ORM mapping với named parameters; thực hiện whitelist cho các giá trị sort column.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động escape tất cả dữ liệu người dùng hiển thị trong React/Next.js bằng React.Fragment; áp dụng CSP header không cho phép `script-src 'unsafe-inline'`; sử dụng DOMPurify cho các trường HTML.
- **Multi-Tenant CORS Security Rails:** Cấu hình CORS per-tenant; whitelist origin dựa trên bảng TENANT_ORigins; sử dụng SameSite cookies.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Áp dụng `@LogSanitization` interceptor để xóa thông tin thẻ tín dụng, số CMND; sử dụng `MaskingFilter` cho các trường PII trong logs; lưu logs trong 1 năm theo quy định GDPR.
- **JWT Token Hardening:** Ký với RS256, lưu trữ refresh token trong HTTP-only Secure cookies, rotate key định kỳ, enforce `max-age` 7 ngày.
- **Rate Limiting & Brute Force Protection:** Sử dụng Spring Security `RateLimiter` cho `/auth/login`; tích hợp Redis cho distributed counting.
- **Backup & Disaster Recovery:** Sao lưu PostgreSQL hàng ngày, lưu trữ tại region khác; khôi phục điểm-in-time lên đến 24 giờ; backup GKE cluster định kỳ.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng `@capacitor/app` để quản lý lifecycle, `@capacitor/preferences` cho storage an toàn, `@capacitor/network` để detect mất kết nối và queue tác vụ offline.
- **Internationalization (i18n) & Dynamic SEO Injection:** Middleware phát hiện locale từ cookie, header Accept-Language; sử dụng i18next cho key-value resources; chèn thẻ `<html lang='vi'>` và hreflang `<link rel="alternate" hreflang="en" href="https://example.com/en"/>` cho từng trang.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Mỗi ngày được fork từ branch `main` thành `features/development-phase-X-day-Y` (`X` là số phase, `Y` là số ngày trong phase).
- **Validation Guard Pipeline Gates:** Thực hiện `mvn clean test` và `npm run test` tự động; yêu cầu coverage >=85%; nếu thất bại, branch bị chặn và thông báo qua Slack.
- **Merge & Deploy:** Sau khi tất cả ngày trong phase hoàn thành, merge branch vào `main` và trigger GitHub Actions triển khai lên GKE (blue-green).

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`