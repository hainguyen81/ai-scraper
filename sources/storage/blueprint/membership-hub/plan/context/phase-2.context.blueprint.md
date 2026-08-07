# Giai đoạn 2: Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260807060838 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 06:08:38 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý Kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 2 tập trung vào việc triển khai quản lý trung tâm với CRUD, phân quyền và gán Center Admin. Giai đoạn này bao gồm việc xây dựng controller danh sách trung tâm, triển khai logic tạo/cập nhật trung tâm và triển khai gán/rút quyền Center Admin cho người dùng.

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép (Các tệp, đường dẫn và điểm cuối)
- `./sources/backend/centers/CenterController.java`
- `./sources/backend/centers/CenterService.java`
- `./sources/backend/centers/CenterAdminService.java`
- `./sources/backend/centers/CenterRepository.java`
- `./sources/backend/centers/Center.java`
- `./sources/backend/centers/CenterAdmin.java`
- `./sources/backend/centers/CenterControllerTest.java`
- `./sources/backend/centers/CenterServiceTest.java`
- `./sources/docs/phase2-documentation.md`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm xây dựng mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Nhà kiểm thử Chất lượng Chuyên nghiệp. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng kiểm soát chất lượng. Trách nhiệm tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật Chuyên nghiệp và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách Kỹ thuật toàn diện, tài liệu tham khảo lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp bậc thang dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp rõ ràng kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chướng ngại vật cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc dịch vụ vi mô vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Triển khai hoàn chỉnh controller danh sách trung tâm.
- Triển khai hoàn chỉnh logic tạo/cập nhật trung tâm.
- Triển khai hoàn chỉnh gán/rút quyền Center Admin cho người dùng.
- Đảm bảo tuân thủ OWASP và hoàn thành kiểm thử chức năng cho các yêu cầu đã phân bổ.
- Đảm bảo ánh xạ 100% ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: Xây dựng controller danh sách trung tâm

#### 📝 Nhiệm vụ con 1.1: Triển khai CenterController để hiển thị danh sách trung tâm

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/centers/CenterController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-002], [REQ-004], [DAT-003]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Tạo tài liệu kỹ thuật cho giai đoạn 2

##### Chuyên viên được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/phase2-documentation.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-002], [REQ-004], [DAT-003]<!--END_TAGS-->

### 🌤️ Ngày 2: Triển khai logic tạo/cập nhật trung tâm

#### 📝 Nhiệm vụ con 2.1: Triển khai logic tạo/cập nhật trung tâm trong CenterService

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/centers/CenterService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-005], [DAT-003]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Viết bộ kiểm thử cho CenterController và CenterService

##### Chuyên viên được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/centers/CenterControllerTest.java;./sources/backend/centers/CenterServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-005], [DAT-003]<!--END_TAGS-->

### 🌤️ Ngày 3: Triển khai gán/rút quyền Center Admin

#### 📝 Nhiệm vụ con 3.1: Triển khai gán/rút quyền Center Admin cho người dùng trong CenterAdminService

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/centers/CenterAdminService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-006], [ARC-002], [DAT-003]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.2: Viết bộ kiểm thử cho CenterAdminService

##### Chuyên viên được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/centers/CenterAdminServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-006], [ARC-002], [DAT-003]<!--END_TAGS-->

### 🌤️ Ngày 4: Triển khai manifest GKE cho dịch vụ trung tâm

#### 📝 Nhiệm vụ con 4.1: Tạo manifest triển khai dịch vụ quản lý trung tâm trên GKE

##### Chuyên viên được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/k8s/center-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001], [NFR-003], [NFR-004]<!--END_TAGS-->