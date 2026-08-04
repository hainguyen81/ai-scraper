# Giai Đoạn 2: <!--PHASE_NAME_START-->QuanLyNguoiDungVaTrungTam<!--PHASE_NAME_END--> | Mô Tả: Triển khai các tính năng quản lý người dùng, quản lý trung tâm, quản lý khóa học

## 📊 Document Control

| Mục | Chi Tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260804145722 |
| **Tên Dự Án** | membership-hub |
| **Giai Đoạn** | 2 |
| **Tên Giai Đoạn** | <!--PHASE_NAME_START-->QuanLyNguoiDungVaTrungTam<!--PHASE_NAME_END--> |
| **Mô Tả** | Triển khai các tính năng quản lý người dùng, quản lý trung tâm, quản lý khóa học |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/04 14:57:22 |
| **Tác Giả** | Kiến Trúc Sư Hệ Thống Doanh Nghiệp (SA Agent) |
| **Phê Duyệt** | Đang chờ xem xét của Ban Quản Trị Kỹ Thuật |

## 1. Phạm Vi Hoạt Động và Mục Tiêu của Giai Đoạn
Giai đoạn này tập trung vào việc triển khai các tính năng quản lý người dùng, quản lý trung tâm, và quản lý khóa học. Các nhiệm vụ bao gồm:
- Triển khai các dịch vụ đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
- Triển khai các dịch vụ xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm
- Triển khai các dịch vụ xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học

## 2. Phạm Vi Kỹ Thuật và Ranh Giới Thư Mục (Files, paths, và endpoints)
- **Backend:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/user`, `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/center`, `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course`
- **Frontend:** `./sources/frontend/src/components/user`, `./sources/frontend/src/components/center`, `./sources/frontend/src/components/course`

## 3. Hướng Dẫn Chức Năng Đặc Biệt cho Các Đặc Sứ Đặc Biệt
- **Coder:** Triển khai các dịch vụ đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng, xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm, xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học
- **Tester:** Viết các test case cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng, xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm, xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học
- **Reviewer:** Review code cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng, xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm, xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP
- Đảm bảo độ phủ kiểm thử chức năng hoàn chỉnh cho các yêu cầu được phân bổ
- Đảm bảo 100% ánh xạ ID Tag

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### DAY 4: <!--DAY_HEADER_START-->TRIỂN KHAI CÁC TÍNH NĂNG QUẢN LÝ NGƯỜI DÙNG<!--DAY_HEADER_END-->

#### SUB-TASK 4.1: Triển khai các dịch vụ đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
##### Đặc Sứ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/user`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003]<!--END_TAGS-->

#### SUB-TASK 4.2: Viết các test case cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
##### Đặc Sứ Được Phân Công: Tester
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/user;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/user`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003]<!--END_TAGS-->

#### SUB-TASK 4.3: Review code cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
##### Đặc Sứ Được Phân Công: Reviewer
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/user`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003]<!--END_TAGS-->

### DAY 5: <!--DAY_HEADER_START-->TRIỂN KHAI CÁC TÍNH NĂNG QUẢN LÝ TRUNG TÂM<!--DAY_HEADER_END-->

#### SUB-TASK 5.1: Triển khai các dịch vụ xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm
##### Đặc Sứ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/center`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->

#### SUB-TASK 5.2: Viết các test case cho các tính năng xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm
##### Đặc Sứ Được Phân Công: Tester
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/center;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/center`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->

#### SUB-TASK 5.3: Review code cho các tính năng xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm
##### Đặc Sứ Được Phân Công: Reviewer
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/center`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->

### DAY 6: <!--DAY_HEADER_START-->TRIỂN KHAI CÁC TÍNH NĂNG QUẢN LÝ KHÓA HỌC<!--DAY_HEADER_END-->

#### SUB-TASK 6.1: Triển khai các dịch vụ xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học
##### Đặc Sứ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->

#### SUB-TASK 6.2: Viết các test case cho các tính năng xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học
##### Đặc Sứ Được Phân Công: Tester
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/course;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->

#### SUB-TASK 6.3: Review code cho các tính năng xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học
##### Đặc Sứ Được Phân Công: Reviewer
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->