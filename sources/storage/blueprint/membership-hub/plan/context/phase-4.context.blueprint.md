# Giai đoạn 4: Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống | Mô tả: Giai đoạn 4 tập trung vào triển khai toàn bộ chức năng ghi danh học viên, điểm danh qua mã QR, quản lý thẻ hội viên, hệ thống thông báo đa kênh, khuyến mãi và thông báo, cùng với cấu hình và cài đặt hệ thống. Các thành phần chính bao gồm: EnrollmentController và EnrollmentService để xử lý đăng ký khóa học; AttendanceService để ghi nhận điểm danh một cách idempotent; NotificationService để gửi push và tin nhắn Zalo; MembershipController để quản lý thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống. Ngoài ra, giai đoạn này cũng triển khai các bảng dữ liệu liên quan: ENROLLMENTS, ATTENDANCE, STUDENTCARDS, NOTIFICATIONS, PROMOTIONS, ANNOUNCEMENTS, SYSTEMSETTINGS. Mọi giao tiếp API được bảo mật bằng JWT, các truy vấn dữ liệu được tối ưu bằng chỉ mục và chuẩn bị sẵn sàng cho việc mở rộng theo nhu cầu.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807042343 |
| **Tên Dự Án** | membership-hub |
| **Giai Đoạn** | 4 |
| **Tên Giai Đoạn** | Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống |
| **Mô Tả** | Giai đoạn 4 tập trung vào triển khai toàn bộ chức năng ghi danh học viên, điểm danh qua mã QR, quản lý thẻ hội viên, hệ thống thông báo đa kênh, khuyến mãi và thông báo, cùng với cấu hình và cài đặt hệ thống. Các thành phần chính bao gồm: EnrollmentController và EnrollmentService để xử lý đăng ký khóa học; AttendanceService để ghi nhận điểm danh một cách idempotent; NotificationService để gửi push và tin nhắn Zalo; MembershipController để quản lý thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống. Ngoài ra, giai đoạn này cũng triển khai các bảng dữ liệu liên quan: ENROLLMENTS, ATTENDANCE, STUDENTCARDS, NOTIFICATIONS, PROMOTIONS, ANNOUNCEMENTS, SYSTEMSETTINGS. Mọi giao tiếp API được bảo mật bằng JWT, các truy vấn dữ liệu được tối ưu bằng chỉ mục và chuẩn bị sẵn sàng cho việc mở rộng theo nhu cầu. |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày/Thời Gian** | 2026/08/07 04:23:43 |
| **Tác Giả** | Enterprise System Architect (SA Agent) |
| **Phê Duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu giai đoạn

Giai đoạn 4 thực hiện toàn bộ chức năng ghi danh học viên, điểm danh qua mã QR, quản lý thẻ hội viên, hệ thống thông báo đa kênh, khuyến mãi và thông báo, cùng với cấu hình và cài đặt hệ thống. Các thành phần chính bao gồm: EnrollmentController và EnrollmentService để xử lý đăng ký khóa học; AttendanceService để ghi nhận điểm danh một cách idempotent; NotificationService để gửi push và tin nhắn Zalo; MembershipController để quản lý thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống. Ngoài ra, giai đoạn này cũng triển khai các bảng dữ liệu liên quan: ENROLLMENTS, ATTENDANCE, STUDENTCARDS, NOTIFICATIONS, PROMOTIONS, ANNOUNCEMENTS, SYSTEMSETTINGS. Mọi giao tiếp API được bảo mật bằng JWT, các truy vấn dữ liệu được tối ưu bằng chỉ mục và chuẩn bị sẵn sàng cho việc mở rộng theo nhu cầu.

## 2. Phạm vi kỹ thuật và ranh giới thư mục

- Thư mục backend: `./sources/backend/enrollment/`, `./sources/backend/attendance/`, `./sources/backend/notifications/`, `./sources/backend/membership/`
- Thư mục docs: `./sources/docs/`
- Các điểm cuối API:
  - `POST /api/v1/enrollments`
  - `POST /api/v1/attendance/scan`
  - `POST /api/v1/notifications`
  - `POST /api/v1/promotions`
  - `POST /api/v1/announcements`
  - `GET /api/v1/membership/{studentId}/card`
  - `POST /api/v1/membership/renew`

## 3. Hướng dẫn chức năng dành cho từng nhân viên phụ trách

- **Coder**: Đóng vai trò là Nhà phát triển ứng dụng cấp cao. Trách nhiệm triển khai mã nguồn cho các dịch vụ backend và thành phần frontend/mobile. Không viết bộ kiểm thử hoặc manifest.
- **Tester**: Đóng vai trò là Lead/Principal QC/QA. Chuyên về viết bộ kiểm thử, kiểm tra tích hợp, kiểm tra hiệu năng. Không sửa mã nguồn.
- **Reviewer**: Đóng vai trò là Kiểm tra mã, phân tích tĩnh, vá lỗi bảo mật. Kiểm tra chất lượng, sửa lỗi, bảo mật OWASP.
- **Doc**: Đóng vai trò là Technical Writer và Enterprise Systems Architect. Soạn tài liệu kỹ thuật, sơ đồ dữ liệu, quy trình triển khai, và các tiêu chuẩn bảo mật.
- **Docker**: Đóng vai trò là chuyên gia containerization, multi‑stage Dockerfile, tối ưu kích thước, đẩy image lên DockerHub.
- **GCP**: Đóng vai trò là chuyên gia tự động hóa GCP, xây dựng và đẩy image lên Artifact Registry, triển khai trên Cloud Run.
- **GKE**: Đóng vai trò là chuyên gia Kubernetes, xây dựng manifest, HPA, Helm chart, triển khai microservices trên GKE.

## 4. Định nghĩa Hoàn thành (DoD)

- Tất cả các yêu cầu [REQ-010] đến [REQ-018] được triển khai và kiểm thử thành công.
- Mọi API được bảo mật bằng JWT, có thời gian hết hạn 15 phút và refresh token 7 ngày.
- Kiểm thử unit, integration, E2E đạt 100% coverage cho các module liên quan.
- Kiểm tra OWASP Top 10, bảo mật OWASP, và NFR-001, NFR-003, NFR-004, NFR-006 được đáp ứng.
- Tất cả các tag ID được map đầy đủ, không còn tag chưa được sử dụng.
- Tài liệu kỹ thuật hoàn chỉnh, bao gồm sơ đồ dữ liệu, kiến trúc, quy trình triển khai, và hướng dẫn bảo mật.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ NGÀY 1: Xây dựng controller ghi danh khóa học

#### 📝 Mục tiêu 1.0: Khởi tạo tài liệu kiến trúc giai đoạn 4
##### Được giao: Doc
##### Đường dẫn:
* **Đường dẫn**: ./sources/docs/phase4_architecture_overview.md
##### Thẻ theo dõi:
* **Thẻ theo dõi**: <!--START_TAGS-->[ARC-004], [ARC-005], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011], [EXC-001], [EXC-002], [EXC-003], [EXC-005], [NFR-001], [NFR-003], [NFR-004], [NFR-006]<!--END_TAGS-->

#### 📝 Mục tiêu 1.1: Triển khai EnrollmentController
##### Được giao: Coder
##### Đường dẫn:
* **Đường dẫn**: ./sources/backend/enrollment/org/nlh4j/sources/membershiphub/EnrollmentController.java
##### Thẻ theo dõi:
* **Thẻ theo dõi**: <!--START_TAGS-->[ARC-004], [REQ-010], [DAT-005]<!--END_TAGS-->

### 🌤️ NGÀY 2: Triển khai logic đăng ký khóa học

#### 📝 Mục tiêu 2.1: Triển khai EnrollmentService
##### Được giao: Coder
##### Đường dẫn:
* **Đường dẫn**: ./sources/backend/enrollment/org/nlh4j/sources/membershiphub/EnrollmentService.java
##### Thẻ theo dõi:
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-011], [DAT-005], [ARC-005]<!--END_TAGS-->

### 🌤️ NGÀY 3: Triển khai dịch vụ điểm danh QR

#### 📝 Mục tiêu 3.1: Triển khai AttendanceService
##### Được giao: Coder
##### Đường dẫn:
* **Đường dẫn**: ./sources/backend/attendance/org/nlh4j/sources/membershiphub/AttendanceService.java
##### Thẻ theo dõi:
* **Thẻ theo dõi**: <!--START_TAGS-->[ARC-007], [REQ-012], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->

### 🌤️ NGÀY 4: Triển khai dịch vụ thông báo

#### 📝 Mục tiêu 4.1: Triển khai NotificationService
##### Được giao: Coder
##### Đường dẫn:
* **Đường dẫn**: ./sources/backend/notifications/org/nlh4j/sources/membershiphub/NotificationService.java
##### Thẻ theo dõi:
* **Thẻ theo dõi**: <!--START_TAGS-->[ARC-008], [REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->

### 🌤️ NGÀY 5: Triển khai controller thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống

#### 📝 Mục tiêu 5.1: Triển khai MembershipController
##### Được giao: Coder
##### Đường dẫn:
* **Đường dẫn**: ./sources/backend/membership/org/nlh4j/sources/membershiphub/MembershipController.java
##### Thẻ theo dõi:
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->