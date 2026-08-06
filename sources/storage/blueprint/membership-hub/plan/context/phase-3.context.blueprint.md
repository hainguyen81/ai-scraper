# Giai đoạn 3: Xây dựng dịch vụ thông báo, cập nhật giao diện web và tài liệu bảo mật

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260806145545 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng dịch vụ thông báo, cập nhật giao diện web và tài liệu bảo mật<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Xây dựng dịch vụ thông báo, cập nhật giao diện web và tài liệu bảo mật<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/06 14:55:45 |
| **Tác giả** | Kiến trúc hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản trị kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 3 tập trung vào việc xây dựng dịch vụ thông báo, cập nhật giao diện web và tài liệu bảo mật. Các nhiệm vụ bao gồm:
- Xây dựng dịch vụ thông báo với các chức năng gửi thông báo qua ứng dụng di động và nhóm Zalo.
- Cập nhật giao diện web với các chức năng nhận thông báo.
- Tạo tài liệu bảo mật mô tả các quy tắc bảo mật và xử lý ngoại lệ.

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép
- `./sources/backend/notification-service`
- `./sources/frontend/web-app`
- `./sources/docs/security.md`

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

### 🌤️ Ngày 5: Xây dựng dịch vụ thông báo

#### 📝 Nhiệm vụ con 1.1: Xây dựng dịch vụ thông báo
##### Đặc vụ được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/service/NotificationService.java`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[REQ-016], [ARC-008], [DAT-008]<!--END_TAGS-->

### 🌤️ Ngày 6: Cập nhật giao diện web và tài liệu bảo mật

#### 📝 Nhiệm vụ con 2.1: Cập nhật giao diện web
##### Đặc vụ được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend/web-app/src/components/notification/index.tsx`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[ARC-009]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Tạo tài liệu bảo mật
##### Đặc vụ được chỉ định: Doc
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/security.md`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[NFR-003]<!--END_TAGS-->