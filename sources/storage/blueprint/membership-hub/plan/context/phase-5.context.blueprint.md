# Giai đoạn 5: <!--PHASE_NAME_START-->infraDeployment<!--PHASE_NAME_END--> | Mô tả: Đóng gói Docker, triển khai GKE, và thiết lập CI/CD cho toàn bộ hệ thống membership‑hub, đảm bảo tuân thủ các yêu cầu NFR về khả năng sẵn sàng, bảo mật, quy mô, và hiệu năng.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260803170121 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn kỹ thuật** | <!--PHASE_NAME_START-->infraDeployment<!--PHASE_NAME_END--> |
| **Mô tả** | Đóng gói Docker, triển khai GKE, và thiết lập CI/CD cho toàn bộ hệ thống membership‑hub, đảm bảo tuân thủ các yêu cầu NFR về khả năng sẵn sàng, bảo mật, quy mô, và hiệu năng. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/03 17:01:21 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và mục tiêu của giai đoạn
Giai đoạn 5 tập trung vào việc xây dựng hạ tầng triển khai và CI/CD cho toàn bộ stack microservices, bao gồm:
- **Docker**: Tạo Dockerfile đa stage, tối ưu kích thước, hỗ trợ multi‑arch, và chuẩn bị image cho Quarkus services.
- **GCP**: Viết Terraform modules để provision GKE cluster, VPC, IAM, Cloud SQL, Pub/Sub, Cloud Storage, và cấu hình CI/CD pipeline.
- **Kubernetes**: Tạo Helm chart cho deployment, service, ingress, và cấu hình HPA, liveness/readiness probes, và secrets management.
- **CI/CD**: Thiết lập GitHub Actions workflow để build, test, push image, và deploy tới GKE, đồng thời kích hoạt rollback và canary.

Mục tiêu chính:
- Đảm bảo **image size < 500 MB** và **base image < 200 MB** (NFR‑005).
- Đạt **99.9 % uptime** và **auto‑failover** (NFR‑002, NFR‑004).
- Thực thi **OWASP Top 10** và **TLS 1.3** (NFR‑003, NFR‑006).
- Hỗ trợ **đa ngôn ngữ** và **GDPR/CCPA** trong logs (NFR‑007, NFR‑008).
- Cung cấp **backup** và **DR** cho GKE và Cloud SQL (NFR‑009).

## 2. Phạm vi kỹ thuật và ranh giới thư mục
| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/infra/docker/` | Dockerfile và multi‑stage build scripts. |
| `./sources/infra/gcp/terraform/` | Terraform modules: GKE, VPC, IAM, Cloud SQL, Pub/Sub, Cloud Storage, CI/CD. |
| `./sources/infra/k8s/helm/` | Helm chart: deployment, service, ingress, HPA, probes, secrets. |
| `./sources/infra/cicd/` | GitHub Actions workflow YAML. |

Endpoint routing không thay đổi; các services vẫn expose REST APIs qua Quarkus, được expose bởi Ingress trong Helm chart.

## 3. Hướng dẫn chức năng dành cho các đại lý phụ trách
- **Docker**: Xây dựng Dockerfile, chạy `docker build`, kiểm tra kích thước, push tới GCR.  
- **GCP**: Viết Terraform, chạy `terraform init`, `terraform plan`, `terraform apply`, kiểm tra trạng thái resource.  
- **GKE**: Deploy Helm chart, kiểm tra pod readiness, HPA scaling, và canary rollout.  
- **Doc**: Tạo tài liệu chi tiết về cấu hình Docker, Terraform, Helm, và CI/CD, lưu trong `./sources/infra/docs/`.  
- **Reviewer**: Kiểm tra static code analysis, lint, và security scanning cho các file cấu hình.  
- **Tester**: Viết unit tests cho Terraform modules (terraform validate), integration tests cho Helm chart (kubectl apply + health checks).  

## 4. Định nghĩa Hoàn thành giai đoạn (DoD)
- **Image size**: Docker image < 500 MB, base image < 200 MB.  
- **Uptime**: GKE cluster đạt 99.9 % uptime, có auto‑failover.  
- **Security**: Tất cả logs encrypted, TLS 1.3, OWASP mitigations, audit logs retained 1 year.  
- **Scalability**: HPA hoạt động, read replicas cho Cloud SQL.  
- **Backup**: Cloud SQL full backup daily, point‑in‑time recovery 24 h.  
- **Tag coverage**: 100 % mapping of all NFR tags in phase.  
- **Documentation**: Hoàn thiện tài liệu trong `./sources/infra/docs/`.  
- **CI/CD**: Workflow chạy thành công, deploy tới GKE, rollback khả dụng.  

## 5. LỊCH THỰC HIỆN KIẾT THUẬT NGÀY ĐẾN NGÀY

### DAY 1: XÂY DỰNG VÀ TỐI ƯU HÌNH ẢNH Docker

#### SUB-TASK 1.1: Viết Dockerfile đa stage, tối ưu kích thước, hỗ trợ multi‑arch
##### Địa chỉ phụ trách: Docker
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/docker/Dockerfile`
* **Thẻ theo dõi**: <!--START_TAGS-->[NFR-005]<!--END_TAGS-->
```dockerfile
FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN ./mvnw -DskipTests clean package

FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
CMD ["java", "-jar", "app.jar"]
```

### DAY 2: PHIÊN BÁN VÀ CẤU HÌNH THỰC HIỆN Terraform trên GCP

#### SUB-TASK 2.1: Viết Terraform modules để provision GKE, VPC, IAM, Cloud SQL, Pub/Sub, và cấu hình CI/CD
##### Địa chỉ phụ trách: GCP
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/gcp/terraform/main.tf`
* **Thẻ theo dõi**: <!--START_TAGS-->[NFR-002], [NFR-004], [NFR-006], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->
```hcl
provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_container_cluster" "membership" {
  name     = "membership-cluster"
  location = var.region
  initial_node_count = 3
  node_config {
    machine_type = "e2-medium"
    oauth_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
  lifecycle {
    prevent_destroy = true
  }
}

resource "google_sql_database_instance" "membership" {
  name = "membership-db"
  region = var.region
  database_version = "POSTGRES_15"
  settings {
    tier = "db-custom-1-3840"
  }
}
```

### DAY 3: TRIỂN KHAI KUBERNETES BẰNG HELM CHART VÀ CI/CD PIPELINE

#### SUB-TASK 3.1: Deploy Helm chart, kiểm tra readiness, HPA, và canary rollout
##### Địa chỉ phụ trách: GKE
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/k8s/helm/membership-hub/Chart.yaml`
* **Thẻ theo dõi**: <!--START_TAGS-->[NFR-002], [NFR-004], [NFR-006], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->
```yaml
apiVersion: v2
name: membership-hub
description: Helm chart for membership-hub services
type: application
version: 0.1.0
appVersion: "1.0"
```

#### SUB-TASK 3.2: Thiết lập GitHub Actions workflow cho CI/CD
##### Địa chỉ phụ trách: Docker
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/cicd/ci-cd.yml`
* **Thẻ theo dõi**: <!--START_TAGS-->[NFR-002], [NFR-004], [NFR-006], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->
```yaml
name: CI/CD
on:
  push:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
      - name: Build Docker
        run: docker build -t gcr.io/${{ secrets.GCP_PROJECT }}/membership-hub:latest .
      - name: Push Docker
        run: docker push gcr.io/${{ secrets.GCP_PROJECT }}/membership-hub:latest
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up GCP credentials
        uses: google-github-actions/auth@v1
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}
      - name: Deploy Helm
        run: |
          helm upgrade --install membership-hub ./sources/infra/k8s/helm/membership-hub \
            --namespace membership \
            --set image.repository=gcr.io/${{ secrets.GCP_PROJECT }}/membership-hub \
            --set image.tag=latest
```

---