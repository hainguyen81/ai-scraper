# Giai Đoạn 3: <!--PHASE_NAME_START-->DangKyVaGhiDanhHocVienDiemDanhVaQuanLyTheHoiVien<!--PHASE_NAME_END--> | Mô Tả: Triển khai các tính năng đăng ký và ghi danh học viên, điểm danh và quét mã QR

## 📊 Document Control

| Mục | Chi Tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260804145722 |
| **Tên Dự Án** | membership-hub |
| **Giai Đoạn** | 3 |
| **Tên Giai Đoạn** | <!--PHASE_NAME_START-->DangKyVaGhiDanhHocVienDiemDanhVaQuanLyTheHoiVien<!--PHASE_NAME_END--> |
| **Mô Tả** | Triển khai các tính năng đăng ký và ghi danh học viên, điểm danh và quét mã QR |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/04 14:57:22 |
| **Tác Giả** | Kiến Trúc Sư Hệ Thống Doanh Nghiệp (SA Agent) |
| **Phê Duyệt** | Đang chờ xem xét của Ban Quản Trị Kỹ Thuật |

## 1. Phạm Vi Hoạt Động và Mục Tiêu của Giai Đoạn
Giai đoạn này tập trung vào việc triển khai các tính năng đăng ký và ghi danh học viên, điểm danh và quét mã QR. Các nhiệm vụ bao gồm:
- Triển khai các dịch vụ duyệt khóa học, đăng ký khóa học của học viên
- Triển khai các dịch vụ chụp ảnh điểm danh QR, tính chất bất biến của điểm danh
- Tích hợp các tính năng điểm danh và quét mã QR với ứng dụng di động

## 2. Phạm Vi Kỹ Thuật và Ranh Giới Thư Mục (Files, paths, và endpoints)
- **Backend:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/enrollment`, `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/attendance`
- **Frontend:** `./sources/frontend/src/components/enrollment`, `./sources/frontend/src/components/attendance`

## 3. Hướng Dẫn Chức Năng Đặc Biệt cho Các Đặc Sứ Đặc Biệt
- **Coder:** Triển khai các dịch vụ duyệt khóa học, đăng ký khóa học của học viên, chụp ảnh điểm danh QR, tính chất bất biến của điểm danh
- **Tester:** Viết các test case cho các tính năng duyệt khóa học, đăng ký khóa học của học viên, chụp ảnh điểm danh QR, tính chất bất biến của điểm danh
- **Reviewer:** Review code cho các tính năng duyệt khóa học, đăng ký khóa học của học viên, chụp ảnh điểm danh QR, tính chất bất biến của điểm danh

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP
- Đảm bảo độ phủ kiểm thử chức năng hoàn chỉnh cho các yêu cầu được phân bổ
- Đảm bảo 100% ánh xạ ID Tag

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### DAY 7: <!--DAY_HEADER_START-->TRIỂN KHAI CÁC TÍNH NĂNG ĐĂNG KÝ VÀ GHI DANH HỌC VIÊN<!--DAY_HEADER_END-->

#### SUB-TASK 7.1: Triển khai các dịch vụ duyệt khóa học, đăng ký khóa học của học viên
##### Đặc Sứ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/enrollment`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

#### SUB-TASK 7.2: Viết các test case cho các tính năng duyệt khóa học, đăng ký khóa học của học viên
##### Đặc Sứ Được Phân Công: Tester
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/enrollment;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/enrollment`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

#### SUB-TASK 7.3: Review code cho các tính năng duyệt khóa học, đăng ký khóa học của học viên
##### Đặc Sứ Được Phân Công: Reviewer
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/enrollment`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

### DAY 8: <!--DAY_HEADER_START-->TRIỂN KHAI CÁC TÍNH NĂNG ĐIỂM DANH VÀ QUÉT MÃ QR<!--DAY_HEADER_END-->

#### SUB-TASK 8.1: Triển khai các dịch vụ chụp ảnh điểm danh QR, tính chất bất biến của điểm danh
##### Đặc Sứ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/attendance`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002]<!--END_TAGS-->

#### SUB-TASK 8.2: Viết các test case cho các tính năng chụp ảnh điểm danh QR, tính chất bất biến của điểm danh
##### Đặc Sứ Được Phân Công: Tester
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/attendance;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/attendance`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002]<!--END_TAGS-->

#### SUB-TASK 8.3: Review code cho các tính năng chụp ảnh điểm danh QR, tính chất bất biến của điểm danh
##### Đặc Sứ Được Phân Công: Reviewer
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/attendance`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002]<!--END_TAGS-->

### DAY 9: <!--DAY_HEADER_START-->TÍCH HỢP CÁC TÍNH NĂNG ĐIỂM DANH VÀ QUÉT MÃ QR VỚI ỨNG DỤNG DI ĐỘNG<!--DAY_HEADER_END-->

#### SUB-TASK 9.1: Tích hợp các tính năng điểm danh và quét mã QR với ứng dụng di động
##### Đặc Sứ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/frontend/src/components/attendance`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002]<!--END_TAGS-->

#### SUB-TASK 9.2: Viết các test case cho các tính năng điểm danh và quét mã QR trên ứng dụng di động
##### Đặc Sứ Được Phân Công: Tester
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/frontend/src/components/attendance;./sources/frontend/src/components/attendance`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002]<!--END_TAGS-->

#### SUB-TASK 9.3: Review code cho các tính năng điểm danh và quét mã QR trên ứng dụng di động
##### Đặc Sứ Được Phân Công: Reviewer
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/frontend/src/components/attendance`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002]<!--END_TAGS-->