# Giai đoạn 4: <!--PHASE_NAME_START-->Xây dựng giao diện người dùng và ứng dụng di động<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805153934 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng giao diện người dùng và ứng dụng di động<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng giao diện người dùng và ứng dụng di động. Chúng tôi sẽ xây dựng giao diện người dùng để hiển thị thông tin về các khóa học, giáo viên, trung tâm và trạng thái tài khoản. Ứng dụng di động sẽ cho phép người dùng quét mã QR để điểm danh, nhận thông báo đẩy và tương tác với chatbot AI.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 15:39:34 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị Kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 4 tập trung vào việc xây dựng giao diện người dùng và ứng dụng di động. Chúng tôi sẽ xây dựng giao diện người dùng để hiển thị thông tin về các khóa học, giáo viên, trung tâm và trạng thái tài khoản. Ứng dụng di động sẽ cho phép người dùng quét mã QR để điểm danh, nhận thông báo đẩy và tương tác với chatbot AI.

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép (Tệp, đường dẫn và điểm cuối)
- `./sources/frontend`
- `./sources/mobile`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chủ tịch. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và các ứng dụng frontend/mobile. Cấm viết bộ kiểm tra hoặc biểu mẫu cơ sở hạ tầng.
*   **Tester**: Hoạt động như một Trưởng/Chủ tịch QC/QA. Chuyên về kỹ thuật bộ kiểm tra, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm tra JUnit, kiểm tra tích hợp, kiểm tra tự động E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng.
*   **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Doc**: Chức năng như một Nhà viết Kỹ thuật Cấp cao và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn các tài liệu kỹ thuật Markdown toàn diện, tham chiếu lược đồ, bản đồ hệ thống và danh mục kiến trúc. Mỗi tệp tài liệu được tạo ra phải nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng microservices vào các cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% bộ kiểm tra chức năng cho các yêu cầu được phân bổ.
- Hoàn thành 100% kiểm tra ánh xạ Tag ID.

## 5. Nhật ký thực thi kiến trúc theo ngày

### DAY 7: <!--DAY_HEADER_START-->XÂY DỰNG GIAO DIỆN NGƯỜI DÙNG VÀ ỨNG DỤNG DI ĐỘNG<!--DAY_HEADER_END-->

#### SUB-TASK 7.1: Triển khai giao diện người dùng và ứng dụng di động
##### Chuyên viên được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]<!--END_TAGS-->

#### SUB-TASK 7.2: Viết các bài kiểm tra đơn vị và tích hợp cho giao diện người dùng và ứng dụng di động
##### Chuyên viên được chỉ định: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend;./sources/frontend/src/test/java/org/nlh4j/saas/membershiphub/frontend/FrontendServiceTest.java`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]<!--END_TAGS-->

#### SUB-TASK 7.3: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### Chuyên viên được chỉ định: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]<!--END_TAGS-->