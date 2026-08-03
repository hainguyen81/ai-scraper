# Giai đoạn 2: <!--PHASE_NAME_START-->courseEnrollmentAttendanceCard<!--PHASE_NAME_END--> | Mô tả: Giai đoạn 2 tập trung vào xây dựng và triển khai các mô-đun khóa học, ghi danh, điểm danh và thẻ hội viên, bao gồm thiết kế schema, API, logic nghiệp vụ, kiểm thử, và tuân thủ các tiêu chuẩn bảo mật OWASP.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260803170121 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn kỹ thuật** | <!--PHASE_NAME_START-->courseEnrollmentAttendanceCard<!--PHASE_NAME_END--> |
| **Mô tả** | Giai đoạn 2 tập trung vào xây dựng và triển khai các mô-đun khóa học, ghi danh, điểm danh và thẻ hội viên, bao gồm thiết kế schema, API, logic nghiệp vụ, kiểm thử, và tuân thủ các tiêu chuẩn bảo mật OWASP. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/03 17:01:21 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và mục tiêu giai đoạn
Giai đoạn 2 thực hiện toàn bộ chức năng liên quan đến quản lý khóa học, ghi danh học viên, điểm danh qua QR và quản lý thẻ hội viên. Các nhiệm vụ chính bao gồm:
- Thiết kế và triển khai schema PostgreSQL cho bảng `COURSES`, `ENROLLMENTS`, `ATTENDANCE`, `STUDENTCARDS`.
- Xây dựng dịch vụ REST (`CourseService`, `EnrollmentService`, `AttendanceService`, `CardService`) với logic nghiệp vụ, kiểm tra xung đột lịch, tính tính chất bất biến điểm danh và tính hợp lệ thẻ.
- Tích hợp bảo mật OWASP (prepared statements, input validation, CSRF tokens, rate limiting) và tuân thủ NFR về hiệu năng, bảo mật, và bảo mật dữ liệu.
- Viết unit test đầy đủ cho từng dịch vụ, đạt 100% coverage, và thực hiện review mã nguồn để đảm bảo tuân thủ OWASP Top 10.
- Đảm bảo tất cả các Tag ID được ánh xạ đầy đủ và ghi nhận trong nhật ký thực thi.

## 2. Phạm vi kỹ thuật và ranh giới thư mục
| Đường dẫn thư mục | Mô tả |
| :--- | :--- |
| `./sources/backend.course/` | Dịch vụ, controller, repository, DTO cho khóa học. |
| `./sources/backend.enrollment/` | Dịch vụ, controller, repository, DTO cho ghi danh. |
| `./sources/backend.attendance/` | Dịch vụ, controller, repository, DTO cho điểm danh. |
| `./sources/backend.card/` | Dịch vụ, controller, repository, DTO cho thẻ hội viên. |
| Endpoints | `/api/courses`, `/api/enrollments`, `/api/attendance`, `/api/cards` |

## 3. Hướng dẫn chức năng đại lý phụ
- **Coder**: Xây dựng lớp dịch vụ, controller, repository, DTO, và logic nghiệp vụ; triển khai bảo mật OWASP; tạo DDL SQL; viết mã theo chuẩn Quarkus và Hibernate.  
- **Tester**: Viết unit test cho từng dịch vụ, kiểm tra tính đúng đắn, độ an toàn, và độ tin cậy; đạt 100% coverage; sử dụng Testcontainers cho PostgreSQL.  
- **Reviewer**: Kiểm tra mã nguồn, thực hiện static analysis, xác nhận tuân thủ OWASP Top 10, tối ưu hiệu năng, và ghi nhận audit logs.  
- **Doc**: Tạo tài liệu API, mô hình dữ liệu, hướng dẫn triển khai; cập nhật README và tài liệu bảo mật.  

## 4. Định nghĩa Hoàn thành (DoD)
- 100% test coverage cho tất cả các dịch vụ thuộc Phase 2.  
- Mọi API đáp ứng tiêu chuẩn OWASP (prepared statements, input validation, CSRF, rate limiting).  
- Tất cả các Tag ID (REQ‑007…REQ‑015, ARC‑007…ARC‑009, DAT‑004…DAT‑007, EXC‑001, EXC‑002, NFR‑001, NFR‑003, NFR‑005, NFR‑006, NFR‑007, NFR‑008) được ghi nhận trong nhật ký thực thi.  
- Schema PostgreSQL được triển khai thành công, các constraint và index phù hợp.  
- Đánh giá bảo mật đạt mức 0 điểm rủi ro OWASP Top 10.  

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: XÂY DỰNG MÔ-ĐUN KHÓA HỌC

#### SUB-TASK 1.1: Xây dựng CourseService, CRUD khóa học và kiểm tra xung đột lịch
##### Đại lý phụ được giao: Coder
##### Thành phần và yêu cầu kỹ thuật được nhắm tới:
* **Đường dẫn mục tiêu**: `./sources/backend.course/src/main/java/com/membershiphub/course/CourseService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009], [ARC-007], [ARC-008], [ARC-009], [DAT-004], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 1.2: Viết unit test cho CourseService
##### Đại lý phụ được giao: Tester
##### Thành phần và yêu cầu kỹ thuật được nhắm tới:
* **Đường dẫn mục tiêu**: `./sources/backend.course/src/test/java/com/membershiphub/course/CourseServiceTest.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009], [ARC-007], [ARC-008], [ARC-009], [DAT-004], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 1.3: Review CourseService cho tuân thủ OWASP và hiệu năng
##### Đại lý phụ được giao: Reviewer
##### Thành phần và yêu cầu kỹ thuật được nhắm tới:
* **Đường dẫn mục tiêu**: `./sources/backend.course/src/main/java/com/membershiphub/course/CourseService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-007], [REQ-008], [REQ-009], [ARC-007], [ARC-008], [ARC-009], [DAT-004], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

### DAY 2: XÂY DỰNG MÔ-ĐUN GHI DANH

#### SUB-TASK 2.1: Xây dựng EnrollmentService, logic ghi danh và kiểm tra quyền
##### Đại lý phụ được giao: Coder
##### Thành phần và yêu cầu kỹ thuật được nhắm tới:
* **Đường dẫn mục tiêu**: `./sources/backend.enrollment/src/main/java/com/membershiphub/enrollment/EnrollmentService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-010], [REQ-011], [ARC-007], [ARC-008], [ARC-009], [DAT-005], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 2.2: Viết unit test cho EnrollmentService
##### Đại lý phụ được giao: Tester
##### Thành phần và yêu cầu kỹ thuật được nhắm tới:
* **Đường dẫn mục tiêu**: `./sources/backend.enrollment/src/test/java/com/membershiphub/enrollment/EnrollmentServiceTest.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-010], [REQ-011], [ARC-007], [ARC-008], [ARC-009], [DAT-005], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 2.3: Review EnrollmentService cho bảo mật và hiệu năng
##### Đại lý phụ được giao: Reviewer
##### Thành phần và yêu cầu kỹ thuật được nhắm tới:
* **Đường dẫn mục tiêu**: `./sources/backend.enrollment/src/main/java/com/membershiphub/enrollment/EnrollmentService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-010], [REQ-011], [ARC-007], [ARC-008], [ARC-009], [DAT-005], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

### DAY 3: XÂY DỰNG MÔ-ĐUN ĐIỂM DANH VÀ THẺ

#### SUB-TASK 3.1: Xây dựng AttendanceService và CardService, logic điểm danh bất biến và tính hợp lệ thẻ
##### Đại lý phụ được giao: Coder
##### Thành phần và yêu cầu kỹ thuật được nhắm tới:
* **Đường dẫn mục tiêu**: `./sources/backend.attendance/src/main/java/com/membershiphub/attendance/AttendanceService.java`, `./sources/backend.card/src/main/java/com/membershiphub/card/CardService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007], [ARC-008], [ARC-009], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 3.2: Viết unit test cho AttendanceService và CardService
##### Đại lý phụ được giao: Tester
##### Thành phần và yêu cầu kỹ thuật được nhắm tới:
* **Đường dẫn mục tiêu**: `./sources/backend.attendance/src/test/java/com/membershiphub/attendance/AttendanceServiceTest.java`, `./sources/backend.card/src/test/java/com/membershiphub/card/CardServiceTest.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007], [ARC-008], [ARC-009], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 3.3: Review AttendanceService và CardService cho bảo mật và hiệu năng
##### Đại lý phụ được giao: Reviewer
##### Thành phần và yêu cầu kỹ thuật được nhắm tới:
* **Đường dẫn mục tiêu**: `./sources/backend.attendance/src/main/java/com/membershiphub/attendance/AttendanceService.java`, `./sources/backend.card/src/main/java/com/membershiphub/card/CardService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-012], [REQ-013], [REQ-014], [REQ-015], [ARC-007], [ARC-008], [ARC-009], [DAT-006], [DAT-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->