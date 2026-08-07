# Giai đoạn 1: <!--PHASE_NAME_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản<!--PHASE_NAME_END-->

## 📊 Kiểm Soát Tài Liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807042343 |
| **Tên Dự Án** | membership-hub |
| **Giai Đoạn** | 1 |
| **Tên Giai Đoạn** | <!--PHASE_NAME_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản<!--PHASE_NAME_END--> |
| **Mô Tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc triển khai dịch vụ quản lý người dùng, xác thực, và phân quyền, bao gồm đăng ký, OAuth2, JWT, và kiểm tra đầu vào, đồng thời chuẩn bị tài liệu kiến trúc chi tiết cho toàn bộ hệ thống.<!--PHASE_DESC_END--> |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày/Thời Gian** | 2026/08/07 04:23:43 |
| **Tác Giả** | Enterprise System Architect (SA Agent) |
| **Phê Duyệt** | Pending Technical Governance Review |

## 1. Phạm Vi và Mục Tiêu Hoạt Động Giai Đoạn

Giai đoạn 1 thực hiện toàn bộ chức năng quản lý người dùng, bao gồm đăng ký, xác thực OAuth2, cấp JWT, và phân quyền. Các thành phần chính bao gồm `UserService`, `AuthController`, và bảng dữ liệu `USERS`/`ROLES`. Mọi thao tác đều tuân thủ OWASP Top 10, bao gồm kiểm tra đầu vào, mã hóa mật khẩu, prepared statements, CSRF, và XSS.

## 2. Phạm Vi Kỹ Thuật & Ranh Giới Đường Dẫn Cho Phép

- **Backend**: `./sources/org/nlh4j/saas/membershiphub/users/` (Java, Quarkus)
- **Database**: PostgreSQL, bảng `USERS`, `ROLES`
- **API**: `/api/v1/auth/register`, `/api/v1/auth/social`, `/api/v1/users/{userId}/role`
- **Security**: JWT 15 phút, refresh 7 ngày, OAuth2 (Firebase, Google, Facebook)

## 3. Hướng Dẫn Hoạt Động Đặc Biệt cho Các Đại Diện Phụ

- **Doc**: Tài liệu kiến trúc, sơ đồ dữ liệu, quy trình triển khai.
- **Coder**: Viết mã nguồn Java, kiểm tra đầu vào, bảo mật OWASP.
- **Tester**: Kiểm thử đơn vị, tích hợp, bảo mật.
- **Reviewer**: Kiểm tra mã, bảo mật, tuân thủ OWASP.
- **Docker**: Xây dựng Dockerfile, multi‑stage, tối ưu kích thước.
- **GCP**: Đẩy image lên Artifact Registry, triển khai Cloud Run.
- **GKE**: Tạo manifest, HPA, Helm chart.

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)

- Tất cả các yêu cầu [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006] được triển khai và kiểm thử.
- Đảm bảo OWASP Top 10: CSRF, XSS, SQLi, bảo mật JWT.
- Độ phủ kiểm thử ≥ 85 %, báo cáo SonarQube không có blocker.
- Tài liệu kiến trúc hoàn chỉnh, bản vẽ ERD, và hướng dẫn triển khai.
- Mã nguồn được commit vào nhánh `features/development-phase-1-day-1` và `features/development-phase-1-day-2`.

## 5. Nhật Ký Thực Hiện Kiến Trúc Theo Ngày

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ NGƯỜI DÙNG<!--DAY_HEADER_END-->

#### 📝 Nhiệm Vụ 1.1: Khởi tạo, thiết kế và lập bản đồ toàn bộ tài liệu kỹ thuật, bản vẽ kiến trúc, cấu trúc dữ liệu, và kiến trúc triển khai cho giai đoạn này, bao gồm mô tả chi tiết các thành phần, luồng dữ liệu, và quy trình triển khai.
##### Đại Diện Phụ: Doc
##### Đường Dẫn Mục Tiêu: ./sources/docs/phase1_technical_overview.md
##### Thẻ Định Vị: <!--START_TAGS-->[ARC-001], [ARC-006], [REQ-001], [REQ-002], [REQ-003], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006], [NFR-008]<!--END_TAGS-->

#### 📝 Nhiệm Vụ 1.2: Triển khai lớp UserService để xử lý đăng ký người dùng mới, tạo bản ghi trong bảng USERS với vai trò mặc định là Student, tuân thủ REQ-001 và ARC-001, đồng thời áp dụng OWASP bảo mật: kiểm tra đầu vào, mã hóa mật khẩu, sử dụng prepared statements, và bảo vệ CSRF.
##### Đại Diện Phụ: Coder
##### Đường Dẫn Mục Tiêu: ./sources/org/nlh4j/saas/membershiphub/users/UserService.java
##### Thẻ Định Vị: <!--START_TAGS-->[ARC-001], [REQ-001], [DAT-001]<!--END_TAGS-->

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->XÂY DỰNG XÁC THỰC OAUTH2<!--DAY_HEADER_END-->

#### 📝 Nhiệm Vụ 2.1: Xây dựng AuthController để xử lý xác thực OAuth2 từ Firebase/Google/Facebook, trao đổi mã lấy thông tin người dùng, cập nhật vai trò và cấp JWT token (ARC-006), đồng thời hỗ trợ phân quyền người dùng (REQ-003), thực hiện kiểm tra đầu vào, mã hóa mật khẩu, bảo vệ CSRF, và tuân thủ OWASP.
##### Đại Diện Phụ: Coder
##### Đường Dẫn Mục Tiêu: ./sources/org/nlh4j/saas/membershiphub/users/AuthController.java
##### Thẻ Định Vị: <!--START_TAGS-->[ARC-006], [REQ-002], [REQ-003], [DAT-001]<!--END_TAGS-->