# Giai đoạn 1: <!--PHASE_NAME_START-->coreServicesImplementation<!--PHASE_NAME_END--> | Mô tả: Triển khai các dịch vụ cốt lõi bao gồm xác thực người dùng, quản lý vai trò, quản lý trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, validation đầu vào và xử lý ngoại lệ theo tiêu chuẩn OWASP.
## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260803050419 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên Kỹ Thuật Giai Đoạn** | <!--PHASE_NAME_START-->coreServicesImplementation<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai các dịch vụ cốt lõi bao gồm xác thực người dùng, quản lý vai trò, quản lý trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, validation đầu vào và xử lý ngoại lệ theo tiêu chuẩn OWASP. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày.Giờ** | 2026/08/03 05:04:19 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 1. Phạm vi Hoạt động & Mục tiêu Giai đoạn
Giai đoạn này tập trung vào việc xây dựng các dịch vụ backend cốt lõi cho hệ thống membership‑hub. Các thành phần chính bao gồm:

* **Xác thực & Quản lý Người dùng** – đăng ký người dùng qua email/mật khẩu và OAuth2 (Firebase, Google, Facebook), cấp JWT/refresh token, thực thi RBAC, và ghi log các thay đổi vai trò.
* **Quản lý Trung tâm** – CRUD các trung tâm, ánh xạ người dùng vào vai trò Center Admin, và đảm bảo tính duy nhất của tax_id.
* **Quản lý Khóa học** – định nghĩa khóa học, phân công giáo viên, kiểm tra xung đột lịch dạy, và áp dụng các ràng buộc về sức chứa.
* **Ghi danh Học viên** – cho phép học viên duyệt và đăng ký khóa học, tự động tạo tài khoản học viên nếu cần, và kích hoạt thông báo.
* **Điểm danh & Quét QR** – ghi nhận điểm danh bất biến qua QR, đảm bảo idempotent, và xử lý các trường hợp ngoại lệ về mạng/lỗi trùng lặp.
* **Thẻ Hội viên** – quản lý thẻ hội viên kỹ thuật số với logic ngày hiệu lực, hỗ trợ gia hạn, và hiển thị trạng thái còn lại.
* **Validation & Xử lý Ngoại lệ** – validation đầu vào nghiêm ngặt (email, mật khẩu, định dạng số), exception handlers chuẩn hóa (ví dụ: VALIDATION_FAILED), và tuân thủ OWASP Top 10 (SQLi, XSS, CSRF, injection).

Tất cả các dịch vụ được container hóa, triển khai trên Kubernetes, và tích hợp với các thành phần hạ tầng (Firebase Auth, Redis, Cloud Logging) theo thiết kế microservices.

## 2. Phạm vi Kỹ thuật & Ranh giới Thư mục
* `./sources/backend.auth` – dịch vụ xác thực (đăng ký, OAuth2, vai trò).
* `./sources/backend.user` – quản lý người dùng chung (profile, trạng thái).
* `./sources/backend.center` – quản lý trung tâm (tạo, cập nhật, ánh xạ admin).
* `./sources/backend.course` – quản lý khóa học (tạo, phân công giáo viên, kiểm tra xung đột).
* `./sources/backend.enrollment` – ghi danh học viên (duyệt, đăng ký, thông báo).
* `./sources/backend.attendance` – ghi nhận điểm danh (QR, bất biến, retry).
* `./sources/backend.membership` – thẻ hội viên (hiển thị, gia hạn, logic ngày hiệu lực).
* `./sources/infra` – tài nguyên hạ tầng (Docker, CI/CD, GCP, GKE).

Tất cả các đường dẫn đều tuân thủ quy tắc bắt đầu bằng `./sources/`. Các file Java phải nằm trong gói `org.nlh4j.saas.membershiphub`.

## 3. Chỉ thị Chức năng dành cho Đại diện Sub‑Agent
* **Coder** – triển khai logic nghiệp vụ, validation, bảo mật, và logging theo Clean Code và SOLID.
* **Tester** – viết unit/integration tests (JUnit5, Mockito) bao phủ các trường hợp thành công/lỗi, đảm bảo tuân thủ NFR và OWASP.
* **Reviewer** – đánh giá chất lượng code, kiểm tra các vấn đề về race condition, xung đột khóa duy nhất, và các lỗ hổng bảo mật tiềm ẩn.
* **Doc** – soạn thảo OpenAPI spec cho từng endpoint, bao gồm request/response schemas, error responses, và tham chiếu tag IDs.
* **Docker** – tạo multi‑stage Dockerfile, healthcheck, ký image, và push lên registry với các tag `latest` và `v1.0`.
* **GCP** – provision project, bật Firebase Auth, IAM roles, Secret Manager, Cloud Logging, và Pub/Sub cho thông báo.
* **GKE** – triển khai Helm charts, cấu hình HPA, NetworkPolicy, readiness/liveness probes, và tích hợp CI/CD.

## 4. Định nghĩa Mục tiêu Hoàn thành Giai đoạn (DoD)
* Tất cả các service cốt lõi được triển khai với các endpoint REST đầy đủ chức năng.
* 100 % test coverage cho các component backend.auth (unit + integration).
* Đánh giá code hoàn chỉnh: không có lỗi bảo mật nghiêm trọng, tuân thủ OWASP, và các đề xuất cải tiến được ghi lại.
* Tài liệu OpenAPI hoàn chỉnh cho các endpoint auth, bao gồm tag IDs.
* Docker image được build, scan, push, và có thể triển khai trên GKE.
* Tài nguyên GCP được cấu hình (Firebase Auth, IAM, Secret Manager, Logging) và có thể kiểm tra.
* Kubernetes Deployment sẵn sàng với HPA, NetworkPolicy, và tích hợp CI/CD.
* Tất cả các tag IDs mục tiêu (`[REQ-001]`‑`[REQ-003]`, `[ARC-006]`, `[DAT-001]`, `[EXC-004]`, `[NFR-001]`, `[NFR-003]`, `[NFR-006]`, `[NFR-002]`, `[NFR-004]`) được mapping chính xác.

## 5. Nhật ký Thực hiện theo Ngày

### DAY 1: Triển khai xác thực người dùng và quản lý vai trò cốt lõi

#### SUB-TASK 1.1: Triển khai các endpoint xác thực (register, social OAuth2, role update) với bảo mật nghiêm ngặt theo OWASP
##### Đại diện được chỉ định: Coder
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.auth
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]<!--END_TAGS-->

#### SUB-TASK 1.2: Tạo bộ kiểm tra tích hợp cho các endpoint xác thực, bao gồm các trường hợp thành công/lỗi và retry
##### Đại diện được chỉ định: Tester
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.auth;./sources/backend.auth[TestAuthSuite]
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]<!--END_TAGS-->

#### SUB-TASK 1.3: Đánh giá chất lượng code cho service auth, tập trung vào thiết kế SOLID, xử lý ngoại lệ, và bảo mật (OWASP)
##### Đại diện được chỉ định: Reviewer
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.auth
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]<!--END_TAGS-->

#### SUB-TASK 1.4: Soạn thảo OpenAPI spec cho các endpoint auth, bao gồm request/response schemas, error responses, và tag IDs
##### Đại diện được chỉ định: Doc
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.auth
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]<!--END_TAGS-->

#### SUB-TASK 1.5: Tạo multi‑stage Dockerfile cho Auth service, thiết lập healthcheck, và push image lên registry
##### Đại diện được chỉ định: Docker
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.auth
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006]<!--END_TAGS-->

#### SUB-TASK 1.6: Provision tài nguyên GCP (Firebase Auth, IAM, Secret Manager, Cloud Logging) cho Phase 1
##### Đại diện được chỉ định: GCP
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/infra
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-006], [NFR-003], [NFR-006]<!--END_TAGS-->

#### SUB-TASK 1.7: Triển khai Auth service lên GKE với HPA, Ingress TLS, và tích hợp CI/CD
##### Đại diện được chỉ định: GKE
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** ./sources/backend.auth
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-006], [NFR-002], [NFR-004]<!--END_TAGS-->