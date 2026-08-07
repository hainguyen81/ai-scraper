# Giai đoạn 3: <!--PHASE_NAME_START-->Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807024254 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng toàn bộ mô-đun quản lý khóa học, bao gồm việc triển khai controller, service và service phân công giáo viên, đồng thời thiết lập schema dữ liệu, API contract và kiểm tra tính nhất quán lịch học. Các chức năng chính bao gồm: hiển thị danh sách khóa học, tạo/ cập nhật khóa học với kiểm tra xung đột lịch, và gán/ rút giáo viên cho khóa học. Tất cả các endpoint đều tuân thủ chuẩn REST, bảo mật JWT, và áp dụng OWASP Top‑10. Phần triển khai còn bao gồm việc viết tài liệu kiến trúc, kiểm thử, và chuẩn bị containerization cho môi trường GKE.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 07:35:34 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và mục tiêu thực thi giai đoạn
Giai đoạn 3 yêu cầu triển khai toàn bộ mô-đun quản lý khóa học, bao gồm:
- Xây dựng **CourseController** để cung cấp danh sách, tạo, cập nhật và gán giáo viên cho khóa học.
- Xây dựng **CourseService** để xử lý nghiệp vụ tạo/ cập nhật khóa học, đồng thời kiểm tra xung đột lịch với giáo viên đã được phân công.
- Xây dựng **CourseTeacherService** để thực hiện gán/rút giáo viên vào khóa học và gửi thông báo push khi có thay đổi.
- Định nghĩa schema **COURSES** trong PostgreSQL, bao gồm các trường khóa học, ngày bắt đầu/ kết thúc, giáo viên, và giới hạn số học viên.
- Định nghĩa API contract cho các endpoint: `GET /api/v1/courses`, `POST /api/v1/courses`, `PUT /api/v1/courses/{courseId}/teacher/{teacherId}`.
- Đảm bảo tất cả các endpoint được bảo vệ bằng JWT, áp dụng RBAC, và tuân thủ OWASP Top‑10 (SQL injection, XSS, CSRF, etc.).
- Viết tài liệu kiến trúc, schema, và hướng dẫn triển khai containerization cho môi trường GKE.
- Kiểm thử unit, integration, và E2E với coverage 100% cho các yêu cầu REQ-007, REQ-008, REQ-009.

## 2. Phạm vi kỹ thuật & ranh giới thư mục (Files, paths, và endpoints)
- **Thư mục chính**: `./sources/backend/courses/`
- **File controller**: `./sources/backend/courses/CourseController.java`
- **File service**: `./sources/backend/courses/CourseService.java`
- **File teacher service**: `./sources/backend/courses/CourseTeacherService.java`
- **Schema file**: `./sources/backend/courses/CourseSchema.sql`
- **Endpoints**:
  - `GET /api/v1/courses` – trả về danh sách khóa học.
  - `POST /api/v1/courses` – tạo khóa học mới.
  - `PUT /api/v1/courses/{courseId}` – cập nhật thông tin khóa học.
  - `PUT /api/v1/courses/{courseId}/teacher/{teacherId}` – gán giáo viên cho khóa học.

## 3. Hướng dẫn chức năng của các đại lý phụ
- **Coder**: Phát triển mã nguồn Java cho controller, service, và repository. Không viết test, manifest, hoặc tài liệu.
- **Tester**: Viết test unit, integration, và E2E cho các lớp Java. Nếu không có file nguồn cụ thể, ghi `INTEGRATION_SCOPE;./sources/backend/tests/integration/CourseWorkflowTest.java`.
- **Reviewer**: Kiểm tra biên dịch, phân tích tĩnh, và vá lỗi bảo mật OWASP. Đảm bảo mã tuân thủ SonarQube.
- **Doc**: Viết tài liệu kỹ thuật, schema, và hướng dẫn triển khai. Tạo file `./sources/docs/courses_architecture.md`.
- **Docker**: Xây dựng Dockerfile đa‑stage cho backend, tối ưu kích thước, và chuẩn bị image cho GKE.
- **GCP**: Đẩy image lên Artifact Registry và triển khai lên GKE.
- **GKE**: Viết manifest deployment, service, HPA, và cấu hình networking cho backend.

## 4. Định nghĩa Hoàn thành (DoD)
- Tất cả các endpoint REQ-007, REQ-008, REQ-009 được triển khai và hoạt động đúng theo API contract.
- Kiểm thử unit, integration, và E2E đạt 100% coverage cho các yêu cầu này.
- Mã nguồn tuân thủ OWASP Top‑10 và đạt SonarQube quality gate.
- Tất cả tag ID (REQ-007, REQ-008, REQ-009, ARC-003, DAT-004) được ánh xạ và ghi lại trong logs.
- Tài liệu kiến trúc, schema, và hướng dẫn triển khai được hoàn thiện và lưu trong `./sources/docs/`.
- Docker image có kích thước < 500 MB và được đẩy lên Artifact Registry.
- Manifest GKE triển khai thành công với HPA và autoscaling.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->XÂY DỰNG CONTROLLER DANH SÁCH KHÓA HỌC<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 1.1: Triển khai CourseController để hiển thị danh sách khóa học và hỗ trợ CRUD.
##### Được Giao Cho: Coder
##### Đường Dẫn Mục Tiêu: `./sources/backend/courses/CourseController.java`
##### Thẻ Truyền Tính: <!--START_TAGS-->[ARC-003], [REQ-007], [DAT-004]<!--END_TAGS-->
##### Hướng Dẫn Công Nghệ Chi Tiết:
- Xây dựng lớp `CourseController` với các phương thức:
  - `@GetMapping("/api/v1/courses")` trả về danh sách khóa học.
  - `@PostMapping("/api/v1/courses")` tạo khóa học mới.
  - `@PutMapping("/api/v1/courses/{courseId}")` cập nhật khóa học.
- Sử dụng `CourseService` để thực hiện nghiệp vụ.
- Bảo vệ endpoint bằng `@PreAuthorize` theo RBAC (System Admin, Center Admin).
- Đảm bảo trả về mã lỗi 400/409 khi có dữ liệu trùng lặp hoặc xung đột.
- Kiểm tra dữ liệu đầu vào với `@Valid` và `BindingResult`.
- Thêm logging với SLF4J, ghi lại userId, action, và thời gian.

```json
// GET /api/v1/courses
{
  "courses": [
    {
      "courseId": "uuid",
      "title": "Lập trình Java nâng cao",
      "description": "Khóa học về Quarkus và Kubernetes",
      "startDate": "2026-09-01",
      "endDate": "2026-12-31",
      "teacherId": "a1b2c3d4-...",
      "maxStudents": 20
    }
  ]
}
```

```json
// POST /api/v1/courses
{
  "title": "Lập trình Java nâng cao",
  "description": "Khóa học về Quarkus và Kubernetes",
  "startDate": "2026-09-01",
  "endDate": "2026-12-31",
  "teacherId": "a1b2c3d4-...",
  "maxStudents": 20
}
```

```json
// PUT /api/v1/courses/{courseId}
{
  "title": "Lập trình Java nâng cao Updated",
  "description": "Updated description",
  "startDate": "2026-09-01",
  "endDate": "2026-12-31",
  "teacherId": "a1b2c3d4-...",
  "maxStudents": 25
}
```

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

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->XÂY DỰNG LOGIC TẠO/ CẬP NHẬT KHÓA HỌC<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 2.1: Triển khai CourseService để xử lý tạo và cập nhật khóa học, kiểm tra xung đột lịch.
##### Được Giao Cho: Coder
##### Đường Dẫn Mục Tiêu: `./sources/backend/courses/CourseService.java`
##### Thẻ Truyền Tính: <!--START_TAGS-->[REQ-008], [DAT-004]<!--END_TAGS-->
##### Hướng Dẫn Công Nghệ Chi Tiết:
- Phương thức `createCourse(CourseDto)`:
  - Kiểm tra xung đột lịch với giáo viên hiện có: truy vấn `SELECT * FROM COURSES WHERE teacherId = :teacherId AND ((startDate <= :endDate AND endDate >= :startDate))`.
  - Nếu có xung đột, trả về lỗi 409 với thông báo chi tiết.
  - Nếu không, lưu bản ghi vào bảng `COURSES`.
- Phương thức `updateCourse(courseId, CourseDto)`:
  - Kiểm tra xung đột lịch tương tự.
  - Cập nhật các trường được cung cấp.
- Sử dụng `@Transactional` để đảm bảo atomicity.
- Thêm logging và exception handling cho `DataIntegrityViolationException`.

```json
// POST /api/v1/courses
{
  "title": "Lập trình Java nâng cao",
  "description": "Khóa học về Quarkus và Kubernetes",
  "startDate": "2026-09-01",
  "endDate": "2026-12-31",
  "teacherId": "a1b2c3d4-...",
  "maxStudents": 20
}
```

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

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->XÂY DỰNG GÁN/ RÚT GIÁO VIÊN VÀ GỬI THÔNG BÁO<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 3.1: Triển khai CourseTeacherService để gán/rút giáo viên vào khóa học và gửi thông báo push.
##### Được Giao Cho: Coder
##### Đường Dẫn Mục Tiêu: `./sources/backend/courses/CourseTeacherService.java`
##### Thẻ Truyền Tính: <!--START_TAGS-->[REQ-009], [ARC-003], [DAT-004]<!--END_TAGS-->
##### Hướng Dẫn Công Nghệ Chi Tiết:
- Phương thức `assignTeacher(courseId, teacherId)`:
  - Kiểm tra tồn tại khóa học và giáo viên.
  - Cập nhật trường `teacherId` trong bảng `COURSES`.
  - Tạo bản ghi mapping (nếu có bảng mapping riêng) hoặc cập nhật trực tiếp.
  - Gửi thông báo push tới giáo viên qua `NotificationService`.
- Phương thức `removeTeacher(courseId)`:
  - Đặt `teacherId` thành NULL hoặc giá trị mặc định.
  - Gửi thông báo rút quyền.
- Sử dụng `@Transactional` và `@PreAuthorize` để bảo vệ quyền.
- Thêm logging và exception handling cho `EntityNotFoundException`.

```json
// PUT /api/v1/courses/{courseId}/teacher/{teacherId}
{
  "action": "assign"
}
```

```json
// PUT /api/v1/courses/{courseId}/teacher/{teacherId}
{
  "action": "remove"
}
```

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