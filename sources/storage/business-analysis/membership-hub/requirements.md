# SOFTWARE REQUIREMENTS SPECIFICATION: membership-hub

## 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU
- **Mục tiêu & giá trị cốt lõi**
  - Cung cấp nền tảng quản lý hội viên đa trung tâm thống nhất.
  - Cho phép theo dõi điểm danh thời gian thực qua quét mã QR.
  - Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
  - Hỗ trợ truyền thông đa kênh (web, di động, nhóm Zalo).
  - Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.
- **Nhóm người dùng mục tiêu**
  - Quản trị viên hệ thống (siêu người dùng toàn cầu)
  - Quản trị viên trung tâm (người quản lý cấp trung tâm)
  - Quản lý (phụ trách, quyền hạn giới hạn)
  - Giáo viên (chỉ đọc lịch học)
  - Học viên (duyệt khóa học, ghi danh, xem thẻ hội viên)
  - Người dùng ứng dụng di động (cùng vai trò, giao diện phản hồi)
- **Ma trận kiểm soát truy cập dựa trên vai trò (RBAC)** (mỗi ánh xạ quyền hạn được gắn thẻ `[ARC-XXX]`)
  - **[ARC-001]** Quản trị viên hệ thống: toàn quyền truy cập tất cả các trung tâm.
  - **[ARC-002]** Quản trị viên trung tâm: toàn quyền trong trung tâm của mình, không thể ảnh hưởng đến các trung tâm khác.
  - **[ARC-003]** Quản lý: có thể tạo thông báo, quản lý học viên, chỉ định học viên vào các khóa học hiện có, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
  - **[ARC-004]** Giáo viên: xem các khóa học, danh sách học viên, lịch học của mình; chỉ đọc.
  - **[ARC-005]** Học viên: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.
- **Kiến trúc & luồng dữ liệu toàn cầu** [ARC-006] (Xác thực), [ARC-007] (Xử lý QR điểm danh), [ARC-008] (Gửi thông báo), [ARC-009] (Tích hợp backend ứng dụng di động):
  - **[ARC-006]** Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT với thời gian sống 15 phút và token làm mới.
  - **[ARC-007]** Luồng xử lý QR điểm danh: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi nhận điểm danh một cách idempotent.
  - **[ARC-008]** Luồng gửi thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo được chỉ định cho thông báo, chỉ định khóa học, và cảnh báo điểm danh.
  - **[ARC-009]** Luồng tích hợp backend ứng dụng di động: frontend Next.js tiêu thụ REST APIs; xác thực qua bearer token; hỗ trợ caching offline cho kết nối hạn chế.

## 2. CÁC EPIC CHỨC NĂNG NÂNG CAO (Lặp lại cho từng mô-đun chính)

### 2.1 Quản lý người dùng
**Yêu cầu chức năng cốt lõi**
- **[REQ-001]** Đăng ký người dùng: Là người dùng tiềm năng, tôi muốn đăng ký bằng email và mật khẩu (hoặc nhà cung cấp xã hội) để có thể có tài khoản trong hệ thống.
- **[REQ-002]** Xác thực xã hội: Là người dùng, tôi muốn đăng nhập/đăng ký bằng Firebase, Google hoặc Facebook OAuth để có thể sử dụng thông tin xác thực hiện có.
- **[REQ-003]** Phân quyền người dùng: Là quản trị viên, tôi muốn chỉ định hoặc thay đổi vai trò của người dùng (System Admin, Center Admin, Manager, Teacher, Student) để đảm bảo thực thi quyền hạn chính xác.

**Tiêu chí chấp nhận & tương tác** (Gherkin)
- **[REQ-001]**
  - *Given* một người dùng cung cấp email duy nhất, mật khẩu mạnh và đồng ý với điều khoản, *When* họ gửi biểu mẫu đăng ký, *Then* hệ thống xác thực đầu vào, tạo bản ghi người dùng mới với vai trò ‘Student’ (hoặc ‘Teacher’ nếu được mời) và trả về phản hồi thành công cùng JWT token.
- **[REQ-002]**
  - *Given* một người dùng chọn nhà cung cấp xã hội, *When* họ xác thực qua cửa sổ popup của nhà cung cấp, *Then* hệ thống nhận mã OAuth2, trao đổi lấy thông tin người dùng, tạo hoặc cập nhật bản ghi người dùng cục bộ và cấp JWT token.
- **[REQ-003]**
  - *Given* một quản trị viên chọn người dùng và vai trò mới, *When* hành động gán được xác nhận, *Then* cột vai trò của người dùng được cập nhật và quyền hạn tương ứng được áp dụng ngay lập tức.

**Luồng ngoại lệ của mô-đun**
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, mật khẩu yếu): Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- **[DAT-001]** Bảng Users
  - uuid user_id PK "NOT NULL"
  - varchar email "NOT NULL, UNIQUE"
  - char password_hash "NOT NULL"
  - varchar full_name "NOT NULL"
  - smallint role_id FK
  - varchar provider "DEFAULT 'local'"
  - timestamp created_at "NOT NULL, DEFAULT NOW()"
  - timestamp updated_at "NOT NULL, DEFAULT NOW()"
- **[DAT-002]** Bảng Roles
  - smallint role_id PK "NOT NULL"
  - varchar name "UNIQUE, NOT NULL"
  - varchar description
- erDiagram
```
erDiagram {
    USERS {
        uuid user_id PK "NOT NULL"
        varchar email "NOT NULL, UNIQUE"
        char password_hash "NOT NULL"
        varchar full_name "NOT NULL"
        smallint role_id FK
        varchar provider "DEFAULT 'local'"
        timestamp created_at "NOT NULL, DEFAULT NOW()"
        timestamp updated_at "NOT NULL, DEFAULT NOW()"
    }
    ROLES {
        smallint role_id PK "NOT NULL"
        varchar name "UNIQUE, NOT NULL"
        varchar description
    }
    ROLES ||--o{ USERS : role_id
    USERS ||--o{ GLOBAL : placeholder
    GLOBAL {
        varchar placeholder
    }
}
```

### 2.2 Quản lý trung tâm
**Yêu cầu chức năng cốt lõi**
- **[REQ-004]** Xem danh sách trung tâm: Là bất kỳ người dùng đã xác thực, tôi muốn xem danh sách tất cả các trung tâm cùng địa chỉ, mã số thuế và liên hệ quản trị viên để có thể xác định các trung tâm liên quan.
- **[REQ-005]** Tạo/Cập nhật/Xóa trung tâm: Là System Admin, tôi muốn thêm, chỉnh sửa hoặc xóa bản ghi trung tâm để thông tin trung tâm luôn chính xác.
- **[REQ-006]** Chỉ định quản trị viên trung tâm: Là System Admin, tôi muốn chỉ định hoặc hủy chỉ định một người dùng làm Center Admin cho một trung tâm cụ thể để phân quyền quản lý.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-004]**
  - *Given* một người dùng điều hướng đến trang Centers, *When* yêu cầu hoàn tất, *Then* một bảng các trung tâm (Tên, Địa chỉ, TaxID, Liên hệ Quản trị viên) được hiển thị.
- **[REQ-005]**
  - *Given* một System Admin cung cấp tên trung tâm, địa chỉ, mã số thuế, số điện thoại liên hệ và email, *When* hành động lưu được thực hiện, *Then* trung tâm được lưu trữ và xuất hiện trong danh sách; nếu mã số thuế bị trùng lặp, thao tác thất bại với lỗi xung đột.
- **[REQ-006]**
  - *Given* một System Admin chọn người dùng và trung tâm, *When* hành động chỉ định được xác nhận, *Then* vai trò của người dùng được đặt thành ‘Center Admin’ và ID trung tâm được ghi lại; thao tác hủy chỉ định đảo ngược hành động.

**Luồng ngoại lệ của mô-đun**
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- **[DAT-003]** Bảng Centers
  - uuid center_id PK "NOT NULL"
  - varchar name "NOT NULL"
  - varchar address "NOT NULL"
  - varchar tax_id "UNIQUE, NOT NULL"
  - varchar contact_phone
  - varchar contact_email
- erDiagram
```
erDiagram {
    CENTERS {
        uuid center_id PK "NOT NULL"
        varchar name "NOT NULL"
        varchar address "NOT NULL"
        varchar tax_id "UNIQUE, NOT NULL"
        varchar contact_phone
        varchar contact_email
    }
    CENTERS ||--o{ GLOBAL : placeholder
    GLOBAL {
        varchar placeholder
    }
}
```

### 2.3 Quản lý khóa học
**Yêu cầu chức năng cốt lõi**
- **[REQ-007]** Xem danh sách khóa học: Là bất kỳ người dùng đã xác thực, tôi muốn xem tất cả các khóa học cùng lịch học và giáo viên được chỉ định để có thể duyệt các khóa học được cung cấp.
- **[REQ-008]** Tạo/Cập nhật/Xóa khóa học (Tránh xung đột): Là System Admin hoặc Center Admin, tôi muốn quản lý khóa học (thêm, chỉnh sửa, xóa) trong khi đảm bảo không có lịch học trùng lặp cho cùng một giáo viên hoặc địa điểm.
- **[REQ-009]** Chỉ định giáo viên cho khóa học: Là System Admin, tôi muốn chỉ định hoặc hủy chỉ định giáo viên cho khóa học để cập nhật trách nhiệm giảng dạy.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-007]**
  - *Given* một người dùng truy cập trang Courses, *When* yêu cầu hoàn tất, *Then* một lưới hiển thị CourseID, Title, StartDate, EndDate, TeacherName.
- **[REQ-008]**
  - *Given* một admin cung cấp CourseTitle, StartDate, EndDate, TeacherID, *When* hành động lưu được kích hoạt, *Then* hệ thống xác thực rằng giáo viên không có lịch học khác chồng lấn các ngày này; nếu có xung đột, lỗi được trả về; nếu không, khóa học được lưu trữ.
- **[REQ-009]**
  - *Given* một admin chọn một khóa học và một giáo viên, *When* hành động chỉ định được thực hiện, *Then* ánh xạ khóa học-giáo viên được tạo và một thông báo được xếp hàng cho ứng dụng di động của giáo viên; thao tác hủy chỉ định xóa ánh xạ.

**Luồng ngoại lệ của mô-đun**
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- **[DAT-004]** Bảng Courses
  - uuid course_id PK "NOT NULL"
  - varchar title "NOT NULL"
  - text description
  - date start_date "NOT NULL"
  - date end_date "NOT NULL"
  - uuid teacher_id FK
  - int max_students "DEFAULT 30"
- erDiagram
```
erDiagram {
    COURSES {
        uuid course_id PK "NOT NULL"
        varchar title "NOT NULL"
        text description
        date start_date "NOT NULL"
        date end_date "NOT NULL"
        uuid teacher_id FK
        int max_students "DEFAULT 30"
    }
    USERS ||--o{ COURSES : teacher_id
    COURSES ||--o{ GLOBAL : placeholder
    GLOBAL {
        varchar placeholder
    }
}
```

### 2.4 Đăng ký & ghi danh học viên
**Yêu cầu chức năng cốt lõi**
- **[REQ-010]** Duyệt khóa học: Là Học viên, tôi muốn duyệt các khóa học có sẵn (trừ các khóa học đã ghi danh) để có thể chọn các khóa học để tham gia.
- **[REQ-011]** Ghi danh khóa học: Là Học viên, tôi muốn ghi danh vào một khóa học (có sẵn hoặc mới), điều này tự động tạo tài khoản học viên nếu thiếu và chỉ định học viên vào khóa học.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-010]**
  - *Given* một Học viên đăng nhập và điều hướng đến trang Browse Courses, *When* yêu cầu hoàn tất, *Then* một danh sách các khóa học cùng sức chứa và lịch học được hiển thị, loại trừ các khóa học mà học viên đã có bản ghi ghi danh.
- **[REQ-011]**
  - *Given* một Học viên chọn một khóa học và gửi yêu cầu ghi danh, *When* backend xử lý yêu cầu, *Then* một bản ghi ghi danh mới được tạo; nếu học viên chưa có tài khoản cục bộ, một tài khoản được tạo với vai trò ‘Student’; một thông báo được xếp hàng cho ứng dụng di động của học viên và nhóm Zalo của trung tâm.

**Luồng ngoại lệ của mô-đun**
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- **[DAT-005]** Bảng Enrollments
  - uuid enrollment_id PK "NOT NULL"
  - uuid student_id FK
  - uuid course_id FK
  - timestamp enrollment_date "DEFAULT NOW()"
- erDiagram
```
erDiagram {
    ENROLLMENTS {
        uuid enrollment_id PK "NOT NULL"
        uuid student_id FK
        uuid course_id FK
        timestamp enrollment_date "DEFAULT NOW()"
    }
    USERS ||--o{ ENROLLMENTS : student_id
    COURSES ||--o{ ENROLLMENTS : course_id
    ENROLLMENTS ||--o{ GLOBAL : placeholder
    GLOBAL {
        varchar placeholder
    }
}
```

### 2.5 Chấm công & quét QR
**Yêu cầu chức năng cốt lõi**
- **[REQ-012]** Chụp ảnh QR điểm danh: Là Học viên (qua ứng dụng di động), tôi muốn quét mã QR khi bắt đầu lớp học để điểm danh của tôi được ghi nhận cho ngày hiện tại.
- **[REQ-013]** Idempotency điểm danh: Dịch vụ điểm danh phải đảm bảo rằng nhiều lần quét từ cùng một học viên cho cùng một khóa học trong cùng một ngày tạo ra một bản ghi điểm danh.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-012]**
  - *Given* một Học viên mở máy quét, quét một mã QR hợp lệ của khóa học và xác nhận điểm danh, *When* API nhận payload, *Then* hệ thống xác thực mối quan hệ học viên-khóa học, tạo bản ghi điểm danh với timestamp và trả về phản hồi thành công; các lần quét trùng lặp trong cùng một ngày bị bỏ qua.
- **[REQ-013]**
  - *Given* một học viên quét QR hai lần trong vòng một phút, *When* dịch vụ xử lý cả hai yêu cầu, *Then* chỉ một hàng điểm danh được tạo; các yêu cầu tiếp theo trả về thành công với cờ ‘duplicate’.

**Luồng ngoại lệ của mô-đun**
- **[EXC-001]** Mạng & Kết nối bị rớt trong khi quét QR: Nếu một học viên quét QR nhưng mạng không khả dụng, *When* ứng dụng thử lại yêu cầu sau khi kết nối lại, *Then* điểm danh được ghi nhận khi dịch vụ khả dụng.
- **[EXC-002]** Gửi điểm danh trùng lặp: Nếu cùng một học viên quét cùng một mã QR nhiều lần trong cùng một ngày, *When* hệ thống phát hiện trùng lặp, *Then* nó trả về phản hồi thành công chỉ ra ‘đã ghi nhận’ và không tạo hàng bổ sung.
- **[EXC-003]** Gửi thông báo thất bại: Khi một thông báo push không thể được gửi (ví dụ: token thiết bị không hợp lệ), *Then* hệ thống ghi lại lỗi và lên lịch thử lại tối đa ba lần trước khi đánh dấu là thất bại.
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- **[DAT-006]** Bảng Attendance
  - uuid attendance_id PK "NOT NULL"
  - uuid student_id FK
  - uuid course_id FK
  - date attendance_date "NOT NULL"
  - timestamp timestamp "DEFAULT NOW()"
- erDiagram
```
erDiagram {
    ATTENDANCE {
        uuid attendance_id PK "NOT NULL"
        uuid student_id FK
        uuid course_id FK
        date attendance_date "NOT NULL"
        timestamp timestamp "DEFAULT NOW()"
    }
    USERS ||--o{ ATTENDANCE : student_id
    COURSES ||--o{ ATTENDANCE : course_id
    ATTENDANCE ||--o{ GLOBAL : placeholder
    GLOBAL {
        varchar placeholder
    }
}
```

### 2.6 Quản lý thẻ hội viên
**Yêu cầu chức năng cốt lõi**
- **[REQ-014]** Hiển thị hiệu lực thẻ: Là Học viên, tôi muốn xem thẻ hội viên của mình hiển thị ngày hiệu lực còn lại để biết khi nào cần gia hạn.
- **[REQ-015]** Gia hạn thẻ: Là Học viên, tôi muốn gia hạn thẻ hội viên bằng cách thanh toán một khoản phí, điều này cập nhật ngày kết thúc.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-014]**
  - *Given* một Học viên mở trang Card, *When* yêu cầu tải hoàn tất, *Then* giao diện hiển thị tổng số ngày hiệu lực, ngày đã sử dụng, và ngày còn lại; dữ liệu được lấy từ thực thể StudentCard.
- **[REQ-015]**
  - *Given* một Học viên chọn một khoảng thời gian gia hạn (ví dụ: 30 ngày), xác nhận thanh toán, *When* dịch vụ thanh toán xác nhận thành công, *Then* EndDate của StudentCard được gia hạn thêm số ngày đã chọn và một thông báo xác nhận được gửi.

**Luồng ngoại lệ của mô-đun**
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- **[DAT-007]** Bảng StudentCards
  - uuid card_id PK "NOT NULL"
  - uuid student_id FK
  - date issue_date "NOT NULL"
  - int validity_days "NOT NULL"
  - int remaining_days "computed"
- erDiagram
```
erDiagram {
    STUDENTCARDS {
        uuid card_id PK "NOT NULL"
        uuid student_id FK
        date issue_date "NOT NULL"
        int validity_days "NOT NULL"
        int remaining_days "computed"
    }
    USERS ||--o{ STUDENTCARDS : student_id
    STUDENTCARDS ||--o{ GLOBAL : placeholder
    GLOBAL {
        varchar placeholder
    }
}
```

### 2.7 Thông báo & giao tiếp
**Yêu cầu chức năng cốt lõi**
- **[REQ-016]** Kích hoạt thông báo: Khi một admin tạo thông báo, chỉ định giáo viên cho khóa học hoặc ghi danh học viên, hệ thống phải tạo một thông báo gửi đến ứng dụng di động của học viên và đăng bài lên nhóm Zalo được chỉ định.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-016]**
  - *Given* một admin thực hiện hành động yêu cầu thông báo, *When* hành động được lưu, *Then* một bản ghi Notification được tạo, một payload push notification được xếp hàng cho ứng dụng di động và một tin nhắn văn bản được gửi đến nhóm chat Zalo.

**Luồng ngoại lệ của mô-đun**
- **[EXC-003]** Gửi thông báo thất bại: Khi một thông báo push không thể được gửi (ví dụ: token thiết bị không hợp lệ), *Then* hệ thống ghi lại lỗi và lên lịch thử lại tối đa ba lần trước khi đánh dấu là thất bại.
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- **[DAT-008]** Bảng Notifications
  - uuid notification_id PK "NOT NULL"
  - uuid user_id FK
  - varchar group_zalo
  - text message "NOT NULL"
  - timestamp sent_at "DEFAULT NOW()"
  - boolean delivered "DEFAULT false"
- erDiagram
```
erDiagram {
    NOTIFICATIONS {
        uuid notification_id PK "NOT NULL"
        uuid user_id FK
        varchar group_zalo
        text message "NOT NULL"
        timestamp sent_at "DEFAULT NOW()"
        boolean delivered "DEFAULT false"
    }
    USERS ||--o{ NOTIFICATIONS : user_id
    NOTIFICATIONS ||--o{ GLOBAL : placeholder
    GLOBAL {
        varchar placeholder
    }
}
```

### 2.8 Quản lý khuyến mãi & thông báo
**Yêu cầu chức năng cốt lõi**
- **[REQ-017]** Quản lý khuyến mãi: Là Center Admin hoặc Manager, tôi muốn tạo, chỉnh sửa hoặc xóa các khuyến mãi (giảm giá, ưu đãi) với ngày bắt đầu/kết thúc để học viên có thể xem các ưu đãi áp dụng.
- **[REQ-018]** Quản lý thông báo: Là Center Admin hoặc Manager, tôi muốn tạo, chỉnh sửa hoặc xóa các thông báo có ngày hết hạn tùy chọn để phát sóng toàn trang.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-017]**
  - *Given* một admin cung cấp PromotionName, mô tả, điều kiện, startDate, endDate, *When* lưu, *Then* khuyến mãi xuất hiện trong danh sách hiển thị cho học viên; nếu endDate bị bỏ qua, khuyến mãi được coi là vĩnh viễn.
- **[REQ-018]**
  - *Given* một admin nhập AnnouncementTitle, nội dung, hết hạn tùy chọn, *When* lưu, *Then* thông báo được hiển thị trên toàn trang; nếu hết hạn được đặt, nó tự động biến mất sau ngày đó.

**Luồng ngoại lệ của mô-đun**
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- **[DAT-009]** Bảng Promotions
  - uuid promo_id PK "NOT NULL"
  - varchar code "UNIQUE"
  - smallint discount_percent "NOT NULL"
  - date start_date
  - date end_date
  - text description
- **[DAT-010]** Bảng Announcements
  - uuid announcement_id PK "NOT NULL"
  - varchar title "NOT NULL"
  - text content "NOT NULL"
  - date start_date
  - date end_date
- erDiagram
```
erDiagram {
    PROMOTIONS {
        uuid promo_id PK "NOT NULL"
        varchar code "UNIQUE"
        smallint discount_percent "NOT NULL"
        date start_date
        date end_date
        text description
    }
    ANNOUNCEMENTS {
        uuid announcement_id PK "NOT NULL"
        varchar title "NOT NULL"
        text content "NOT NULL"
        date start_date
        date end_date
    }
    PROMOTIONS ||--o{ GLOBAL : placeholder
    ANNOUNCEMENTS ||--o{ GLOBAL : placeholder
    GLOBAL {
        varchar placeholder
    }
}
```

### 2.9 Chatbot dịch vụ khách hàng AI
**Yêu cầu chức năng cốt lõi**
- **[REQ-019]** Tích hợp chatbot AI: Là bất kỳ người dùng, tôi muốn tương tác với một chatbot AI có thể trả lời các câu hỏi phổ biến về khóa học, giáo viên, trung tâm và trạng thái tài khoản.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-019]**
  - *Given* một người dùng mở widget chat, *When* họ đặt một câu hỏi, *Then* AI trả về một câu trả lời liên quan hoặc chuyển đến hỗ trợ con người nếu độ tin cậy thấp.

**Luồng ngoại lệ của mô-đun**
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- **[DAT-011]** Bảng SystemSettings
  - varchar setting_key PK "NOT NULL"
  - text setting_value "NOT NULL"
  - varchar description
- erDiagram
```
erDiagram {
    SYSTEMSETTINGS {
        varchar setting_key PK "NOT NULL"
        text setting_value "NOT NULL"
        varchar description
    }
    SYSTEMSETTINGS ||--o{ GLOBAL : placeholder
    GLOBAL {
        varchar placeholder
    }
}
```

### 2.10 Tính năng ứng dụng di động
**Yêu cầu chức năng cốt lõi**
- **[REQ-020]** Giao diện ứng dụng di động theo vai trò: Là người dùng di động, tôi muốn một giao diện phản hồi phản ánh chức năng web cho vai trò được chỉ định (Student, Teacher, Admin, v.v.).
- **[REQ-021]** Push notification trên di động: Là người dùng đã đăng ký, tôi muốn nhận thông báo push trên thiết bị di động cho xác nhận điểm danh, thông báo mới và tin nhắn nhắc nhở.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-020]**
  - *Given* một người dùng đăng nhập trên Android hoặc iOS, *When* ứng dụng tải, *Then* menu điều hướng và màn hình phù hợp được hiển thị dựa trên vai trò của người dùng.
- **[REQ-021]**
  - *Given* một sự kiện backend kích hoạt một push, *When* token thiết bị được đăng ký, *Then* thông báo được phân phối qua Firebase Cloud Messaging (FCM) hoặc APNs.

**Luồng ngoại lệ của mô-đun**
- **[EXC-003]** Gửi thông báo thất bại: Khi một thông báo push không thể được gửi (ví dụ: token thiết bị không hợp lệ), *Then* hệ thống ghi lại lỗi và lên lịch thử lại tối đa ba lần trước khi đánh dấu là thất bại.
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- Không có bảng mới; sử dụng các bảng Users và Notifications hiện có.

### 2.11 Bản địa hóa & SEO
**Yêu cầu chức năng cốt lõi**
- **[REQ-022]** Phát hiện ngôn ngữ mặc định: Là khách truy cập, tôi muốn hệ thống sử dụng tùy chọn ngôn ngữ trước đó của tôi, rơi vào cài đặt mặc định của trình duyệt, để có trải nghiệm cá nhân hóa.
- **[REQ-023]** SEO đa ngôn ngữ: Hệ thống phải hỗ trợ SEO cho ít nhất tiếng Anh, tiếng Việt và tiếng Tây Ban Nha; mỗi trang phải bao gồm thẻ meta và liên kết hreflang theo ngôn ngữ.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-022]**
  - *Given* một người dùng truy cập trang web, *When* hệ thống đánh giá ngôn ngữ, *Then* nó chọn ngôn ngữ được lưu nếu có; nếu không, nó sử dụng Accept-Language header; giao diện được cập nhật tương ứng.
- **[REQ-023]**
  - *Given* một trang được yêu cầu với một ngôn ngữ cụ thể, *When* trang được render, *Then* HTML bao gồm một thẻ `<html lang='en'>` và các liên kết hreflang trỏ đến các phiên bản ngôn ngữ thay thế.

**Luồng ngoại lệ của mô-đun**
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- Không có bảng mới; SystemSettings có thể lưu các giá trị locale.

### 2.12 Báo cáo & phân tích
**Yêu cầu chức năng cốt lõi**
- **[REQ-024]** Tạo báo cáo điểm danh: Là admin, tôi muốn tạo một báo cáo điểm danh hàng ngày cho một trung tâm (CSV) hiển thị tình trạng điểm danh của từng học viên.
- **[REQ-025]** Bảng điều khiển tóm tắt ghi danh: Là Center Admin, tôi muốn một bảng điều khiển thời gian thực tóm tắt tổng số học viên, khóa học hoạt động và các buổi học sắp tới.

**Tiêu chí chấp nhận & tương tác**
- **[REQ-024]**
  - *Given* một admin chọn một trung tâm và khoảng thời gian, *When* báo cáo được yêu cầu, *Then* một tệp CSV được tạo với các cột: StudentName, CourseName, AttendanceDate, Status.
- **[REQ-025]**
  - *Given* một admin mở bảng điều khiển, *When* dữ liệu được làm mới, *Then* các thẻ hiển thị totalStudents, activeCourses, upcomingSessions (trong 7 ngày tới).

**Luồng ngoại lệ của mô-đun**
- **[EXC-004]** Xác thực đầu vào không hợp lệ: Nếu xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

**Từ điển dữ liệu của mô-đun**
- Không có bảng mới; sử dụng các bảng điểm danh, ghi danh hiện có.

### 3. LUỒNG NGOẠI LỆ & TRƯỜNG HỢP ĐẶC BIỆT
- **[EXC-001]** Mạng & Kết nối bị rớt trong khi quét QR:
  - *If* một học viên quét QR nhưng mạng không khả dụng, *When* ứng dụng thử lại yêu cầu sau khi kết nối lại, *Then* điểm danh được ghi nhận khi dịch vụ khả dụng.

- **[EXC-002]** Gửi điểm danh trùng lặp:
  - *If* cùng một học viên quét cùng một mã QR nhiều lần trong cùng một ngày, *When* hệ thống phát hiện trùng lặp, *Then* nó trả về phản hồi thành công chỉ ra ‘đã ghi nhận’ và không tạo hàng bổ sung.

- **[EXC-003]** Gửi thông báo thất bại:
  - *When* một thông báo push không thể được gửi (ví dụ: token thiết bị không hợp lệ), *Then* hệ thống ghi lại lỗi và lên lịch thử lại tối đa ba lần trước khi đánh dấu là thất bại.

- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc):
  - *If* xác thực thất bại khi gửi biểu mẫu, *When* lỗi được trả về cho người dùng, *Then* một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

- **[EXC-005]** Khôi phục hệ thống sau sự cố:
  - *If* dịch vụ trở nên không khả dụng, *When* nó khôi phục, *Then* bất kỳ quét QR đang chờ xử lý nào được xử lý theo thứ tự FIFO và người dùng nhận được thông báo về các sự kiện đã khôi phục.

### 4. YÊU CẦU PHI CHỨC NĂNG TOÀN CẦU
- **[NFR-001]** Chỉ số hiệu năng:
  - Các phản hồi API cốt lõi (xác thực, chụp ảnh điểm danh, danh sách khóa học) phải hoàn tất trong vòng 200 ms trung bình.
  - Các truy vấn cơ sở dữ liệu phải được lập chỉ mục để hỗ trợ đọc trong dưới một giây cho tối đa 10.000 người dùng đồng thời.

- **[NFR-002]** Tính khả dụng:
  - Mục tiêu 99,9% thời gian hoạt động hàng năm; SLA bao gồm khả năng tự động chuyển đổi giữa các cụm GKE.

- **[NFR-003]** Bảo mật:
  - Tất cả dữ liệu trong quá trình truyền phải sử dụng TLS 1.3; mã hóa AES-256 khi lưu trữ.
  - JWT access token hết hạn sau 15 phút; refresh token có thời gian sống 7 ngày.
  - Thực hiện các biện pháp kiểm soát OWASP Top 10 (SQL injection, XSS, CSRF).

- **[NFR-004]** Khả năng mở rộng & tính khả dụng:
  - Mở rộng quy mô theo chiều ngang các dịch vụ Quarkus qua Kubernetes HPA dựa trên CPU > 70% hoặc độ trễ yêu cầu > 300 ms.
  - Sử dụng các bản sao đọc PostgreSQL cho khối lượng công việc báo cáo.

- **[NFR-005]** Kích thước hình ảnh Docker:
  - Hình ảnh cơ sở < 200 MB; hình ảnh cuối cùng < 500 MB.

- **[NFR-006]** Logging & Kiểm toán:
  - Tất cả các hành động của người dùng (thay đổi vai trò, bản ghi điểm danh, thông báo) phải được ghi lại với timestamp, ID người dùng và chi tiết hành động; nhật ký được lưu giữ trong 1 năm.

- **[NFR-007]** Hỗ trợ đa ngôn ngữ:
  - Các chuỗi UI phải được ngoại hóa; hỗ trợ tiếng Anh, tiếng Việt, tiếng Tây Ban Nha; chuyển đổi ngôn ngữ mà không cần tải lại trang khi có thể.

- **[NFR-008]** Tuân thủ GDPR/CCPA:
  - Xóa dữ liệu cá nhân theo yêu cầu của người dùng; xuất dữ liệu ở định dạng JSON; quản lý sự đồng ý cho truyền thông tiếp thị.

- **[NFR-009]** Sao lưu & Khôi phục thảm họa:
  - Sao lưu PostgreSQL hàng ngày đầy đủ; khôi phục điểm trong thời gian lên đến 24 giờ; sao lưu cụm GKE đến khu vực riêng biệt.