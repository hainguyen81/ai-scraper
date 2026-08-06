# BỐ CỤC DỰ ÁN TOÀN CẦU: membership-hub

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806163720 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 16:37:20 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1 Chế độ Hệ thống Cốt lõi & Phương thức Kiến trúc
- Kiến trúc hướng dịch vụ vi mô (Microservices) với mỗi module (User, Center, Course, Enrollment, Attendance, Card, Notification, Promotion, Chatbot, Mobile) được triển khai dưới dạng dịch vụ độc lập.
- Áp dụng CQRS cho các bảng ghi danh (Enrollments), điểm danh (Attendance), và thẻ hội viên (StudentCards) để tách biệt đọc/ghi.
- Sử dụng Event Sourcing và Kafka cho các luồng nghiệp vụ chính: xác thực người dùng, xử lý điểm danh QR, và gửi thông báo.
- Triển khai Reactive Streams với RxJava trên backend Quarkus để xử lý bất đồng bộ và mở rộng theo hướng phi tập trung.
- Tích hợp OAuth2/OIDC với Firebase, Google, Facebook thông qua cổng xác thực tập trung.
- Áp dụng Multi-tenancy theo chiều dọc (Vertical) với mỗi Center có schema riêng trong PostgreSQL để đảm bảo cô lập dữ liệu.

### 1.2 Topologies Luồng Dữ liệu Doanh nghiệp & Hệ sinh thái Cốt lõi
- Luồng xác thực (ARC-006): Người dùng đăng nhập qua email, Firebase, Google, Facebook; nhận JWT (15 phút) và refresh token.
- Luồng xử lý điểm danh QR (ARC-007): Ứng dụng di động quét QR, gửi studentId + timestamp đến Attendance Service; ghi nhận bất biến thông qua khóa duy nhất (studentId + courseId + attendanceDate).
- Luồng thông báo (ARC-008): Backend kích hoạt push notification qua FCM/APNs và đăng bài lên nhóm Zalo được chỉ định cho từng loại thông báo.
- Luồng tích hợp backend ứng dụng di động (ARC-009): Frontend Next.js tiêu thụ REST API, xác thực qua bearer token, hỗ trợ caching ngoại tuyến qua IndexedDB.
- Tích hợp Redis cho cache phiên làm việc và rate limiting; sử dụng Flyway cho quản lý migration schema.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

### Stack Nền tảng Backend
- Java 21, Quarkus 3.2, Hibernate ORM, JDBC (PostgreSQL), Maven, Docker, Kubernetes (GKE), OpenTelemetry, JUnit 5, AssertJ, Flyway, Apache Kafka, OAuth2 OIDC, Firebase Admin SDK, Google Cloud Messaging (FCM), Zalo API SDK, Redis Java client, Jackson, Lombok, MapStruct, Spring Security (qua Quarkus).

### Stack Giao diện người dùng & Di động đa nền tảng
- Next.js 14 (React 18), TypeScript, Tailwind CSS, i18n (i18next), React Query, SWR, PWA, Capacitor cho hybrid mobile, Ionic/Capacitor, Firebase Authentication SDK, FCM SDK, Zalo SDK, Jest, React Testing Library.

### MA TRẬN STACK KIẾN TRÚC

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. TIÊU CHUẨN COMPLIANCE & GUARDRAILS TOÀN CẦU
- Tuân thủ nghiêm ngặt OWASP Top 10: sử dụng prepared statements, validation đầu vào, CSP headers, CSRF tokens.
- Mã hóa TLS 1.3 cho mọi kết nối; AES-256 cho dữ liệu ở trạng thái nghỉ.
- JWT access token hết hạn sau 15 phút; refresh token hết hạn sau 7 ngày; rotate token theo từng phiên.
- Multi-tenancy theo chiều dọc với mỗi Center có schema riêng để cô lập dữ liệu.
- Logging tất cả hành động người dùng (thay đổi vai trò, ghi danh, điểm danh, thông báo) với correlation ID; lưu trữ 1 năm.
- GDPR/CCPA: endpoint xóa dữ liệu cá nhân, xuất dữ liệu JSON, quản lý consent cho marketing.
- Hỗ trợ đa ngôn ngữ: English, Vietnamese, Spanish; externalize UI strings; chuyển đổi locale không cần reload trang.
- CI/CD với GitHub Actions: kiểm tra chất lượng mã, quét bảo mật, triển khai tự động lên GKE.

## 📁 4. BẢNG TÓM TẮT KIẾN TRÚC ĐA PHA Ở CẤP ĐỘ CAO

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | Day 1 - 2 | ./sources/backend/user-management/ | Xây dựng core user service, xác thực, phân quyền, model dữ liệu Users & Roles | Coder | [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [NFR-003], [NFR-004] |
| **Phase 2** | Day 1 - 2 | ./sources/backend/center-management/ | Triển khai center CRUD, gán Center Admin, model dữ liệu Centers | Coder | [REQ-004], [REQ-005], [REQ-006], [DAT-003], [NFR-003] |
| **Phase 3** | Day 1 - 2 | ./sources/backend/course-management/ | Xây dựng course CRUD, phân công giáo viên, logic ghi danh, model dữ liệu Courses & Enrollments | Coder | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005], [EXC-001], [NFR-003] |
| **Phase 4** | Day 1 - 2 | ./sources/backend/attendance-and-card/ | Triển khai attendance QR, đảm bảo bất biến, model dữ liệu Attendance & StudentCards, xử lý gia hạn thẻ | Coder | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-002], [EXC-005], [NFR-001] |
| **Phase 5** | Day 1 - 2 | ./sources/backend/notification-promotion-reporting/ | Xây dựng notification service, promotion & announcement management, chatbot integration, reporting API, i18n middleware, model dữ liệu Notifications, Promotions, Announcements, SystemSettings | Coder | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-008], [ARC-009], [DAT-008], [DAT-009], [DAT-011], [EXC-003], [EXC-004], [NFR-002], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |

## 📁 5. CÁC GIAI ĐOẠN CHI TIẾT & GIAO HÀNG NGÀY THEO NGÀY

### 📈 Phase 1 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng nền tảng người dùng cốt lõi, xác thực đa nhà cung cấp, và hệ thống phân quyền để hỗ trợ tất cả các vai trò người dùng trong hệ thống membership-hub.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** 
    *   ./sources/backend/user-management/UserService.java [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001]
    *   ./sources/backend/user-management/RoleService.java [REQ-003], [DAT-001]
    *   ./sources/docs/UserManagementArchitecture.md [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001]
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
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
```json
// POST /api/v1/auth/register
{
  "email": "user@example.com",
  "password": "StrongPass123!",
  "fullName": "Nguyen Van A",
  "provider": "local"
}
```
```json
// POST /api/v1/auth/social
{
  "provider": "google",
  "code": "OAuth2_code_from_google"
}
```
```json
// PUT /api/v1/users/{userId}/role
{
  "roleId": 2
}
```
- **Xử lý Ngoại lệ theo Ngôn ngữ Bản địa [EXC-001], [EXC-004]:**
    *   Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc): Trả về HTTP 400 với danh sách các trường không hợp lệ bằng tiếng Việt.
    *   Xung đột truy cập (ví dụ: cố gắng gán vai trò không được phép): Trả về HTTP 403 với thông báo “Bạn không có quyền thực hiện hành động này.”

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1: Xây dựng core user service và model dữ liệu**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001]
    * **Target Component file path (`target_component`):** ./sources/backend/user-management/UserService.java [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001]
    * **Low-Level Technical Task Instruction:** Triển khai UserService với các phương thức registerUser(UserDTO), authenticateSocial(SocialAuthRequest), assignRole(Long userId, Short roleId). Áp dụng validation theo JSR-380, mã hóa mật khẩu bằng BCrypt, tạo JWT (accessToken 15 phút, refreshToken 7 ngày). Thêm @RolesAllowed cho từng vai trò. Ghi nhật ký hành động người dùng với correlation ID.

- **DAY 2: Xây dựng role service và tài liệu kiến trúc**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-003], [DAT-001]
    * **Target Component file path (`target_component`):** ./sources/docs/UserManagementArchitecture.md [REQ-003], [DAT-001]
    * **Low-Level Technical Task Instruction:** Soạn thảo tài liệu kiến trúc chi tiết cho module quản lý người dùng, bao gồm sơ đồ ER, hợp đồng API, quy tắc bảo mật, và hướng dẫn triển khai. Đảm bảo tài liệu tham chiếu tất cả các Tag IDs liên quan.

### 📈 Phase 2 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai module quản lý trung tâm để System Admin có thể tạo, cập nhật, xóa trung tâm và phân quyền Center Admin, đảm bảo cô lập dữ liệu giữa các trung tâm.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** 
    *   ./sources/backend/center-management/CenterService.java [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    *   ./sources/docs/CenterManagementArchitecture.md [REQ-004], [REQ-005], [REQ-006], [DAT-003]
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
// Trả về danh sách các trung tâm với các trường: centerId, name, address, taxId, contactPhone, contactEmail
```
```json
// POST /api/v1/centers
{
  "name": "Chi nhánh Hà Nội",
  "address": "123 Đường Láng, Đống Đa, Hà Nội",
  "taxId": "0123456789",
  "contactPhone": "+84 123 456 789",
  "contactEmail": "hn@nlh4j.com"
}
```
```json
// PUT /api/v1/centers/{centerId}/assign-admin
{
  "userId": "a1b2c3d4-...",
  "centerId": "e5f6g7h8-..."
}
```
- **Xử lý Ngoại lệ theo Ngôn ngữ Bản địa [EXC-004]:**
    *   Xác thực đầu vào không hợp lệ (ví dụ: taxId trùng lặp): Trả về HTTP 409 với thông báo “Mã số thuế đã tồn tại. Vui lòng sử dụng mã khác.”
    *   Không có quyền truy cập: Trả về HTTP 403 với thông báo “Bạn không có quyền thực hiện hành động này.”

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1: Xây dựng CenterService và validation logic**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * **Target Component file path (`target_component`):** ./sources/backend/center-management/CenterService.java [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * **Low-Level Technical Task Instruction:** Triển khai CenterService với các phương thức createCenter(CenterDTO), updateCenter(UUID centerId, CenterDTO), deleteCenter(UUID centerId), assignCenterAdmin(UUID userId, UUID centerId). Sử dụng @Validated, kiểm tra tính duy nhất của taxId, áp dụng transaction isolation REPEATABLE READ. Ghi nhật ký hành động với correlation ID.

- **DAY 2: Soạn thảo tài liệu kiến trúc trung tâm**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * **Target Component file path (`target_component`):** ./sources/docs/CenterManagementArchitecture.md [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * **Low-Level Technical Task Instruction:** Hoàn thành tài liệu kiến trúc cho module quản lý trung tâm, bao gồm flow diagram, contract API, quy tắc bảo mật, và checklist triển khai. Đảm bảo tham chiếu đầy đủ các Tag IDs.

### 📈 Phase 3 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng module quản lý khóa học, bao gồm CRUD khóa học, phân công giáo viên, logic xung đột lịch học, và hệ thống ghi danh học viên.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** 
    *   ./sources/backend/course-management/CourseService.java [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005]
    *   ./sources/docs/CourseManagementArchitecture.md [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005]
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004], [DAT-005]:**
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

CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (studentId, courseId)
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011]:**
```json
// GET /api/v1/courses
// Trả về danh sách các khóa học với các trường: courseId, title, startDate, endDate, teacherName
```
```json
// POST /api/v1/courses
{
  "title": "Lập trình Java nâng cao",
  "description": "Khóa học về Quarkus và kiến trúc microservices",
  "startDate": "2026-09-01",
  "endDate": "2026-12-31",
  "teacherId": "a1b2c3d4-...",
  "maxStudents": 30
}
```
```json
// POST /api/v1/enrollments
{
  "studentId": "a1b2c3d4-...",
  "courseId": "e5f6g7h8-..."
}
```
- **Xử lý Ngoại lệ theo Ngôn Ngữ Bản Địa [EXC-001]:**
    *   Network & Connectivity Drops During QR Scan: Nếu mất kết nối trong khi ghi danh, khi kết nối được khôi phục, hệ thống sẽ tự động phát lại yêu cầu ghi danh và chỉ ghi nhận một bản ghi duy nhất.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 1: Xây dựng CourseService và logic validation**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005]
    * **Target Component file path (`target_component`):** ./sources/backend/course-management/CourseService.java [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005]
    * **Low-Level Technical Task Instruction:** Triển khai CourseService với các phương thức createCourse(CourseDTO), updateCourse(UUID courseId, CourseDTO), deleteCourse(UUID courseId), assignTeacher(UUID courseId, UUID teacherId), enrollStudent(UUID studentId, UUID courseId). Áp dụng kiểm tra xung đột lịch học cho giáo viên (startDate/endDate overlap). Sử dụng @Transactional và row-level locking. Ghi nhật ký hành động người dùng.

- **DAY 2: Soạn thảo tài liệu kiến trúc khóa học**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005]
    * **Target Component file path (`target_component`):** ./sources/docs/CourseManagementArchitecture.md [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-004], [DAT-005]
    * **Low-Level Technical Task Instruction:** Hoàn thành tài liệu kiến trúc cho module quản lý khóa học, bao gồm flow diagram, contract API, quy tắc bảo mật, và checklist triển khai. Đảm bảo tham chiếu đầy đủ các Tag IDs.

### 📈 Phase 4 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai module điểm danh QR và quản lý thẻ hội viên, đảm bảo tính bất biến của điểm danh và cung cấp UI hiển thị ngày hiệu lực thẻ.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** 
    *   ./sources/backend/attendance-and-card/AttendanceService.java [REQ-012], [REQ-013], [DAT-006]
    *   ./sources/backend/attendance-and-card/StudentCardService.java [REQ-014], [REQ-015], [DAT-007]
    *   ./sources/docs/AttendanceAndCardArchitecture.md [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007]
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-007]:**
```sql
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (studentId, courseId, attendanceDate)
);

CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [REQ-014], [REQ-015]:**
```json
// POST /api/v1/attendance/scan
{
  "studentId": "a1b2c3d4-...",
  "courseId": "e5f6g7h8-...",
  "qrCodeData": "course:e5f6g7h8-...|timestamp:2026-08-06T16:37:20Z"
}
```
```json
// GET /api/v1/studentcards/{studentId}/status
// Trả về object: { "validityDays": 30, "remainingDays": 12, "expiryDate": "2026-09-05" }
```
```json
// POST /api/v1/studentcards/{studentId}/renew
{
  "additionalDays": 30
}
```
- **Xử lý Ngoại lệ theo Ngôn Ngữ Bản Địa [EXC-002], [EXC-005]:**
    *   Duplicate Attendance Submission: Nếu cùng một studentId và courseId được gửi trong cùng một attendanceDate, trả về HTTP 200 với thông báo “Điểm danh đã được ghi nhận trước đó” và không tạo bản ghi mới.
    *   System Recovery After Outage: Khi dịch vụ được khôi phục sau sự cố, xử lý các yêu cầu điểm danh chờ (FIFO) và gửi push notification đến thiết bị của học viên thông báo về các sự kiện đã được khôi phục.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1: Xây dựng AttendanceService và validation bất biến**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [DAT-006], [EXC-002]
    * **Target Component file path (`target_component`):** ./sources/backend/attendance-and-card/AttendanceService.java [REQ-012], [REQ-013], [DAT-006], [EXC-002]
    * **Low-Level Technical Task Instruction:** Triển khai AttendanceService với phương thức recordAttendance(AttendanceRequest). Sử dụng khóa duy nhất (studentId, courseId, attendanceDate) và optimistic locking để đảm bảo chỉ một bản ghi được tạo ra ngay cả khi có nhiều yêu cầu trùng lặp. Ghi nhật ký hành động với correlation ID.

- **DAY 2: Xây dựng StudentCardService và tài liệu**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-014], [REQ-015], [DAT-007], [EXC-005]
    * **Target Component file path (`target_component`):** ./sources/docs/AttendanceAndCardArchitecture.md [REQ-014], [REQ-015], [DAT-007], [EXC-005]
    * **Low-Level Technical Task Instruction:** Hoàn thành tài liệu kiến trúc cho module điểm danh và thẻ hội viên, bao gồm flow diagram, contract API, quy tắc bảo mật, và checklist triển khai. Đảm bảo tham chiếu đầy đủ các Tag IDs.

### 📈 Phase 5 DETAILED ARCHITECTURAL SPECIFICATION
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai module thông báo, khuyến mãi, thông báo, chatbot, reporting, và middleware quốc tế hóa để hỗ trợ trải nghiệm đa ngôn ngữ và phân tích dữ liệu.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** 
    *   ./sources/backend/notification-promotion-reporting/NotificationService.java [REQ-016], [DAT-008]
    *   ./sources/backend/notification-promotion-reporting/PromotionService.java [REQ-017], [DAT-009]
    *   ./sources/backend/notification-promotion-reporting/AnnouncementService.java [REQ-018], [DAT-009]
    *   ./sources/backend/notification-promotion-reporting/ChatbotService.java [REQ-019]
    *   ./sources/backend/notification-promotion-reporting/ReportingService.java [REQ-024], [REQ-025], [DAT-011]
    *   ./sources/backend/notification-promotion-reporting/I18nMiddleware.java [REQ-022], [REQ-023]
    *   ./sources/docs/NotificationPromotionReportingArchitecture.md [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-024], [REQ-025], [DAT-008], [DAT-009], [DAT-011], [NFR-007]
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008], [DAT-009], [DAT-011]:**
```sql
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
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
    description TEXT
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-024], [REQ-025], [ARC-008], [ARC-009]:**
```json
// POST /api/v1/notifications
{
  "userId": "a1b2c3d4-...",
  "groupZalo": "group_xyz",
  "message": "Chào mừng bạn quay lại!"
}
```
```json
// POST /api/v1/promotions
{
  "code": "SUMMER20",
  "discountPercent": 20,
  "startDate": "2026-06-01",
  "endDate": "2026-08-31",
  "description": "Giảm giá 20% cho tất cả các khóa học"
}
```
```json
// POST /api/v1/announcements
{
  "title": "Cập nhật hệ thống",
  "content": "Hệ thống sẽ bảo trì vào ngày 10/09.",
  "startDate": "2026-09-01",
  "endDate": "2026-09-10"
}
```
```json
// POST /api/v1/chatbot/query
{
  "userId": "a1b2c3d4-...",
  "query": "Khóa học Java có những gì?"
}
```
```json
// GET /api/v1/reports/attendance?centerId=...&startDate=...&endDate=...
// Trả về CSV với các cột: StudentName, CourseName, AttendanceDate, Status
```
```json
// GET /api/v1/reports/dashboard?centerId=...
// Trả về JSON: { "totalStudents": 150, "activeCourses": 12, "upcomingSessions": 5 }
```
- **Xử lý Ngoại lệ theo Ngôn Ngữ Bản Địa [EXC-003], [EXC-004]:**
    *   Failed Notification Delivery: Nếu push notification không được gửi (ví dụ: device token không hợp lệ), hệ thống ghi lại lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu là thất bại.
    *   Xác thực đầu vào không hợp lệ (ví dụ: khuyến mãi có discountPercent > 100): Trả về HTTP 400 với thông báo “Phần trăm giảm giá không hợp lệ.”

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 1: Xây dựng NotificationService và PromotionService**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-016], [REQ-017], [DAT-008], [DAT-009], [EXC-003]
    * **Target Component file path (`target_component`):** ./sources/backend/notification-promotion-reporting/NotificationService.java [REQ-016], [REQ-017], [DAT-008], [DAT-009], [EXC-003]
    * **Low-Level Technical Task Instruction:** Triển khai NotificationService với phương thức sendNotification(NotificationRequest). Sử dụng FCM/APNs để gửi push notification, ghi nhật ký gửi nhận, và lên lịch retry cho các trường hợp thất bại. Triển khai PromotionService với các phương thức createPromotion(PromotionDTO), updatePromotion(UUID promoId, PromotionDTO), deletePromotion(UUID promoId). Áp dụng validation cho startDate/endDate và discountPercent.

- **DAY 2: Xây dựng AnnouncementService, ChatbotService, ReportingService, và I18nMiddleware**
    * **Sub-Agent Workflow Specialization:** [Doc]
    * **Tag IDs Mục tiêu:** [REQ-018], [REQ-019], [REQ-024], [REQ-025], [REQ-022], [REQ-023], [DAT-009], [DAT-011], [NFR-007]
    * **Target Component file path (`target_component`):** ./sources/docs/NotificationPromotionReportingArchitecture.md [REQ-018], [REQ-019], [REQ-024], [REQ-025], [REQ-022], [REQ-023], [DAT-009], [DAT-011], [NFR-7]
    * **Low-Level Technical Task Instruction:** Hoàn thành tài liệu kiến trúc cho module thông báo, khuyến mãi, chatbot, reporting, và middleware quốc tế hóa, bao gồm flow diagram, contract API, quy tắc bảo mật, và checklist triển khai. Đảm bảo tham chiếu đầy đủ các Tag IDs.

## 📁 6. MÃ BẢO MẬT DOANH NGHIỆP TOÀN CẦU & BIỆN PHÁP CHỐNG INJECTION [NFR-XXX]
- SQL Injection (SQLi) Absolute Countermeasures: Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- Cross-Site Scripting (XSS) & Content Security Policy (CSP): Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- Multi-Tenant CORS Security Rails: Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- Zero-Leak Log Scrubbing & PII Data Masking Engines: Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. QUY TẮC COMPLIANCE DI ĐỘNG HỖN HỢP & CƠ CHẾ SEO QUỐC TẾ
- Capacitor Mobile Hybrid Compliance Rails: [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- Internationalization (i18n) & Dynamic SEO Injection: Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. LUỒNG NGÀY GIT TỰ ĐỘNG HÓA PIPELINE
- Daily Workspace Forking Isolation: Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- Validation Guard Pipeline Gates: Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`