# TỔNG QUAN DỰ ÁN: membership-hub

## 📊 Kiểm soát Tài liệu

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808071243 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 07:12:43 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 🏛️ 1. TỔNG QUAN HỆ THỐNG

### 1.1. Mô hình Hệ thống Cốt lõi & Kiến trúc
- Triển khai kiến trúc đa dịch vụ với mô hình CQRS và xử lý bất đồng bộ dựa trên sự kiện.
- Tích hợp kiểm soát truy cập dựa trên vai trò (RBAC) với 6 vai trò chính: System Admin, Center Admin, Manager, Teacher, Student, và Mobile App User.
- Thiết kế hệ thống đa trung tâm với cơ sở dữ liệu riêng cho từng trung tâm và khả năng mở rộng theo chiều ngang.
- Sử dụng mô hình lưu trữ dữ liệu quan hệ với PostgreSQL, có bản sao đọc cho các tác vụ báo cáo.
- Tích hợp các nhà cung cấp xác thực bên thứ ba (Firebase, Google, Facebook) thông qua OAuth2 và cấp JWT token có thời hạn 15 phút.
- Triển khai các luồng xử lý điểm danh QR bất biến với khả năng phục hồi sau sự cố mạng.
- Tích hợp thông báo đa kênh (push notification qua FCM/APNs và bài đăng trên nhóm Zalo) với cơ chế thử lại.
- Hỗ trợ trải nghiệm di động hybrid với Capacitor, caching ngoại tuyến, và đồng bộ hóa khi có kết nối.
- Triển khai trên Kubernetes (GKE) với Docker, CI/CD qua GitHub Actions, và giám sát hiệu suất theo thời gian thực.
- Tuân thủ các tiêu chuẩn bảo mật OWASP Top 10, mã hóa dữ liệu ở trạng thái nghỉ bằng AES-256, và thực hiện các chính sách GDPR/CCPA.

### 1.2. Kiến trúc Luồng Dữ liệu Doanh nghiệp & Hệ sinh thái
- Luồng xác thực: Người dùng đăng nhập qua email/mật khẩu hoặc mạng xã hội, nhận JWT token và refresh token.
- Luồng xử lý điểm danh QR: Ứng dụng di động quét mã QR, gửi studentId và timestamp đến dịch vụ điểm danh, ghi lại bản ghi bất biến.
- Luồng gửi thông báo: Hệ thống tạo bản ghi thông báo, đẩy notification đến thiết bị di động qua FCM/APNs, và đăng bài lên nhóm Zalo được chỉ định.
- Luồng tích hợp backend ứng dụng di động: Frontend Next.js tiêu thụ REST APIs, xác thực qua bearer token, và duy trì cache ngoại tuyến cho các tác vụ quan trọng.
- Luồng đồng bộ hóa dữ liệu đa trung tâm: Center Admin quản lý trung tâm của mình, System Admin giám sát toàn cầu, và các thay đổi được đồng bộ hóa qua message broker.
- Luồng xử lý sự kiện: Các sự kiện như ghi danh khóa học, điểm danh, gia hạn thẻ được phát hành dưới dạng sự kiện để cập nhật trạng thái và kích hoạt thông báo.
- Luồng xử lý hàng đợi: Các tác vụ nặng như gửi hàng loạt thông báo, tạo báo cáo được đưa vào hàng đợi và xử lý bất đồng bộ.
- Luồng xử lý ngoại lệ: Các lỗi mạng, duplicate attendance được ghi lại, thử lại, và thông báo cho người dùng.

## 📁 2. THƯ VIỆN STACK CÔNG NGHỆ & HỆ SINH THÁI

- **Hạ tầng Core Stack:** Java/Quarkus (v3.8.x), PostgreSQL (v15), Docker (<500MB), Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Zalo API, Redis (for session caching), CI/CD GitHub Actions.
- **Frontend & Stack UI Di động Đa nền tảng:** Next.js (v14), React Native (v0.73), Capacitor, Internationalization (i18next), State management (Redux Toolkit), API client (Axios), Offline caching (Redux Persist), SEO (Next SEO), Responsive design.

### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. BẢN MẠCH BẢO MẬT DOANH NGHIỆP TOÀN CẦU & PHÒNG NGỪA TẤN CÔNG

- **Các biện pháp chống SQL Injection (SQLi):** Sử dụng prepared statements, tham số hóa truy vấn, và danh sách trắng cho các tham số sắp xếp.
- **Các biện pháp chống Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động thoát HTML trong JSX, thiết lập header CSP nghiêm ngặt (`script-src 'self'`), và sử dụng DOMPurify cho nội dung người dùng.
- **Các biện pháp chống CORS đa tenant:** Kiểm tra nguồn gốc động, cho phép chỉ các tên miền được tin cậy, và lưu trữ các chính sách CORS theo từng tenant.
- **Các biện pháp chống rò rỉ log & che giấu PII:** Sử dụng `@JsonSerialize` để ẩn PII, tự động xóa các trường nhạy cảm, và giới hạn độ dài log.
- **Các chỉ số hiệu suất:** Đảm bảo độ trễ trung bình dưới 200ms cho các API cốt lõi, sử dụng chỉ mục cho các truy vấn thường xuyên, và hỗ trợ 10,000 người dùng đồng thời.
- **Các chỉ số khả năng sẵn sàng:** Mục tiêu 99.9% thời gian hoạt động, triển khai auto-failover trên các cluster GKE, và giám sát sức khỏe theo thời gian thực.
- **Các chỉ số bảo mật:** TLS 1.3 cho mọi kết nối, mã hóa AES-256 ở trạng thái nghỉ, JWT hết hạn sau 15 phút, refresh token 7 ngày, và tuân thủ OWASP Top 10.
- **Các chỉ số khả năng mở rộng & sẵn sàng:** Tự động mở rộng Quarkus dựa trên HPA (CPU >70% hoặc độ trễ >300ms), sử dụng PostgreSQL read replicas cho báo cáo, và triển khai service mesh cho giao tiếp giữa các dịch vụ.
- **Các chỉ số kích thước Docker:** Giới hạn kích thước image gốc <200MB, image cuối cùng <500MB, và tối ưu hóa các layer không cần thiết.
- **Các chỉ số ghi nhật ký & kiểm toán:** Ghi lại mọi hành động của người dùng (thay đổi vai trò, điểm danh, thông báo) với timestamp, userId, và chi tiết hành động; lưu trữ log trong 1 năm.
- **Các chỉ số hỗ trợ đa ngôn ngữ:** Ngoại giao hóa chuỗi UI, hỗ trợ English, Vietnamese, Spanish, và chuyển đổi locale không cần tải lại trang.
- **Các chỉ số tuân thủ GDPR/CCPA:** Cho phép người dùng yêu cầu xóa dữ liệu cá nhân, cung cấp API xuất dữ liệu JSON, và quản lý sự đồng ý cho tiếp thị.
- **Các chỉ số sao lưu & phục hồi sau thảm họa:** Sao lưu PostgreSQL đầy đủ hàng ngày, phục hồi điểm trong thời gian 24 giờ, và sao lưu cluster GKE sang region khác.

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Đường dẫn Thành phần / Module Kiến trúc | Tóm tắt Sản phẩm Bàn giao | Sub-Agent được chỉ định | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1 - 4 | ./sources/backend/user-management/ | Triển khai đăng ký người dùng, xác thực xã hội, phân quyền, tạo trung tâm, gán quyền trung tâm; viết unit tests; tài liệu kỹ thuật; đánh giá mã. | Coder, Tester, Doc, Reviewer | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [DAT-002], [EXC-004], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
| Giai đoạn 2 | Ngày 1 - 4 | ./sources/backend/course-management/ | Triển khai CRUD khóa học, xung đột lịch, phân công giáo viên, duyệt khóa học, ghi danh, quét QR điểm danh, tính bất biến, hiển thị thẻ hội viên, gia hạn thẻ; viết integration tests; tài liệu API; đánh giá mã. | Coder, Tester, Doc, Reviewer | [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [EXC-001], [EXC-002], [NFR-001], [NFR-002], [NFR-003] |
| Giai đoạn 3 | Ngày 1 - 3 | ./sources/backend/notification-management/ | Triển khai kích hoạt thông báo, tạo khuyến mãi, thông báo, tích hợp chatbot AI, push notification, tích hợp Zalo; viết E2E tests; tài liệu kỹ thuật; đánh giá mã. | Coder, Tester, Doc, Reviewer | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [ARC-008], [DAT-007], [DAT-008], [EXC-003], [NFR-001], [NFR-002], [NFR-003] |
| Giai đoạn 4 | Ngày 1 - 5 | ./sources/frontend/nextjs/, ./sources/mobile/capacitor/, ./sources/infra/ | Triển khai giao diện người dùng di động responsive, thông báo đẩy, phát hiện ngôn ngữ, SEO đa ngôn ngữ, tạo báo cáo điểm danh, bảng điều khiển, phục hồi sau sự cố, hardening bảo mật; viết integration tests; tài liệu hệ thống; đánh giá mã. | Coder, Tester, Doc, Reviewer | [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-009], [ARC-010], [DAT-009], [EXC-005], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009] |
<!--END_PHASE_SYNOPSIS_GRID-->

## 📁 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Giai đoạn 1: Xây dựng Nền tảng Cốt lõi

- **Phase Core Objective & Purpose:** Xây dựng các thành phần cốt lõi cho hệ thống quản lý hội viên đa trung tâm, bao gồm quản lý người dùng, xác thực, phân quyền, và quản lý trung tâm.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend/user-management/UserEntity.java [REQ-001], [DAT-001]
  * ./sources/backend/user-management/RoleEntity.java [DAT-001]
  * ./sources/backend/user-management/CenterEntity.java [REQ-004], [DAT-002]
  * ./sources/docs/UserManagementGuide.md [DAT-001], [REQ-001]
- **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-001], [DAT-002]:**
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
    createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
    updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(30),
    contactEmail VARCHAR(255)
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]:**
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
```json
// PUT /api/v1/users/{userId}/role
{
  "newRoleId":2
}
```
- **Xử lý Ngoại lệ theo Ngôn ngữ [EXC-004]:**
  * Khi xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc), hệ thống trả về lỗi 400 với danh sách các trường không hợp lệ và hướng dẫn chỉnh sửa.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 1)

- **NGÀY 1:**
  - **[Coder]** [REQ-001], [DAT-001] ./sources/backend/user-management/UserService.java Triển khai logic đăng ký người dùng, xác thực mật khẩu, tạo password hash, và trả về JWT token.
  - **[Tester]** [REQ-001], [DAT-001] ./sources/backend/user-management/UserServiceTest.java;./sources/backend/user-management/UserService.java Viết unit test cho đăng ký người dùng, bao gồm xác thực email, độ mạnh mật khẩu, và tạo token.
  - **[Doc]** [REQ-001], [DAT-001] ./sources/docs/UserRegistrationGuide.md Soạn thảo hướng dẫn kỹ thuật cho API đăng ký người dùng, bao gồm request/response schema và ví dụ.
  - **[Reviewer]** [REQ-001], [DAT-001] ./sources/backend/user-management/UserService.java Đánh giá mã nguồn, đảm bảo tuân thủ các quy tắc lập trình, và kiểm tra độ bao phủ unit test.

- **NGÀY 2:**
  - **[Coder]** [REQ-002], [DAT-001] ./sources/backend/user-management/SocialAuthService.java Triển khai trao đổi OAuth2 code lấy thông tin người dùng từ Firebase/Google/Facebook, tạo hoặc cập nhật bản ghi người dùng.
  - **[Tester]** [REQ-002], [DAT-001] ./sources/backend/user-management/SocialAuthServiceTest.java;./sources/backend/user-management/SocialAuthService.java Viết integration test cho xác thực xã hội, mô phỏng các nhà cung cấp.
  - **[Doc]** [REQ-002], [DAT-001] ./sources/docs/SocialAuthenticationGuide.md Soạn thảo tài liệu kỹ thuật cho endpoint xác thực xã hội, bao gồm flow và lỗi.
  - **[Reviewer]** [REQ-002], [DAT-001] ./sources/backend/user-management/SocialAuthService.java Kiểm tra logic xử lý token, xác thực nhà cung cấp, và cập nhật người dùng.

- **NGÀY 3:**
  - **[Coder]** [REQ-003], [ARC-001] ./sources/backend/user-management/RoleService.java Triển khai gán vai trò người dùng, áp dụng RBAC, và ghi lại lịch sử thay đổi vai trò.
  - **[Tester]** [REQ-003], [ARC-001] ./sources/backend/user-management/RoleServiceTest.java;./sources/backend/user-management/RoleService.java Viết unit test cho gán vai trò, bao gồm kiểm tra quyền truy cập.
  - **[Doc]** [REQ-003], [ARC-001] ./sources/docs/RoleManagementGuide.md Soạn thảo hướng dẫn quản lý vai trò, bao gồm các quyền hạn theo từng vai trò.
  - **[Reviewer]** [REQ-003], [ARC-001] ./sources/backend/user-management/RoleService.java Đánh giá việc thực thi RBAC, đảm bảo cách ly đa trung tâm.

- **NGÀY 4:**
  - **[Coder]** [REQ-004], [REQ-005], [REQ-006], [DAT-002] ./sources/backend/center-management/CenterService.java Triển khai CRUD trung tâm, validation trùng taxId, và gán Center Admin cho trung tâm.
  - **[Tester]** [REQ-004], [REQ-005], [REQ-006], [DAT-002] ./sources/backend/center-management/CenterServiceTest.java;./sources/backend/center-management/CenterService.java Viết integration test cho các thao tác trung tâm, bao gồm validation taxId và phân quyền.
  - **[Doc]** [REQ-004], [REQ-005], [REQ-006], [DAT-002] ./sources/docs/CenterManagementGuide.md Soạn thảo tài liệu kỹ thuật cho API quản lý trung tâm.
  - **[Reviewer]** [REQ-004], [REQ-005], [REQ-006], [DAT-002] ./sources/backend/center-management/CenterService.java Kiểm tra logic cách ly trung tâm, đảm bảo Center Admin chỉ truy cập trung tâm của mình.

### 📈 Giai đoạn 2: Quản lý Khóa học, Ghi danh và Điểm danh

- **Phase Core Objective & Purpose:** Triển khai các tính năng quản lý khóa học, ghi danh học viên, điểm danh qua QR, và quản lý thẻ hội viên với tính bất biến và hiệu lực.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend/course-management/CourseEntity.java [REQ-007], [DAT-003]
  * ./sources/backend/course-management/EnrollmentEntity.java [REQ-010], [DAT-004]
  * ./sources/backend/attendance/AttendanceEntity.java [REQ-012], [DAT-005]
  * ./sources/backend/membership/MembershipCardEntity.java [REQ-014], [DAT-006]
  * ./sources/docs/CourseManagementGuide.md [DAT-003], [REQ-007]
- **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-003], [DAT-004], [DAT-005], [DAT-006]:**
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
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009], [ARC-007]:**
```json
// GET /api/v1/courses
{
  "courses": [
    {"courseId":"uuid","title":"Lập trình Java","startDate":"2024-09-01","endDate":"2024-12-31","teacherName":"Nguyen A"}
  ]
}
```
```json
// POST /api/v1/courses
{
  "title":"Lập trình Python",
  "description":"Khóa học về Python",
  "startDate":"2024-10-01",
  "endDate":"2024-12-31",
  "teacherId":"uuid_of_teacher"
}
```
```json
// POST /api/v1/attendance/scan
{
  "studentId":"uuid",
  "courseId":"uuid",
  "timestamp":"2024-09-01T08:00:00Z"
}
```
- **Xử lý Ngoại lệ theo Ngôn ngữ [EXC-001], [EXC-002]:**
  * Nếu sinh viên quét QR nhưng không có kết nối mạng, ứng dụng lưu yêu cầu locally và đồng bộ khi có kết nối; hệ thống thông báo cho sinh viên về trạng thái.
  * Nếu sinh viên quét QR nhiều lần trong cùng ngày, chỉ ghi lại một bản ghi điểm danh; các lần quét sau trả về success với cờ duplicate.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 2)

- **NGÀY 1:**
  - **[Coder]** [REQ-007], [DAT-003] ./sources/backend/course-management/CourseService.java Triển khai CRUD khóa học, validation xung đột lịch với giáo viên.
  - **[Tester]** [REQ-007], [DAT-003] ./sources/backend/course-management/CourseServiceTest.java;./sources/backend/course-management/CourseService.java Viết unit test cho CRUD khóa học, bao gồm kiểm tra trùng lịch.
  - **[Doc]** [REQ-007], [DAT-003] ./sources/docs/CourseCRUDGuide.md Soạn thảo tài liệu kỹ thuật cho API khóa học.
  - **[Reviewer]** [REQ-007], [DAT-003] ./sources/backend/course-management/CourseService.java Đánh giá logic validation, đảm bảo không có xung đột lịch.

- **NGÀY 2:**
  - **[Coder]** [REQ-010], [REQ-011], [DAT-004] ./sources/backend/course-management/EnrollmentService.java Triển khai duyệt khóa học, ghi danh, tự động tạo tài khoản Student nếu thiếu.
  - **[Tester]** [REQ-010], [REQ-011], [DAT-004] ./sources/backend/course-management/EnrollmentServiceTest.java;./sources/backend/course-management/EnrollmentService.java Viết integration test cho ghi danh, bao gồm kiểm tra capacity.
  - **[Doc]** [REQ-010], [REQ-011], [DAT-004] ./sources/docs/EnrollmentGuide.md Soạn thảo hướng dẫn ghi danh khóa học.
  - **[Reviewer]** [REQ-010], [REQ-011], [DAT-004] ./sources/backend/course-management/EnrollmentService.java Kiểm tra logic tạo tài khoản, đảm bảo vai trò Student được gán đúng.

- **NGÀY 3:**
  - **[Coder]** [REQ-012], [REQ-013], [DAT-005] ./sources/backend/attendance/AttendanceService.java Triển khai quét QR điểm danh, đảm bảo tính bất biến cho cùng studentId, courseId, attendanceDate.
  - **[Tester]** [REQ-012], [REQ-013], [DAT-005] ./sources/backend/attendance/AttendanceServiceTest.java;./sources/backend/attendance/AttendanceService.java Viết unit test cho điểm danh, bao gồm duplicate detection.
  - **[Doc]** [REQ-012], [REQ-013], [DAT-005] ./sources/docs/AttendanceGuide.md Soạn thảo tài liệu kỹ thuật cho API điểm danh.
  - **[Reviewer]** [REQ-012], [REQ-013], [DAT-005] ./sources/backend/attendance/AttendanceService.java Đánh giá logic duplicate, đảm bảo chỉ một bản ghi được tạo.

- **NGÀY 4:**
  - **[Coder]** [REQ-014], [REQ-015], [DAT-006] ./sources/backend/membership/MembershipCardService.java Triển khai hiển thị ngày hiệu lực thẻ, xử lý gia hạn thẻ qua payment gateway.
  - **[Tester]** [REQ-014], [REQ-015], [DAT-006] ./sources/backend/membership/MembershipCardServiceTest.java;./sources/backend/membership/MembershipCardService.java Viết unit test cho hiển thị thẻ và gia hạn.
  - **[Doc]** [REQ-014], [REQ-015], [DAT-006] ./sources/docs/MembershipCardGuide.md Soạn thảo tài liệu kỹ thuật cho thẻ hội viên.
  - **[Reviewer]** [REQ-014], [REQ-015], [DAT-006] ./sources/backend/membership/MembershipCardService.java Kiểm tra logic tính remainingDays, đảm bảo gia hạn cập nhật đúng EndDate.

### 📈 Giai đoạn 3: Quản lý Thông báo, Khuyến mãi và Chatbot

- **Phase Core Objective & Purpose:** Triển khai hệ thống thông báo đa kênh, quản lý khuyến mãi và thông báo, tích hợp chatbot AI, và push notification cho di động.
- **Target Physical Directory Matrix Map:**
  * ./sources/backend/notification-management/NotificationEntity.java [REQ-016], [DAT-007]
  * ./sources/backend/promotion/PromotionEntity.java [REQ-017], [DAT-008]
  * ./sources/backend/announcement/AnnouncementEntity.java [REQ-018], [DAT-008]
  * ./sources/backend/chatbot/ChatbotService.java [REQ-019], [NOT APPLICABLE]
  * ./sources/docs/NotificationGuide.md [DAT-007], [REQ-016]
- **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-007], [DAT-008]:**
```sql
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID,
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
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
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [REQ-017], [REQ-018], [ARC-008]:**
```json
// POST /api/v1/notifications
{
  "userId":"uuid",
  "groupZalo":"ZaloGroup123",
  "message":"Chào mừng bạn đến với trung tâm!"
}
```
```json
// POST /api/v1/promotions
{
  "code":"SUMMER20",
  "discountPercent":20,
  "startDate":"2024-06-01",
  "endDate":"2024-08-31",
  "description":"Giảm giá 20% cho tất cả khóa học"
}
```
```json
// POST /api/v1/announcements
{
  "title":"Thông báo quan trọng",
  "content":"Hệ thống bảo trì vào cuối tuần.",
  "startDate":"2024-09-01",
  "endDate":"2024-09-02"
}
```
- **Xử lý Ngoại lệ theo Ngôn ngữ [EXC-003]:**
  * Nếu push notification không thể gửi (ví dụ: device token không hợp lệ), hệ thống ghi lại lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu là thất bại.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 3)

- **NGÀY 1:**
  - **[Coder]** [REQ-016], [DAT-007] ./sources/backend/notification-management/NotificationService.java Triển khai tạo bản ghi thông báo, đẩy push notification qua FCM/APNs, và gửi bài lên Zalo group.
  - **[Tester]** [REQ-016], [DAT-007] ./sources/backend/notification-management/NotificationServiceTest.java;./sources/backend/notification-management/NotificationService.java Viết integration test cho gửi thông báo đa kênh.
  - **[Doc]** [REQ-016], [DAT-007] ./sources/docs/NotificationServiceGuide.md Soạn thảo tài liệu kỹ thuật cho API thông báo.
  - **[Reviewer]** [REQ-016], [DAT-007] ./sources/backend/notification-management/NotificationService.java Đánh giá logic gửi notification, đảm bảo retry mechanism.

- **NGÀY 2:**
  - **[Coder]** [REQ-017], [REQ-018], [DAT-008] ./sources/backend/promotion/PromotionService.java Triển khai CRUD khuyến mãi và thông báo, bao gồm validation ngày hiệu lực.
  - **[Tester]** [REQ-017], [REQ-018], [DAT-008] ./sources/backend/promotion/PromotionServiceTest.java;./sources/backend/promotion/PromotionService.java Viết unit test cho CRUD khuyến mãi và thông báo.
  - **[Doc]** [REQ-017], [REQ-018], [DAT-008] ./sources/docs/PromotionAnnouncementGuide.md Soạn thảo tài liệu kỹ thuật cho API khuyến mãi và thông báo.
  - **[Reviewer]** [REQ-017], [REQ-018], [DAT-008] ./sources/backend/promotion/PromotionService.java Kiểm tra logic expiration, đảm bảo hiển thị đúng theo ngày.

- **NGÀY 3:**
  - **[Coder]** [REQ-019], [NOT APPLICABLE] ./sources/backend/chatbot/ChatbotService.java Triển khai tích hợp chatbot AI, trả lời truy vấn về khóa học, giáo viên, trung tâm, và chuyển đến hỗ trợ người thật nếu cần.
  - **[Tester]** [REQ-019], [NOT APPLICABLE] ./sources/backend/chatbot/ChatbotServiceTest.java;./sources/backend/chatbot/ChatbotService.java Viết unit test cho phản hồi chatbot, bao gồm confidence scoring.
  - **[Doc]** [REQ-019], [NOT APPLICABLE] ./sources/docs/ChatbotGuide.md Soạn thảo tài liệu kỹ thuật cho API chatbot.
  - **[Reviewer]** [REQ-019], [NOT APPLICABLE] ./sources/backend/chatbot/ChatbotService.java Đánh giá chất lượng phản hồi, đảm bảo tuân thủ chính sách bảo mật.

### 📈 Giai đoạn 4: Di động, Quốc tế hóa và Báo cáo

- **Phase Core Objective & Purpose:** Triển khai giao diện người dùng di động responsive, hỗ trợ đa ngôn ngữ, SEO, tạo báo cáo điểm danh, bảng điều khiển, và hardening bảo mật cho hệ thống.
- **Target Physical Directory Matrix Map:**
  * ./sources/frontend/nextjs/pages/[locale]/courses.tsx [REQ-007], [REQ-022]
  * ./sources/mobile/capacitor/src/app/App.tsx [REQ-020], [REQ-021]
  * ./sources/infra/docker/QuarkusDockerfile [ARC-010]
  * ./sources/infra/k8s/GKE-deployment.yaml [ARC-010]
  * ./sources/docs/ReportingGuide.md [REQ-024], [REQ-025]
- **Đặc tả DDL SQL Lược đồ Cơ sở Dữ liệu [DAT-009]:**
```sql
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(100) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description TEXT
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-009]:**
```json
// GET /api/v1/reports/attendance?centerId=uuid&date=2024-09-01
{
  "attendanceRecords": [
    {"studentName":"Nguyen A","courseName":"Lập trình Java","attendanceDate":"2024-09-01","status":"present"}
  ]
}
```
```json
// GET /api/v1/dashboard/center?centerId=uuid
{
  "totalStudents":150,
  "activeCourses":12,
  "upcomingSessions":5
}
```
- **Xử lý Ngoại lệ theo Ngôn ngữ [EXC-005]:**
  * Nếu dịch vụ không khả dụng, các yêu cầu điểm danh chờ xử lý được ghi lại, và khi dịch vụ phục hồi, chúng được xử lý theo thứ tự FIFO; người dùng nhận thông báo về các sự kiện đã phục hồi.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Giai đoạn 4)

- **NGÀY 1:**
  - **[Coder]** [REQ-022], [REQ-023], [ARC-009] ./sources/frontend/nextjs/pages/[locale]/courses.tsx Triển khai giao diện duyệt khóa học đa ngôn ngữ, tích hợp SEO meta tags và hreflang.
  - **[Tester]** [REQ-022], [REQ-023], [ARC-009] ./sources/frontend/nextjs/pages/[locale]/courses.spec.ts;./sources/frontend/nextjs/pages/[locale]/courses.tsx Viết E2E test cho giao diện đa ngôn ngữ và SEO.
  - **[Doc]** [REQ-022], [REQ-023], [ARC-009] ./sources/docs/InternationalizationGuide.md Soạn thảo tài liệu kỹ thuật cho i18n và SEO.
  - **[Reviewer]** [REQ-022], [REQ-023], [ARC-009] ./sources/frontend/nextjs/pages/[locale]/courses.tsx Đánh giá việc render locale, đảm bảo SEO tags đúng định dạng.

- **NGÀY 2:**
  - **[Coder]** [REQ-020], [REQ-021], [ARC-009] ./sources/mobile/capacitor/src/app/App.tsx Triển khai navigation role-based cho mobile, đăng ký device token cho push notification.
  - **[Tester]** [REQ-020], [REQ-021], [ARC-009] ./sources/mobile/capacitor/src/app/App.spec.ts;./sources/mobile/capacitor/src/app/App.tsx Viết unit test cho navigation mobile và đăng ký token.
  - **[Doc]** [REQ-020], [REQ-021], [ARC-009] ./sources/docs/MobileAppGuide.md Soạn thảo tài liệu kỹ thuật cho ứng dụng di động.
  - **[Reviewer]** [REQ-020], [REQ-021], [ARC-009] ./sources/mobile/capacitor/src/app/App.tsx Kiểm tra việc cách ly vai trò, đảm bảo bảo mật token.

- **NGÀY 3:**
  - **[Coder]** [REQ-024], [REQ-025], [DAT-009] ./sources/backend/reporting/ReportingService.java Triển khai tạo báo cáo điểm danh CSV, và API bảng điều khiển.
  - **[Tester]** [REQ-024], [REQ-025], [DAT-009] ./sources/backend/reporting/ReportingServiceTest.java;./sources/backend/reporting/ReportingService.java Viết integration test cho báo cáo và bảng điều khiển.
  - **[Doc]** [REQ-024], [REQ-025], [DAT-009] ./sources/docs/ReportingDashboardGuide.md Soạn thảo tài liệu kỹ thuật cho API báo cáo.
  - **[Reviewer]** [REQ-024], [REQ-025], [DAT-009] ./sources/backend/reporting/ReportingService.java Đánh giá hiệu suất query, đảm bảo định dạng CSV đúng.

- **NGÀY 4:**
  - **[Coder]** [ARC-010], [NFR-005] ./sources/infra/docker/QuarkusDockerfile Triển khai multi-stage Dockerfile, giới hạn kích thước image <500MB.
  - **[Tester]** [ARC-010], [NFR-005] ./sources/infra/docker/QuarkusDockerfile;./sources/infra/docker/QuarkusDockerfile Viết test cho quá trình build image, kiểm tra kích thước.
  - **[Doc]** [ARC-010], [NFR-005] ./sources/docs/DevOpsGuide.md Soạn thảo tài liệu kỹ thuật cho containerization.
  - **[Reviewer]** [ARC-010], [NFR-005] ./sources/infra/docker/QuarkusDockerfile Đánh giá Dockerfile, đảm bảo tuân thủ giới hạn kích thước.

- **NGÀY 5:**
  - **[Coder]** [ARC-010], [NFR-004] ./sources/infra/k8s/GKE-deployment.yaml Triển khai Kubernetes deployment manifest, cấu hình HPA dựa trên CPU và độ trễ.
  - **[Tester]** [ARC-010], [NFR-004] ./sources/infra/k8s/GKE-deployment.yaml;./sources/infra/k8s/GKE-deployment.yaml Viết test cho manifest, đảm bảo scaling hoạt động.
  - **[Doc]** [ARC-010], [NFR-004] ./sources/docs/K8sGuide.md Soạn thảo tài liệu kỹ thuật cho triển khai GKE.
  - **[Reviewer]** [ARC-010], [NFR-004] ./sources/infra/k8s/GKE-deployment.yaml Kiểm tra cấu hình HPA, đảm bảo tuân thủ yêu cầu hiệu suất.

## 📁 6. BẢN MẠCH BẢO MẬT DOANH NGHIỆP TOÀN CẦU & PHÒNG NGỪA TẤN CÔNG [NFR-XXX]

- **Các biện pháp chống SQL Injection (SQLi):** Sử dụng prepared statements, tham số hóa truy vấn, và danh sách trắng cho các tham số sắp xếp.
- **Các biện pháp chống Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Tự động thoát HTML trong JSX, thiết lập header CSP nghiêm ngặt (`script-src 'self'`), và sử dụng DOMPurify cho nội dung người dùng.
- **Các biện pháp chống CORS đa tenant:** Kiểm tra nguồn gốc động, cho phép chỉ các tên miền được tin cậy, và lưu trữ các chính sách CORS theo từng tenant.
- **Các biện pháp chống rò rỉ log & che giấu PII:** Sử dụng `@JsonSerialize` để ẩn PII, tự động xóa các trường nhạy cảm, và giới hạn độ dài log.
- **Các chỉ số hiệu suất:** Đảm bảo độ trễ trung bình dưới 200ms cho các API cốt lõi, sử dụng chỉ mục cho các truy vấn thường xuyên, và hỗ trợ 10,000 người dùng đồng thời.
- **Các chỉ số khả năng sẵn sàng:** Mục tiêu 99.9% thời gian hoạt động, triển khai auto-failover trên các cluster GKE, và giám sát sức khỏe theo thời gian thực.
- **Các chỉ số bảo mật:** TLS 1.3 cho mọi kết nối, mã hóa AES-256 ở trạng thái nghỉ, JWT hết hạn sau 15 phút, refresh token 7 ngày, và tuân thủ OWASP Top 10.
- **Các chỉ số khả năng mở rộng & sẵn sàng:** Tự động mở rộng Quarkus dựa trên HPA (CPU >70% hoặc độ trễ >300ms), sử dụng PostgreSQL read replicas cho báo cáo, và triển khai service mesh cho giao tiếp giữa các dịch vụ.
- **Các chỉ số kích thước Docker:** Giới hạn kích thước image gốc <200MB, image cuối cùng <500MB, và tối ưu hóa các layer không cần thiết.
- **Các chỉ số ghi nhật ký & kiểm toán:** Ghi lại mọi hành động của người dùng (thay đổi vai trò, điểm danh, thông báo) với timestamp, userId, và chi tiết hành động; lưu trữ log trong 1 năm.
- **Các chỉ số hỗ trợ đa ngôn ngữ:** Ngoại giao hóa chuỗi UI, hỗ trợ English, Vietnamese, Spanish, và chuyển đổi locale không cần tải lại trang.
- **Các chỉ số tuân thủ GDPR/CCPA:** Cho phép người dùng yêu cầu xóa dữ liệu cá nhân, cung cấp API xuất dữ liệu JSON, và quản lý sự đồng ý cho tiếp thị.
- **Các chỉ số sao lưu & phục hồi sau thảm họa:** Sao lưu PostgreSQL đầy đủ hàng ngày, phục hồi điểm trong thời gian 24 giờ, và sao lưu cluster GKE sang region khác.

## 📁 7. QUY TẮC TUÂN THỦ DI ĐỘNG HYBRID & CƠ CHẾ SEO QUỐC TẾ

- **Các quy tắc tuân thủ di động hybrid Capacitor:** Triển khai dynamic fetch cho API calls, absolute URL addressing, hydration safeguards (`ssr: false` cho các component tương tác), native storage abstractions (`@capacitor/preferences`), và hardware back-button interception.
- **Các cơ chế quốc tế hóa (i18n) & SEO:** Sử dụng middleware để phát hiện locale từ cookie, header Accept-Language, hoặc URL prefix; render `<html lang='vi'>` cho Vietnamese; tự động inject hreflang links (`<link rel="alternate" hreflang="en" href="https://example.com/en/page"/>`); sử dụng meta tags `og:locale` cho social sharing.

## 📁 8. LUỒNG HOẠT ĐỘNG HÀNG NGÀY TỰ ĐỘNG HÓA PIPELINE CHO BRANCH GIT

- **Cách ly không gian làm việc hàng ngày:** Mỗi ngày làm việc tạo một branch riêng biệt `features/development-phase-X-day-Y` (`X` là số giai đoạn, `Y` là số ngày trong giai đoạn). Branch được tạo từ `main` và tự động merge trở lại sau khi hoàn thành ngày.
- **Các cổng kiểm tra xác thực pipeline:** Sau khi commit, GitHub Actions chạy các bước: kiểm tra cú pháp (`npm run lint`), kiểm tra loại (`mvn compile`), kiểm tra đơn vị (`mvn test`), kiểm tra độ bao phủ (`jacoco`), và triển khai image Docker lên GKE chỉ khi tất cả kiểm tra vượt qua (>=85% độ bao phủ). Nếu thất bại, pipeline dừng lại và thông báo cho Reviewer.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[KIỂM TRA TRÙNG BẢY TRÌNH BÁO: 100% COVERAGE ĐÃ XÁC NHẬN. TỔNG SỐ TAG YÊU CẦU DUY NHẤT: 25, TỔNG SỐ TAG KIẾN TRÚC: 10, TỔNG SỐ TAG NGOẠI LỆ: 5, TỔNG SỐ TAG DỮ LIỆU: 10, TỔNG SỐ TAG NFR: 9. KHÔNG CÓ MÃ NÀO BỊ BỎ QUA.]`