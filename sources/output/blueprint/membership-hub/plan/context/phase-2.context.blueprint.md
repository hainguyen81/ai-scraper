# Giai đoạn 2: <!--PHASE_NAME_START-->trien_khai_quan_ly_nguoi_dung_trung_tam_khoa_hoc<!--PHASE_NAME_END--> | Mô tả: Triển khai các tính năng quản lý người dùng, quản lý trung tâm, quản lý khóa học
## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260804142715 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->trien_khai_quan_ly_nguoi_dung_trung_tam_khoa_hoc<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai các tính năng quản lý người dùng, quản lý trung tâm, quản lý khóa học |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/04 14:27:15 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 2 tập trung vào việc triển khai các tính năng quản lý người dùng, quản lý trung tâm và quản lý khóa học. Các nhiệm vụ chính bao gồm:
- Triển khai các dịch vụ đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
- Triển khai các dịch vụ xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm
- Triển khai các dịch vụ xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép
- `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/user`
- `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/center`
- `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course`

## 3. Hướng dẫn chức năng dành riêng cho các tác vụ con
- **Coder:** Triển khai các dịch vụ đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng, xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm, xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học.
- **Tester:** Viết các test case cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng, xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm, xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học.
- **Reviewer:** Review code cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng, xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm, xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
- Hoàn thành việc triển khai các tính năng quản lý người dùng, quản lý trung tâm và quản lý khóa học.
- Đảm bảo 100% tuân thủ các tiêu chuẩn OWASP.
- Hoàn thành các bài kiểm tra chức năng cho các yêu cầu được phân bổ.
- Đảm bảo 100% ánh xạ ID Tag.

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### DAY 4: <!--DAY_HEADER_START-->TRIEN_KHAI_QUAN_LY_NGUOI_DUNG<!--DAY_HEADER_END-->

#### SUB-TASK 4.1: Triển khai các dịch vụ đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
##### Tác vụ con được giao: Coder
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/user`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003]<!--END_TAGS-->

#### SUB-TASK 4.2: Viết các test case cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
##### Tác vụ con được giao: Tester
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/user;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/user`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003]<!--END_TAGS-->

#### SUB-TASK 4.3: Review code cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
##### Tác vụ con được giao: Reviewer
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/user`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003]<!--END_TAGS-->

### DAY 5: <!--DAY_HEADER_START-->TRIEN_KHAI_QUAN_LY_TRUNG_TAM<!--DAY_HEADER_END-->

#### SUB-TASK 5.1: Triển khai các dịch vụ xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm
##### Tác vụ con được giao: Coder
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/center`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->

#### SUB-TASK 5.2: Viết các test case cho các tính năng xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm
##### Tác vụ con được giao: Tester
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/center;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/center`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->

#### SUB-TASK 5.3: Review code cho các tính năng xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm, phân quyền quản trị trung tâm
##### Tác vụ con được giao: Reviewer
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/center`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->

### DAY 6: <!--DAY_HEADER_START-->TRIEN_KHAI_QUAN_LY_KHOA_HOC<!--DAY_HEADER_END-->

#### SUB-TASK 6.1: Triển khai các dịch vụ xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học
##### Tác vụ con được giao: Coder
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->

#### SUB-TASK 6.2: Viết các test case cho các tính năng xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học
##### Tác vụ con được giao: Tester
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/course;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->

#### SUB-TASK 6.3: Review code cho các tính năng xem danh sách khóa học, tạo/cập nhật/xóa khóa học, phân công giáo viên vào khóa học
##### Tác vụ con được giao: Reviewer
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/course`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009]<!--END_TAGS-->