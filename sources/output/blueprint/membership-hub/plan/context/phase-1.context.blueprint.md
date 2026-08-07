# Giai đoạn 1: <!--PHASE_NAME_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807073534 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào xây dựng lõi người dùng, quản lý vai trò và triển khai cơ chế xác thực bao gồm đăng ký, OAuth2, JWT và kiểm tra đầu vào.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 07:35:34 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## Phạm vi và mục tiêu thực thi giai đoạn

Giai đoạn 1 thực hiện xây dựng lõi người dùng, quản lý vai trò và triển khai cơ chế xác thực. Các thành phần chính bao gồm:

- Định nghĩa bảng `USERS` và `ROLES` trong PostgreSQL.
- Xây dựng dịch vụ `UserService` để xử lý đăng ký và quản lý người dùng.
- Xây dựng `AuthController` để cung cấp API đăng ký, đăng nhập OAuth2 và cập nhật vai trò.
- Tạo tài liệu kỹ thuật mô tả kiến trúc và quy trình xác thực.
- Xây dựng Dockerfile, script triển khai GCP và manifest Kubernetes cho GKE.
- Viết kiểm thử đơn vị và tích hợp, thực hiện đánh giá bảo mật OWASP.

## Phạm vi kỹ thuật cho phép & Ranh giới thư mục

- **Backend**: `./sources/backend/users/UserService.java`, `./sources/backend/users/AuthController.java`
- **Database**: Bảng `ROLES`, `USERS` (PostgreSQL)
- **API Endpoints**: `/api/v1/auth/register`, `/api/v1/auth/social`, `/api/v1/users/{userId}/role`
- **Docker**: `./sources/docker/backend/Dockerfile`
- **GCP**: `./sources/gcp/deploy.sh`
- **GKE**: `./sources/k8s/namespace.yaml`, `./sources/k8s/deployment.yaml`
- **Documentation**: `./sources/docs/user_module_overview.md`
- **Tests**: `./sources/backend/users/UserServiceTest.java`, `./sources/backend/users/AuthControllerTest.java`
- **Review**: `./sources/review/AuthControllerReview.txt`

## Chỉ đạo chức năng đại lý phụ

- **Coder**: Phát triển mã nguồn ứng dụng backend, triển khai dịch vụ người dùng và xác thực.
- **Tester**: Thiết kế và thực thi các bộ kiểm thử đơn vị và tích hợp cho `UserService` và `AuthController`.
- **Reviewer**: Kiểm tra mã, bảo mật, và tuân thủ OWASP cho các thành phần backend.
- **Doc**: Soạn tài liệu kỹ thuật chi tiết cho mô-đun người dùng và quy trình xác thực.
- **Docker**: Xây dựng Dockerfile, tối ưu hình ảnh, và chuẩn bị cho triển khai.
- **GCP**: Tạo script triển khai tới Google Cloud Artifact Registry và cấu hình môi trường.
- **GKE**: Tạo manifest Kubernetes, HPA, và triển khai dịch vụ lên GKE.

## Định nghĩa Hoàn thành giai đoạn

- 100% kiểm thử đơn vị cho `UserService` và `AuthController` với độ phủ ≥ 90%.
- 100% kiểm thử tích hợp cho các API xác thực.
- 100% đánh giá bảo mật OWASP (SQLi, XSS, CSRF, etc.) vượt qua.
- Định nghĩa và triển khai schema dữ liệu `ROLES` và `USERS` trong PostgreSQL.
- Xây dựng và kiểm tra Dockerfile, tạo image < 500 MB.
- Kiểm tra script GCP triển khai và xác nhận image được đẩy tới Artifact Registry.
- Kiểm tra manifest GKE, triển khai thành công, HPA hoạt động.
- Hoàn thành tài liệu kỹ thuật chi tiết cho mô-đun người dùng.
- Đảm bảo mọi tag ID được ánh xạ và ghi lại trong các logs.

## LỊCH THỰC HIỆN KIẾT THUẬT NGÀY

### Ngày 1: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ NGƯỜI DÙNG VÀ TÀI LIỆU<!--DAY_HEADER_END-->

#### Nhiệm vụ phụ 1.1: Xây dựng UserService
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: ./sources/backend/users/UserService.java
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-001], [REQ-001], [DAT-001]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**: Xây dựng lớp `UserService` để xử lý đăng ký người dùng mới, tạo bản ghi trong bảng `USERS` với vai trò mặc định là `Student`, tuân thủ `REQ-001` và `ARC-001`. Đảm bảo kiểm tra đầu vào, hash mật khẩu, và lưu trữ an toàn.  
**Đặc tả DDL SQL cho Ma trận dữ liệu [DAT-001]**  
```sql
CREATE TABLE ROLES (
    roleId SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE,
    description VARCHAR(200)
);

CREATE TABLE USERS (
    userId UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    passwordHash CHAR(60) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    roleId SMALLINT NOT NULL REFERENCES ROLES(roleId),
    provider ENUM('local','firebase','google','facebook') NOT NULL DEFAULT 'local',
    createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
    updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
);
```

#### Nhiệm vụ phụ 1.2: Viết kiểm thử cho UserService
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: ./sources/backend/users/UserServiceTest.java
* **Thẻ truy xuất**: <!--START_TAGS-->[REQ-001], [DAT-001]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**: Viết các test JUnit5 cho `UserService`, bao gồm kiểm tra đăng ký thành công, lỗi email trùng, và xác thực hash mật khẩu.

#### Nhiệm vụ phụ 1.3: Tài liệu mô-đun người dùng
##### Đại lý phụ được giao: Doc
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: ./sources/docs/user_module_overview.md
* **Thẻ truy xuất**: <!--START_TAGS-->[DAT-001]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**: Soạn tài liệu chi tiết mô tả kiến trúc `UserService`, cấu trúc database, quy trình đăng ký và xác thực.

#### Nhiệm vụ phụ 1.4: Xây dựng Dockerfile backend
##### Đại lý phụ được giao: Docker
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: ./sources/docker/backend/Dockerfile
* **Thẻ truy xuất**: <!--START_TAGS-->[DAT-001]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**: Xây dựng Dockerfile sử dụng image `eclipse-temurin:17-jdk-alpine`, copy jar, expose port 8080, ENTRYPOINT. Đảm bảo kích thước < 500 MB.

```dockerfile
FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app
COPY target/membership-hub.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","app.jar"]
```

### Ngày 2: <!--DAY_HEADER_START-->XÂY DỰNG CONTROLLER XÁC THỰC VÀ TRIỂN KHAI MÔ HÌNH<!--DAY_HEADER_END-->

#### Nhiệm vụ phụ 2.1: Xây dựng AuthController
##### Đại lý phụ được giao: Coder
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: ./sources/backend/users/AuthController.java
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-006], [REQ-002], [REQ-003], [DAT-001]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**: Xây dựng `AuthController` để xử lý đăng ký, đăng nhập OAuth2, và cập nhật vai trò. Đảm bảo bảo mật JWT, refresh token, và kiểm tra đầu vào.  
**Hợp đồng API và Định tuyến Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]**  
```json
// POST /api/v1/auth/register
{
  "email": "user@example.com",
  "password": "StrongPass123!",
  "fullName": "Nguyen Van A",
  "provider": "local"
}
```
```json
// POST /api/v1/auth/social
{
  "provider": "google",
  "code": "OAuth2_code_from_google",
  "redirectUri": "https://app.example.com/auth/callback"
}
```
```json
// PUT /api/v1/users/{userId}/role
{
  "roleId": 2
}
```
**Xử lý ngoại lệ địa phương [EXC-004]**  
```
Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc): Trả về HTTP 400 với danh sách các trường không hợp lệ và hướng dẫn chỉnh sửa.
```

#### Nhiệm vụ phụ 2.2: Kiểm tra AuthController
##### Đại lý phụ được giao: Tester
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: ./sources/backend/users/AuthControllerTest.java
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-006], [REQ-002], [REQ-003]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**: Viết test JUnit5 cho `AuthController`, bao gồm kiểm tra đăng ký thành công, lỗi đăng nhập, và cập nhật vai trò.

#### Nhiệm vụ phụ 2.3: Đánh giá bảo mật AuthController
##### Đại lý phụ được giao: Reviewer
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: ./sources/review/AuthControllerReview.txt
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-006], [REQ-002], [REQ-003]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**: Kiểm tra mã nguồn, xác thực OWASP, bảo mật JWT, và bảo vệ against injection.

#### Nhiệm vụ phụ 2.4: Triển khai GCP script
##### Đại lý phụ được giao: GCP
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: ./sources/gcp/deploy.sh
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-006]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**: Viết script bash để build Docker image và đẩy tới Google Cloud Artifact Registry.  
```bash
#!/usr/bin/env bash
gcloud builds submit --tag gcr.io/PROJECT_ID/membership-hub
```

#### Nhiệm vụ phụ 2.5: Triển khai GKE manifests
##### Đại lý phụ được giao: GKE
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: ./sources/k8s/namespace.yaml, ./sources/k8s/deployment.yaml
* **Thẻ truy xuất**: <!--START_TAGS-->[ARC-006]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**: Tạo namespace và deployment manifest cho backend, cấu hình HPA, và triển khai lên GKE.  
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: membership-hub
```
```yaml
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
```