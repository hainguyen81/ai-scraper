# Giai đoạn 3: <!--PHASE_NAME_START-->Triển khai các tính năng đăng ký học viên, điểm danh QR, quản lý thẻ hội viên<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805144718 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai các tính năng đăng ký học viên, điểm danh QR, quản lý thẻ hội viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai các tính năng đăng ký học viên, điểm danh QR, quản lý thẻ hội viên<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 14:47:18 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 3 tập trung vào việc triển khai các tính năng đăng ký học viên, điểm danh QR và quản lý thẻ hội viên. Các nhiệm vụ chính bao gồm:
- Triển khai các tính năng duyệt khóa học, đăng ký khóa học của học viên
- Triển khai các tính năng chụp ảnh điểm danh QR, tính chất bất biến của điểm danh
- Triển khai các tính năng hiển thị tính hợp lệ của thẻ, gia hạn thẻ

## 2. Phạm vi kỹ thuật và biên giới thư mục (Thư mục, đường dẫn và điểm cuối)
- `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java`
- `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java`
- `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Lập trình viên Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
*   **Tester**: Hoạt động như một Chuyên viên Kiểm thử Chất lượng Cấp cao/QA. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng kiểm soát chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng.
*   **Reviewer**: Trách nhiệm về việc xác minh biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về các bài kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chướng ngại vật cổng chất lượng SonarQube.
*   **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật Cấp cao và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về việc biên soạn các tài liệu kỹ thuật Markdown toàn diện, tài liệu tham khảo lược đồ, bản đồ hệ thống và danh mục kiến trúc. Mỗi tệp tài liệu được tạo ra phải nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Docker**: Chuyên về việc container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng microservices vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này
- Đảm bảo tuân thủ các tiêu chuẩn doanh nghiệp OWASP
- Hoàn thành 100% bộ kiểm thử chức năng cho các yêu cầu được phân bổ
- Hoàn thành 100% ánh xạ ID Tag

## 5. Nhật ký thực thi kiến trúc theo ngày

### DAY 6: <!--DAY_HEADER_START-->TRIỂN KHAI CÁC TÍNH NĂNG ĐĂNG KÝ HỌC VIÊN VÀ ĐIỂM DANH QR<!--DAY_HEADER_END-->

#### SUB-TASK 6.1: Triển khai các tính năng duyệt khóa học, đăng ký khóa học của học viên
##### Sub-Agent được chỉ định: Coder
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

#### SUB-TASK 6.2: Viết các test case cho các tính năng đăng ký học viên
##### Sub-Agent được chỉ định: Tester
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollment-service/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentServiceTest.java;./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

#### SUB-TASK 6.3: Review code cho các tính năng đăng ký học viên
##### Sub-Agent được chỉ định: Reviewer
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

#### SUB-TASK 6.4: Triển khai các tính năng chụp ảnh điểm danh QR, tính chất bất biến của điểm danh
##### Sub-Agent được chỉ định: Coder
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-012], [REQ-013]<!--END_TAGS-->

#### SUB-TASK 6.5: Viết các test case cho các tính năng điểm danh QR
##### Sub-Agent được chỉ định: Tester
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/attendance-service/src/test/java/org/nlh4j/saas/membershiphub/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-012], [REQ-013]<!--END_TAGS-->

#### SUB-TASK 6.6: Review code cho các tính năng điểm danh QR
##### Sub-Agent được chỉ định: Reviewer
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-012], [REQ-013]<!--END_TAGS-->

### DAY 7: <!--DAY_HEADER_START-->TRIỂN KHAI CÁC TÍNH NĂNG QUẢN LÝ THẺ HỘI VIÊN<!--DAY_HEADER_END-->

#### SUB-TASK 7.1: Triển khai các tính năng hiển thị tính hợp lệ của thẻ, gia hạn thẻ
##### Sub-Agent được chỉ định: Coder
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->

#### SUB-TASK 7.2: Viết các test case cho các tính năng quản lý thẻ hội viên
##### Sub-Agent được chỉ định: Tester
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/card-service/src/test/java/org/nlh4j/saas/membershiphub/card/CardServiceTest.java;./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->

#### SUB-TASK 7.3: Review code cho các tính năng quản lý thẻ hội viên
##### Sub-Agent được chỉ định: Reviewer
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->