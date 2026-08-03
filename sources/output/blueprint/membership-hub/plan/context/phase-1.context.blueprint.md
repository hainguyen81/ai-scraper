# Giai đoạn 1: <!--PHASE_NAME_START-->phase1_userAuthDocker<!--PHASE_NAME_END--> | Mô tả: Xây dựng nền tảng người dùng, xác thực OAuth2, và cấu hình Docker/GCP ban đầu cho hệ thống membership-hub.  
## 📊 Document Control  

| Mục | Chi tiết |  
| :--- | :--- |  
| **Mã Blueprint** | ARCH-20260803132420 |  
| **Tên Dự án** | membership-hub |  
| **Giai đoạn** | 1 |  
| **Tên Giai đoạn Kỹ thuật** | <!--PHASE_NAME_START-->phase1_userAuthDocker<!--PHASE_NAME_END--> |  
| **Mô tả** | Xây dựng nền tảng người dùng, xác thực OAuth2, và cấu hình Docker/GCP ban đầu cho hệ thống membership-hub. |  
| **Phiên bản** | 1.0 (Baseline) |  
| **Ngày/Giờ** | 2026/08/03 13:24:20 |  
| **Tác giả** | Enterprise System Architect (SA Agent) |  
| **Phê duyệt** | Pending Technical Governance Review |  

## 1. Phạm vi và Mục tiêu Giai đoạn  
Giai đoạn 1 tập trung vào việc triển khai hai dịch vụ cốt lõi: **User Service** và **Auth Service**. Các dịch vụ này cung cấp API đăng ký, đăng nhập, và lấy thông tin người dùng, đồng thời tích hợp OAuth2 với Firebase, Google, và Facebook. Ngoài ra, giai đoạn còn xây dựng Dockerfile đa giai đoạn và cấu hình tài nguyên GCP ban đầu (VPC, Cloud SQL, Redis, Secret Manager). Mọi thành phần phải tuân thủ nguyên tắc OWASP Top 10, bảo mật JWT, và bảo vệ dữ liệu nhạy cảm.  

## 2. Phạm vi Kỹ thuật & Ranh giới Thư mục  
- **Backend**  
  - `./sources/backend.users` – Resource `UserResource`, entity `User`, repository `UserRepository`.  
  - `./sources/backend.auth` – Resource `AuthResource`, service `AuthService`, event `UserAuthenticatedEvent`.  
- **Infrastructure**  
  - `./sources/infra.dockerfile` – Dockerfile đa giai đoạn cho cả `users` và `auth`.  
  - `./sources/infra.gcp` – Terraform/IaC cho VPC, Cloud SQL, Redis, Secret Manager.  
- **REST Endpoints**  
  - `POST /api/v1/auth/register` – đăng ký người dùng.  
  - `POST /api/v1/auth/social` – đăng nhập bằng OAuth2.  
  - `GET /api/v1/auth/me` – lấy thông tin người dùng hiện tại.  
  - `POST /api/v1/users` – endpoint đăng ký (được dùng trong test).  

## 3. Chỉ đạo Chức năng Đặc thù Agent  
- **Coder**: triển khai mã nguồn Java/Kotlin, cấu hình Quarkus, bảo mật JWT, mã hóa BCrypt, tạo Dockerfile.  
- **Reviewer**: thực hiện static code analysis (SonarQube), kiểm tra OWASP, chạy unit test, kiểm tra coverage ≥ 85 %.  
- **Doc**: biên soạn tài liệu API (OpenAPI), ghi chú trong `./sources/docs.api`.  

## 4. Định nghĩa Hoàn thành Giai đoạn  
- Tất cả yêu cầu [REQ-001], [REQ-002], [REQ-003] được triển khai và kiểm thử thành công.  
- Mọi tag trong Phase 1 được ánh xạ chính xác (25 tag).  
- Đạt OWASP compliance: SQLi, XSS, CSRF, JWT, TLS 1.3.  
- Coverage unit test ≥ 85 % cho `users` và `auth`.  
- Docker image size < 500 MB.  
- GCP IaC triển khai thành công, các tài nguyên được ghi nhận trong `./sources/infra.gcp`.  

## 5. Nhật ký Thực thi Kiến trúc Theo Ngày  

### DAY 1: XÂY DỰNG DỊCH VỤ NGƯỜI DÙNG  

#### SUB-TASK 1.1: Triển khai UserResource và User entity  
##### Assigned Sub-Agent: Coder  
##### Targeted Components & Technical Requirements:  
* **Đường dẫn**: `./sources/backend.users`  
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-001], [DAT-001], [EXC-004]<!--END_TAGS-->  

### DAY 2: XÂY DỰNG DỊCH VỤ XÁC THỰC OAuth2  

#### SUB-TASK 2.1: Triển khai AuthResource và AuthService  
##### Assigned Sub-Agent: Coder  
##### Targeted Components & Technical Requirements:  
* **Đường dẫn**: `./sources/backend.auth`  
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-002], [ARC-006], [EXC-004]<!--END_TAGS-->  

### DAY 3: ĐÁNH GIÁ CHẤT LƯỢNG MÃ VÀ KIỂM TRA BẢO MẬT  

#### SUB-TASK 3.1: Kiểm tra static code, unit test, coverage, và Docker build  
##### Assigned Sub-Agent: Reviewer  
##### Targeted Components & Technical Requirements:  
* **Đường dẫn**: `./sources/backend.users`  
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-001], [REQ-002], [DAT-001], [NFR-001], [NFR-006], [EXC-004]<!--END_TAGS-->