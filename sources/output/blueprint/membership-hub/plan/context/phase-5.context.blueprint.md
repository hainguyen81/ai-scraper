# Giai đoạn 5: <!--PHASE_NAME_START-->Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến Trúc** | ARCH-20260807042343 |
| **Tên Dự Án** | membership-hub |
| **Giai Đoạn** | 5 |
| **Tên Giai Đoạn** | Phát triển giao diện di động, thông báo đẩy, chatbot AI, i18n, SEO, báo cáo và hardening DevOps |
| **Mô Tả** | <!--PHASE_DESC_START-->Giai đoạn 5 tập trung vào việc xây dựng giao diện di động đa nền tảng, tích hợp thông báo đẩy qua Firebase Cloud Messaging và Apple Push Notification Service, triển khai chatbot AI hỗ trợ trả lời câu hỏi của người dùng, hỗ trợ đa ngôn ngữ và SEO, tạo tài liệu báo cáo và hardening DevOps cho toàn bộ hệ thống. Phần công việc bao gồm phát triển ứng dụng di động hybrid, tạo tài liệu kỹ thuật, cấu hình CI/CD, bảo mật, và tuân thủ các yêu cầu NFR liên quan đến hiệu năng, bảo mật, và độ sẵn sàng.<!--PHASE_DESC_END--> |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày/Thời Gian** | 2026/08/07 04:23:43 |
| **Tác Giả** | Enterprise System Architect (SA Agent) |
| **Phê Duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu giai đoạn
Giai đoạn 5 thực hiện toàn bộ chức năng phát triển giao diện di động, tích hợp thông báo đẩy, chatbot AI, hỗ trợ đa ngôn ngữ và SEO, tạo tài liệu báo cáo, và hardening DevOps. Các thành phần chính bao gồm:
- Ứng dụng di động hybrid (React Native + Capacitor) với Firebase Auth, FCM/APNs, và Zalo API.
- Chatbot AI sử dụng mô hình ngôn ngữ tự nhiên (OpenAI GPT-4 hoặc tương đương) để trả lời câu hỏi về khóa học, giáo viên, trung tâm, và tài khoản.
- Hỗ trợ i18n với các ngôn ngữ tiếng Việt, tiếng Anh, và tiếng Tây Ban Nha, đồng thời chèn thẻ `<meta>` và `hreflang` cho SEO.
- Tài liệu báo cáo và hardening DevOps bao gồm quy trình CI/CD, Dockerfile, Helm chart, và cấu hình GKE.

## 2. Phạm vi kỹ thuật & ranh giới thư mục (Files, paths, và endpoints)
- **Thư mục**:
  - `./sources/frontend/mobile/` – mã nguồn ứng dụng di động.
  - `./sources/docs/` – tài liệu kỹ thuật, báo cáo, và hướng dẫn triển khai.
- **Endpoint**:
  - `GET /api/v1/mobile/user/{userId}/profile`
  - `POST /api/v1/mobile/tokens`
  - `POST /api/v1/chatbot/query`
  - `GET /api/v1/reports/attendance?centerId=...&date=...`

## 3. Hướng dẫn chức năng của các Sub-Agent
- **Coder**: Phát triển mã nguồn ứng dụng di động và tài liệu kỹ thuật. Không viết test, manifest, hoặc cấu hình CI/CD.
- **Tester**: Thiết kế và thực thi bộ kiểm thử JUnit, integration test, và E2E automation. Không sửa mã nguồn.
- **Doc**: Soạn tài liệu kỹ thuật, sơ đồ kiến trúc, mô hình dữ liệu, và quy trình triển khai. Đảm bảo tài liệu nằm trong `./sources/docs/`.
- **Reviewer**: Kiểm tra mã, phân tích tĩnh, vá lỗi bảo mật OWASP, và đảm bảo chất lượng code.
- **Docker**: Xây dựng Dockerfile đa stage, tối ưu kích thước, và đẩy image lên DockerHub.
- **GCP**: Tự động hóa triển khai trên Google Cloud, đẩy image lên Artifact Registry, và triển khai trên Cloud Run.
- **GKE**: Xây dựng manifest Kubernetes, HPA, Helm chart, và triển khai microservices trên GKE.

## 4. Định nghĩa DoD (Definition of Done)
- Tất cả các yêu cầu [REQ-019] tới [REQ-025] được triển khai và kiểm thử thành công.
- Đạt 100% coverage cho unit, integration, và E2E tests.
- Đạt OWASP Top 10 compliance, bảo mật OWASP, và NFR-002, NFR-005, NFR-007, NFR-008, NFR-009.
- Mỗi tag ID được map đầy đủ, không còn tag chưa được sử dụng.
- Tài liệu kỹ thuật, sơ đồ kiến trúc, và báo cáo hoàn chỉnh, lưu trữ trong `./sources/docs/`.

## 5. LỊCH THỰC HIỆN NGÀY ĐÓNG

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->XÂY DỰNG LÓI ỨNG DỤNG DI ĐỘNG<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 1.1: Triển khai lõi ứng dụng di động hybrid với điều hướng vai trò, tích hợp Firebase Auth và xử lý push notification
##### Được giao: Coder
##### Định hướng thành phần & yêu cầu kỹ thuật:
* **Đường dẫn**: ./sources/frontend/mobile/App.js
* **Thẻ theo dõi**: <!--START_TAGS-->[ARC-009], [REQ-019], [REQ-020], [NFR-002], [NFR-005]<!--END_TAGS-->

#### 📝 NHIỆM VỤ 1.2: Khởi tạo tài liệu kiến trúc hệ thống, bao gồm sơ đồ kiến trúc, mô hình dữ liệu, và quy trình triển khai
##### Được giao: Doc
##### Định hướng thành phần & yêu cầu kỹ thuật:
* **Đường dẫn**: ./sources/docs/phase5-architecture.md
* **Thẻ theo dõi**: <!--START_TAGS-->[ARC-009], [ARC-010], [REQ-019], [REQ-020], [NFR-002], [NFR-005]<!--END_TAGS-->

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->TẠO TÀI LIỆU BÁO CÁO VÀ SEO<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ 2.1: Tạo tài liệu báo cáo và SEO, bao gồm hướng dẫn tạo báo cáo điểm danh CSV, chèn meta tags đa ngôn ngữ và hreflang, thực hiện tuân thủ GDPR/CCPA, sao lưu PostgreSQL, ghi lại quy trình triển khai Docker và GKE
##### Được giao: Doc
##### Định hướng thành phần & yêu cầu kỹ thuật:
* **Đường dẫn**: ./sources/docs/reporting-and-seo.md
* **Thẻ theo dõi**: <!--START_TAGS-->[ARC-010], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [NFR-007], [NFR-008], [NFR-009]<!--END_TAGS-->