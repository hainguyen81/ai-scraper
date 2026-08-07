# Giai đoạn 2: <!--PHASE_NAME_START-->Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807042343 |
| **Tên Dự Án** | membership-hub |
| **Giai Đoạn** | 2 |
| **Tên Giai Đoạn** | <!--PHASE_NAME_START-->Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin<!--PHASE_NAME_END--> |
| **Mô Tả** | <!--PHASE_DESC_START-->Giai đoạn này triển khai quản lý trung tâm, bao gồm xây dựng API CRUD cho trung tâm, kiểm tra trùng lặp taxId, phân quyền Center Admin, cập nhật role trong bảng USERS, và triển khai manifest GKE cho dịch vụ trung tâm với autoscaling dựa trên CPU và độ trễ.<!--PHASE_DESC_END--> |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày/Thời Gian** | 2026/08/07 04:23:43 |
| **Tác Giả** | Enterprise System Architect (SA Agent) |
| **Phê Duyệt** | Pending Technical Governance Review |

## 1. Phạm Vi Hoạt Động Giai Đoạn & Mục Tiêu

Giai đoạn 2 tập trung vào triển khai quản lý trung tâm, bao gồm:
- Xây dựng các API CRUD cho trung tâm (tạo, đọc, cập nhật, xóa) với kiểm tra trùng lặp `taxId`.
- Phân quyền Center Admin: gán và rút quyền cho người dùng, cập nhật `roleId` trong bảng `USERS`.
- Tạo và triển khai manifest Kubernetes (GKE) cho dịch vụ trung tâm, bao gồm autoscaling dựa trên CPU và độ trễ.
- Đảm bảo tuân thủ các yêu cầu bảo mật, hiệu năng và khả năng mở rộng (NFR-001, NFR-003, NFR-004).
- Đảm bảo tất cả các yêu cầu [REQ-004], [REQ-005], [REQ-006] và dữ liệu [DAT-003] được triển khai đầy đủ.

## 2. Phạm Vi Kỹ Thuật & Giới Hạn Đường Dẫn (Tệp, Đường dẫn, và Điểm cuối API)

- **Backend**: `./sources/backend/centers/`
  - `CenterController.java` – API endpoints: `GET /api/v1/centers`, `POST /api/v1/centers`, `PUT /api/v1/centers/{centerId}/admin/{userId}`
  - `CenterService.java` – Logic for create/update/delete center, taxId validation.
  - `CenterAdminService.java` – Logic for assigning/removing Center Admin, updating `roleId` in `USERS`.
- **Infrastructure**: `./sources/infra/k8s/`
  - `center-deployment.yaml` – Kubernetes deployment, HPA, autoscaling configuration.

## 3. Hướng Dẫn Chức Năng Đặc Biệt Cho Mỗi Đại Diện Phụ

- **Coder**: Phát triển mã nguồn ứng dụng, thực hiện các lớp Java cho backend, không viết test hoặc manifest.
- **Tester**: Viết bộ kiểm thử JUnit, kiểm thử tích hợp, kiểm thử hiệu năng, không sửa mã nguồn.
- **Doc**: Soạn tài liệu kỹ thuật, mô tả kiến trúc, sơ đồ dữ liệu, tài liệu triển khai.
- **Reviewer**: Kiểm tra mã, phân tích tĩnh, sửa lỗi bảo mật, đảm bảo tuân thủ OWASP.
- **Docker**: Xây dựng Dockerfile đa giai đoạn, tối ưu gói, đẩy image lên DockerHub.
- **GCP**: Tự động triển khai image lên Google Artifact Registry, cấu hình Cloud Run.
- **GKE**: Xây dựng manifest Kubernetes, HPA, Helm chart, triển khai dịch vụ lên GKE.

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)

- Tất cả các yêu cầu [REQ-004], [REQ-005], [REQ-006] và dữ liệu [DAT-003] được triển khai và kiểm thử thành công.
- Đạt 100% coverage kiểm thử cho các module liên quan.
- Tuân thủ đầy đủ các yêu cầu bảo mật OWASP, NFR-001, NFR-003, NFR-004.
- Mọi thẻ ID được ánh xạ chính xác, không có thẻ chưa được sử dụng.

## 5. Nhật Ký Thực Hiện Kiến Trúc Ngày Mỗi Ngày

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->XÂY DỰNG CONTROLLER DANH SÁCH TRUNG TÂM<!--DAY_HEADER_END-->

#### 📝 Nhiệm Vụ 1.1: Triển khai CenterController để hiển thị danh sách trung tâm (REQ-004) và phục vụ các thao tác CRUD cho System Admin (ARC-002).
##### Địa Diện Phụ: Coder
##### Yêu Cầu Thành Phần & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu**: ./sources/backend/centers/CenterController.java
* **Thẻ Định Vị Theo Dõi**: <!--START_TAGS-->[REQ-004], [ARC-002], [DAT-003]<!--END_TAGS-->

#### 📝 Nhiệm Vụ 1.2: Soạn tài liệu kỹ thuật cho giai đoạn 2, bao gồm mô tả kiến trúc, sơ đồ dữ liệu, và quy trình triển khai.
##### Địa Diện Phụ: Doc
##### Yêu Cầu Thành Phần & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu**: ./sources/docs/phase2_technical_overview.md
* **Thẻ Định Vị Theo Dõi**: <!--START_TAGS-->[DAT-003], [NFR-001], [NFR-003], [NFR-004]<!--END_TAGS-->

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->XÂY DỰNG SERVICE TẠO/ CẬP NHẬT TRUNG TÂM<!--DAY_HEADER_END-->

#### 📝 Nhiệm Vụ 2.1: Triển khai CenterService để tạo/cập nhật trung tâm (REQ-005) và kiểm tra trùng lặp taxId.
##### Địa Diện Phụ: Coder
##### Yêu Cầu Thành Phần & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu**: ./sources/backend/centers/CenterService.java
* **Thẻ Định Vị Theo Dõi**: <!--START_TAGS-->[REQ-005], [DAT-003]<!--END_TAGS-->

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->XÂY DỰNG SERVICE GÁN RÚT QUYỀN CENTER ADMIN<!--DAY_HEADER_END-->

#### 📝 Nhiệm Vụ 3.1: Triển khai CenterAdminService để gán/rút quyền Center Admin (REQ-006) và cập nhật roleId trong USERS.
##### Địa Diện Phụ: Coder
##### Yêu Cầu Thành Phần & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu**: ./sources/backend/centers/CenterAdminService.java
* **Thẻ Định Vị Theo Dõi**: <!--START_TAGS-->[REQ-006], [ARC-002], [DAT-003]<!--END_TAGS-->

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->TẠO MANIFEST GKE CHO DỊCH VỤ TRUNG TÂM<!--DAY_HEADER_END-->

#### 📝 Nhiệm Vụ 4.1: Tạo manifest GKE cho dịch vụ trung tâm (center-deployment.yaml) với autoscaling dựa trên CPU và độ trễ.
##### Địa Diện Phụ: GKE
##### Yêu Cầu Thành Phần & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu**: ./sources/infra/k8s/center-deployment.yaml
* **Thẻ Định Vị Theo Dõi**: <!--START_TAGS-->[NFR-001], [NFR-003], [NFR-004]<!--END_TAGS-->