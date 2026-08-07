# Giai đoạn 3: Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260807060838 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 06:08:38 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý Kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 3 tập trung vào việc xây dựng quản lý khóa học với xung đột lịch và phân công giáo viên. Giai đoạn này bao gồm việc xây dựng controller danh sách khóa học, triển khai logic tạo/cập nhật khóa học và triển khai gán/rút giáo viên vào khóa học.

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép (Các tệp, đường dẫn và điểm cuối)
- `./sources/backend/courses/CourseController.java`
- `./sources/backend/courses/CourseService.java`
- `./sources/backend/courses/CourseTeacherService.java`
- `./sources/backend/courses/CourseRepository.java`
- `./sources/backend/courses/Course.java`
- `./sources/backend/courses/CourseTeacher.java`
- `./sources/backend/courses/CourseControllerTest.java`
- `./sources/backend/courses/CourseServiceTest.java`
- `./sources/docs/phase3-documentation.md`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm xây dựng mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Nhà kiểm thử Chất lượng Chuyên nghiệp. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng kiểm soát chất lượng. Trách nhiệm tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật Chuyên nghiệp và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách Kỹ thuật toàn diện, tài liệu tham khảo lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp bậc thang dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp rõ ràng kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chướng ngại vật cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc dịch vụ vi mô vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Triển khai hoàn chỉnh controller danh sách khóa học.
- Triển khai hoàn chỉnh logic tạo/cập nhật khóa học.
- Triển khai hoàn chỉnh gán/rút giáo viên vào khóa học.
- Đảm bảo tuân thủ OWASP và hoàn thành kiểm thử chức năng cho các yêu cầu đã phân bổ.
- Đảm bảo ánh xạ 100% ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: Xây dựng controller danh sách khóa học

#### 📝 Nhiệm vụ con 1.1: Triển khai CourseController để hiển thị danh sách khóa học

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/courses/CourseController.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-003], [REQ-007], [DAT-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Tạo tài liệu kỹ thuật cho giai đoạn 3

##### Chuyên viên được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/phase3-documentation.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-003], [REQ-007], [DAT-004]<!--END_TAGS-->

### 🌤️ Ngày 2: Triển khai logic tạo/cập nhật khóa học

#### 📝 Nhiệm vụ con 2.1: Triển khai logic tạo/cập nhật khóa học trong CourseService

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/courses/CourseService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-008], [DAT-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Viết bộ kiểm thử cho CourseController và CourseService

##### Chuyên viên được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/courses/CourseControllerTest.java;./sources/backend/courses/CourseServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-008], [DAT-004]<!--END_TAGS-->

### 🌤️ Ngày 3: Triển khai gán/rút giáo viên vào khóa học

#### 📝 Nhiệm vụ con 3.1: Triển khai gán/rút giáo viên vào khóa học trong CourseTeacherService

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/courses/CourseTeacherService.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-009], [ARC-003], [DAT-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.2: Viết bộ kiểm thử cho CourseTeacherService

##### Chuyên viên được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/courses/CourseTeacherServiceTest.java
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-009], [ARC-003], [DAT-004]<!--END_TAGS-->