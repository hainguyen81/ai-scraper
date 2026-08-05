# Giai đoạn 3: <!--PHASE_NAME_START-->Xây dựng dịch vụ thông báo và khuyến mãi<!--PHASE_NAME_END--> | Mô tả: Giai đoạn này tập trung vào việc xây dựng dịch vụ thông báo và khuyến mãi. Chúng tôi sẽ xây dựng dịch vụ thông báo để gửi thông báo đến người dùng qua ứng dụng di động và nhóm Zalo. Dịch vụ thông báo sẽ cho phép quản trị viên tạo thông báo mới và gửi đến người dùng cụ thể hoặc toàn bộ người dùng. Dịch vụ khuyến mãi sẽ cho phép quản trị viên tạo mã khuyến mãi với ngày bắt đầu và kết thúc, và hiển thị các khuyến mãi hiện tại cho người dùng.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805153934 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng dịch vụ thông báo và khuyến mãi<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng dịch vụ thông báo và khuyến mãi. Chúng tôi sẽ xây dựng dịch vụ thông báo để gửi thông báo đến người dùng qua ứng dụng di động và nhóm Zalo. Dịch vụ thông báo sẽ cho phép quản trị viên tạo thông báo mới và gửi đến người dùng cụ thể hoặc toàn bộ người dùng. Dịch vụ khuyến mãi sẽ cho phép quản trị viên tạo mã khuyến mãi với ngày bắt đầu và kết thúc, và hiển thị các khuyến mãi hiện tại cho người dùng.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 15:39:34 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị Kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 3 tập trung vào việc xây dựng dịch vụ thông báo và khuyến mãi. Chúng tôi sẽ xây dựng dịch vụ thông báo để gửi thông báo đến người dùng qua ứng dụng di động và nhóm Zalo. Dịch vụ thông báo sẽ cho phép quản trị viên tạo thông báo mới và gửi đến người dùng cụ thể hoặc toàn bộ người dùng. Dịch vụ khuyến mãi sẽ cho phép quản trị viên tạo mã khuyến mãi với ngày bắt đầu và kết thúc, và hiển thị các khuyến mãi hiện tại cho người dùng.

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép (Tệp, đường dẫn và điểm cuối)
- `./sources/backend/notifications`
- `./sources/backend/promotions`

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

### DAY 5: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ THÔNG BÁO<!--DAY_HEADER_END-->

#### SUB-TASK 5.1: Triển khai dịch vụ thông báo
##### Chuyên viên được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notifications`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016], [DAT-008]<!--END_TAGS-->

#### SUB-TASK 5.2: Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ thông báo
##### Chuyên viên được chỉ định: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notifications;./sources/backend/notifications/src/test/java/org/nlh4j/saas/membershiphub/notifications/NotificationServiceTest.java`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

#### SUB-TASK 5.3: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### Chuyên viên được chỉ định: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notifications`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

### DAY 6: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ KHUYẾN MÃI<!--DAY_HEADER_END-->

#### SUB-TASK 6.1: Triển khai dịch vụ khuyến mãi và thông báo
##### Chuyên viên được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/promotions`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-017], [REQ-018], [DAT-009]<!--END_TAGS-->

#### SUB-TASK 6.2: Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ khuyến mãi và thông báo
##### Chuyên viên được chỉ định: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/promotions;./sources/backend/promotions/src/test/java/org/nlh4j/saas/membershiphub/promotions/PromotionServiceTest.java`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-017], [REQ-018]<!--END_TAGS-->

#### SUB-TASK 6.3: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### Chuyên viên được chỉ định: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/promotions`
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-017], [REQ-018]<!--END_TAGS-->