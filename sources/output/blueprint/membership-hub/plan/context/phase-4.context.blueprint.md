# Giai đoạn 4: Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Bản vẽ** | ARCH-20260807025651 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | Triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống |
| **Mô tả** | Giai đoạn này tập trung vào việc triển khai hệ thống ghi danh học viên, điểm danh QR, quản lý thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 02:56:51 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc triển khai hệ thống ghi danh học viên, điểm danh QR, quản lý thẻ hội viên, thông báo, khuyến mãi, thông báo và cài đặt hệ thống, bao gồm:
- Ghi danh học viên vào khóa học
- Điểm danh học viên qua mã QR
- Quản lý thẻ hội viên
- Gửi thông báo đến học viên và nhóm Zalo
- Quản lý khuyến mãi và thông báo
- Cài đặt hệ thống

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép
- `./sources/backend/enrollment/EnrollmentController.java`
- `./sources/backend/enrollment/EnrollmentService.java`
- `./sources/backend/enrollment/EnrollmentRepository.java`
- `./sources/backend/enrollment/Enrollment.java`
- `./sources/backend/enrollment/dto/EnrollmentRequest.java`
- `./sources/backend/enrollment/exception/EnrollmentNotFoundException.java`
- `./sources/backend/enrollment/exception/EnrollmentConflictException.java`
- `./sources/backend/enrollment/exception/InvalidEnrollmentDataException.java`
- `./sources/backend/attendance/AttendanceController.java`
- `./sources/backend/attendance/AttendanceService.java`
- `./sources/backend/attendance/AttendanceRepository.java`
- `./sources/backend/attendance/Attendance.java`
- `./sources/backend/attendance/dto/AttendanceRequest.java`
- `./sources/backend/attendance/exception/AttendanceNotFoundException.java`
- `./sources/backend/attendance/exception/AttendanceConflictException.java`
- `./sources/backend/attendance/exception/InvalidAttendanceDataException.java`
- `./sources/backend/membership/MembershipController.java`
- `./sources/backend/membership/MembershipService.java`
- `./sources/backend/membership/MembershipRepository.java`
- `./sources/backend/membership/Membership.java`
- `./sources/backend/membership/dto/MembershipRequest.java`
- `./sources/backend/membership/exception/MembershipNotFoundException.java`
- `./sources/backend/membership/exception/MembershipConflictException.java`
- `./sources/backend/membership/exception/InvalidMembershipDataException.java`
- `./sources/backend/notifications/NotificationController.java`
- `./sources/backend/notifications/NotificationService.java`
- `./sources/backend/notifications/NotificationRepository.java`
- `./sources/backend/notifications/Notification.java`
- `./sources/backend/notifications/dto/NotificationRequest.java`
- `./sources/backend/notifications/exception/NotificationNotFoundException.java`
- `./sources/backend/notifications/exception/NotificationConflictException.java`
- `./sources/backend/notifications/exception/InvalidNotificationDataException.java`
- `./sources/backend/promotions/PromotionController.java`
- `./sources/backend/promotions/PromotionService.java`
- `./sources/backend/promotions/PromotionRepository.java`
- `./sources/backend/promotions/Promotion.java`
- `./sources/backend/promotions/dto/PromotionRequest.java`
- `./sources/backend/promotions/exception/PromotionNotFoundException.java`
- `./sources/backend/promotions/exception/PromotionConflictException.java`
- `./sources/backend/promotions/exception/InvalidPromotionDataException.java`
- `./sources/backend/announcements/AnnouncementController.java`
- `./sources/backend/announcements/AnnouncementService.java`
- `./sources/backend/announcements/AnnouncementRepository.java`
- `./sources/backend/announcements/Announcement.java`
- `./sources/backend/announcements/dto/AnnouncementRequest.java`
- `./sources/backend/announcements/exception/AnnouncementNotFoundException.java`
- `./sources/backend/announcements/exception/AnnouncementConflictException.java`
- `./sources/backend/announcements/exception/InvalidAnnouncementDataException.java`
- `./sources/backend/systemsettings/SystemSettingController.java`
- `./sources/backend/systemsettings/SystemSettingService.java`
- `./sources/backend/systemsettings/SystemSettingRepository.java`
- `./sources/backend/systemsettings/SystemSetting.java`
- `./sources/backend/systemsettings/dto/SystemSettingRequest.java`
- `./sources/backend/systemsettings/exception/SystemSettingNotFoundException.java`
- `./sources/backend/systemsettings/exception/SystemSettingConflictException.java`
- `./sources/backend/systemsettings/exception/InvalidSystemSettingDataException.java`

## 3. Định nghĩa chức năng chuyên dụng của Sub-Agent
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

### 🌤️ Ngày 1: Xây dựng controller ghi danh khóa học

#### 📝 Nhiệm vụ con 1.1: Triển khai lớp EnrollmentController để xử lý đăng ký khóa học

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-004], [REQ-010], [DAT-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Tạo lớp EnrollmentRepository để tương tác với cơ sở dữ liệu

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentRepository.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.3: Xây dựng thực thể Enrollment

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/Enrollment.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.4: Tạo DTO cho yêu cầu ghi danh

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/dto/EnrollmentRequest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.5: Xây dựng các ngoại lệ tùy chỉnh cho quản lý ghi danh

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/exception/EnrollmentNotFoundException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/exception/EnrollmentConflictException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/exception/InvalidEnrollmentDataException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

### 🌤️ Ngày 2: Triển khai logic đăng ký khóa học

#### 📝 Nhiệm vụ con 2.1: Triển khai lớp EnrollmentService để xử lý đăng ký khóa học

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-011], [DAT-005], [ARC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Tạo bộ kiểm thử cho lớp EnrollmentService

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/enrollment/tests/EnrollmentServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-011], [DAT-005], [ARC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.3: Tạo tài liệu kiến trúc cho hệ thống ghi danh học viên

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/enrollment-system.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-004]<!--END_TAGS-->

### 🌤️ Ngày 3: Triển khai dịch vụ điểm danh QR

#### 📝 Nhiệm vụ con 3.1: Triển khai lớp AttendanceController để xử lý điểm danh QR

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/AttendanceController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-007], [REQ-012], [DAT-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.2: Triển khai lớp AttendanceService để xử lý điểm danh QR

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/AttendanceService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-012], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.3: Tạo lớp AttendanceRepository để tương tác với cơ sở dữ liệu

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/AttendanceRepository.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.4: Xây dựng thực thể Attendance

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/Attendance.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.5: Tạo DTO cho yêu cầu điểm danh

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/dto/AttendanceRequest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-012]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.6: Xây dựng các ngoại lệ tùy chỉnh cho quản lý điểm danh

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/exception/AttendanceNotFoundException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/attendance/exception/AttendanceConflictException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/attendance/exception/InvalidAttendanceDataException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.7: Tạo bộ kiểm thử cho lớp AttendanceService

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/attendance/tests/AttendanceServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-012], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->

### 🌤️ Ngày 4: Triển khai dịch vụ thông báo

#### 📝 Nhiệm vụ con 4.1: Triển khai lớp NotificationController để xử lý thông báo

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notifications/NotificationController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008], [REQ-016], [DAT-008]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.2: Triển khai lớp NotificationService để xử lý thông báo

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notifications/NotificationService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.3: Tạo lớp NotificationRepository để tương tác với cơ sở dữ liệu

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notifications/NotificationRepository.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-008]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.4: Xây dựng thực thể Notification

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notifications/Notification.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-008]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.5: Tạo DTO cho yêu cầu thông báo

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notifications/dto/NotificationRequest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-016]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.6: Xây dựng các ngoại lệ tùy chỉnh cho quản lý thông báo

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notifications/exception/NotificationNotFoundException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/notifications/exception/NotificationConflictException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/notifications/exception/InvalidNotificationDataException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.7: Tạo bộ kiểm thử cho lớp NotificationService

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/notifications/tests/NotificationServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->

### 🌤️ Ngày 5: Triển khai controller thẻ hội viên, khuyến mãi, thông báo và cài đặt hệ thống

#### 📝 Nhiệm vụ con 5.1: Triển khai lớp MembershipController để xử lý thẻ hội viên

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/membership/MembershipController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.2: Triển khai lớp MembershipService để xử lý thẻ hội viên

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/membership/MembershipService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.3: Tạo lớp MembershipRepository để tương tác với cơ sở dữ liệu

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/membership/MembershipRepository.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-007], [DAT-009], [DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.4: Xây dựng thực thể Membership

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/membership/Membership.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-007], [DAT-009], [DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.5: Tạo DTO cho yêu cầu thẻ hội viên

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/membership/dto/MembershipRequest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.6: Xây dựng các ngoại lệ tùy chỉnh cho quản lý thẻ hội viên

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/membership/exception/MembershipNotFoundException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/membership/exception/MembershipConflictException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/membership/exception/InvalidMembershipDataException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.7: Tạo bộ kiểm thử cho lớp MembershipService

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/membership/tests/MembershipServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.8: Triển khai lớp PromotionController để xử lý khuyến mãi

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/promotions/PromotionController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017], [DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.9: Triển khai lớp PromotionService để xử lý khuyến mãi

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/promotions/PromotionService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017], [DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.10: Tạo lớp PromotionRepository để tương tác với cơ sở dữ liệu

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/promotions/PromotionRepository.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.11: Xây dựng thực thể Promotion

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/promotions/Promotion.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.12: Tạo DTO cho yêu cầu khuyến mãi

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/promotions/dto/PromotionRequest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.13: Xây dựng các ngoại lệ tùy chỉnh cho quản lý khuyến mãi

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/promotions/exception/PromotionNotFoundException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/promotions/exception/PromotionConflictException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/promotions/exception/InvalidPromotionDataException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.14: Tạo bộ kiểm thử cho lớp PromotionService

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/promotions/tests/PromotionServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017], [DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.15: Triển khai lớp AnnouncementController để xử lý thông báo

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/announcements/AnnouncementController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018], [DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.16: Triển khai lớp AnnouncementService để xử lý thông báo

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/announcements/AnnouncementService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018], [DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.17: Tạo lớp AnnouncementRepository để tương tác với cơ sở dữ liệu

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/announcements/AnnouncementRepository.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.18: Xây dựng thực thể Announcement

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/announcements/Announcement.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.19: Tạo DTO cho yêu cầu thông báo

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/announcements/dto/AnnouncementRequest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.20: Xây dựng các ngoại lệ tùy chỉnh cho quản lý thông báo

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/announcements/exception/AnnouncementNotFoundException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/announcements/exception/AnnouncementConflictException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/announcements/exception/InvalidAnnouncementDataException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.21: Tạo bộ kiểm thử cho lớp AnnouncementService

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/announcements/tests/AnnouncementServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018], [DAT-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.22: Triển khai lớp SystemSettingController để xử lý cài đặt hệ thống

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/SystemSettingController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.23: Triển khai lớp SystemSettingService để xử lý cài đặt hệ thống

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/SystemSettingService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.24: Tạo lớp SystemSettingRepository để tương tác với cơ sở dữ liệu

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/SystemSettingRepository.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.25: Xây dựng thực thể SystemSetting

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/SystemSetting.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.26: Tạo DTO cho yêu cầu cài đặt hệ thống

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/dto/SystemSettingRequest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.27: Xây dựng các ngoại lệ tùy chỉnh cho quản lý cài đặt hệ thống

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/exception/SystemSettingNotFoundException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/exception/SystemSettingConflictException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/exception/InvalidSystemSettingDataException.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[EXC-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.28: Tạo bộ kiểm thử cho lớp SystemSettingService

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/systemsettings/tests/SystemSettingServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

### 🌤️ Ngày 6: Kiểm tra và tối ưu hóa mã nguồn

#### 📝 Nhiệm vụ con 6.1: Kiểm tra và sửa lỗi biên dịch

##### Chuyên gia được chỉ định: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-004], [REQ-010], [DAT-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-011], [DAT-005], [ARC-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/attendance/AttendanceController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-007], [REQ-012], [DAT-006]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/attendance/AttendanceService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-012], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/membership/MembershipController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/membership/MembershipService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/notifications/NotificationController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008], [REQ-016], [DAT-008]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/notifications/NotificationService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/promotions/PromotionController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017], [DAT-009]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/promotions/PromotionService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017], [DAT-009]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/announcements/AnnouncementController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018], [DAT-009]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/announcements/AnnouncementService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018], [DAT-009]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/SystemSettingController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/SystemSettingService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 6.2: Kiểm tra chất lượng mã và bảo mật

##### Chuyên gia được chỉ định: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-011], [DAT-005], [ARC-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/attendance/AttendanceService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-012], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/membership/MembershipService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007], [DAT-009], [DAT-011], [EXC-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/notifications/NotificationService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/promotions/PromotionService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017], [DAT-009]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/announcements/AnnouncementService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018], [DAT-009]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/backend/systemsettings/SystemSettingService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 6.3: Cập nhật tài liệu kỹ thuật

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/enrollment-system.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-004]<!--END_TAGS-->

### 🌤️ Ngày 7: Triển khai và kiểm thử tích hợp

#### 📝 Nhiệm vụ con 7.1: Triển khai dịch vụ ghi danh học viên lên môi trường thử nghiệm

##### Chuyên gia được chỉ định: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/enrollment-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.2: Triển khai dịch vụ điểm danh QR lên môi trường thử nghiệm

##### Chuyên gia được chỉ định: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/attendance-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-007]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.3: Triển khai dịch vụ thông báo lên môi trường thử nghiệm

##### Chuyên gia được chỉ định: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/notification-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.4: Triển khai dịch vụ thẻ hội viên lên môi trường thử nghiệm

##### Chuyên gia được chỉ định: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/membership-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.5: Triển khai dịch vụ khuyến mãi lên môi trường thử nghiệm

##### Chuyên gia được chỉ định: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/promotion-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.6: Triển khai dịch vụ thông báo lên môi trường thử nghiệm

##### Chuyên gia được chỉ định: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/announcement-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.7: Triển khai dịch vụ cài đặt hệ thống lên môi trường thử nghiệm

##### Chuyên gia được chỉ định: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/systemsetting-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.8: Kiểm thử tích hợp cho hệ thống ghi danh học viên

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/enrollment/tests/integration/EnrollmentIntegrationTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-010], [REQ-011], [ARC-004], [ARC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.9: Kiểm thử tích hợp cho hệ thống điểm danh QR

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/attendance/tests/integration/AttendanceIntegrationTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-012], [ARC-007], [EXC-001], [EXC-002]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.10: Kiểm thử tích hợp cho hệ thống thông báo

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/notifications/tests/integration/NotificationIntegrationTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-016], [ARC-008], [EXC-003]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.11: Kiểm thử tích hợp cho hệ thống thẻ hội viên

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/membership/tests/integration/MembershipIntegrationTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [EXC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.12: Kiểm thử tích hợp cho hệ thống khuyến mãi

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/promotions/tests/integration/PromotionIntegrationTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.13: Kiểm thử tích hợp cho hệ thống thông báo

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/announcements/tests/integration/AnnouncementIntegrationTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.14: Kiểm thử tích hợp cho hệ thống cài đặt hệ thống

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/systemsettings/tests/integration/SystemSettingIntegrationTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.15: Kiểm tra hiệu suất và tải

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/performance/EnrollmentPerformanceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/performance/AttendancePerformanceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/performance/NotificationPerformanceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/performance/MembershipPerformanceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/performance/PromotionPerformanceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/performance/AnnouncementPerformanceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/performance/SystemSettingPerformanceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001]<!--END_TAGS-->

### 🌤️ Ngày 8: Triển khai và kiểm thử trên môi trường sản xuất

#### 📝 Nhiệm vụ con 8.1: Triển khai dịch vụ ghi danh học viên lên môi trường sản xuất

##### Chuyên gia được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/enrollment-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.2: Triển khai dịch vụ điểm danh QR lên môi trường sản xuất

##### Chuyên gia được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/attendance-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-007]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.3: Triển khai dịch vụ thông báo lên môi trường sản xuất

##### Chuyên gia được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/notification-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.4: Triển khai dịch vụ thẻ hội viên lên môi trường sản xuất

##### Chuyên gia được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/membership-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.5: Triển khai dịch vụ khuyến mãi lên môi trường sản xuất

##### Chuyên gia được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/promotion-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.6: Triển khai dịch vụ thông báo lên môi trường sản xuất

##### Chuyên gia được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/announcement-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.7: Triển khai dịch vụ cài đặt hệ thống lên môi trường sản xuất

##### Chuyên gia được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/systemsetting-service-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.8: Kiểm thử cuối cùng trên môi trường sản xuất

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/e2e/EnrollmentE2ETest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-010], [REQ-011], [ARC-004], [ARC-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/e2e/AttendanceE2ETest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-012], [ARC-007], [EXC-001], [EXC-002]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/e2e/NotificationE2ETest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-016], [ARC-008], [EXC-003]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/e2e/MembershipE2ETest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [EXC-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/e2e/PromotionE2ETest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-017]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/e2e/AnnouncementE2ETest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-018]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/backend/tests/e2e/SystemSettingE2ETest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[DAT-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 8.9: Cập nhật tài liệu triển khai

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/deployment-guide.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-004], [ARC-007], [ARC-008], [REQ-014], [REQ-015], [REQ-017], [REQ-018], [DAT-011]<!--END_TAGS-->