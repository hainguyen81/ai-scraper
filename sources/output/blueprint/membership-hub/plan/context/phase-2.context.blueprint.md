# Giai đoạn 2: <!--PHASE_NAME_START-->phase2_centers_courses_enrollments<!--PHASE_NAME_END--> | Mô tả: Triển khai các dịch vụ quản lý trung tâm, khóa học, ghi danh, khuyến mãi và thông báo, bao gồm thiết kế schema, API, và tuân thủ OWASP, NFR, và mapping tag đầy đủ.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260803132420 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên Giai đoạn Kỹ thuật** | <!--PHASE_NAME_START-->phase2_centers_courses_enrollments<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai các dịch vụ quản lý trung tâm, khóa học, ghi danh, khuyến mãi và thông báo, bao gồm thiết kế schema, API, và tuân thủ OWASP, NFR, và mapping tag đầy đủ. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/03 13:24:20 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu Giai đoạn
Giai đoạn 2 tập trung vào triển khai các dịch vụ backend cho quản lý trung tâm, khóa học, ghi danh, khuyến mãi và thông báo. Các thành phần chính bao gồm:
- **Dịch vụ Trung tâm** (`./sources/backend.centers`) – CRUD, kiểm tra duy nhất cho `taxId`, áp dụng OWASP A01-A10, bảo vệ dữ liệu nhạy cảm, sử dụng prepared statements, kiểm tra đầu vào, logging audit.
- **Dịch vụ Khóa học** (`./sources/backend.courses`) – CRUD, kiểm tra xung đột lịch dạy, áp dụng OWASP A01-A10, bảo vệ dữ liệu nhạy cảm, logging audit.
- **Dịch vụ Ghi danh** (`./sources/backend.enrollments`) – CRUD, kiểm tra khả năng, áp dụng OWASP A01-A10, bảo vệ dữ liệu nhạy cảm, logging audit.
- **Dịch vụ Khuyến mãi & Thông báo** (`./sources/backend.promotions`) – CRUD cho bảng `PROMOTIONS` và `ANNOUNCEMENTS`, áp dụng OWASP A01-A10, bảo vệ dữ liệu nhạy cảm, logging audit.

## 2. Phạm vi Kỹ thuật & Ranh giới Thư mục
| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/backend.centers` | Dịch vụ quản lý trung tâm, bao gồm `CenterResource`, `CenterService`, `CenterRepository`. |
| `./sources/backend.courses` | Dịch vụ quản lý khóa học, bao gồm `CourseResource`, `CourseService`, `CourseRepository`. |
| `./sources/backend.enrollments` | Dịch vụ quản lý ghi danh, bao gồm `EnrollmentResource`, `EnrollmentService`, `EnrollmentRepository`. |
| `./sources/backend.promotions` | Dịch vụ quản lý khuyến mãi và thông báo, bao gồm `PromotionResource`, `AnnouncementResource`, `PromotionService`, `AnnouncementService`. |
| **REST Endpoints** | `GET /api/v1/centers`, `POST /api/v1/centers`, `PUT /api/v1/centers/{id}`, `DELETE /api/v1/centers/{id}`; `GET /api/v1/courses`, `POST /api/v1/courses`, `PUT /api/v1/courses/{id}`, `DELETE /api/v1/courses/{id}`; `GET /api/v1/enrollments`, `POST /api/v1/enrollments`; `POST /api/v1/promotions`, `PUT /api/v1/promotions/{id}`, `POST /api/v1/announcements`, `PUT /api/v1/announcements/{id}`. |

## 3. Hướng dẫn chức năng dành cho Sub-Agent
| Sub-Agent | Trách nhiệm |
| :--- | :--- |
| **Coder** | Triển khai mã nguồn Java/Kotlin, cấu hình Quarkus, bảo mật JWT, mã hóa BCrypt, tạo Dockerfile, triển khai API, bảo vệ dữ liệu, logging audit. |
| **Tester** | Viết và thực thi các test tích hợp, unit, và end‑to‑end cho từng dịch vụ, sử dụng pair syntax `<source file>;<test file>`. |
| **Reviewer** | Thực hiện static code analysis (SonarQube), kiểm tra OWASP, chạy unit test, đảm bảo coverage ≥ 85 %. |
| **Doc** | Biên soạn tài liệu API (OpenAPI), ghi chú trong `./sources/docs.api`, cập nhật DDL, mô tả chi tiết. |

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Tất cả các endpoint CRUD đã triển khai và đáp ứng yêu cầu chức năng.
- DDL cho các bảng `CENTERS`, `COURSES`, `ENROLLMENTS`, `PROMOTIONS`, `ANNOUNCEMENTS` đã được tạo và kiểm tra.
- Tất cả các endpoint đã được kiểm tra unit, integration, và end‑to‑end với coverage ≥ 85 %.
- Đảm bảo tuân thủ OWASP Top 10 (A01-A10) cho toàn bộ dịch vụ.
- Tất cả tag ID trong Phase 2 đã được ánh xạ chính xác (≥ 100 %).
- Đã thực hiện audit log cho mọi thao tác thay đổi dữ liệu.
- Đã triển khai Docker image cho từng dịch vụ, kích thước < 500 MB.

## 5. Nhật ký Thực thi Kiến trúc theo Ngày

### DAY 1: TRIỂN KHAI DỊCH VỤ TRUNG TÂM

#### Sub-Task 1.1: Triển khai endpoint CRUD cho trung tâm, kiểm tra duy nhất cho taxId, áp dụng OWASP A01-A10, bảo vệ dữ liệu nhạy cảm, sử dụng prepared statements, kiểm tra đầu vào, logging audit.
##### Nhân viên phụ trách: Coder
##### Yêu cầu thành phần & kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.centers/org/nlh4j/sources/centers/CenterResource.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-004], [DAT-003], [NFR-002], [NFR-004]<!--END_TAGS-->

### DAY 2: TRIỂN KHAI DỊCH VỤ KHÓA HỌC VÀ GHI DANH

#### Sub-Task 2.1: Triển khai endpoint CRUD cho khóa học, kiểm tra xung đột lịch dạy, áp dụng OWASP A01-A10, bảo vệ dữ liệu nhạy cảm, logging audit.
##### Nhân viên phụ trách: Coder
##### Yêu cầu thành phần & kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.courses/org/nlh4j/sources/courses/CourseResource.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-007], [DAT-004], [NFR-002], [NFR-004]<!--END_TAGS-->

#### Sub-Task 2.2: Triển khai endpoint CRUD cho ghi danh, kiểm tra khả năng, áp dụng OWASP A01-A10, bảo vệ dữ liệu nhạy cảm, logging audit.
##### Nhân viên phụ trách: Coder
##### Yêu cầu thành phần & kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.enrollments/org/nlh4j/sources/enrollments/EnrollmentResource.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-010], [DAT-005], [NFR-002], [NFR-004]<!--END_TAGS-->

### DAY 3: TRIỂN KHAI DỊCH VỤ KHƯƠNG MÃ & THÔNG BÁO

#### Sub-Task 3.1: Triển khai endpoint CRUD cho khuyến mãi và thông báo, áp dụng OWASP A01-A10, bảo vệ dữ liệu nhạy cảm, logging audit.
##### Nhân viên phụ trách: Coder
##### Yêu cầu thành phần & kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.promotions/org/nlh4j/sources/promotions/PromotionResource.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-017], [REQ-018], [DAT-009], [NFR-002], [NFR-004]<!--END_TAGS-->

## Database Schema DDL SQL Specification

```sql
-- [DAT-003] Centers
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(20) NOT NULL UNIQUE,
    contactPhone VARCHAR(30),
    contactEmail VARCHAR(255)
);
```

```sql
-- [DAT-004] Courses
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

```sql
-- [DAT-005] Enrollments
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE(studentId, courseId)
);
```

```sql
-- [DAT-009] Promotions & Announcements
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

## API and Event Routing Contracts

- `GET /api/v1/centers` – trả về danh sách trung tâm.
- `POST /api/v1/centers` – tạo trung tâm mới, kiểm tra trùng `taxId`.
- `PUT /api/v1/centers/{id}` – cập nhật trung tâm.
- `DELETE /api/v1/centers/{id}` – xóa trung tâm.
- `GET /api/v1/courses` – trả về danh sách khóa học.
- `POST /api/v1/courses` – tạo khóa học, kiểm tra xung đột lịch dạy.
- `PUT /api/v1/courses/{id}` – cập nhật khóa học.
- `DELETE /api/v1/courses/{id}` – xóa khóa học.
- `GET /api/v1/enrollments` – trả về danh sách ghi danh.
- `POST /api/v1/enrollments` – ghi danh vào khóa học, tự động tạo tài khoản học viên nếu chưa tồn tại.
- `POST /api/v1/promotions` – tạo khuyến mãi mới.
- `PUT /api/v1/promotions/{id}` – cập nhật khuyến mãi.
- `POST /api/v1/announcements` – tạo thông báo mới.
- `PUT /api/v1/announcements/{id}` – cập nhật thông báo.