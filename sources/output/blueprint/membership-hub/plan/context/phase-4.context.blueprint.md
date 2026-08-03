# Giai đoạn 4: <!--PHASE_NAME_START-->phase4_notification_and_security<!--PHASE_NAME_END--> | Mô tả: Triển khai hạ tầng Docker đa giai đoạn, cấu hình tài nguyên GCP (VPC, IAM, Cloud Storage), triển khai dịch vụ thông báo push, và ghi chép quy tắc bảo mật, đồng thời thực hiện kiểm tra OWASP và NFR.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260803132420 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên Giai đoạn Kỹ thuật** | <!--PHASE_NAME_START-->phase4_notification_and_security<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai hạ tầng Docker đa giai đoạn, cấu hình tài nguyên GCP (VPC, IAM, Cloud Storage), triển khai dịch vụ thông báo push, và ghi chép quy tắc bảo mật, đồng thời thực hiện kiểm tra OWASP và NFR. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/03 13:24:20 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
Giai đoạn 4 tập trung vào việc hoàn thiện hạ tầng triển khai và bảo mật cho hệ thống membership‑hub. Các mục tiêu chính bao gồm:
- Cập nhật Dockerfile đa giai đoạn để giảm kích thước ảnh, tối ưu thời gian build và tuân thủ NFR‑005 (độ lớn ảnh < 500 MB).
- Cấu hình tài nguyên GCP (VPC, IAM, Cloud Storage, Secret Manager, Cloud SQL, Redis) theo mô hình IaC, đáp ứng NFR‑009 (đảm bảo sao lưu và khôi phục).
- Triển khai dịch vụ thông báo push (NotificationService) với logic retry, ghi nhận trạng thái delivered, và xử lý ngoại lệ EXC‑003.
- Soạn tài liệu bảo mật (docs.security) ghi nhận các quy tắc RBAC, OWASP Top 10, và các biện pháp bảo vệ dữ liệu.
- Đảm bảo toàn bộ các yêu cầu NFR, REQ, DAT, EXC được kiểm tra, ghi nhận và liên kết đầy đủ.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/infra.dockerfile` | Dockerfile đa giai đoạn cho toàn bộ backend |
| `./sources/infra.gcp` | Terraform/IaC scripts tạo VPC, IAM, Cloud Storage, Secret Manager, Cloud SQL, Redis |
| `./sources/backend.notifications` | Dịch vụ NotificationResource (REST API) |
| `./sources/docs.security` | Tài liệu bảo mật, quy tắc OWASP, RBAC, audit log |

REST endpoint cho NotificationService:
```
POST /api/v1/notifications
```
- Body: `{ "userId": "<UUID>", "groupZalo": "<string>", "message": "<string>" }`
- Response: `{ "notificationId": "<UUID>", "sentAt": "<timestamp>", "delivered": false }`

## 3. Dedicated Sub-Agent Functional Directives
| Agent | Trách nhiệm |
| :--- | :--- |
| **Docker** | Cập nhật Dockerfile, kiểm tra kích thước ảnh, thực thi build, push lên registry. |
| **GCP** | Triển khai IaC, cấu hình IAM, VPC, Cloud Storage, Secret Manager, Cloud SQL, Redis. |
| **Coder** | Phát triển NotificationResource, triển khai logic retry, ghi nhận trạng thái delivered, xử lý EXC‑003. |
| **Doc** | Soạn tài liệu bảo mật, ghi nhận quy tắc OWASP, RBAC, audit log, liên kết tag. |
| **Tester** | Kiểm tra unit, integration, và end‑to‑end cho NotificationService, Docker build, IaC deployment. |
| **Reviewer** | Phân tích tĩnh mã, kiểm tra OWASP, bảo mật, và tuân thủ NFR. |

## 4. Phase Definition of Done (DoD)
- **Tất cả REQ, DAT, EXC, NFR** trong Phase 4 được triển khai, kiểm tra và ghi nhận đầy đủ.
- **Docker image** < 500 MB, build thành công, push lên registry.
- **IaC deployment** thành công, tài nguyên GCP khởi tạo đúng cấu hình, backup được cấu hình.
- **NotificationService** trả về `delivered=true` sau retry tối đa 3 lần, ghi nhận log chi tiết.
- **Tài liệu bảo mật** hoàn chỉnh, liên kết tất cả tag, kiểm tra OWASP Top 10, audit log tuân thủ NFR‑006.
- **Coverage**: Unit test ≥ 85 %, integration test ≥ 80 %, end‑to‑end ≥ 70 %.
- **CI/CD**: GitHub Actions chạy thành công, build, test, push, deploy.
- **Tag mapping**: Mỗi tag trong Phase 4 xuất hiện ít nhất một lần trong logs.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: CẬP NHẬT DOCKERFILE ĐA GIAI ĐỘNG

#### SUB-TASK 1.1: Cập nhật Dockerfile đa giai đoạn
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path**: `./sources/infra.dockerfile`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-016], [NFR-006]<!--END_TAGS-->
* **OWASP Compliance**: Sử dụng multi‑stage build, loại bỏ layer không cần thiết, chỉ giữ runtime dependencies, bảo vệ image khỏi injection.

### DAY 2: CẤU HÌNH TÀI NGUYÊN GCP

#### SUB-TASK 2.1: Cấu hình VPC, IAM, Cloud Storage
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path**: `./sources/infra.gcp`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-017], [REQ-018], [NFR-009]<!--END_TAGS-->
* **OWASP Compliance**: IAM roles được phân quyền tối thiểu, VPC firewall rules, encryption at rest, secret management.

### DAY 3: TRIỂN KHAI DỊCH VỤ THÔNG BÁO PUSH

#### SUB-TASK 3.1: Triển khai NotificationResource
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path**: `./sources/backend.notifications`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->
* **OWASP Compliance**: Prepared statements, input validation, retry logic, audit logging, token sanitization.

### DAY 4: GHI CHÉP QUY TẮC BẢO MẬT VÀ KIỂM TRA OWASP

#### SUB-TASK 4.1: Soạn tài liệu bảo mật
##### Assigned Sub-Agent: Doc
##### Targeted Components & Technical Requirements:
* **Target Path**: `./sources/docs.security`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-017], [REQ-018], [DAT-008], [EXC-003], [NFR-006], [NFR-009]<!--END_TAGS-->
* **OWASP Compliance**: Ghi nhận các biện pháp bảo vệ, audit log, RBAC, encryption, backup, disaster recovery.