# SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub

## 1. TỔNG QUAN DỰ ÁN VÀ KIẾN THUẬT TOÀN CỤC

### 1.1 Mục tiêu và Giá trị cốt lõi
- Cung cấp nền tảng quản lý thành viên đa trung tâm.  
- Cho phép ghi nhận điểm danh thời gian thực thông qua mã QR.  
- Cung cấp thẻ thành viên điện tử với tính năng đếm ngày hợp lệ.  
- Hỗ trợ đa kênh truyền thông (web, mobile, nhóm Zalo).  
- Tăng cường tính tin cậy, mở rộng, bảo mật, thân thiện người dùng, hỗ trợ đa ngôn ngữ.  

### 1.2 Nhân khẩu học người dùng
- **[ARC-001]** System Admin: người dùng siêu quyền toàn cục.  
- **[ARC-002]** Center Admin: quản trị viên cấp trung tâm, chỉ thao tác trong trung tâm của mình.  
- **[ARC-003]** Manager: tạo thông báo, quản lý sinh viên, gán sinh viên cho khóa học, xem danh sách khóa học, không chỉnh sửa khóa học hoặc gán giáo viên.  
- **[ARC-004]** Teacher: xem khóa học, danh sách sinh viên, lịch học; chỉ đọc.  
- **[ARC-005]** Student: duyệt khóa học, đăng ký, xem thẻ thành viên, gia hạn ngày hợp lệ.  
- **[ARC-006]** Mobile App User: các vai trò trên nền tảng di động với giao diện đáp ứng.  

### 1.3 Ma trận RBAC
| Vai trò | Quyền |
|---------|-------|
| System Admin | [ARC-001] |
| Center Admin | [ARC-002] |
| Manager | [ARC-003] |
| Teacher | [ARC-004] |
| Student | [ARC-005] |

### 1.4 Kiến trúc và luồng dữ liệu chính
- **[ARC-006] Authentication Flow**: Hỗ trợ email/mật khẩu, Firebase, Google, Facebook OAuth2; phát JWT 15 điểm, refresh 7 ngày.  
- **[ARC-007] Attendance QR Processing Flow**: Ứng dụng di động quét QR, gửi studentID và timestamp, dịch vụ xác thực và ghi nhận điểm danh một lần duy nhất.  
- **[ARC-008] Notification Delivery Flow**: Thông báo đẩy tới ứng dụng di động và đăng bài vào nhóm Zalo cho thông báo, giao việc, cảnh báo điểm danh.  
- **[ARC-009] Mobile App Backend Integration Flow**: Next.js frontend tiêu thụ REST API, xác thực bằng bearer token, hỗ trợ lưu trữ tạm thời offline.  

## 2. PHẦN MỀM ĐƯỢC CHI TIẾP MÔ HÌNH EPIC

### 2.1 Quản lý người dùng
- **[REQ-001]** Đăng ký người dùng: *As a prospective user, I want to register using email and password (or social providers) so that I can obtain an account in the system.*  
  - **Acceptance Criteria**  
    - *Given* a user provides unique email, strong password, và đồng ý điều khoản,  
    - *When* họ submit đăng ký,  
    - *Then* hệ thống validate, tạo User với role ‘Student’, trả JWT.  
  - **[EXC-004]** Validation failures: email hợp lệ, mật khẩu mạnh, checkbox terms.  
- **[REQ-002]** Xác thực xã hội: *As a user, I want to sign‑in/up using Firebase, Google, or Facebook OAuth.*  
  - **Acceptance Criteria**  
    - *Given* user chọn provider,  
    - *When* authentication thực hiện,  
    - *Then* nhận code, trao đổi token, tạo/ cập nhật User ასეთი, phát JWT.  
  - **[EXC-004]** Validation failures: provider token missing.  
- **[REQ-003]** Phân quyền người dùng: *As an administrator, I want to assign or change a user’s role.*  
  - **Acceptance Criteria**  
    - *Given* admin chọn user và role mới,  
    - *When* xác nhận,  
    - *Then* cập nhật role, ghi audit log.  
  - **[EXC-004]** Input validation: role must be one of defined.  

**Database Tables**  
- **[DAT-001] Users**  
  ```mermaid
  erDiagram
      Users {
          VARCHAR(255) userId PK "Unique identifier"
          VARCHAR(255) email NOT NULL "Login identifier"
          CHAR(60) passwordHash NOT NULL "bcrypt hash"
          VARCHAR(100) fullName NOT NULL "Real name"
          SMALLINT roleId NOT NULL "Role"
          ENUM('local','firebase','google','facebook') provider NOT NULL "Auth provider"
          TIMESTAMP createdAt NOT NULL "Account creation"
          TIMESTAMP updatedAt NOT NULL "Last update"
      }
      Roles {
          SMALLINT roleId PK "Role identifier"
          VARCHAR(30) name NOT NULL "Role name"
          VARCHAR(200) description "Description"
      }
      Users }o--|| Roles : "roleId"
  ```
- **[DAT-008] Roles** (see above)

### 2.2 Quản lý trung tâm
- **[REQ-004]** Xem danh sách trung tâm: *As any authenticated user, I want to see a list of all centers.*  
  - **Acceptance Criteria**  
    - *Given* user vào trang Centers,  
    - *When* request hoàn thành,  
    - *Then* hiển thị bảng Name, Address, TaxID, AdminContact.  
- **[REQ-005]** Tạo/sửa/xóa trung tâm: *As a System Admin, I want to add, edit, or remove a center.*  
  - **Acceptance Criteria**  
    - *Given* admin nhập dữ liệu,  
    - *When* save,  
    - *Then* persist, nếu TaxID trùng trả lỗi conflict.  
  - **[EXC-004]** Validation: TaxID unique, numeric 10‑13 digits.  
- **[REQ-006]** Gán/huỷ quản trị trung tâm: *As a System Admin, I want to assign or unassign a user as a Center Admin.*  
  - **Acceptance Criteria**  
    - *Given* admin chọn user và center,  
    - *When* action xác nhận,  
    - *Then* role set 'Center Admin', centerId ghi.  

**Database Tables**  
- **[DAT-002] Centers**  
  ```mermaid
  erDiagram
      Centers {
          UUID centerId PK "Unique identifier"
          VARCHAR(100) name NOT NULL "Center name"
          VARCHAR(255) address NOT NULL "Physical address"
          VARCHAR(20) taxId NOT NULL "Tax ID"
          VARCHAR(20) contactPhone optional "Phone"
          VARCHAR(100) contactEmail optional "Email"
      }
  ```  

### 2.3 Quản lý khóa học
- **[REQ-007]** Xem danh sách khóa học: *As any authenticated user, I want to see all courses.*  
  - **Acceptance Criteria**  
    - *Given* user vào trang Courses,ORM,  
    - *When* request hoàn thành,  
    - *Then* hiển thị CourseID, Title, StartDate, EndDate, TeacherName.  
- **[REQ-008]** Tạo/sửa/xóa khóa học: *As a System Admin or Center Admin, I want to manage courses ensuring no overlap.*  
  - **Acceptance Criteria**  
    - *Given* admin cung cấp thông tin,  
    - *When* save,  
    - *Then* validate teacher không lịch trùng, nếu trùng trả error.  
  - **[EXC-004]** Validation: EndDate >= StartDate.  
- **[REQ-009]** Gán/huỷ giáo viên cho khóa học: *As a System Admin, I want to assign or unassign teachers.*  
  - **Acceptance Criteria**  
    - *Given* admin chọn course và teacher,  
    - *When* thực hiện,  
    - *Then* tạo bản ghi CourseTeacher, gửi notification.  

**Database Tables**  
- **[DAT-003] Courses**  
  ```mermaid
  erDiagram
      Courses {
          UUID courseId PK "Unique identifier"
          VARCHAR(150) title NOT NULL "Course name"
          TEXT description optional "Detail"
          DATE startDate NOT NULL "Start date"
          DATE endDate NOT NULL "End date"
          UUID teacherId NOT NULL "Assigned teacher"
          INT maxStudents DEFAULT 30 "Capacity"
      }
      Users }o--|| Courses : "teacherId"
  ```  

### 2.4 Đăng ký và đăng ký khóa học
- **[REQ-010]** Duyệt khóa học: *As a Student, I want to browse available courses excluding already enrolled.*  
  - **Acceptance Criteria**  
    - *Given* student vào Browse Courses,  
    - *When* request hoàn thành,  
    - *Then* hiển thị danh sách các khóa với capacity, lịch, loại trừ khóa đã đăng ký.  
- **[REQ-011]** Đăng ký khóa học: *As a Student, I want to register for a course, auto‑create account if missing.*  
  - **Acceptance Criteria**  
    - *Given* student chọn course và submit,  
    - *When* backend xử lý,  
    - *Then* tạo Enrollment, nếu chưa có user tạo mới, gửi notification, đại đăng nhóm Zalo.  

**Database Tables**  
- **[DAT-004] Enrollments**  
  ```mermaid
  erDiagram
      Enrollments {
          UUID enrollmentId PK "Unique identifier"
          UUID studentId NOT NULL "Enrolled student"
          UUID courseId NOT NULL "Course"
          TIMESTAMP enrollmentDate NOT NULL "When enrolled"
      }
      Users }o--|| Enrollments : "studentId"
      Courses }o--|| Enrollments : "courseId"
  ```  

### 2.5 Điểm danh và quét QR
- **[REQ-012]** Ghi nhận điểm danh qua QR: *As a Student, I want to scan a QR code at class start.*  
  - **Acceptance Criteria**  
    - *Given* student quét QR và xác nhận,  
    - *When* API nhận payload,  
    - *Thenased* validate student‑course, hexadecimal, create Attendance, trả success, duplicate lờ.  
  - **[EXC-001]** Hoạt động khi mạng mất: retry khi reconnect.  
  - **[EXC-002]** Duplicate scan: return success với flag ‘already recorded’.  
- **[REQ-013]** Đảm bảo idempotency: *Attendance service must guarantee single record for multiple scans.*  
  - **Acceptance Criteria**  
    - *Given* student scan twice within minute,  
    - *When* xử lý,  
    - *Then* chỉ một Attendance, response duplicate flag fut.  

**Database TablesUw**  
- **[DAT-005] Attendance**  
  ```mermaid
  erDiagram
      Attendance {
          UUID attendanceId PK "Unique identifier"
          UUID studentId NOT NULL "Student present"
          UUID courseId NOT NULL "Course attended"
          DATE attendanceDate NOT NULL "Date"
          TIMESTAMP timestamp NOT NULL "Exact time"
      }
      Users }o--|| Attendance : "studentId"
      Courses }o--|| Attendance : "courseId"
  ```  

### 2.6 Quản lý thẻ thành viên
- **[REQ-014]** Xem thẻ thành viên: *As a Student, I want to view my membership card showing remaining validity days.*  
  - **Acceptance Criteria**  
    - *Given* student vào Card page,  
    - *When* request load,  
    - *Then* UI hiển thị total days, used, remainingද.  
- **[REQ-015]** Gia hạn thẻ: *As a Student, I want to extend my membership card validity by paying a fee.*  
  - **Acceptance Criteria**  
    - *Given* student chọn kỳ hạn, xác nhận thanh toán,  
    - *When* payment backend confirm,  
    - *Then* update EndDate, gửi confirmation.  

**Database Tables**  
- **[DAT-006] StudentCards**  
  ```mermaid
  erDiagram
      StudentCards {
          UUID cardId PK "Unique identifier"
          UUID studentId NOT NULL "Owner"
          DATE issueDate NOT NULL "Issue date"
          INT validityDays NOT NULL "Total validity days"
          INT remainingDays NOT NULL "Days left"
      }
      Users }o--|| StudentCards : "studentId"
  ```  

### 2.7 Thông báo và giao tiếp
- **[REQ-016]** Kích hoạt thông báo: *When an admin creates an announcement, assigns a teacher, or registers a student.*  
  - **Acceptance Criteria**  
    - *Given* action save,  
    - *When* event,  
    - *Then* tạo Notification record, queue push, gửi Zalo.  
  - **[EXC-003]** Failed notification delivery: log, retry up to 3 lần.  

**Database Tables**  
- **[DAT-007] Notifications**  
  ```mermaid
  erDiagram
      Notifications {
          UUID notificationId PK "Unique identifier"
          UUID userId optional "Target user"
          VARCHAR(50) groupZalo optional "Zalo group"
          TEXT message NOT NULL "Content"
          TIMESTAMP sentAt NOT NULL "Sent time"
          BOOLEAN delivered DEFAULT false "Delivery status"
      }
      Users }o--|| Notifications : "userId"
  ```  

### 2.8 Kích thước khuyến mãi và thông báo
- **[REQ-017]** QuảnGift: *As a Center Admin or Manager, I want to create, edit, or delete promotions.*  
  - **Acceptance Criteria**  
    - *Given* admin nhập PromotionName, description, conditions, start vừa, end,  
    - *When* save,  
    - *Then* promotion appears, endDate optional perpetual.  
- **[REQ-018]** Quản thông báo: *As左 Center Admin hoặc Manager, I want to create, edit, or delete announcements.*  
  - **Acceptance Criteria**  
    - *Given* admin nhập Title, content, expiry,  
    - *When* save,  
    - *Then* hiển thị site-wide, auto disappear after expiry.  

**Database Tables**  
- **[DAT-009] Promotions**  
  ```mermaid
  erDiagram
      Promotions {
          UUID promoId PK "Unique identifier"
          VARCHAR(30) code NOT NULL "Discount code"
          SMALLINT discountPercent NOT NULL "Percentage"
          DATE startDate optional "Start"
          DATE endDate optional "End"
          TEXT description optional "Details"
      }
  ```  
- **[DAT-010] Announcements**  
  ```mermaid
  erDiagram
      Announcements {
          UUID announcementId PK "Unique identifier"
          VARCHAR(150) title NOT NULL "Title"
          TEXT content NOT NULL "Content"
          DATE startDate optional "Effective start"
          DATE endDate optional "Effective end"
      }
  ```  

### 2.9 Trợ lý khách hàng AI
- **[REQ-019]** Tích hợp chatbot AI: *As any user, I want to interact with an AI chatbot.*  
  - **Acceptance Criteria**  
    - *Given* user mở chat widget,  
    - *When* hỏi câu hỏi,  
    - *Then* AI trả lời hoặc escalates.  

### 2.10 Tính năng chính của ứng dụng di động
- **[REQ-020]** Giao diện tùy theo vai trò: *As a mobile user, I want a responsive UI.*  
  - **Acceptance Criteria**  
    - *Given* user đăng nhập Android/iOS,  
    - *When* tải app,  
    - *Then* hiển thị menu và màn hình phù hợp role.  
- **[REQ-021]** Thông báo đẩy: *As a registered user, I want to receive push notifications.*  
  - **Acceptance Criteria**  
    - *Given* backend trigger,  
    - *When* device token đăng ký,  
    - *Then* deliver via FCM hoặc APNs.  

**Database Tables**  
.credentials for device tokens? Not given; skip.

### 2.11 Hỗ trợ đa ngôn ngữ và SEO
- **[REQ-022]** Phát hiện ngôn ngữ: *As a visitor, I want system to use my language preference.*  
  - **Acceptance Criteria**  
    - *Given* user truy cập,  
    - *When* evaluate locale,  
    - *Then* chọn stored language hoặc Accept-Language.  
- **[REQ-023]** SEO đa ngôn ngữ: *Platform supports SEO forۈز English, Vietnamese, Spanish.*  
  - **Acceptance Criteria**  
    - *Given* page has locale,  
    - *When* render,  
    - *Then* tag lang và hreflang.  

### 2.12 Báo cáo và phân tích
- **[REQ-024]** Tạo báo cáo điểm danh: *As an admin, I want to generate daily attendance report.*  
  - **Acceptance Criteria**  
    - *Given* admin chọn center và date range,  
    - *When* request,  
    - *Then* xuất CSV với StudentName, CourseName, AttendanceDate, Status.  
- **[REQ-025]** Dashboard tóm tắt đăng ký: *As a Center Admin, I want real‑time dashboard.*  
  - **Acceptance Criteria**  
    - *Given* admin vào dashboard,  
    - *When* data refresh,  
    - *Then* hiေန card tổngStudents, activeCourses, upcomingSessions.  

## 3. YÊU CẦU PHI CHỨC NĂNG

- **[NFR-001]** Hiệu suất: API trả 200 ms trung bình. Truy vấn được index 10 000 concurrent users.  
- **[NFR-002]** Tính sẵn sàng: 99.9 % uptime; failover GKE.  
- **[NFR-003]** Bảo mật: TLS 1.3, AES‑256, JWT 15 điểm, refresh 7 ngày, OWASP Top 10.  
- **[NFR-004]** Mở rộng: HPA theo CPU >70 %, latency >300 ms, replicas PostgreSQL read.  
- **[NFR77]** Docker Image: base <200 MB, final <500 MB.  
Practices: above numbers.

- **[NFR-006]** Logging & audit: log user actions, store 1 năm.  
- **[NFR-007]** Hỗ trợ đa ngôn ngữ: strings externalized, switch locale ilman reload.  
- **[NFR-008]** GDPR/CCPA: delete data on request, export JSON, consent marketing.  
- **[NFR-009]** Backup & DR: daily full backup, PITR 24 h, cluster backup region.

## 4. BẢNG ĐỊNH NGHĨA DỮ LIỆU CHI TIẾT

- **[DAT-001] Users** – đã định nghĩa trước.  
- **[DAT-002] Centers** – đã định nghĩa trước.  
- **[DAT-003] Courses** – đã định nghĩa trước.  
- **[DAT-004] Enrollments** – đã định nghĩa trước.  
- **[DAT-005] Attendance** – đã định nghĩa trước.  
- **[DAT-006] StudentCards** – đã định nghĩa trước.  
- **[DAT-007] Notifications** – đã định nghĩa trước.  
- **[DAT-008] Roles** – đã định nghĩa trước.  
- **[DAT-009] Promotions** – đã định nghĩa trước.  
- **[DAT-010] Announcements** – đã định nghĩa trước.  
- **[DAT-011] SystemSettings** – chưa được chi tiết:  
  ```mermaid
  erDiagram
      SystemSettings {
          VARCHAR(50) settingKey PK "Configuration key"
          TEXT settingValue NOT NULL "Value"
          VARCHAR(200) description optional "Meaning"
      }
  ```  

## 5. CHỈNH HÓA ĐIỀU KHI XỬ LÝ LỖI

- **[EXC-001]** Mạng mất trong quét QR: retry after reconnection, ghi log.  
- **[EXC-002]** Duplicate scan: return flag, không tạo thêm record.  
- **[EXC-003]** Thông báo không gửi: log, retry 3 lần.  
- **[EXC-004]** Validation error: trả lỗi 400, bao gồm danh sách trường lỗi.  
- **[EXC-005]** Khôi phục sau outage: xử lý pending scans FIFO, thông báo hồi phục.