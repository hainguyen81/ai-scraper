# Giai đoạn 1: <!--PHASE_NAME_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807034424 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào xây dựng lõi người dùng, vai trò và xác thực cơ bản, bao gồm đăng ký, OAuth2, JWT và validation đầu vào, đồng thời thiết lập bảng dữ liệu người dùng và vai trò.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 03:44:24 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu của Giai đoạn

Giai đoạn 1 triển khai toàn bộ chức năng quản lý người dùng và xác thực, bao gồm:
- Đăng ký người dùng mới với mật khẩu bảo mật và xác thực email.
- Xác thực OAuth2 qua Firebase, Google, Facebook.
- Phân quyền người dùng dựa trên vai trò (System Admin, Center Admin, Manager, Teacher, Student).
- Thiết lập bảng dữ liệu `USERS` và `ROLES` trong PostgreSQL.
- Cung cấp API REST `/api/v1/auth/register`, `/api/v1/auth/social`, `/api/v1/users/{userId}/role`.
- Đảm bảo tuân thủ OWASP Top 10, bảo mật JWT, và bảo vệ CSRF.

## 2. Phạm vi Kỹ thuật & Giới hạn Thư mục

- **Backend**: `./sources/org/nlh4j/sources/membershiphub/backend/users/UserService.java`, `./sources/org/nlh4j/sources/membershiphub/backend/users/AuthController.java`
- **Database**: Tạo bảng `ROLES` và `USERS` theo DDL SQL trong PostgreSQL.
- **API**: `POST /api/v1/auth/register`, `POST /api/v1/auth/social`, `PUT /api/v1/users/{userId}/role`
- **Authentication**: JWT 15 phút, refresh token 7 ngày, OAuth2 flow.
- **Security**: PreparedStatement, bcrypt, CSRF token, TLS 1.3.

## 3. Hướng dẫn Cụ thể cho Các Agent

- **Coder**: Phát triển mã nguồn Java cho `UserService` và `AuthController`. Không viết test hoặc manifest.
- **Tester**: Tạo bộ test JUnit cho các lớp, test tích hợp API, không sửa mã nguồn.
- **Doc**: Viết tài liệu kiến trúc, sơ đồ ER, quy trình triển khai. Tạo file `.md` trong `./sources/docs/`.
- **Reviewer**: Kiểm tra mã, bảo mật, tuân thủ OWASP, sửa lỗi biên dịch.
- **Docker**: Xây dựng Dockerfile multi‑stage cho `UserService`, tối ưu kích thước < 500 MB.
- **GCP**: Đẩy image lên Google Artifact Registry, triển khai trên Cloud Run.
- **GKE**: Tạo manifest deployment, HPA, service, ingress cho `UserService`.

## 4. Định nghĩa Hoàn thành (DoD)

- Tất cả các API hoạt động đúng theo yêu cầu.
- Kiểm thử unit ≥ 90 % và integration ≥ 80 %.
- Đánh giá OWASP, SonarQube đạt 0 blocker.
- Tài liệu kiến trúc hoàn chỉnh, lưu trữ trong `./sources/docs/`.
- Mã nguồn được commit vào nhánh `features/development-phase-1-day-1` và `features/development-phase-1-day-2`.
- Đã triển khai Docker image và push lên GCR.
- Đã triển khai GKE deployment và kiểm tra HPA.

## 5. LỊCH THỰC HIỆN HÀNG NGÀY

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->TRIỂN KHAI DỊCH VỤ QUẢN LÝ NGƯỜI DÙNG CƠ BẢN<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ 1.1: Triển khai lớp UserService để xử lý đăng ký người dùng mới, tạo bản ghi trong bảng USERS với vai trò mặc định là Student, tuân thủ REQ-001 và ARC-001.  
##### Được giao cho: Coder  
##### Yêu cầu Đường dẫn & Yêu cầu Kỹ thuật:  
* **Đường dẫn Mục tiêu**: ./sources/org/nlh4j/sources/membershiphub/backend/users/UserService.java  
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-001], [ARC-001], [DAT-001], [NFR-001], [NFR-003], [NFR-006], [NFR-008]<!--END_TAGS-->  

#### 📝 Nhiệm vụ 1.2: Viết tài liệu kiến trúc tổng quan cho giai đoạn 1, bao gồm mô hình kiến trúc, sơ đồ ER, và quy trình triển khai.  
##### Được giao cho: Doc  
##### Yêu cầu Đường dẫn & Yêu cầu Kỹ thuật:  
* **Đường dẫn Mục tiêu**: ./sources/docs/phase1_architecture_overview.md  
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-001], [ARC-001], [DAT-001], [NFR-001], [NFR-003], [NFR-006], [NFR-008]<!--END_TAGS-->  

#### 📝 Nhiệm vụ 1.3: Kiểm tra mã nguồn UserService, xác nhận tuân thủ OWASP, kiểm tra lỗi biên dịch.  
##### Được giao cho: Reviewer  
##### Yêu cầu Đường dẫn & Yêu cầu Kỹ thuật:  
* **Đường dẫn Mục tiêu**: ./sources/org/nlh4j/sources/membershiphub/backend/users/UserService.java  
* **Thẻ Tracability**: <!--START_TAGS-->[ARC-001], [DAT-001], [NFR-001], [NFR-003], [NFR-006], [NFR-008]<!--END_TAGS-->  

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->TRIỂN KHAI DỊCH VỤ XÁC THỰC OAUTH2 VÀ JWT<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ 2.1: Triển khai AuthController để xử lý xác thực OAuth2 từ Firebase/Google/Facebook, trao đổi mã lấy thông tin người dùng, cập nhật vai trò và cấp JWT token (ARC-006), đồng thời hỗ trợ phân quyền người dùng (REQ-003).  
##### Được giao cho: Coder  
##### Yêu cầu Đường dẫn & Yêu cầu Kỹ thuật:  
* **Đường dẫn Mục tiêu**: ./sources/org/nlh4j/sources/membershiphub/backend/users/AuthController.java  
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-002], [REQ-003], [ARC-006], [DAT-001], [NFR-001], [NFR-003], [NFR-006], [NFR-008]<!--END_TAGS-->  

#### 📝 Nhiệm vụ 2.2: Xây dựng Dockerfile multi‑stage cho UserService, tối ưu kích thước < 500 MB.  
##### Được giao cho: Docker  
##### Yêu cầu Đường dẫn & Yêu cầu Kỹ thuật:  
* **Đường dẫn Mục tiêu**: ./sources/org/nlh4j/sources/membershiphub/backend/users/Dockerfile  
* **Thẻ Tracability**: <!--START_TAGS-->[ARC-001], [NFR-005], [NFR-006]<!--END_TAGS-->