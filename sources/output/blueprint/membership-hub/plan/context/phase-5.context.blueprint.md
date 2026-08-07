# Giai đoạn 5: <!--PHASE_NAME_START-->Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807073534 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng giao diện di động, tích hợp thông báo đẩy, chatbot AI, hỗ trợ đa ngôn ngữ, tối ưu SEO, tạo tài liệu báo cáo và thực hiện hardening DevOps cho toàn bộ hệ thống. Các thành phần chính bao gồm ứng dụng di động hybrid (React Native/Capacitor), tài liệu báo cáo và SEO (Markdown), và các cấu hình DevOps (Docker, GCP, GKE).<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 07:35:34 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi thực thi và mục tiêu

Giai đoạn 5 thực hiện toàn bộ các chức năng liên quan đến giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps. Các nhiệm vụ chính bao gồm:

- Xây dựng ứng dụng di động hybrid (React Native + Capacitor) với xác thực Firebase, quản lý token JWT, và cấu hình push notification (FCM/APNs).
- Tích hợp chatbot AI qua endpoint `/api/v1/chatbot/query` để hỗ trợ người dùng trả lời câu hỏi về khóa học, giáo viên, trung tâm, và trạng thái hội viên.
- Cài đặt đa ngôn ngữ (i18n) cho toàn bộ ứng dụng di động và trang web, bao gồm chuyển hướng URL, thẻ `<html lang='...'>`, và sitemap đa ngôn ngữ.
- Tạo tài liệu báo cáo điểm danh, dashboard, và tài liệu SEO (Markdown) cho các trang web.
- Thực hiện hardening DevOps: xây dựng Dockerfile multi‑stage, cấu hình CI/CD trên GitHub Actions, triển khai images lên Google Cloud Artifact Registry, và triển khai microservices lên GKE với HPA, Helm chart, và cấu hình bảo mật (TLS 1.3, RBAC, secrets management).

## 2. Phạm vi kỹ thuật & ranh giới thư mục

| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/frontend/mobile/` | Ứng dụng di động hybrid (React Native + Capacitor). |
| `./sources/docs/` | Tài liệu báo cáo, SEO, và hướng dẫn triển khai. |
| Endpoints | `GET /api/v1/mobile/user/{userId}/profile`<br>`POST /api/v1/mobile/tokens`<br>`POST /api/v1/chatbot/query`<br>`GET /api/v1/reports/attendance?centerId=...&date=...` |

## 3. Định hướng chức năng của các đại lý phụ

- **Coder**: Phát triển mã nguồn ứng dụng di động và tài liệu Markdown. Không viết test hoặc manifest.
- **Tester**: Viết test JUnit, integration, E2E, và kiểm tra hiệu năng. Không sửa code production.
- **Doc**: Soạn thảo tài liệu kỹ thuật, mô hình dữ liệu, luồng API, và tài liệu triển khai. Đảm bảo đầy đủ các tài liệu cho giai đoạn này.
- **Reviewer**: Kiểm tra biên dịch, phân tích tĩnh, và bảo mật OWASP. Sửa lỗi và bảo vệ code.
- **Docker**: Xây dựng Dockerfile multi‑stage, tối ưu image, và push lên DockerHub.
- **GCP**: Đẩy images lên Google Cloud Artifact Registry và triển khai trên Cloud Run.
- **GKE**: Xây dựng manifest Kubernetes, HPA, Helm chart, và triển khai microservices lên GKE.

## 4. Định nghĩa DoD (Definition of Done)

- Tất cả API và endpoint đã triển khai trả về đúng theo contract, lỗi 4xx/5xx được xử lý.
- Tài liệu kỹ thuật, báo cáo, và SEO hoàn chỉnh, được lưu trong `./sources/docs/`.
- Docker images được build, kiểm tra size < 500 MB, và push lên DockerHub.
- CI/CD pipeline trên GitHub Actions chạy thành công, coverage 100 % cho các yêu cầu [REQ-019]–[REQ-025].
- GCP deployment thành công, images được push lên Artifact Registry.
- GKE deployment thành công, HPA hoạt động, và các cấu hình bảo mật (TLS 1.3, RBAC) được kiểm tra.
- OWASP Top‑10 kiểm tra, không có lỗ hổng, và SonarQube quality gate đạt.
- Mã nguồn được review, biên dịch, và không có lỗi runtime.
- Mọi tag ID được map 100 % và xuất hiện trong logs.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### 🌤️ DAY 1: <!--DAY_HEADER_START-->XÂY DỰNG GIAI DI ĐỘNG<!--DAY_HEADER_END-->

#### 📝 Tài liệu Kiến trúc Giai đoạn 5

##### Assigned Sub-Agent: Doc

##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/docs/phase5_architecture.md
* **Traceability Tag Tokens**: <!--START_TAGS-->[ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: Soạn thảo tài liệu chi tiết về kiến trúc toàn cục, mô hình dữ liệu, luồng API, quy trình triển khai, và các biện pháp bảo mật cho giai đoạn này.

#### 📝 Triển khai App.js

##### Assigned Sub-Agent: Coder

##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/mobile/App.js
* **Traceability Tag Tokens**: <!--START_TAGS-->[ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: Triển khai giao diện di động hybrid, tích hợp Firebase Auth, quản lý token JWT, và cấu hình push notification (FCM/APNs).

### 🌤️ DAY 2: <!--DAY_HEADER_START-->XÂY DỰNG TÀI LIỆU BÁO CÁO VÀ SEO<!--DAY_HEADER_END-->

#### 📝 Tài liệu Báo cáo và SEO

##### Assigned Sub-Agent: Coder

##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/docs/reporting-and-seo.md
* **Traceability Tag Tokens**: <!--START_TAGS-->[ARC-010], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: Soạn tài liệu báo cáo điểm danh, dashboard, và tối ưu SEO đa ngôn ngữ cho trang web.