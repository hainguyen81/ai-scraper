# Giai đoạn 1: <!--PHASE_NAME_START-->Xây dựng lõi người dùng, xác thực và phân quyền; triển khai các bảng dữ liệu cơ bản.<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260807134137 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Xây dựng lõi người dùng, xác thực và phân quyền; triển khai các bảng dữ liệu cơ bản.<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 1 tập trung vào xây dựng lõi người dùng, xác thực và phân quyền, triển khai các bảng dữ liệu cơ bản, định nghĩa API và exception handlers, và chuẩn bị tài liệu kiến trúc. Các thành phần chính bao gồm: lớp thực thể User và Role, controller xác thực, endpoint đăng ký, đăng nhập mạng xã hội, gán vai trò, và exception handler xử lý lỗi xác thực đầu vào. Tài liệu kiến trúc chi tiết các mô hình dữ liệu, luồng API, và quy trình triển khai sẽ được lập trình trong tài liệu Phase1_Architecture.md.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 13:41:37 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và mục tiêu thực thi giai đoạn

Giai đoạn 1 thực hiện toàn bộ quy trình đăng ký người dùng, xác thực qua mạng xã hội, và phân quyền vai trò. Các bảng dữ liệu `users` và `roles` được tạo ra, cùng với các ràng buộc khóa ngoại, kiểm tra duy nhất và kiểm tra giá trị hợp lệ. API `/api/v1/auth/register`, `/api/v1/auth/social`, và `/api/v1/users/{id}/role` được triển khai, đồng thời exception handler `EXC-004` xử lý lỗi đầu vào. Tài liệu kiến trúc chi tiết được lập trình trong `Phase1_Architecture.md`.

## 2. Phạm vi kỹ thuật cho phép & biên giới thư mục

- **Backend**: `./sources/backend/org/nlh4j/saas/membershiphub/user-management/`
- **Documentation**: `./sources/docs/Phase1_Architecture.md`
- **API Endpoints**:
  - `/api/v1/auth/register` (POST)
  - `/api/v1/auth/social` (POST)
  - `/api/v1/users/{id}/role` (PUT)

## 3. Hướng dẫn chức năng của các tác nhân phụ

* **Coder**: Chức năng là nhà phát triển ứng dụng cấp cao. Trách nhiệm thực hiện mã nguồn ứng dụng trong cả backend và frontend/mobile. Vô hiệu hoá viết bộ kiểm thử hoặc cấu hình hạ tầng.  
* **Tester**: Chức năng là trưởng nhóm kiểm thử. Chuyên môn xây dựng bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa E2E, và kiểm tra hiệu suất. Không sửa đổi mã nguồn sản xuất.  
* **Doc**: Chức năng là nhà văn kỹ thuật. Chuyên môn biên soạn tài liệu kỹ thuật, bản vẽ kiến trúc, mô tả schema, và tài liệu triển khai. Không viết mã nguồn.  
* **Reviewer**: Chức năng là kiểm tra mã. Chuyên môn phân tích tĩnh, kiểm tra bảo mật OWASP, sửa lỗi biên dịch, và giải quyết vấn đề chất lượng.  
* **Docker**: Chức năng là chuyên gia container. Xây dựng Dockerfile đa giai đoạn, tối ưu kích thước, và đẩy image lên DockerHub.  
* **GCP**: Chức năng là chuyên gia GCP. Xây dựng và đẩy image lên Google Artifact Registry, triển khai trên Cloud Run.  
* **GKE**: Chức năng là chuyên gia Kubernetes. Xây dựng manifest deployment, HPA, Helm chart, và triển khai microservices lên GKE.

## 4. Định nghĩa Hoàn thành (DoD)

- Tất cả yêu cầu [REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004] được triển khai đầy đủ.  
- Độ phủ kiểm thử JUnit >= 85%.  
- API đáp ứng đúng cấu trúc JSON đã định nghĩa.  
- Tài liệu kiến trúc `Phase1_Architecture.md` hoàn chỉnh, bao gồm mô hình dữ liệu, luồng API, và quy trình triển khai.  
- Kiểm tra OWASP: bảo vệ chống SQL injection, XSS, CSRF, và bảo mật JWT.  
- Mã nguồn được kiểm tra bởi Reviewer, không có lỗi biên dịch.  
- Mọi tag ID được ánh xạ đầy đủ, không có tag chưa được sử dụng.  
- Không có lỗi nghiêm trọng, hệ thống có thể chạy trong môi trường GKE với Docker image < 500 MB.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->Triển khai lớp thực thể người dùng và vai trò<!--DAY_HEADER_END-->

#### 📝 Triển khai lớp thực thể người dùng và vai trò 1.1:
##### Tác nhân phụ được giao: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/org/nlh4j/saas/membershiphub/user-management/UserEntity.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-001], [DAT-001]<!--END_TAGS-->
* **Mô tả công việc kỹ thuật chi tiết:** Triển khai lớp thực thể UserEntity với các trường userId (UUID PK), email, passwordHash, fullName, roleId (FK), provider (CHECK), timestamps. Áp dụng các ràng buộc NOT NULL, UNIQUE cho email. Thêm lớp thực thể RoleEntity với roleId, name, description. Ghi chú các mối quan hệ khóa ngoại.
* **Database Schema DDL SQL Specification [DAT-001]:**
```sql
CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT NOT NULL,
    provider VARCHAR(20) NOT NULL DEFAULT 'local',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_users_roles FOREIGN KEY (role_id) REFERENCES roles(role_id),
    CONSTRAINT chk_provider CHECK (provider IN ('local','firebase','google','facebook'))
);
```
* **API and Event Routing Contracts [REQ-001], [ARC-006]:**
```json
{
  "endpoints": [
    {
      "path": "/api/v1/auth/register",
      "method": "POST",
      "request": {
        "email": "string",
        "password": "string",
        "fullName": "string",
        "role": "string"
      },
      "response": {
        "userId": "UUID",
        "token": "string",
        "refreshToken": "string"
      }
    },
    {
      "path": "/api/v1/auth/social",
      "method": "POST",
      "request": {
        "provider": "string",
        "code": "string"
      },
      "response": {
        "userId": "UUID",
        "token": "string"
      }
    },
    {
      "path": "/api/v1/users/{id}/role",
      "method": "PUT",
      "request": {
        "roleId": "SMALLINT"
      },
      "response": {
        "userId": "UUID",
        "roleId": "SMALLINT"
      }
    }
  ]
}
```
* **Phase Localized Exception Handlers [EXC-004]:**
  * Xử lý lỗi xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc). Khi xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### 📝 Tài liệu kiến trúc giai đoạn 1 1.2:
##### Tác nhân phụ được giao: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/Phase1_Architecture.md
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-001], [DAT-001]<!--END_TAGS-->
* **Mô tả công việc kỹ thuật chi tiết:** Khởi tạo tài liệu kiến trúc cho giai đoạn 1, bao gồm mô tả chi tiết về kiến trúc, mô hình dữ liệu, API, exception handlers, và quy trình triển khai. Đảm bảo tài liệu đáp ứng tiêu chuẩn OWASP và các yêu cầu bảo mật, bao gồm mô tả bảo mật, kiểm tra, và quy trình kiểm tra.

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->Viết bộ kiểm thử đơn vị cho quản lý người dùng<!--DAY_HEADER_END-->

#### 📝 Viết bộ kiểm thử đơn vị cho quản lý người dùng 2.1:
##### Tác nhân phụ được giao: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/org/nlh4j/saas/membershiphub/user-management/UserEntityTest.java;./sources/backend/org/nlh4j/saas/membershiphub/user-management/UserEntity.java
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-001], [DAT-001]<!--END_TAGS-->
* **Mô tả công việc kỹ thuật chi tiết:** Xây dựng bộ kiểm thử JUnit5 cho UserEntity và RoleEntity, bao gồm kiểm tra các ràng buộc trường (email unique, provider enum), mối quan hệ khóa ngoại, và logic tạo timestamp. Đảm bảo độ phủ trên mã nguồn >= 85%.