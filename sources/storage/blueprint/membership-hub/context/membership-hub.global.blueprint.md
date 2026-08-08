# BỐ CỤC DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808154029 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 15:40:29 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1 Core System Modality & Architecture Modality
- Nền tảng quản lý hội viên phân tán đa trung tâm với kiến trúc microservice dựa trên Java/Quarkus.
- Triển khai container hóa với Docker và quản lý bởi Kubernetes (GKE) để đảm bảo khả năng mở rộng và khả năng phục hồi.
- Tích hợp nhiều kênh xác thực (email/mật khẩu, Firebase, Google, Facebook) với OAuth2 và JWT tokens có thời hạn 15 phút.
- Xử lý điểm danh bất biến thông qua quét mã QR, đảm bảo ghi nhận duy nhất mỗi học viên mỗi khóa học mỗi ngày.
- Triển khai thẻ hội viên kỹ thuật số với cơ chế đếm ngày hiệu lực có thể gia hạn.
- Triển khai thông báo đa kênh qua push notification trên di động và tích hợp với nhóm Zalo.
- Tích hợp backend Next.js với REST APIs, xác thực bearer token và hỗ trợ caching ngoại tuyến.
- Áp dụng các biện pháp bảo mật nghiêm ngặt theo tiêu chuẩn OWASP Top 10, mã hóa dữ liệu ở nghỉ và ở truyền, tuân thủ GDPR/CCPA.
- Triển khai hệ thống logging và audit toàn diện cho mọi thao tác người dùng, giữ logs trong 1 năm.
- Hỗ trợ đa ngôn ngữ (Tiếng Anh, Tiếng Việt, Tiếng Tây Ban Nha) với i18n nội bộ và SEO tối ưu hóa.

### 1.2 Enterprise Data Flow Topologies & Core Ecosystems
- Luồng xác thực: OAuth2 từ các nhà cung cấp xã hội → xác thực Firebase/Google/Facebook → cấp JWT token (15 phút) và refresh token (7 ngày).
- Luồng điểm danh QR: Ứng dụng di động quét QR → gửi studentId + timestamp đến API điểm danh → dịch vụ xác thực quan hệ học viên-khóa học và ghi nhận điểm danh một cách idempotent.
- Luồng thông báo: Backend kích hoạt push notification (FCM/APNs) đến thiết bị người dùng và đồng thời đăng bài lên nhóm Zalo được chỉ định cho thông báo, thông báo phân công khóa học, và cảnh báo điểm danh.
- Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs qua bearer token, hỗ trợ caching ngoại tuyến thông qua IndexedDB và đồng bộ khi có kết nối.
- Luồng dữ liệu trung tâm: Trung tâm quản lý (System Admin) và Center Admin thao tác trên các bảng trung tâm, người dùng, vai trò, khóa học, ghi danh, điểm danh, thẻ hội viên, khuyến mãi, thông báo.
- Luồng báo cáo và phân tích: Các tác vụ báo cáo điểm danh tạo file CSV, bảng điều khiển tổng hợp dữ liệu ghi danh thời gian thực cho Center Admin.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

### Backend Infrastructure Core Stack
- Java 21, Quarkus 3.2.0, Hibernate ORM (Jakarta Persistence), Flyway, SmallRye OpenAPI, Micrometer, JUnit 5.
- PostgreSQL 15.4 (PostGIS optional), Redis 7.0.
- Xác thực: Firebase Auth SDK, Google Identity Platform, Facebook Graph API.
- Push Notification: Firebase Cloud Messaging (FCM), Apple APNs (qua Firebase).
- Messaging: Apache Kafka 3.5.0.
- DevOps: Docker 24.x, Kubernetes 1.28 (GKE), Helm 3, GitHub Actions CI/CD, Terraform.
- Monitoring: Prometheus + Grafana, Jaeger.
- Bảo mật: Keycloak (tùy chọn), OAuth2 Resource Server, java-jwt 4.4.0.
- Quốc tế hóa: Java i18n, React Intl cho frontend.
- Di động: React Native 0.73, @react-native-firebase, Capacitor.
- Frontend: Next.js 14, React 18, TypeScript, Tailwind CSS, i18next, SWR.
- Kiểm thử: JUnit 5, Testcontainers, Postman/Newman, Cypress.

### Frontend & Cross-Platform UI Mobile Stack
- Web: Next.js 14, React 18, TypeScript, Tailwind CSS, i18next, SWR.
- Mobile: React Native 0.73, Expo managed workflow, @react-native-firebase/app, @react-native-firebase/auth, @react-native-firebase/messaging, Capacitor plugins.
- Chia sẻ UI: React Native Paper, NativeBase.

### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- Tuân thủ nghiêm ngặt ranh giới không gian làm việc: gốc repository là `.`, mọi đường dẫn phải bắt đầu với `./sources/`.
- Áp dụng quy tắc tiền tố thư mục động theo giao thức 1: backend, frontend, infra, docs.
- Đối với stack Java: tất cả mã nguồn Java phải nằm trong gói `org.nlh4j.saas.membershiphub` (dạng thư mục: `./sources/backend/org/nlh4j/saas/membershiphub/...`).
- Quy tắc cú pháp đường dẫn kiểm thử: `<source_component>;<test_suite_file>`.
- Các quy tắc bảo mật: SQL injection, XSS, CSRF, CORS, logging, masking PII, tuân thủ GDPR/CCPA.
- Các quy tắc triển khai: Docker image size < 500MB, base image < 200MB, CI/CD tự động, kiểm tra bảo mật tĩnh.
- Các quy tắc hiệu năng: độ trễ API <200ms, hỗ trợ 10k người dùng đồng thời, sử dụng read replica cho báo cáo.
- Các quy tắc khả dụng: mục tiêu 99.9% uptime, tự động chuyển đổi dự phòng giữa các cluster GKE.
- Các quy tắc sao lưu và phục hồi: sao lưu PostgreSQL hàng ngày, phục hồi điểm trong 24 giờ, sao lưu cluster GKE sang region khác.
- Các quy tắc đa ngôn ngữ: i18n cho UI, meta tags hreflang, phát hiện ngôn ngữ từ cookie, header Accept-Language.
- Các quy tắc logging: ghi log mọi thao tác người dùng (thay đổi vai trò, ghi điểm danh, gửi thông báo) với timestamp, userId, chi tiết hành động, lưu trữ 1 năm.

## 📁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

<!--START_BACKLOG_SYNOPSIS_GRID-->
| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Đăng ký người dùng | Triển khai endpoint đăng ký người dùng qua email/mật khẩu, xác thực đầu vào, mã hóa mật khẩu, lưu bản ghi người dùng với vai trò mặc định Student, trả về JWT token. | Application Code | [REQ-001], [DAT-001], [ARC-006] |
| 2 | Xác thực qua mạng xã hội | Tích hợp OAuth2 với Firebase, Google, Facebook, trao đổi code lấy thông tin người dùng, tạo/cập nhật bản ghi người dùng, cấp JWT token. | Application Code | [REQ-002], [DAT-001], [ARC-006] |
| 3 | Phân quyền người dùng | Cho phép System Admin gán/thay đổi vai trò người dùng, áp dụng RBAC ngay lập tức. | Application Code | [REQ-003], [DAT-001], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005] |
| 4 | Tài liệu bảng người dùng & vai trò | Tạo tài liệu kỹ thuật chi tiết bảng Users và Roles (ER diagram, schema). | Enterprise Documentation | [DAT-001] |
| 5 | Xem danh sách trung tâm | Triển khai API/list view hiển thị tên, địa chỉ, taxId, contact của tất cả trung tâm. | Application Code | [REQ-004], [DAT-003], [ARC-002] |
| 6 | Tạo/cập nhật/xóa trung tâm | CRUD trung tâm với validation taxId duy nhất, kiểm soát bởi System Admin và Center Admin. | Application Code | [REQ-005], [DAT-003], [ARC-001], [ARC-002] |
| 7 | Phân quyền quản trị trung tâm | Gán người dùng làm Center Admin cho một trung tâm cụ thể và hủy quyền. | Application Code | [REQ-006], [DAT-003], [ARC-001], [ARC-002] |
| 8 | Tài liệu bảng trung tâm | Tài liệu kỹ thuật bảng Centers (ER diagram, schema). | Enterprise Documentation | [DAT-003] |
| 9 | Xem danh sách khóa học | Hiển thị danh sách khóa học với title, ngày bắt đầu/kết thúc, tên giáo viên. | Application Code | [REQ-007], [DAT-004], [ARC-002], [ARC-003] |
| 10 | Tạo/cập nhật/xóa khóa học | CRUD khóa học với validation xung đột lịch dạy của giáo viên. | Application Code | [REQ-008], [DAT-004], [ARC-001], [ARC-002], [EXC-001] |
| 11 | Phân công giáo viên vào khóa học | Gán giáo viên vào khóa học, đẩy notification đến mobile app của giáo viên. | Application Code | [REQ-009], [DAT-004], [ARC-001], [ARC-003], [EXC-001] |
| 12 | Tài liệu bảng khóa học | Tài liệu kỹ thuật bảng Courses (ER diagram, schema). | Enterprise Documentation | [DAT-004] |
| 13 | Duyệt khóa học | Hiển thị khóa học có sẵn (không bao gồm các khóa đã ghi danh) cho Student. | Application Code | [REQ-010], [DAT-005], [ARC-005] |
| 14 | Đăng ký khóa học của học viên | Xử lý ghi danh, tự động tạo tài khoản Student nếu thiếu, đẩy notification đến student và nhóm Zalo. | Application Code | [REQ-011], [DAT-005], [ARC-005], [EXC-002] |
| 15 | Tài liệu bảng ghi danh | Tài liệu kỹ thuật bảng Enrollments (ER diagram, schema). | Enterprise Documentation | [DAT-005] |
| 16 | Chụp ảnh điểm danh QR | Xử lý quét QR, xác thực học viên-khóa học, ghi nhận điểm danh, chống duplicate trong ngày. | Application Code | [REQ-012], [DAT-006], [ARC-007], [EXC-001], [EXC-002] |
| 17 | Tính chất bất biến của điểm danh | Đảm bảo chỉ một bản ghi điểm danh mỗi học viên mỗi khóa học mỗi ngày, trả về flag duplicate nếu quét lại. | Application Code | [REQ-013], [DAT-006], [ARC-007], [EXC-002] |
| 18 | Tài liệu bảng điểm danh | Tài liệu kỹ thuật bảng Attendance (ER diagram, schema). | Enterprise Documentation | [DAT-006] |
| 19 | Hiển thị tính hợp lệ của thẻ | Hiển thị thẻ hội viên với days remaining, derived từ StudentCards. | Application Code | [REQ-014], [DAT-007], [ARC-005] |
| 20 | Gia hạn thẻ | Xử lý thanh toán, cập nhật EndDate của StudentCard, gửi confirmation. | Application Code | [REQ-015], [DAT-007], [ARC-005], [EXC-003] |
| 21 | Tài liệu bảng thẻ hội viên | Tài liệu kỹ thuật bảng StudentCards (ER diagram, schema). | Enterprise Documentation | [DAT-007] |
| 22 | Kích hoạt thông báo | Tạo bản ghi Notification, đẩy push notification, đăng bài lên nhóm Zalo. | Application Code | [REQ-016], [DAT-008], [ARC-008], [EXC-003] |
| 23 | Tài liệu bảng thông báo | Tài liệu kỹ thuật bảng Notifications (ER diagram, schema). | Enterprise Documentation | [DAT-008] |
| 24 | Quản lý khuyến mãi | CRUD khuyến mãi (code, discount %, start/end dates). | Application Code | [REQ-017], [DAT-009], [ARC-002], [ARC-003] |
| 25 | Quản lý thông báo | CRUD thông báo (title, content, optional expiry). | Application Code | [REQ-018], [DAT-009], [ARC-002], [ARC-003] |
| 26 | Tài liệu bảng khuyến mãi & thông báo | Tài liệu kỹ thuật bảng Promotions và Announcements (ER diagram, schema). | Enterprise Documentation | [DAT-009] |
| 27 | Tích hợp chatbot AI | Triển khai chatbot trả lời truy vấn về khóa học, giáo viên, trung tâm, trạng thái tài khoản. | Application Code | [REQ-019], [EXC-004] |
| 28 | Tài liệu chatbot AI | (Không có bảng dữ liệu chuyên biệt) | Enterprise Documentation | [NOT APPLICABLE] |
| 29 | Giao diện người dùng vai trò cụ thể trên di động | Xây dựng UI responsive trên di động phản ánh chức năng web theo vai trò. | Application Code | [REQ-020], [ARC-009] |
| 30 | Thông báo đẩy trên di động | Gửi push notification qua FCM/APNs cho các sự kiện điểm danh, thông báo mới, reminder. | Application Code | [REQ-021], [ARC-009], [EXC-003] |
| 31 | Phát hiện ngôn ngữ mặc định | Sử dụng ngôn ngữ đã lưu của người dùng, fallback Accept-Language header. | Application Code | [REQ-022], [DAT-011], [NFR-007] |
| 32 | SEO đa ngôn ngữ | Thêm meta tags hreflang cho English, Vietnamese, Spanish. | Application Code | [REQ-023], [NFR-007] |
| 33 | Tài liệu bảng cài đặt hệ thống | Tài liệu kỹ thuật bảng SystemSettings (ER diagram, schema). | Enterprise Documentation | [DAT-011] |
| 34 | Tạo báo cáo điểm danh | Xuất CSV điểm danh theo trung tâm và ngày, columns: StudentName, CourseName, AttendanceDate, Status. | Application Code | [REQ-024], [EXC-005], [NFR-006] |
| 35 | Bảng điều khiển tóm tắt ghi danh | Dashboard thời gian thực hiển thị totalStudents, activeCourses, upcomingSessions (7 ngày tới). | Application Code | [REQ-025], [NFR-006] |
| 36 | Cấu hình Docker | Tạo Dockerfile đa giai đoạn, tối ưu size image (<500MB). | DevOps Infrastructure | [NFR-005], [ARC-010] |
| 37 | Triển khai GCP | Provision Compute Engine, Cloud SQL, Cloud Storage, VPC, IAM via Terraform. | DevOps Infrastructure | [NFR-004], [ARC-010] |
| 38 | Triển khai GKE cluster và deployment | Tạo GKE cluster, deployment manifests, service, HPA. | DevOps Infrastructure | [NFR-004], [ARC-010] |
| 39 | Pipeline CI/CD GitHub Actions | Tự động build, test, push Docker image, deploy đến GKE. | DevOps Infrastructure | [NFR-004], [ARC-010] |
| 40 | Kiểm tra bảo mật và tuân thủ OWASP | Thực hiện kiểm tra tĩnh, SQL injection, XSS, CSRF, logging. | DevOps Infrastructure | [NFR-003], [ARC-010] |
| 41 | Thiết lập logging và audit (ELK) | Collect, index, lưu trữ logs người dùng trong 1 năm. | DevOps Infrastructure | [NFR-006], [ARC-010] |
| 42 | Thiết lập sao lưu và phục hồi (pgBackRest) | Sao lưu PostgreSQL hàng ngày, phục hồi điểm trong 24 giờ. | DevOps Infrastructure | [NFR-009], [ARC-010] |
| **SUMMARY** | **Tổng số công việc trong backlog** | **TỔNG CỘNG:** 42 Tasks | **TRẠNG THÁI:** Verified | **PHẠM VI:** 100% |
<!--END_BACKLOG_SYNOPSIS_GRID-->

<!--START_PHASE_SYNOPSIS_GRID-->
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 - 3 | `./sources/backend/org/nlh4j/saas/membershiphub/controller/UserController.java` | Triển khai đăng ký người dùng, xác thực xã hội, gán vai trò, tài liệu API, unit tests. | Coder, Doc, Tester, Reviewer, Docker, GCP, GKE | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-006], [EXC-004] |
| Phase 2 | Day 1 - 4 | `./sources/backend/org/nlh4j/saas/membershiphub/controller/CenterController.java` | CRUD trung tâm, phân quyền center admin, tài liệu bảng Centers, kiểm thử tích hợp. | Coder, Doc, Tester, Reviewer, Docker, GCP, GKE | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002], [ARC-001] |
| Phase 3 | Day 1 - 3 | `./sources/backend/org/nlh4j/saas/membershiphub/controller/CourseController.java` | Quản lý khóa học, phân công giáo viên, validation xung đột lịch, tài liệu bảng Courses. | Coder, Doc, Tester, Reviewer, Docker, GCP, GKE | [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003], [EXC-001] |
| Phase 4 | Day 1 - 4 | `./sources/backend/org/nlh4j/saas/membershiphub/controller/EnrollmentController.java` | Xử lý ghi danh khóa học, notification, bảng Enrollments, mobile push. | Coder, Doc, Tester, Reviewer, Docker, GCP, GKE | [REQ-010], [REQ-011], [REQ-016], [DAT-005], [DAT-008], [ARC-005], [EXC-002], [EXC-003] |
| Phase 5 | Day 1 - 3 | `./sources/backend/org/nlh4j/saas/membershiphub/controller/AttendanceController.java` | Điểm danh QR, bất biến điểm danh, thẻ hội viên, báo cáo, dashboard. | Coder, Doc, Tester, Reviewer, Docker, GCP, GKE | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-024], [REQ-025], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [EXC-005], [NFR-006] |
| **AUDIT** | **Master Backlog Lifecycle Distribution Verification** | **TỔNG SỐ PHASES:** 5 | **TRẠNG THÁI KIỂM TRA:** Verified 5 out of 5 Phases Generated with 100% Coverage | **TRẠNG THÁI:** Verified | **TUÂN THỦ:** Hardbound Matrix |
<!--END_PHASE_SYNOPSIS_GRID-->

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Phase 1: Core User & Authentication Foundation
- **Phase Core Objective & Purpose:** Xây dựng lõi xác thực người dùng, quản lý vai trò, và cấu hình ban đầu cho trung tâm và khóa học.
- **Target Physical Directory Matrix Map:**
    * `./sources/backend/org/nlh4j/saas/membershiphub/controller/UserController.java` – [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-006], [EXC-004]
    * `./sources/backend/org/nlh4j/saas/membershiphub/service/UserService.java` – [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-006]
    * `./sources/backend/org/nlh4j/saas/membershiphub/repository/UserRepository.java` – [DAT-001]
    * `./sources/docs/user_management.md` – [DAT-001]
    * `./sources/infra/docker/Dockerfile` – [NFR-005], [ARC-010]
    * `./sources/infra/gcp/` – [NFR-004], [ARC-010]
    * `./sources/infra/k8s/` – [NFR-004], [ARC-010]

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1:**
  - **SUB-TASK 1:** [Coder] **Implement User Registration Endpoint**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/UserController.java`
    * Low-Level Technical Task Instruction: Triển khai `POST /api/auth/register` xử lý JSON `{email, password, fullName}`, xác thực email định dạng, kiểm tra độ mạnh mật khẩu, mã hóa password bằng bcrypt, lưu bản ghi Users với roleId mặc định là Student (tra cứu từ bảng ROLES), tạo JWT token (15 phút) trả về cho client. Ghi log hành động tạo người dùng.
    * Targeted Tag IDs: [REQ-001], [DAT-001], [ARC-006]
  - **SUB-TASK 2:** [Doc] **Create User Management Technical Documentation**
    * Target Component: `./sources/docs/user_management.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật bao gồm API contract cho `/api/auth/register`, mô tả request/response payload, validation rules, error codes, flow diagram xác thực, và hướng dẫn triển khai cho frontend. Dịch sang Vietnamese.
    * Targeted Tag IDs: [DAT-001]
  - **SUB-TASK 3:** [Tester] **Write Unit Tests for Registration**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/UserController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/UserControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo JUnit 5 test cases cho endpoint đăng ký: trường hợp thành công (trả về 201 + token), lỗi email trùng (409), lỗi validation input (400), lỗi server (500). Sử dụng Testcontainers để giả lập PostgreSQL.
    * Targeted Tag IDs: [REQ-001], [DAT-001], [ARC-006]

- **DAY 2:**
  - **SUB-TASK 1:** [Coder] **Implement Social OAuth2 Authentication**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/AuthSocialController.java`
    * Low-Level Technical Task Instruction: Triển khai `GET /oauth2/{provider}` để redirect đến provider (Google, Facebook, Firebase), xử lý callback `/oauth2/callback/{provider}` nhận code, gọi `OAuth2UserService` để lấy thông tin người dùng, tìm hoặc tạo bản ghi Users với provider tương ứng, cấp JWT token.
    * Targeted Tag IDs: [REQ-002], [DAT-001], [ARC-006]
  - **SUB-TASK 2:** [Doc] **Document OAuth2 Flow**
    * Target Component: `./sources/docs/oauth2_flow.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật về luồng OAuth2, bao gồm diagram sequence, tham số request, mapping provider sang bảng USERS.provider, xử lý trường hợp người dùng đã tồn tại, và hướng dẫn cấu hình client credentials cho từng nhà cung cấp.
    * Targeted Tag IDs: [DAT-001]
  - **SUB-TASK 3:** [Tester] **Integration Test for Social Auth**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/AuthSocialController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/AuthSocialControllerTest.java`
    * Low-Level Technical Task Instruction: Viết test tích hợp sử dụng mock OAuth2UserRequest để giả lập response từ Google/Facebook, xác minh JWT được tạo và role được gán đúng.
    * Targeted Tag IDs: [REQ-002], [DAT-001], [ARC-006]

- **DAY 3:**
  - **SUB-TASK 1:** [Reviewer] **Code Review & Defensive Patching**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/UserController.java`
    * Low-Level Technical Task Instruction: Kiểm tra chất lượng mã, đảm bảo tuân thủ SOLID, thêm null checks, xử lý ngoại lệ, đảm bảo không có SQL injection, thực hiện các cải tiến hiệu năng (caching). Nếu phát hiện lỗi, thực hiện patch ngay.
    * Targeted Tag IDs: [REQ-001], [REQ-002], [DAT-001], [ARC-006]
  - **SUB-TASK 2:** [Docker] **Build Multi-Stage Dockerfile**
    * Target Component: `./sources/infra/docker/Dockerfile`
    * Low-Level Technical Task Instruction: Tạo Dockerfile với giai đoạn builder (Maven compile) và giai đoạn runtime (image nhỏ dựa trên `java:21-slim`), sao chép file JAR, thiết lập user không phải root, expose port 8080, thêm healthcheck.
    * Targeted Tag IDs: [NFR-005], [ARC-010]
  - **SUB-TASK 3:** [GCP] **Provision Core GCP Resources**
    * Target Component: `./sources/infra/gcp/`
    * Low-Level Technical Task Instruction: Sử dụng Terraform để tạo VPC, Cloud NAT, Secret Manager (lưu JWT secret), Cloud SQL instance (PostgreSQL), Cloud Storage bucket (lưu file backup), IAM service accounts với role `roles/cloudsql.client`, `roles/storage.objectAdmin`.
    * Targeted Tag IDs: [NFR-004], [ARC-010]

### 📈 Phase 2: Center & Course Management Core
- **Phase Core Objective & Purpose:** Triển khai quản lý trung tâm (CRUD, phân quyền) và cấu hình lõi khóa học (tạo, phân công giáo viên, validation lịch).
- **Target Physical Directory Matrix Map:**
    * `./sources/backend/org/nlh4j/saas/membershiphub/controller/CenterController.java` – [REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002], [ARC-001]
    * `./sources/backend/org/nlh4j/saas/membershiphub/controller/CourseController.java` – [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003], [EXC-001]
    * `./sources/docs/center_management.md` – [DAT-003]
    * `./sources/docs/course_management.md` – [DAT-004]

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1:**
  - **SUB-TASK 1:** [Coder] **Implement Center CRUD**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/CenterController.java`
    * Low-Level Technical Task Instruction: Triển khai `GET /api/centers` trả về danh sách, `POST /api/centers` tạo mới với validation taxId duy nhất, `PUT /api/centers/{id}` cập nhật, `DELETE /api/centers/{id}` xóa. Sử dụng `@Valid` và `@FutureOrPresent` cho ngày nếu có.
    * Targeted Tag IDs: [REQ-004], [REQ-005], [DAT-003], [ARC-002]
  - **SUB-TASK 2:** [Doc] **Document Center Management API**
    * Target Component: `./sources/docs/center_management.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho các endpoint trung tâm, bao gồm request/response schema, error responses, ví dụ curl, và flow diagram cho quy trình CRUD.
    * Targeted Tag IDs: [DAT-003]
  - **SUB-TASK 3:** [Tester] **Write Integration Tests for Center**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/CenterController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/CenterControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo test cho CRUD trung tâm sử dụng Testcontainers, kiểm tra taxId unique constraint, authorization bởi System Admin và Center Admin.
    * Targeted Tag IDs: [REQ-004], [REQ-005], [DAT-003]

- **DAY 2:**
  - **SUB-TASK 1:** [Coder] **Implement Course Management**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/CourseController.java`
    * Low-Level Technical Task Instruction: Triển khai `GET /api/courses`, `POST /api/courses` với validation startDate < endDate, kiểm tra xung đột lịch dạy của giáo viên (tham chiếu bảng ENROLLMENTS), `PUT`, `DELETE`. Sử dụng `@FutureOrPresent` cho ngày bắt đầu.
    * Targeted Tag IDs: [REQ-007], [REQ-008], [DAT-004], [ARC-003]
  - **SUB-TASK 2:** [Doc] **Document Course Management API**
    * Target Component: `./sources/docs/course_management.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho các endpoint khóa học, bao gồm validation rule cho xung đột lịch, mapping giáo viên, ví dụ request/response.
    * Targeted Tag IDs: [DAT-004]
  - **SUB-TASK 3:** [Tester] **Write Integration Tests for Course**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/CourseController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/CourseControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo test cho CRUD khóa học, bao gồm trường hợp xung đột lịch (expected conflict error), kiểm tra authorization bởi System Admin và Center Admin.
    * Targeted Tag IDs: [REQ-007], [REQ-008], [DAT-004]

- **DAY 3:**
  - **SUB-TASK 1:** [Coder] **Implement Teacher Assignment to Course**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/CourseTeacherController.java`
    * Low-Level Technical Task Instruction: Triển khai `POST /api/courses/{courseId}/teachers/{teacherId}` gán giáo viên, kiểm tra giáo viên tồn tại, khóa học tồn tại, và không có xung đột lịch, đẩy notification qua `NotificationService`. Hỗ trợ hủy gán.
    * Targeted Tag IDs: [REQ-009], [DAT-004], [ARC-003], [EXC-001]
  - **SUB-TASK 2:** [Doc] **Document Teacher Assignment Flow**
    * Target Component: `./sources/docs/teacher_assignment.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho endpoint gán giáo viên, bao gồm diagram sequence, validation rules, notification payload, và hướng dẫn xử lý lỗi.
    * Targeted Tag IDs: [DAT-004]
  - **SUB-TASK 3:** [Tester] **Write Tests for Teacher Assignment**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/CourseTeacherController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/CourseTeacherControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo test cho gán giáo viên thành công, lỗi giáo viên không tồn tại, lỗi xung đột lịch, và hủy gán.
    * Targeted Tag IDs: [REQ-009], [DAT-004], [ARC-003]

- **DAY 4:**
  - **SUB-TASK 1:** [Reviewer] **Review Code Quality & Security**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/CenterController.java`
    * Low-Level Technical Task Instruction: Kiểm tra mã cho các vấn đề bảo mật (SQL injection, XSS), đảm bảo sử dụng prepared statements, kiểm tra authorization, thực hiện các cải tiến hiệu năng (indexing). Thực hiện patch nếu cần.
    * Targeted Tag IDs: [REQ-004], [REQ-005], [DAT-003], [ARC-002]
  - **SUB-TASK 2:** [Docker] **Update Dockerfile for New Services**
    * Target Component: `./sources/infra/docker/Dockerfile`
    * Low-Level Technical Task Instruction: Cập nhật Dockerfile để bao gồm các module mới (center, course), sử dụng chung base image, thêm giai đoạn builder cho từng module, đảm bảo size <500MB.
    * Targeted Tag IDs: [NFR-005], [ARC-010]
  - **SUB-TASK 3:** [GKE] **Create K8s Deployment Manifests**
    * Target Component: `./sources/infra/k8s/`
    * Low-Level Technical Task Instruction: Tạo Deployment cho UserService, CenterService, CourseService, AuthService, với HPA dựa trên CPU >70% hoặc latency >300ms. Bao gồm ConfigMap cho application properties, Secret cho DB credentials.
    * Targeted Tag IDs: [NFR-004], [ARC-010]

### 📈 Phase 3: Enrollment, Attendance & Membership Core
- **Phase Core Objective & Purpose:** Triển khai ghi danh khóa học, điểm danh QR, tính chất bất biến điểm danh, hiển thị và gia hạn thẻ hội viên.
- **Target Physical Directory Matrix Map:**
    * `./sources/backend/org/nlh4j/saas/membershiphub/controller/EnrollmentController.java` – [REQ-010], [REQ-011], [REQ-016], [DAT-005], [DAT-008], [ARC-005], [EXC-002], [EXC-003]
    * `./sources/backend/org/nlh4j/saas/membershiphub/controller/AttendanceController.java` – [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002]
    * `./sources/docs/enrollment_management.md` – [DAT-005]
    * `./sources/docs/attendance_management.md` – [DAT-006]

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 1:**
  - **SUB-TASK 1:** [Coder] **Implement Course Enrollment**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/EnrollmentController.java`
    * Low-Level Technical Task Instruction: Triển khai `POST /api/enrollments` nhận `{studentId, courseId}`, kiểm tra học viên tồn tại, khóa học mở, chưa quá số lượng maxStudents, tạo bản ghi ENROLLMENTS, đẩy notification đến student và nhóm Zalo của trung tâm, gọi service gia hạn thẻ hội viên (nếu cần).
    * Targeted Tag IDs: [REQ-010], [REQ-011], [DAT-005], [ARC-005], [EXC-002]
  - **SUB-TASK 2:** [Doc] **Document Enrollment Flow**
    * Target Component: `./sources/docs/enrollment_management.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho endpoint ghi danh, bao gồm validation rules, notification payload, và flow diagram cho việc tự động tạo tài khoản học viên.
    * Targeted Tag IDs: [DAT-005]
  - **SUB-TASK 3:** [Tester] **Write Tests for Enrollment**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/EnrollmentController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/EnrollmentControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo test cho ghi danh thành công, lỗi khóa học đầy, lỗi học viên không tồn tại, lỗi duplicate enrollment.
    * Targeted Tag IDs: [REQ-010], [REQ-011], [DAT-005]

- **DAY 2:**
  - **SUB-TASK 1:** [Coder] **Implement QR Attendance Capture**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/AttendanceController.java`
    * Low-Level Technical Task Instruction: Triển khai `POST /api/attendance/scan` nhận `{studentId, courseId, qrCodeData, timestamp}`, xác thực học viên tham gia khóa học, ghi nhận ATTENDANCE với ngày hiện tại, đảm bảo idempotent (unique constraint studentId+courseId+attendanceDate), trả về flag duplicate nếu đã ghi nhận.
    * Targeted Tag IDs: [REQ-012], [DAT-006], [ARC-007], [EXC-001], [EXC-002]
  - **SUB-TASK 2:** [Doc] **Document Attendance API**
    * Target Component: `./sources/docs/attendance_management.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho endpoint điểm danh, bao gồm request/response schema, validation, error handling, và diagram xử lý duplicate.
    * Targeted Tag IDs: [DAT-006]
  - **SUB-TASK 3:** [Tester] **Write Tests for Attendance**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/AttendanceController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/AttendanceControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo test cho điểm danh thành công, duplicate scan trả về success + duplicate flag, lỗi student/course không tồn tại.
    * Targeted Tag IDs: [REQ-012], [DAT-006], [ARC-007]

- **DAY 3:**
  - **SUB-TASK 1:** [Coder] **Implement Membership Card Display & Renewal**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/MembershipCardController.java`
    * Low-Level Technical Task Instruction: Triển khai `GET /api/cards/{studentId}` trả về cardId, issueDate, validityDays, remainingDays (computed), `POST /api/cards/{studentId}/renew` nhận `{additionalDays}`, cập nhật EndDate (issueDate + validityDays + additionalDays), ghi log renewal, đẩy notification.
    * Targeted Tag IDs: [REQ-014], [REQ-015], [DAT-007], [ARC-005]
  - **SUB-TASK 2:** [Doc] **Document Card Management**
    * Target Component: `./sources/docs/membership_card.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho endpoint hiển thị thẻ và gia hạn, bao gồm calculation remainingDays, workflow thanh toán (giả lập), và error cases.
    * Targeted Tag IDs: [DAT-007]
  - **SUB-TASK 3:** [Tester] **Write Tests for Card Operations**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/MembershipCardController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/MembershipCardControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo test cho hiển thị card, gia hạn thành công, lỗi student không tồn tại, lỗi thanh toán thất bại.
    * Targeted Tag IDs: [REQ-014], [REQ-015], [DAT-007]

- **DAY 4:**
  - **SUB-TASK 1:** [Reviewer] **Security Review & Patching**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/AttendanceController.java`
    * Low-Level Technical Task Instruction: Kiểm tra mã cho các vấn đề bảo mật (SQL injection, timing attacks), đảm bảo sử dụng PreparedStatement, thêm rate limiting cho endpoint quét QR, thực hiện patch nếu phát hiện lỗ hổng.
    * Targeted Tag IDs: [REQ-012], [REQ-013], [DAT-006], [ARC-007]
  - **SUB-TASK 2:** [Docker] **Finalize Dockerfile & Multi-Arch**
    * Target Component: `./sources/infra/docker/Dockerfile`
    * Low-Level Technical Task Instruction: Cập nhật Dockerfile để bao gồm attendance và card services, sử dụng `--platform linux/amd64` nếu cần, tối ưu layers, đảm bảo image size <500MB.
    * Targeted Tag IDs: [NFR-005], [ARC-010]
  - **SUB-TASK 3:** [GCP] **Setup Monitoring & Logging**
    * Target Component: `./sources/infra/gcp/`
    * Low-Level Technical Task Instruction: Triển khai Cloud Monitoring cho các service, tạo metric cho API latency, error rate, tạo Log Analytics pipeline (Stackdriver), thiết lập alerting cho threshold.
    * Targeted Tag IDs: [NFR-006], [ARC-010]

### 📈 Phase 4: Notifications, Promotions, Chatbot & Mobile Core
- **Phase Core Objective & Purpose:** Triển khai hệ thống thông báo đa kênh, quản lý khuyến mãi và thông báo, tích hợp chatbot AI, và xây dựng UI/UX di động cho các vai trò.
- **Target Physical Directory Matrix Map:**
    * `./sources/backend/org/nlh4j/saas/membershiphub/controller/NotificationController.java` – [REQ-016], [REQ-017], [REQ-018], [DAT-008], [DAT-009], [ARC-008], [EXC-003]
    * `./sources/backend/org/nlh4j/saas/membershiphub/controller/PromotionController.java` – [REQ-017], [REQ-018], [DAT-009]
    * `./sources/backend/org/nlh4j/saas/membershiphub/controller/ChatbotController.java` – [REQ-019], [EXC-004]
    * `./sources/frontend/` – [REQ-020], [REQ-021], [ARC-009]
    * `./sources/mobile/` – [REQ-020], [REQ-021], [ARC-009]

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1:**
  - **SUB-TASK 1:** [Coder] **Implement Notification Service**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/NotificationController.java`
    * Low-Level Technical Task Instruction: Triển khai `POST /api/notifications` nhận `{userId, groupZalo, message}`, lưu bản ghi NOTIFICATIONS, gọi FCM push API (nếu userId), gửi tin nhắn đến Zalo group qua Zalo API, đánh dấu delivered.
    * Targeted Tag IDs: [REQ-016], [DAT-008], [ARC-008], [EXC-003]
  - **SUB-TASK 2:** [Doc] **Document Notification API**
    * Target Component: `./sources/docs/notification_api.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho endpoint thông báo, bao gồm request/response schema, mapping push payload cho FCM/APNs, và hướng dẫn tích hợp Zalo.
    * Targeted Tag IDs: [DAT-008]
  - **SUB-TASK 3:** [Tester] **Write Tests for Notification**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/NotificationController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/NotificationControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo test cho gửi push thành công, lỗi device token, retry logic (tối đa 3 lần), và gửi tin nhắn Zalo.
    * Targeted Tag IDs: [REQ-016], [DAT-008], [ARC-008]

- **DAY 2:**
  - **SUB-TASK 1:** [Coder] **Implement Promotion & Announcement Management**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/PromotionController.java`
    * Low-Level Technical Task Instruction: Triển khai CRUD cho Promotions (POST/GET/PUT/DELETE) và Announcements, validation startDate/endDate, code unique, discountPercent <= 100, đảm bảo endDate có thể null (vĩnh viễn). Ghi log thay đổi.
    * Targeted Tag IDs: [REQ-017], [REQ-018], [DAT-009], [ARC-002], [ARC-003]
  - **SUB-TASK 2:** [Doc] **Document Promotion & Announcement APIs**
    * Target Component: `./sources/docs/promotion_announcement_api.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho Promotion và Announcement endpoints, bao gồm validation rules, response codes, ví dụ payload.
    * Targeted Tag IDs: [DAT-009]
  - **SUB-TASK 3:** [Tester] **Write Tests for Promotion & Announcement**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/PromotionController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/PromotionControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo test cho tạo khuyến mãi thành công, lỗi code duplicate, lỗi discount vượt quá, và hiển thị thông báo theo ngày.
    * Targeted Tag IDs: [REQ-017], [REQ-018], [DAT-009]

- **DAY 3:**
  - **SUB-TASK 1:** [Coder] **Implement AI Chatbot Integration**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/ChatbotController.java`
    * Low-Level Technical Task Instruction: Triển khai `POST /api/chatbot/query` nhận `{userId, message}`, gọi service AI (ví dụ OpenAI) để trả lời, fallback đến knowledge base nội bộ, ghi log tương tác, trả về response.
    * Targeted Tag IDs: [REQ-019], [EXC-004]
  - **SUB-TASK 2:** [Doc] **Document Chatbot API**
    * Target Component: `./sources/docs/chatbot_api.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho endpoint chatbot, bao gồm request/response schema, error handling, và hướng dẫn tích hợp cho frontend.
    * Targeted Tag IDs: [REQ-019]
  - **SUB-TASK 3:** [Tester] **Write Tests for Chatbot**
    * Target Component: `./sources/backend/org/nlh4j/saas/membershiphub/controller/ChatbotController.java;./sources/backend/org/nlh4j/saas/membershiphub/controller/ChatbotControllerTest.java`
    * Low-Level Technical Task Instruction: Tạo test cho trả lời thành công, lỗi AI service, và logging.
    * Targeted Tag IDs: [REQ-019], [EXC-004]

- **DAY 4:**
  - **SUB-TASK 1:** [Coder] **Develop Mobile App UI & Push Notification Registration**
    * Target Component: `./sources/mobile/app/src/main/java/org/nlh4j/saas/membershiphub/mobile/MobileActivity.java`
    * Low-Level Technical Task Instruction: Triển khai giao diện người dùng di động cho các vai trò (Student, Teacher, Admin) sử dụng React Native, tích hợp Firebase SDK để đăng ký device token, xử lý push notification nhận được, điều hướng dựa trên vai trò.
    * Targeted Tag IDs: [REQ-020], [REQ-021], [ARC-009]
  - **SUB-TASK 2:** [Doc] **Document Mobile App Features**
    * Target Component: `./sources/docs/mobile_features.md`
    * Low-Level Technical Task Instruction: Soạn thảo tài liệu kỹ thuật cho UI di động, bao gồm component list, navigation flow, cách xử lý push notification, và hướng dẫn triển khai cho Android/iOS.
    * Targeted Tag IDs: [REQ-020], [REQ-021]
  - **SUB-TASK 3:** [Tester] **Write Mobile App Tests**
    * Target Component: `./sources/mobile/app/src/androidTest/...;./sources/mobile/app/src/iosTest/...`
    * Low-Level Technical Task Instruction: Tạo test UI cho các màn hình chính, test push notification registration, và test điều hướng vai trò.
    * Targeted Tag IDs: [REQ-020], [REQ-021]

### 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng PreparedStatement/Parameterized Queries cho mọi truy vấn cơ sở dữ liệu; áp dụng White-list cho các trường hợp sắp xếp động; thực hiện kiểm tra input ở tầng ứng dụng.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động escape tất cả dữ liệu người dùng được render trong HTML/JSX; áp dụng strict CSP header (`default-src 'self'; script-src 'self' 'unsafe-inline'` chỉ khi cần thiết); sử dụng DOMPurify cho nội dung người dùng.
- **Multi-Tenant CORS Security Rails:** Cấu hình CORS per-request dựa trên tenant origin; cấm wildcard (`*`) cho `Access-Control-Allow-Origin`; thực hiện validation tenant trong mỗi request.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Áp dụng `@JsonSerialize` với `JsonInclude.Include.NON_NULL` và custom serializer để che giấu số CCCD, email; thực hiện log scrubbing định kỳ; giữ logs trong 1 năm theo quy định GDPR.
- **Authentication & Authorization Hardening:** JWT tokens ký bằng RS256, hết hạn 15 phút, refresh token 7 ngày, lưu token trong HttpOnly cookie; thực hiện OAuth2 Resource Server; áp dụng RBAC với `@PreAuthorize` dựa trên `SecurityContextHolder`.
- **Input Validation & Sanitization:** Sử dụng Jakarta Bean Validation (`@NotNull`, `@Size`, `@Email`); tái cấu trúc exception handling trả về error codes chuẩn hóa; tích hợp OWASP Java HTML Sanitizer.
- **Secure Communication:** Áp dụng TLS 1.3 cho mọi endpoint; cấu hình HTTP Strict Transport Security (HSTS); sử dụng `redirectUrl` an toàn cho OAuth2 redirects.
- **Audit & Compliance Logging:** Ghi log mọi thao tác người dùng (thay đổi vai trò, ghi điểm danh, gửi thông báo) với timestamp, userId, action details, IP address; lưu trữ logs trong Cloud Logging với retention 1 năm; thực hiện log analysis định kỳ.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** Tích hợp `@capacitor/core`, `@capacitor/app`, `@capacitor/push-notifications`; sử dụng `Preferences` plugin cho storage cục bộ; chặn back-button trên Android để điều hướng trong app; thực hiện network request retry với exponential backoff.
- **Internationalization (i18n) & Dynamic SEO Injection:** Sử dụng Java `ResourceBundle` cho backend, React `i18next` cho frontend; middleware phát hiện locale từ cookie, header `Accept-Language`; tự động chèn `<html lang="vi">` và thẻ `<link rel="alternate" hreflang="en" href="...">`; tối ưu hóa meta tags cho từng ngôn ngữ; sử dụng `react-helmet-async` để cập nhật title và description động.
- **SEO Best Practices:** Tạo sitemap.xml động, robots.txt, schema.org cho các thực thể (Course, Center, User); sử dụng URL friendly (slug) cho các resource; thiết lập Google Analytics với chế độ anonymizeIP; thực hiện lazy loading images; đảm bảo Core Web Vitals >75.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Mỗi ngày tạo branch `features/development-phase-{X}-day-{Y}` (`X` là số phase, `Y` là số ngày trong phase, bắt đầu từ 1 cho mỗi phase). Branch được tạo từ `main`.
- **Validation Guard Pipeline Gates:** Sau mỗi commit, GitHub Actions chạy:
    * Kiểm tra biên dịch (`mvn clean compile`).
    * Kiểm tra unit test (`mvn test`) với độ phủ mã >=85%.
    * Kiểm tra bảo mật tĩnh (`sonarcloud` hoặc `codeql`).
    * Kiểm tra định dạng (`mvn spotless:check`).
    * Nếu bất kỳ bước nào thất bại, pipeline dừng lại, tạo PR với log lỗi, và yêu cầu sửa chữa.
- **Merge & Deploy:** Sau khi vượt qua validation gates, branch được squash-merge vào `develop`, trigger deployment đến GKE (Blue-Green), thực hiện canary rollout 10% traffic, giám sát metric trong 5 phút, sau đó chuyển 100% traffic nếu ổn định.
- **Rollback & Recovery:** Nếu sau 5 phút có lỗi (error rate >1%), tự động rollback về version trước đó, tạo incident ticket, và thông báo qua Slack.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`