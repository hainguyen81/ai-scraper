# Thiết Lập Cơ Sở Hạ Tầng Và Xác Thực: <!--PHASE_NAME_START-->ThietLapCoSoHaTangVaXacThuc<!--PHASE_NAME_END--> | Mô Tả: Thiết lập cơ sở hạ tầng backend và frontend, triển khai cơ sở dữ liệu PostgreSQL, tích hợp Firebase Authentication

## 📊 Document Control

| Mục | Chi Tiết |
| :--- | :--- |
| **ID Blueprint** | ARCH-20260804145722 |
| **Tên Dự Án** | membership-hub |
| **Giai Đoạn** | 1 |
| **Tên Giai Đoạn** | <!--PHASE_NAME_START-->ThietLapCoSoHaTangVaXacThuc<!--PHASE_NAME_END--> |
| **Mô Tả** | Thiết lập cơ sở hạ tầng backend và frontend, triển khai cơ sở dữ liệu PostgreSQL, tích hợp Firebase Authentication |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/04 14:57:22 |
| **Tác Giả** | Kiến Trúc Sư Hệ Thống Doanh Nghiệp (SA Agent) |
| **Phê Duyệt** | Đang chờ xem xét của Ban Quản Trị Kỹ Thuật |

## 1. Phạm Vi Hoạt Động và Mục Tiêu của Giai Đoạn
Giai đoạn này tập trung vào việc thiết lập cơ sở hạ tầng backend và frontend, triển khai cơ sở dữ liệu PostgreSQL, và tích hợp Firebase Authentication. Các nhiệm vụ bao gồm:
- Thiết lập cấu hình cơ sở dữ liệu PostgreSQL
- Tích hợp Firebase Authentication
- Thiết lập cấu hình Docker và Kubernetes (GKE)
- Triển khai cơ sở hạ tầng trên Google Cloud Platform (GCP)

## 2. Phạm Vi Kỹ Thuật và Ranh Giới Thư Mục (Files, paths, và endpoints)
- **Backend:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/config`, `./sources/backend/src/main/resources/db/migration`
- **Frontend:** `./sources/frontend/src/components/auth`
- **Docker:** `./sources/backend/Dockerfile`
- **GCP:** `./sources/infra/gcp`

## 3. Hướng Dẫn Chức Năng Đặc Biệt cho Các Đặc Sứ Đặc Biệt
- **Coder:** Triển khai cấu hình cơ sở dữ liệu PostgreSQL, tích hợp Firebase Authentication, thiết lập cấu hình Docker và Kubernetes (GKE)
- **Tester:** Viết các test case cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
- **Reviewer:** Review code cho các tính năng đăng ký người dùng, xác thực qua mạng xã hội, phân quyền người dùng
- **Docker:** Viết Dockerfile cho dịch vụ backend, cấu hình multi-stage build để giảm kích thước image
- **GCP:** Triển khai cơ sở hạ tầng trên Google Cloud Platform, cấu hình VPC, IAM, và các dịch vụ cần thiết

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)
- Hoàn thành 100% các yêu cầu chức năng được phân bổ cho giai đoạn này
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP
- Đảm bảo độ phủ kiểm thử chức năng hoàn chỉnh cho các yêu cầu được phân bổ
- Đảm bảo 100% ánh xạ ID Tag

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### DAY 1: <!--DAY_HEADER_START-->THIẾT LẬP CƠ SỞ HẠ TẦNG BACKEND VÀ FRONTEND<!--DAY_HEADER_END-->

#### SUB-TASK 1.1: Triển khai cấu hình cơ sở dữ liệu PostgreSQL, tích hợp Firebase Authentication, thiết lập cấu hình Docker và Kubernetes (GKE)
##### Đặc Sứ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/config`
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-006], [ARC-010]<!--END_TAGS-->

#### SUB-TASK 1.2: Viết Dockerfile cho dịch vụ backend, cấu hình multi-stage build để giảm kích thước image
##### Đặc Sứ Được Phân Công: Docker
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/Dockerfile`
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-010]<!--END_TAGS-->

#### SUB-TASK 1.3: Triển khai cơ sở hạ tầng trên Google Cloud Platform, cấu hình VPC, IAM, và các dịch vụ cần thiết
##### Đặc Sứ Được Phân Công: GCP
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/infra/gcp`
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-010]<!--END_TAGS-->

### DAY 2: <!--DAY_HEADER_START-->TRIỂN KHAI CƠ SỞ DỮ LIỆU POSTGRESQL<!--DAY_HEADER_END-->

#### SUB-TASK 2.1: Viết các script Flyway/Liquibase để tạo các bảng cơ sở dữ liệu, thiết lập các ràng buộc và chỉ mục
##### Đặc Sứ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/resources/db/migration`
* **Traceability Tag Tokens:** <!--START_TAGS-->[DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]<!--END_TAGS-->

### DAY 3: <!--DAY_HEADER_START-->TÍCH HỢP FIREBASE AUTHENTICATION<!--DAY_HEADER_END-->

#### SUB-TASK 3.1: Triển khai các dịch vụ xác thực qua email/mật khẩu, Firebase, Google, và Facebook OAuth2, cấu hình JWT token với thời hạn 15 phút và refresh token
##### Đặc Sứ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường Dẫn Mục Tiêu:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/auth`
* **Traceability Tag Tokens:** <!--START_TAGS-->[ARC-006]<!--END_TAGS-->