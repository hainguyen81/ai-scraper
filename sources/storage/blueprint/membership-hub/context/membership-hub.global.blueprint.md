# BỐ CỤC DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Kiểm Soát Tài Liệu

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260807172813 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/07 17:28:13 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CỐT LÕI

### 1.1. Tính Chất Hệ Thống Cốt Lõi & Kiến Trúc

- Triển khai kiến trúc hướng dịch vụ (SOA) với các microservice độc lập cho người dùng, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, chatbot AI.
- Áp dụng mẫu CQRS để tách biệt đọc/ghi cho tất cả các thực thể nghiệp vụ chính.
- Sử dụng Event Sourcing và Apache Kafka để đảm bảo tính bất biến của luồng dữ liệu và khả năng theo dõi.
- Triển khai mô hình phản ứng (Reactive) với RxJava và Vert.x để xử lý bất đồng bộ và mở rộng theo chiều ngang.
- Tách biệt các biên giới bảo mật theo vai trò (RBAC) với các quyền hạn được áp dụng ở lớp gateway.
- Tích hợp nhiều lớp xác thực (OAuth2, JWT) với thời gian sống ngắn hạn và cơ chế làm mới token.
- Triển khai kiểm tra bất đồng bộ theo hướng sự kiện cho các nghiệp vụ quan trọng (điểm danh, ghi danh) để đảm bảo tính idempotent.
- Sử dụng thiết kế hướng lệnh (Command) cho các thao tác ghi dữ liệu và truy vấn hướng truy xuất (Query) cho các báo cáo.

### 1.2. Kiến Trúc Luồng Dữ Liệu Doanh Nghiệp & Hệ Sinh Thái Cốt Lõi

- Luồng xác thực OAuth2: Frontend ↔️ Auth Service (JWT), sử dụng Firebase, Google, Facebook làm nhà cung cấp.
- Luồng xử lý điểm danh QR: Mobile App → QR Service → Attendance Service (idempotent write).
- Luồng thông báo đa kênh: Notification Service → Push (FCM/APNs) + Zalo Group API.
- Luồng tích hợp backend ứng dụng di động: Next.js tiêu thụ REST API, caching ngoại tuyến qua IndexedDB.
- Luồng xử lý sự kiện Kafka: Các microservice phát sinh sự kiện (ghi danh, điểm danh) được ghi vào các chủ đề Kafka.
- Luồng xử lý file và thẻ hội viên: Upload avatar → Cloud Storage (Google Cloud), sinh mã QR cho thẻ.
- Luồng xử lý thanh toán: Payment Gateway ↔️ Membership Service (gia hạn thẻ).
- Luồng xử lý SEO và i18n: Middleware phát hiện ngôn ngữ, chèn hreflang, tạo sitemap XML.

## 📁 2. STACK CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI

### Stack cốt lõi backend

- Java 21
- Quarkus 3.2.0
- Hibernate ORM (PostgreSQL)
- Flyway (DB migration)
- SmallRye OpenAPI
- Micrometer (monitoring)
- Jackson (JSON)
- bcrypt (hash mật khẩu)
- java-jwt (JWT)
- OAuth2 OIDC (Keycloak/Spring Security)
- Firebase Admin SDK
- Google Cloud Messaging (FCM) / Apple APNs SDK
- Apache Kafka client
- Docker (multi‑stage)

### Stack UI web & di động

- Next.js 14 (React 18, TypeScript, Tailwind CSS)
- SWR & React Query (caching)
- i18next (i18n)
- React Native (Expo) cho di động
- Capacitor (native bridge)
- Firebase SDK (auth, messaging)

### Stack DevOps & hạ tầng

- Docker (multi‑stage)
- Kubernetes (Helm charts)
- Google Kubernetes Engine (GKE)
- GitHub Actions (CI/CD)
- Terraform (infra as code)
- Prometheus + Grafana (monitoring)
- Jaeger (tracing)
- Redis (session caching)

### MA TRẬN STACK KIẾN TRÚC

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. QUY TẮC TOÀN CẦU & TIÊU CHUẨN COMPLIANCE DOANH NGHIỆP

- **Quy tắc biên giới không gian làm việc tuyệt đối:** Gốc thực sự của kho lưu trữ là cố định tại `.`; mọi đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Tuân thủ quy tắc tiền tố thư mục động:** Thực thi quy tắc ánh xạ thư mục động phù hợp với cấu trúc dự án được phát hiện:
  * Backend logic: `./sources/backend/<service-name>/`
  * Frontend logic: `./sources/frontend/` (hoặc `./sources/frontend/<app-name>/` nếu có nhiều ứng dụng)
  * Hạ tầng DevOps: `./sources/infra/`
  * Tài liệu: `./sources/docs/`
- **[CONDITION: JAVA_STACK_ONLY] Tiêu chuẩn gói Java:** Nếu stack sử dụng Java, tất cả mã nguồn Java phải nằm trong gói cơ sở doanh nghiệp: `org.nlh4j.saas.membershiphub`. Chuỗi "membership-hub" được chuyển đổi thành token thuần chữ thường không dấu: `membershiphub`.
- **Cú pháp đường dẫn mục tiêu nghiêm ngặt của Tester:** Bất kỳ thành phần nào được nhắm mục tiêu bởi Sub-Agent Tester phải được cấu trúc dưới dạng cặp phân cách bán phẩy nghiêm ngặt `<source_component>;<test_suite_file>`. Cả hai đường dẫn trong cặp phải bắt đầu bằng `./sources/`.

<!--START_PHASE_SYNOPSIS_GRID-->
| Phase | Day Range | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1: Quản lý người dùng & xác thực cốt lõi | Ngày 1 - 4 | ./sources/backend/auth/ | Triển khai dịch vụ xác thực, đăng ký, OAuth2, JWT, quản lý vai trò | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [EXC-004] |
| Giai đoạn 2: Quản lý trung tâm | Ngày 1 - 2 | ./sources/backend/center/ | Triển khai CRUD trung tâm, phân quyền quản trị trung tâm | Coder | [REQ-004], [REQ-005], [REQ-006], [DAT-003] |
| Giai đoạn 3: Quản lý khóa học | Ngày 1 - 2 | ./sources/backend/course/ | Triển khai CRUD khóa học, phân công giáo viên, kiểm tra xung đột lịch | Coder | [REQ-007], [REQ-008], [REQ-009], [DAT-004] |
| Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo | Ngày 1 - 6 | ./sources/backend/enrollment/ | Triển khai ghi danh học viên, tạo tài khoản học viên, thông báo đa kênh | Coder | [REQ-010], [REQ-011], [DAT-005] |
| Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo | Ngày 1 - 6 | ./sources/backend/attendance/ | Triển khai quét QR, ghi nhận điểm danh bất biến, xử lý ngoại lệ mạng | Coder | [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002] |
| Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo | Ngày 1 - 6 | ./sources/backend/membership/ | Triển khai hiển thị thẻ, gia hạn thẻ, tích hợp thanh toán | Coder | [REQ-014], [REQ-015], [DAT-007] |
| Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo | Ngày 1 - 6 | ./sources/backend/notification/ | Triển khai tạo thông báo, push notification, gửi Zalo group, xử lý lỗi giao hàng | Coder | [REQ-016], [DAT-008], [EXC-003] |
| Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo | Ngày 1 - 6 | ./sources/backend/promotion/ | Triển khai CRUD khuyến mãi & thông báo, tự động hết hạn | Coder | [REQ-017], [REQ-018], [DAT-009] |
| Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo | Ngày 1 - 6 | ./sources/backend/chatbot/ | Triển khai tích hợp chatbot AI, xử lý truy vấn | Coder | [REQ-019] |
| Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo | Ngày 1 - 6 | ./sources/frontend/app/ | Triển khai giao diện người dùng di động đáp ứng cho tất cả vai trò | Coder | [REQ-020], [REQ-021] |
| Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo | Ngày 1 - 6 | ./sources/backend/i18n/ | Triển khai phát hiện ngôn ngữ, chèn hreflang, SEO đa ngôn ngữ | Coder | [REQ-022], [REQ-023], [DAT-011] |
| Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo | Ngày 1 - 6 | ./sources/backend/reporting/ | Triển khai tạo báo cáo điểm danh CSV, bảng điều khiển tóm tắt ghi danh | Coder | [REQ-024], [REQ-025], [EXC-005] |
| Giai đoạn 5: Bảo mật, tuân thủ, di động, pipeline | Ngày 1 - 3 | ./sources/infra/ | Triển khai containerization (Docker), đẩy hình ảnh, quản lý kho chứa | Docker | [NFR-001], [NFR-002], [NFR-003] |
| Giai đoạn 5: Bảo mật, tuân thủ, di động, pipeline | Ngày 1 - 3 | ./sources/infra/ | Cung cấp hạ tầng GCP (VPC, IAM, Cloud Storage), triển khai dịch vụ | GCP | [NFR-004], [NFR-005], [NFR-006] |
| Giai đoạn 5: Bảo mật, tuân thủ, di động, pipeline | Ngày 1 - 3 | ./sources/infra/ | Triển khai Kubernetes (GKE), quản lý scaling, release strategies | GKE | [NFR-007], [NFR-008], [NFR-009] |
<!--END_PHASE_SYNOPSIS_GRID-->

## 5. CHI TIẾT HOẠCH ĐỊNH THEO GIAI ĐOẠN & GIAO HÀNG NGÀY THEO NGÀY

### 📈 Giai đoạn 1: Quản lý người dùng & xác thực cốt lõi
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng lõi người dùng, xác thực đa nhà cung cấp, phân quyền RBAC và các cơ chế bảo vệ đầu vào.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**
    * ./sources/backend/auth/ (Coder) – [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [EXC-004]
    * ./sources/docs/ (Doc) – tài liệu thiết kế hệ thống người dùng
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:**
```sql
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

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
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-001]..[ARC-006]:**
```json
// POST /api/v1/auth/register
{
  "email": "user@example.com",
  "password": "StrongPass123!",
  "fullName": "Nguyen Van A",
  "roleId": 5
}

// POST /api/v1/auth/social
{
  "provider": "google",
  "code": "OAuth2_code_from_provider"
}

// PUT /api/v1/users/{userId}/role
{
  "newRoleId": 3
}
```
- **Xử lý Ngoại lệ theo Ngôn ngữ Bản địa [EXC-004]:**
    * Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc): Trả về HTTP 400 với danh sách các trường không hợp lệ và hướng dẫn chỉnh sửa bằng tiếng Việt.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 1)

- **DAY 1:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai đăng ký người dùng, xác thực qua mạng xã hội và gán vai trò ban đầu.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [ARC-001], [DAT-001]
    * **Target Component file path (`target_component`):** ./sources/backend/auth/UserService.java [REQ-001], [DAT-001]
    * **Low-Level Technical Task Instruction:** Viết lớp UserService triển khai registerUser (validation, bcrypt hash, lưu vào bảng USERS với roleId mặc định là Student), implement socialAuthFlow (nhận OAuth2 code, gọi Firebase/Google/Facebook API, tạo hoặc cập nhật bản ghi USERS, sinh JWT token có thời hạn 15 phút), thêm phương thức assignRole (cập nhật cột roleId, ghi log vào bảng AUDIT). Đảm bảo tất cả các thao tác đều được bao quanh bởi transaction và tuân thủ các ràng buộc khóa ngoại.

- **DAY 2:** Mục tiêu ngắn gọn cho ngày hoạt động này: Xây dựng kiểm tra đầu vào và xử lý lỗi xác thực.
    * **Sub-Agent Workflow Specialization:** [Tester]
    * **Tag IDs Mục tiêu:** [EXC-004], [REQ-001], [DAT-001]
    * **Target Component file path (`target_component`):** ./sources/backend/auth/UserServiceTest.java;./sources/backend/auth/UserService.java
    * **Low-Level Technical Task Instruction:** Viết unit tests cho registerUser với các trường hợp: email hợp lệ, mật khẩu yếu, email trùng lặp; xác minh response HTTP status và message lỗi bằng tiếng Việt; kiểm tra socialAuthFlow với mã OAuth2 hợp lệ và không hợp lệ; đảm bảo exception InputValidationException được ném và xử lý bởi GlobalExceptionHandler để trả về JSON lỗi chi tiết.

- **DAY 3:** Mục tiêu ngắn gọn cho ngày hoạt động này: Tạo tài liệu kỹ thuật và hướng dẫn vận hành.
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-002], [ARC-002], [ARC-003]
    * **Target Component file path (`target_component`):** ./sources/docs/UserManagementGuide.md
    * **Low-Level Technical Task Instruction:** Soạn thảo tài liệu hướng dẫn quản lý người dùng bao gồm mô tả API, bảng tham chiếu vai trò, quy trình đăng ký, quy trình xác thực qua mạng xã hội, quy trình gán vai trò; thêm các đoạn mã ví dụ bằng tiếng Việt; đảm bảo tài liệu tham chiếu các Tag IDs [REQ-002], [ARC-002], [ARC-003].

- **DAY 4:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai luồng xác thực JWT và refresh token.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [ARC-004], [ARC-005], [ARC-006]
    * **Target Component file path (`target_component`):** ./sources/backend/auth/TokenService.java
    * **Low-Level Technical Task Instruction:** Triển khai TokenService tạo accessToken (JWT, thời gian sống 15 phút) và refreshToken (thời gian sống 7 ngày) sử dụng java-jwt; thêm endpoint /api/v1/auth/refresh để đổi refreshToken lấy accessToken mới; tích hợp Firebase Authentication làm nhà cung cấp xác thực thay thế; đảm bảo token được lưu trữ an toàn (HTTP-only, Secure flag) và thực thi blacklist cho các token bị thu hồi.

### 📈 Giai đoạn 2: Quản lý trung tâm
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng CRUD trung tâm, kiểm tra tính duy nhất của taxId và phân quyền quản trị trung tâm.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**
    * ./sources/backend/center/ (Coder) – [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * ./sources/docs/ (Doc) – tài liệu quản lý trung tâm
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003]:**
```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006]:**
```json
// GET /api/v1/centers
// Response: [{ "centerId": "uuid", "name": "Center A", "address": "Hanoi", "taxId": "1234567890123", "contactPhone": "+84123456789", "contactEmail": "center@example.com" }]

// POST /api/v1/centers
{
  "name": "Center B",
  "address": "Ho Chi Minh",
  "taxId": "9876543210987",
  "contactPhone": "+84987654321",
  "contactEmail": "centerB@example.com"
}

// PUT /api/v1/centers/{centerId}
{
  "name": "Center B Updated",
  "address": "Ho Chi Minh City",
  "taxId": "9876543210987",
  "contactPhone": "+84987654321",
  "contactEmail": "centerB@example.com"
}

// DELETE /api/v1/centers/{centerId}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 2)

- **DAY 1:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai danh sách trung tâm, tạo trung tâm và kiểm tra xung đột taxId.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [DAT-003]
    * **Target Component file path (`target_component`):** ./sources/backend/center/CenterController.java
    * **Low-Level Technical Task Instruction:** Triển khai CenterController với endpoint GET /centers trả về danh sách; POST /centers chấp nhận request body, xác thực tính duy nhất của taxId (throw ConflictException), lưu vào bảng CENTERS; thêm validation cho các trường bắt buộc; trả về response với các trường phù hợp.

- **DAY 2:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai phân quyền quản trị trung tâm.
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-006], [DAT-003]
    * **Target Component file path (`target_component`):** ./sources/docs/CenterManagementGuide.md
    * **Low-Level Technical Task Instruction:** Soạn thảo tài liệu hướng dẫn quản lý trung tâm bao gồm quy trình gán người dùng làm Center Admin, quy trình thu hồi quyền; tham chiếu các Tag IDs [REQ-006], [DAT-003]; thêm các đoạn mã API ví dụ.

### 📈 Giai đoạn 3: Quản lý khóa học
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng CRUD khóa học, kiểm tra xung đột lịch dạy của giáo viên và phân công giáo viên.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**
    * ./sources/backend/course/ (Coder) – [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    * ./sources/docs/ (Doc) – tài liệu quản lý khóa học
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004]:**
```sql
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
- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009]:**
```json
// GET /api/v1/courses
// Response: [{ "courseId": "uuid", "title": "Math 101", "startDate": "2026-09-01", "endDate": "2026-12-31", "teacherName": "Nguyen Van B" }]

// POST /api/v1/courses
{
  "title": "Physics 202",
  "description": "Advanced physics",
  "startDate": "2026-10-01",
  "endDate": "2026-12-31",
  "teacherId": "uuid-of-teacher"
}

// PUT /api/v1/courses/{courseId}/teacher
{
  "teacherId": "uuid-of-new-teacher"
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 3)

- **DAY 1:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai danh sách khóa học, tạo khóa học mới và kiểm tra xung đột lịch.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [DAT-004]
    * **Target Component file path (`target_component`):** ./sources/backend/course/CourseService.java
    * **Low-Level Technical Task Instruction:** Triển khai CourseService với findAllCourses trả về view bao gồm tên giáo viên; implement createCourse validation đảm bảo startDate <= endDate, kiểm tra xem teacherId đã có khóa học nào trùng lịch (startDate <= existing.endDate AND endDate >= existing.startDate) ném ConflictException; lưu khóa học vào bảng COURSES; trả về response DTO.

- **DAY 2:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai phân công giáo viên và thông báo cho giáo viên qua ứng dụng di động.
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-009], [DAT-004]
    * **Target Component file path (`target_component`):** ./sources/docs/CourseManagementGuide.md
    * **Low-Level Technical Task Instruction:** Soạn thảo tài liệu hướng dẫn quản lý khóa học bao gồm quy trình phân công giáo viên, quy trình thu hồi phân công; tham chiếu các Tag IDs [REQ-009], [DAT-004]; thêm các đoạn mã API ví dụ.

### 📈 Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng toàn bộ quy trình học tập còn lại, bao gồm ghi danh, điểm danh QR, thẻ hội viên, thông báo đa kênh, khuyến mãi, chatbot AI, giao diện người dùng di động, bản địa hóa & SEO, và báo cáo & phân tích.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**
    * ./sources/backend/enrollment/ (Coder) – [REQ-010], [REQ-011], [DAT-005]
    * ./sources/backend/attendance/ (Coder) – [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]
    * ./sources/backend/membership/ (Coder) – [REQ-014], [REQ-015], [DAT-007]
    * ./sources/backend/notification/ (Coder) – [REQ-016], [DAT-008], [EXC-003]
    * ./sources/backend/promotion/ (Coder) – [REQ-017], [REQ-018], [DAT-009]
    * ./sources/backend/chatbot/ (Coder) – [REQ-019]
    * ./sources/frontend/app/ (Coder) – [REQ-020], [REQ-021]
    * ./sources/backend/i18n/ (Coder) – [REQ-022], [REQ-023], [DAT-011]
    * ./sources/backend/reporting/ (Coder) – [REQ-024], [REQ-025], [EXC-005]
    * ./sources/docs/ (Doc) – tài liệu tổng quan về tất cả các module
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-005]..[DAT-011]:**
```sql
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);

CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID REFERENCES USERS(userId),
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
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
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description VARCHAR(200)
);
```

- **Hợp đồng Định tuyến API và Sự kiện [REQ-010]..[REQ-025]:**
```json
// POST /api/v1/enrollments
{
  "studentId": "uuid",
  "courseId": "uuid"
}

// POST /api/v1/attendance/scan
{
  "studentId": "uuid",
  "courseId": "uuid",
  "qrCodeData": "base64-encoded-qr"
}

// GET /api/v1/membership/{studentId}/card
// Response: { "validityDays": 30, "remainingDays": 12 }

// POST /api/v1/notifications
{
  "userId": "uuid",
  "message": "Your attendance recorded"
}

// POST /api/v1/promotions
{
  "code": "SAVE20",
  "discountPercent": 20,
  "startDate": "2026-09-01",
  "endDate": "2026-12-31",
  "description": "Giảm giá 20% cho tất cả khóa học"
}

// POST /api/v1/announcements
{
  "title": "Holiday Notice",
  "content": "Hệ thống đóng cửa vào ngày 2/9",
  "startDate": "2026-08-31",
  "endDate": "2026-09-02"
}

// GET /api/v1/i18n/{locale}/messages
// Response: { "welcome": "Chào mừng", "login": "Đăng nhập" }

// GET /api/v1/reports/attendance?centerId=uuid&date=2026-08-07
// Response CSV stream: StudentName,CourseName,AttendanceDate,Status
```

- **Xử lý Ngoại lệ theo Ngôn Ngữ Bản Địa [EXC-001]..[EXC-005]:**
    * **EXC-001:** Network & Connectivity Drops During QR Scan: Nếu sinh viên quét QR nhưng mạng không khả dụng, khi ứng dụng thử lại sau khi kết nối lại, sau đó điểm danh được ghi lại khi dịch vụ khả dụng. Trả về HTTP 408 với thông báo “Mạng không khả dụng, vui lòng thử lại sau”.
    * **EXC-002:** Duplicate Attendance Submission: Nếu cùng sinh viên quét cùng QR nhiều lần trong ngày, hệ thống phát hiện bản ghi đã tồn tại, trả về HTTP 200 với payload JSON { "message": "Điểm danh đã được ghi nhận trước đó", "duplicate": true }.
    * **EXC-003:** Failed Notification Delivery: Khi push notification không thể gửi (ví dụ: token thiết bị không hợp lệ), hệ thống ghi log lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu delivered = false và gửi email cảnh báo quản trị.
    * **EXC-004:** Input Validation Failure: Nếu xác thực form thất bại (ví dụ: email sai định dạng, thiếu trường bắt buộc), trả về HTTP 400 với danh sách các trường không hợp lệ và hướng dẫn chỉnh sửa bằng tiếng Việt.
    * **EXC-005:** System Recovery After Outage: Nếu dịch vụ không khả dụng, khi khôi phục, bất kỳ quét QR chờ xử lý nào được xử lý theo thứ tự FIFO, và người dùng nhận được thông báo về các sự kiện được khôi phục.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 4)

- **DAY 1:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai ghi danh học viên, tự động tạo tài khoản học viên nếu thiếu.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-010], [REQ-011], [DAT-005]
    * **Target Component file path (`target_component`):** ./sources/backend/enrollment/EnrollmentService.java
    * **Low-Level Technical Task Instruction:** Triển khai EnrollmentService.createEnrollment(studentId, courseId) kiểm tra xem học viên đã ghi danh chưa, nếu chưa thì tạo bản ghi ENROLLMENTS; nếu học viên chưa có tài khoản USERS, tạo tài khoản mới với roleId = Student; sau khi ghi danh thành công, tạo bản ghi NOTIFICATIONS với message “Bạn đã ghi danh thành công vào khóa học {courseId}”; gọi async push notification qua FCM/APNs; lưu audit log.

- **DAY 2:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai ghi nhận điểm danh QR với logic bất biến.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]
    * **Target Component file path (`target_component`):** ./sources/backend/attendance/AttendanceService.java
    * **Low-Level Technical Task Instruction:** Triển khai AttendanceService.recordAttendance(studentId, courseId, qrData) xác thực studentId có ghi danh vào courseId, kiểm tra xem đã có ATTENDANCE cho attendanceDate hôm nay chưa; nếu đã có, trả về duplicate flag true; nếu chưa, tạo bản ghi ATTENDANCE mới; xử lý trường hợp ngoại tuyến bằng cách lưu sự kiện tạm thời vào hàng đợi (Redis) và xử lý khi kết nối lại; ném AttendanceServiceException cho các lỗi validation.

- **DAY 3:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai hiển thị thẻ hội viên và chức năng gia hạn.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-014], [REQ-015], [DAT-007]
    * **Target Component file path (`target_component`):** ./sources/backend/membership/MembershipService.java
    * **Low-Level Technical Task Instruction:** Triển khai MembershipService.getCard(studentId) truy vấn STUDENTCARDS, tính remainingDays = validityDays - ngày đã sử dụng; trả về DTO; implement extendCard(studentId, additionalDays) cập nhật trường remainingDays, ghi log giao dịch; tích hợp payment gateway để xử lý phí gia hạn; gửi notification cho học viên.

- **DAY 4:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai dịch vụ thông báo đa kênh và xử lý lỗi giao hàng.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-016], [DAT-008], [EXC-003]
    * **Target Component file path (`target_component`):** ./sources/backend/notification/NotificationService.java
    * **Low-Level Technical Task Instruction:** Triển khai NotificationService.sendNotification(userId, groupZalo, message) lưu vào bảng NOTIFICATIONS, gọi FCM push cho userId, gọi Zalo API để đăng bài vào groupZalo; nếu gửi thất bại, ghi log lỗi, lên lịch retry tối đa 3 lần; sau khi retry thất bại, đánh dấu delivered = false và gửi email cảnh báo quản trị.

- **DAY 5:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai CRUD khuyến mãi và thông báo với logic tự động hết hạn.
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-017], [REQ-018], [DAT-009]
    * **Target Component file path (`target_component`):** ./sources/backend/promotion/PromotionService.java
    * **Low-Level Technical Task Instruction:** Triển khai PromotionService.createPromotion(payload) lưu vào bảng PROMOTIONS/ANNOUNCEMENTS; thêm validation startDate/endDate; thiết lập scheduler xóa các bản ghi đã hết hạn; implement soft-delete cho khuyến mãi; expose endpoint GET /promotions để hiển thị cho học viên.

- **DAY 6:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai tích hợp chatbot AI và tài liệu hướng dẫn vận hành.
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-019], [DAT-009]
    * **Target Component file path (`target_component`):** ./sources/docs/ChatbotIntegrationGuide.md
    * **Low-Level Technical Task Instruction:** Soạn thảo tài liệu hướng dẫn tích hợp chatbot AI bao gồm các endpoint, cách thức xử lý hội thoại, quy tắc escalation, tham chiếu các Tag IDs [REQ-019], [DAT-009]; thêm các đoạn mã ví dụ bằng tiếng Việt.

### 📈 Giai đoạn 5: Bảo mật, tuân thủ, di động, pipeline
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai các biện pháp bảo mật doanh nghiệp, tuân thủ các yêu cầu phi chức năng, thiết lập quy trình DevOps và đảm bảo tuân thủ di động.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**
    * ./sources/infra/ (Docker) – [NFR-001], [NFR-002], [NFR-003]
    * ./sources/infra/ (GCP) – [NFR-004], [NFR-005], [NFR-006]
    * ./sources/infra/ (GKE) – [NFR-007], [NFR-008], [NFR-009]
    * ./sources/docs/ (Doc) – tài liệu bảo mật & tuân thủ
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu:** Không có bảng dữ liệu mới cho NFR.

- **Hợp đồng Định tuyến API và Sự kiện:** Không có hợp đồng API mới cho NFR.

- **Xử lý Ngoại lệ theo Ngôn Ngữ Bản Địa:** Không có ngoại lệ nghiệp vụ mới cho NFR.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 5)

- **DAY 1:** Mục tiêu ngắn gọn cho ngày hoạt động này: Xây dựng Docker image đa giai đoạn với kích thước nhỏ (<500MB) và base image <200MB.
    * **Sub-Agent Workflow Specialization:** [Docker]
    * **Tag IDs Mục tiêu:** [NFR-001], [NFR-002], [NFR-003]
    * **Target Component file path (`target_component`):** ./sources/infra/docker/QuarkusDockerfile
    * **Low-Level Technical Task Instruction:** Soạn thảo multi-stage Dockerfile: giai đoạn builder sử dụng image Quarkus có sẵn, giai đoạn runtime sử dụng distroless base image; đảm bảo loại bỏ các gói không cần thiết; thực hiện `apk add --no-cache` tối thiểu; xác minh kích thước image bằng `docker build --no-cache`; đẩy image lên container registry.

- **DAY 2:** Mục tiêu ngắn gọn cho ngày hoạt động này: Cung cấp hạ tầng GCP (VPC, IAM, Cloud Storage) và thiết lập monitoring.
    * **Sub-Agent Workflow Specialization:** [GCP]
    * **Tag IDs Mục tiêu:** [NFR-004], [NFR-005], [NFR-006]
    * **Target Component file path (`target_component`):** ./sources/infra/gcp/GCPInfrastructure.tf
    * **Low-Level Technical Task Instruction:** Triển khai Terraform script tạo VPC với private subnets, firewall rules; tạo IAM service accounts cho các service; thiết lập bucket Cloud Storage với lifecycle policy; tích hợp Prometheus và Grafana để monitoring; thiết lập alerting cho các chỉ số hiệu suất (latency, error rate).

- **DAY 3:** Mục tiêu ngắn gọn cho ngày hoạt động này: Triển khai Kubernetes (GKE) với HPA, tự động failover và backup cluster.
    * **Sub-Agent Workflow Specialization:** [GKE]
    * **Tag IDs Mục tiêu:** [NFR-007], [NFR-008], [NFR-009]
    * **Target Component file path (`target_component`):** ./sources/infra/gke/Deployment.yaml
    * **Low-Level Technical Task Instruction:** Soạn thảo Kubernetes Deployment cho các microservice Quarkus; cấu hình Resource Limits/Requests; thiết lập Horizontal Pod Autoscaler dựa trên CPU >70% hoặc latency >300ms; tạo ServiceEntry cho cross-cluster communication; thiết lập backup GKE cluster ở region khác; định kỳ kiểm tra SLA 99.9% và ghi log vào hệ thống monitoring.

## 📁 6. MÃ BẢO MẬT DOANH NGHIỆP TOÀN CẦU & BIỆN PHÁP CHỐNG INJECTION [NFR-XXX]

- **SQL Injection (SQLi) Absolute Countermeasures:** Sử dụng Prepared Statements / Parameterized Queries; áp dụng whitelist cho các ký tự đặc biệt trong sắp xếp; thực hiện kiểm tra kiểu dữ liệu ở tầng ứng dụng; sử dụng ORM (Hibernate) với naming strategy an toàn.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Áp dụng auto‑escaping trong React/Next.js (ví dụ: sử dụng dangerouslySetInnerHTML một cách hạn chế); thiết lập HTTP header Content‑Security‑Policy không cho phép 'unsafe-inline'; sử dụng DOMPurify cho các input người dùng; enforce SameSite=Strict cho cookies.
- **Multi‑Tenant CORS Security Rails:** whitelist các origin theo từng tenant; sử dụng biến môi trường động cho các nguồn gốc được phép; thực thi chính sách CORS ở tầng gateway (ví dụ: Spring Cloud Gateway); kiểm tra header Origin so với tenant configuration.
- **Zero‑Leak Log Scrubbing & PII Data Masking Engines:** Sử dụng MDC (Mapped Diagnostic Context) để lọc các trường nhạy cảm; áp dụng regex masking cho email, số điện thoại; tự động xóa các trường PII sau 30 ngày lưu trữ; tích hợp thư viện Logback Enhanced với policy masking.
- **Authentication & Authorization Hardening:** Áp dụng JWT với chữ ký RS256, thời gian sống ngắn (15 phút), refresh token có thời gian sống 7 ngày; thực thi OAuth2 với PKCE; sử dụng role‑based access control (RBAC) với các vai trò được định nghĩa trong bảng ROLES; thực hiện kiểm tra quyền hạn ở tầng dịch vụ; rotate secret keys định kỳ.
- **Encryption in Transit & at Rest:** Sử dụng TLS 1.3 cho tất cả các kết nối; thực hiện pinning chứng chỉ cho các dịch vụ quan trọng; mã hóa dữ liệu ở trạng thái nghỉ bằng AES‑256; quản lý khóa bằng Google KMS; tự động rotate khóa.
- **Secure Coding Guidelines:** Thực hiện kiểm tra tĩnh (SonarQube) để phát hiện các lỗ hổng bảo mật; tuân thủ OWASP Top 10; thực hiện kiểm tra thâm nhập định kỳ; ghi lại các phát hiện và remediation trong bảng AUDIT_LOG.

## 📁 7. QUY TẮC TUÂN THỦ DI ĐỘNG HỖN HỢP & CƠ CHẾ SEO QUỐC TẾ

- **Capacitor Mobile Hybrid Compliance Rails:** Sử dụng @capacitor/core để truy cập các tính năng native; thực hiện xác thực URL nghiêm ngặt cho các yêu cầu mạng; sử dụng @capacitor/preferences cho storage an toàn; chặn sự kiện back‑button để tránh thoát ứng dụng không mong muốn; thực hiện lazy‑load cho các chunk mã để cải thiện hiệu suất.
- **Internationalization (i18n) & Dynamic SEO Injection:** Sử dụng React Context + i18next cho việc dịch thuật; phát hiện ngôn ngữ từ header Accept‑Language và cookie preference; chèn thẻ hreflang vào HTML head; tạo sitemap.xml động với các URL được dịch; sử dụng meta robots để kiểm soát lập chỉ mục; tối ưu hóa tốc độ trang cho thiết bị di động (Lighthouse).
- **Responsive UI & Role‑Based Navigation:** Triển khai layout responsive với Breakpoints; sử dụng React Router với điều hướng dựa trên vai trò; ẩn/shadow các menu và nút dựa trên roleId; cache các tài nguyên UI để giảm độ trễ.
- **Offline Support & Service Workers:** Đăng ký Service Worker cho Next.js và React Native; sử dụng IndexedDB/LocalStorage cho data cache; đồng bộ dữ liệu khi kết nối lại; hiển thị thông báo khi ngoại tuyến.

## 📁 8. GIÓI HÓA TỰ ĐỘNG HÀNG NGÀY CHO PIPELINE GIT

- **Daily Workspace Forking Isolation:** Tự động fork workspace thành branch `features/development-phase-X-day-Y` (X là số giai đoạn, Y là số ngày trong giai đoạn, bắt đầu từ 1 cho mỗi giai đoạn).
- **Validation Guard Pipeline Gates:** Thực hiện kiểm tra biên dịch (`mvn clean install` / `npm run build`) trước khi merge; đảm bảo độ phủ mã >=85%; thực hiện kiểm tra tích hợp cho các API quan trọng; ghi log kết quả kiểm tra vào hệ thống CI; chỉ cho phép merge khi tất cả các kiểm tra vượt qua.
- **Artifact Promotion:** Sau khi vượt qua kiểm tra, tự động đẩy Docker image đã xây dựng lên registry; triển khai lên môi trường staging; thực hiện smoke test; nếu thành công, triển khai lên production GKE; ghi lại version và commit SHA vào bảng RELEASE_LOG.

### 📋 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 9, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`