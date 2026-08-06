# Giai đoạn 5: Triển khai Docker, Kubernetes và tài liệu triển khai

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260806145545 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai Docker, Kubernetes và tài liệu triển khai<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai Docker, Kubernetes và tài liệu triển khai<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/06 14:55:45 |
| **Tác giả** | Kiến trúc hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 5 tập trung vào việc triển khai Docker, Kubernetes và tài liệu triển khai. Các nhiệm vụ bao gồm:
- Triển khai Docker với các cấu hình container hóa.
- Triển khai Kubernetes với các cấu hình triển khai và scaling tự động.
- Tạo tài liệu triển khai mô tả các quy tắc triển khai và bảo mật.

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép
- `./sources/infra/docker`
- `./sources/infra/k8s`
- `./sources/docs/deployment.md`

## 3. Hướng dẫn chức năng dành riêng cho Sub-Agent
* **Coder**: Hoạt động như một Lập trình viên Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Trưởng/QC/QA Cấp cao. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng kiểm soát chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E, và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu nhiệm vụ con mục tiêu liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn MUST strictly output the literal token `INTEGRATION_SCOPE` as the first parameter of the semicolon pair (e.g., `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết kỹ thuật Cấp cao và Kiến trúc hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách Kỹ thuật toàn diện, tham chiếu lược đồ, bản thiết kế kiến trúc, và danh mục kiến trúc doanh nghiệp được tùy chỉnh cho các lớp topology dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra MUST được liệt kê như một thực thể đường dẫn tệp rõ ràng kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
* **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh, và vá lỗ hổng phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, sửa chữa lỗ hổng bảo mật OWASP, và giải quyết các chặn cổng chất lượng SonarQube.
* **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói, và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
* **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
* **GKE**: Chuyên về điều phối sản xuất container trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm, và triển khai tải trọng dịch vụ vi dịch vụ vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này.
- Đảm bảo tuân thủ các tiêu chuẩn doanh nghiệp OWASP.
- Đảm bảo độ phủ kiểm thử chức năng hoàn chỉnh cho các yêu cầu được phân bổ.
- Đảm bảo 100% ánh xạ Tag ID.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: Triển khai Docker và Kubernetes

#### 📝 Nhiệm vụ con 1.1: Triển khai Docker
##### Đặc vụ được chỉ định: Docker
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/docker/Dockerfile`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[ARC-010]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Triển khai Kubernetes
##### Đặc vụ được chỉ định: GKE
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/k8s/deployment.yaml`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.3: Tạo tài liệu triển khai
##### Đặc vụ được chỉ định: Doc
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/deployment.md`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[NFR-002], [NFR-004], [NFR-005]<!--END_TAGS-->