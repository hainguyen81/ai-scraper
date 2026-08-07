# Giai đoạn 1: Xây dựng lõi người dùng, vai trò và xác thực cơ bản (bao gồm đăng ký, OAuth2, JWT và validation đầu vào)

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260807060838 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Xây dựng lõi người dùng, vai trò và xác thực cơ bản (bao gồm đăng ký, OAuth2, JWT và validation đầu vào)<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 06:08:38 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý Kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 1 tập trung vào việc xây dựng lõi người dùng, vai trò và xác thực cơ bản (bao gồm đăng ký, OAuth2, JWT và validation đầu vào). Giai đoạn này bao gồm việc triển khai dịch vụ quản lý người dùng cơ bản, xây dựng controller xác thực và tích hợp OAuth2, cũng như triển khai cơ sở dữ liệu và API liên quan.

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép (Các tệp, đường dẫn và điểm cuối)
- `./sources/backend/users/UserService.java`
- `./sources/backend/users/AuthController.java`
- `./sources/backend/users/UserRepository.java`
- `./sources/backend/users/User.java`
- `./sources/backend/users/Role.java`
- `./sources/backend/users/AuthService.java`
- `./sources/backend/users/AuthControllerTest.java`
- `./sources/backend/users/UserServiceTest.java`
- `./sources/docs/phase1-documentation.md`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm xây dựng mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Nhà kiểm thử Chất lượng Chuyên nghiệp. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng kiểm soát chất lượng. Trách nhiệm tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật Chuyên nghiệp và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách Kỹ thuật toàn diện, tài liệu tham khảo lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp bậc thang dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp rõ ràng kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chướng ngại vật cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc dịch vụ vi mô vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Triển khai hoàn chỉnh dịch vụ quản lý người dùng cơ bản.
- Xây dựng controller xác thực và tích hợp OAuth2.
- Triển khai cơ sở dữ liệu và API liên quan.
- Đảm bảo tuân thủ OWASP và hoàn thành kiểm thử chức năng cho các yêu cầu đã phân bổ.
- Đảm bảo ánh xạ 100% ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: Triển khai dịch vụ quản lý người dùng cơ bản

#### 📝 Nhiệm vụ con 1.1: Triển khai lớp UserService để xử lý đăng ký người dùng mới

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/UserService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-001], [REQ-001], [DAT-001]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Tạo bảng Users và Roles trong cơ sở dữ liệu

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/UserRepository.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-001]<!--END_TAGS-->

### 🌤️ Ngày 2: Xây dựng controller xác thực và tích hợp OAuth2

#### 📝 Nhiệm vụ con 2.1: Xây dựng AuthController để xử lý xác thực OAuth2 từ Firebase/Google/Facebook

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/AuthController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006], [REQ-002], [REQ-003], [DAT-001]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Triển khai AuthService để xử lý logic xác thực và cấp JWT token

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/AuthService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006], [REQ-002], [REQ-003]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.3: Viết bộ kiểm thử cho AuthController và UserService

##### Chuyên viên được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/AuthControllerTest.java;./sources/backend/users/UserServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-002], [REQ-003]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.4: Tạo tài liệu kỹ thuật cho giai đoạn 1

##### Chuyên viên được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/phase1-documentation.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-001], [ARC-006], [REQ-001], [REQ-002], [REQ-003], [DAT-001]<!--END_TAGS-->