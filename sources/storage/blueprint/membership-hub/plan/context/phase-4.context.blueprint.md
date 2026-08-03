# Giai đoạn 4: <!--PHASE_NAME_START-->attendance_enrollment_module<!--PHASE_NAME_END--> | Mô tả: Triển khai module ghi danh học viên, điểm danh QR, và quản lý thẻ hội viên với service điểm danh QR idempotent, xử lý ngoại lệ network và duplicate scans, và tích hợp với hệ thống thông báo

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260803053505 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên kỹ thuật giai đoạn** | <!--PHASE_NAME_START-->attendance_enrollment_module<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai module ghi danh học viên, điểm danh QR, và quản lý thẻ hội viên với service điểm danh QR idempotent, xử lý ngoại lệ network và duplicate scans, và tích hợp với hệ thống thông báo |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/03 05:35:05 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu giai đoạn

Giai đoạn này tập trung vào việc xây dựng module quản lý ghi danh, điểm danh và thẻ hội viên với các chức năng chính:

- Triển khai schema cơ sở dữ liệu cho bảng Enrollments, Attendance và StudentCards với các ràng buộc toàn vẹn dữ liệu
- Xây dựng dịch vụ ghi danh học viên vào khóa học với validation nghiêm ngặt
- Triển khai API điểm danh QR idempotent đảm bảo không có bản ghi trùng lặp
- Thiết lập cơ chế xử lý ngoại lệ network và duplicate scans
- Triển khai chức năng quản lý thẻ hội viên với tính năng gia hạn
- Tích hợp với hệ thống thông báo tự động cho các sự kiện ghi danh và điểm danh
- Triển khai hệ thống logging kiểm toán đáp ứng các tiêu chuẩn bảo mật doanh nghiệp

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép

**Thư mục và tệp được phép:**
- `./sources/backend.membershiphub.attendance/enrollments.sql` - DDL schema cho bảng Enrollments
- `./sources/backend.membershiphub.attendance/attendances.sql` - DDL schema cho bảng Attendance
- `./sources/backend.membershiphub.attendance/studentcards.sql` - DDL schema cho bảng StudentCards
- `./sources/backend.membershiphub.attendance/enrollment-service.java` - Dịch vụ chính quản lý ghi danh và điểm danh
- `./sources/backend.membershiphub.attendance/studentcard-service.java` - Dịch vụ quản lý thẻ hội viên

**Endpoint API:**
- `GET /api/v1/courses/browse` - Lấy danh sách khóa học có sẵn cho học viên
- `POST /api/v1/enrollments` - Ghi danh học viên vào khóa học
- `POST /api/v1/attendance/scan` - Quét mã QR điểm danh
- `GET /api/v1/studentcards/{studentId}` - Lấy thông tin thẻ hội viên
- `POST /api/v1/studentcards/{studentId}/renew` - Gia hạn thẻ hội viên

## 3. Chỉ đạo chức năng cho Sub-Agent chuyên dụng

**Coder:** Triển khai mã nguồn Java/Quarkus với tuân thủ SOLID, sử dụng JPA/Hibernate cho persistence, áp dụng @Valid cho validation, @Transactional cho các thao tác ghi. Đảm bảo logic điểm danh QR idempotent hoạt động chính xác và xử lý ngoại lệ network đúng cách.

**Tester:** Xây dựng bộ kiểm thử JUnit 5 và Testcontainers với độ phủ mã ≥85%, kiểm thử happy path và các scenario lỗi network, duplicate scans, và validation.

**Reviewer:** Thực hiện phân tích tĩnh mã nguồn, kiểm tra tuân thủ OWASP Top 10, đảm bảo không có lỗ hổng SQL injection hoặc XSS trong các API điểm danh và ghi danh.

**Doc:** Biên soạn tài liệu kỹ thuật đầy đủ bao gồm API documentation với OpenAPI, schema documentation và hướng dẫn triển khai cho module ghi danh và điểm danh.

## 4. Định nghĩa hoàn thành (DoD) cho giai đoạn

- ✅ 100% các requirement [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015] được triển khai đầy đủ
- ✅ Schema database [DAT-005], [DAT-006], [DAT-007] được tạo thành công với tất cả ràng buộc
- ✅ Logic điểm danh QR idempotent hoạt động chính xác
- ✅ Xử lý ngoại lệ network và duplicate scans [EXC-001], [EXC-002]
- ✅ Tuân thủ các tiêu chuẩn bảo mật [NFR-001], [NFR-003]
- ✅ Độ phủ kiểm thử ≥85% cho tất cả các dịch vụ
- ✅ 100% các Tag ID được ánh xạ và kiểm tra

## 5. NHẬT KÝ THỰC THI KIẾN TRÚC THEO NGÀY

### NGÀY 7: TRIỂN KHAI SERVICE GHI DANH HỌC VIÊN VÀ ĐIỂM DANH QR

#### SUB-TASK 7.1: Triển khai schema cơ sở dữ liệu Enrollments, Attendance và StudentCards
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.attendance/enrollments.sql`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[DAT-005]<!--END_TAGS-->

#### SUB-TASK 7.2: Triển khai EnrollmentService với các phương thức ghi danh và điểm danh QR idempotent
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.attendance/enrollment-service.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [ARC-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003]<!--END_TAGS-->

### NGÀY 8: TRIỂN KHAI SERVICE QUẢN LÝ THẺ HỘI VIÊN VÀ GIA HẠN

#### SUB-TASK 8.1: Triển khai StudentCardService với các phương thức quản lý thẻ và gia hạn
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.attendance/studentcard-service.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [NFR-003]<!--END_TAGS-->

### NGÀY 9: VIẾT BỘ KIỂM TRA TÍCH HỢP CHO GHI DANH, ĐIỂM DANH, VÀ THẺ

#### SUB-TASK 9.1: Kiểm thử tích hợp cho các API ghi danh, điểm danh và quản lý thẻ
##### Sub-Agent được chỉ định: Tester
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.attendance/enrollment-service.java;./sources/backend.membershiphub.attendance/enrollmentservice-integration-test.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [ARC-007], [EXC-001], [EXC-002]<!--END_TAGS-->