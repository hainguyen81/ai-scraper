# Giai đoạn 5: <!--PHASE_NAME_START-->phase5_reporting_dashboard_k8s_frontend<!--PHASE_NAME_END--> | Mô tả: Triển khai giao diện web Next.js, ứng dụng di động Capacitor, dịch vụ báo cáo, manifest Kubernetes GKE, và hoàn thiện pipeline CI/CD, đồng thời ghi chép tài liệu kỹ thuật và tuân thủ OWASP, NFR.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260803132420 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên Giai đoạn Kỹ thuật** | <!--PHASE_NAME_START-->phase5_reporting_dashboard_k8s_frontend<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai giao diện web Next.js, ứng dụng di động Capacitor, dịch vụ báo cáo và dashboard, chuẩn bị manifest Kubernetes cho GKE, và hoàn thiện pipeline CI/CD, đồng thời ghi chép tài liệu kỹ thuật và tuân thủ OWASP, NFR. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/03 13:24:20 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu của Giai đoạn
Trong Giai đoạn 5, đội ngũ sẽ triển khai toàn bộ giao diện người dùng web Next.js và ứng dụng di động Capacitor, đồng thời xây dựng dịch vụ báo cáo và dashboard, chuẩn bị manifest Kubernetes cho GKE, và hoàn thiện pipeline CI/CD. Các thành phần sẽ được xây dựng theo nguyên tắc modular, bảo mật OWASP, tuân thủ NFR, và được kiểm tra đầy đủ qua unit, integration, và end‑to‑end tests. Tài liệu kỹ thuật sẽ được ghi chép chi tiết, bao gồm kiến trúc, quy trình triển khai, và các biện pháp bảo mật.

## 2. Phạm vi Kỹ thuật & Giới hạn Đường dẫn
| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/frontend.web` | Giao diện web Next.js |
| `./sources/frontend.mobile` | Ứng dụng di động Capacitor |
| `./sources/backend.reporting` | Dịch vụ báo cáo và dashboard |
| `./sources/infra.k8s` | Manifest Kubernetes cho GKE |
| `./sources/infra.cicd` | Pipeline CI/CD và cấu hình GitHub Actions |

**REST Endpoints:**
- `GET /api/v1/reports/attendance`
- `GET /api/v1/dashboard/enrollment`
- `GET /api/v1/i18n/{lang}`
- `GET /api/v1/seo/{lang}`
- `POST /api/v1/chatbot/query`

## 3. Hướng dẫn Đặc thù Sub-Agent
- **Coder**: Xây dựng mã nguồn, triển khai tính năng, tuân thủ OWASP, NFR.  
- **GKE**: Xây dựng manifest Kubernetes, triển khai, cấu hình HPA, TLS, Ingress.  
- **Doc**: Soạn tài liệu kỹ thuật, ghi chép quy trình, bảo mật, OWASP.  
- **Tester**: Viết và chạy unit, integration, end‑to‑end tests, báo cáo coverage.  
- **Reviewer**: Phân tích tĩnh mã, kiểm tra OWASP, bảo mật, tuân thủ NFR.

## 4. Định nghĩa Hoàn thành (DoD)
- Tất cả các yêu cầu [REQ-019] đến [REQ-025] được triển khai và kiểm tra.  
- Tất cả các tag được ánh xạ ít nhất một lần trong logs.  
- OWASP Top 10 được kiểm tra và khắc phục.  
- Coverage unit ≥ 85 %, integration ≥ 80 %, end‑to‑end ≥ 70 %.  
- Docker image < 500 MB.  
- Kubernetes deployment thành công, HPA hoạt động.  
- CI/CD pipeline chạy thành công, push image, deploy.  
- Tài liệu kỹ thuật hoàn chỉnh, bao gồm kiến trúc, quy trình, bảo mật.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: TRIỂN KHAI GIAO DIỆN WEB VÀ ỨNG DỤNG DI ĐỘNG

#### SUB-TASK 1.1: Xây dựng giao diện web Next.js
##### Trách nhiệm Sub-Agent: Coder
##### Công cụ mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/frontend.web`
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-019], [REQ-022], [REQ-023], [NFR-001], [NFR-003], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 1.2: Xây dựng ứng dụng di động Capacitor
##### Trách nhiệm Sub-Agent: Coder
##### Công cụ mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/frontend.mobile`
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-020], [REQ-021], [NFR-001], [NFR-003], [NFR-007], [NFR-008]<!--END_TAGS-->

### DAY 2: TRIỂN KHAI DỊCH VỤ BÁO CÁO VÀ MANIFEST KUBERNETES

#### SUB-TASK 2.1: Xây dựng dịch vụ báo cáo và dashboard
##### Trách nhiệm Sub-Agent: Coder
##### Công cụ mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.reporting`
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-024], [REQ-025], [ARC-009], [NFR-001], [NFR-004], [NFR-006]<!--END_TAGS-->

#### SUB-TASK 2.2: Xây dựng manifest Kubernetes cho GKE
##### Trách nhiệm Sub-Agent: GKE
##### Công cụ mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra.k8s`
* **Thẻ Tracability**: <!--START_TAGS-->[ARC-010], [NFR-001], [NFR-002], [NFR-004], [NFR-005]<!--END_TAGS-->

### DAY 3: HOÀN THI CI/CD PIPELINE VÀ TÀI LIỆU KỸ THUẬT

#### SUB-TASK 3.1: Thiết lập pipeline CI/CD và ghi chép tài liệu
##### Trách nhiệm Sub-Agent: Doc
##### Công cụ mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra.cicd`
* **Thẻ Tracability**: <!--START_TAGS-->[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [EXC-005]<!--END_TAGS-->

#### SUB-TASK 3.2: Kiểm tra tích hợp và end‑to‑end
##### Trách nhiệm Sub-Agent: Tester
##### Công cụ mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.reporting;./sources/tests/backend.reporting.test`
* **Thẻ Tracability**: <!--START_TAGS-->[REQ-024], [REQ-025], [ARC-009], [NFR-001], [NFR-004], [NFR-006]<!--END_TAGS-->

#### SUB-TASK 3.3: Phân tích tĩnh mã và bảo mật
##### Trách nhiệm Sub-Agent: Reviewer
##### Công cụ mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.reporting`
* **Thẻ Tracability**: <!--START_TAGS-->[NFR-001], [NFR-003], [NFR-006]<!--END_TAGS-->