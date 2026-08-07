# Giai Đoạn 3: <!--PHASE_NAME_START-->Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807042343 |
| **Tên Dự Án** | membership-hub |
| **Giai Đoạn** | 3 |
| **Tên Giai Đoạn** | <!--PHASE_NAME_START-->Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên<!--PHASE_NAME_END--> |
| **Mô Tả** | <!--PHASE_DESC_START-->Xây dựng hệ thống quản lý khóa học, bao gồm tạo, cập nhật, xoá khóa học, kiểm tra xung đột lịch với giáo viên, và gán/giải quyền giáo viên cho khóa học. Hệ thống cung cấp API REST để truy xuất danh sách khóa học, tạo mới, cập nhật, và gán giáo viên, đồng thời thực thi kiểm tra xung đột lịch và bảo mật theo OWASP.<!--PHASE_DESC_END--> |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày/Thời Gian** | 2026/08/07 04:23:43 |
| **Tác Giả** | Enterprise System Architect (SA Agent) |
| **Phê Duyệt** | Pending Technical Governance Review |

## Phạm Vi Hoạt Động & Mục Tiêu Giai Đoạn

Giai đoạn 3 tập trung vào xây dựng toàn bộ chức năng quản lý khóa học, bao gồm:
- Tạo, cập nhật, xoá khóa học với kiểm tra xung đột lịch và tài nguyên.
- Gán và giải quyền giáo viên cho khóa học, đồng thời gửi thông báo push và tin nhắn Zalo.
- Cung cấp API REST `/api/v1/courses` để truy xuất danh sách, tạo mới và gán giáo viên.
- Đảm bảo tuân thủ các yêu cầu bảo mật OWASP, hiệu năng NFR-001, NFR-003, NFR-004 và đầy đủ mapping tag ID.

## Phạm Vi Kỹ Thuật & Giới Hạn Đường Dẫn

- Thư mục dịch vụ backend: `./sources/backend/courses/`
- Thư mục gói Java: `./sources/backend/courses/org/nlh4j/sources/membershiphub/`
- Điểm cuối REST:
  - GET `/api/v1/courses`
  - POST `/api/v1/courses`
  - PUT `/api/v1/courses/{courseId}/teacher/{teacherId}`

## Chỉ Định Chức Năng Đối Tượng Được Giao Nhận

- **Coder**: Đóng vai trò là Nhà phát triển ứng dụng cấp cao. Chịu trách nhiệm triển khai mã nguồn cho cả backend và frontend/mobile. Không viết bộ kiểm thử hoặc manifest.
- **Tester**: Đóng vai trò là QC/QA trưởng. Chuyên về viết bộ kiểm thử, kiểm tra tích hợp, kiểm tra hiệu năng. Không sửa mã nguồn.
- **Doc**: Đóng vai trò là Nhà viết tài liệu kỹ thuật. Chuyên biên soạn tài liệu kỹ thuật, sơ đồ dữ liệu, bản vẽ kiến trúc.
- **Reviewer**: Đóng vai trò là Kiểm tra mã, phân tích tĩnh, vá lỗi bảo mật.
- **Docker**: Đóng vai trò là chuyên gia containerization.
- **GCP**: Đóng vai trò là chuyên gia tự động hóa GCP.
- **GKE**: Đóng vai trò là chuyên gia Kubernetes.

## Định Nghĩa Hoàn Thành Giai Đoạn

- Tất cả các yêu cầu [REQ-007], [REQ-008], [REQ-009] được triển khai và kiểm thử thành công.
- Đạt 100% coverage kiểm thử cho các module liên quan.
- Đảm bảo tuân thủ OWASP Top 10 và NFR-001, NFR-003, NFR-004.
- Kiểm tra toàn bộ mapping tag ID, không có tag chưa được sử dụng.

## Ngày-đến-Ngày Thực Hiện Kiến Trúc

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->XÂY DỰNG CONTROLLER DANH SÁCH KHÓA HỌC<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 1.1: Triển khai CourseController để hiển thị danh sách khóa học (REQ-007) và hỗ trợ CRUD cho System/Center Admin (ARC-003).

##### Được Giao Nhận: Coder

##### Yêu Cầu Thành Phần & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu**: ./sources/backend/courses/org/nlh4j/sources/membershiphub/CourseController.java
* **Thẻ Định Vị Theo Dõi**: <!--START_TAGS-->[REQ-007], [DAT-004], [ARC-003]<!--END_TAGS-->

#### 📝 NHIỆM VỤ 1.2: Tạo tài liệu kiến trúc cho giai đoạn 3

##### Được Giao Nhận: Doc

##### Yêu Cầu Thành Phần & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu**: ./sources/docs/phase3_architecture_overview.md
* **Thẻ Định Vị Theo Dõi**: <!--START_TAGS-->[ARC-003], [DAT-004], [NFR-001], [NFR-003], [NFR-004]<!--END_TAGS-->

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->XÂY DỰNG LOGIC TẠO/CẬP NHẬT KHÓA HỌC<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 2.1: Triển khai CourseService để tạo, cập nhật khóa học, kiểm tra xung đột lịch với giáo viên (REQ-008).

##### Được Giao Nhận: Coder

##### Yêu Cầu Thành Phần & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu**: ./sources/backend/courses/org/nlh4j/sources/membershiphub/CourseService.java
* **Thẻ Định Vị Theo Dõi**: <!--START_TAGS-->[REQ-008], [DAT-004], [ARC-003]<!--END_TAGS-->

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->XÂY DỰNG GÁN/RÚT GIÁO VIÊN VÀ KHÓA HỌC<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 3.1: Triển khai CourseTeacherService để gán/giải quyền giáo viên cho khóa học (REQ-009).

##### Được Giao Nhận: Coder

##### Yêu Cầu Thành Phần & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu**: ./sources/backend/courses/org/nlh4j/sources/membershiphub/CourseTeacherService.java
* **Thẻ Định Vị Theo Dõi**: <!--START_TAGS-->[REQ-009], [DAT-004], [ARC-003]<!--END_TAGS-->