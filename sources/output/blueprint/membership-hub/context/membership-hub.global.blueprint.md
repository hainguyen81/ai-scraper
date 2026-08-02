# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Kiểm Soát Tài Liệu

| Item | Chi Tiết |
| :--- | :--- |
| **Mã Bản Vẽ** | ARCH-20260802155040 |
| **Tên Dự Án** | membership-hub |
| **Phiên Bản** | 1.0 (Baseline) |
| **Ngày.Giờ** | 2026/08/02 15:50:40 |
| **Tác Giả** | Kiến Trúc Sư Hệ Thống Doanh Nghiệp (SA Agent) |
| **Phê Duyệt** | Chờ Kiểm Tra Quản Lý Kỹ Thuật |

## 📊 1. TỔNG QUAN HỆ THỐNG & MÔ HÌNH KIẾN TRÚC CƠ BẢN
### 1.1. Mô Hình Hệ Thống Cơ Bản & Mô Hình Kiến Trúc
Hệ thống membership-hub được thiết kế dựa trên mô hình kiến trúc microservices, với các thành phần chính bao gồm: dịch vụ đăng ký, dịch vụ quản lý thành viên, dịch vụ thanh toán, và dịch vụ tích hợp. Mô hình này cho phép hệ thống có thể mở rộng và phát triển linh hoạt.

### 1.2. Kiến Trúc Dòng Dữ Liệu Doanh Nghiệp & Hệ Sinh Thái Cơ Bản
Hệ thống sử dụng kiến trúc dòng dữ liệu异步, với các kênh thông điệp, cổng nhập dữ liệu, và kiến trúc phân tán. Điều này cho phép hệ thống có thể xử lý và phân tích dữ liệu một cách hiệu quả.

## 📁 2. TÀI NGUYÊN CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI
- **Ngăn xếp Cơ sở Hạ tầng Backend:** Hệ thống sử dụng ngôn ngữ lập trình Java, framework Spring Boot, và cơ sở dữ liệu MySQL.
- **Ngăn xếp Frontend & Di động:** Hệ thống sử dụng framework React, thư viện Redux, và trình duyệt web.

## 📁 3. HÀNG RÀO AN TOÀN & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
- **Quy tắc Giới Hạn Không Gian Làm Việc:** Không gian làm việc của dự án được cố định tại thư mục gốc `..`.
- **Quy tắc Đặt Tiền Tố Đường Dẫn Động:** Hệ thống sử dụng quy tắc đặt tiền tố đường dẫn động để đảm bảo tính linh hoạt và mở rộng.
- **[ĐIỀU KIỆN: JAVA_STACK_ONLY] Tiêu Chuẩn Gói Java:** Nếu hệ thống sử dụng framework Java, tất cả mã nguồn Java phải nằm trong gói `org.nlh4j.saas.<tên_dự_án_alphanumeric_lowercase>`.
- **Quy tắc Cú Pháp Đường Dẫn Mục Tiêu Tester:** Mọi thành phần được Tester Sub-Agent nhắm đến phải được cấu trúc dưới dạng cặp đường dẫn nghiêm ngặt `<thành_phần_nguồn>;<tệp_thử_nghiệm>`.

## 📁 4. TỔNG QUAN KIẾN TRÚC ĐA GIAI ĐOẠN
| Giai đoạn | Phạm vi Ngày | Thành phần/Mô-đun Đường dẫn | Tóm tắt Vận hàng Kỹ thuật | Sub-Agent được Giao | Mã Thẻ Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 5. CHUYÊN MÔN GIAI ĐOẠN & VẬN HÀNH HÀNG NGÀY
### Giai đoạn 1: Thiết kế Hệ Thống
- **Mục tiêu & Mục đích Giai đoạn:** Thiết kế hệ thống và xây dựng kiến trúc cơ bản.
- **Ma trận Đường dẫn Thư mục Vật lý:** 
  - `./sources/backend`
  - `./sources/frontend`
- **Đặc tả DDL SQL Cơ sở Dữ liệu [DAT-XXX]:** 
```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);
```
- **Hợp đồng API và Sự kiện [REQ-XXX], [ARC-XXX]:** 
```json
{
  "type": "object",
  "properties": {
    "id": {"type": "integer"},
    "name": {"type": "string"},
    "email": {"type": "string"}
  }
}
```
- **Bộ xử lý Ngoại lệ Địa phương [EXC-XXX]:** 
  - Xử lý ngoại lệ khi đăng ký thành viên.

#### 📅 Phân phối Công việc Sub-Agent Hàng ngày (Giai đoạn 1)
- **NGÀY 1:** Thiết kế hệ thống và xây dựng kiến trúc cơ bản.
  - **Chuyên môn Sub-Agent:** 
    * **Coder:** 
      - **Đường dẫn Thành phần mục tiêu (`target_component`):** `./sources/backend/user-service`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Thiết kế và xây dựng dịch vụ đăng ký thành viên.
      - **Mã Thẻ Mục tiêu:** [REQ-001], [DAT-001]
    * **Tester:** 
      - **Đường dẫn Thành phần mục tiêu (`target_component`):** `./sources/backend/user-service;./sources/test/user-service-test`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Kiểm tra dịch vụ đăng ký thành viên.
      - **Mã Thẻ Mục tiêu:** [REQ-001], [DAT-001]

## 📁 6. MÃ HỆ THỐNG AN TOÀN DOANH NGHIỆP & BIỆN PHÁP CHỐNG TIÊM CODE [NFR-XXX]
- **Biện pháp Chống Tiêm Code SQL (SQLi) Tuyệt đối:** Sử dụng các câu lệnh chuẩn bị, tham số vị trí, và danh sách trắng.
- **Biện pháp Chống Tiêm Code Trang web (XSS) & Chính sách Bảo mật Nội dung (CSP):** Sử dụng các tiêu chuẩn tự động hóa, thoát khỏi ngữ cảnh, và hạn chế `unsafe-inline`.

## 📁 7. QUY TẮC TUÂN THỦ DI ĐỘNG HYBRID & CƠ CHẾ TIÊM SEO QUỐC TẾ
- **Quy tắc Tuân thủ Di động Hybrid:** Sử dụng các quy tắc động, địa chỉ tuyệt đối, và các biện pháp an toàn.
- **Cơ chế Tiêm SEO Quốc tế:** Sử dụng các kiến trúc middleware, nhận dạng ngôn ngữ, và hạn chế robots.

## 📁 8. LUỒNG PIPELINE TỰ ĐỘNG HÀNG NGÀY
- **Forking Isolation Không gian Làm việc Hàng ngày:** Sử dụng các quy tắc fork không gian làm việc.
- **Cổng Kiểm tra Pipeline:** Sử dụng các quy tắc kiểm tra, xác thực, và ghi nhật ký.