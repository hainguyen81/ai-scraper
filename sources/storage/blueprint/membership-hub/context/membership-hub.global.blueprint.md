# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Kiểm soát Tài liệu

| Mục | Chi tiết |
| :--- | :--- |
| **ID Bản thiết kế** | ARCH-20260803043556 |
| **Tên Dự án** | membership-hub |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày.Giờ** | 2026/08/03 04:35:56 |
| **Tác giả** | Kiến trúc sư Hệ thống Doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ Đánh giá Quản trị Kỹ thuật |

## 📊 1. TỔNG QUAN HỆ THỐNG & PHƯƠNG THỨC KIẾN TRÚC CỐT LÕI

### 1.1. Phương thức Hệ thống Cốt lõi & Phương thức Kiến trúc
Hệ thống `membership-hub` được thiết kế theo kiến trúc microservices phân tán, sử dụng mô hình CQRS (Command Query Responsibility Segregation) để tách biệt luồng ghi (command) và đọc (query), đảm bảo hiệu suất và khả năng mở rộng. Kiến trúc phản ứng (Reactive) được áp dụng thông qua framework Quarkus để xử lý các yêu cầu không đồng bộ và có khả năng chịu tải cao. Mô hình Event-Driven Architecture (EDA) được sử dụng cho các luồng thông báo và tích hợp bên ngoài (Zalo, FCM/APNs), đảm bảo tính nhất quán cuối cùng và khả năng phục hồi.

### 1.2. Cấu trúc Luồng Dữ liệu Doanh nghiệp & Hệ sinh thái Cốt lõi
Các kênh truyền thông không đồng bộ được quản lý thông qua Redis cho caching phiên và message brokering nhẹ. Cổng thu thập dữ liệu xử lý xác thực OAuth2 và JWT token issuance. Các topology chủ đề (topic topologies) bao gồm: `notifications` cho push notifications, `zalo-messages` cho tích hợp Zalo API, và `attendance-scans` cho xử lý điểm danh QR idempotent. Kiến trúc fan-out bên ngoài chéo kênh đảm bảo thông báo được phân phối đồng thời tới ứng dụng di động và các nhóm Zalo được chỉ định.

## 📁 2. NGĂN XẾP CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI

- **Ngăn xếp Hạ tầng Backend Cốt lõi:** Java 17+, Quarkus 3.2+ (runtime engine, dependency injection, RESTEasy Reactive), Hibernate ORM với Panache, SmallRye Reactive Messaging, Quarkus Security với JWT và OAuth2, Flyway cho database migrations, PostgreSQL JDBC driver.
- **Ngăn xếp Frontend & UI Đa nền tảng Di động:** Next.js 14+ (web framework), React Native 0.72+ (mobile app), React i18next cho đa ngôn ngữ, Capacitor cho wrapper native, Zalo SDK cho tích hợp, Firebase SDK cho authentication và cloud messaging.

## 📁 3. CÁC TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP & RAIL BẢO VỆ TOÀN CẦU

- **Quy tắc Ranh giới Không gian làm việc Tuyệt đối:** Root không gian làm việc repository thực sự được cố định vĩnh viễn tại project root `..`. Tất cả các đường dẫn được tạo PHẢI bắt đầu với `./sources/`.
- **Tuân thủ Tiền tố Thư mục Động:** Thực thi nghiêm ngặt các quy tắc ánh xạ đường dẫn động được định nghĩa trong Protocol 1, khớp chính xác với cấu trúc dự án được phát hiện.
- **[ĐIỀU KIỆN: CHỈ_JAVA_STACK] Tiêu chuẩn Gói Java:** Nếu ngăn xếp công nghệ sử dụng các framework Java, tất cả mã nguồn Java PHẢI nằm nghiêm ngặt trong foundation package của công ty: `org.nlh4j.saas.membershiphub`. Bạn PHẢI chuyển đổi động chuỗi "membership-hub" thành một token chữ thường thuần chữ số nghiêm ngặt bằng cách loại bỏ khoảng trắng, dấu gạch ngang và gạch dưới. Các dự án không phải Java hoàn toàn bị cấm áp dụng segment package này.
- **Cú pháp Đường dẫn Mục tiêu Tester Nghiêm ngặt:** Bất kỳ component nào được nhắm mục tiêu bởi một Sub-Agent Tester phải được cấu trúc như một cặp phân tách bằng dấu chấm phẩy nghiêm ngặt `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn bên trong cặp PHẢI bắt đầu với `./sources/`.

## 📁 4. LƯỢC ĐỒ KIẾN TRÚC ĐA GIAI ĐOẠN CẤP CAO

| Giai đoạn | Khoảng ngày | Đường dẫn Cấu phần / Module Kiến trúc | Tóm tắt Sản phẩm Bàn giao Kỹ thuật | Sub-Agent được chỉ định | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1-4 | `./sources/backend.auth-service/`<br>`./sources/backend.user-center-service/`<br>`./sources/infra/database/` | Thiết lập dịch vụ xác thực, schema cơ sở dữ liệu người dùng & vai trò, tích hợp OAuth2, triển khai RBAC cơ bản. | Coder, Tester, Docker, GCP | [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-006] |
| 2 | 5-7 | `./sources/backend.course-service/`<br>`./sources/backend.enrollment-service/`<br>`./sources/frontend.web-app/` | Triển khai quản lý trung tâm & khóa học, logic ghi danh, giao diện web cơ bản để duyệt khóa học. | Coder, Tester, Reviewer, Doc | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [DAT-003], [DAT-004], [DAT-005], [NFR-001], [NFR-007] |
| 3 | 8-10 | `./sources/backend.attendance-service/`<br>`./sources/backend.membership-service/`<br>`./sources/frontend.mobile-app/` | Dịch vụ quét QR điểm danh idempotent, quản lý thẻ hội viên, khung ứng dụng di động đa vai trò. | Coder, Tester, Docker, GKE | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-020], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [NFR-001], [NFR-004] |
| 4 | 11-13 | `./sources/backend.notification-service/`<br>`./sources/backend.promo-announce-service/` | Dịch vụ thông báo đa kênh (FCM/APNs, Zalo), quản lý khuyến mãi & thông báo, tích hợp chatbot AI cơ bản. | Coder, Tester, GCP, GKE | [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-021], [DAT-008], [DAT-009], [EXC-003], [NFR-002], [NFR-004], [NFR-008] |
| 5 | 14-15 | `./sources/backend.reporting-service/`<br>`./sources/infra/ci-cd/` | Báo cáo điểm danh, dashboard tổng quan, hoàn thiện pipeline CI/CD, triển khai tự động hóa. | Coder, Tester, Doc, Docker, GCP, GKE | [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-011], [EXC-005], [NFR-005], [NFR-009] |

## 5. CHUYÊN MÔN HÓA GIAI ĐOẠN CHI TIẾT & SẢN PHẨM BÀN GIAO THEO TỪNG NGÀY

<!--START_DELIMITTER-->
### Đặc tả Kiến trúc Chi tiết Giai đoạn 1
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Thiết lập nền tảng xác thực và ủy quyền vững chắc cho toàn bộ hệ thống. Giai đoạn này tập trung vào việc tạo lược đồ cơ sở dữ liệu người dùng, triển khai luồng đăng ký/đăng nhập (email/mật khẩu và OAuth2), thiết lập cơ chế RBAC cơ bản, và đảm bảo các biện pháp bảo mật (JWT, mã hóa) ngay từ đầu.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:**
  * `./sources/backend.auth-service/src/main/java/org/nlh4j/saas/membershiphub/AuthResource.java` [REQ-001], [REQ-002], [ARC-006]
  * `./sources/backend.auth-service/src/main/resources/db/migration/V1__init_users_roles_schema.sql` [DAT-001]
  * `./sources/backend.user-center-service/src/main/java/org/nlh4j/saas/membershiphub/UserManagementResource.java` [REQ-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]
  * `./sources/backend.auth-service/src/test/java/org/nlh4j/saas/membershiphub/AuthResourceTest.java;./sources/backend.auth-service/src/main/java/org/nlh4j/saas/membershiphub/AuthResource.java` [REQ-001], [REQ-002]
  * `./sources/infra/database/init/01-create-db.sql` [NFR-003]
  * `./sources/infra/docker/Dockerfile.auth-service` [NFR-005]
- **Đặc tả DDL SQL Schema Cơ sở dữ liệu [DAT-001]:**
```sql
CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) NOT