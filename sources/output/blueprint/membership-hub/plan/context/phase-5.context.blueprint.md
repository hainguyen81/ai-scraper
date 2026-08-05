# Giai đoạn 5: <!--PHASE_NAME_START-->Triển khai các tính năng báo cáo, phân tích, bản địa hóa, SEO<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805144718 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai các tính năng báo cáo, phân tích, bản địa hóa, SEO<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai các tính năng báo cáo, phân tích, bản địa hóa, SEO<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 14:47:18 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 5 tập trung vào việc triển khai các tính năng báo cáo, phân tích và bản địa hóa, SEO. Các nhiệm vụ chính bao gồm:
- Triển khai các tính năng tạo báo cáo điểm danh, bảng điều khiển tóm tắt ghi danh
- Triển khai các tính năng phát hiện ngôn ngữ mặc định, SEO đa ngôn ngữ

## 2. Phạm vi kỹ thuật và biên giới thư mục (Thư mục, đường dẫn và điểm cuối)
- `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java`
- `./sources/backend/i18n-service/src/main/java/org/nlh4j/saas/membershiphub/i18n/I18nService.java`

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

### DAY 3: <!--DAY_HEADER_START-->TRIỂN KHAI CÁC TÍNH NĂNG BÁO CÁO VÀ PHÂN TÍCH<!--DAY_HEADER_END-->

#### SUB-TASK 3.1: Triển khai các tính năng tạo báo cáo điểm danh, bảng điều khiển tóm tắt ghi danh
##### Sub-Agent được chỉ định: Coder
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-024], [REQ-025]<!--END_TAGS-->

#### SUB-TASK 3.2: Viết các test case cho các tính năng báo cáo và phân tích
##### Sub-Agent được chỉ định: Tester
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/report-service/src/test/java/org/nlh4j/saas/membershiphub/report/ReportServiceTest.java;./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-024], [REQ-025]<!--END_TAGS-->

#### SUB-TASK 3.3: Review code cho các tính năng báo cáo và phân tích
##### Sub-Agent được chỉ định: Reviewer
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-024], [REQ-025]<!--END_TAGS-->

### DAY 4: <!--DAY_HEADER_START-->TRIỂN KHAI CÁC TÍNH NĂNG BẢN ĐỊA HÓA VÀ SEO<!--DAY_HEADER_END-->

#### SUB-TASK 4.1: Triển khai các tính năng phát hiện ngôn ngữ mặc định, SEO đa ngôn ngữ
##### Sub-Agent được chỉ định: Coder
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/i18n-service/src/main/java/org/nlh4j/saas/membershiphub/i18n/I18nService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-022], [REQ-023]<!--END_TAGS-->

#### SUB-TASK 4.2: Viết các test case cho các tính năng bản địa hóa và SEO
##### Sub-Agent được chỉ định: Tester
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/i18n-service/src/test/java/org/nlh4j/saas/membershiphub/i18n/I18nServiceTest.java;./sources/backend/i18n-service/src/main/java/org/nlh4j/saas/membershiphub/i18n/I18nService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-022], [REQ-023]<!--END_TAGS-->

#### SUB-TASK 4.3: Review code cho các tính năng bản địa hóa và SEO
##### Sub-Agent được chỉ định: Reviewer
##### Yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/backend/i18n-service/src/main/java/org/nlh4j/saas/membershiphub/i18n/I18nService.java`
* **Token Tag Tracibility:** <!--START_TAGS-->[REQ-022], [REQ-023]<!--END_TAGS-->