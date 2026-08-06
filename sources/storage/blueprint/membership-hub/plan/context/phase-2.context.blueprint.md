# Giai đoạn 2: Xây dựng dịch vụ khóa học, điểm danh, ứng dụng di động và tài liệu API

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260806145545 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng dịch vụ khóa học, điểm danh, ứng dụng di động và tài liệu API<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Xây dựng dịch vụ khóa học, dịch vụ điểm danh, ứng dụng di động, và tài liệu API<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/06 14:55:45 |
| **Tác giả** | Kiến trúc hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 2 tập trung vào việc xây dựng dịch vụ khóa học, dịch vụ điểm danh, ứng dụng di động, và tài liệu API. Các nhiệm vụ bao gồm:
- Xây dựng dịch vụ khóa học với các chức năng quản lý khóa học, phân công giáo viên, và điểm danh.
- Tạo dịch vụ điểm danh với các chức năng quét mã QR và xử lý điểm danh trùng lặp.
- Xây dựng ứng dụng di động với các chức năng điểm danh qua mã QR và nhận thông báo.
- Tạo tài liệu API mô tả các endpoint và hợp đồng sự kiện.

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép
- `./sources/backend/course-service`
- `./sources/backend/attendance-service`
- `./sources/frontend/mobile-app`
- `./sources/docs/api.md`

## 3. Hướng dẫn chức năng dành riêng cho Sub-Agent
* **Coder**: Hoạt động như một Lập trình viên Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Trưởng/QC/QA Cấp cao. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng kiểm soát chất lượng. Trách nhiệm về việc tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử E2E, và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu nhiệm vụ con mục tiêu liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn MUST strictly output the literal token `INTEGRATION_SCOPE` as the first parameter of the semicolon pair (e.g., `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết kỹ thuật Cấp cao và Kiến trúc hệ thống doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách Kỹ thuật toàn diện, tham chiếu lược đồ, bản thiết kế kiến trúc, và danh mục kiến trúc doanh nghiệp được tùy chỉnh cho các lớp topology dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra MUST được liệt kê như một thực thể đường dẫn tệp rõ ràng kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
* **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh, và vá lỗ hổng phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, sửa chữa lỗ hổng bảo mật OWASP, và giải quyết các chặn cổng chất lượng SonarQube.
* **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói, và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
* **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
* **GKE**: Chuyên về điều phối sản xuất container trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm, và triển khai tải trọng dịch vụ vi dịch vụ vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này.
- Đảm bảo tuân thủ các tiêu chuẩn doanh nghiệp OWASP.
- Đảm bảo độ phủ kiểm thử chức năng hoàn chỉnh cho các yêu cầu được phân bổ.
- Đảm bảo 100% ánh xạ Tag ID.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 3: Xây dựng dịch vụ khóa học và điểm danh

#### 📝 Nhiệm vụ con 1.1: Xây dựng dịch vụ khóa học
##### Đặc vụ được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/service/CourseService.java`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-004]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Xây dựng dịch vụ điểm danh
##### Đặc vụ được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/service/AttendanceService.java`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[REQ-012], [REQ-013], [DAT-006]<!--END_TAGS-->

### 🌤️ Ngày 4: Xây dựng ứng dụng di động và tài liệu API

#### 📝 Nhiệm vụ con 2.1: Xây dựng ứng dụng di động
##### Đặc vụ được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend/mobile-app/src/screens/attendance/index.tsx`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[ARC-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Tạo tài liệu API
##### Đặc vụ được chỉ định: Doc
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/api.md`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[ARC-003], [ARC-004]<!--END_TAGS-->