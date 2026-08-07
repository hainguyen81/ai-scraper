# Giai đoạn 1: Xây dựng lõi người dùng, vai trò và xác thực cơ bản (bao gồm đăng ký, OAuth2, JWT và validation đầu vào)

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Bản vẽ** | ARCH-20260807025651 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên giai đoạn** | Xây dựng lõi người dùng, vai trò và xác thực cơ bản (bao gồm đăng ký, OAuth2, JWT và validation đầu vào) |
| **Mô tả** | Giai đoạn này tập trung vào việc xây dựng hệ thống xác thực người dùng cơ bản, bao gồm đăng ký qua email/mật khẩu, xác thực qua mạng xã hội (Firebase, Google, Facebook), phân quyền người dùng và quản lý token JWT. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 02:56:51 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc xây dựng hệ thống xác thực người dùng cơ bản, bao gồm:
- Đăng ký người dùng qua email và mật khẩu
- Xác thực qua mạng xã hội (Firebase, Google, Facebook)
- Phân quyền người dùng (System Admin, Center Admin, Manager, Teacher, Student)
- Quản lý token JWT với thời hạn 15 phút và refresh token

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép
- `./sources/backend/users/UserService.java`
- `./sources/backend/users/AuthController.java`
- `./sources/backend/users/UserRepository.java`
- `./sources/backend/users/User.java`
- `./sources/backend/users/Role.java`
- `./sources/backend/users/dto/UserRegistrationRequest.java`
- `./sources/backend/users/dto/SocialAuthRequest.java`
- `./sources/backend/users/dto/RoleAssignmentRequest.java`
- `./sources/backend/users/exception/InvalidInputException.java`
- `./sources/backend/users/exception/DuplicateEmailException.java`
- `./sources/backend/users/exception/AuthenticationException.java`
- `./sources/backend/users/security/JwtTokenProvider.java`
- `./sources/backend/users/security/CustomUserDetailsService.java`
- `./sources/backend/users/security/SecurityConfig.java`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Chức năng như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và các ứng dụng khách frontend/mobile. Bị cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Chức năng như một Nhà kiểm thử Chất lượng/Chuyên gia QC. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E và kịch bản xác nhận hiệu suất. Bị cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con nhiệm vụ liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị giới hạn, bạn PHẢI xuất ra chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn tài liệu Kỹ thuật Chi tiết, tài liệu tham khảo lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp công nghệ hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp rõ ràng kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh và vá lỗ hổng phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR) và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai tải trọng dịch vụ vi mô vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này
- Đảm bảo 100% độ phủ kiểm thử chức năng
- Đảm bảo 100% ánh xạ ID Tag
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP
- Đảm bảo mã nguồn được kiểm tra và phê duyệt bởi Reviewer

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: Triển khai dịch vụ quản lý người dùng cơ bản

#### 📝 Nhiệm vụ con 1.1: Triển khai lớp UserService để xử lý đăng ký người dùng mới

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/UserService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-001], [DAT-001]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Tạo lớp UserRepository để tương tác với cơ sở dữ liệu

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/UserRepository.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-001]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.3: Xây dựng các thực thể User và Role

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/User.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-001]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/users/Role.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-001]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.4: Tạo các DTO cho yêu cầu đăng ký và xác thực xã hội

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/dto/UserRegistrationRequest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-001]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/users/dto/SocialAuthRequest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-002]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.5: Xây dựng các ngoại lệ tùy chỉnh cho xác thực đầu vào

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/exception/InvalidInputException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/users/exception/DuplicateEmailException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/users/exception/AuthenticationException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

### 🌤️ Ngày 2: Xây dựng controller xác thực và tích hợp OAuth2

#### 📝 Nhiệm vụ con 2.1: Xây dựng lớp AuthController để xử lý xác thực

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/AuthController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-002], [REQ-003], [ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Triển khai lớp JwtTokenProvider để quản lý token JWT

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/security/JwtTokenProvider.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.3: Xây dựng lớp CustomUserDetailsService để tải thông tin người dùng

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/security/CustomUserDetailsService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.4: Cấu hình bảo mật ứng dụng

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/security/SecurityConfig.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.5: Tạo bộ kiểm thử cho các lớp xác thực

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/users/tests/AuthControllerTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-002], [REQ-003], [ARC-006]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/users/tests/JwtTokenProviderTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.6: Tạo tài liệu kiến trúc cho hệ thống xác thực

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/authentication-system.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

### 🌤️ Ngày 3: Kiểm tra và tối ưu hóa mã nguồn

#### 📝 Nhiệm vụ con 3.1: Kiểm tra và sửa lỗi biên dịch

##### Chuyên gia được chỉ định: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/UserService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-001], [DAT-001]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/users/AuthController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-002], [REQ-003], [ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.2: Kiểm tra chất lượng mã và bảo mật

##### Chuyên gia được chỉ định: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/users/security/JwtTokenProvider.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/users/security/SecurityConfig.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.3: Cập nhật tài liệu kỹ thuật

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/authentication-system.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

### 🌤️ Ngày 4: Triển khai và kiểm thử tích hợp

#### 📝 Nhiệm vụ con 4.1: Triển khai dịch vụ xác thực lên môi trường thử nghiệm

##### Chuyên gia được chỉ định: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/auth-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.2: Kiểm thử tích hợp cho hệ thống xác thực

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/users/tests/integration/AuthIntegrationTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-002], [REQ-003], [ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.3: Kiểm tra hiệu suất và tải

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/users/tests/performance/AuthPerformanceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001]<!--END_TAGS-->

### 🌤️ Ngày 5: Triển khai và kiểm thử trên môi trường sản xuất

#### 📝 Nhiệm vụ con 5.1: Triển khai dịch vụ xác thực lên môi trường sản xuất

##### Chuyên gia được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/auth-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.2: Kiểm thử cuối cùng trên môi trường sản xuất

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/users/tests/e2e/AuthE2ETest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-002], [REQ-003], [ARC-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.3: Cập nhật tài liệu triển khai

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/deployment-guide.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->