# Giai đoạn 1: <!--PHASE_NAME_START-->user_core_services<!--PHASE_NAME_END--> | Mô tả: Triển khai các dịch vụ cốt lõi quản lý người dùng bao gồm đăng ký, xác thực xã hội, gán vai trò, schema cơ sở dữ liệu và logging kiểm toán bảo mật

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260803053505 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên kỹ thuật giai đoạn** | <!--PHASE_NAME_START-->user_core_services<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai các dịch vụ cốt lõi quản lý người dùng bao gồm đăng ký, xác thực xã hội, gán vai trò, schema cơ sở dữ liệu và logging kiểm toán bảo mật |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/03 05:35:05 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu giai đoạn

Giai đoạn này tập trung vào việc xây dựng nền tảng cốt lõi cho hệ thống quản lý người dùng, bao gồm:

- Triển khai schema cơ sở dữ liệu cho bảng Users và Roles với các ràng buộc toàn vẹn dữ liệu
- Xây dựng dịch vụ đăng ký người dùng với xác thực email/mật khẩu và hỗ trợ OAuth2 cho các nhà cung cấp xã hội (Firebase, Google, Facebook)
- Triển khai cơ chế phân quyền RBAC với khả năng gán và thay đổi vai trò người dùng
- Thiết lập hệ thống logging kiểm toán đáp ứng các tiêu chuẩn bảo mật doanh nghiệp
- Triển khai xử lý ngoại lệ chi tiết cho validation đầu vào và xung đột dữ liệu

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép

**Thư mục và tệp được phép:**
- `./sources/backend.membershiphub.user/users.sql` - DDL schema cho bảng Users
- `./sources/backend.membershiphub.user/roles.sql` - DDL schema cho bảng Roles  
- `./sources/backend.membershiphub.user/user-service.java` - Dịch vụ chính quản lý người dùng

**Endpoint API:**
- `POST /api/v1/auth/register` - Đăng ký người dùng mới
- `POST /api/v1/auth/social` - Xác thực qua nhà cung cấp xã hội
- `PUT /api/v1/users/{userId}/role` - Cập nhật vai trò người dùng (chỉ System Admin)

## 3. Chỉ đạo chức năng cho Sub-Agent chuyên dụng

**Coder:** Triển khai mã nguồn Java/Quarkus với tuân thủ SOLID, sử dụng BCrypt cho mã hóa mật khẩu, JWT với access token 15 phút và refresh token 7 ngày, áp dụng @Valid cho validation và @Transactional cho các thao tác ghi.

**Tester:** Xây dựng bộ kiểm thử JUnit 5 với độ phủ mã ≥85%, sử dụng Mock cho các dependency, kiểm thử happy path và các scenario lỗi validation.

**Reviewer:** Thực hiện phân tích tĩnh mã nguồn, kiểm tra tuân thủ OWASP Top 10, đảm bảo không có lỗ hổng SQL injection hoặc XSS.

**Doc:** Biên soạn tài liệu kỹ thuật đầy đủ bao gồm API documentation với OpenAPI, schema documentation và hướng dẫn triển khai.

## 4. Định nghĩa hoàn thành (DoD) cho giai đoạn

- ✅ 100% các requirement [REQ-001], [REQ-002], [REQ-003] được triển khai đầy đủ
- ✅ Schema database [DAT-001] được tạo thành công với tất cả ràng buộc
- ✅ Luồng xác thực [ARC-006] hoạt động với OAuth2 và JWT
- ✅ Xử lý ngoại lệ [EXC-004] cho validation đầu vào
- ✅ Tuân thủ các tiêu chuẩn bảo mật [NFR-001], [NFR-003], [NFR-006]
- ✅ Độ phủ kiểm thử ≥85% cho tất cả các dịch vụ
- ✅ 100% các Tag ID được ánh xạ và kiểm tra

## 5. NHẬT KÝ THỰC THI KIẾN TRÚC THEO NGÀY

### NGÀY 1: TRIỂN KHAI DỊCH VỤ ĐĂNG KÝ NGƯỜI DÙNG VÀ API XÁC THỰC XÃ HỘI

#### SUB-TASK 1.1: Triển khai schema cơ sở dữ liệu Users và Roles
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.user/users.sql`, `./sources/backend.membershiphub.user/roles.sql`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[DAT-001]<!--END_TAGS-->

#### SUB-TASK 1.2: Triển khai UserService với phương thức register và socialAuthenticate
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.user/user-service.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-001], [REQ-002], [ARC-006], [EXC-004], [NFR-001], [NFR-003], [NFR-006]<!--END_TAGS-->

### NGÀY 2: VIẾT BỘ KIỂM TRA ĐƠN VỊ VÀ TÍCH HỢP CHO CÁC CHỨC NĂNG NGƯỜI DÙNG

#### SUB-TASK 2.1: Kiểm thử đơn vị cho các phương thức register và socialAuthenticate
##### Sub-Agent được chỉ định: Tester
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.user/user-service.java;./sources/backend.membershiphub.user/userservice-test.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-001], [REQ-002], [DAT-001], [EXC-004]<!--END_TAGS-->

#### SUB-TASK 2.2: Kiểm thử tích hợp cho API endpoints
##### Sub-Agent được chỉ định: Tester
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.user/user-service.java;./sources/backend.membershiphub.user/user-controller-test.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-001], [REQ-002], [ARC-006], [EXC-004]<!--END_TAGS-->