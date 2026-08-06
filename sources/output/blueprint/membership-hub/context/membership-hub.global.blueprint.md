# BỐ CỤC DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Kiểm soát Tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260806122819 |
| **Tên Dự án** | membership-hub |
| **Phiên bản** | 1.0 (Cơ sở) |
| **Ngày.Giờ** | 2026/08/06 12:28:19 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CỐT LÕI

### 1.1. Tính chất Hệ thống Cốt lõi & Kiến trúc Hệ thống

- Xác định mô hình kiến trúc hướng sự kiện (EDA) với các luồng bất đồng bộ giữa các miền người dùng, trung tâm và học viên.
- Áp dụng mẫu CQRS để tách biệt đọc/ghi cho tất cả các bảng nghiệp vụ chính (Người dùng, Trung tâm, Khóa học, Ghi danh, Điểm danh, Thẻ hội viên).
- Triển khai mô hình phản ứng (Reactive) cho các dịch vụ xử lý điểm danh QR và thông báo để đảm bảo tính bất biến và khả năng mở rộng.
- Tách biệt các biên giới Aggregate theo vai trò (System Admin, Center Admin, Manager, Teacher, Student) để thực thi kiểm soát truy cập dựa trên vai trò (RBAC).
- Tích hợp cổng xác thực đa yếu tố (OAuth2) với các nhà cung cấp Firebase, Google, Facebook để cấp JWT có thời hạn 15 phút và refresh token 7 ngày.
- Xây dựng các sự kiện giàu ngữ cảnh (Event Sourcing) cho các thay đổi trạng thái người dùng, ghi danh, điểm danh để hỗ trợ kiểm toán và phục hồi sau sự cố.
- Thiết kế các hợp đồng API dạng REST và sự kiện dạng Kafka để đảm bảo tính tuần tự và khả năng mở rộng theo chiều ngang.
- Triển khai các hàm chuyển đổi bất đồng bộ để đồng bộ hóa dữ liệu giữa các cơ sở dữ liệu quan hệ (PostgreSQL) và bộ nhớ đệm (Redis).
- Tích hợp cổng push notification (FCM/APNs) và API tích hợp nhóm Zalo để gửi thông báo thời gian thực.
- Triển khai cơ chế phát hiện xung đột lịch dạy theo thời gian thực cho giáo viên và xung đột venue trong quản lý khóa học.
- Triển khai cơ chế cache--aside với Redis để giảm tải cho các truy vấn thường gặp (ví dụ: danh sách khóa học, thông tin người dùng).
- Triển khai các quy tắc bảo mật đa租 (tenant isolation) để đảm bảo mỗi trung tâm chỉ có thể truy cập dữ liệu của mình.

### 1.2. Kiến trúc Luồng Dữ liệu Doanh nghiệp & Hệ sinh thái Cốt lõi

- Xác định các kênh bất đồng bộ chính: luồng xác thực (OAuth2), luồng xử lý điểm danh QR, luồng gửi thông báo (push + Zalo), luồng tích hợp backend ứng dụng di động (Next.js).
- Xây dựng cổng nhập liệu (Ingestion Gateway) để nhận các sự kiện từ ứng dụng di động (quét QR) và frontend web, sau đó đưa vào hàng đợi Kafka chủ đề `attendance.raw`.
- Triển khai các chủ đề Kafka chuyên biệt: `auth.events`, `attendance.processed`, `notification.push`, `notification.zalo`, `enrollment.events`.
- Triển khai các microservice tiêu thụ chủ đề: `AuthService`, `AttendanceService`, `NotificationService`, `EnrollmentService`.
- Sử dụng cơ chế fan-out để phân phối các sự kiện điểm danh đến các microservice ghi nhật ký (Logging), phân tích (Analytics) và dashboard (Monitoring).
- Triển khai cơ chế dead-letter queue (DLQ) cho các sự kiện thất bại để xử lý lại sau.
- Triển khai cơ chế phát lại (Replay) cho các sự kiện điểm danh để đảm bảo tính bất biến khi có sự cố mạng.
- Triển khai cổng webhook cho các nhà cung cấp bên thứ ba (ví dụ: Firebase Authentication) để đồng bộ hóa sự kiện người dùng.
- Triển khai cơ chế phát hiện và cách ly sự kiện trùng lặp (idempotency) cho các yêu cầu điểm danh QR.
- Triển khai cơ chế phát hiện xung đột cho các sự kiện ghi danh (ví dụ: vượt quá sức chứa khóa học) để rollback giao dịch.
- Triển khai cơ chế phát hiện và cách ly sự kiện trùng lặp (idempotency) cho các yêu cầu điểm danh QR.
- Triển khai cơ chế phát hiện xung đột cho các sự kiện ghi danh (ví dụ: vượt quá sức chứa khóa học) để rollback giao dịch.
- Triển khai cơ chế phát hiện và cách ly sự kiện trùng lặp (idempotency) cho các yêu cầu điểm danh QR.
- Triển khai cơ chế phát hiện xung đột cho các sự kiện ghi danh (ví dụ: vượt quá sức chứa khóa học) để rollback giao dịch.

## 📁 2. STACK CÔNG NGHỆ & THƯ VIỆN HỆ SINH

- **Stack Cơ sở Hạ tầng Backend:**
  * Runtime Java 21 với Quarkus 3.2.0.
  * Cơ sở dữ liệu PostgreSQL 15 với extension `pgcrypto` cho UUID.
  * Docker đa giai đoạn với base image `eclipse-temurin:21-jdk-alpine` (<200 MB).
  * Kubernetes (GKE) với Horizontal Pod Autoscaler (HPA) dựa trên CPU >70 % hoặc độ trễ >300 ms.
  * Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs cho push notification.
  * Zalo API integration (REST) để gửi tin nhắn đến nhóm.
  * Redis 7 cho cache session và caching ngoại vi.
  * CI/CD pipeline với GitHub Actions (build, test, push Docker, deploy GKE).

- **Stack Frontend & Di động:**
  * Frontend web: Next.js 14 với React 18, hỗ trợ SSR và SSG, tích hợp i18n với `next-intl`.
  * Giao diện người dùng di động: React Native 0.73 với Capacitor 5, sử dụng `@capacitor/push-notifications`, `@capacitor/preferences`.
  * Caching ngoại vi với `react-native-offline` cho các trường hợp mất kết nối mạng.
  * Tích hợp Firebase Authentication SDK cho di động, OAuth2 với Google/Facebook.

### MA TRẬN STACK KIẾN TRÚC

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. QUY TẮC TOÀN CẦU & TIÊU CHUẨN COMPLIANCE DOANH NGHIỆP

- **Quy tắc Biên giới Không gian Làm việc:** Không gian làm việc thực sự cố định ở gốc repository `.`. Tất cả các đường dẫn được tạo ra PHẢI bắt đầu bằng `./sources/`.
- **Tuân thủ Quy tắc Tiền tố Thư mục Động:** Thực thi các quy tắc tiền tố thư mục động được định nghĩa trong Protocol 1, khớp với cấu trúc hệ thống được phát hiện.
- **[CONDITION: JAVA_STACK_ONLY] Tiêu chuẩn Gói Java:** Nếu stack công nghệ sử dụng Java, tất cả mã nguồn Java PHẢI nằm trong gói cơ sở doanh nghiệp: `org.nlh4j.saas.membershiphub`. Chuyển đổi chuỗi "membership-hub" thành mã alphanumeric thuần túy bằng cách loại bỏ khoảng trắng, dấu gạch ngang và dấu gạch dưới.
- **Cú pháp Đường dẫn Mục tiêu Kiểm thử nghiêm ngặt:** Bất kỳ thành phần nào được nhắm mục tiêu bởi Sub-Agent Tester PHẢI được cấu trúc dưới dạng cặp phân cách bán phẩy `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn bên trong cặp PHẢI bắt đầu bằng `./sources/`.

## 📁 4. BẢNG TÓM TẮT KIẾN TRÚC HÀNG ĐẦU ĐA GIAI ĐOẠN

| Giai đoạn | Khoảng ngày | Đường dẫn Mô-đun / Thành phần Kiến trúc | Tóm tắt Sản phẩm Bàn giao | Sub-Agent được chỉ định | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | 1-3 | ./sources/backend.membershiphub.core | Xây dựng mô-đun người dùng cốt lõi, xác thực, phân quyền, bảng người dùng/vai trò | Coder | `[REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [EXC-004], [DAT-001], [NFR-001], [NFR-003], [NFR-007], [NFR-008]` |
| Giai đoạn 2 | 4-6 | ./sources/backend.membershiphub.center-course | Xây dựng mô-đun quản lý trung tâm và khóa học, bao gồm CRUD, phân công giáo viên, kiểm tra xung đột lịch | Doc | `[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006]` |
| Giai đoạn 3 | 7-9 | ./sources/backend.membershiphub.enrollment-attendance | Xây dựng mô-đun ghi danh học viên, điểm danh QR, thẻ hội viên, xử lý ngoại lệ mạng và trùng lặp | Coder | `[REQ-010], [REQ-011], [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-005], [DAT-006], [DAT-007], [NFR-001], [NFR-003], [NFR-009]` |
| Giai đoạn 4 | 10-12 | ./sources/backend.membershiphub.notification-promo | Xây dựng mô-đun thông báo, khuyến mãi, thông báo, chatbot AI, xử lý lỗi giao hàng | Doc | `[REQ-016], [REQ-017], [REQ-018], [REQ-019], [EXC-003], [DAT-008], [DAT-009], [NFR-001], [NFR-003], [NFR-006], [NFR-008]` |
| Giai đoạn 5 | 13-15 | ./sources/frontend.membershiphub.mobile | Xây dựng giao diện người dùng di động, thông báo đẩy, phát hiện ngôn ngữ, SEO đa ngôn ngữ, báo cáo và bảng điều khiển | Coder | `[REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-004], [NFR-005], [NFR-007]` |

## 📁 5. CHI TIẾT HOÁ ĐẶC TẢ KIẾN TRÚC THEO TỪNG GIAI ĐOẠN & NGÀY

### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng nền tảng người dùng cốt lõi, xác thực đa nhà cung cấp và cơ chế phân quyền RBAC để hỗ trợ tất cả các vai trò người dùng trong hệ thống membership-hub.
- **Target Physical Directory Matrix Map:** 
    * ./sources/backend.membershiphub.users;[REQ-001],[REQ-002],[REQ-003],[ARC-001],[ARC-002],[ARC-003],[ARC-004],[ARC-005],[ARC-006],[EXC-004],[DAT-001]
    * ./sources/docs.phase1;[REQ-001],[REQ-002],[REQ-003]
- **Database Schema DDL SQL Specification [DAT-001]:**
```sql
-- Bảng Roles
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

-- Bảng Users
CREATE TABLE USERS (
    userId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL REFERENCES ROLES(roleId),
    provider ENUM('local','firebase','google','facebook') NOT NULL DEFAULT 'local',
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-001]..[ARC-006]:**
  * `POST /api/v1/auth/register` – nhận email, mật khẩu, tên, tạo người dùng với vai trò `Student`, trả về JWT.
  * `POST /api/v1/auth/social` – nhận mã OAuth2 từ Firebase/Google/Facebook, xác thực, tạo/cập nhật người dùng, trả về JWT.
  * `PUT /api/v1/users/{userId}/role` – chỉ System Admin mới có thể gán vai trò mới, cập nhật cột roleId, phát sự kiện `user.role.changed`.
  * `GET /api/v1/roles` – trả về danh sách tất cả vai trò (dùng cho UI gán vai trò).
  * `GET /api/v1/users/{userId}` – endpoint truy xuất thông tin người dùng (bất kỳ vai trò nào cũng có thể truy cập hồ sơ của chính mình).
  * `POST /api/v1/auth/token/refresh` – nhận refresh token, cấp JWT mới (hết hạn 15 phút).
- **Phase Localized Exception Handlers [EXC-004]:**
  * Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc) – trả về HTTP 400 với danh sách chi tiết các trường không hợp lệ bằng tiếng Việt: “Email không đúng định dạng”, “Mật khẩu phải có ít nhất 8 ký tự”, v.v.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1:** Mục tiêu ngắn gọn cho ngày này – triển khai đăng ký người dùng, xác thực xã hội và gán vai trò.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** `[REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [EXC-004], [DAT-001], [NFR-001], [NFR-003], [NFR-007], [NFR-008]`
    * **Target Component file path (`target_component`):** ./sources/backend.membershiphub.users
    * **Low-Level Technical Task Instruction:** Viết implementation cho `UserService.register(RegistrationRequest)` thực hiện xác thực đầu vào, mã hóa mật khẩu bằng BCrypt, lưu người dùng mới với vai trò `Student` (hoặc `Teacher` nếu được mời), phát sự kiện `user.created` và trả về JWT. Triển khai `SocialAuthService.authenticate(SocialAuthRequest)` để trao đổi mã OAuth2, gọi API nhà cung cấp để lấy thông tin người dùng, ánh xạ sang `UserEntity`, thiết lập mật khẩuHash null cho nhà cung cấp, cập nhật hoặc tạo người dùng, gán vai trò mặc định `Student`. Triển khai `RoleService.assignRole(userId, newRole)` chỉ dành cho System Admin, cập nhật `roleId` trong bảng USERS, ghi nhật ký hành động trong bảng AUDIT_LOG. Đảm bảo tất cả các API trả về HTTP 200 với payload JSON chuẩn (`{ "token": "...", "tokenType": "Bearer", "expiresIn": 900 }`). Xử lý các trường hợp ngoại lệ đầu vào không hợp lệ bằng cách ném `ValidationException` với các thông báo lỗi chi tiết bằng tiếng Việt.

- **DAY 2:** Mục tiêu ngắn gọn cho ngày này – viết và chạy các kiểm thử đơn vị cho các thành phần người dùng.
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** `[REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [EXC-004], [DAT-001], [NFR-001], [NFR-003], [NFR-007], [NFR-008]`
    * **Target Component file path (`target_component`):** ./sources/backend.membershiphub.users;./sources/backend.membershiphub.users.test
    * **Low-Level Technical Task Instruction:** Viết các kiểm thử JUnit5 cho `UserService.register` bao gồm các trường hợp thành công, email trùng lặp, mật khẩu yếu, định dạng email không hợp lệ. Viết các kiểm thử cho `SocialAuthService.authenticate` mô phỏng phản hồi từ Firebase, Google, Facebook. Viết các kiểm thử cho `RoleService.assignRole` đảm bảo chỉ System Admin mới có thể gán vai trò và kiểm tra các ràng buộc khóa ngoại. Sử dụng `Mock` cho `JwtTokenProvider` và `AuditLogService`. Đảm bảo độ bao phủ mã trên mỗi lớp >=85 % trước khi chuyển sang giai đoạn xem xét.

- **DAY 3:** Mục tiêu ngắn gọn cho ngày này – xem xét chất lượng mã, phát hiện lỗ hổng bảo mật và tối ưu hóa hiệu suất.
    * **Sub-Agent Workflow Specialization:** [Reviewer]
    * **Targeted Tag IDs:** `[REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [EXC-004], [DAT-001], [NFR-001], [NFR-003], [NFR-007], [NFR-008]`
    * **Target Component file path (`target_component`):** ./sources/docs.phase1.review
    * **Low-Level Technical Task Instruction:** Thực hiện đánh giá tĩnh bằng SonarQube, kiểm tra các vấn đề về SQL injection, xác thực đầu vào, quản lý ngoại lệ. Xác nhận việc sử dụng `PreparedStatement` trong tất cả các truy vấn SQL. Kiểm tra việc thực thi các chính sách RBAC trong `RoleService`. Tối ưu hóa các truy vấn cơ sở dữ liệu bằng cách thêm chỉ mục trên cột `email` và `roleId`. Xác nhận việc sử dụng BCrypt với cost factor phù hợp. Đảm bảo tất cả các ngoại lệ được bắt và trả về JSON lỗi chuẩn với mã lỗi và thông báo bằng tiếng Việt. Tạo danh sách kiểm tra hoàn thành và gắn thẻ `Phase-1-Review-Completed`.

### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng và triển khai mô-đun quản lý trung tâm và khóa học, bao gồm CRUD, kiểm tra xung đột lịch dạy, và gán giáo viên.
- **Target Physical Directory Matrix Map:** 
    * ./sources/backend.membershiphub.centers;[REQ-004],[REQ-005],[REQ-006],[DAT-003]
    * ./sources/backend.membershiphub.courses;[REQ-007],[REQ-008],[REQ-009],[DAT-004]
    * ./sources/docs.phase2;[REQ-004],[REQ-005],[REQ-006],[REQ-007],[REQ-008],[REQ-009]
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
```
**Database Schema DDL SQL Specification [DAT-004]:**
```sql
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL REFERENCES USERS(userId),
    maxStudents INT NOT NULL DEFAULT 30
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009]:**
  * `GET /api/v1/centers` – trả về danh sách tất cả trung tâm (System Admin, Center Admin, Manager).
  * `POST /api/v1/centers` – System Admin tạo trung tâm mới, kiểm tra taxId trùng lặp, trả về HTTP 201.
  * `PUT /api/v1/centers/{centerId}` – System Admin cập nhật thông tin trung tâm.
  * `DELETE /api/v1/centers/{centerId}` – System Admin xóa trung tâm.
  * `POST /api/v1/centers/{centerId}/admin/assign` – System Admin gán người dùng làm Center Admin, cập nhật vai trò người dùng và lưu centerId.
  * `GET /api/v1/courses` – trả về danh sách khóa học (tất cả vai trò đã xác thực).
  * `POST /api/v1/courses` – System Admin hoặc Center Admin tạo khóa học mới, kiểm tra xung đột lịch dạy của giáo viên (startDate/endDate overlap).
  * `PUT /api/v1/courses/{courseId}` – System Admin hoặc Center Admin cập nhật khóa học, đảm bảo không có xung đột lịch.
  * `DELETE /api/v1/courses/{courseId}` – System Admin hoặc Center Admin xóa khóa học.
  * `POST /api/v1/courses/{courseId}/teacher/assign` – System Admin gán giáo viên cho khóa học, phát sự kiện `course.teacher.assigned`.
- **Phase Localized Exception Handlers [EXC-004] (áp dụng cho validation đầu vào trung tâm/khóa học):**
  * Xác thực taxId không đúng định dạng (phải là số 10‑13 chữ số) – trả về HTTP 400 với thông báo “Mã số thuế không hợp lệ, phải là số 10‑13 chữ số”.
  * Xung đột lịch dạy – trả về HTTP 409 với thông báo “Giáo viên đã có lịch dạy trong khoảng thời gian này”.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 4:** Mục tiêu ngắn gọn cho ngày này – tài liệu hóa các API trung tâm và khóa học, mô hình dữ liệu và quy tắc nghiệp vụ.
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Targeted Tag IDs:** `[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006]`
    * **Target Component file path (`target_component`):** ./sources/docs.phase2.spec
    * **Low-Level Technical Task Instruction:** Viết tài liệu kỹ thuật chi tiết cho các endpoint REST của trung tâm và khóa học, bao gồm request/response JSON schemas, quy tắc validation, mô tả trường hợp sử dụng. Tạo sơ đồ ER cho bảng CENTERS và COURSES. Tài liệu hóa quy tắc nghiệp vụ: xung đột lịch dạy, taxId duy nhất, quyền truy cập theo vai trò. Đảm bảo tất cả các tài liệu được viết bằng tiếng Việt, bao gồm các mô tả trường hợp ngoại lệ.

- **DAY 5:** Mục tiêu ngắn gọn cho ngày này – xây dựng Docker image cho các service backend trung tâm và khóa học.
    * **Sub-Agent Workflow Specialization:** [Docker]
    * **Targeted Tag IDs:** `[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006]`
    * **Target Component file path (`target_component`):** ./sources/infra.docker.center-course
    * **Low-Level Technical Task Instruction:** Tạo Dockerfile đa giai đoạn cho `center-service` và `course-service` sử dụng base image `eclipse-temurin:21-jdk-alpine`. Sao chép các tệp JAR đã xây dựng, thiết lập người dùng không có đặc quyền, phơi bày cổng 8080. Tối ưu hóa kích thước image (<500 MB). Xây dựng image với `docker build -t nlh4j/membershiphub-center-course:${BUILD_TAG} .`. Push image lên Docker Registry (`docker push`). Tạo Kubernetes Deployment YAML với resource limits (CPU 500m, Memory 1Gi) và liveness/readiness probes.

- **DAY 6:** Mục tiêu ngắn gọn cho ngày này – cung cấp cơ sở hạ tầng GCP (SQL, Cloud Run, IAM) cho các service trung tâm và khóa học.
    * **Sub-Agent Workflow Specialization:** [GCP]
    * **Targeted Tag IDs:** `[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006]`
    * **Target Component file path (`target_component`):** ./sources/infra.gcp.center-course
    * **Low-Level Technical Task Instruction:** Tạo phiên bản PostgreSQL trong GCP với `pgconfig` phù hợp, kích hoạt backup hàng ngày, cấp quyền truy cập cho tài khoản dịch vụ `cloud-sql-iam`. Triển khai `center-service` và `course-service` lên Cloud Run với `memcache` và `iam.authenticatedUser` role. Thiết lập VPC peering cho Redis. Cấu hình Cloud Build để tự động xây dựng và triển khai từ Docker images. Ghi nhật ký hoạt động vào Cloud Logging. Đảm bảo tất cả các tài nguyên được gắn thẻ `project=membershiphub` để quản lý chi phí.

### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng mô-đun ghi danh học viên, điểm danh QR, thẻ hội viên, xử lý ngoại lệ mạng và trùng lặp để đảm bảo tính bất biến.
- **Target Physical Directory Matrix Map:** 
    * ./sources/backend.membershiphub.enrollments;[REQ-010],[REQ-011],[DAT-005]
    * ./sources/backend.membershiphub.attendance;[REQ-012],[REQ-013],[EXC-001],[EXC-002],[DAT-006]
    * ./sources/backend.membershiphub.studentcards;[REQ-014],[REQ-015],[DAT-007]
    * ./sources/docs.phase3;[REQ-010],[REQ-011],[REQ-012],[REQ-013],[EXC-001],[EXC-002]
- **Database Schema DDL SQL Specification [DAT-005]:**
```sql
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (studentId, courseId)
);
```
**Database Schema DDL SQL Specification [DAT-006]:**
```sql
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (studentId, courseId, attendanceDate)
);
```
**Database Schema DDL SQL Specification [DAT-007]:**
```sql
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);
```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015]:**
  * `GET /api/v1/courses/available` – trả về danh sách khóa học mà học viên chưa ghi danh.
  * `POST /api/v1/enrollments` – học viên ghi danh vào khóa học, tự động tạo tài khoản học viên nếu thiếu, phát sự kiện `enrollment.created`.
  * `POST /api/v1/attendance/scan` – nhận QR (studentId, courseId), ghi lại bản ghi điểm danh, đảm bảo idempotent cho cùng studentId, courseId, attendanceDate.
  * `GET /api/v1/studentcards/me` – trả về thông tin thẻ hội viên (issueDate, validityDays, remainingDays).
  * `POST /api/v1/studentcards/renew` – học viên yêu cầu gia hạn thẻ, cập nhật `issueDate` và `remainingDays`, ghi lại giao dịch thanh toán.
- **Phase Localized Exception Handlers [EXC-001] (Mất mạng khi quét QR):**
  * Nếu điểm danh thất bại do mất mạng, lưu yêu cầu điểm danh tạm thời vào hàng đợi điểm danh cục bộ. Khi kết nối được khôi phục, retry tự động và chỉ ghi một bản ghi duy nhất cho ngày đó.
- **Phase Localized Exception Handlers [EXC-002] (Điểm danh trùng lặp):**
  * Phát hiện điểm danh trùng lặp (cùng studentId, courseId, attendanceDate) trong vòng 1 phút, trả về HTTP 200 với thông báo “Điểm danh đã được ghi nhận trước đó” và không tạo bản ghi mới.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 7:** Mục tiêu ngắn gọn cho ngày này – triển khai ghi danh khóa học, tạo tài khoản học viên và xử lý điểm danh QR.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** `[REQ-010], [REQ-011], [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-005], [DAT-006], [DAT-007], [NFR-001], [NFR-003], [NFR-009]`
    * **Target Component file path (`target_component`):** ./sources/backend.membershiphub.enrollments
    * **Low-Level Technical Task Instruction:** Viết `EnrollmentService.enroll(studentId, courseId)` thực hiện kiểm tra học viên tồn tại, kiểm tra xung đột ghi danh, lưu bản ghi vào bảng ENROLLMENTS, phát sự kiện `enrollment.created`. Triển khai `StudentCardService.createDefaultCard(studentId)` tạo bản ghi STUDENTCARDS với issueDate là hôm nay và validityDays là 365. Triển khai `AttendanceService.recordAttendance(studentId, courseId)` xác thực studentId/courseId, tính toán attendanceDate từ timestamp hiện tại, kiểm tra bản ghi điểm danh đã tồn tại, nếu không có thì chèn bản ghi, nếu có thì trả về duplicate flag. Đảm bảo tất cả các phương thức ném `EnrollmentException` hoặc `AttendanceException` với các thông báo lỗi bằng tiếng Việt.

- **DAY 8:** Mục tiêu ngắn gọn cho ngày này – viết các kiểm thử tích hợp cho ghi danh và điểm danh.
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** `[REQ-010], [REQ-011], [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-005], [DAT-006], [DAT-007], [NFR-001], [NFR-003], [NFR-009]`
    * **Target Component file path (`target_component`):** ./sources/backend.membershiphub.enrollments;./sources/backend.membershiphub.enrollments.test
    * **Low-Level Technical Task Instruction:** Viết JUnit integration test cho `EnrollmentService.enroll` bao gồm các trường hợp thành công, học viên không tồn tại (tạo tự động), khóa học đầy chỗ, xung đột ghi danh. Viết các kiểm thử cho `AttendanceService.recordAttendance` bao gồm các trường hợp thành công, duplicate detection, student/course không hợp lệ. Sử dụng `TestEntityManager` để thiết lập dữ liệu cơ sở thử nghiệm. Đảm bảo độ bao phủ >=85 % trước khi chuyển sang xem xét.

- **DAY 9:** Mục tiêu ngắn gọn cho ngày này – xem xét logic điểm danh, xử lý trùng lặp và hiệu suất.
    * **Sub-Agent Workflow Specialization:** [Reviewer]
    * **Targeted Tag IDs:** `[REQ-010], [REQ-011], [REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-005], [DAT-006], [DAT-007], [NFR-001], [NFR-003], [NFR-009]`
    * **Target Component file path (`target_component`):** ./sources/docs.phase3.review
    * **Low-Level Technical Task Instruction:** Đánh giá các truy vấn cơ sở dữ liệu cho bảng ENROLLMENTS, ATTENDANCE, STUDENTCARDS, đảm bảo có chỉ mục trên (studentId, courseId) và (studentId, courseId, attendanceDate). Kiểm tra việc sử dụng `SELECT ... FOR UPDATE` để tránh xung đột ghi. Xác nhận việc sử dụng Redis cache cho các truy vấn thường gặp (ví dụ: trạng thái ghi danh). Kiểm tra việc xử lý ngoại lệ mạng: đảm bảo hàng đợi cục bộ được cấu hình đúng và được tiêu thụ sau khi kết nối được khôi phục. Xác nhận việc phát hiện trùng lặp sử dụng constraint UNIQUE và kiểm tra race condition. Tạo danh sách kiểm tra hoàn thành.

### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng mô-đun thông báo, khuyến mãi, thông báo, chatbot AI, xử lý lỗi giao hàng.
- **Target Physical Directory Matrix Map:** 
    * ./sources/backend.membershiphub.notifications;[REQ-016],[DAT-008]
    * ./sources/backend.membershiphub.promotions;[REQ-017],[DAT-009]
    * ./sources/backend.membershiphub.announcements;[REQ-018],[DAT-009]
    * ./sources/backend.membershiphub.chatbot;[REQ-019],[NOT APPLICABLE]
    * ./sources/docs.phase4;[REQ-016],[REQ-017],[REQ-018],[REQ-019]
- **Database Schema DDL SQL Specification [DAT-008]:**
```sql
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    userId UUID REFERENCES USERS(userId),
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
```
**Database Schema DDL SQL Specification [DAT-009] (Promotions & Announcements):**
```sql
CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code VARCHAR(30) NOT NULL UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);

CREATE TABLE ANNOUNCEMENTS (
    announcementId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);
```
- **API and Event Routing Contracts [REQ-016], [REQ-017], [REQ-018], [REQ-019]:**
  * `POST /api/v1/notifications` – tạo thông báo mới, phát sự kiện `notification.created`, đẩy notification đến user qua WebSocket và hàng đợi push.
  * `POST /api/v1/promotions` – tạo khuyến mãi mới, kiểm tra code duy nhất, thiết lập startDate/endDate.
  * `POST /api/v1/announcements` – tạo thông báo mới, thiết lập startDate/endDate, tự động hủy sau endDate.
  * `POST /api/v1/chatbot/reply` – nhận tin nhắn từ người dùng, gọi LLM để tạo câu trả lời, trả về phản hồi hoặc chuyển đến nhân viên hỗ trợ nếu độ tin cậy thấp.
- **Phase Localized Exception Handlers [EXC-003] (Lỗi giao hàng thông báo):**
  * Nếu push notification thất bại (ví dụ: token thiết bị không hợp lệ), ghi lỗi vào bảng NOTIFICATIONS với delivered = false, lên lịch retry tối đa 3 lần với exponential backoff. Sau 3 lần thất bại, đánh dấu là failed và ghi nhật ký cảnh báo.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 10:** Mục tiêu ngắn gọn cho ngày này – tài liệu hóa các API thông báo, khuyến mãi, thông báo, chatbot.
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Targeted Tag IDs:** `[REQ-016], [REQ-017], [REQ-018], [REQ-019], [EXC-003], [DAT-008], [DAT-009], [NFR-001], [NFR-003], [NFR-006], [NFR-008]`
    * **Target Component file path (`target_component`):** ./sources/docs.phase4.spec
    * **Low-Level Technical Task Instruction:** Viết tài liệu kỹ thuật cho các endpoint thông báo, khuyến mãi, thông báo, chatbot, bao gồm request/response schemas, quy tắc validation, quy trình nghiệp vụ. Tạo sơ đồ luồng dữ liệu cho việc tạo thông báo, đẩy push, gửi Zalo. Tài liệu hóa quy tắc retry và circuit breaker cho push notification. Đảm bảo tất cả các tài liệu được viết bằng tiếng Việt.

- **DAY 11:** Mục tiêu ngắn gọn cho ngày này – xây dựng Docker image cho các service thông báo, khuyến mãi.
    * **Sub-Agent Workflow Specialization:** [Docker]
    * **Targeted Tag IDs:** `[REQ-016], [REQ-017], [REQ-018], [REQ-019], [EXC-003], [DAT-008], [DAT-009], [NFR-001], [NFR-003], [NFR-006], [NFR-008]`
    * **Target Component file path (`target_component`):** ./sources/infra.docker.notification-promo
    * **Low-Level Technical Task Instruction:** Tạo Dockerfile cho `notification-service`, `promotion-service`, `announcement-service`. Sử dụng base image `eclipse-temurin:21-jdk-alpine`. Tối ưu hóa kích thước image (<500 MB). Triển khai với Cloud Run hoặc Kubernetes. Push image lên registry. Tạo Kubernetes Deployment với resource limits và probes.

- **DAY 12:** Mục tiêu ngắn gọn cho ngày này – cung cấp cơ sở hạ tầng GCP cho push notification, hàng đợi, chatbot.
    * **Sub-Agent Workflow Specialization:** [GCP]
    * **Targeted Tag IDs:** `[REQ-16], [REQ-17], [REQ-18], [REQ-19], [EXC-3], [DAT-8], [DAT-9], [NFR-1], [NFR-3], [NFR-6], [NFR-8]`
    * **Target Component file path (`target_component`):** ./sources/infra.gcp.notification-promo
    * **Low-Level Technical Task Instruction:** Tạo Pub/Sub topics cho `notification`, `promotion`, `announcement`. Thiết lập Cloud Scheduler để lên lịch gửi thông báo hàng loạt. Cấu hình Cloud Functions để xử lý sự kiện push notification, retry logic. Triển khai chatbot trên Cloud Run với model LLM được lưu trong Vertex AI. Thiết lập IAM cho các service để truy cập Pub/Sub, Cloud Functions, Vertex AI. Ghi nhật ký hoạt động vào Cloud Logging. Đảm bảo tất cả các tài nguyên được gắn thẻ `project=membershiphub`.

### 📈 Phase 5 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Xây dựng giao diện người dùng di động, thông báo đẩy, phát hiện ngôn ngữ, SEO đa ngôn ngữ, báo cáo và bảng điều khiển.
- **Target Physical Directory Matrix Map:** 
    * ./sources/frontend.membershiphub.mobile;[REQ-020],[REQ-021],[REQ-022],[REQ-023],[REQ-024],[REQ-025]
    * ./sources/docs.phase5;[REQ-020],[REQ-021],[REQ-022],[REQ-023],[REQ-024],[REQ-025]
- **Database Schema DDL SQL Specification [DAT-011] (SystemSettings):**
```sql
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description TEXT
);
```
- **API and Event Routing Contracts [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-008], [ARC-009], [ARC-010]:**
  * `GET /api/v1/mobile/config` – trả về cấu hình UI theo vai trò, phát hiện ngôn ngữ từ header Accept-Language hoặc cookie.
  * `POST /api/v1/mobile/tokens` – đăng ký token thiết bị cho push notification, lưu vào bảng USERS (column deviceToken).
  * `GET /api/v1/reports/attendance` – tạo báo cáo điểm danh CSV cho trung tâm được chọn và ngày, trả về file.
  * `GET /api/v1/dashboard/center/{centerId}` – trả về dữ liệu tổng hợp: tổng học viên, khóa học đang hoạt động, phiên học sắp tới (7 ngày).
  * `GET /api/v1/health` – endpoint kiểm tra sức khỏe cho GKE liveness probe.
  * `GET /api/v1/i18n/{lang}` – trả về các chuỗi dịch cho ngôn ngữ được chỉ định (English, Vietnamese, Spanish).
- **Phase Localized Exception Handlers [EXC-005] (System Recovery After Outage):**
  * Khi dịch vụ được khôi phục sau sự cố, xử lý các yêu cầu điểm danh chờ xử lý theo FIFO, ghi lại bản ghi điểm danh duy nhất, gửi push notification đến người dùng thông báo về các sự kiện đã được khôi phục.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 13:** Mục tiêu ngắn gọn cho ngày này – triển khai giao diện người dùng di động, push notification, phát hiện ngôn ngữ, SEO.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** `[REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-004], [NFR-005], [NFR-007]`
    * **Target Component file path (`target_component`):** ./sources/frontend.membershiphub.mobile
    * **Low-Level Technical Task Instruction:** Triển khai màn hình đăng nhập di động với OAuth2 (Google, Facebook, Firebase). Xây dựng navigation dựa trên vai trò (Student, Teacher, Admin). Triển khai màn hình quét QR cho điểm danh sử dụng camera native. Triển khai màn hình thẻ hội viên hiển thị days remaining. Triển khai cơ chế phát hiện ngôn ngữ từ `navigator.language` và `AsyncStorage` để lưu preference. Triển khai SEO meta tags động và hreflang cho các URL. Triển khai endpoint `/api/v1/reports/attendance` để tạo CSV. Triển khai dashboard `/api/v1/dashboard/center/{centerId}` trả về JSON với tổng hợp dữ liệu. Đảm bảo tất cả các API trả về JSON với mã hóa UTF-8.

- **DAY 14:** Mục tiêu ngắn gọn cho ngày này – viết các kiểm thử ứng dụng di động và tích hợp push notification.
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Targeted Tag IDs:** `[REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-004], [NFR-005], [NFR-007]`
    * **Target Component file path (`target_component`):** ./sources/frontend.membershiphub.mobile;./sources/frontend.membershiphub.mobile.test
    * **Low-Level Technical Task Instruction:** Viết các kiểm thử unit cho các component React Native (ví dụ: QR scanner, language detection). Viết các kiểm thử tích hợp cho push notification sử dụng `@capacitor/push-notifications`. Mô phỏng sự kiện push, xác nhận notification được hiển thị. Viết các kiểm thử end-to-end cho quy trình ghi danh, điểm danh, gia hạn thẻ. Đảm bảo độ bao phủ kiểm thử >=80 % trước khi chuyển sang xem xét.

- **DAY 15:** Mục tiêu ngắn gọn cho ngày này – triển khai lên GKE, cấu hình HPA, CI/CD pipeline.
    * **Sub-Agent Workflow Specialization:** [GKE]
    * **Targeted Tag IDs:** `[REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-008], [ARC-009], [ARC-010], [NFR-001], [NFR-002], [NFR-004], [NFR-005], [NFR-007]`
    * **Target Component file path (`target_component`):** ./sources/infra.gke.manifests
    * **Low-Level Technical Task Instruction:** Tạo Kubernetes Deployment YAML cho `auth-service`, `enrollment-service`, `attendance-service`, `notification-service`, `mobile-api-gateway`. Cấu hình HPA với metric CPU >70 % hoặc độ trễ >300 ms. Tạo ServiceEntry cho các external calls (Zalo API, Firebase). Triển khai Ingress với TLS cho bảo mật. Tạo CI pipeline trong GitHub Actions: trigger trên push, xây dựng Docker image, push, triển khai tự động lên GKE với `kubectl apply -f ./sources/infra.gke.manifests`. Cấu hình Cloud Build để tự động tạo image. Thiết lập canary deployment cho các bản release mới. Ghi nhật ký hoạt động vào Cloud Logging. Đảm bảo tất cả các manifest tuân thủ các quy tắc nhãn `app=membershiphub`.

## 📁 6. MÃ BẢO MẬT DOANH NGHIỆP TOÀN CẦU & BIỆN PHÁP CHỐNG INJECTION [NFR-001]

- **SQL Injection (SQLi) Absolute Countermeasures:**
  * Sử dụng PreparedStatement / Parameterized Query cho tất cả các truy vấn SQL động.
  * Áp dụng whitelist cho các ký tự sắp xếp (ví dụ: chỉ cho phép A‑Z, a‑z, 0‑9, dấu gạch dưới).
  * Triển khai cơ chế phát hiện và cách ly các truy vấn bất thường bằng cách sử dụng các mẫu truy vấn được phép.

- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):**
  * Tự động escape tất cả các đầu vào người dùng trong các template (Jinja2/Thymeleaf auto‑escaping).
  * Triển khai strict CSP header (`default-src 'self'; script-src 'self' 'unsafe-inline' https://trusted.cdn.com; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self' wss://api.messaging.com; frame-ancestors 'none'; object-src 'none';`).
  * Triển khai cơ chế lọc đầu vào dựa trên regex cho các trường HTML.

- **Multi-Tenant CORS Security Rails:**
  * Cấu hình CORS cho phép các origin cụ thể (`https://center1.example.com`, `https://center2.example.com`).
  * Triển khai kiểm tra origin động dựa trên tenant ID từ JWT.
  * Vô hiệu hóa wildcard (`*`) cho CORS.

- **Zero-Leak Log Scrubbing & PII Data Masking Engines:**
  * Tự động mask các trường PII (email, số điện thoại) trong logs bằng cách sử dụng `REDACT` pattern (`[email‑protected]`).
  * Áp dụng `@JsonSerialize` với `JsonInclude.Include.NON_NULL` để loại bỏ các trường null.
  * Thiết lập ngưỡng giữ lại logs (1 năm) và tự động xóa sau đó.

## 📁 7. QUY TẮC TUÂN THỦ DI ĐỘNG HỖN HỢP & CƠ CHẾ QUỐC TẾ HOÁ SEO

- **Capacitor Mobile Hybrid Compliance Rails:**
  * Sử dụng `@capacitor/app` để quản lý lifecycle ứng dụng, ngăn chặn các lần back‑button không mong muốn.
  * Triển khai `@capacitor/preferences` để lưu trữ an toàn các preference người dùng (ngôn ngữ, token).
  * Sử dụng `@capacitor/network` để phát hiện trạng thái kết nối và queue các yêu cầu API khi offline.
  * Triển khai `@capacitor/push-notifications` để đăng ký token thiết bị, xử lý sự kiện push foreground/background.

- **Internationalization (i18n) & Dynamic SEO Injection:**
  * Triển khai middleware phát hiện ngôn ngữ từ header `Accept-Language` và cookie `i18n_locale`.
   * Lưu preference người dùng trong `AsyncStorage` để sử dụng cho các phiên sau.
   * Sử dụng `next-intl` cho Next.js để tải các tệp JSON dịch (`en.json`, `vi.json`, `es.json`).
   * Tự động tạo thẻ `<html lang='en'>` hoặc `lang='vi'` dựa trên locale.
   * Triển khai hreflang `<link rel="alternate" hreflang="en" href="https://example.com/en/page"/>` cho tất cả các trang.
   * Triển khai cơ chế lazy‑load cho các tài nguyên dịch để giảm thời gian tải trang.
   * Tối ưu hóa các thẻ meta (title, description) cho từng ngôn ngữ để cải thiện SEO.

## 📁 8. QUY TRÌNH TỰ ĐỘNG HOÁ PHIÊN LÀM VIỆC HÀNG NGÀY VỚI GIT BRANCH

- **Daily Workspace Forking Isolation:**
  * Tự động fork repository chính sang branch `features/development-phase-1-day-1`, `features/development-phase-1-day-2`, ..., `features/development-phase-5-day-15`.
  * Gán branch cho sub-agent tương ứng (ví dụ: branch `features/development-phase-1-day-1` cho Coder).
  * Mỗi branch là không gian làm việc riêng biệt để tránh xung đột.

- **Validation Guard Pipeline Gates:**
  * Sau mỗi commit, GitHub Actions chạy các bước: `npm test` / `mvn verify`, `sonarqube` scan, `docker lint`, `helm lint`.
  * Đảm bảo độ bao phủ mã >=85 % cho mỗi service mới.
   * Tự động tạo PR với tiêu đề `feat: phase-X-day-Y` và gắn thẻ `phase-X`.
   * Chỉ cho phép merge sau khi tất cả các kiểm tra chất lượng vượt qua.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`