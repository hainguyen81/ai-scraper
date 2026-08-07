# Giai đoạn 1: Quản lý người dùng & xác thực cốt lõi
<!--PHASE_NAME_START-->Quản lý người dùng & xác thực cốt lõi<!--PHASE_NAME_END-->

## 📊 Kiểm Soát Tài Liệu

| Mục | Chi Tiết |
| :--- | :--- |
| **ID Bản vẽ** | ARCH-20260807172813 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Quản lý người dùng & xác thực cốt lõi<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng lõi người dùng, xác thực đa nhà cung cấp, phân quyền RBAC và các cơ chế bảo vệ đầu vào.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 17:28:13 |
| **Tác giả** | Kiến Trúc Hệ Thống Doanh Nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban Quản Trị Kỹ Thuật |

## 1. Phạm Vi Hoạt Động & Mục Tiêu Của Giai Đoạn
Giai đoạn này tập trung vào việc triển khai lõi người dùng, xác thực đa nhà cung cấp, phân quyền RBAC và các cơ chế bảo vệ đầu vào. Các yêu cầu bao gồm đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng và quản lý vai trò.

## 2. Phạm Vi Kỹ Thuật & Ranh Giới Thư Mục (Tệp, đường dẫn và điểm cuối)
- ./sources/backend/auth/ (Coder) – [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [EXC-004]
- ./sources/docs/ (Doc) – tài liệu thiết kế hệ thống người dùng

## 3. Hướng Dẫn Chức Năng Cụ Thể Cho Các Đặc Sỹ Phụ
*   **Coder**: Hoạt động như một Lập Trình Viên Ứng Dụng Cấp Cao/Chuyên Gia. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và ứng dụng khách frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu hạ tầng.
* **Tester**: Hoạt động như một Trưởng/Chuyên Gia Kiểm Chất/QA. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng kiểm tra chất lượng. Trách nhiệm là tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con nhiệm vụ liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất ra chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà Viết Kỹ Thuật Chuyên Gia và Kiến Trúc Hệ Thống Doanh Nghiệp. Chuyên về biên soạn tài liệu Kỹ Thuật Chi Tiết, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp công nghệ hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác nhận lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng dịch vụ microservices vào các cụm GKE hoạt động.

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)
- Triển khai hoàn chỉnh các dịch vụ xác thực, đăng ký, OAuth2, JWT, quản lý vai trò.
- Kiểm tra và xác nhận các yêu cầu chức năng cốt lõi.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Triển khai đăng ký người dùng, xác thực qua mạng xã hội và gán vai trò ban đầu<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 1.1: [Triển khai đăng ký người dùng, xác thực qua mạng xã hội và gán vai trò ban đầu]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/auth/UserService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-001], [DAT-001]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Viết lớp UserService triển khai registerUser (validation, bcrypt hash, lưu vào bảng USERS với roleId mặc định là Student), implement socialAuthFlow (nhận OAuth2 code, gọi Firebase/Google/Facebook API, tạo hoặc cập nhật bản ghi USERS, sinh JWT token có thời hạn 15 phút), thêm phương thức assignRole (cập nhật cột roleId, ghi log vào bảng AUDIT). Đảm bảo tất cả các thao tác đều được bao quanh bởi transaction và tuân thủ các ràng buộc khóa ngoại.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Xây dựng kiểm tra đầu vào và xử lý lỗi xác thực<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 2.1: [Xây dựng kiểm tra đầu vào và xử lý lỗi xác thực]
##### Đặc Sỹ Phụ Được Phân Công: Tester
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/auth/UserServiceTest.java;./sources/backend/auth/UserService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[EXC-004], [REQ-001], [DAT-001]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Viết unit tests cho registerUser với các trường hợp: email hợp lệ, mật khẩu yếu, email trùng lặp; xác minh response HTTP status và message lỗi bằng tiếng Việt; kiểm tra socialAuthFlow với mã OAuth2 hợp lệ và không hợp lệ; đảm bảo exception InputValidationException được ném và xử lý bởi GlobalExceptionHandler để trả về JSON lỗi chi tiết.

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->Tạo tài liệu kỹ thuật và hướng dẫn vận hành<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 3.1: [Tạo tài liệu kỹ thuật và hướng dẫn vận hành]
##### Đặc Sỹ Phụ Được Phân Công: Doc
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/UserManagementGuide.md
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-002], [ARC-002], [ARC-003]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Soạn thảo tài liệu hướng dẫn quản lý người dùng bao gồm mô tả API, bảng tham chiếu vai trò, quy trình đăng ký, quy trình xác thực qua mạng xã hội, quy trình gán vai trò; thêm các đoạn mã ví dụ bằng tiếng Việt; đảm bảo tài liệu tham chiếu các Tag IDs [REQ-002], [ARC-002], [ARC-003].

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->Triển khai luồng xác thực JWT và refresh token<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 4.1: [Triển khai luồng xác thực JWT và refresh token]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/auth/TokenService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[ARC-004], [ARC-005], [ARC-006]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai TokenService tạo accessToken (JWT, thời gian sống 15 phút) và refreshToken (thời gian sống 7 ngày) sử dụng java-jwt; thêm endpoint /api/v1/auth/refresh để đổi refreshToken lấy accessToken mới; tích hợp Firebase Authentication làm nhà cung cấp xác thực thay thế; đảm bảo token được lưu trữ an toàn (HTTP-only, Secure flag) và thực thi blacklist cho các token bị thu hồi.

* **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:**
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

* **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-001]..[ARC-006]:**
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

* **Xử lý Ngoại lệ theo Ngôn ngữ Bản địa [EXC-004]:**
    * Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc): Trả về HTTP 400 với danh sách các trường không hợp lệ và hướng dẫn chỉnh sửa bằng tiếng Việt.