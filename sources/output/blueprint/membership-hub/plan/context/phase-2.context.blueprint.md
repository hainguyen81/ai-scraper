# Giai đoạn 2: <!--PHASE_NAME_START-->notification_promotion_announcement_chatbot_reporting_localization<!--PHASE_NAME_END--> | Mô tả: Triển khai các dịch vụ thông báo đa kênh, quản lý khuyến mãi, thông báo hệ thống, chatbot AI, báo cáo, và bản địa hóa ngôn ngữ cho hệ thống membership-hub, bao gồm schema cơ sở dữ liệu, hợp đồng API, xử lý ngoại lệ, và tuân thủ các tiêu chuẩn bảo mật doanh nghiệp.
## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260803050419 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên Kỹ Thuật Giai Đoạn** | <!--PHASE_NAME_START-->notification_promotion_announcement_chatbot_reporting_localization<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai các dịch vụ thông báo đa kênh, quản lý khuyến mãi, thông báo hệ thống, chatbot AI, báo cáo, và bản địa hóa ngôn ngữ cho hệ thống membership-hub, bao gồm schema cơ sở dữ liệu, hợp đồng API, xử lý ngoại lệ, và tuân thủ các tiêu chuẩn bảo mật doanh nghiệp. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày.Giờ** | 2026/08/03 05:04:19 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 1. Phạm vi Hoạt động & Mục tiêu Giai đoạn
Giai đoạn này tập trung vào việc triển khai toàn diện các dịch vụ phi lõi cho membership‑hub, bao gồm:

* **Service Thông báo** – tạo, gửi push notification qua FCM/APNs, ghi log vào bảng `notifications`, hỗ trợ retry logic cho trường hợp device token không hợp lệ.
* **Service Khuyến mãi** – quản lý mã giảm giá với validation về tính duy nhất, phạm vi ngày tháng, và kiểm soát discountPercent (0‑100 %).
* **Service Thông báo** – quản lý thông báo hệ thống với startDate/endDate tùy chọn, tự động hiển thị/ẩn dựa trên ngày.
* **Service Chatbot** – tích hợp Spring AI để trả lời truy vấn người dùng về khóa học, giáo viên, trung tâm, hỗ trợ cả trường hợp không tự tin (escalation).
* **Service Báo cáo** – endpoint `/reports/attendance` trả về CSV với các trường: StudentName, CourseName, AttendanceDate, Status; hỗ trợ filtering theo centerId và khoảng ngày.
* **Service Bản địa hóa** – cung cấp endpoint `/api/v1/i18n/{lang}` trả về các chuỗi UI cho các locale được hỗ trợ (VI, EN, ES).

Tất cả các thành phần này tuân thủ nghiêm ngặt các quy định bảo mật OWASP Top 10 (A01‑Broken Access Control, A03‑Injection, A07‑Identification & Authentication Failures) và các yêu cầu bảo mật doanh nghiệp (NFR‑001 → NFR‑009). Các schema cơ sở dữ liệu được định nghĩa bởi `[DAT-008]`, `[DAT-009]`, `[DAT-011]`; hợp đồng API bởi `[REQ-016]`‑`[REQ-025]`; xử lý ngoại lệ bởi `[EXC-003]`; và các chỉ số hiệu năng/tính sẵn sàng bởi `[NFR-001]`, `[NFR-002]`, `[NFR-003]`, `[NFR-004]`, `[NFR-005]`, `[NFR-007]`, `[NFR-008]`.

## 2. Phạm vi Kỹ thuật & Ranh giới Thư mục
Tất cả các thành phần được triển khai dưới đây đều tuân thủ quy tắc bắt đầu bằng `./sources/`:

| Component | Đường dẫn Vật lý | Endpoint REST Chính |
|-----------|--------------|-------------------|
| **Notification** | `./sources/backend.notification` | `POST /api/v1/notifications` |
| **Promotion** | `./sources/backend.promotion` | `POST /api/v1/promotions` |
| **Announcement** | `./sources/backend.announcement` | `POST /api/v1/announcements` |
| **Chatbot** | `./sources/backend.chatbot` | `POST /api/v1/chatbot/query` |
| **Reporting** | `./sources/backend.reporting` | `GET /api/v1/reports/attendance` |
| **Localization** | `./sources/backend.localization` | `GET /api/v1/i18n/{lang}` |
| **Infrastructure** | `./sources/infra` | — (Pub/Sub, Secret Manager, Helm charts) |

Tất cả các file Java phải nằm trong gói `org.nlh4j.saas.membershiphub` (đã được chuẩn hóa thành tên token lowercase `membershiphub`).

## 3. Chỉ thị Chức năng dành cho Đại diện Sub‑Agent
* **Tester** – Viết và thực thi các bài kiểm tra tích hợp bao phủ toàn bộ các endpoint của Notification, Promotion, Announcement, Chatbot, Reporting, và Localization. Đảm bảo retry logic cho notification failures, validation cho promotion code uniqueness, auto‑hide logic cho announcement, và các trường hợp fallback cho chatbot. Tuân thủ OWASP A03 (Injection) bằng cách sử dụng parameterized queries trong test data.
* **Reviewer** – Thực hiện phân tích tĩnh mã nguồn cho Promotion và Announcement services. Kiểm tra các lỗ hổng SQL injection, XSS trong description fields, và tuân thủ các quy tắc RBAC. Đề xuất các index cho Promotion code và Announcement date ranges. Đảm bảo tuân thủ NFR‑001 (Performance) và NFR‑003 (Security).
* **Doc** – Soạn thảo OpenAPI 3.0 spec cho tất cả các API thuộc Phase 2. Bao gồm request/response schemas, error responses, và ví dụ sử dụng. Ghi chú quy tắc tự động hiển thị thông báo dựa trên startDate/endDate. Đính kèm các tag IDs tương ứng trong mỗi phần tài liệu.
* **Docker** – Tạo multi‑stage Dockerfile cho Chatbot service (Java 21 + Spring AI). Tối ưu hóa kích thước image (< 200 MB), thêm healthcheck `/ready`, và push image với tag `chatbot:v1`. Đảm bảo image được ký với Cosign để tuân thủ NFR‑005 (Docker Image Size).
* **GCP** – Provision Pub/Sub topic `notifications`, Cloud Scheduler jobs để kích hoạt gửi thông báo định kỳ, và lưu trữ khóa Zalo API trong Secret Manager. Cấu hình IAM cho service account `event.receiver` với role `roles/pubsub.publisher`. Đảm bảo tuân thủ NFR‑003 (Security) và NFR‑004 (Scalability).
* **GKE** – Triển khai Helm chart cho Reporting service. Cấu hình Deployment với resource limits (CPU 250m, Memory 512Mi), HPA dựa trên latency, và NetworkPolicy hạn chế giao tiếp dịch vụ. Thêm readiness/liveness probes. Đảm bảo tuân thủ NFR‑002 (Availability) và NFR‑004 (Scalability).

## 4. Định nghĩa Mục tiêu Hoàn thành Giai đoạn (DoD)
* **Functional Completion** – Tất cả sáu service (Notification, Promotion, Announcement, Chatbot, Reporting, Localization) được triển khai với đầy đủ các endpoint REST như được định nghĩa trong hợp đồng API `[REQ-016]`‑`[REQ-025]`.
* **Data Schema** – Các bảng `notifications` (`[DAT-008]`), `promotions` & `announcements` (`[DAT-009]`), và `system_settings` (`[DAT-011]`) được tạo trong PostgreSQL với các index được đề xuất.
* **Exception Handling** – Ngoại lệ `[EXC-003]` (Failed Notification Delivery) được xử lý: ghi log, lên lịch retry tối đa 3 lần, đánh dấu `delivered = false`, và tạo sự kiện `NotificationFailed`.
* **Security & OWASP** – 100 % tuân thủ OWASP Top 10: sử dụng prepared statements, validation/sanitization đầu vào, CSP headers, và kiểm tra xác thực JWT cho mọi endpoint. Đã hoàn thành quét OWASP ZAP, không có lỗ hổng nghiêm trọng.
* **NFR Compliance** – Đáp ứng các chỉ số NFR‑001 (phản hồi API < 200 ms), NFR‑002 (99.9 % uptime), NFR‑003 (TLS 1.3, mã hóa AES‑256), NFR‑004 (HPA, read replicas), NFR‑005 (image size < 200 MB), NFR‑007 (multi‑language support), NFR‑008 (GDPR/CCPA data controls).
* **Test Coverage** – Unit + integration tests đạt ≥ 95 % coverage cho backend.notification, backend.promotion, backend.announcement, backend.chatbot, backend.reporting, backend.localization. Tất cả các trường hợp biên và lỗi được bao phủ.
* **Documentation** – OpenAPI spec hoàn chỉnh cho tất cả các service Phase 2, bao gồm request/response schemas, error codes, và ví dụ sử dụng. Tài liệu được lưu trữ trong `./sources/backend.*/docs/`.
* **Container & Registry** – Docker image cho Chatbot được build, scan, ký, và push với tag `chatbot:v1`. Tất cả các image tuân thủ quy tắc size < 500 MB.
* **Cloud Infrastructure** – Tài nguyên GCP (Pub/Sub, Secret Manager, IAM, Cloud Scheduler) được provision và có thể kiểm tra. Service account `event.receiver` có các quyền cần thiết.
* **Kubernetes** – Reporting service được triển khai trên GKE với Helm, có HPA, NetworkPolicy, và probes. Đã tích hợp CI/CD để tự động deploy khi có commit mới vào branch `main`.
* **Tag ID Mapping** – 100 % các tag IDs mục tiêu (`[REQ-016]`‑`[REQ-025]`, `[EXC-003]`, `[DAT-008]`, `[DAT-009]`, `[DAT-011]`, `[NFR-001]`, `[NFR-002]`, `[NFR-003]`, `[NFR-004]`, `[NFR-005]`, `[NFR-007]`, `[NFR-008]`) được mapping chính xác trong tất cả các tài liệu, code, và nhật ký.

## 5. Nhật ký Thực hiện theo Ngày

### DAY 1: Triển khai và kiểm thử các dịch vụ thông báo, khuyến mãi, thông báo, chatbot, báo cáo, và bản địa hóa

#### SUB-TASK 1.1: Triển khai endpoint tạo notification với push FCM/APNs và logic retry cho device token không hợp lệ
##### Đại diện được chỉ định: Tester
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.notification;./sources/backend.notification[TestNotificationSuite]
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016], [EXC-003], [DAT-008], [NFR-001], [NFR-003]<!--END_TAGS-->

#### SUB-TASK 1.2: Đánh giá logic validation cho promotion code (tính duy nhất, phạm vi ngày tháng, discountPercent) và kiểm tra bảo mật
##### Đại diện được chỉ định: Reviewer
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.promotion
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-017], [DAT-009], [NFR-001]<!--END_TAGS-->

#### SUB-TASK 1.3: Soạn thảo OpenAPI spec cho Announcement API, bao gồm schema startDate/endDate tùy chọn và quy tắc tự động hiển thị
##### Đại diện được chỉ định: Doc
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.announcement
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-018], [DAT-009], [NFR-001]<!--END_TAGS-->

#### SUB-TASK 1.4: Tạo multi‑stage Dockerfile cho Chatbot service (Java 21 + Spring AI), tối ưu hóa kích thước image và thêm healthcheck
##### Đại diện được chỉ định: Docker
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.chatbot
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-019], [NFR-005], [NFR-001]<!--END_TAGS-->

#### SUB-TASK 1.5: Cấu hình Pub/Sub topic `notifications`, Cloud Scheduler jobs, và Secret Manager cho khóa Zalo API trên GCP
##### Đại diện được chỉ định: GCP
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-008], [NFR-003], [NFR-004]<!--END_TAGS-->

#### SUB-TASK 1.6: Triển khai Reporting service lên GKE với resource limits, HPA dựa trên latency, và NetworkPolicy
##### Đại diện được chỉ định: GKE
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.reporting
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-024], [REQ-025], [DAT-011], [NFR-002], [NFR-004]<!--END_TAGS-->