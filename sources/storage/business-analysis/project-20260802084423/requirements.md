# SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub

## 1. Tổng quan dự án & Kiến trúc toàn cầu

### Mục tiêu sản phẩm & Giá trị cốt lõi
- Cung cấp một nền tảng thống nhất để quản lý nhiều trung tâm thành viên.
- Cho phép theo dõi thời gian thực thông qua quét mã QR.
- Cung cấp thẻ thành viên kỹ thuật số với tính toán ngày hiệu lực.
- Tạo điều kiện giao tiếp đa kênh (web, di động, nhóm Zalo).
- Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính dễ sử dụng, hỗ trợ đa ngôn ngữ.

### Đối tượng người dùng mục tiêu
- Quản trị viên hệ thống (siêu người dùng toàn cầu)
- Quản trị viên trung tâm (nhà quản lý cấp trung tâm)
- Người quản lý (phó quản trị viên, quyền hạn giới hạn)
- Giáo viên (chỉ đọc lịch học)
- Học sinh (duyệt khóa học, ghi danh, xem thẻ)
- Người dùng ứng dụng di động (cùng các vai trò, giao diện đáp ứng)

### Ma trận kiểm soát truy cập dựa trên vai trò toàn cầu (RBAC)
- [ARC-001] Quản trị viên hệ thống: toàn bộ quyền trên tất cả các trung tâm.
- [ARC-002] Quản trị viên trung tâm: toàn bộ quyền trong trung tâm của mình, không ảnh hưởng đến trung tâm khác.
- [ARC-003] Người quản lý: có thể tạo thông báo, quản lý học sinh, gán học sinh hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
- [ARC-004] Giáo viên: xem các khóa học của mình, danh sách học sinh, lịch học; chỉ đọc.
- [ARC-005] Học sinh: duyệt khóa học, đăng ký khóa học mới, xem thẻ thành viên (ngày còn lại), gia hạn ngày thẻ.

### Blueprint công nghệ & hạ tầng toàn cầu
- [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời gian hiệu lực 15 phút và token làm mới.
- [ARC-007] Luồng xử lý QR chấm công: ứng dụng di động quét QR, gửi studentID và timestamp đến backend; dịch vụ xác thực và ghi nhận chấm công một cách idempotent.
- [ARC-008] Luồng thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và gửi bài viết đến nhóm Zalo được chỉ định cho thông báo, phân công khóa học và cảnh báo chấm công.
- [ARC-009] Luồng tích hợp ứng dụng di động: Frontend Next.js tiêu thụ REST APIs; xác thực qua bearer tokens; hỗ trợ caching offline cho kết nối hạn chế.

## 2. Các mô-đun chức năng chính

### 2.1 Quản lý người dùng

**Core Functional Requirements**

- **[REQ-001]** Đăng ký người dùng: Là người dùng tiềm năng, tôi muốn đăng ký sử dụng email và mật khẩu (hoặc nhà cung cấp xã hội) để có được một tài khoản trong hệ thống.
  - Acceptance Criteria:
    - Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role ‘Student’ (or ‘Teacher’ if invited), and returns a success response with a JWT token. *[REQ-001]*
  - Data Inputs & Field Validations:
    - Email: bắt buộc, tối đa 255 ký tự, phải chứa một dấu '@' và phần tên miền (ví dụ: user@example.com). Phải là duy nhất.
    - Password: bắt buộc, tối thiểu 8 ký tự, ít nhất một chữ hoa, một chữ thường, một chữ số, một ký tự đặc biệt.
    - Terms: bắt buộc checkbox.

- **[REQ-002]** Xác thực xã hội: Là người dùng, tôi muốn đăng nhập/đăng ký bằng Firebase, Google, hoặc Facebook OAuth để tận dụng thông tin xác thực hiện có.
  - Acceptance Criteria:
    - Given a user selects a social provider, When they authenticate through the provider's popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. *[REQ-002]*
  - Data Inputs & Field Validations: provider token, tùy chọn hình ảnh hồ sơ.

- **[REQ-003]** Gán vai trò người dùng: Là quản trị viên, tôi muốn gán hoặc thay đổi vai trò của người dùng (System Admin, Center Admin, Manager, Teacher, Student) để quyền được thực thi chính xác.
  - Acceptance Criteria:
    - Given an admin selects a user and a new role, When the assignment is confirmed, Then the user's role column is updated, and appropriate permissions are applied immediately. *[REQ-003]*
  - Data Inputs & Field Validations: Role dropdown, bắt buộc ghi nhật ký kiểm toán.

**Module Exception Flows**

- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc):
  - If validation fails on form submission, When the error is returned to the user, Then a clear message lists each invalid field and prompts correction.

**Module Localized Data Dictionary**

- **[DAT-001]** Bảng Users & Roles
  - Bảng Users:
    - uuid userId PK "Unique identifier"
    - varchar email "" "Primary login identifier, max 255 chars, unique"
    - char passwordHash "" "bcrypt hash"
    - varchar fullName "" "Real name"
    - smallint roleId FK "Assigned role, FK → ROLES.roleId"
    - varchar provider "" "Auth provider, enum('local','firebase','google','facebook'), default 'local'"
    - timestamp createdAt "" "Account creation timestamp"
    - timestamp updatedAt "" "Last update timestamp"
  - Bảng Roles:
    - smallint roleId PK "Role identifier"
    - varchar name PK "Role name, unique"
    - varchar description "" "Role description"

```
```mermaid
erDiagram
    USERS {
        uuid userId PK "Unique identifier"
        varchar email "" "Primary login identifier, max 255 chars, unique"
        char passwordHash "" "bcrypt hash"
        varchar fullName "" "Real name"
        smallint roleId FK "Assigned role, FK → ROLES.roleId"
        varchar provider "" "Auth provider, enum('local','firebase','google','facebook'), default 'local'"
        timestamp createdAt "" "Account creation timestamp"
        timestamp updatedAt "" "Last update timestamp"
    }
    ROLES {
        smallint roleId PK "Role identifier"
        varchar name PK "Role name, unique"
        varchar description "" "Role description"
    }
    USERS ||--o{ ROLES : "roleId"
```
```

### 2.2 Quản lý trung tâm

**Core Functional Requirements**

- **[REQ-004]** Xem danh sách trung tâm: Là bất kỳ người dùng đã xác thực, tôi muốn xem danh sách tất cả các trung tâm với địa chỉ, mã số thuế, và thông tin liên hệ quản trị viên để có thể xác định các trung tâm liên quan.
  - Acceptance Criteria:
    - Given a user navigates to the Centers page, When the request completes, Then a table of centers (Name, Address, TaxID, AdminContact) is displayed. *[REQ-004]*
  - Data Inputs & Field Validations: None (read‑only).

- **[REQ-005]** Tạo/Cập nhật/Xóa trung tâm: Là System Admin, tôi muốn thêm, chỉnh sửa, hoặc xóa một bản ghi trung tâm để thông tin trung tâm được cập nhật liên tục.
  - Acceptance Criteria:
    - Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; if duplicate tax ID exists, the operation fails with a conflict error. *[REQ-005]*
  - Data Inputs & Field Validations:
    - Name: bắt buộc, tối đa 100 ký tự.
    - Address: bắt buộc, tối đa 255 ký tự.
    - TaxID: bắt buộc, số, 10‑13 chữ số, duy nhất.
    - Contact Phone: tùy chọn, có thể bao gồm +, chữ số, dấu cách, gạch nối, ngoặc đơn.
    - Contact Email: tùy chọn, phải là email hợp lệ.

- **[REQ-006]** Phân công quản trị viên trung tâm: Là System Admin, tôi muốn gán hoặc gỡ một người dùng làm Center Admin cho một trung tâm cụ thể để ủy quyền kiểm soát.
  - Acceptance Criteria:
    - Given a System Admin selects a user and a center, When the assign action is confirmed, Then the user's role is set to ‘Center Admin’ and the center ID is recorded; unassign reverses the operation. *[REQ-006]*
  - Data Inputs & Field Validations: User ID, Center ID.

**Module Exception Flows**

- **[EXC-006]** Xác thực dữ liệu trùng lặp (ví dụ: mã số thuế đã tồn tại):
  - If duplicate tax ID is provided, When validation runs, Then the operation fails with a conflict error.

**Module Localized Data Dictionary**

- **[DAT-002]** Bảng Centers
  - Bảng Centers:
    - uuid centerId PK "Unique identifier"
    - varchar name "" "Center name, max 100 chars"
    - varchar address "" "Physical address, max 255 chars"
    - varchar taxId "" "Tax identification number, numeric, 10-13 digits, unique"
    - varchar contactPhone "" "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
    - varchar contactEmail "" "Contact email, optional, must be valid email format"

```
```mermaid
erDiagram
    CENTERS {
        uuid centerId PK "Unique identifier"
        varchar name "" "Center name, max 100 chars"
        varchar address "" "Physical address, max 255 chars"
        varchar taxId "" "Tax identification number, numeric, 10-13 digits, unique"
        varchar contactPhone "" "Contact telephone, optional, may include +, digits, spaces, hyphens, parentheses"
        varchar contactEmail "" "Contact email, optional, must be valid email format"
    }
```
```

### 2.3 Quản lý khóa học

**Core Functional Requirements**

- **[REQ-007]** Xem danh sách khóa học: Là bất kỳ người dùng đã xác thực, tôi muốn xem tất cả các khóa học với lịch trình và giáo viên được chỉ định để có thể duyệt các khóa học.
  - Acceptance Criteria:
    - Given a user visits the Courses page, When the request completes, Then a grid displays CourseID, Title, StartDate, EndDate, TeacherName. *[REQ-007]*
  - Data Inputs & Field Validations: None.

- **[REQ-008]** Tạo/Cập nhật/Xóa khóa học (tránh xung đột): Là System Admin hoặc Center Admin, tôi muốn quản lý khóa học (thêm, chỉnh sửa, xóa) trong khi đảm bảo không có lịch