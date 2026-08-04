# Giai đoạn 1: <!--PHASE_NAME_START-->thiet_lap_co_so_ha_tang<!--PHASE_NAME_END--> | Mô tả: Thiết lập cơ sở hạ tầng backend và frontend, triển khai cơ sở dữ liệu PostgreSQL, tích hợp Firebase Authentication
## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260804142715 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->thiet_lap_co_so_ha_tang<!--PHASE_NAME_END--> |
| **Mô tả** | Thiết lập cơ sở hạ tầng backend và frontend, triển khai cơ sở dữ liệu PostgreSQL, tích hợp Firebase Authentication |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/04 14:27:15 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn 1 tập trung vào việc thiết lập cơ sở hạ tầng backend và frontend, triển khai cơ sở dữ liệu PostgreSQL và tích hợp Firebase Authentication. Các nhiệm vụ chính bao gồm:
- Thiết lập cấu hình cơ sở dữ liệu PostgreSQL
- Tích hợp Firebase Authentication
- Thiết lập cấu hình Docker và Kubernetes (GKE)
- Viết các script Flyway/Liquibase để tạo các bảng cơ sở dữ liệu
- Triển khai các dịch vụ xác thực qua email/mật khẩu, Firebase, Google, và Facebook OAuth2

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép
- `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/config`
- `./sources/backend/src/main/resources/db/migration`
- `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/auth`
- `./sources/backend/Dockerfile`
- `./sources/infra/gcp`

## 3. Hướng dẫn chức năng dành riêng cho các tác vụ con
- **Coder:** Triển khai cấu hình cơ sở dữ liệu PostgreSQL, tích hợp Firebase Authentication, thiết lập cấu hình Docker và Kubernetes (GKE), viết các script Flyway/Liquibase để tạo các bảng cơ sở dữ liệu, triển khai các dịch vụ xác thực qua email/mật khẩu, Firebase, Google, và Facebook OAuth2.
- **Docker:** Viết Dockerfile cho dịch vụ backend, cấu hình multi-stage build để giảm kích thước image.
- **GCP:** Triển khai cơ sở hạ tầng trên Google Cloud Platform, cấu hình VPC, IAM, và các dịch vụ cần thiết.

## 4. Định nghĩa hoàn thành giai đoạn (DoD)
- Hoàn thành việc thiết lập cơ sở hạ tầng backend và frontend.
- Triển khai cơ sở dữ liệu PostgreSQL thành công.
- Tích hợp Firebase Authentication thành công.
- Đảm bảo 100% tuân thủ các tiêu chuẩn OWASP.
- Hoàn thành các bài kiểm tra chức năng cho các yêu cầu được phân bổ.
- Đảm bảo 100% ánh xạ ID Tag.

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### DAY 1: <!--DAY_HEADER_START-->THIET_LAP_CO_SO_HA_TANG_BACKEND_VA_FRONTEND<!--DAY_HEADER_END-->

#### SUB-TASK 1.1: Thiết lập cơ sở hạ tầng backend và frontend
##### Tác vụ con được giao: Coder
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/config`
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-006], [ARC-010]<!--END_TAGS-->

#### SUB-TASK 1.2: Viết Dockerfile cho dịch vụ backend
##### Tác vụ con được giao: Docker
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/Dockerfile`
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-010]<!--END_TAGS-->

#### SUB-TASK 1.3: Triển khai cơ sở hạ tầng trên Google Cloud Platform
##### Tác vụ con được giao: GCP
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/infra/gcp`
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-010]<!--END_TAGS-->

### DAY 2: <!--DAY_HEADER_START-->TRIEN_KHAI_CO_SO_DU_LIEU_POSTGRESQL<!--DAY_HEADER_END-->

#### SUB-TASK 2.1: Viết các script Flyway/Liquibase để tạo các bảng cơ sở dữ liệu
##### Tác vụ con được giao: Coder
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/main/resources/db/migration`
* **Traceability Tag Tokens:** <!--START_TAGS-->[DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]<!--END_TAGS-->

### DAY 3: <!--DAY_HEADER_START-->TICH_HOP_FIREBASE_AUTHENTICATION<!--DAY_HEADER_END-->

#### SUB-TASK 3.1: Triển khai các dịch vụ xác thực qua email/mật khẩu, Firebase, Google, và Facebook OAuth2
##### Tác vụ con được giao: Coder
##### Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/auth`
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->