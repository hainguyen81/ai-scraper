# Giai đoạn 4: <!--PHASE_NAME_START-->Xây dựng giao diện người dùng và ứng dụng di động<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805155024 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng giao diện người dùng và ứng dụng di động<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Xây dựng giao diện người dùng và ứng dụng di động<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 15:50:24 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 4 tập trung vào việc xây dựng giao diện người dùng và ứng dụng di động. Giao diện người dùng sẽ bao gồm các trang web và ứng dụng di động cho phép người dùng tương tác với hệ thống. Ứng dụng di động sẽ cung cấp các tính năng như quét mã QR để điểm danh, xem thông báo và quản lý thẻ hội viên.

## 2. Phạm vi kỹ thuật và biên giới thư mục (Tệp, đường dẫn và điểm cuối)
- `./sources/frontend`
- `./sources/mobile`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và các ứng dụng frontend/mobile. Cấm viết bộ kiểm tra hoặc biểu mẫu cơ sở hạ tầng.
*   **Tester**: Hoạt động như một Nhà kiểm soát chất lượng/Chuyên gia QC/QA Cấp cao. Chuyên về kỹ thuật bộ kiểm tra, xác nhận và cổng chất lượng. Trách nhiệm là tạo các bộ kiểm tra JUnit, kiểm tra tích hợp, tự động hóa kiểm tra E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Doc**: Chức năng như một Nhà viết tài liệu kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn các tài liệu kỹ thuật Markdown toàn diện, tham chiếu lược đồ, bản đồ hệ thống và danh mục kiến trúc. Mỗi tệp tài liệu được tạo ra phải nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng microservices vào các cụm GKE hoạt động.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn 4.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP doanh nghiệp.
- Đảm bảo độ phủ kiểm tra chức năng hoàn chỉnh cho các yêu cầu được phân bổ.
- Đảm bảo 100% ánh xạ ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 7: <!--DAY_HEADER_START-->XÂY DỰNG GIAO DIỆN NGƯỜI DÙNG VÀ ỨNG DỤNG DI ĐỘNG<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 7.1: Triển khai giao diện người dùng và ứng dụng di động
##### Người phụ trách: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend`
* **Token theo dõi:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.2: Viết các bài kiểm tra đơn vị và tích hợp cho giao diện người dùng và ứng dụng di động
##### Người phụ trách: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend;./sources/frontend/src/test/java/org/nlh4j/saas/membershiphub/frontend/FrontendServiceTest.java`
* **Token theo dõi:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.3: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### Người phụ trách: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend`
* **Token theo dõi:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]<!--END_TAGS-->