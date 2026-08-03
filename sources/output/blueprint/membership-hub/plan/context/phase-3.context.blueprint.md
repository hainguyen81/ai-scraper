# Giai đoạn 3: <!--PHASE_NAME_START-->course_management_module<!--PHASE_NAME_END--> | Mô tả: Triển khai module quản lý khóa học bao gồm danh sách khóa học công khai, CRUD khóa học với kiểm tra xung đột lịch giảng, gán giáo viên, và tích hợp với RBAC cho Manager và System/Center Admin

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260803053505 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên kỹ thuật giai đoạn** | <!--PHASE_NAME_START-->course_management_module<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai module quản lý khóa học bao gồm danh sách khóa học công khai, CRUD khóa học với kiểm tra xung đột lịch giảng, gán giáo viên, và tích hợp với RBAC cho Manager và System/Center Admin |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/03 05:35:05 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu giai đoạn

Giai đoạn này tập trung vào việc xây dựng module quản lý khóa học với các chức năng chính:

- Triển khai schema cơ sở dữ liệu cho bảng Courses với các ràng buộc toàn vẹn dữ liệu
- Xây dựng dịch vụ CRUD đầy đủ cho quản lý khóa học với validation nghiêm ngặt
- Triển khai API danh sách khóa học công khai cho tất cả người dùng đã xác thực
- Thiết lập cơ chế kiểm tra xung đột lịch giảng để đảm bảo giáo viên không bị trùng lịch
- Triển khai chức năng gán giáo viên vào khóa học với thông báo tự động
- Tích hợp với RBAC cho Manager và System/Center Admin với phân quyền chi tiết
- Triển khai hệ thống logging kiểm toán đáp ứng các tiêu chuẩn bảo mật doanh nghiệp

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép

**Thư mục và tệp được phép:**
- `./sources/backend.membershiphub.course/courses.sql` - DDL schema cho bảng Courses
- `./sources/backend.membershiphub.course/course-service.java` - Dịch vụ chính quản lý khóa học
- `./sources/backend.membershiphub.course/course-repository.java` - Repository JPA cho Courses
- `./sources/backend.membershiphub.course/course-controller.java` - REST Controller cho API khóa học

**Endpoint API:**
- `GET /api/v1/courses` - Lấy danh sách tất cả khóa học (công khai)
- `POST /api/v1/courses` - Tạo khóa học mới (chỉ System Admin và Center Admin)
- `PUT /api/v1/courses/{courseId}` - Cập nhật thông tin khóa học (chỉ System Admin và Center Admin)
- `DELETE /api/v1/courses/{courseId}` - Xóa mềm khóa học (chỉ System Admin và Center Admin)
- `POST /api/v1/courses/{courseId}/teachers/{teacherId}` - Gán giáo viên vào khóa học (chỉ System Admin)

## 3. Chỉ đạo chức năng cho Sub-Agent chuyên dụng

**Coder:** Triển khai mã nguồn Java/Quarkus với tuân thủ SOLID, sử dụng JPA/Hibernate cho persistence, áp dụng @Valid cho validation, @PreAuthorize cho phân quyền, và @Transactional cho các thao tác ghi. Đảm bảo logic kiểm tra xung đột lịch giảng hoạt động chính xác.

**Tester:** Xây dựng bộ kiểm thử JUnit 5 và Testcontainers với độ phủ mã ≥85%, kiểm thử happy path và các scenario lỗi validation, xung đột lịch giảng, và phân quyền.

**Reviewer:** Thực hiện phân tích tĩnh mã nguồn, kiểm tra tuân thủ OWASP Top 10, đảm bảo không có lỗ hổng SQL injection hoặc XSS trong các API khóa học.

**Doc:** Biên soạn tài liệu kỹ thuật đầy đủ bao gồm API documentation với OpenAPI, schema documentation và hướng dẫn triển khai cho module khóa học.

## 4. Định nghĩa hoàn thành (DoD) cho giai đoạn

- ✅ 100% các requirement [REQ-007], [REQ-008], [REQ-009] được triển khai đầy đủ
- ✅ Schema database [DAT-004] được tạo thành công với tất cả ràng buộc
- ✅ Logic kiểm tra xung đột lịch giảng hoạt động chính xác
- ✅ Xử lý validation đầu vào và xung đột lịch giáo viên
- ✅ Tuân thủ các tiêu chuẩn bảo mật [NFR-001], [NFR-002]
- ✅ Độ phủ kiểm thử ≥85% cho tất cả các dịch vụ
- ✅ 100% các Tag ID được ánh xạ và kiểm tra

## 5. NHẬT KÝ THỰC THI KIẾN TRÚC THEO NGÀY

### NGÀY 5: TRIỂN KHAI SERVICE QUẢN LÝ KHÓA HỌC VÀ LOGIC TRÁNH XUNG ĐỘT

#### SUB-TASK 5.1: Triển khai schema cơ sở dữ liệu Courses
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.course/courses.sql`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[DAT-004]<!--END_TAGS-->

#### SUB-TASK 5.2: Triển khai CourseService với các phương thức CRUD và kiểm tra xung đột lịch
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.course/course-service.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003], [NFR-001], [NFR-002]<!--END_TAGS-->

### NGÀY 6: VIẾT BỘ KIỂM TRA CHO CÁC CHỨC NĂNG QUẢN LÝ KHÓA HỌC

#### SUB-TASK 6.1: Kiểm thử tích hợp cho các API CRUD khóa học và logic xung đột
##### Sub-Agent được chỉ định: Tester
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.course/course-service.java;./sources/backend.membershiphub.course/courseservice-integration-test.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003]<!--END_TAGS-->