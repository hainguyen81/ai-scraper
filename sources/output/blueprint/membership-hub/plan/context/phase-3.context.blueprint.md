# Giai đoạn 3: <!--PHASE_NAME_START-->Xây dựng dịch vụ thông báo và khuyến mãi<!--PHASE_NAME_END--> | Mô tả: Xây dựng dịch vụ thông báo và khuyến mãi

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805160938 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng dịch vụ thông báo và khuyến mãi<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Xây dựng dịch vụ thông báo và khuyến mãi<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 16:09:38 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị Kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 3 tập trung vào việc xây dựng dịch vụ thông báo và khuyến mãi. Dịch vụ thông báo sẽ cho phép hệ thống gửi thông báo đến người dùng thông qua ứng dụng di động và nhóm Zalo. Dịch vụ khuyến mãi sẽ cho phép quản trị viên tạo, chỉnh sửa và xóa các chương trình khuyến mãi với ngày bắt đầu và kết thúc.

## 2. Phạm vi kỹ thuật và biên giới thư mục (Tệp, đường dẫn và điểm cuối)
- `./sources/backend/notifications`
- `./sources/backend/promotions`

## 3. Hướng dẫn chức năng của Sub-Agent chuyên dụng
*   **Coder**: Hoạt động như một Lập trình viên Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng khách frontend/mobile. Cấm viết bộ kiểm tra hoặc biểu mẫu cơ sở hạ tầng.
*   **Tester**: Hoạt động như một Trưởng/QA Chất lượng Kiểm soát. Chuyên về kỹ thuật bộ kiểm tra, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm tra JUnit, kiểm tra tích hợp, kiểm tra tự động E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật Chuyên nghiệp và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn các tài liệu kỹ thuật Markdown toàn diện, tham chiếu lược đồ, bản đồ hệ thống và danh mục kiến trúc. Mỗi tệp tài liệu được tạo ra phải nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
    # YÊU CẦU CẤP CAO CỦA ĐẠI LÝ TÀI LIỆU (CỔNG QUAN TRỌNG):
    - Bạn bị CẤM nghiêm ngặt từ bỏ hoặc loại bỏ đại lý 'Doc' khỏi bất kỳ giai đoạn nào được tính toán.
    - Đối với MỖI giai đoạn được tính toán, vào **Ngày 1** của giai đoạn đó, bạn PHẢI phân bổ một nhiệm vụ tài liệu hệ thống cơ bản cho đại lý **Doc**. Nhiệm vụ này PHẢI yêu cầu đại lý 'Doc' lập bản đồ kiến trúc, điểm cuối, lược đồ cơ sở dữ liệu hoặc bản đồ topology triển khai tương ứng với ngăn xếp hoạt động của giai đoạn đó.
    - Thất bại trong việc phân bổ đại lý 'Doc' vào Ngày 1 của bất kỳ giai đoạn nào sẽ gây ra vi phạm hợp đồng kỹ thuật thảm khốc.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng microservices vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này.
- Đảm bảo 100% tuân thủ các tiêu chuẩn bảo mật OWASP.
- Đảm bảo 100% độ phủ kiểm tra chức năng cho các yêu cầu được phân bổ.
- Đảm bảo 100% ánh xạ ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 5: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ THÔNG BÁO<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 5.1: <!--SUB_TASK_START-->Triển khai dịch vụ thông báo<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notifications`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-016], [DAT-008]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.2: <!--SUB_TASK_START-->Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ thông báo<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notifications;./sources/backend/notifications/src/test/java/org/nlh4j/saas/membershiphub/notifications/NotificationServiceTest.java`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.3: <!--SUB_TASK_START-->Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notifications`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

### 🌤️ Ngày 6: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ KHUYẾN MÃI<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 6.1: <!--SUB_TASK_START-->Triển khai dịch vụ khuyến mãi và thông báo<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/promotions`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-017], [REQ-018], [DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 6.2: <!--SUB_TASK_START-->Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ khuyến mãi và thông báo<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/promotions;./sources/backend/promotions/src/test/java/org/nlh4j/saas/membershiphub/promotions/PromotionServiceTest.java`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-017], [REQ-018]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 6.3: <!--SUB_TASK_START-->Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/promotions`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-017], [REQ-018]<!--END_TAGS-->