# Giai đoạn 2: <!--PHASE_NAME_START-->Xây dựng dịch vụ đăng ký, điểm danh và quản lý thẻ hội viên<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805162429 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng dịch vụ đăng ký, điểm danh và quản lý thẻ hội viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Xây dựng dịch vụ đăng ký, điểm danh và quản lý thẻ hội viên<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 16:24:29 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 2 tập trung vào việc xây dựng dịch vụ đăng ký, điểm danh và quản lý thẻ hội viên. Các nhiệm vụ bao gồm triển khai dịch vụ đăng ký khóa học và điểm danh, triển khai dịch vụ quản lý thẻ hội viên, và viết các bài kiểm tra đơn vị và tích hợp cho các dịch vụ này.

## 2. Phạm vi kỹ thuật cho phép và ranh giới thư mục (Tệp, đường dẫn và điểm cuối)
- `./sources/backend/enrollments`
- `./sources/backend/attendance`
- `./sources/backend/membership`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng khách frontend/mobile. Cấm viết bộ kiểm tra hoặc biểu mẫu cơ sở hạ tầng.
*   **Tester**: Hoạt động như một Nhà kiểm soát chất lượng/Chuyên gia QC/QA cấp cao. Chuyên về kỹ thuật bộ kiểm tra, xác nhận và cổng chất lượng. Trách nhiệm là tạo các bộ kiểm tra JUnit, kiểm tra tích hợp, tự động hóa kiểm tra E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng.
*   **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm toán chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Doc**: Chức năng như một Nhà viết tài liệu kỹ thuật cấp cao và Kiến trúc sư hệ thống doanh nghiệp. Chuyên về biên soạn các tài liệu kỹ thuật Markdown toàn diện, tham chiếu lược đồ, bản đồ hệ thống và danh mục kiến trúc. Mỗi tệp tài liệu được tạo ra phải nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng microservices vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Triển khai hoàn chỉnh dịch vụ đăng ký khóa học và điểm danh.
- Triển khai hoàn chỉnh dịch vụ quản lý thẻ hội viên.
- Viết các bài kiểm tra đơn vị và tích hợp cho các dịch vụ này.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Đảm bảo 100% độ phủ chức năng cho các yêu cầu đã phân bổ.
- Đảm bảo 100% ánh xạ ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 3: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ ĐĂNG KÝ VÀ ĐIỂM DANH<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 3.1: Triển khai dịch vụ đăng ký khóa học và điểm danh
##### Chuyên viên được phân công: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollments`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-010], [REQ-011], [DAT-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.2: Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ đăng ký và điểm danh
##### Chuyên viên được phân công: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollments;./sources/backend/enrollments/src/test/java/org/nlh4j/saas/membershiphub/enrollments/EnrollmentServiceTest.java`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.3: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### Chuyên viên được phân công: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/enrollments`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-010], [REQ-011]<!--END_TAGS-->

### 🌤️ Ngày 4: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ QUẢN LÝ THẺ HỘI VIÊN<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 4.1: Triển khai dịch vụ quản lý thẻ hội viên
##### Chuyên viên được phân công: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/membership`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.2: Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ quản lý thẻ hội viên
##### Chuyên viên được phân công: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/membership;./sources/backend/membership/src/test/java/org/nlh4j/saas/membershiphub/membership/MembershipServiceTest.java`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.3: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### Chuyên viên được phân công: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/membership`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-014], [REQ-015]<!--END_TAGS-->