# Giai đoạn 5: <!--PHASE_NAME_START-->Triển khai hệ thống và cấu hình hạ tầng<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805155024 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai hệ thống và cấu hình hạ tầng<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai hệ thống và cấu hình hạ tầng<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 15:50:24 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 5 tập trung vào việc triển khai hệ thống và cấu hình hạ tầng. Hạ tầng bao gồm các dịch vụ backend, cơ sở dữ liệu, và các dịch vụ cloud. Triển khai sẽ bao gồm việc cấu hình Docker, triển khai trên Google Cloud Platform (GCP), và cấu hình Kubernetes (GKE).

## 2. Phạm vi kỹ thuật và biên giới thư mục (Tệp, đường dẫn và điểm cuối)
- `./sources/infra/docker`
- `./sources/infra/gcp`
- `./sources/infra/gke`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và các ứng dụng frontend/mobile. Cấm viết bộ kiểm tra hoặc biểu mẫu cơ sở hạ tầng.
*   **Tester**: Hoạt động như một Nhà kiểm soát chất lượng/Chuyên gia QC/QA Cấp cao. Chuyên về kỹ thuật bộ kiểm tra, xác nhận và cổng chất lượng. Trách nhiệm là tạo các bộ kiểm tra JUnit, kiểm tra tích hợp, tự động hóa kiểm tra E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Doc**: Chức năng như một Nhà viết tài liệu kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn các tài liệu kỹ thuật Markdown toàn diện, tham chiếu lược đồ, bản đồ hệ thống và danh mục kiến trúc. Mỗi tệp tài liệu được tạo ra phải nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng microservices vào các cụm GKE hoạt động.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn 5.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP doanh nghiệp.
- Đảm bảo độ phủ kiểm tra chức năng hoàn chỉnh cho các yêu cầu được phân bổ.
- Đảm bảo 100% ánh xạ ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 8: <!--DAY_HEADER_START-->TRIỂN KHAI HỆ THỐNG VÀ CẤU HÌNH HẠ TẦNG<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 8.1: Triển khai Docker và cấu hình hạ tầng
##### Người phụ trách: Docker
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/docker`
* **Token theo dõi:** <!--START_TAGS-->[NFR-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.2: Triển khai Google Cloud Platform và cấu hình hạ tầng
##### Người phụ trách: GCP
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gcp`
* **Token theo dõi:** <!--START_TAGS-->[NFR-002], [NFR-003], [NFR-006], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.3: Triển khai Google Kubernetes Engine và cấu hình hạ tầng
##### Người phụ trách: GKE
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gke`
* **Token theo dõi:** <!--START_TAGS-->[NFR-001], [NFR-004]<!--END_TAGS-->

### 🌤️ Ngày 9: <!--DAY_HEADER_START-->KIỂM TRA VÀ TRIỂN KHAI HỆ THỐNG<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 9.1: Viết các bài kiểm tra đơn vị và tích hợp cho hạ tầng
##### Người phụ trách: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra;./sources/infra/src/test/java/org/nlh4j/saas/membershiphub/infra/InfraServiceTest.java`
* **Token theo dõi:** <!--START_TAGS-->[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 9.2: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### Người phụ trách: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra`
* **Token theo dõi:** <!--START_TAGS-->[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->