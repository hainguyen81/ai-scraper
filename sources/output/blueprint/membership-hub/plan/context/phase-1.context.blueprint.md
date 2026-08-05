# Giai đoạn 1: <!--PHASE_NAME_START-->Xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805160938 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 16:09:38 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị Kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 1 tập trung vào việc xây dựng dịch vụ xác thực, quản lý trung tâm và khóa học. Dịch vụ xác thực sẽ hỗ trợ đăng ký và đăng nhập qua email/mật khẩu và OAuth2. Dịch vụ quản lý trung tâm sẽ cho phép tạo, cập nhật và xóa trung tâm. Dịch vụ quản lý khóa học sẽ cho phép tạo, cập nhật và xóa khóa học, và phân công giáo viên vào khóa học.

## 2. Phạm vi kỹ thuật và biên giới thư mục (Tệp, đường dẫn và điểm cuối)
- `./sources/backend/auth`
- `./sources/backend/centers`
- `./sources/backend/courses`

## 3. Hướng dẫn chức năng của Sub-Agent chuyên dụng
*   **Coder**: Hoạt động như một Lập trình viên Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm về việc triển khai mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng khách frontend/mobile. Cấm viết bộ kiểm tra hoặc biểu mẫu cơ sở hạ tầng.
*   **Tester**: Hoạt động như một Trưởng/QA Chất lượng Kiểm soát. Chuyên về kỹ thuật bộ kiểm tra, xác nhận và cổng chất lượng. Trách nhiệm về việc tạo bộ kiểm tra JUnit, kiểm tra tích hợp, kiểm tra tự động E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật Chuyên nghiệp và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn các tài liệu kỹ thuật Markdown toàn diện, tham chiếu lược đồ, bản đồ hệ thống và danh mục kiến trúc. Mỗi tệp tài liệu được tạo ra phải nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
    # YÊU CẦU CẤP CAO CỦA ĐẠI LÝ TÀI LIỆU (CỔNG QUAN TRỌNG):
    - Bạn bị CẤM nghiêm ngặt từ bỏ hoặc loại bỏ đại lý 'Doc' khỏi bất kỳ giai đoạn nào được tính toán.
    - Đối với MỖI giai đoạn được tính toán, vào **Ngày 1** của giai đoạn đó, bạn PHẢI phân bổ một nhiệm vụ tài liệu hệ thống cơ bản cho đại lý **Doc**. Nhiệm vụ này PHẢI yêu cầu đại lý 'Doc' lập bản đồ kiến trúc, điểm cuối, lược đồ cơ sở dữ liệu hoặc bản đồ topology triển khai tương ứng với ngăn xếp hoạt động của giai đoạn đó.
    - Thất bại trong việc phân bổ đại lý 'Doc' vào Ngày 1 của bất kỳ giai đoạn nào sẽ gây ra vi phạm hợp đồng kỹ thuật thảm khốc.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm về việc xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm về việc xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng microservices vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này.
- Đảm bảo 100% tuân thủ các tiêu chuẩn bảo mật OWASP.
- Đảm bảo 100% độ phủ kiểm tra chức năng cho các yêu cầu được phân bổ.
- Đảm bảo 100% ánh xạ ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ XÁC THỰC<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 1.1: <!--SUB_TASK_START-->Triển khai dịch vụ xác thực với các phương thức đăng ký và đăng nhập qua email/mật khẩu và OAuth2<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-001], [REQ-002], [DAT-001]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: <!--SUB_TASK_START-->Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ xác thực<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth;./sources/backend/auth/src/test/java/org/nlh4j/saas/membershiphub/auth/AuthServiceTest.java`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-001], [REQ-002]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.3: <!--SUB_TASK_START-->Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/auth`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-001], [REQ-002]<!--END_TAGS-->

### 🌤️ Ngày 2: <!--DAY_HEADER_START-->XÂY DỰNG DỊCH VỤ QUẢN LÝ TRUNG TÂM VÀ KHÓA HỌC<!--DAY_HEADER_END-->

#### 📝 Nhiệm vụ con 2.1: <!--SUB_TASK_START-->Triển khai dịch vụ quản lý trung tâm và khóa học<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/centers`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [DAT-003]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: <!--SUB_TASK_START-->Viết các bài kiểm tra đơn vị và tích hợp cho dịch vụ quản lý trung tâm và khóa học<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/centers;./sources/backend/centers/src/test/java/org/nlh4j/saas/membershiphub/centers/CenterServiceTest.java`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.3: <!--SUB_TASK_START-->Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình<!--SUB_TASK_END-->
##### Đại lý được chỉ định: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/centers`
* **Token ID theo dõi:** <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->