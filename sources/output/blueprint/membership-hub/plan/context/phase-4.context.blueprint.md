# Giai đoạn 4: <!--PHASE_NAME_START-->Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, và cài đặt hệ thống<!--PHASE_NAME_END-->



## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807073534 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, và cài đặt hệ thống<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này thực hiện toàn bộ chức năng ghi danh học viên, điểm danh qua mã QR, quản lý thẻ hội viên, gửi thông báo push và Zalo, quản lý khuyến mãi, thông báo, và cấu hình hệ thống. Các thành phần backend được triển khai theo mô hình CQRS, sử dụng Kafka cho sự kiện, và bảo mật JWT, RBAC. Các bảng dữ liệu chính gồm ENROLLMENTS, ATTENDANCE, NOTIFICATIONS, STUDENTCARDS, PROMOTIONS, ANNOUNCEMENTS, SYSTEMSETTINGS. Các API REST được bảo vệ bằng JWT và kiểm tra quyền. Các exception handler được triển khai cho mạng, duplicate, và lỗi giao hàng.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 07:35:34 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |



## 1. Phạm vi thực thi và mục tiêu

Giai đoạn 4 tập trung vào việc triển khai các dịch vụ backend chính: Enrollment, Attendance, Notification, Membership. Mỗi dịch vụ chịu trách nhiệm cho một phần của quy trình học tập: đăng ký khóa học, ghi danh qua QR, gửi thông báo, và quản lý thẻ hội viên, khuyến mãi, thông báo, cài đặt hệ thống. Các thành phần được triển khai theo kiến trúc micro‑service, sử dụng Quarkus, PostgreSQL, Kafka, Redis, FCM/APNs, Zalo API, và Docker/Kubernetes. Mọi API đều tuân thủ JWT, RBAC, và OWASP Top‑10. Các exception handler được triển khai để xử lý mạng, duplicate, và lỗi giao hàng. Tất cả dữ liệu được ghi log và audit theo NFR‑006. Độ trễ trung bình của API phải dưới 200 ms (NFR‑001), bảo mật TLS 1.3 (NFR‑003), và có khả năng mở rộng theo CPU > 70 % (NFR‑004).  

## 2. Phạm vi kỹ thuật & ranh giới thư mục

| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/backend/enrollment/` | Các lớp controller, service, repository cho đăng ký khóa học. |
| `./sources/backend/attendance/` | Dịch vụ điểm danh QR. |
| `./sources/backend/notifications/` | Dịch vụ gửi thông báo push và Zalo. |
| `./sources/backend/membership/` | Dịch vụ quản lý thẻ hội viên, khuyến mãi, thông báo, cài đặt hệ thống. |
| `./sources/docs/` | Tài liệu kỹ thuật, sơ đồ kiến trúc, quy trình triển khai. |
| Endpoints | `POST /api/v1/enrollments`<br>`POST /api/v1/attendance/scan`<br>`POST /api/v1/notifications`<br>`GET /api/v1/membership/{studentId}/card`<br>`POST /api/v1/membership/{studentId}/renew`<br>`POST /api/v1/promotions`<br>`POST /api/v1/announcements` |

## 3. Hướng dẫn chức năng của các đại lý phụ

| Đại lý | Mô tả |
| :--- | :--- |
| **Coder** | Phát triển mã nguồn Java cho backend services, không viết test hoặc manifest. |
| **Tester** | Viết test JUnit, integration, E2E, performance. Không sửa code production. |
| **Doc** | Viết tài liệu kỹ thuật, sơ đồ, quy trình, lưu trong `./sources/docs/`. |
| **Reviewer** | Kiểm tra compile, static analysis, OWASP, SonarQube. |
| **Docker** | Xây dựng Dockerfile multi‑stage, tối ưu image, push lên DockerHub. |
| **GCP** | Đẩy image lên Artifact Registry, triển khai trên Cloud Run. |
| **GKE** | Xây dựng manifest, HPA, Helm chart, triển khai trên GKE. |

## 4. Định nghĩa DoD

- Tất cả API đã triển khai trả về đúng theo contract, lỗi 4xx/5xx được xử lý.  
- Coverage unit/integration 100 % cho các yêu cầu [REQ‑010]…[REQ‑018].  
- OWASP Top‑10 được kiểm tra, không có lỗ hổng.  
- Tất cả tag ID được map 100 %.  
- Độ trễ trung bình < 200 ms, bảo mật TLS 1.3, logging 1 year.  
- Image Docker < 500 MB, HPA tự động scale.  

## 5. Lịch trình thực thi ngày theo ngày

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->XÂY DỰNG CONTROLLER GHI DANH KHÓA HỌC<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 1.1: Triển khai EnrollmentController để xử lý đăng ký khóa học và tạo tài khoản sinh viên nếu thiếu

##### Assigned Sub-Agent: Coder

##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/backend/enrollment/EnrollmentController.java
* **Traceability Tag Tokens**: <!--START_TAGS-->[ARC-004], [REQ-010], [DAT-005]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: 
  - Thiết kế lớp `EnrollmentController` với các phương thức REST: `POST /api/v1/enrollments`, `GET /api/v1/enrollments/{studentId}`.
  - Sử dụng `EnrollmentService` để thực thi nghiệp vụ đăng ký, kiểm tra tồn tại sinh viên, tạo tài khoản nếu chưa có, cập nhật vai trò thành `Student`.
  - Bảo vệ endpoint bằng `@PreAuthorize` với quyền `ROLE_STUDENT` hoặc `ROLE_ADMIN`.
  - Xử lý lỗi 400 khi dữ liệu thiếu, 409 khi đã đăng ký, 404 khi khóa học không tồn tại.
  - Ghi log chi tiết với SLF4J: userId, action, timestamp, status.

**Database Schema DDL SQL Specification [DAT-005]**:
```sql
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW()
);
```

**API and Event Routing Contracts [REQ-010]**:
```json
// POST /api/v1/enrollments
{
  "studentId": "a1b2c3d4-...",
  "courseId": "e5f6g7h8-..."
}
```

#### 📝 NHIỆM VỤ 1.2: Tạo tài liệu kiến trúc chi tiết cho giai đoạn 4

##### Assigned Sub-Agent: Doc

##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/docs/enrollment_phase4_architecture.md
* **Traceability Tag Tokens**: <!--START_TAGS-->[ARC-004], [ARC-005], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [EXC-001], [EXC-002], [EXC-003], [EXC-005], [NFR-001], [NFR-003], [NFR-004], [NFR-006], [NFR-009]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: 
  - Soạn thảo tài liệu `enrollment_phase4_architecture.md` bao gồm: mô tả tổng quan, sơ đồ kiến trúc, mô hình dữ liệu, luồng API, quy trình triển khai, quy tắc bảo mật, và kế hoạch kiểm thử.
  - Đảm bảo tài liệu phản ánh đầy đủ các thành phần: Enrollment, Attendance, Notification, Membership, và các bảng dữ liệu tương ứng.
  - Ghi chú các điểm quan trọng: tính nhất quán dữ liệu, idempotency, bảo mật JWT, và quy trình khôi phục khi lỗi.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->XÂY DỰNG SERVICE GHI DANH KHÓA HỌC<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 2.1: Triển khai EnrollmentService để xử lý đăng ký khóa học và cập nhật vai trò

##### Assigned Sub-Agent: Coder

##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/backend/enrollment/EnrollmentService.java
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-011], [DAT-005], [ARC-005]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: 
  - Phương thức `registerEnrollment(StudentDto, CourseDto)` thực thi logic: kiểm tra tồn tại sinh viên, tạo tài khoản nếu chưa có, kiểm tra khóa học tồn tại, kiểm tra đã đăng ký, ghi bản ghi vào bảng ENROLLMENTS.
  - Sử dụng `@Transactional` để đảm bảo atomicity.
  - Xử lý ngoại lệ `DataIntegrityViolationException` và trả về lỗi 409.
  - Gửi thông báo qua `NotificationService` và cập nhật `StudentCards` nếu cần.
  - Đảm bảo bảo mật bằng prepared statements và kiểm tra quyền.

**Database Schema DDL SQL Specification [DAT-005]**:
```sql
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW()
);
```

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->XÂY DỰNG SERVICE ĐIỂM DANH QR<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 3.1: Triển khai AttendanceService để xử lý điểm danh QR và đảm bảo tính bất biến

##### Assigned Sub-Agent: Coder

##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/backend/attendance/AttendanceService.java
* **Traceability Tag Tokens**: <!--START_TAGS-->[ARC-007], [REQ-012], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: 
  - Phương thức `scanAttendance(AttendanceDto)` nhận studentId, courseId, qrCodeData, timestamp.
  - Kiểm tra tồn tại sinh viên, khóa học, và mối quan hệ học viên-khoá.
  - Kiểm tra duplicate: truy vấn `SELECT 1 FROM ATTENDANCE WHERE studentId = :studentId AND courseId = :courseId AND attendanceDate = CURRENT_DATE`.
  - Nếu duplicate, trả về success với flag `alreadyRecorded: true`.
  - Nếu chưa, ghi bản ghi vào bảng ATTENDANCE với timestamp hiện tại.
  - Xử lý ngoại lệ mạng: nếu không kết nối, lưu tạm thời và retry khi kết nối được (EXC-001).
  - Đảm bảo idempotency và bảo mật bằng prepared statements.
  - Ghi log chi tiết.

**Database Schema DDL SQL Specification [DAT-006]**:
```sql
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW()
);
```

**API and Event Routing Contracts [REQ-012]**:
```json
// POST /api/v1/attendance/scan
{
  "studentId": "a1b2c3d4-...",
  "courseId": "e5f6g7h8-...",
  "qrCodeData": "course:e5f6g7h8-...|date:2026-08-07"
}
```

**Phase Localized Exception Handlers [EXC-001]**:
- Mất mạng khi quét QR: Khi sinh viên quét QR nhưng không có kết nối mạng, khi kết nối được khôi phục, ứng dụng sẽ tự động gửi lại yêu cầu điểm danh; dịch vụ sẽ đảm bảo chỉ ghi một bản ghi điểm danh duy nhất.

**Phase Localized Exception Handlers [EXC-002]**:
- Điểm danh trùng lặp: Nếu cùng một sinh viên quét cùng một QR nhiều lần trong ngày, hệ thống sẽ phát hiện duplicate, trả về success với cờ ‘alreadyRecorded’ và không tạo thêm hàng.

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->XÂY DỰNG SERVICE THÔNG BÁO<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 4.1: Triển khai NotificationService để gửi thông báo push và Zalo

##### Assigned Sub-Agent: Coder

##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/backend/notifications/NotificationService.java
* **Traceability Tag Tokens**: <!--START_TAGS-->[ARC-008], [REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: 
  - Phương thức `sendNotification(NotificationDto)` tạo bản ghi NOTIFICATIONS, đẩy push qua FCM/APNs, gửi tin nhắn Zalo.
  - Xử lý lỗi giao hàng: nếu push thất bại, ghi log, lên lịch retry tối đa 3 lần (EXC-003).
  - Bảo mật: xác thực token, kiểm tra quyền.
  - Đảm bảo idempotency và logging.

**Database Schema DDL SQL Specification [DAT-008]**:
```sql
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID REFERENCES USERS(userId),
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
```

**API and Event Routing Contracts [REQ-016]**:
```json
// POST /api/v1/notifications
{
  "userId": "a1b2c3d4-...",
  "groupZalo": "hoc_vien_hn",
  "message": "Bạn đã được ghi danh vào khóa học mới."
}
```

**Phase Localized Exception Handlers [EXC-003]**:
- Giao hàng thông báo thất bại: Nếu push notification không thể gửi (ví dụ: token thiết bị không hợp lệ), hệ thống ghi log lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu là thất bại.

### 🌤️ NGÀY 5: <!--DAY_HEADER_START-->XÂY DỰNG SERVICE THẺ HỘI VIÊN VÀ CÀI ĐẶT HỆ THỐNG<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 5.1: Triển khai MembershipController để quản lý thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống

##### Assigned Sub-Agent: Coder

##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/backend/membership/MembershipController.java
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: 
  - Phương thức `getStudentCard(studentId)` trả về thông tin thẻ, `renewCard(studentId, days)` gia hạn thẻ, `createPromotion(PromotionDto)`, `createAnnouncement(AnnouncementDto)`, `updateSystemSetting(SystemSettingDto)`.
  - Kiểm tra quyền: `ROLE_STUDENT` cho thẻ, `ROLE_ADMIN` cho khuyến mãi, thông báo, cài đặt.
  - Cập nhật bảng STUDENTCARDS, PROMOTIONS, ANNOUNCEMENTS, SYSTEMSETTINGS.
  - Xử lý ngoại lệ khôi phục hệ thống (EXC-005) khi dịch vụ không khả dụng.

**Database Schema DDL SQL Specification [DAT-007]**:
```sql
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);
```

**Database Schema DDL SQL Specification [DAT-009]**:
```sql
CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);
```

**Database Schema DDL SQL Specification [DAT-011]**:
```sql
CREATE TABLE SYSTEMSETTINGS (
    settingKey VARCHAR(50) PRIMARY KEY,
    settingValue TEXT NOT NULL,
    description TEXT
);
```

**Phase Localized Exception Handlers [EXC-005]**:
- Khôi phục hệ thống sau sự cố: Nếu dịch vụ không khả dụng, khi khôi phục, các lần quét điểm danh chờ xử lý được xử lý theo thứ tự FIFO, và người dùng nhận được thông báo về các sự kiện đã khôi phục.

**API and Event Routing Contracts [REQ-014]**:
```json
// GET /api/v1/membership/{studentId}/card
// trả về thẻ hội viên với daysRemaining
```

**API and Event Routing Contracts [REQ-015]**:
```json
// POST /api/v1/membership/{studentId}/renew
{
  "days": 30
}
```

**API and Event Routing Contracts [REQ-017]**:
```json
// POST /api/v1/promotions
{
  "code": "SUMMER20",
  "discountPercent": 20,
  "startDate": "2026-06-01",
  "endDate": "2026-08-31",
  "description": "Giảm giá 20% cho tất cả khóa học."
}
```

**API and Event Routing Contracts [REQ-018]**:
```json
// POST /api/v1/announcements
{
  "title": "Thông báo nghỉ lễ",
  "content": "Trung tâm nghỉ lễ từ 01/09 đến 05/09.",
  "startDate": "2026-08-31",
  "endDate": "2026-09-05"
}
```

**API and Event Routing Contracts [REQ-016]**:
```json
// POST /api/v1/notifications
{
  "userId": "a1b2c3d4-...",
  "groupZalo": "hoc_vien_hn",
  "message": "Bạn đã được ghi danh vào khóa học mới."
}
```