# Giai đoạn 4: <!--PHASE_NAME_START-->studentCardsService<!--PHASE_NAME_END--> | Mô tả: Thiết kế, triển khai và kiểm thử dịch vụ thẻ hội viên, bao gồm định nghĩa bảng dữ liệu, DTO, API REST, logic xử lý, kiểm thử, tài liệu, và tuân thủ OWASP.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260802135007 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên Giai đoạn Kỹ thuật** | <!--PHASE_NAME_START-->studentCardsService<!--PHASE_NAME_END--> |
| **Mô tả** | Thiết kế, triển khai và kiểm thử dịch vụ thẻ hội viên, bao gồm định nghĩa bảng dữ liệu, DTO, API REST, logic xử lý, kiểm thử, tài liệu, và tuân thủ OWASP. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/02 13:50:07 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu Giai đoạn
Giai đoạn 4 tập trung vào việc xây dựng dịch vụ thẻ hội viên (`StudentCards`) cho membership‑hub. Công việc bao gồm:
- Định nghĩa bảng dữ liệu `StudentCards` (DAT-007) với các ràng buộc, chỉ mục và tính toán ngày còn lại.
- Thiết kế DTO và API REST `/studentcards` (REQ-014) đáp ứng yêu cầu hiển thị và gia hạn thẻ.
- Xây dựng lớp `StudentCardService` và `StudentCardController` với logic xử lý, tính ngày còn lại, và cập nhật thời hạn thẻ.
- Kiểm thử đơn vị và tích hợp, đảm bảo độ phủ ≥ 85 % và tuân thủ OWASP (SQLi, XSS, CSRF, CSP).
- Tài liệu API (OpenAPI/Swagger) và hướng dẫn sử dụng, lưu trữ trong `./sources/backend/studentcards/docs`.
- Đánh giá static code, bảo mật, và kiểm tra tuân thủ NFR.

## 2. Phạm vi Kỹ thuật & Giới hạn Thư mục
| Đường dẫn tuyệt đối | Mô tả |
| :--- | :--- |
| `./sources/backend/studentcards` | Dịch vụ thẻ hội viên (Java/Quarkus) |
| `./sources/backend/studentcards/src/main/java/org/nlh4j/sources/studentcards` | Package Java chính |
| `./sources/backend/studentcards/src/main/resources/db/migration` | DDL SQL migration |
| `./sources/backend/studentcards/src/main/java/org/nlh4j/sources/studentcards/dto` | DTOs |
| `./sources/backend/studentcards/src/main/java/org/nlh4j/sources/studentcards/service` | Service layer |
| `./sources/backend/studentcards/src/main/java/org/nlh4j/sources/studentcards/controller` | REST controller |
| `./sources/backend/studentcards/src/test/java/org/nlh4j/sources/studentcards` | Unit & integration tests |
| `./sources/backend/studentcards/docs` | Tài liệu API & hướng dẫn |

Endpoint chính:
- `GET /studentcards/{studentId}` – lấy thông tin thẻ, ngày còn lại.
- `POST /studentcards/{studentId}/extend` – gia hạn thẻ, cập nhật `issueDate` và `validityDays`.

## 3. Hướng dẫn Đặc thù cho Mỗi Agent
- **Coder**: Viết mã nguồn Java, DDL, DTO, service, controller, và test. Tuân thủ quy tắc OWASP, sử dụng prepared statements, và kiểm tra bảo mật.
- **Tester**: Viết unit tests (JUnit 5) và integration tests (REST Assured). Đảm bảo coverage ≥ 85 % và kiểm tra các trường hợp ngoại lệ.
- **Reviewer**: Thực hiện static code analysis (SonarQube), kiểm tra tuân thủ OWASP, và rà soát cú pháp Java.
- **Doc**: Tạo tài liệu API (OpenAPI/Swagger) và hướng dẫn sử dụng, lưu trữ trong `docs`.
- **Docker / GCP / GKE**: Không áp dụng trong giai đoạn này.

## 4. Định nghĩa Hoàn thành (DoD)
- Bảng `StudentCards` được tạo thành công trong PostgreSQL (DAT-007).
- API `/studentcards` đáp ứng yêu cầu [REQ-014] với mã trạng thái HTTP phù hợp.
- Service và controller tuân thủ OWASP (SQLi, XSS, CSRF, CSP) và được kiểm tra static code.
- Unit test coverage ≥ 85 % cho `StudentCardService`; integration test coverage ≥ 80 % cho `StudentCardController`.
- Tài liệu API và hướng dẫn sử dụng hoàn chỉnh, lưu trữ trong `docs`.
- 100 % tag ID được map trong logs.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: TẠO BẢNG VÀ ĐỊNH NGHĨA DDL

#### SUB-TASK 1.1: Xây dựng file DDL cho bảng StudentCards
##### Được giao Agent: Coder
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/src/main/resources/db/migration/V001__create_studentcards_table.sql`
* **Thẻ Định danh**: <!--START_TAGS-->[DAT-007]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[DAT-007]<!--END_TAGS-->

#### SUB-TASK 1.2: Định nghĩa constraints và index
##### Được giao Agent: Coder
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/src/main/resources/db/migration/V001__create_studentcards_table.sql`
* **Thẻ Định danh**: <!--START_TAGS-->[DAT-007]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[DAT-007]<!--END_TAGS-->

### DAY 2: XÂY ĐỀ CẤP DTO & API CONTRACT

#### SUB-TASK 2.1: Tạo DTO StudentCardResponse
##### Được giao Agent: Coder
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/src/main/java/org/nlh4j/sources/studentcards/dto/StudentCardResponse.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-014]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

#### SUB-TASK 2.2: Xây dựng API contract JSON cho GET và POST
##### Được giao Agent: Coder
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/src/main/java/org/nlh4j/sources/studentcards/controller/StudentCardController.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-014]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

### DAY 3: XÂY ĐỀ CẤP SERVICE & CONTROLLER

#### SUB-TASK 3.1: Triển khai StudentCardService với logic tính ngày còn lại
##### Được giao Agent: Coder
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/src/main/java/org/nlh4j/sources/studentcards/service/StudentCardService.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-014], [DAT-007]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014], [DAT-007]<!--END_TAGS-->

#### SUB-TASK 3.2: Xây dựng StudentCardController với endpoint GET/POST
##### Được giao Agent: Coder
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/src/main/java/org/nlh4j/sources/studentcards/controller/StudentCardController.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-014], [DAT-007]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014], [DAT-007]<!--END_TAGS-->

### DAY 4: KIỂM THỬ ĐƠN VỊ

#### SUB-TASK 4.1: Viết unit test cho StudentCardService
##### Được giao Agent: Tester
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/src/test/java/org/nlh4j/sources/studentcards/service/StudentCardServiceTest.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-014]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

### DAY 5: KIỂM THỬ TÍNH TỔNG, RÀU SOÁT, VÀ TÀI LIỆU

#### SUB-TASK 5.1: Viết integration test cho StudentCardController
##### Được giao Agent: Tester
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/src/test/java/org/nlh4j/sources/studentcards/controller/StudentCardControllerIT.java`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-014]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

#### SUB-TASK 5.2: Thực hiện static code review và OWASP kiểm tra
##### Được giao Agent: Reviewer
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/src/main/java/org/nlh4j/sources/studentcards`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-014]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->

#### SUB-TASK 5.3: Tạo tài liệu API và hướng dẫn sử dụng
##### Được giao Agent: Doc
##### Thành phần & Yêu cầu kỹ thuật:
* **Đường dẫn**: `./sources/backend/studentcards/docs/studentcards_api.md`
* **Thẻ Định danh**: <!--START_TAGS-->[REQ-014]<!--END_TAGS-->
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-014]<!--END_TAGS-->