# Giai đoạn 5: Bảo mật, tuân thủ, di động, pipeline

## 📊 Kiểm Soát Tài Liệu

| Mục | Chi Tiết |
| :--- | :--- |
| **ID Bản vẽ** | ARCH-20260807172813 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Bảo mật, tuân thủ, di động, pipeline<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc triển khai các biện pháp bảo mật doanh nghiệp, tuân thủ các yêu cầu phi chức năng, thiết lập quy trình DevOps và đảm bảo tuân thủ di động.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 17:28:13 |
| **Tác giả** | Kiến Trúc Hệ Thống Doanh Nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban Quản Trị Kỹ Thuật |

## 1. Phạm Vi Hoạt Động & Mục Tiêu Của Giai Đoạn
Giai đoạn này tập trung vào việc triển khai các biện pháp bảo mật doanh nghiệp, tuân thủ các yêu cầu phi chức năng, thiết lập quy trình DevOps và đảm bảo tuân thủ di động. Các yêu cầu bao gồm xây dựng Docker image đa giai đoạn, cung cấp hạ tầng GCP, triển khai Kubernetes (GKE) với HPA, tự động failover và backup cluster.

## 2. Phạm Vi Kỹ Thuật & Ranh Giới Thư Mục (Tệp, đường dẫn và điểm cuối)
- ./sources/infra/ (Docker) – [NFR-001], [NFR-002], [NFR-003]
- ./sources/infra/ (GCP) – [NFR-004], [NFR-005], [NFR-006]
- ./sources/infra/ (GKE) – [NFR-007], [NFR-008], [NFR-009]
- ./sources/docs/ (Doc) – tài liệu bảo mật & tuân thủ

## 3. Hướng Dẫn Chức Năng Cụ Thể Cho Các Đặc Sỹ Phụ
*   **Coder**: Hoạt động như một Lập Trình Viên Ứng Dụng Cấp Cao/Chuyên Gia. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và ứng dụng khách frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu hạ tầng.
* **Tester**: Hoạt động như một Trưởng/Chuyên Gia Kiểm Chất/QA. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng kiểm tra chất lượng. Trách nhiệm là tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con nhiệm vụ liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất ra chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà Viết Kỹ Thuật Chuyên Gia và Kiến Trúc Hệ Thống Doanh Nghiệp. Chuyên về biên soạn tài liệu Kỹ Thuật Chi Tiết, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp công nghệ hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác nhận lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng dịch vụ microservices vào các cụm GKE hoạt động.

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)
- Triển khai hoàn chỉnh các biện pháp bảo mật doanh nghiệp, tuân thủ các yêu cầu phi chức năng, thiết lập quy trình DevOps và đảm bảo tuân thủ di động.
- Kiểm tra và xác nhận các yêu cầu chức năng cốt lõi.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Xây dựng Docker image đa giai đoạn với kích thước nhỏ (<500MB) và base image <200MB<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 1.1: [Xây dựng Docker image đa giai đoạn với kích thước nhỏ (<500MB) và base image <200MB]
##### Đặc Sỹ Phụ Được Phân Công: Docker
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/docker/QuarkusDockerfile
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[NFR-001], [NFR-002], [NFR-003]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Soạn thảo multi-stage Dockerfile: giai đoạn builder sử dụng image Quarkus có sẵn, giai đoạn runtime sử dụng distroless base image; đảm bảo loại bỏ các gói không cần thiết; thực hiện `apk add --no-cache` tối thiểu; xác minh kích thước image bằng `docker build --no-cache`; đẩy image lên container registry.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Cung cấp hạ tầng GCP (VPC, IAM, Cloud Storage) và thiết lập monitoring<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 2.1: [Cung cấp hạ tầng GCP (VPC, IAM, Cloud Storage) và thiết lập monitoring]
##### Đặc Sỹ Phụ Được Phân Công: GCP
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/GCPInfrastructure.tf
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[NFR-004], [NFR-005], [NFR-006]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai Terraform script tạo VPC với private subnets, firewall rules; tạo IAM service accounts cho các service; thiết lập bucket Cloud Storage với lifecycle policy; tích hợp Prometheus và Grafana để monitoring; thiết lập alerting cho các chỉ số hiệu suất (latency, error rate).

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->Triển khai Kubernetes (GKE) với HPA, tự động failover và backup cluster<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 3.1: [Triển khai Kubernetes (GKE) với HPA, tự động failover và backup cluster]
##### Đặc Sỹ Phụ Được Phân Công: GKE
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/Deployment.yaml
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Soạn thảo Kubernetes Deployment cho các microservice Quarkus; cấu hình Resource Limits/Requests; thiết lập Horizontal Pod Autoscaler dựa trên CPU >70% hoặc latency >300ms; tạo ServiceEntry cho cross-cluster communication; thiết lập backup GKE cluster ở region khác; định kỳ kiểm tra SLA 99.9% và ghi log vào hệ thống monitoring.