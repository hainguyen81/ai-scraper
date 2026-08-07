# Giai đoạn 5: Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260807060838 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 06:08:38 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý Kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 5 tập trung vào việc phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps. Giai đoạn này bao gồm việc xây dựng lõi ứng dụng di động, tạo tài liệu báo cáo và SEO.

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép (Các tệp, đường dẫn và điểm cuối)
- `./sources/frontend/mobile/App.js`
- `./sources/docs/reporting-and-seo.md`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm xây dựng mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu cơ sở hạ tầng.
* **Tester**: Hoạt động như một Nhà kiểm thử Chất lượng Chuyên nghiệp. Chuyên về kỹ thuật kiểm thử, xác nhận và cổng kiểm soát chất lượng. Trách nhiệm tạo bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà viết tài liệu Kỹ thuật Chuyên nghiệp và Kiến trúc sư Hệ thống Doanh nghiệp. Chuyên về biên soạn tài liệu Quy cách Kỹ thuật toàn diện, tài liệu tham khảo lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp bậc thang dự án hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp rõ ràng kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác minh biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chướng ngại vật cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất trong Google Kubernetes Engine. Trách nhiệm xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai khối lượng công việc dịch vụ vi mô vào cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Triển khai hoàn chỉnh lõi ứng dụng di động.
- Tạo hoàn chỉnh tài liệu báo cáo và SEO.
- Đảm bảo tuân thủ OWASP và hoàn thành kiểm thử chức năng cho các yêu cầu đã phân bổ.
- Đảm bảo ánh xạ 100% ID Tag.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: Xây dựng lõi ứng dụng di động

#### 📝 Nhiệm vụ con 1.1: Triển khai lõi ứng dụng di động hybrid với điều hướng vai trò, tích hợp Firebase Auth và xử lý push notification

##### Chuyên viên được chỉ định: Coder
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/frontend/mobile/App.js
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]<!--END_TAGS-->

#### 📝 Nhiệm vụ con 1.2: Tạo tài liệu kỹ thuật cho giai đoạn 5

##### Chuyên viên được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/phase5-documentation.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]<!--END_TAGS-->

### 🌤️ Ngày 2: Tạo tài liệu báo cáo và SEO

#### 📝 Nhiệm vụ con 2.1: Tạo tài liệu báo cáo và SEO, bao gồm hướng dẫn tạo báo cáo điểm danh CSV, chèn meta tags đa ngôn ngữ và hreflang, thực hiện tuân thủ GDPR/CCPA và sao lưu PostgreSQL

##### Chuyên viên được chỉ định: Doc
##### Thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/reporting-and-seo.md
* **Mã thông báo theo dõi:** <!--START_TAGS-->[ARC-010], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->