# Giai đoạn 5: <!--PHASE_NAME_START-->deploymentOnGKE<!--PHASE_NAME_END--> | Mô tả: Triển khai toàn bộ hệ thống membership‑hub lên nền tảng Kubernetes (GKE), bao gồm xây dựng Docker images, cấu hình cluster, triển khai manifests, thiết lập HPA, bảo mật, và giám sát.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260802135007 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn kỹ thuật** | <!--PHASE_NAME_START-->deploymentOnGKE<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai toàn bộ hệ thống membership‑hub lên nền tảng Kubernetes (GKE), bao gồm xây dựng Docker images, cấu hình cluster, triển khai manifests, thiết lập HPA, bảo mật, và giám sát. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/02 13:50:07 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu Giai đoạn

Giai đoạn 5 thực hiện toàn bộ quy trình triển khai hệ thống membership‑hub lên Google Kubernetes Engine (GKE). Các hoạt động chính bao gồm:

1. **Xây dựng và đẩy Docker images** cho tất cả các micro‑service (users, centers, attendance, studentcards, …) vào Google Container Registry (GCR) với kích thước tối đa 500 MB.
2. **Tạo và cấu hình GKE cluster**: node pool, autoscaling, network policies, IAM roles, và bảo mật mạng.
3. **Triển khai Kubernetes manifests** (Deployment, Service, Ingress, HPA, liveness/readiness probes) cho từng service.
4. **Thiết lập giám sát và ghi log** (Stackdriver, Prometheus, Grafana) và cấu hình alerting.
5. **Kiểm tra tính sẵn sàng**: health‑check, scaling, và xác thực rằng các service đáp ứng đúng yêu cầu NFR‑002 (độ sẵn sàng 99.9 %) và NFR‑004 (tự động scale).

## 2. Phạm vi Kỹ thuật & Ranh giới Thư mục

| Đường dẫn tuyệt đối | Mô tả |
| :--- | :--- |
| `./sources/infra/deployment` | Thư mục chứa script build, push, và cấu hình GKE. |
| `./sources/infra/deployment/scripts` | Script shell cho build, push, và tạo cluster. |
| `./sources/infra/deployment/k8s` | Tập tin YAML cho Deployment, Service, Ingress, HPA, NetworkPolicy, HealthCheck, Monitoring. |
| `./sources/infra/deployment/gcr` | Thư mục chứa cấu hình GCR repository và IAM. |
| `./sources/infra/deployment/gke` | Cấu hình cluster, node pool, và autoscaling. |

## 3. Hướng dẫn Đặc thù cho Mỗi Agent

| Agent | Trách nhiệm |
| :--- | :--- |
| **Docker** | Viết và chạy script build Docker, tag, và đẩy images lên GCR. |
| **GCP** | Tạo và cấu hình GKE cluster, node pool, IAM, và network policies. |
| **GKE** | Triển khai manifests, thiết lập HPA, liveness/readiness probes, và monitoring. |
| **Tester** | Kiểm tra tính sẵn sàng, scaling, và health‑check của các service. |
| **Reviewer** | Kiểm tra static code, cấu hình bảo mật, và tuân thủ OWASP. |
| **Doc** | Tạo tài liệu triển khai, cấu hình, và hướng dẫn vận hành. |

## 4. Định nghĩa Hoàn thành (DoD)

- Cluster GKE được tạo và có ít nhất 3 node pool với autoscaling bật.
- Tất cả Docker images được đẩy thành công vào GCR và kích thước < 500 MB.
- Mỗi micro‑service có Deployment, Service, Ingress, HPA, liveness/readiness probes, và health‑check hoạt động.
- Hệ thống giám sát (Prometheus + Grafana) hiển thị metrics và alerting cho các service.
- Kiểm tra tự động (Tester) xác nhận 100 % endpoint trả về 200 OK và scaling đáp ứng đúng cấu hình HPA.
- Tất cả các tag ID [NFR-002], [NFR-004] được ghi nhận trong logs và đạt 100 % mapping.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: XÂY ĐỀ CẤP VÀ ĐĂNG KÝ HÌNH ẢNH

#### SUB-TASK 1.1: Xây dựng Docker images cho toàn bộ micro‑service
##### Được giao Agent: Docker
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/scripts/build.sh`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 1.2: Tag và đẩy images lên GCR
##### Được giao Agent: Docker
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/scripts/push.sh`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 1.3: Tạo repository GCR và cấu hình IAM
##### Được giao Agent: GCP
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/gcr/setup.sh`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 1.4: Tạo cluster GKE và node pool
##### Được giao Agent: GCP
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/gke/create_cluster.sh`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 1.5: Cấu hình NetworkPolicy cho cluster
##### Được giao Agent: GKE
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/k8s/network-policy.yaml`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 1.6: Triển khai Deployment và Service cho từng micro‑service
##### Được giao Agent: GKE
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/k8s/deployment.yaml`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 1.7: Thiết lập HPA cho các Deployment
##### Được giao Agent: GKE
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/k8s/hpa.yaml`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 1.8: Cấu hình liveness/readiness probes và health‑check
##### Được giao Agent: GKE
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/k8s/health-check.yaml`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 1.9: Thiết lập monitoring và alerting
##### Được giao Agent: GKE
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/k8s/monitoring.yaml`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

### DAY 2: XÂY ĐỀ CẤP VÀ KIỂM THỬ TỔNG

#### SUB-TASK 2.1: Kiểm tra tính sẵn sàng và scaling của các service
##### Được giao Agent: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `INTEGRATION_SCOPE;./sources/infra/deployment/tests/health_check_test.sh`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 2.2: Kiểm tra tự động scaling theo HPA
##### Được giao Agent: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `INTEGRATION_SCOPE;./sources/infra/deployment/tests/hpa_scaling_test.sh`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 2.3: Kiểm tra monitoring và alerting
##### Được giao Agent: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `INTEGRATION_SCOPE;./sources/infra/deployment/tests/monitoring_test.sh`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 2.4: Kiểm tra bảo mật mạng và IAM
##### Được giao Agent: Reviewer
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/gke/security_review.sh`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 2.5: Tạo tài liệu triển khai và vận hành
##### Được giao Agent: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/deployment/docs/DeploymentGuide.md`
* **Thẻ Định danh Theo Dõi**: <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->
*Thẻ Định danh Theo Dõi:* <!--START_TAGS-->[NFR-002], [NFR-004]<!--END_TAGS-->