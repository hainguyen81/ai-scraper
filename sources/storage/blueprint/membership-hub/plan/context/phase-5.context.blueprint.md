# Giai đoạn 5: Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Bản vẽ** | ARCH-20260807025651 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps |
| **Mô tả** | Giai đoạn này tập trung vào việc phát triển giao diện di động, tích hợp thông báo đẩy, triển khai chatbot AI, hỗ trợ đa ngôn ngữ, tối ưu hóa SEO, tạo báo cáo và củng cố môi trường DevOps. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 02:56:51 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc phát triển giao diện di động, tích hợp thông báo đẩy, triển khai chatbot AI, hỗ trợ đa ngôn ngữ, tối ưu hóa SEO, tạo báo cáo và củng cố môi trường DevOps, bao gồm:
- Phát triển giao diện di động với điều hướng vai trò
- Tích hợp thông báo đẩy qua FCM/APNs
- Triển khai chatbot AI để trả lời các truy vấn phổ biến
- Hỗ trợ đa ngôn ngữ cho giao diện người dùng
- Tối ưu hóa SEO cho các trang web và ứng dụng di động
- Tạo báo cáo điểm danh và bảng điều khiển tóm tắt
- Củng cố môi trường DevOps với các quy trình kiểm thử và triển khai tự động

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép
- `./sources/frontend/mobile/App.js`
- `./sources/frontend/mobile/components/NotificationService.js`
- `./sources/frontend/mobile/components/Chatbot.js`
- `./sources/frontend/mobile/i18n/locales/en.json`
- `./sources/frontend/mobile/i18n/locales/vi.json`
- `./sources/frontend/mobile/i18n/locales/es.json`
- `./sources/frontend/mobile/utils/seo.js`
- `./sources/frontend/mobile/reports/AttendanceReport.js`
- `./sources/frontend/mobile/reports/Dashboard.js`
- `./sources/docs/reporting-and-seo.md`

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

### 🌤️ Ngày 1: Xây dựng lõi ứng dụng di động

#### 📝 Nhiệm vụ con 1.1: Triển khai lõi ứng dụng di động với điều hướng vai trò

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/App.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Tạo tài liệu kiến trúc cho hệ thống giao diện di động

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/mobile-architecture.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-009]<!--END_TAGS-->

### 🌤️ Ngày 2: Tích hợp thông báo đẩy và chatbot AI

#### 📝 Nhiệm vụ con 2.1: Triển khai dịch vụ thông báo đẩy

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/components/NotificationService.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008], [REQ-021], [NFR-006]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.2: Triển khai chatbot AI

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/components/Chatbot.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 2.3: Tạo tài liệu kiến trúc cho hệ thống thông báo và chatbot

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/notification-and-chatbot.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008], [REQ-019], [REQ-021]<!--END_TAGS-->

### 🌤️ Ngày 3: Hỗ trợ đa ngôn ngữ và SEO

#### 📝 Nhiệm vụ con 3.1: Triển khai đa ngôn ngữ cho giao diện người dùng

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/i18n/locales/en.json
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/i18n/locales/vi.json
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/i18n/locales/es.json
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.2: Tối ưu hóa SEO cho ứng dụng di động

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/utils/seo.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-023], [NFR-007]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 3.3: Tạo tài liệu kiến trúc cho hệ thống đa ngôn ngữ và SEO

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/i18n-and-seo.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->

### 🌤️ Ngày 4: Tạo báo cáo và bảng điều khiển

#### 📝 Nhiệm vụ con 4.1: Triển khai báo cáo điểm danh

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/reports/AttendanceReport.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-024], [EXC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.2: Triển khai bảng điều khiển tóm tắt

##### Chuyên gia được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/reports/Dashboard.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-025]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 4.3: Tạo tài liệu kiến trúc cho hệ thống báo cáo và bảng điều khiển

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/reporting-and-dashboard.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-024], [REQ-025], [EXC-005]<!--END_TAGS-->

### 🌤️ Ngày 5: Củng cố môi trường DevOps

#### 📝 Nhiệm vụ con 5.1: Tạo Dockerfile cho ứng dụng di động

##### Chuyên gia được chỉ định: Docker
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/Dockerfile
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.2: Triển khai ứng dụng di động lên Google Cloud Run

##### Chuyên gia được chỉ định: GCP
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gcp/mobile-app-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-010]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 5.3: Tạo tài liệu kiến trúc cho hệ thống DevOps

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/devops-architecture.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-010], [NFR-005]<!--END_TAGS-->

### 🌤️ Ngày 6: Kiểm thử và tối ưu hóa

#### 📝 Nhiệm vụ con 6.1: Kiểm thử tích hợp cho hệ thống giao diện di động

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/frontend/mobile/tests/integration/MobileIntegrationTest.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-009], [ARC-008], [NFR-002], [NFR-005], [NFR-006], [NFR-007], [EXC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 6.2: Kiểm thử hiệu suất cho hệ thống giao diện di động

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/frontend/mobile/tests/performance/MobilePerformanceTest.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[NFR-001]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 6.3: Kiểm tra chất lượng mã và bảo mật

##### Chuyên gia được chỉ định: Reviewer
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/App.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/components/NotificationService.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008], [REQ-021], [NFR-006]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/components/Chatbot.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/i18n/locales/en.json
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/i18n/locales/vi.json
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/i18n/locales/es.json
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/utils/seo.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-023], [NFR-007]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/reports/AttendanceReport.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-024], [EXC-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/reports/Dashboard.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-025]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 6.4: Cập nhật tài liệu kỹ thuật

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/mobile-architecture.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-009]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/docs/notification-and-chatbot.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-008], [REQ-019], [REQ-021]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/docs/i18n-and-seo.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-022], [REQ-023], [NFR-007]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/docs/reporting-and-dashboard.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-024], [REQ-025], [EXC-005]<!--END_TAGS-->

* **Đường dẫn mục tiêu:** ./sources/docs/devops-architecture.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-010], [NFR-005]<!--END_TAGS-->

### 🌤️ Ngày 7: Triển khai và kiểm thử cuối cùng

#### 📝 Nhiệm vụ con 7.1: Triển khai ứng dụng di động lên môi trường sản xuất

##### Chuyên gia được chỉ định: GKE
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra/gke/mobile-app-deployment.yaml
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-009], [ARC-008], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-002], [NFR-005], [NFR-006], [NFR-007], [EXC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.2: Kiểm thử cuối cùng trên môi trường sản xuất

##### Chuyên gia được chỉ định: Tester
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** INTEGRATION_SCOPE;./sources/frontend/mobile/tests/e2e/MobileE2ETest.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-009], [ARC-008], [NFR-002], [NFR-005], [NFR-006], [NFR-007], [EXC-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 7.3: Cập nhật tài liệu triển khai

##### Chuyên gia được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/deployment-guide.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-009], [ARC-008], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-002], [NFR-005], [NFR-006], [NFR-007], [EXC-005]<!--END_TAGS-->