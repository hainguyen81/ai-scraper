# Giai đoạn 4: Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260807060838 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 06:08:38 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý Kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 4 tập trung vào việc triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống. Giai đoạn này bao gồm việc xây dựng controller ghi danh khóa học, triển khai logic đăng ký khóa học, triển khai dịch vụ điểm danh QR, triển khai dịch vụ thông báo, triển khai controller thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống.

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép (Các tệp, đường dẫn và điểm cuối)
- `./sources/backend/enrollment/EnrollmentController.java`
- `./sources/backend/enrollment/EnrollmentService.java`
- `./sources/backend/attendance/AttendanceService.java`
- `./sources/backend/notifications/NotificationService.java`
- `./sources/backend/membership/MembershipController.java`
- `./sources/backend/enrollment/EnrollmentRepository.java`
- `./sources/backend/enrollment/Enrollment.java`
- `./sources/backend/attendance/AttendanceRepository.java`
- `./sources/backend/attendance/Attendance.java`
- `./sources/backend/notifications/NotificationRepository.java`
- `./sources/backend/notifications/Notification.java`
- `./sources/backend/membership/MembershipRepository.java`
- `./sources/backend/membership/Membership.java`
- `./sources/backend/enrollment/EnrollmentControllerTest.java`
- `./sources/backend/enrollment/EnrollmentServiceTest.java`
- `./sources/backend/attendance/AttendanceServiceTest.java`
- `./sources/backend/notifications/NotificationServiceTest.java`
- `./sources/backend/membership/MembershipControllerTest.java`
- `./sources/docs/phase4-documentation.md`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm xây dựng mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Nhà kiểm thử Chất lượng Chuyên nghiệp. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng kiểm soát chất lượng. Trách nhiệm tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật Chuyên nghiệp và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách Kỹ thuật toàn diện, tài liệu tham khảo lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp bậc thang dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp rõ ràng kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chướng ngại vật cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc dịch vụ vi mô vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Triển khai hoàn chỉnh controller ghi danh khóa học.
- Triển khai hoàn chỉnh logic đăng ký khóa học.
- Triển khai hoàn chỉnh dịch vụ điểm danh QR.
- Triển khai hoàn chỉnh dịch vụ thông báo.
- Triển khai hoàn chỉnh controller thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống.
- Đảm bảo tuân thủ OWASP và hoàn thành kiểm thử chức năng cho các yêu cầu đã phân bổ.
- Đảm bảo ánh xạ 100% ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: Xây dựng controller ghi danh khóa học

#### 📝 Nhiệm vụ con 1.1: Triển khai EnrollmentController để duyệt khóa học và xử lý đăng ký

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-004], [REQ-010], [DAT-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Tạo tài liệu kỹ thuật cho giai đoạn 4

##### Chuyên viên được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/phase4-documentation.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-004], [REQ-010], [DAT-005]<!--END_TAGS-->

### 🌤️ Ngày 2: Triển khai logic đăng ký khóa học

#### 📝 Nhiệm vụ con 2.1: Triển khai logic đăng ký khóa học trong EnrollmentService

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-011], [DAT-005], [ARC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Viết bộ kiểm thử cho EnrollmentController và EnrollmentService

##### Chuyên viên được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentControllerTest.java;./sources/backend/enrollment/EnrollmentServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-011], [DAT-005], [ARC-005]<!--END_TAGS-->

### 🌤️ Ngày 3: Triển khai dịch vụ điểm danh QR

#### 📝 Nhiệm vụ con 3.1: Triển khai dịch vụ điểm danh QR trong AttendanceService

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/AttendanceService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-007], [REQ-012], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.2: Viết bộ kiểm thử cho AttendanceService

##### Chuyên viên được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/AttendanceServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-007], [REQ-012], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->

### 🌤️ Ngày 4: Triển khai dịch vụ thông báo

#### 📝 Nhiệm vụ con 4.1: Triển khai dịch vụ thông báo trong NotificationService

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notifications/NotificationService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008], [REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.2: Viết bộ kiểm thử cho NotificationService

##### Chuyên viên được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notifications/NotificationServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008], [REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->

### 🌤️ Ngày 5: Triển khai controller thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống

#### 📝 Nhiệm vụ con 5.1: Triển khai MembershipController để hiển thị thẻ hội viên và xử lý gia hạn thẻ

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/membership/MembershipController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.2: Viết bộ kiểm thử cho MembershipController

##### Chuyên viên được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/membership/MembershipControllerTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->