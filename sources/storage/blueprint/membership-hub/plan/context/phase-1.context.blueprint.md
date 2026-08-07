# Giai đoạn 1: <!--PHASE_NAME_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản<!--PHASE_NAME_END-->

## 📊 Bảng Kiểm Soát

| Item | Details |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807070031 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn đầu tiên tập trung vào xây dựng hệ thống quản lý người dùng, xác thực, phân quyền và lưu trữ dữ liệu người dùng. Các thành phần chính bao gồm UserService, AuthController, và bảng dữ liệu ROLES, USERS. Hệ thống hỗ trợ đăng ký, đăng nhập bằng email/mật khẩu và OAuth2, cấp JWT, và thực thi kiểm tra đầu vào.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/07 07:00:31 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Sự chấp thuận** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu của Giai đoạn

Giai đoạn 1 nhằm triển khai toàn bộ cơ sở hạ tầng người dùng, bao gồm đăng ký, xác thực, phân quyền và lưu trữ dữ liệu người dùng. Các mục tiêu chính:

- Xây dựng UserService để xử lý đăng ký người dùng mới, tạo bản ghi trong bảng USERS với vai trò mặc định là Student.
- Triển khai AuthController để hỗ trợ đăng nhập bằng email/mật khẩu và OAuth2 (Firebase, Google, Facebook), cấp JWT và refresh token.
- Định nghĩa và triển khai bảng dữ liệu ROLES và USERS, bao gồm các ràng buộc, chỉ mục và kiểm tra đầu vào.
- Đảm bảo tuân thủ các yêu cầu bảo mật: mã hóa mật khẩu, bảo vệ JWT, kiểm tra đầu vào, và ghi nhận audit trail.

## 2. Phạm vi Kỹ thuật & Ranh giới Thư mục

- **Thư mục chính**: `./sources/backend/users/`
- **Endpoint REST**:
  - `POST /api/v1/auth/register`
  - `POST /api/v1/auth/social`
  - `PUT /api/v1/users/{userId}/role`
- **Cấu trúc gói Java**: `org.nlh4j.saas.membershiphub.backend.users`

## 3. Hướng dẫn Chức năng của Sub-Agent

| Sub-Agent | Mô tả |
| :--- | :--- |
| **Coder** | Phát triển mã nguồn ứng dụng, bao gồm Java, TypeScript, SQL. Không viết test hoặc cấu hình DevOps. |
| **Tester** | Viết test JUnit, integration, E2E. Không sửa mã nguồn. |
| **Doc** | Tạo tài liệu kỹ thuật, schema, kiến trúc. |
| **Reviewer** | Kiểm tra mã, bảo mật, tuân thủ OWASP. |
| **Docker** | Xây dựng Dockerfile, multi-stage, tối ưu kích thước. |
| **GCP** | Đẩy image lên Artifact Registry, triển khai Cloud Run. |
| **GKE** | Xây dựng manifest Kubernetes, HPA, Helm. |

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)

- Tất cả các yêu cầu [REQ-001], [REQ-002], [REQ-003], [ARC-006] được triển khai và kiểm tra thành công.
- Định nghĩa DDL SQL cho [DAT-001] được áp dụng và migration thành công.
- Tất cả các exception handler [EXC-004] được triển khai và kiểm tra.
- Đạt 100% coverage test cho các module UserService và AuthController.
- Đạt 100% compliance OWASP, audit trail ghi nhận mọi thay đổi vai trò và đăng ký.
- Tài liệu kiến trúc và schema được hoàn thiện và lưu trữ trong `./sources/docs/`.

## 5. LOG THỰC HIỆN KIẾT THUẬT NGÀY MỖI NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ QUẢN LÝ NGƯỜI DÙNG CƠ BẢN<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 1.1: Triển khai lớp UserService để xử lý đăng ký người dùng mới, tạo bản ghi trong bảng USERS với vai trò mặc định là Student, tuân thủ REQ-001 và ARC-001.
##### Sub-Agent Giao Nhiệm: Coder
##### Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn Mục tiêu**: ./sources/backend/users/UserService.java
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-001], [DAT-001], [ARC-001]<!--END_TAGS-->
* **Hướng dẫn Công nghệ Cấp thấp**:  
  - Định nghĩa interface `UserService` với phương thức `registerUser(RegisterRequest request)` trả về `UserDto`.  
  - Sử dụng `PasswordEncoder` (BCrypt) để mã hóa mật khẩu.  
  - Kiểm tra email duy nhất trước khi lưu.  
  - Gán roleId mặc định là `2` (Student) từ bảng ROLES.  
  - Ghi log audit với `AuditService.logCreateUser(userId, email)`.  
  - Trả về JWT token (15 phút) và refresh token (7 ngày) thông qua `JwtProvider`.  
  - Xử lý ngoại lệ `EmailAlreadyExistsException` trả về HTTP 409.

#### 📝 NHIỆM VỤ 1.2: Tài liệu kiến trúc tổng thể
##### Sub-Agent Giao Nhiệm: Doc
##### Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn Mục tiêu**: ./sources/docs/phase1-architecture.md
* **Thẻ Tracability**: <!--START_TAGS-->[ARC-001], [ARC-006], [DAT-001]<!--END_TAGS-->
* **Hướng dẫn Công nghệ Cấp thấp**:  
  - Mô tả kiến trúc microservice, flow xác thực, schema ER diagram.  
  - Đính kèm DDL SQL cho ROLES và USERS.  
  - Định nghĩa các endpoint REST và payload JSON.  
  - Ghi chú về bảo mật, audit, và quy trình CI/CD.

#### 📝 NHIỆM VỤ 1.3: Định nghĩa DDL SQL cho bảng ROLES và USERS
##### Sub-Agent Giao Nhiệm: Coder
##### Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn Mục tiêu**: ./sources/backend/migrations/001_create_user_tables.sql
* **Thẻ Tracability**: <!--START_TAGS-->[DAT-001]<!--END_TAGS-->
* **Hướng dẫn Công nghệ Cấp thấp**:  
  - Xây dựng DDL SQL dưới dạng script migration.  
  - Đảm bảo các constraint, index, và default values.  
  - Định nghĩa enum `provider` với giá trị `local`, `firebase`, `google`, `facebook`.

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
```

#### 📝 NHIỆM VỤ 1.4: Hợp đồng API và Sự kiện cho đăng ký và xác thực
##### Sub-Agent Giao Nhiệm: Coder
##### Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn Mục tiêu**: ./sources/backend/docs/api-auth.json
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-006]<!--END_TAGS-->
* **Hướng dẫn Công nghệ Cấp thấp**:  
  - Định nghĩa payload JSON cho `POST /api/v1/auth/register`, `POST /api/v1/auth/social`, `PUT /api/v1/users/{userId}/role`.  
  - Mô tả response status, body, và mã lỗi.

```json
// POST /api/v1/auth/register
{
  "email": "user@example.com",
  "password": "StrongPass123!",
  "fullName": "Nguyen Van A",
  "provider": "local"
}
```

```json
// POST /api/v1/auth/social
{
  "provider": "google",
  "code": "OAuth2_code_from_google",
  "redirectUri": "https://app.example.com/auth/callback"
}
```

```json
// PUT /api/v1/users/{userId}/role
{
  "roleId": 2
}
```

#### 📝 NHIỆM VỤ 1.5: Xử lý ngoại lệ Xác thực đầu vào không hợp lệ
##### Sub-Agent Giao Nhiệm: Coder
##### Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn Mục tiêu**: ./sources/backend/users/exception/ValidationExceptionHandler.java
* **Thẻ Tracability**: <!--START_TAGS-->[EXC-004]<!--END_TAGS-->
* **Hướng dẫn Công nghệ Cấp thấp**:  
  - Định nghĩa `@ControllerAdvice` để bắt `MethodArgumentNotValidException`.  
  - Trả về HTTP 400 với danh sách trường không hợp lệ và hướng dẫn chỉnh sửa.  
  - Ghi log chi tiết lỗi.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->XÂY DỰNG AUTH CONTROLLER VÀ TÍNH NĂNG XÁC THỰC<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 2.1: Triển khai AuthController để xử lý xác thực OAuth2 từ Firebase/Google/Facebook, trao đổi mã lấy thông tin người dùng, cập nhật vai trò và cấp JWT token (ARC-006), đồng thời hỗ trợ phân quyền người dùng (REQ-003).
##### Sub-Agent Giao Nhiệm: Coder
##### Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn Mục tiêu**: ./sources/backend/users/AuthController.java
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-002], [REQ-003], [ARC-006]<!--END_TAGS-->
* **Hướng dẫn Công nghệ Cấp thấp**:  
  - Định nghĩa endpoint `POST /api/v1/auth/social` nhận `provider`, `code`, `redirectUri`.  
  - Gọi SDK Firebase/Google/Facebook để lấy thông tin người dùng.  
  - Kiểm tra tồn tại người dùng trong bảng USERS, nếu chưa có tạo mới với roleId `2` (Student).  
  - Cập nhật roleId nếu cần.  
  - Cấp JWT token (15 phút) và refresh token (7 ngày) thông qua `JwtProvider`.  
  - Trả về response JSON gồm `accessToken`, `refreshToken`, `expiresIn`.  
  - Xử lý ngoại lệ `OAuthException` trả về HTTP 401.  
  - Ghi log audit với `AuditService.logAuth(provider, userId)`.

#### 📝 NHIỆM VỤ 2.2: Hợp đồng API và Sự kiện cho xác thực OAuth2
##### Sub-Agent Giao Nhiệm: Coder
##### Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn Mục tiêu**: ./sources/backend/docs/api-social-auth.json
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-002], [ARC-006]<!--END_TAGS-->
* **Hướng dẫn Công nghệ Cấp thấp**:  
  - Định nghĩa payload JSON cho `POST /api/v1/auth/social`.  
  - Mô tả response status, body, và mã lỗi.

```json
// POST /api/v1/auth/social
{
  "provider": "google",
  "code": "OAuth2_code_from_google",
  "redirectUri": "https://app.example.com/auth/callback"
}
```

#### 📝 NHIỆM VỤ 2.3: Xử lý ngoại lệ Xác thực đầu vào không hợp lệ
##### Sub-Agent Giao Nhiệm: Coder
##### Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn Mục tiêu**: ./sources/backend/users/exception/ValidationExceptionHandler.java
* **Thẻ Tracability**: <!--START_TAGS-->[EXC-004]<!--END_TAGS-->
* **Hướng dẫn Công nghệ Cấp thấp**:  
  - Định nghĩa `@ControllerAdvice` để bắt `MethodArgumentNotValidException`.  
  - Trả về HTTP 400 với danh sách trường không hợp lệ và hướng dẫn chỉnh sửa.  
  - Ghi log chi tiết lỗi.