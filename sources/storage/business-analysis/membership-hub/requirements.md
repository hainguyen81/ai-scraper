## 1. Tổng quan dự án & Kiến trúc toàn cục

- **Mục tiêu sản phẩm & giá trị cốt lõi**
  - Cung cấp nền tảng thống nhất quản lý hội viên đa trung tâm.
  - Cho phép chấm công thời gian thực qua quét QR.
  - Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
  - Hỗ trợ truyền thông đa kênh (web, mobile, nhóm Zalo).
  - Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

- **Đối tượng người dùng mục tiêu**
  - Quản trị viên hệ thống (toàn quyền siêu cấp)
  - Quản trị viên trung tâm (quyền hạn trong trung tâm)
  - Quản lý (phụ trách, quyền hạn giới hạn)
  - Giáo viên (chỉ xem lịch giảng và danh sách học viên)
  - Học viên (duyệt khóa học, ghi danh, xem thẻ hội viên)
  - Người dùng ứng dụng di động (giao diện đáp ứng cho tất cả vai trò trên)

- **Ma trận RBAC toàn cục**
  - [ARC-001] **System Admin**: toàn bộ quyền trên tất cả trung tâm.
  - [ARC-002] **Center Admin**: toàn bộ quyền trong trung tâm của mình, không thể tác động đến trung tâm khác.
  - [ARC-003] **Manager**: có thể tạo thông báo, quản lý học viên, gán học viên vào khóa học hiện có, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
  - [ARC-004] **Teacher**: xem khóa học của mình, danh sách học viên, lịch giảng; chỉ đọc.
  - [ARC-005] **Student**: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên cá nhân (ngày hiệu lực còn lại), gia hạn thẻ.

- **Kiến trúc & luồng dữ liệu**
  - [ARC-006] **Luồng xác thực**: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT (hết hạn 15 phút) và refresh token.
  - [ARC-007] **Luồng xử lý chấm công QR**: ứng dụng di động quét QR, gửi studentID và timestamp đến backend; dịch vụ xác thực và ghi nhận chấm công một cách idempotent.
  - [ARC-008] **Luồng gửi thông báo**: hệ thống kích hoạt push notification đến ứng dụng di động và đăng thông báo lên nhóm Zalo được chỉ định cho các sự kiện: thông báo, chỉ định khóa học, cảnh báo chấm công.
  - [ARC-009] **Luồng tích hợp backend ứng dụng di động**: frontend Next.js tiêu thụ REST APIs; xác thực qua bearer token; hỗ trợ caching offline cho trường hợp mất kết nối.
  - [ARC-010] **Blueprint công nghệ & hạn chế hạ tầng**: 
    - Ngôn ngữ/backend: Java/Kotlin (Quarkus) triển khai trên Kubernetes (GKE).
    - Database: PostgreSQL với read‑replica cho reporting.
    - Message queue: Kafka cho các sự kiện thông báo.
    - Lưu trữ: object storage (GCS) cho file báo cáo CSV.
    - CI/CD: GitHub Actions với bảo mật đa lớp.
    - Container: Docker với base image < 200 MB, final image < 500 MB.
    - Multi‑tenant: mỗi trung tâm được cô lập qua schema/database riêng hoặc hàng rào dữ liệu.
    - Observability: Prometheus + Grafana, Loki logging.

## 2. Các module chức năng

### 2.1 Quản lý người dùng

#### [REQ-001] Đăng ký người dùng
*As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.*

**Acceptance Criteria**
- Given a user provides a unique email, a strong password, and agrees to terms, When they submit the registration form, Then the system validates the input, creates a new user record with role “Student” (or “Teacher” if invited), and returns a success response with a JWT token. *[REQ-001]*

**Data Inputs & Field Validations**
- **Email**: bắt buộc, tối đa 255 ký tự, phải chứa đúng một ký tự “@” và phần tên miền hợp lệ (ví dụ user@example.com). Phải là duy nhất.
- **Password**: bắt buộc, ít nhất 8 ký tự, bao gồm ít nhất một chữ hoa, một chữ thường, một chữ số, một ký tự đặc biệt.
- **Terms**: checkbox chấp nhận điều khoản, bắt buộc.

#### [REQ-002] Xác thực xã hội
*As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth so that I can leverage existing credentials.*

**Acceptance Criteria**
- Given a user selects a social provider, When they authenticate through the provider’s popup, Then the system receives an OAuth2 code, exchanges it for user info, creates or updates the local user record, and issues a JWT token. *[REQ-002]*

**Data Inputs**
- Mã thông báo từ nhà cung cấp OAuth2.
- Hình ảnh hồ sơ tùy chọn.

#### [REQ-003] Phân quyền người dùng
*As an administrator, I want to assign or change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) so that permissions are correctly enforced.*

**Acceptance Criteria**
- Given an admin selects a user and a new role, When the assignment is confirmed, Then the user’s role column is updated, and appropriate permissions are applied immediately. *[REQ-003]*

**Data Inputs**
- Trường chọn vai trò.
- Bắt buộc ghi nhật ký kiểm toán cho mỗi thay đổi vai trò.

### 2.2 Quản lý trung tâm

#### [REQ-004] Xem danh sách trung tâm
*As any authenticated user, I want to see a list of all centers with address, tax ID, and admin contact so that I can identify relevant centers.*

**Acceptance Criteria**
- Given a user navigates to trang Centers, When the request completes, Then một bảng hiển thị các trung tâm (Name, Address, TaxID, AdminContact) được hiển thị. *[REQ-004]*

#### [REQ-005] Tạo/Cập nhật/Xóa trung tâm
*As a System Admin, I want to add, edit, or remove a center record so that center information stays current.*

**Acceptance Criteria**
- Given a System Admin provides center name, address, tax ID, primary contact phone and email, When the save action is executed, Then the center is persisted and appears in the list; nếu trùng lặp tax ID, thao tác thất bại với lỗi xung đột. *[REQ-005]*

**Data Inputs**
- **Name**: bắt buộc, tối đa 100 ký tự.
- **Address**: bắt buộc, tối đa 255 ký tự.
- **TaxID**: bắt buộc, số, 10‑13 chữ số, duy nhất.
- **Contact Phone**: tùy chọn, có thể bao gồm +, chữ số, dấu cách, gạch ngang, ngoặc đơn.
- **Contact Email**: tùy chọn, phải là định dạng email hợp lệ.

#### [REQ-006] Phân công quản trị viên trung tâm
*As a System Admin, I want to assign or unassign a user as a Center Admin for a specific center so that administrative control is delegated.*

**Acceptance Criteria**
- Given a System Admin chọn một người dùng và một trung tâm, Khi xác nhận hành động, Sau đó vai trò người dùng được đặt thành “Center Admin” và ID trung tâm được ghi lại; thao tác hủy bỏ đảo ngược hành động. *[REQ-006]*

**Data Inputs**
- ID người dùng.
- ID trung tâm.

### 2.3 Quản lý khóa học

#### [REQ-007] Xem danh sách khóa học
*As any authenticated user, I want to see all courses with schedule and assigned teacher so that I can browse offerings.*

**Acceptance Criteria**
- Given a user truy cập trang Courses, Khi yêu cầu hoàn tất, Sau đó một lưới hiển thị CourseID, Title, StartDate, EndDate, TeacherName được hiển thị. *[REQ-007]*

#### [REQ-008] Tạo/Cập nhật/Xóa khóa học (Tránh xung đột lịch)
*As a System Admin or Center Admin, I want to manage courses (add, edit, remove) while ensuring no overlapping schedules for the same teacher or venue.*

**Acceptance Criteria**
- Given an admin cung cấp CourseTitle, StartDate, EndDate, TeacherID, Khi kích hoạt hành động lưu, Sau đó hệ thống xác thực rằng giáo viên không có lịch trình khác chồng lấn với các ngày này; nếu xung đột, lỗi được trả về; ngược lại khóa học được lưu. *[REQ-008]*

**Data Inputs**
- **Title**: bắt buộc, tối đa 150 ký tự.
- **StartDate/EndDate**: bắt buộc, EndDate >= StartDate.
- **TeacherID**: bắt buộc, khóa ngoại.
- Logic kiểm tra chồng lấn được thực thi ở mức DB/trigger.

#### [REQ-009] Chỉ định giáo viên cho khóa học
*As a System Admin, I want to assign or unassign teachers to courses so that teaching responsibilities are updated.*

**Acceptance Criteria**
- Given an admin chọn một khóa học và một giáo viên, Khi hành động chỉ định được thực thi, Sau đó ánh xạ giáo viên-khóa học được tạo và một thông báo được xếp hàng cho ứng dụng di động của giáo viên; thao tác hủy bỏ xóa ánh xạ. *[REQ-009]*

**Data Inputs**
- CourseID (bắt buộc).
- TeacherID (bắt buộc, phải tồn tại).

### 2.4 Đăng ký & ghi danh học viên

#### [REQ-010] Duyệt khóa học
*As a Student, I want to browse available courses (excluding those already enrolled) so that I can select courses to join.*

**Acceptance Criteria**
- Given a Student đăng nhập và truy cập trang Browse Courses, Khi yêu cầu hoàn tất, Sau đó một danh sách các khóa học với sức chứa và lịch trình được hiển thị, loại trừ các khóa học mà học viên đã có bản ghi ghi danh. *[REQ-010]*

#### [REQ-011] Đăng ký khóa học của học viên
*As a Student, I want to register for a course (existing or new), which auto‑creates a Student account if missing, and assigns the student to the course.*

**Acceptance Criteria**
- Given a Student chọn một khóa học và gửi đăng ký, Khi backend xử lý yêu cầu, Sau đó một bản ghi ghi danh mới được tạo; nếu học viên không có tài khoản cục bộ, một tài khoản được tạo với vai trò “Student”; một thông báo được xếp hàng cho ứng dụng di động của học viên và nhóm Zalo của trung tâm. *[REQ-011]*

**Data Inputs**
- **CourseID**: bắt buộc, phải là khóa học đang hoạt động.
- **StudentID**: được suy ra từ token xác thực (hoặc được tạo trên‑fly).

### 2.5 Chấm công & quét QR

#### [REQ-012] Ghi nhận chấm công qua QR
*As a Student (via mobile app), I want to scan a QR code at class start so that my attendance is recorded for the current day.*

**Acceptance Criteria**
- Given a Student mở máy quét, quét một QR hợp lệ của khóa học và xác nhận chấm công, Khi API nhận được payload, Sau đó hệ thống xác thực mối quan hệ học viên-khóa học, tạo một bản ghi Attendance với timestamp, và trả về phản hồi thành công; các lần quét trùng lặp trong cùng ngày bị bỏ qua. *[REQ-012]*

**Data Inputs**
- **QR payload**: chuỗi base64 chứa studentID và courseID.
- **Validation**: học viên phải được ghi danh vào khóa học cho ngày hiện tại.

#### [REQ-013] Tính bất biến khi chấm công
*Luồng chấm công phải đảm bảo rằng nhiều lần quét từ cùng một học viên cho cùng một khóa học trong cùng một ngày tạo ra một bản ghi duy nhất.*

**Acceptance Criteria**
- Given a student scans a QR twice trong vòng một phút, Khi dịch vụ xử lý cả hai yêu cầu, Sau đó chỉ một hàng Attendance được tạo; các yêu cầu tiếp theo trả về thành công với cờ “duplicate”. *[REQ-013]*

**Data Inputs**
- Khóa duy nhất (StudentID, CourseID, Date).

### 2.6 Quản lý thẻ hội viên

#### [REQ-014] Hiển thị tính hợp lệ của thẻ
*As a Student, I want to view my membership card showing remaining validity days so that I know when renewal is needed.*

**Acceptance Criteria**
- Given a Student mở trang Card, Khi yêu cầu tải, Sau đó giao diện hiển thị tổng số ngày hiệu lực, ngày đã sử dụng, ngày còn lại; dữ liệu được lấy từ thực thể StudentCard. *[REQ-014]*

#### [REQ-015] Gia hạn thẻ hội viên
*As a Student, I want to extend my membership card validity by paying a fee, which updates the end date.*

**Acceptance Criteria**
- Given a Student chọn một khoảng thời gian gia hạn (ví dụ 30 ngày), xác nhận thanh toán, Khi dịch vụ thanh toán xác nhận thành công, Sau đó EndDate của StudentCard được gia hạn thêm các ngày đã chọn và một thông báo xác nhận được gửi. *[REQ-015]*

**Data Inputs**
- **RenewalDays**: số nguyên, từ 1 đến 365.
- Tích hợp cổng thanh toán (ngoài phạm vi).

### 2.7 Thông báo & truyền thông

#### [REQ-016] Kích hoạt thông báo
*Khi quản trị viên tạo thông báo, chỉ định giáo viên cho khóa học, hoặc ghi danh học viên, hệ thống phải tạo một thông báo đến ứng dụng di động của học viên và đăng thông báo lên nhóm Zalo được chỉ định.*

**Acceptance Criteria**
- Given an admin thực hiện một hành động yêu cầu thông báo, Khi hành động được lưu, Sau đó một bản ghi Notification được tạo, một payload push notification được xếp hàng cho ứng dụng di động, và một tin nhắn được gửi đến nhóm chat Zalo. *[REQ-016]*

**Data Inputs**
- Đối tượng mục tiêu (học viên, giáo viên, nhóm).
- Nội dung thông báo, phương tiện tùy chọn.

### 2.8 Quản lý khuyến mãi & thông báo

#### [REQ-017] Quản lý khuyến mãi
*As a Center Admin or Manager, I want to create, edit, or delete promotions (discounts, offers) with start/end dates so that students can see applicable deals.*

**Acceptance Criteria**
- Given an admin cung cấp PromotionName, description, conditions, startDate, endDate, Khi lưu, Sau đó khuyến mãi xuất hiện trong danh sách hiển thị cho học viên; nếu endDate bị bỏ qua, khuyến mãi được coi là vĩnh viễn. *[REQ-017]*

**Data Inputs**
- **Name**: bắt buộc, tối đa 100 ký tự.
- **StartDate/EndDate**: tùy chọn, định dạng YYYY‑MM‑DD.
- **Description**: tối đa 500 ký tự.

#### [REQ-018] Quản lý thông báo
*As a Center Admin or Manager, I want to create, edit, or delete announcements with optional expiry dates for broadcast to all users.*

**Acceptance Criteria**
- Given an admin nhập AnnouncementTitle, content, tùy chọn expiry, Khi lưu, Sau đó thông báo được hiển thị trên toàn trang web; nếu expiry được đặt, nó tự động biến mất sau ngày đó. *[REQ-018]*

**Data Inputs**
- **Title**: bắt buộc, tối đa 150 ký tự.
- **Content**: bắt buộc, tối đa 2000 ký tự.

### 2.9 Chatbot dịch vụ khách hàng AI

#### [REQ-019] Tích hợp chatbot AI
*As any user, I want to interact with an AI chatbot that can answer common queries about courses, teachers, centers, and account status.*

**Acceptance Criteria**
- Given a user mở widget chat, Khi họ đặt câu hỏi, Sau đó AI trả về một câu trả lời phù hợp hoặc chuyển đến hỗ trợ con người nếu độ tin cậy thấp. *[REQ-019]*

**Data Inputs**
- Văn bản đầu vào từ người dùng.
- Thời gian timeout phiên (ví dụ 5 phút).

### 2.10 Tính năng cốt lõi ứng dụng di động

#### [REQ-020] Giao diện người dùng di động theo vai trò
*As a mobile user, I want a responsive UI that mirrors web functionality for my assigned role (Student, Teacher, Admin, etc.).*

**Acceptance Criteria**
- Given a user đăng nhập trên Android hoặc iOS, Khi ứng dụng tải, Sau đó menu điều hướng thích hợp và các màn hình được hiển thị dựa trên vai trò của người dùng. *[REQ-020]*

#### [REQ-021] Thông báo đẩy trên di động
*As a registered user, I want to receive push notifications on my mobile device for attendance confirmations, new announcements, and reminder messages.*

**Acceptance Criteria**
- Given a backend event kích hoạt thông báo, Khi token thiết bị được đăng ký, Sau đó thông báo được phân phối qua Firebase Cloud Messaging (FCM) hoặc APNs. *[REQ-021]*

**Data Inputs**
- **DeviceToken**: chuỗi token duy nhất.
- **Platform**: enum (iOS/Android).

### 2.11 Bản địa hóa & SEO

#### [REQ-022] Phát hiện ngữ cảnh mặc định
*As a visitor, I want the system to use my previously selected language preference, falling back to browser settings, for a personalized experience.*

**Acceptance Criteria**
- Given a user truy cập trang web, Khi hệ thống đánh giá ngữ cảnh, Sau đó nó chọn ngôn ngữ đã lưu nếu có; nếu không sử dụng header Accept‑Language; giao diện được cập nhật tương ứng. *[REQ-022]*

#### [REQ-023] SEO đa ngôn ngữ
*Nền tảng phải hỗ trợ SEO cho ít nhất tiếng Anh, tiếng Việt, và tiếng Tây Ban Nha; mỗi trang phải bao gồm thẻ meta language-specific và các thuộc tính hreflang.*

**Acceptance Criteria**
- Given a page được yêu cầu với một locale cụ thể, Khi trang được render, Sau đó HTML bao gồm một thẻ <html lang='en'> và các liên kết hreflang trỏ đến các phiên bản ngôn ngữ thay thế. *[REQ-023]*

**Data Inputs**
- Mã ngôn ngữ (en, vi, es).

### 2.12 Báo cáo & phân tích

#### [REQ-024] Tạo báo cáo chấm công
*As an admin, I want to generate a daily attendance report for a center (CSV) showing each student’s presence status.*

**Acceptance Criteria**
- Given an admin chọn một trung tâm và khoảng thời gian, Khi báo cáo được yêu cầu, Sau đó một tệp CSV được tạo với các cột: StudentName, CourseName, AttendanceDate, Status. *[REQ-024]*

**Data Inputs**
- Khoảng thời gian: start ≤ end, tối đa 30 ngày.

#### [REQ-025] Bảng điều khiển tổng quan ghi danh
*As a Center Admin, I want a real‑time dashboard summarizing total students, active courses, and upcoming sessions.*

**Acceptance Criteria**
- Given an admin mở bảng điều khiển, Khi dữ liệu được làm mới, Sau đó các thẻ hiển thị totalStudents, activeCourses, upcomingSessions (7‑ngày tiếp theo). *[REQ-025]*

**Data Inputs**
- Khoảng thời gian làm mới (có thể cấu hình, mặc định 15 phút).

## 3. Luồng ngoại lệ và trường hợp đặc biệt

- **[EXC-001]** Network & Connectivity Drops During QR Scan:
  - Nếu một học viên quét QR nhưng mạng không khả dụng, Khi ứng dụng thử lại sau khi kết nối, Sau đó chấm công được ghi nhận một khi dịch vụ khả dụng.

- **[EXC-002]** Duplicate Attendance Submission:
  - Nếu cùng một học viên quét cùng một QR nhiều lần trong cùng một ngày, Khi hệ thống phát hiện trùng lặp, Sau đó nó trả về thành công với cờ “already recorded” và không tạo thêm hàng.

- **[EXC-003]** Failed Notification Delivery:
  - Khi một push notification không thể gửi (ví dụ: token thiết bị không hợp lệ), Sau đó hệ thống ghi lại lỗi và lên lịch thử lại tối đa ba lần trước khi đánh dấu là thất bại.

- **[EXC-004]** Invalid Input Validation (ví dụ: email sai định dạng, thiếu trường bắt buộc):
  - Nếu xác thực thất bại khi gửi biểu mẫu, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu sửa.

- **[EXC-005]** System Recovery After Outage:
  - Nếu dịch vụ không khả dụng, Khi nó khôi phục, Sau đó bất kỳ quét QR chờ xử lý nào được xử lý theo thứ tự FIFO, và người dùng nhận được thông báo về các sự kiện đã khôi phục.

## 4. Từ điển dữ liệu

| Entity | Field | Data Type | Constraints | Description |
|--------|-------|-----------|-------------|-------------|
| **Users** | **[DAT-001]** user_id | UUID | PK, NOT NULL | Unique identifier |
| | **[DAT-002]** email | VARCHAR(255) | NOT NULL, UNIQUE | Primary login identifier |
| | **[DAT-003]** password_hash | CHAR(60) | NOT NULL | bcrypt hash |
| | **[DAT-004]** full_name | VARCHAR(100) | NOT NULL | Real name |
| | **[DAT-005]** role_id | SMALLINT | FK → Roles.role_id | Assigned role |
| | **[DAT-006]** provider | ENUM('local','firebase','google','facebook') | DEFAULT 'local' | Auth provider |
| | **[DAT-007]** created_at | TIMESTAMP | NOT NULL, DEFAULT now() | Account creation |
| | **[DAT-008]** updated_at | TIMESTAMP | NOT NULL, DEFAULT now() | Last update |
| **Centers** | **[DAT-009]** center_id | UUID | PK, NOT NULL | Unique identifier |
| | **[DAT-010]** name | VARCHAR(100) | NOT NULL | Center name |
| | **[DAT-011]** address | VARCHAR(255) | NOT NULL | Physical address |
| | **[DAT-012]** tax_id | VARCHAR(20) | UNIQUE, NOT NULL | Tax identification number |
| | **[DAT-013]** contact_phone | VARCHAR(20) | OPTIONAL | Contact telephone |
| | **[DAT-014]** contact_email | VARCHAR(100) | OPTIONAL | Contact email |
| **Courses** | **[DAT-015]** course_id | UUID | PK, NOT NULL | Unique identifier |
| | **[DAT-016]** title | VARCHAR(150) | NOT NULL | Course name |
| | **[DAT-017]** description | TEXT | OPTIONAL | Detailed description |
| | **[DAT-018]** start_date | DATE | NOT NULL | Course start |
| | **[DAT-019]** end_date | DATE | NOT NULL | Course end |
| | **[DAT-020]** teacher_id | UUID | FK → Users.user_id | Assigned teacher |
| | **[DAT-021]** max_students | INT | DEFAULT 30 | Capacity |
| **Enrollments** | **[DAT-022]** enrollment_id | UUID | PK, NOT NULL | Unique identifier |
| | **[DAT-023]** student_id | UUID | FK → Users.user_id | Enrolled student |
| | **[DAT-024]** course_id | UUID | FK → Courses.course_id | Course |
| | **[DAT-025]** enrollment_date | TIMESTAMP | DEFAULT now() | When enrolled |
| **Attendance** | **[DAT-026]** attendance_id | UUID | PK, NOT NULL | Unique identifier |
| | **[DAT-027]** student_id | UUID | FK → Users.user_id | Student present |
| | **[DAT-028]** course_id | UUID | FK → Courses.course_id | Course attended |
| | **[DAT-029]** attendance_date | DATE | NOT NULL | Date of attendance |
| | **[DAT-030]** timestamp | TIMESTAMP | DEFAULT now() | Exact time recorded |
| **StudentCards** | **[DAT-031]** card_id | UUID | PK, NOT NULL | Unique identifier |
| | **[DAT-032]** student_id | UUID | FK → Users.user_id | Owner |
| | **[DAT-033]** issue_date | DATE | NOT NULL | Card issue date |
| | **[DAT-034]** validity_days | INT | NOT NULL | Total validity days |
| | **[DAT-035]** remaining_days | INT | computed | Days left until expiry |
| **Notifications** | **[DAT-036]** notification_id | UUID | PK, NOT NULL | Unique identifier |
| | **[DAT-037]** user_id | UUID | FK → Users.user_id (OPTIONAL) | Target user |
| | **[DAT-038]** group_zalo | VARCHAR(50) | OPTIONAL | Target Zalo group |
| | **[DAT-039]** message | TEXT | NOT NULL | Notification content |
| | **[DAT-040]** sent_at | TIMESTAMP | DEFAULT now() | When sent |
| | **[DAT-041]** delivered | BOOLEAN | DEFAULT false | Delivery status |
| **Roles** | **[DAT-042]** role_id | SMALLINT | PK | Role identifier |
| | **[DAT-043]** name | VARCHAR(30) | UNIQUE, NOT NULL | Role name |
| | **[DAT-044]** description | VARCHAR(200) | OPTIONAL | Role description |
| **Promotions** | **[DAT-045]** promo_id | UUID | PK, NOT NULL | Unique identifier |
| | **[DAT-046]** code | VARCHAR(30) | UNIQUE | Discount code |
| | **[DAT-047]** discount_percent | SMALLINT | NOT NULL | Discount percentage |
| | **[DAT-048]** start_date | DATE | OPTIONAL | Promotion start |
| | **[DAT-049]** end_date | DATE | OPTIONAL | Promotion end |
| | **[DAT-050]** description | TEXT | OPTIONAL | Promo details |
| **Announcements** | **[DAT-051]** announcement_id | UUID | PK, NOT NULL | Unique identifier |
| | **[DAT-052]** title | VARCHAR(150) | NOT NULL | Title |
| | **[DAT-053]** content | TEXT | NOT NULL | Content |
| | **[DAT-054]** start_date | DATE | OPTIONAL | Effective start |
| | **[DAT-055]** end_date | DATE | OPTIONAL | Effective end |
| **SystemSettings** | **[DAT-056]** setting_key | VARCHAR(50) | PK | Configuration key |
| | **[DAT-057]** setting_value | TEXT | NOT NULL | Configuration value |
| | **[DAT-058]** description | VARCHAR(200) | OPTIONAL | Meaning of setting |

## 5. Yêu cầu phi chức năng

- **[NFR-001]** Performance Metrics:
  - Thời gian phản hồi lõi API (xác thực, chấm công, danh sách khóa học) ≤ 200 ms trung bình.
  - Các truy vấn cơ sở dữ liệu được lập chỉ mục để hỗ trợ đọc trong < 1 giây với 10 000 người dùng đồng thời.

- **[NFR-002]** Availability:
  - Mục tiêu 99,9 % thời gian hoạt động hàng năm; bao gồm SLA với khả năng phục hồi tự động trên nhiều cụm GKE.

- **[NFR-003]** Security:
  - Tất cả dữ liệu trong quá trình truyền phải sử dụng TLS 1.3; mã hóa AES‑256 khi lưu trữ.
  - JWT access token hết hạn sau 15 phút; refresh token có thời hạn 7‑ngày.
  - Triển khai các biện pháp đối phó OWASP Top 10 (SQL injection, XSS, CSRF).

- **[NFR-004]** Scalability & High Availability:
  - Tăng cường theo chiều ngang các dịch vụ Quarkus qua Kubernetes HPA dựa trên CPU > 70 % hoặc độ trễ yêu cầu > 300 ms.
  - Tạo bản sao PostgreSQL read‑replica cho workloads reporting.

- **[NFR-005]** Docker Image Size:
  - Hình ảnh cơ sở < 200 MB; hình ảnh cuối cùng < 500 MB.

- **[NFR-006]** Logging & Audit:
  - Ghi nhật ký mọi hành động người dùng (thay đổi vai trò, bản ghi chấm công, thông báo) với timestamp, userID, chi tiết hành động; lưu giữ 1‑năm.

- **[NFR-007]** Multi‑Language Support:
  - Chuỗi giao diện được bên ngoài hóa; hỗ trợ tiếng Anh, tiếng Việt, tiếng Tây Ban Nha; chuyển đổi locale mà không cần tải lại trang khi có thể.

- **[NFR-008]** GDPR/CCPA Compliance:
  - Xóa dữ liệu cá nhân theo yêu cầu; xuất dữ liệu ở định dạng JSON; quản lý sự đồng ý cho truyền thông tiếp thị.

- **[NFR-009]** Backup & Disaster Recovery:
  - Sao lưu PostgreSQL đầy đủ hàng ngày; phục hồi tại bất kỳ điểm nào trong 24‑giờ; sao lưu cụm GKE đến khu vực riêng biệt.

---
*Kết thúc SRS*