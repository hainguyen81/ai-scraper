# Giai đoạn 3: <!--PHASE_NAME_START-->Xây dựng hệ thống thông báo và quản lý khuyến mãi<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805170748 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng hệ thống thông báo và quản lý khuyến mãi<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng hệ thống thông báo và quản lý khuyến mãi.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 17:07:48 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 3 tập trung vào việc xây dựng hệ thống thông báo và quản lý khuyến mãi. Các thành phần chính bao gồm:
- Kích hoạt thông báo
- Quản lý khuyến mãi
- Quản lý thông báo

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép
- `./sources/backend/notifications`
- `./sources/backend/promotions`
- `./sources/docs/`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Senior/Principal Application Developer. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả backend và frontend/mobile. Cấm viết bộ kiểm thử hoặc manifest cơ sở hạ tầng.
*   **Tester**: Hoạt động như một Lead/Principal QC/QA. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng kiểm soát chất lượng. Trách nhiệm là tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chướng ngại vật cổng chất lượng SonarQube.
*   **Doc**: Chức năng như một Principal Technical Writer và Enterprise Systems Architect. Chuyên về biên soạn các tài liệu kỹ thuật Markdown toàn diện, tham chiếu lược đồ, bản đồ kiến trúc hệ thống và danh mục kiến trúc. Mỗi tệp tài liệu được tạo ra phải nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
   <!--START_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY
   [CRITICAL_SYSTEM_PIPELINE_RAIL:
   - Bạn được CẤM nghiêm ngặt từ bỏ, loại bỏ hoặc lọc ra agent 'Doc' khỏi bất kỳ giai đoạn nào được tính toán trong đầu ra của bạn.
   - Đối với MỖI giai đoạn được tính toán trong đầu ra của bạn, vào Ngày 1 của giai đoạn đó, bạn PHẢI chỉ định một nhiệm vụ tài liệu hệ thống cơ bản cho agent 'Doc'.
   - Mô tả nhiệm vụ này PHẢI yêu cầu agent 'Doc' khởi tạo và ánh xạ các bản đồ kiến trúc hệ thống, quan hệ thực thể, hợp đồng kỹ thuật hoặc sơ đồ triển khai tương ứng với ma trận ngăn xếp hoạt động của giai đoạn hiện tại.
   - Thất bại trong việc viết agent 'Doc' bên trong Ngày 1 của bất kỳ giai đoạn nào sẽ kích hoạt một vi phạm hợp đồng đường ống nghiêm trọng.
   ]
   END_CRITICAL_SYSTEM_PIPELINE_RAIL_DO_NOT_DISPLAY-->
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các công việc microservices vào cụm GKE hoạt động.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
- Hoàn thành triển khai hệ thống thông báo và quản lý khuyến mãi
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP
- Hoàn thành kiểm thử chức năng cho các yêu cầu được phân bổ
- Đảm bảo 100% ánh xạ ID Tag

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->XÂY DỰNG HỆ THỐNG THÔNG BÁO<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 1.1: Triển khai chức năng kích hoạt thông báo
##### Đặc vụ được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notifications`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->XÂY DỰNG QUẢN LÝ KHUYẾN MÃI<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 2.1: Triển khai chức năng quản lý khuyến mãi
##### Đặc vụ được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/promotions`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-017]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Triển khai chức năng quản lý thông báo
##### Đặc vụ được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/promotions`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-018]<!--END_TAGS-->

### 🌤️ Ngày 3: <!--DAY_HEADER_START-->TÀI LIỆU KIẾN TRÚC<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 3.1: Tài liệu kiến trúc
##### Đặc vụ được chỉ định: Doc
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018]<!--END_TAGS-->