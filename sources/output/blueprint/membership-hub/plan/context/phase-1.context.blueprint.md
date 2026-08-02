# Giai đoạn 1: <!--PHASE_NAME_START-->phase1UserCenterService<!--PHASE_NAME_END--> | Mô tả: Thiết kế và triển khai dịch vụ người dùng và trung tâm, bao gồm định nghĩa schema, API, và logic xử lý, đáp ứng các yêu cầu đăng ký, quản lý người dùng, và quản lý trung tâm.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260802135007 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên Giai đoạn Kỹ thuật** | <!--PHASE_NAME_START-->phase1UserCenterService<!--PHASE_NAME_END--> |
| **Mô tả** | Thiết kế và triển khai dịch vụ người dùng và trung tâm, bao gồm định nghĩa schema, API, và logic xử lý, đáp ứng các yêu cầu đăng ký, quản lý người dùng, và quản lý trung tâm. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/02 13:50:07 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
Giai đoạn 1 tập trung vào việc xây dựng hai dịch vụ cốt lõi của hệ thống membership-hub: **User Service** và **Center Service**. Các dịch vụ này chịu trách nhiệm:
- Định nghĩa và triển khai schema PostgreSQL cho bảng `users` và `centers`.
- Cung cấp REST API `/users` và `/centers` với các phương thức POST/GET/PUT/DELETE phù hợp.
- Xử lý đăng ký, xác thực, và quản lý vai trò người dùng (System Admin, Center Admin, Manager, Teacher, Student).
- Quản lý thông tin trung tâm, bao gồm tên, địa chỉ, mã số thuế, và liên hệ quản trị.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP, bảo vệ chống SQL Injection, XSS, CSRF, và bảo mật JWT.
- Đảm bảo tính nhất quán dữ liệu, tính toàn vẹn tham chiếu, và khả năng mở rộng theo kiến trúc microservices.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Directory Matrix**  
  - `./sources/backend/users` – chứa mã nguồn Java Quarkus cho User Service.  
  - `./sources/backend/centers` – chứa mã nguồn Java Quarkus cho Center Service.
- **Database Schema**  
  - `users` table (DAT-001) – định nghĩa trong DDL SQL.  
  - `centers` table (DAT-003) – định nghĩa trong DDL SQL.
- **REST Endpoints**  
  - `/users` – POST (đăng ký), GET (liệt kê), PUT (cập nhật), DELETE (xóa).  
  - `/centers` – POST (tạo), GET (liệt kê), PUT (cập nhật), DELETE (xóa).
- **Event Routing** – các sự kiện đăng ký và cập nhật sẽ được phát ra qua Kafka (ARC-001, ARC-004) để đồng bộ dữ liệu giữa các microservice.

## 3. Dedicated Sub-Agent Functional Directives
| Agent | Trách nhiệm chính |
| :--- | :--- |
| **Coder** | Viết mã nguồn Java, triển khai DDL, viết unit test, và chuẩn bị tài liệu API. |
| **Tester** | Viết và chạy integration tests, kiểm tra tính toàn vẹn dữ liệu và bảo mật. |
| **Reviewer** | Phân tích tĩnh, kiểm tra cú pháp, và đảm bảo tuân thủ quy chuẩn mã nguồn. |
| **Doc** | Tạo tài liệu kỹ thuật, mô tả API, và hướng dẫn triển khai. |
| **Docker** | Xây dựng Docker image cho các service. |
| **GCP** | Cấu hình tài nguyên GCP (Cloud SQL, Cloud Pub/Sub). |
| **GKE** | Triển khai và quản lý cluster Kubernetes. |

## 4. Phase Definition of Done (DoD)
- Tất cả các yêu cầu [REQ-001], [REQ-004] được triển khai hoàn chỉnh.  
- Schema PostgreSQL cho `users` và `centers` được tạo và migration thành công.  
- API `/users` và `/centers` đáp ứng đúng contract JSON và bảo mật JWT.  
- Unit test coverage ≥ 85 % cho cả hai dịch vụ.  
- Integration test coverage ≥ 80 % và không có lỗi bảo mật OWASP.  
- Tất cả tag ID được map 100 % trong logs.  
- Code được review và static analysis không phát hiện lỗi nghiêm trọng.  
- Tài liệu API và hướng dẫn triển khai được hoàn thiện.  
- Docker image được build và push tới registry.  
- Đã triển khai thử nghiệm trên GKE (đối với giai đoạn này, deployment có thể được mock).  

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: XÂY ĐOÁN DỊCH VỤ NGƯỜI DÙNG

#### SUB-TASK 1.1: Thiết kế và triển khai lớp UserService để xử lý đăng ký và quản lý người dùng, bao gồm xác thực, hashing mật khẩu, và lưu trữ dữ liệu vào bảng users.  
##### Người phụ trách: Coder  
##### Các thành phần & Yêu cầu kỹ thuật:  
* **Đường dẫn mục tiêu**: ./sources/backend/users/UserService.java  
* **Thẻ Trac theo dõi**: <!--START_TAGS-->[REQ-001], [DAT-001]<!--END_TAGS-->

### DAY 2: XÂY ĐOÁN DỊCH VỤ TRUNG TÂM

#### SUB-TASK 2.1: Thiết kế và triển khai lớp CenterService để xử lý tạo, cập nhật, và xóa trung tâm, bao gồm kiểm tra tính duy nhất của mã số thuế và lưu trữ dữ liệu vào bảng centers.  
##### Người phụ trách: Coder  
##### Các thành phần & Yêu cầu kỹ thuật:  
* **Đường dẫn mục tiêu**: ./sources/backend/centers/CenterService.java  
* **Thẻ Trac theo dõi**: <!--START_TAGS-->[REQ-004], [DAT-003]<!--END_TAGS-->