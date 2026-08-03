# Giai đoạn 2: <!--PHASE_NAME_START-->center_management_module<!--PHASE_NAME_END--> | Mô tả: Triển khai module quản lý trung tâm bao gồm CRUD trung tâm, danh sách trung tâm công khai, phân quyền quản trị trung tâm, và tích hợp với RBAC cho Center Admin

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260803053505 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên kỹ thuật giai đoạn** | <!--PHASE_NAME_START-->center_management_module<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai module quản lý trung tâm bao gồm CRUD trung tâm, danh sách trung tâm công khai, phân quyền quản trị trung tâm, và tích hợp với RBAC cho Center Admin |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/03 05:35:05 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu giai đoạn

Giai đoạn này tập trung vào việc xây dựng module quản lý trung tâm với các chức năng chính:

- Triển khai schema cơ sở dữ liệu cho bảng Centers với các ràng buộc toàn vẹn dữ liệu
- Xây dựng dịch vụ CRUD đầy đủ cho quản lý trung tâm với validation nghiêm ngặt
- Triển khai API danh sách trung tâm công khai cho tất cả người dùng đã xác thực
- Thiết lập cơ chế phân quyền RBAC cho Center Admin với khả năng gán và hủy gán
- Kiểm tra xung đột Tax ID để đảm bảo tính duy nhất
- Triển khai hệ thống logging kiểm toán đáp ứng các tiêu chuẩn bảo mật doanh nghiệp

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép

**Thư mục và tệp được phép:**
- `./sources/backend.membershiphub.center/centers.sql` - DDL schema cho bảng Centers
- `./sources/backend.membershiphub.center/center-service.java` - Dịch vụ chính quản lý trung tâm
- `./sources/backend.membershiphub.center/center-repository.java` - Repository JPA cho Centers
- `./sources/backend.membershiphub.center/center-controller.java` - REST Controller cho API trung tâm

**Endpoint API:**
- `GET /api/v1/centers` - Lấy danh sách tất cả trung tâm (công khai)
- `POST /api/v1/centers` - Tạo trung tâm mới (chỉ System Admin)
- `PUT /api/v1/centers/{centerId}` - Cập nhật thông tin trung tâm (chỉ System Admin)
- `DELETE /api/v1/centers/{centerId}` - Xóa mềm trung tâm (chỉ System Admin)
- `POST /api/v1/centers/{centerId}/admins/{userId}` - Gán người dùng làm Center Admin (chỉ System Admin)

## 3. Chỉ đạo chức năng cho Sub-Agent chuyên dụng

**Coder:** Triển khai mã nguồn Java/Quarkus với tuân thủ SOLID, sử dụng JPA/Hibernate cho persistence, áp dụng @Valid cho validation, @PreAuthorize cho phân quyền, và @Transactional cho các thao tác ghi.

**Tester:** Xây dựng bộ kiểm thử JUnit 5 và Testcontainers với độ phủ mã ≥85%, kiểm thử happy path và các scenario lỗi validation, xung đột Tax ID.

**Reviewer:** Thực hiện phân tích tĩnh mã nguồn, kiểm tra tuân thủ OWASP Top 10, đảm bảo không có lỗ hổng SQL injection hoặc XSS.

**Doc:** Biên soạn tài liệu kỹ thuật đầy đủ bao gồm API documentation với OpenAPI, schema documentation và hướng dẫn triển khai.

## 4. Định nghĩa hoàn thành (DoD) cho giai đoạn

- ✅ 100% các requirement [REQ-004], [REQ-005], [REQ-006] được triển khai đầy đủ
- ✅ Schema database [DAT-003] được tạo thành công với tất cả ràng buộc
- ✅ Luồng phân quyền [ARC-002] hoạt động với RBAC cho Center Admin
- ✅ Xử lý validation đầu vào và xung đột Tax ID
- ✅ Tuân thủ các tiêu chuẩn bảo mật [NFR-003], [NFR-004], [NFR-005]
- ✅ Độ phủ kiểm thử ≥85% cho tất cả các dịch vụ
- ✅ 100% các Tag ID được ánh xạ và kiểm tra

## 5. NHẬT KÝ THỰC THI KIẾN TRÚC THEO NGÀY

### NGÀY 3: TRIỂN KHAI SERVICE QUẢN LÝ TRUNG TÂM VÀ CÁC ENDPOINT CRUD

#### SUB-TASK 3.1: Triển khai schema cơ sở dữ liệu Centers
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.center/centers.sql`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[DAT-003]<!--END_TAGS-->

#### SUB-TASK 3.2: Triển khai CenterService với các phương thức CRUD và phân quyền
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.center/center-service.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002], [NFR-003], [NFR-004], [NFR-005]<!--END_TAGS-->

### NGÀY 4: VIẾT BỘ KIỂM TRA TÍCH HỢP CHO CÁC API TRUNG TÂM

#### SUB-TASK 4.1: Kiểm thử tích hợp cho các API CRUD trung tâm
##### Sub-Agent được chỉ định: Tester
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.center/center-service.java;./sources/backend.membershiphub.center/centerservice-integration-test.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [DAT-003], [ARC-002]<!--END_TAGS-->