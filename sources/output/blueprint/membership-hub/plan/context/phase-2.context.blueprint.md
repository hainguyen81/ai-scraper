# Giai đoạn 2: <!--PHASE_NAME_START-->phase2WebInterface<!--PHASE_NAME_END--> | Mô tả: Thiết kế, triển khai giao diện web cho membership-hub, bao gồm hiển thị danh sách khóa học, xử lý thông báo đẩy, và bảo mật OWASP cho toàn bộ frontend.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260802135007 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên Giai đoạn Kỹ thuật** | <!--PHASE_NAME_START-->phase2WebInterface<!--PHASE_NAME_END--> |
| **Mô tả** | Thiết kế, triển khai giao diện web cho membership-hub, bao gồm hiển thị danh sách khóa học, xử lý thông báo đẩy, và bảo mật OWASP cho toàn bộ frontend. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/02 13:50:07 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu Giai đoạn
Giai đoạn 2 tập trung vào việc xây dựng toàn bộ giao diện web của membership-hub, bao gồm:
- Tạo và duy trì schema dữ liệu `courses` (DDL) để phục vụ frontend.
- Phát triển component `CourseList` hiển thị danh sách khóa học, lấy dữ liệu từ API `/courses`.
- Tích hợp hệ thống thông báo đẩy (FCM/APNs) qua component `NotificationHandler`.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP (XSS, CSRF, CSP, token management).
- Viết unit và integration tests, thực hiện static code review, và chuẩn bị tài liệu kỹ thuật.

## 2. Phạm vi Kỹ thuật & Giới hạn Thư mục
| Đường dẫn tuyệt đối | Mô tả |
| :--- | :--- |
| `./sources/frontend/web/migrations` | Tập tin DDL SQL cho bảng `courses`. |
| `./sources/frontend/web/components` | Các component React: `CourseList.js`, `NotificationHandler.js`. |
| `./sources/frontend/web/pages` | Trang `CoursesPage.js`, `NotificationPage.js`. |
| `./sources/frontend/web/security` | Kiểm tra OWASP: `OWASPCompliance.js`. |
| `./sources/frontend/web/components/__tests__` | Unit tests cho component. |
| `./sources/frontend/web/pages/__tests__` | Integration tests cho trang. |
| `./sources/frontend/web/docs` | Tài liệu kỹ thuật. |

## 3. Hướng dẫn Đặc thù cho Sub-Agent
| Agent | Trách nhiệm |
| :--- | :--- |
| **Coder** | Viết mã nguồn frontend, DDL, và các component. |
| **Tester** | Viết và chạy unit/integration tests, xác thực tính đúng đắn. |
| **Reviewer** | Phân tích tĩnh, kiểm tra cú pháp, tuân thủ OWASP. |
| **Doc** | Tạo và cập nhật tài liệu kỹ thuật. |
| **Docker** | (Không áp dụng trong giai đoạn này) |
| **GCP** | (Không áp dụng trong giai đoạn này) |
| **GKE** | (Không áp dụng trong giai đoạn này) |

## 4. Định nghĩa Hoàn thành (DoD)
- Tất cả các yêu cầu `[REQ-020]`, `[REQ-021]` được triển khai đầy đủ.
- Schema `courses` được tạo và migration file tồn tại trong `./sources/frontend/web/migrations/courses.sql`.
- Tất cả component và trang đều tuân thủ OWASP: XSS, CSRF, CSP, token handling.
- Unit test coverage ≥ 85 % cho component `CourseList` và `NotificationHandler`.
- Integration test coverage ≥ 80 % cho `CoursesPage`.
- Static code review không phát hiện lỗi nghiêm trọng.
- Tài liệu kỹ thuật hoàn chỉnh trong `./sources/frontend/web/docs/README.md`.
- 100 % tag ID được map trong logs.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 4: THIẾT KẾ VÀ TRIỂN KHAI GIAO DIỆN WEB

#### SUB-TASK 4.1: Tạo file DDL cho bảng courses
##### Coder
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/web/migrations/courses.sql
* **Traceability Tag Tokens**: <!--START_TAGS-->[DAT-001]<!--END_TAGS-->

#### SUB-TASK 4.2: Tạo component CourseList.js
##### Coder
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/web/components/CourseList.js
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-020], [DAT-001]<!--END_TAGS-->

#### SUB-TASK 4.3: Tạo component NotificationHandler.js
##### Coder
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/web/components/NotificationHandler.js
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-021]<!--END_TAGS-->

#### SUB-TASK 4.4: Tích hợp API fetch courses và hiển thị danh sách
##### Coder
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/web/pages/CoursesPage.js
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-020], [DAT-001]<!--END_TAGS-->

#### SUB-TASK 4.5: Tích hợp push notification listener và hiển thị toast
##### Coder
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/web/pages/NotificationPage.js
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-021]<!--END_TAGS-->

#### SUB-TASK 4.6: Kiểm tra OWASP XSS, CSRF, CSP, và bảo mật token
##### Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/web/security/OWASPCompliance.js
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-020], [REQ-021]<!--END_TAGS-->

#### SUB-TASK 4.7: Viết unit tests cho CourseList và NotificationHandler
##### Tester
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/web/components/__tests__/CourseList.test.js;./sources/frontend/web/components/__tests__/NotificationHandler.test.js
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-020], [REQ-021]<!--END_TAGS-->

#### SUB-TASK 4.8: Viết integration test cho CoursesPage
##### Tester
##### Targeted Components & Technical Requirements:
* **Target Path**: INTEGRATION_SCOPE;./sources/frontend/web/pages/CoursesPage.test.js
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-020]<!--END_TAGS-->

#### SUB-TASK 4.9: Review code static analysis
##### Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/web
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-020], [REQ-021]<!--END_TAGS-->

#### SUB-TASK 4.10: Compile documentation
##### Doc
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/frontend/web/docs/README.md
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-020], [REQ-021]<!--END_TAGS-->