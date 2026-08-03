# Giai đoạn 4: <!--PHASE_NAME_START-->mobileUiSettings<!--PHASE_NAME_END--> | Mô tả: Triển khai giao diện di động đa nền tảng, tích hợp tính năng push, đa ngôn ngữ, SEO, và API cài đặt hệ thống, đồng thời bảo đảm tuân thủ OWASP, bảo mật JWT, và ghi nhận cấu hình trong bảng SYSTEMSETTINGS.  

## 📊 Document Control  

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260803170121 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn kỹ thuật** | <!--PHASE_NAME_START-->mobileUiSettings<!--PHASE_NAME_END--> |
| **Mô tả** | Triển khai giao diện di động đa nền tảng, tích hợp tính năng push, đa ngôn ngữ, SEO, và API cài đặt hệ thống, đồng thời bảo đảm tuân thủ OWASP, bảo mật JWT, và ghi nhận cấu hình trong bảng SYSTEMSETTINGS. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/03 17:01:21 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và mục tiêu của giai đoạn  
Giai đoạn 4 tập trung vào việc triển khai giao diện di động đa nền tảng (React/Next.js + Capacitor) với khả năng đăng ký push, đa ngôn ngữ, và tối ưu SEO, đồng thời xây dựng mô-đun backend `SystemSettings` cung cấp API CRUD và lưu trữ cấu hình trong bảng `SYSTEMSETTINGS`. Tất cả các thành phần phải tuân thủ OWASP Top 10, sử dụng JWT 15 phút, và ghi nhận audit cho mọi thay đổi cấu hình.

## 2. Phạm vi kỹ thuật và ranh giới thư mục cho phép  
- **Thư mục frontend**: `./sources/frontend.mobile/` – chứa mã nguồn Next.js/React, TypeScript, Capacitor, i18n, SEO meta tags.  
- **Thư mục backend**: `./sources/backend.settings/` – Quarkus Java service, Hibernate ORM, Flyway migration, REST endpoints.  
- **Endpoints**:  
  - `GET /api/settings` – Lấy toàn bộ cài đặt hệ thống.  
  - `POST /api/settings` – Tạo hoặc cập nhật cài đặt.  
  - `GET /api/settings/:key` – Lấy cài đặt theo key.  
  - `DELETE /api/settings/:key` – Xóa cài đặt.  
- **Tích hợp push**: Firebase Admin SDK (FCM/APNs) và Zalo API cho thông báo.  
- **Bảo mật**: JWT 15 phút, refresh 7 ngày, bảo vệ OWASP, mã hóa AES‑256, TLS 1.3.

## 3. Hướng dẫn chức năng dành cho các đại lý phụ trách  
- **Coder**: Xây dựng UI, navigation, push registration, i18n, SEO meta tags, SystemSettings service, repository, entity, Flyway migration, API endpoints, JWT validation, OWASP mitigations.  
- **Tester**: Viết unit tests cho UI (React Testing Library), integration tests cho API (RestAssured), mock external services (FCM, Zalo), kiểm tra tiêu đề bảo mật, kiểm tra JWT hết hạn, kiểm tra CRUD, kiểm tra i18n fallback.  
- **Doc**: Tạo tài liệu kỹ thuật cho mobile UI (định nghĩa component, navigation, i18n, SEO), tài liệu API SystemSettings (định nghĩa endpoint, schema, ví dụ), hướng dẫn triển khai, checklist OWASP, lưu trữ trong `./sources/frontend.mobile/docs/` và `./sources/backend.settings/docs/`.

## 4. Định nghĩa Hoàn thành giai đoạn (DoD)  
- Tất cả OWASP Top 10 mitigations được triển khai và xác nhận qua static analysis (SonarQube) và dynamic tests.  
- Coverage unit test ≥ 100 % cho `frontend.mobile` và `backend.settings`.  
- Integration tests bao quát toàn bộ CRUD và luồng push notification.  
- Thời gian phản hồi API ≤ 200 ms dưới tải giả lập 10 000 người dùng đồng thời.  
- Tất cả tag yêu cầu ([REQ-020]–[REQ-023], [DAT-011]) được ánh xạ và tham chiếu trong mã và tài liệu.  
- CRUD SystemSettings lưu trữ chính xác và ghi audit logs.  
- Mobile UI vượt kiểm tra truy cập (WCAG 2.1 AA) và audit SEO (Google Lighthouse).  
- Tài liệu hoàn chỉnh và lưu trữ trong thư mục docs tương ứng.

## 5. LỊCH THỰC HIỆN KIẾT THUẬT NGÀY ĐẾN NGÀY  

### DAY 1: XÂY DỰNG GIAO DIỆN DI ĐỘNG VÀ API CÀI ĐẶT HỆ THỐNG  

#### SUB-TASK 1.1: Xây dựng giao diện di động, đăng ký push, đa ngôn ngữ, SEO  
##### ĐẠI LÝ PHỤ TRÁCH: Coder  
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:  
* **Đường dẫn mục tiêu**: `./sources/frontend.mobile/src/main/js/App.js`  
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]<!--END_TAGS-->  

#### SUB-TASK 1.2: Triển khai API và schema SystemSettings  
##### ĐẠI LÝ PHỤ TRÁCH: Coder  
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:  
* **Đường dẫn mục tiêu**: `./sources/backend.settings/src/main/java/com/membershiphub/settings/SystemSettingsService.java`  
* **Thẻ theo dõi**: <!--START_TAGS-->[DAT-011]<!--END_TAGS-->  

### DAY 2: KIỂM THỬ VÀ TÀI LIỆU  

#### SUB-TASK 2.1: Kiểm thử đơn vị cho giao diện di động  
##### ĐẠI LÝ PHỤ TRÁCH: Tester  
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:  
* **Đường dẫn mục tiêu**: `./sources/frontend.mobile/src/test/js/App.test.js`  
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]<!--END_TAGS-->  

#### SUB-TASK 2.2: Kiểm thử đơn vị cho API SystemSettings  
##### ĐẠI LÝ PHỤ TRÁCH: Tester  
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:  
* **Đường dẫn mục tiêu**: `./sources/backend.settings/src/test/java/com/membershiphub/settings/SystemSettingsServiceTest.java`  
* **Thẻ theo dõi**: <!--START_TAGS-->[DAT-011]<!--END_TAGS-->  

#### SUB-TASK 2.3: Tài liệu kỹ thuật cho mobile UI và SystemSettings  
##### ĐẠI LÝ PHỤ TRÁCH: Doc  
##### Thành phần mục tiêu & Yêu cầu kỹ thuật:  
* **Đường dẫn mục tiêu**: `./sources/frontend.mobile/docs/README.md` và `./sources/backend.settings/docs/README.md`  
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-020], [DAT-011]<!--END_TAGS-->