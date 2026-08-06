# BẢN ĐỒ DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Tài liệu Kiểm soát

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260806090527 |
| **Tên Dự án** | membership-hub |
| **Phiên bản** | 1.0 (Bản Baseline) |
| **Ngày.Giờ** | 2026/08/06 09:05:27 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CỐT LÕI

### 1.1. Tính chất Hệ thống Cốt lõi & Kiến trúc Điều khiển
- Kiến trúc đa tenant dựa trên cơ sở dữ liệu PostgreSQL với mô hình phân chia schema theo trung tâm để cô lập dữ liệu.
- Triển khai theo kiểu microservices sử dụng Java/Quarkus cho các dịch vụ lõi, container hóa bằng Docker và điều phối trên Google Kubernetes Engine (GKE).
- Áp dụng mẫu Command Query Responsibility Segregation (CQRS) cho các hoạt động ghi (điểm danh, ghi danh) và truy vấn (báo cáo, thẻ hội viên) để tối ưu hiệu suất.
- Triển khai kiến trúc event-driven với Apache Kafka làm backbone truyền tải các sự kiện điểm danh, ghi danh và thông báo theo thời gian thực.
- Sử dụng Reactive programming trong các dịch vụ xử lý điểm danh QR để đảm bảo khả năng mở rộng và phản hồi nhanh.
- Tách biệt lớp ứng dụng (service) và lớp cơ sở dữ liệu bằng Flyway/Liquibase cho các migration schema.
- Tích hợp Firebase Authentication và Google Cloud Messaging (FCM) để bảo mật ở lớp xác thực và gửi thông báo đẩy.
- Triển khai kiểm soát truy cập dựa trên vai trò (RBAC) với các bảng Roles và Users, có phân quyền theo từng trung tâm.
- Triển khai logging tập trung và audit trail cho tất cả các thao tác thay đổi dữ liệu để phục vụ tuân thủ GDPR/CCPA.
- Thiết kế API theo kiểu REST cho Next.js frontend, tích hợp OAuth2 và JWT với thời gian sống 15 phút để đảm bảo bảo mật ở lớp mạng.

### 1.2. Dòng Chảy Dữ Liệu Doanh nghiệp & Hệ sinh thái Cốt lõi
- Sử dụng Apache Kafka với các chủ đề chuyên biệt: `qr-attendance`, `enrollment`, `notification`, `center-event` để đảm bảo xử lý bất đồng bộ và khả năng mở rộng.
- Triển khai Kafka Connect để đồng bộ hóa dữ liệu điểm danh từ bảng Attendance sang hệ thống phân tích trên Google BigQuery.
- Tích hợp Firebase Cloud Messaging (FCM) và Apple APNs cho các thông báo đẩy đến ứng dụng di động trên cả Android và iOS.
- Triển khai cổng tích hợp Zalo API để gửi tin nhắn văn bản đến các nhóm Zalo được chỉ định cho các sự kiện thông báo, ghi danh và điểm danh.
- Triển khai cổng OAuth2 với Firebase, Google, Facebook để xác thực người dùng và phát hành JWT tokens, đồng thời lưu trữ các sự kiện xác thực trên chủ đề `auth-events`.
- Triển khai cơ chế dead-letter queue (DLQ) cho các sự kiện thất bại, với chính sách tái thử tối đa 3 lần trước khi chuyển sang hàng đợi lỗi.
- Triển khai cơ chế fan-out cho các sự kiện thông báo để đồng thời cập nhật bảng Notifications, gửi push notification và ghi log vào hệ thống audit.
- Sử dụng Redis để cache phiên làm việc người dùng và token xác thực, giảm thời gian trễ cho các yêu cầu xác thực.
- Triển khai cơ chế backpressure và xử lý luồng phản hồi theo kiểu Reactive để đảm bảo độ trễ dưới 200 ms cho các API cốt lõi.
- Triển khai giám sát chủ đề Kafka theo thời gian thực thông qua Prometheus và Grafana để theo dõi sức khỏe hệ thống.

## 📁 2. STACK PHỤ THUỘC & HỆ SINH THÁI LIBRARIES

- **Backend Infrastructure Core Stack:** Java 21 + Quarkus 3.8.x, PostgreSQL 15, Flyway, Apache Kafka 3.5, Redis 7, Docker, Google Cloud Platform (GCP), Google Kubernetes Engine (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API SDK, JUnit 5, Mockito, Lombok, MapStruct, SmallRye OpenAPI, OpenTelemetry, Apache Commons, Spring Security, java-jwt, bcrypt.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js 14 (React 18), TypeScript, Tailwind CSS, i18next, React Query, Redux Toolkit, Capacitor, React Native, Firebase SDK, Material-UI, ESLint/Prettier, Jest, React Testing Library.

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. QUY TẮC BẢO VỆ TOÀN CẦU & TIÊU CHUẨN DOANH NGHIỆP

- Tuân thủ nghiêm ngặt quy tắc biên giới kho lưu trữ: gốc thực sự của kho lưu trữ là cố định tại `.`; tất cả các đường dẫn được tạo ra PHẢI bắt đầu bằng `./sources/`.
- Thực thi quy tắc tiền tố thư mục động phù hợp với quy định trong Protocol 1, khớp với cấu trúc hệ thống được phát hiện.
- [CONDITION: JAVA_STACK_ONLY] Tiêu chuẩn gói Java: Nếu sử dụng khung Java, tất cả mã nguồn Java PHẢI nằm trong gói cơ sở doanh nghiệp `org.nlh4j.saas.membershiphub`. Chuyển đổi "membership-hub" thành chuỗi thuần alphanumeric không có dấu gạch ngang hoặc dấu gạch dưới.
- Cấu trúc nghiêm ngặt cho mục tiêu kiểm thử: Bất kỳ thành phần nào được nhắm mục tiêu bởi tác nhân Tester PHẢI được cấu trúc dưới dạng cặp phân cách bán phẩy `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn trong cặp PHẢI bắt đầu bằng `./sources/`.

## 4. BẢNG TÓM TẮT KIẾN TRÚC HÀNG ĐẦU ĐA PHA

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module Kiến trúc | Tóm tắt Sản phẩm Bàn giao | Sub-Agent được chỉ định | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1-3 | ./sources/backend.user; ./sources/docs/; ./sources/infra/ | Triển khai dịch vụ quản lý người dùng cốt lõi, xác thực, phân quyền RBAC, schema DB, JWT, OAuth2, đăng ký người dùng | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004] |
| Phase 2 | Day 1-2 | ./sources/backend.center; ./sources/docs/; ./sources/infra/ | Triển khai CRUD trung tâm, phân quyền quản trị trung tâm, quản lý khóa học, phân công giáo viên, schema DB cho Trung tâm và Khóa học | Coder | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004], [ARC-010] |
| Phase 3 | Day 1-3 | ./sources/backend.enrollment; ./sources/docs/; ./sources/infra/ | Triển khai ghi danh khóa học, quét điểm danh QR, quản lý thẻ hội viên, schema DB cho Ghi danh, Điểm danh, Thẻ hội viên | Coder | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [EXC-001], [EXC-002] |
| Phase 4 | Day 1-3 | ./sources/backend.notification; ./sources/docs/; ./sources/infra/ | Triển khai engine thông báo, push đến mobile & Zalo, quản lý khuyến mãi & thông báo, schema DB cho Thông báo, Khuyến mãi, Thông báo | Coder | [REQ-016], [REQ-017], [REQ-018], [EXC-003], [DAT-008], [DAT-009] |
| Phase 5 | Day 1-2 | ./sources/backend.localization; ./sources/docs/; ./sources/infra/ | Triển khai bản địa hóa & SEO, báo cáo & phân tích, bảo mật & tuân thủ, schema DB cho Cài đặt hệ thống, audit log, chiến lược backup | Coder | [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [DAT-011] |

## 5. CÁC CHUYÊN ĐỀ GIAI ĐOẠN CHI TIẾT & NGÀY THEO DÕI GIAO HÀNG

<!--START_DELIMITTER-->
### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai nền tảng cốt lõi cho hệ thống quản lý hội viên, bao gồm đăng ký người dùng, xác thực đa nhà cung cấp, phân quyền RBAC và khởi tạo schema cơ sở dữ liệu ban đầu. Mục tiêu là thiết lập các thành phần cơ bản đảm bảo bảo mật, khả năng mở rộng và tuân thủ cho toàn bộ hệ thống đa trung tâm.
- **Target Physical Directory Matrix Map:** 
    *   `./sources/backend.user` (Core user service implementation) [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001]
    *   `./sources/docs/user_management_blueprint.md` (Enterprise specification) [REQ-001], [REQ-002], [REQ-003], [DAT-001]
    *   `./sources/infra/dockerfile_user_service` (Container definition) [ARC-010]
- **Database Schema DDL SQL Specification [DAT-001]:**
```sql
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
    provider ENUM('local', 'firebase', 'google', 'facebook') NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```
- **API and Event Routing Contracts [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
  * **POST /api/v1/auth/register** – Yêu cầu: `{email, password, fullName, roleId}`. Phản hồi: `201 Created` với `{userId, email, roleId, token}`.
  * **POST /api/v1/auth/social** – Yêu cầu: `{provider, code, redirectUri}`. Phản hồi: `200 OK` với `{userId, token}`.
  * **PUT /api/v1/users/{userId}/role** – Yêu cầu: `{roleId}` (chỉ System Admin). Phản hồi: `200 OK` với `{userId, roleId}`.
  * **WebSocket /topic/auth-events** – Gửi sự kiện xác thực OAuth2 để ghi log và thông báo.
- **Phase Localized Exception Handlers [EXC-004]:**
  - Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

<!--END_DELIMITTER-->

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)
- **DAY 1: Triển khai dịch vụ đăng ký người dùng và xác thực cơ bản**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.user` [REQ-001], [DAT-001]
      - **Low-Level Technical Task Instruction:** Triển khai lớp `UserService` với phương thức `registerUser(RegisterRequest)` thực hiện xác thực đầu vào, mã hóa mật khẩu bằng bcrypt, lưu bản ghi người dùng vào bảng `users`, gán vai trò `Student` mặc định, tạo JWT token có thời hạn 15 phút, trả về `UserResponse`. Đảm bảo tuân thủ quy tắc đặt tên gói `org.nlh4j.saas.membershiphub.user`. [REQ-001], [DAT-001]
      - **Targeted Tag IDs:** [REQ-001], [DAT-001]

- **DAY 2: Triển khai xác thực qua mạng xã hội**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.user` [REQ-002], [ARC-006]
      - **Low-Level Technical Task Instruction:** Triển khai phương thức `socialAuthenticate(SocialAuthRequest)` trong `AuthService` để trao đổi mã OAuth2 với Firebase/Google/Facebook, gọi API nhà cung cấp để lấy thông tin người dùng, tìm kiếm hoặc tạo bản ghi người dùng tương ứng, tạo JWT token, trả về `AuthResponse`. Tích hợp với `WebSocket`/topic `auth-events` để ghi log sự kiện. [REQ-002], [ARC-006]
      - **Targeted Tag IDs:** [REQ-002], [ARC-006]

- **DAY 3: Đánh giá chất lượng mã và xem xét bảo mật**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Reviewer]:**
      - **Target Component file path (`target_component`):** `./sources/backend.user` [REQ-001], [REQ-002], [EXC-004]
      - **Low-Level Technical Task Instruction:** Thực hiện đánh giá mã nguồn cho `UserService` và `AuthService`, kiểm tra các lỗ hổng bảo mật (SQL injection, XSS, xác thực JWT), đảm bảo tuân thủ OWASP Top 10, viết ghi chú đánh giá, đề xuất các biện pháp khắc phục. Xử lý các lỗi xác thực đầu vào theo quy định trong [EXC-004]. [EXC-004]
      - **Targeted Tag IDs:** [REQ-001], [REQ-002], [EXC-004]

<!--START_DELIMITTER-->
### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai các chức năng quản lý trung tâm và khóa học, bao gồm CRUD cho trung tâm, phân quyền quản trị, quản lý khóa học, phân công giáo viên và thiết lập schema cơ sở dữ liệu cho các thực thể mới. Mục tiêu là mở rộng nền tảng để hỗ trợ nhiều trung tâm với khả năng cô lập dữ liệu.
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend.center` (Center service implementation) [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    *   `./sources/backend.course` (Course service implementation) [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    *   `./sources/docs/center_course_blueprint.md` (Enterprise specification) [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004]
    *   `./sources/infra/dockerfile_center_course` (Container definition) [ARC-010]
- **Database Schema DDL SQL Specification [DAT-003]:**
```sql
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) NOT NULL UNIQUE,
    contact_phone VARCHAR(30),
    contact_email VARCHAR(255)
);
```
- **Database Schema DDL SQL Specification [DAT-004]:**
```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL REFERENCES users(user_id),
    max_students INT NOT NULL DEFAULT 30
);
```
- **API and Event Routing Contracts [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-010]:**
  * **GET /api/v1/centers** – Trả về danh sách trung tâm (`[{centerId, name, address, taxId, contactPhone, contactEmail}]`).
  * **POST /api/v1/centers** – Tạo trung tâm mới, kiểm tra tính duy nhất của taxId, trả về `201 Created`.
  * **PUT /api/v1/centers/{centerId}** – Cập nhật thông tin trung tâm.
  * **DELETE /api/v1/centers/{centerId}** – Xóa trung tâm.
  * **POST /api/v1/centers/{centerId}/admin/assign** – Gán người dùng làm Center Admin.
  * **GET /api/v1/courses** – Trả về danh sách khóa học (`[{courseId, title, startDate, endDate, teacherName}]`).
  * **POST /api/v1/courses** – Tạo khóa học mới, kiểm tra xung đột lịch dạy của giáo viên.
  * **PUT /api/v1/courses/{courseId}/teacher** – Phân công giáo viên vào khóa học.
  * **WebSocket /topic/center-events** – Gửi sự kiện thay đổi trung tâm và khóa học.
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-003]:**
  - Mạng & Kết nối bị ngắt trong quá trình quét QR: Nếu sinh viên quét mã QR nhưng mạng không khả dụng, Khi ứng dụng thử lại yêu cầu sau khi kết nối lại, Sau đó điểm danh được ghi lại khi dịch vụ khả dụng.
  - Điểm danh trùng lặp: Nếu cùng một sinh viên quét cùng một mã QR nhiều lần trong cùng một ngày, Khi hệ thống phát hiện điểm danh trùng lặp, Sau đó trả về phản hồi thành công với cờ ‘đã ghi’ và không tạo thêm hàng.
  - Thông báo không thể gửi: Khi một thông báo đẩy không thể được gửi (ví dụ: token thiết bị không hợp lệ), Sau đó hệ thống ghi lại lỗi và lên lịch tái thử tối đa 3 lần trước khi đánh dấu là thất bại.

<!--END_DELIMITTER-->

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)
- **DAY 1: Triển khai dịch vụ quản lý trung tâm**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.center` [REQ-004], [REQ-005], [REQ-006], [DAT-003]
      - **Low-Level Technical Task Instruction:** Triển khai `CenterService` với các phương thức `listCenters`, `createCenter`, `updateCenter`, `deleteCenter`, `assignCenterAdmin`. Thực hiện xác thực đầu vào (taxId duy nhất, định dạng email), sử dụng `CenterRepository` để tương tác với bảng `centers`. Áp dụng kiểm soát truy cập dựa trên vai trò (System Admin). [REQ-004], [REQ-005], [REQ-006], [DAT-003]
      - **Targeted Tag IDs:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]

- **DAY 2: Triển khai dịch vụ quản lý khóa học và kiểm thử**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Tester]:**
      - **Target Component file path (`target_component`):** `./sources/backend.center;./sources/tests/center_test_suite.java` [REQ-007], [REQ-008], [REQ-009], [DAT-004]
      - **Low-Level Technical Task Instruction:** Viết bộ kiểm thử tích hợp cho `CourseService` sử dụng JUnit 5 và Mockito, mô phỏng xung đột lịch dạy của giáo viên, xác minh lỗi trả về khi trùng lịch, kiểm tra thành công khi tạo khóa học mới. Đảm bảo độ bao phủ mã >=85%. [REQ-007], [REQ-008], [REQ-009], [DAT-004]
      - **Targeted Tag IDs:** [REQ-007], [REQ-008], [REQ-009], [DAT-004]

<!--START_DELIMITTER-->
### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai các chức năng ghi danh học viên, điểm danh QR, và quản lý thẻ hội viên. Mục tiêu là kết nối người học với khóa học, ghi lại sự tham gia thời gian thực và quản lý vòng đời thẻ hội viên với tính năng gia hạn.
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend.enrollment` (Enrollment service) [REQ-010], [REQ-011], [DAT-005]
    *   `./sources/backend.attendance` (Attendance service) [REQ-012], [REQ-013], [DAT-006]
    *   `./sources/backend.membership` (Membership service) [REQ-014], [REQ-015], [DAT-007]
    *   `./sources/docs/enrollment_attendance_membership_blueprint.md` (Enterprise specification) [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-005], [DAT-006], [DAT-007]
    *   `./sources/infra/dockerfile_enrollment_attendance_membership` (Container definition) [ARC-010]
- **Database Schema DDL SQL Specification [DAT-005]:**
```sql
CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (student_id, course_id)
);
```
- **Database Schema DDL SQL Specification [DAT-006]:**
```sql
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    course_id UUID NOT NULL REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW()
);
```
- **Database Schema DDL SQL Specification [DAT-007]:**
```sql
CREATE TABLE studentcards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL
);
```
- **API and Event Routing Contracts [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007], [ARC-008]:**
  * **GET /api/v1/courses/available** – Trả về danh sách khóa học mà sinh viên chưa ghi danh.
  * **POST /api/v1/enrollments** – Ghi danh sinh viên vào khóa học, tự động tạo tài khoản sinh viên nếu thiếu, trả về `201 Created` với `enrollmentId`.
  * **POST /api/v1/attendance/scan** – Nhận payload `{studentId, courseId, timestamp}`, ghi lại điểm danh, đảm bảo idempotent cho cùng ngày.
  * **GET /api/v1/membership/{studentId}/card** – Trả về thông tin thẻ hội viên (`validityDays`, `remainingDays`).
  * **POST /api/v1/membership/{studentId}/renew** – Gia hạn thẻ hội viên theo số ngày được chọn, cập nhật `endDate` (thông qua `remainingDays`), xử lý thanh toán.
  * **WebSocket /topic/enrollment-events** – Gửi sự kiện ghi danh để thông báo đẩy và cập nhật Zalo group.
  * **WebSocket /topic/attendance-events** – Gửi sự kiện điểm danh để cập nhật thời gian thực.
- **Phase Localized Exception Handlers [EXC-001], [EXC-002], [EXC-005]:**
  - Mạng & Kết nối bị ngắt trong quá trình quét QR: Nếu sinh viên quét mã QR nhưng mạng không khả dụng, Khi ứng dụng thử lại yêu cầu sau khi kết nối lại, Sau đó điểm danh được ghi lại khi dịch vụ khả dụng.
  - Điểm danh trùng lặp: Nếu cùng một sinh viên quét cùng một mã QR nhiều lần trong cùng một ngày, Khi hệ thống phát hiện điểm danh trùng lặp, Sau đó trả về phản hồi thành công với cờ ‘đã ghi’ và không tạo thêm hàng.
  - System Recovery After Outage: Nếu dịch vụ trở nên không khả dụng, Khi nó khôi phục, Sau đó bất kỳ quét điểm danh đang chờ xử lý nào được xử lý theo thứ tự FIFO, và người dùng nhận được thông báo về các sự kiện đã phục hồi.

<!--END_DELIMITTER-->

#### 📅 Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)
- **DAY 1: Triển khai dịch vụ ghi danh và DDL**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Coder]:**
      - **Target Component file path (`target_component`):** `./sources/backend.enrollment` [REQ-010], [REQ-011], [DAT-005]
      - **Low-Level Technical Task Instruction:** Triển khai `EnrollmentService` với phương thức `enrollStudent(studentId, courseId)` thực hiện xác thực mối quan hệ sinh viên-khóa học, chèn bản ghi vào bảng `enrollments`, đảm bảo tính duy nhất, gửi sự kiện ghi danh qua WebSocket `/topic/enrollment-events`. Sử dụng `EnrollmentRepository` để tương tác với cơ sở dữ liệu. [REQ-010], [REQ-011], [DAT-005]
      - **Targeted Tag IDs:** [REQ-010], [REQ-011], [DAT-005]

- **DAY 2: Triển khai dịch vụ điểm danh QR và container hóa**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: Docker]:**
      - **Target Component file path (`target_component`):** `./sources/infra/dockerfile_attendance` [REQ-012], [REQ-013], [DAT-006]
      - **Low-Level Technical Task Instruction:** Tạo Dockerfile đa giai đoạn cho dịch vụ điểm danh (`attendance-service`), chỉ định base image `eclipse-temurin:21-jdk`, sao chép tệp JAR đã biên dịch, thiết lập người dùng không có đặc quyền, phơi bày cổng 8080, tạo điểm vào `/app/entrypoint.sh` để khởi động dịch vụ với `java -jar`. Đảm bảo kích thước ảnh cuối cùng < 500 MB. [REQ-012], [REQ-013], [DAT-006]
      - **Targeted Tag IDs:** [REQ-012], [REQ-013], [DAT-006]

- **DAY 3: Triển khai dịch vụ quản lý thẻ hội viên và cung cấp trên GCP**
  - **Sub-Agent Workflow Specialization:**
    * **[Assigned Sub-Agent literal token: GCP]:**
      - **Target Component file path (`target_component`):** `./sources/infra/gcp_membership_config.yaml` [REQ-014], [REQ-015], [DAT-007]
      - **Low-Level Technical Task Instruction:** Tạo tệp YAML cho Google Cloud Build để biên dịch và triển khai dịch vụ thẻ hội viên lên Cloud Run, thiết lập IAM cho vai trò `membership-service`, cấu hình Cloud SQL cho PostgreSQL, thiết lập Secret Manager cho credential, bật Cloud Monitoring và Cloud Logging. [REQ-014], [REQ-015], [DAT-007]
      - **Targeted Tag IDs:** [REQ-014], [REQ-015], [DAT-007]

<!--START_DELIMITTER-->
### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Phase Core Objective & Purpose:** Triển khai engine thông báo toàn diện, quản lý khuyến mãi & thông báo, tích hợp push notification đến ứng dụng di động và Zalo group, đồng thời triển khai chatbot dịch vụ khách hàng AI để hỗ trợ người dùng.
- **Target Physical Directory Matrix Map:**
    *   `./sources/backend.notification` (Notification service) [REQ-016], [EXC-003], [DAT-008]
    *   `./sources/backend.promotion` (Promotion service) [REQ-017], [DAT-009]
    *   `./sources/backend.announcement` (Announcement service) [REQ-018], [DAT-009]
    *   `./sources/docs/notification_promotion_announcement_blueprint.md` (Enterprise specification) [REQ-016], [REQ-017], [REQ-018], [EXC-003], [DAT-008], [DAT-009]
    *   `./sources/infra/dockerfile_notification_promotion_announcement` (Container definition) [ARC-010]
- **Database Schema DDL SQL Specification [DAT-008]:**
```sql
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID,
    group_zalo VARCHAR(100),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```
- **Database Schema DDL SQL Specification [DAT-009] (Promotions & Announcements):**
```sql
CREATE TABLE promotions (
    promo_id UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discount_percent SMALLINT NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT
);

CREATE TABLE announcements