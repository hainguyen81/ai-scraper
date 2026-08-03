# Giai đoạn 1: <!--PHASE_NAME_START-->authUserCenterSetup<!--PHASE_NAME_END--> | Mô tả: Thiết lập xác thực, quản lý người dùng và trung tâm, bao gồm đăng ký, đăng nhập, phân quyền, CRUD trung tâm, và cấu hình JWT, OAuth2, cùng các biện pháp bảo mật OWASP.

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260803170121 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 1 |
| **Tên giai đoạn kỹ thuật** | <!--PHASE_NAME_START-->authUserCenterSetup<!--PHASE_NAME_END--> |
| **Mô tả** | Thiết lập xác thực, quản lý người dùng và trung tâm, bao gồm đăng ký, đăng nhập, phân quyền, CRUD trung tâm, và cấu hình JWT, OAuth2, cùng các biện pháp bảo mật OWASP. |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/03 17:01:21 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và mục tiêu của giai đoạn
Giai đoạn 1 triển khai toàn bộ chức năng xác thực, quản lý người dùng và quản lý trung tâm. Các thành phần chính bao gồm:
- **Auth**: đăng ký, đăng nhập, OAuth2 (Firebase, Google, Facebook), phát JWT, refresh token, exception handling, bảo mật OWASP.
- **User**: CRUD người dùng, phân quyền (System Admin, Center Admin, Manager, Teacher, Student), lưu trữ bảng USERS & ROLES.
- **Center**: CRUD trung tâm, gán/huỷ Center Admin, lưu trữ bảng CENTERS.
- **Database**: DDL cho USERS, ROLES, CENTERS, các ràng buộc khóa ngoại.
- **Testing**: Unit test cho AuthService, UserService, CenterService.
- **Review**: Kiểm tra tuân thủ OWASP, static analysis, audit logging.
- **Documentation**: API spec, data model, deployment guide.

## 2. Phạm vi kỹ thuật và ranh giới thư mục
| Đường dẫn thư mục | Mô tả |
| :--- | :--- |
| `./sources/backend.auth/` | Các lớp dịch vụ, controller, repository, cấu hình JWT, OAuth2. |
| `./sources/backend.user/` | UserService, RoleService, UserRepository, DTOs. |
| `./sources/backend.center/` | CenterService, CenterRepository, DTOs. |
| `./sources/backend.auth/src/main/java/...` | Đường dẫn Java package `org.nlh4j.saas.membershiphub.auth`. |
| `./sources/backend.user/src/main/java/...` | Đường dẫn Java package `org.nlh4j.saas.membershiphub.user`. |
| `./sources/backend.center/src/main/java/...` | Đường dẫn Java package `org.nlh4j.saas.membershiphub.center`. |
| Endpoints | `/api/auth/register`, `/api/auth/login`, `/api/users`, `/api/centers`. |

## 3. Hướng dẫn chức năng của các đại lý phụ
- **Coder**: Xây dựng các lớp dịch vụ, controller, repository, cấu hình bảo mật, DDL, exception handlers.
- **Tester**: Viết unit test cho các dịch vụ, kiểm tra tính đúng đắn, độ an toàn, và độ tin cậy.
- **Reviewer**: Kiểm tra tuân thủ OWASP, static analysis, audit logging, bảo mật dữ liệu.
- **Doc**: Tạo tài liệu API, mô hình dữ liệu, hướng dẫn triển khai, ghi chú bảo mật.

## 4. Định nghĩa Hoàn thành (DoD)
- 100% coverage test cho AuthService, UserService, CenterService.
- Tất cả các yêu cầu [REQ-001]–[REQ-006], [ARC-001]–[ARC-006], [DAT-001], [DAT-003], [EXC-004] được triển khai và kiểm tra.
- Đảm bảo tuân thủ OWASP Top 10, bảo mật JWT, refresh token, logging audit.
- DDL được áp dụng thành công trên PostgreSQL, các ràng buộc khóa ngoại hoạt động.
- Tất cả tag ID được ánh xạ đầy đủ, không còn tag chưa được triển khai.

## 5. Nhật ký thực thi kiến trúc theo ngày

### DAY 1: XUẤT HIỆN HỆ THỐNG XÁC THỰC

#### SUB-TASK 1.1: Xây dựng AuthService, JWTProvider, OAuth2Config
##### Đối tượng phụ được giao: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 1.2: Xây dựng AuthController, exception handler
##### Đối tượng phụ được giao: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthController.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 1.3: Tài liệu API Auth
##### Đối tượng phụ được giao: Doc
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.auth/docs/AuthAPI.md`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

### DAY 2: XUẤT HIỆN QUẢN LÝ NGƯỜI DÙNG VÀ TRUNG TÂM

#### SUB-TASK 2.1: Xây dựng UserService, RoleService, UserRepository
##### Đối tượng phụ được giao: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.user/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [DAT-001], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 2.2: Xây dựng CenterService, CenterRepository
##### Đối tượng phụ được giao: Coder
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.center/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [DAT-003], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 2.3: Tài liệu mô hình dữ liệu Users, Roles, Centers
##### Đối tượng phụ được giao: Doc
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.user/docs/DataModel.md`
* **Thẻ theo dõi**: <!--START_TAGS-->[DAT-001], [DAT-003]<!--END_TAGS-->

### DAY 3: THỰC HIỆN KIỂM THỬ VÀ ĐÁNH GIÁ BẢO MẬT

#### SUB-TASK 3.1: Viết unit test cho AuthService, UserService, CenterService
##### Đối tượng phụ được giao: Tester
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.auth/src/test/java/org/nlh4j/saas/membershiphub/auth/AuthServiceTest.java;./sources/backend.user/src/test/java/org/nlh4j/saas/membershiphub/user/UserServiceTest.java;./sources/backend.center/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [DAT-001], [DAT-003], [EXC-004], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 3.2: Kiểm tra tuân thủ OWASP, static analysis
##### Đối tượng phụ được giao: Reviewer
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend.auth/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthService.java;./sources/backend.user/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java;./sources/backend.center/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java`
* **Thẻ theo dõi**: <!--START_TAGS-->[NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->

#### SUB-TASK 3.3: Hoàn thiện tài liệu triển khai và bảo mật
##### Đối tượng phụ được giao: Doc
##### Thành phần và yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./docs/DeploymentGuide.md`
* **Thẻ theo dõi**: <!--START_TAGS-->[ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [NFR-001], [NFR-003], [NFR-005], [NFR-006], [NFR-007], [NFR-008]<!--END_TAGS-->