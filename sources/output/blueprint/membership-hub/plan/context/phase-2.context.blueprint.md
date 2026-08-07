# Giai đoạn 2: <!--PHASE_NAME_START-->Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807073534 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 2 tập trung vào triển khai mô-đun Trung tâm, cung cấp đầy đủ các thao tác CRUD cho thực thể Trung tâm, thực thi kiểm soát truy cập dựa trên vai trò cho quản trị viên Trung tâm, và mở rộng các endpoint RESTful cho quản lý Trung tâm. Triển khai bao gồm lưu trữ dữ liệu qua PostgreSQL, hợp đồng API cho danh sách, tạo, cập nhật và gán quản trị viên Trung tâm, cùng với tài liệu triển khai cho containerization và Kubernetes. Yêu cầu bảo mật, khả năng mở rộng và khả năng quan sát được đáp ứng thông qua RBAC, xác thực JWT và cấu hình triển khai GKE.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 07:35:34 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và mục tiêu thực thi giai đoạn

Giai đoạn 2 yêu cầu triển khai toàn bộ mô-đun quản lý Trung tâm, bao gồm:
- Xây dựng API REST cho danh sách, tạo, cập nhật, xoá Trung tâm và gán/giải quyền quản trị viên Trung tâm.
- Định nghĩa bảng `CENTERS` trong PostgreSQL và thực thi các thao tác CRUD qua JPA/Hibernate.
- Đảm bảo RBAC, JWT, và bảo mật OWASP cho các endpoint.
- Tạo Dockerfile đa‑stage cho backend, cấu hình GKE deployment, HPA và autoscaling.
- Cung cấp tài liệu kiến trúc, schema, và hướng dẫn triển khai.

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép

| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/backend/centers/` | Các lớp service, controller, repository, và cấu hình liên quan đến Trung tâm. |
| `./sources/infra/k8s/` | Manifest Kubernetes cho triển khai GKE. |
| `./sources/docker/` | Dockerfile đa‑stage cho backend. |
| `./sources/gcp/` | Script triển khai GCP Artifact Registry và GKE. |
| `./sources/docs/` | Tài liệu kiến trúc, schema, và hướng dẫn triển khai. |
| `./sources/backend/centers/CenterController.java` | API controller cho Trung tâm. |
| `./sources/backend/centers/CenterService.java` | Service xử lý nghiệp vụ Trung tâm. |
| `./sources/backend/centers/CenterAdminService.java` | Service gán/giải quyền quản trị viên Trung tâm. |
| `./sources/infra/k8s/center-deployment.yaml` | Manifest GKE cho dịch vụ Trung tâm. |
| `./sources/docker/backend/Dockerfile` | Dockerfile cho backend. |
| `./sources/gcp/centers-deploy.sh` | Script triển khai GCP. |
| `./sources/docs/centers_architecture.md` | Tài liệu kiến trúc mô-đun Trung tâm. |

## 3. Hướng dẫn chức năng dành cho từng đại lý phụ

- **Coder**: Phát triển mã nguồn ứng dụng backend, triển khai các lớp service, controller, và repository. Không viết test hoặc manifest.
- **Tester**: Thiết kế và thực thi các bộ test JUnit, integration test, và kiểm tra hiệu năng. Không sửa mã nguồn.
- **Reviewer**: Kiểm tra mã, phân tích tĩnh, bảo mật OWASP, và sửa lỗi biên dịch.
- **Doc**: Soạn tài liệu kỹ thuật, schema, và hướng dẫn triển khai. Đảm bảo tài liệu nằm trong `./sources/docs/`.
- **Docker**: Xây dựng Dockerfile đa‑stage, tối ưu hình ảnh, và chuẩn bị cho triển khai.
- **GCP**: Tạo script triển khai GCP Artifact Registry và GKE.
- **GKE**: Xây dựng manifest Kubernetes, HPA, và triển khai dịch vụ.

## 4. Định nghĩa hoàn thành giai đoạn

- Tất cả các endpoint REST cho Trung tâm hoạt động đúng theo hợp đồng API, có bảo mật JWT và RBAC.
- Bảng `CENTERS` được tạo và có dữ liệu mẫu.
- Docker image cho backend được build, kích thước < 500 MB, và đẩy lên Artifact Registry.
- Manifest GKE triển khai thành công, có HPA và autoscaling.
- Tài liệu kiến trúc, schema, và hướng dẫn triển khai được hoàn thiện và lưu trong `./sources/docs/`.
- Tất cả các yêu cầu bảo mật OWASP, NFR-001, NFR-003, NFR-004 được kiểm tra và đáp ứng.
- Tất cả tag ID được ánh xạ và ghi lại trong logs.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->XÂY DỰNG DANH SÁCH TRUNG TÂM<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ phụ 1.1: Triển khai CenterController để hiển thị danh sách trung tâm (REQ-004) và phục vụ các thao tác CRUD cho System Admin (ARC-002).

##### Được giao cho: Coder

##### Được giao cho: Coder

* **Đường dẫn mục tiêu**: ./sources/backend/centers/CenterController.java
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-002], [REQ-004], [DAT-003]<!--END_TAGS-->
* **Hướng dẫn kỹ thuật chi tiết**: Xây dựng lớp `CenterController` với các phương thức GET `/api/v1/centers`, POST `/api/v1/centers`, PUT `/api/v1/centers/{centerId}`, DELETE `/api/v1/centers/{centerId}`. Đảm bảo kiểm tra RBAC, JWT, và trả về mã lỗi 404/409 khi cần. Sử dụng `CenterService` để thực thi nghiệp vụ.

```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
```

```json
// GET /api/v1/centers
{
  "centers": [
    {
      "centerId": "uuid",
      "name": "Hà Nội Center",
      "address": "123 Đường Láng, Đống Đa, Hà Nội",
      "taxId": "0123456789",
      "contactPhone": "+84123456789",
      "contactEmail": "contact@hnc.com"
    }
  ]
}
```

```json
// POST /api/v1/centers
{
  "name": "Hà Nội Center",
  "address": "123 Đường Láng, Đống Đa, Hà Nội",
  "taxId": "0123456789",
  "contactPhone": "+84123456789",
  "contactEmail": "contact@hnc.com"
}
```

```json
// PUT /api/v1/centers/{centerId}
{
  "name": "Hà Nội Center Updated",
  "address": "Updated Address",
  "taxId": "0123456789",
  "contactPhone": "+84123456789",
  "contactEmail": "updated@hnc.com"
}
```

#### 📝 Nhiệm vụ phụ 1.2: Tài liệu kiến trúc mô-đun Trung tâm

##### Được giao cho: Doc

##### Được giao cho: Doc

* **Đường dẫn mục tiêu**: ./sources/docs/centers_architecture.md
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-002], [DAT-003], [REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->
* **Hướng dẫn kỹ thuật chi tiết**: Soạn tài liệu chi tiết mô tả kiến trúc mô-đun Trung tâm, bao gồm sơ đồ lớp, schema bảng `CENTERS`, các endpoint API, quy trình RBAC, và quy trình triển khai Docker/GKE. Đảm bảo tài liệu nằm trong thư mục `./sources/docs/`.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->XÂY DỰNG LOGIC TẠO/CẬP NHẬT TRUNG TÂM<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ phụ 2.1: Triển khai CenterService để xử lý tạo và cập nhật trung tâm (REQ-005)

##### Được giao cho: Coder

##### Được giao cho: Coder

* **Đường dẫn mục tiêu**: ./sources/backend/centers/CenterService.java
* **Thẻ truy xuất**: <!--START_TAGS-->[REQ-005], [DAT-003]<!--END_TAGS-->
* **Hướng dẫn kỹ thuật chi tiết**: Xây dựng lớp `CenterService` với các phương thức `createCenter`, `updateCenter`, `deleteCenter`. Kiểm tra trùng lặp `taxId`, xử lý ngoại lệ 409 Conflict, và lưu dữ liệu vào bảng `CENTERS`.

```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
```

```json
// POST /api/v1/centers
{
  "name": "Hà Nội Center",
  "address": "123 Đường Láng, Đống Đa, Hà Nội",
  "taxId": "0123456789",
  "contactPhone": "+84123456789",
  "contactEmail": "contact@hnc.com"
}
```

```json
// PUT /api/v1/centers/{centerId}
{
  "name": "Hà Nội Center Updated",
  "address": "Updated Address",
  "taxId": "0123456789",
  "contactPhone": "+84123456789",
  "contactEmail": "updated@hnc.com"
}
```

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->XÂY DỰNG GÁN/GIẢI QUYỀN ADMIN TRUNG TÂM<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ phụ 3.1: Triển khai CenterAdminService để gán và rút quyền quản trị viên Trung tâm (REQ-006)

##### Được giao cho: Coder

##### Được giao cho: Coder

* **Đường dẫn mục tiêu**: ./sources/backend/centers/CenterAdminService.java
* **Thẻ truy xuất**: <!--START_TAGS-->[REQ-006], [ARC-002], [DAT-003]<!--END_TAGS-->
* **Hướng dẫn kỹ thuật chi tiết**: Xây dựng lớp `CenterAdminService` với phương thức `assignAdmin(centerId, userId)` và `removeAdmin(centerId, userId)`. Cập nhật `roleId` trong bảng `USERS` thành `Center Admin` và ghi lại mối quan hệ. Kiểm tra quyền RBAC và trả về mã lỗi 403 khi không đủ quyền.

```json
// PUT /api/v1/centers/{centerId}/admin/{userId}
{
  "action": "assign"
}
```

```json
// PUT /api/v1/centers/{centerId}/admin/{userId}
{
  "action": "remove"
}
```

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->XÂY DỰNG TRIỂN KHAI VÀ ĐIỀU KHIỂN GKE<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ phụ 4.1: Triển khai manifest GKE cho dịch vụ Trung tâm (NFR-001, NFR-003, NFR-004)

##### Được giao cho: GKE

##### Được giao cho: GKE

* **Đường dẫn mục tiêu**: ./sources/infra/k8s/center-deployment.yaml
* **Thẻ truy xuất**: <!--START_TAGS-->[NFR-001], [NFR-003], [NFR-004]<!--END_TAGS-->
* **Hướng dẫn kỹ thuật chi tiết**: Xây dựng manifest Kubernetes với Deployment, Service, HPA, và autoscaling dựa trên CPU > 70% hoặc latency > 300 ms. Đảm bảo namespace `membership-hub`, image `gcr.io/PROJECT_ID/membership-hub`, và port 8080.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: membership-hub
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: membership-hub-backend
  namespace: membership-hub
spec:
  replicas: 3
  selector:
    matchLabels:
      app: membership-hub
  template:
    metadata:
      labels:
        app: membership-hub
    spec:
      containers:
      - name: backend
        image: gcr.io/PROJECT_ID/membership-hub
        ports:
        - containerPort: 8080
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: membership-hub-hpa
  namespace: membership-hub
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: membership-hub-backend
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Pods
    pods:
      metric:
        name: request_latency
      target:
        type: AverageValue
        averageValue: 300ms
```

#### 📝 Nhiệm vụ phụ 4.2: Xây dựng Docker image cho dịch vụ Trung tâm (ARC-002, REQ-004, REQ-005, REQ-006, DAT-003)

##### Được giao cho: Docker

##### Được giao cho: Docker

* **Đường dẫn mục tiêu**: ./sources/docker/backend/Dockerfile
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-002], [REQ-004], [REQ-005], [REQ-006], [DAT-003]<!--END_TAGS-->
* **Hướng dẫn kỹ thuật chi tiết**: Xây dựng Dockerfile đa‑stage sử dụng `eclipse-temurin:17-jdk-alpine`, copy jar, expose port 8080, và ENTRYPOINT. Đảm bảo kích thước final image < 500 MB.

```dockerfile
FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -B -DskipTests clean package
COPY src ./src
RUN mvn -B -DskipTests package

FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app
COPY --from=build /app/target/membership-hub.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","app.jar"]
```

#### 📝 Nhiệm vụ phụ 4.3: Xây dựng script triển khai GCP cho dịch vụ Trung tâm (ARC-002, REQ-004, REQ-005, REQ-006, DAT-003)

##### Được giao cho: GCP

##### Được giao cho: GCP

* **Đường dẫn mục tiêu**: ./sources/gcp/centers-deploy.sh
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-002], [REQ-004], [REQ-005], [REQ-006], [DAT-003]<!--END_TAGS-->
* **Hướng dẫn kỹ thuật chi tiết**: Script Bash để build Docker image, push lên Artifact Registry, và triển khai GKE bằng `kubectl apply`. Đảm bảo sử dụng `gcloud` CLI và `kubectl` context đúng.

```bash
#!/usr/bin/env bash
set -e

PROJECT_ID="your-gcp-project-id"
IMAGE_NAME="gcr.io/${PROJECT_ID}/membership-hub"
NAMESPACE="membership-hub"

# Build Docker image
mvn clean package -DskipTests
docker build -t ${IMAGE_NAME}:latest .
docker push ${IMAGE_NAME}:latest

# Deploy to GKE
kubectl config use-context ${PROJECT_ID}-us-central1-a
kubectl apply -f ./sources/infra/k8s/center-deployment.yaml
```