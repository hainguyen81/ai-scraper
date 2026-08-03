# Giai đoạn 5: <!--PHASE_NAME_START-->notification_frontend_integration_and_devops_deployment<!--PHASE_NAME_END--> | Mô tả: Triển khai toàn diện module thông báo, khuyến mãi, thông báo, chatbot AI, UI di động responsive, đa ngôn ngữ, SEO, và thiết lập hạ tầng DevOps hoàn chỉnh với Docker, GCP và GKE

## 📊 Kiểm soát tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260803053505 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên kỹ thuật giai đoạn** | <!--PHASE_NAME_START-->notification_frontend_integration_and_devops_deployment<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai toàn diện module thông báo, khuyến mãi, thông báo, chatbot AI, UI di động responsive, đa ngôn ngữ, SEO, và thiết lập hạ tầng DevOps hoàn chỉnh với Docker, GCP và GKE |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/03 05:35:05 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu giai đoạn

Giai đoạn này tập trung vào việc hoàn thiện hệ thống với các chức năng nâng cao và triển khai hạ tầng production:

- Triển khai schema cơ sở dữ liệu cho bảng Notifications, Promotions, Announcements và SystemSettings
- Xây dựng dịch vụ thông báo đa kênh (push notification, Zalo integration) với retry mechanism
- Triển khai API quản lý khuyến mãi và thông báo với validation nghiêm ngặt
- Tích hợp chatbot AI với OpenAI/Gemini API cho dịch vụ khách hàng tự động
- Phát triển frontend Next.js với responsive design, đa ngôn ngữ và SEO optimization
- Thiết lập cơ sở hạ tầng GCP hoàn chỉnh với VPC, IAM, Cloud SQL và Secret Manager
- Xây dựng Docker multi-stage images cho backend và frontend
- Triển khai lên Google Kubernetes Engine với HPA, canary deployment và monitoring stack

## 2. Phạm vi kỹ thuật và ranh giới thư mục được phép

**Thư mục và tệp được phép:**
- `./sources/backend.membershiphub.notification/notifications.sql` - DDL schema cho bảng Notifications
- `./sources/backend.membershiphub.notification/promotions.sql` - DDL schema cho bảng Promotions
- `./sources/backend.membershiphub.notification/announcements.sql` - DDL schema cho bảng Announcements
- `./sources/backend.membershiphub.notification/systemsettings.sql` - DDL schema cho bảng SystemSettings
- `./sources/backend.membershiphub.notification/notification-service.java` - Dịch vụ chính quản lý thông báo
- `./sources/backend.membershiphub.notification/chatbot-service.java` - Dịch vụ chatbot AI
- `./sources/frontend.nextjs/package.json` - Cấu hình frontend Next.js
- `./sources/infra/gcp/infrastructure.tf` - Cấu hình Terraform cho GCP
- `./sources/infra/docker/backend/Dockerfile` - Dockerfile cho backend
- `./sources/infra/gke/deployments.yaml` - Kubernetes deployments cho GKE

**Endpoint API:**
- `POST /api/v1/notifications` - Tạo và gửi thông báo đa kênh
- `GET /api/v1/promotions` - Lấy danh sách khuyến mãi hiệu lực
- `POST /api/v1/promotions` - Tạo khuyến mãi mới
- `PUT /api/v1/promotions/{promoId}` - Cập nhật khuyến mãi
- `DELETE /api/v1/promotions/{promoId}` - Xóa khuyến mãi
- `POST /api/v1/announcements` - Tạo thông báo mới
- `GET /api/v1/announcements` - Lấy danh sách thông báo hiệu lực
- `POST /api/v1/chatbot/interact` - Tương tác với chatbot AI
- `GET /api/v1/i18n/{locale}` - Lấy bản dịch theo locale
- `GET /api/v1/seo/{locale}/{path}` - Lấy meta tags SEO

## 3. Chỉ đạo chức năng cho Sub-Agent chuyên dụng

**Coder:** Triển khai mã nguồn Java/Quarkus cho các dịch vụ thông báo và chatbot, sử dụng @Transactional, tích hợp FCM, APNs và Zalo API. Phát triển frontend Next.js với TypeScript, Tailwind CSS, react-i18next và SEO optimization.

**Tester:** Xây dựng bộ kiểm thử JUnit 5 và Testcontainers cho các dịch vụ thông báo, kiểm thử integration với FCM và Zalo API mock, đảm bảo độ phủ mã ≥85%.

**Docker:** Tạo multi-stage Dockerfile cho backend và frontend, đảm bảo kích thước image cuối cùng <500MB, thiết lập healthcheck và non-root user.

**GCP:** Triển khai Terraform configuration cho GCP infrastructure bao gồm VPC, IAM, Cloud SQL, Secret Manager và Cloud Scheduler.

**GKE:** Tạo Kubernetes manifests cho deployment, service, ingress, HPA và monitoring stack, triển khai canary deployment với health checks.

## 4. Định nghĩa hoàn thành (DoD) cho giai đoạn

- ✅ 100% các requirement [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023] được triển khai đầy đủ
- ✅ Schema database [DAT-008], [DAT-009], [DAT-011] được tạo thành công với tất cả ràng buộc
- ✅ Tích hợp thành công FCM, APNs và Zalo API cho thông báo đa kênh
- ✅ Frontend Next.js responsive với đa ngôn ngữ và SEO optimization
- ✅ Infrastructure as Code hoàn chỉnh cho GCP và GKE
- ✅ Docker images optimized với kích thước <500MB
- ✅ Tuân thủ các tiêu chuẩn bảo mật [NFR-003], [NFR-006], [NFR-007]
- ✅ Độ phủ kiểm thử ≥85% cho tất cả các dịch vụ mới
- ✅ 100% các Tag ID được ánh xạ và kiểm tra

## 5. NHẬT KÝ THỰC THI KIẾN TRÚC THEO NGÀY

### NGÀY 10: TRIỂN KHAI SERVICE THÔNG BÁO, KHUYẾN MÃI, THÔNG BÁO

#### SUB-TASK 10.1: Triển khai schema cơ sở dữ liệu Notifications, Promotions, Announcements và SystemSettings
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.notification/notifications.sql`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[DAT-008]<!--END_TAGS-->

#### SUB-TASK 10.2: Triển khai NotificationService với các phương thức thông báo đa kênh và retry mechanism
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.notification/notification-service.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [DAT-008], [DAT-009], [NFR-003], [NFR-006]<!--END_TAGS-->

### NGÀY 11: TRIỂN KHAI TÍCH HỢP CHATBOT AI, UI DI ĐỘNG VÀ CẤU HÌNH ĐA NGÔN NGỮ/SEO

#### SUB-TASK 11.1: Triển khai ChatbotService với tích hợp OpenAI/Gemini API và xử lý tương tác
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend.membershiphub.notification/chatbot-service.java`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011], [NFR-007]<!--END_TAGS-->

#### SUB-TASK 11.2: Triển khai frontend Next.js với responsive design, i18n và SEO optimization
##### Sub-Agent được chỉ định: Coder
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/frontend.nextjs/package.json`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[REQ-020], [REQ-021], [REQ-022], [REQ-023]<!--END_TAGS-->

### NGÀY 12: CUNG CẤP CẤU HÌNH HẠ TẦNG GCP (VPC, IAM, CLOUD STORAGE, CLOUD RUN)

#### SUB-TASK 12.1: Triển khai Terraform configuration cho GCP infrastructure với VPC, IAM và Cloud SQL
##### Sub-Agent được chỉ định: GCP
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gcp/infrastructure.tf`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[NFR-004], [NFR-008]<!--END_TAGS-->

### NGÀY 13: XÂY DỰNG DOCKER IMAGE ĐA GIAI ĐOẠN CHO BACKEND VÀ FRONTEND

#### SUB-TASK 13.1: Tạo multi-stage Dockerfile cho backend Quarkus với optimization kích thước
##### Sub-Agent được chỉ định: Docker
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/docker/backend/Dockerfile`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[NFR-005], [NFR-009]<!--END_TAGS-->

### NGÀY 14: TRIỂN KHAI LÊN GOOGLE KUBERNETES ENGINE (GKE) VỚI HPA VÀ QUẢN LÝ RELEASE

#### SUB-TASK 14.1: Tạo Kubernetes manifests cho deployment, service, ingress và HPA
##### Sub-Agent được chỉ định: GKE
##### Các thành phần mục tiêu và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gke/deployments.yaml`
* **Các thẻ truy xuất nguồn gốc:** <!--START_TAGS-->[NFR-002], [NFR-004], [NFR-009]<!--END_TAGS-->