# Giai đoạn 3: <!--PHASE_NAME_START-->attendanceService<!--PHASE_NAME_END--> | Mô tả: Thiết kế, triển khai và kiểm thử dịch vụ điểm danh QR cho membership-hub, bao gồm định nghĩa bảng dữ liệu, API REST, xử lý ngoại lệ, và tích hợp bảo mật OWASP.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260802135007 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên Giai đoạn Kỹ thuật** | <!--PHASE_NAME_START-->attendanceService<!--PHASE_NAME_END--> |
| **Mô tả** | Thiết kế, triển khai và kiểm thử dịch vụ điểm danh QR cho membership-hub, bao gồm định nghĩa bảng dữ liệu, API REST, xử lý ngoại lệ, và tích hợp bảo mật OWASP. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/02 13:50:07 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu Giai đoạn
Giai đoạn 3 tập trung vào việc xây dựng dịch vụ điểm danh (attendance) cho membership-hub. Công việc bao gồm:
- Định nghĩa bảng dữ liệu `Attendance` (DAT-006) với các ràng buộc và chỉ mục phù hợp.
- Thiết kế API REST `/attendance` (REQ-012) để ghi nhận điểm danh qua QR, đồng thời hỗ trợ phản hồi trạng thái “đã ghi nhận” (REQ-013).
- Xây dựng logic xử lý ngoại lệ: mạng không ổn định (EXC-001) và điểm danh trùng lặp (EXC-002).
- Tích hợp bảo mật OWASP (XSS, CSRF, CSP) trong toàn bộ lớp service và controller.
- Kiểm thử đơn vị và tích hợp, đảm bảo độ phủ ≥ 85 % và đáp ứng các tiêu chí NFR.

## 2. Phạm vi Kỹ thuật & Giới hạn Thư mục
| Đường dẫn tuyệt đối | Mô tả |
| :--- | :--- |
| `./sources/backend/attendance` | Dịch vụ điểm danh (Java/Quarkus) |
| `./sources/backend/attendance/src/main/java/org/nlh4j/sources/attendance` | Package Java chính |
| `./sources/backend/attendance/src/main/resources/db/migration` | DDL SQL migration |
| `./sources/backend/attendance/src/test/java/org/nlh4j/sources/attendance` | Unit & integration tests |
| `./sources/backend/attendance/src/main/resources/static` | Tài nguyên tĩnh (nếu cần) |
| `./sources/backend/attendance/src/main/resources/logging` | Cấu hình logging |

Endpoint routing:
- `POST /attendance` – ghi nhận điểm danh.
- `GET /attendance/{studentId}/{courseId}` – kiểm tra trạng thái điểm danh (tùy chọn).

## 3. Hướng dẫn Hoạt động Đặc thù cho từng Agent
- **Coder**: Viết mã nguồn Java, DDL, DTO, exception, unit tests, integration tests, và tài liệu API.
- **Tester**: Viết và thực thi unit tests (JUnit 5) và integration tests (REST Assured), đảm bảo coverage ≥ 85 %.
- **Reviewer**: Thực hiện static code analysis (SonarQube), kiểm tra tuân thủ OWASP, và rà soát cú pháp Java.
- **Doc**: Tạo tài liệu API (OpenAPI/Swagger) và hướng dẫn sử dụng, lưu trữ trong `./sources/backend/attendance/docs`.
- **Docker / GCP / GKE**: Không áp dụng trong giai đoạn này.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Bảng `Attendance` được tạo thành công trong PostgreSQL (DAT-006).
- API `/attendance` đáp ứng các yêu cầu [REQ-012] và [REQ-013] với mã trạng thái HTTP phù hợp.
- Các exception [EXC-001] và [EXC-002] được xử lý đúng cách và trả về thông báo rõ ràng.
- Unit test coverage ≥ 85 % cho `AttendanceService` và `AttendanceController`.
- Integration test coverage ≥ 80 % cho toàn bộ luồng điểm danh.
- Static code analysis không phát hiện lỗi nghiêm trọng, tuân thủ OWASP.
- Tài liệu API và hướng dẫn sử dụng hoàn chỉnh, lưu trữ trong `docs`.
- 100 % tag ID được map trong logs.

## 5. LỊCH THỰC HIỆN HÌNH THÁNH ĐỊA NGÀY

### DAY 1: THÊM ĐỊNH NGHĨA BẢNG VÀ API CƠ BẢN

#### SUB-TASK 1.1: Tạo file DDL cho bảng Attendance
##### Coder
##### Thông tin Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn**: `./sources/backend/attendance/src/main/resources/db/migration/V001__create_attendance_table.sql`
* **Thẻ Định danh**: <!--START_TAGS-->[DAT-006]<!--END_TAGS-->

#### SUB-TASK 1.2: Định nghĩa DTO và API contract cho điểm danh
##### Coder
##### Thông tin Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn**: `./sources/backend/attendance/src/main/java/org/nlh4j/sources/attendance/dto/AttendanceRequest.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-012], [REQ-013]<!--END_TAGS-->

#### SUB-TASK 1.3: Xây dựng skeleton AttendanceService và AttendanceController
##### Coder
##### Thông tin Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn**: `./sources/backend/attendance/src/main/java/org/nlh4j/sources/attendance/service/AttendanceService.java`
* **Đường dẫn**: `./sources/backend/attendance/src/main/java/org/nlh4j/sources/attendance/controller/AttendanceController.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-012], [REQ-013], [DAT-006]<!--END_TAGS-->

### DAY 2: XỬ LÝ EXCEPTION VÀ KIỂM THỬ ĐƠN VỊ

#### SUB-TASK 2.1: Tạo exception classes cho mạng và trùng lặp
##### Coder
##### Thông tin Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn**: `./sources/backend/attendance/src/main/java/org/nlh4j/sources/attendance/exception/NetworkException.java`
* **Đường dẫn**: `./sources/backend/attendance/src/main/java/org/nlh4j/sources/attendance/exception/DuplicateAttendanceException.java`
* **Thẻ Định danh**: <!--START_TAGS-->[EXC-001], [EXC-002]<!--END_TAGS-->

#### SUB-TASK 2.2: Viết unit tests cho AttendanceService
##### Tester
##### Thông tin Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn**: `./sources/backend/attendance/src/test/java/org/nlh4j/sources/attendance/service/AttendanceServiceTest.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002]<!--END_TAGS-->

### DAY 3: KIỂM THỬ TÍNH TỔNG, RÀU SOÁT VÀ TÀI LIỆU

#### SUB-TASK 3.1: Viết integration test cho AttendanceController
##### Tester
##### Thông tin Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn**: `./sources/backend/attendance/src/test/java/org/nlh4j/sources/attendance/controller/AttendanceControllerIT.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]<!--END_TAGS-->

#### SUB-TASK 3.2: Thực hiện static code analysis và OWASP review
##### Reviewer
##### Thông tin Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn**: `./sources/backend/attendance/src/main/java/org/nlh4j/sources/attendance`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]<!--END_TAGS-->

#### SUB-TASK 3.3: Tạo tài liệu API và hướng dẫn sử dụng
##### Doc
##### Thông tin Thành phần và Yêu cầu Kỹ thuật:
* **Đường dẫn**: `./sources/backend/attendance/docs/attendance_api.md`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-012], [REQ-013], [EXC-001], [EXC-002], [DAT-006]<!--END_TAGS-->