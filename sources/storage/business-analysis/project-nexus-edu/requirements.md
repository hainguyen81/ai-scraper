## 1. PROJECT OVERVIEW

- **Product Objectives & Core Values**
  - Cung cấp nền tảng quản lý hội viên đa trung tâm thống nhất.
  - Cho phép theo dõi điểm danh thời gian thực qua quét QR.
  - Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
  - Hỗ trợ truyền thông đa kênh (web, di động, nhóm Zalo).
  - Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

- **Target User Personas**
  - Quản trị viên hệ thống (siêu người dùng toàn cầu)
  - Quản trị viên trung tâm (quản lý cấp trung tâm)
  - Quản lý (phụ trách, quyền hạn giới hạn)
  - Giáo viên (chỉ xem lịch giảng dạy)
  - Học viên (duyệt khóa học, đăng ký, xem thẻ hội viên)
  - Người dùng ứng dụng di động (cùng các vai trò trên, giao diện phản hồi)

- **Role-Based Access Control (RBAC) Matrix**
  - [ARC-001] Hệ thống quản trị viên: toàn quyền trên tất cả các trung tâm.
  - [ARC-002] Quản trị viên trung tâm: toàn quyền trong trung tâm của mình, không ảnh hưởng đến trung tâm khác.
  - [ARC-003] Quản lý: có thể tạo thông báo, quản lý học viên, chỉ định học viên vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
  - [ARC-004] Giáo viên: xem các khóa học của mình, danh sách học viên, lịch dạy; chỉ đọc.
  - [ARC-005] Học viên: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày còn lại), gia hạn ngày thẻ.

- **Architecture & Data Flow (key flows)**
  - [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token với thời hạn 15 phút và token làm mới.
  - [ARC-007] Luồng xử lý điểm danh qua QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
  - [ARC-008] Luồng gửi thông báo: hệ thống kích hoạt thông báo đẩy đến ứng dụng di động và đăng tin nhắn đến nhóm Zalo được chỉ định cho thông báo, chỉ định khóa học và cảnh báo điểm danh.
  - [ARC-009] Luồng tích hợp backend ứng dụng di động: Next.js frontend tiêu thụ REST APIs; xác thực qua bearer token; hỗ trợ lưu trữ ngoại tuyến cho trường hợp mất kết nối.

## 2. FUNCTIONAL REQUIREMENTS

### 2.1 Quản lý người dùng

- **[REQ-001]** Đăng ký người dùng: Là một người dùng tiềm năng, tôi muốn đăng ký bằng email và mật khẩu (hoặc nhà cung cấp mạng xã hội) để có thể sở hữu một tài khoản trong hệ thống.
  - **Acceptance Criteria**:
    - Cho trước một người dùng cung cấp email duy nhất, mật khẩu mạnh và đồng ý với điều khoản, khi họ gửi biểu mẫu đăng ký, thì hệ thống xác thực đầu vào, tạo bản ghi người dùng mới với vai trò ‘Học viên’ (hoặc ‘Giáo viên’ nếu được mời) và trả về phản hồi thành công cùng mã thông báo JWT. *[REQ-001]*
  - **Data Inputs & Field Validations**:
    - Email: bắt buộc, tối đa 255 ký tự, phải chứa một dấu ‘@’ và phần tên miền (ví dụ: user@example.com). Phải duy nhất.
    - Mật khẩu: bắt buộc, tối thiểu 8 ký tự, ít nhất một chữ hoa, một chữ thường, một chữ số, một ký tự đặc biệt.
    - Điều khoản: bắt buộc chọn ô.

- **[REQ-002]** Đăng nhập mạng xã hội: Là một người dùng, tôi muốn đăng nhập/đăng ký bằng Firebase, Google hoặc Facebook OAuth để có thể tận dụng thông tin xác thực hiện có.
  - **Acceptance Criteria**:
    - Cho trước một người dùng chọn một nhà cung cấp mạng xã hội, khi họ xác thực qua cửa sổ pop-up của nhà cung cấp, thì hệ thống nhận được mã OAuth2, trao đổi mã để lấy thông tin người dùng, tạo hoặc cập nhật bản ghi người dùng cục bộ và cấp mã thông báo JWT. *[REQ-002]*
  - **Data Inputs & Field Validations**:
    - Mã thông báo nhà cung cấp, tùy chọn hình ảnh hồ sơ.

- **[REQ-003]** Phân quyền người dùng: Là một quản trị viên, tôi muốn chỉ định hoặc thay đổi vai trò của một người dùng (Hệ thống quản trị viên, Quản trị viên trung tâm, Quản lý, Giáo viên, Học viên) để các quyền được thực thi chính xác.
  - **Acceptance Criteria**:
    - Cho trước một quản trị viên chọn một người dùng và một vai trò mới, khi hành động chỉ định được xác nhận, thì cột vai trò của người dùng được cập nhật và các quyền tương ứng được áp dụng ngay lập tức. *[REQ-003]*
  - **Data Inputs & Field Validations**:
    - Vai trò (thả xuống), bắt buộc ghi nhật ký kiểm toán.

### 2.2 Quản lý trung tâm

- **[REQ-004]** Xem danh sách trung tâm: Là bất kỳ người dùng đã xác thực nào, tôi muốn xem danh sách tất cả các trung tâm cùng địa chỉ, mã số thuế và liên hệ quản trị viên để có thể xác định các trung tâm liên quan.
  - **Acceptance Criteria**:
    - Cho trước một người dùng truy cập trang Trung tâm, khi yêu cầu hoàn tất, thì một bảng các trung tâm (Tên, Địa chỉ, Mã số thuế, Liên hệ quản trị viên) được hiển thị. *[REQ-004]*
  - **Data Inputs & Field Validations**: Không có (chỉ đọc).

- **[REQ-005]** Tạo/Cập nhật/Xóa trung tâm: Là một Hệ thống quản trị viên, tôi muốn thêm, chỉnh sửa hoặc xóa một bản ghi trung tâm để thông tin trung tâm luôn cập nhật.
  - **Acceptance Criteria**:
    - Cho trước một Hệ thống quản trị viên cung cấp tên trung tâm, địa chỉ, mã số thuế, số điện thoại liên hệ và email, khi hành động lưu được thực hiện, thì trung tâm được lưu và xuất hiện trong danh sách; nếu mã số thuế trùng lặp, thao tác thất bại với lỗi xung đột. *[REQ-005]*
  - **Data Inputs & Field Validations**:
    - Tên: bắt buộc, tối đa 100 ký tự.
    - Địa chỉ: bắt buộc, tối đa 255 ký tự.
    - Mã số thuế: bắt buộc, số, 10‑13 chữ số, duy nhất.
    - Số điện thoại liên hệ: tùy chọn, có thể bao gồm +, chữ số, dấu cách, dấu gạch ngang, ngoặc đơn.
    - Email liên hệ: tùy chọn, phải là định dạng email hợp lệ.

- **[REQ-006]** Chỉ định quản trị viên trung tâm: Là một Hệ thống quản trị viên, tôi muốn chỉ định hoặc hủy chỉ định một người dùng làm Quản trị viên trung tâm cho một trung tâm cụ thể để phân quyền kiểm soát.
  - **Acceptance Criteria**:
    - Cho trước một Hệ thống quản trị viên chọn một người dùng và một trung tâm, khi hành động chỉ định được xác nhận, thì vai trò của người dùng được đặt thành ‘Quản trị viên trung tâm’ và ID trung tâm được ghi lại; thao tác hủy chỉ định đảo ngược hoạt động. *[REQ-006]*
  - **Data Inputs & Field Validations**:
    - ID người dùng, ID trung tâm.

### 2.3 Quản lý khóa học

- **[REQ-007]** Xem danh sách khóa học: Là bất kỳ người dùng đã xác thực nào, tôi muốn xem tất cả các khóa học cùng lịch học và giáo viên được chỉ định để có thể duyệt các khóa học được cung cấp.
  - **Acceptance Criteria**:
    - Cho trước một người dùng truy cập trang Khóa học, khi yêu cầu hoàn tất, thì một lưới hiển thị CourseID, Tiêu đề, Ngày bắt đầu, Ngày kết thúc, Tên giáo viên được hiển thị. *[REQ-007]*
  - **Data Inputs & Field Validations**: Không có.

- **[REQ-008]** Tạo/Cập nhật/Xóa khóa học (tránh xung đột): Là một Hệ thống quản trị viên hoặc Quản trị viên trung tâm, tôi muốn quản lý khóa học (thêm, chỉnh sửa, xóa) đồng thời đảm bảo không có lịch học trùng lặp cho cùng một giáo viên hoặc địa điểm.
  - **Acceptance Criteria**:
    - Cho trước một quản trị viên cung cấp Tiêu đề khóa học, Ngày bắt đầu, Ngày kết thúc, ID giáo viên, khi hành động lưu được kích hoạt, thì hệ thống xác thực rằng giáo viên không được lên lịch cho khóa học khác chồng lấn các ngày này; nếu xung đột, lỗi được trả về; nếu không, khóa học được lưu. *[REQ-008]*
  - **Data Inputs & Field Validations**:
    - Tiêu đề: bắt buộc, tối đa 150 ký tự.
    - Ngày bắt đầu/Ngày kết thúc: bắt buộc, Ngày kết thúc >= Ngày bắt đầu.
    - ID giáo viên: bắt buộc, khóa ngoại.
    - Logic kiểm tra chồng lấn được thực thi ở mức DB/trigger.

- **[REQ-009]** Chỉ định giáo viên vào khóa học: Là một Hệ thống quản trị viên, tôi muốn chỉ định hoặc hủy chỉ định giáo viên cho các khóa học để cập nhật trách nhiệm giảng dạy.
  - **Acceptance Criteria**:
    - Cho trước một quản trị viên chọn một khóa học và một giáo viên, khi hành động chỉ định được thực hiện, thì ánh xạ giáo viên-khóa học được tạo và một thông báo được xếp hàng cho ứng dụng di động của giáo viên; thao tác hủy chỉ định xóa ánh xạ. *[REQ-009]*
  - **Data Inputs & Field Validations**:
    - ID khóa học, ID giáo viên (phải tồn tại).

### 2.4 Đăng ký và ghi danh học viên

- **[REQ-010]** Duyệt khóa học: Là một Học viên, tôi muốn duyệt các khóa học có sẵn (trừ các khóa học đã đăng ký) để có thể chọn các khóa học để tham gia.
  - **Acceptance Criteria**:
    - Cho trước một Học viên đăng nhập và truy cập trang Duyệt khóa học, khi yêu cầu hoàn tất, thì một danh sách các khóa học cùng sức chứa và lịch học được hiển thị, trừ các khóa học mà học viên đã có bản ghi đăng ký. *[REQ-010]*
  - **Data Inputs & Field Validations**: Không có.

- **[REQ-011]** Đăng ký khóa học của học viên: Là một Học viên, tôi muốn đăng ký một khóa học (có sẵn hoặc mới), điều này tự động tạo một tài khoản Học viên nếu thiếu và chỉ định học viên vào khóa học.
  - **Acceptance Criteria**:
    - Cho trước một Học viên chọn một khóa học và gửi đăng ký, khi backend xử lý yêu cầu, thì một bản ghi đăng ký mới được tạo; nếu học viên không có tài khoản cục bộ, một tài khoản với vai trò ‘Học viên’ được tạo; một thông báo được xếp hàng cho ứng dụng di động của học viên và nhóm Zalo của trung tâm. *[REQ-011]*
  - **Data Inputs & Field Validations**:
    - ID khóa học: bắt buộc, phải là khóa học hoạt động.
    - ID học viên: được suy ra từ mã thông báo xác thực (hoặc được tạo trên đường bay).

### 2.5 Điểm danh và quét QR

- **[REQ-012]** Ghi nhận điểm danh qua QR: Là một Học viên (qua ứng dụng di động), tôi muốn quét mã QR ở đầu buổi học để ghi lại điểm danh của mình cho ngày hiện tại.
  - **Acceptance Criteria**:
    - Cho trước một Học viên mở máy quét, quét một mã QR hợp lệ của khóa học và xác nhận điểm danh, khi API nhận được tải trọng, thì hệ thống xác thực mối quan hệ học viên-khóa học, tạo một bản ghi Điểm danh với dấu thời gian và trả về phản hồi thành công; các lần quét trùng lặp trong cùng ngày bị bỏ qua. *[REQ-012]*
  - **Data Inputs & Field Validations**:
    - Tải trọng QR: chuỗi base64 mã hóa studentID và courseID.
    - Xác thực: học viên phải được ghi danh vào khóa học cho ngày đó.

- **[REQ-013]** Tính chất không trùng lặp của điểm danh: Dịch vụ điểm danh phải đảm bảo rằng nhiều lần quét từ cùng một học viên cho cùng một khóa học trong cùng một ngày tạo ra một bản ghi điểm danh duy nhất.
  - **Acceptance Criteria**:
    - Cho trước một học viên quét QR hai lần trong vòng một phút, khi dịch vụ xử lý cả hai yêu cầu, thì chỉ một hàng điểm danh được tạo; các yêu cầu tiếp theo trả về thành công với cờ ‘đã ghi’ . *[REQ-013]*
  - **Data Inputs & Field Validations**: Khóa chính gồm (StudentID, CourseID, Date).

### 2.6 Quản lý thẻ hội viên học viên

- **[REQ-014]** Hiển thị tính hợp lệ của thẻ: Là một Học viên, tôi muốn xem thẻ hội viên của mình hiển thị ngày hiệu lực còn lại để biết khi nào cần gia hạn.
  - **Acceptance Criteria**:
    - Cho trước một Học viên mở trang Thẻ, khi yêu cầu tải, thì giao diện hiển thị tổng số ngày hiệu lực, số ngày đã sử dụng và số ngày còn lại; dữ liệu được suy ra từ thực thể StudentCard. *[REQ-014]*
  - **Data Inputs & Field Validations**: Không có (chỉ đọc).

- **[REQ-015]** Gia hạn thẻ hội viên: Là một Học viên, tôi muốn gia hạn thẻ hội viên của mình bằng cách trả một khoản phí, điều này cập nhật ngày kết thúc.
  - **Acceptance Criteria**:
    - Cho trước một Học viên chọn một khoảng thời gian gia hạn (ví dụ: 30 ngày), xác nhận thanh toán, khi dịch vụ thanh toán xác nhận thành công, thì StudentCard’s EndDate được gia hạn thêm số ngày đã chọn và một thông báo xác nhận được gửi. *[REQ-015]*
  - **Data Inputs & Field Validations**:
    - Số ngày gia hạn: số nguyên, 1‑365.
    - Tích hợp cổng thanh toán (ngoài phạm vi).

### 2.7 Thông báo và truyền thông

- **[REQ-016]** Kích hoạt thông báo: Khi một quản trị viên tạo một thông báo, chỉ định một giáo viên vào một khóa học hoặc đăng ký một học viên, hệ thống phải tạo một thông báo gửi đến ứng dụng di động của học viên và đăng một tin nhắn vào nhóm Zalo được chỉ định.
  - **Acceptance Criteria**:
    - Cho trước một quản trị viên thực hiện một hành động yêu cầu thông báo, khi hành động được lưu, thì một bản ghi Thông báo được tạo, một tải trọng thông báo đẩy được xếp hàng cho ứng dụng di động và một tin nhắn văn bản được gửi đến cuộc trò chuyện nhóm Zalo. *[REQ-016]*
  - **Data Inputs & Field Validations**:
    - Đối tượng mục tiêu (học viên, giáo viên, nhóm), nội dung tin nhắn, tùy chọn phương tiện.

### 2.8 Quản lý khuyến mãi và thông báo

- **[REQ-017]** Quản lý khuyến mãi: Là một Quản trị viên trung tâm hoặc Quản lý, tôi muốn tạo, chỉnh sửa hoặc xóa các khuyến mãi (chiết khấu, ưu đãi) với ngày bắt đầu/kết thúc để học viên có thể xem các ưu đãi áp dụng.
  - **Acceptance Criteria**:
    - Cho trước một quản trị viên cung cấp Tên khuyến mãi, mô tả, điều kiện, ngày bắt đầu, ngày kết thúc, khi được lưu, thì khuyến mãi xuất hiện trong danh sách hiển thị cho học viên; nếu ngày kết thúc bị bỏ qua, khuyến mãi được coi là vĩnh viễn. *[REQ-017]*
  - **Data Inputs & Field Validations**:
    - Tên: bắt buộc, tối đa 100 ký tự.
    - Ngày bắt đầu/Ngày kết thúc: tùy chọn, định dạng YYYY‑MM‑DD.
    - Mô tả: tối đa 500 ký tự.

- **[REQ-018]** Quản lý thông báo: Là một Quản trị viên trung tâm hoặc Quản lý, tôi muốn tạo, chỉnh sửa hoặc xóa các thông báo có ngày hết hạn tùy chọn để phát sóng cho tất cả người dùng.
  - **Acceptance Criteria**:
    - Cho trước một quản trị viên nhập Tiêu đề thông báo, nội dung, tùy chọn ngày hết hạn, khi được lưu, thì thông báo được hiển thị trên toàn trang web; nếu có ngày hết hạn, nó tự động biến mất sau ngày đó. *[REQ-018]*
  - **Data Inputs & Field Validations**:
    - Tiêu đề: bắt buộc, tối đa 150 ký tự.
    - Nội dung: bắt buộc, tối đa 2000 ký tự.

### 2.9 Chatbot dịch vụ khách hàng AI

- **[REQ-019]** Tích hợp chatbot AI: Là bất kỳ người dùng nào, tôi muốn tương tác với một chatbot AI có thể trả lời các câu hỏi phổ biến về khóa học, giáo viên, trung tâm và trạng thái tài khoản.
  - **Acceptance Criteria**:
    - Cho trước một người dùng mở cửa sổ chat, khi họ hỏi một câu hỏi, thì AI trả về một câu trả lời liên quan hoặc chuyển đến hỗ trợ con người nếu độ tin cậy thấp. *[REQ-019]*
  - **Data Inputs & Field Validations**: Đầu vào văn bản, thời gian chờ phiên (timeout).

### 2.10 Tính năng cốt lõi của ứng dụng di động

- **[REQ-020]** Giao diện người dùng đặc trưng theo vai trò trên di động: Là một người dùng di động, tôi muốn một giao diện phản hồi phản ánh chức năng web cho vai trò được chỉ định của mình (Học viên, Giáo viên, Quản trị viên, v.v.).
  - **Acceptance Criteria**:
    - Cho trước một người dùng đăng nhập trên Android hoặc iOS, khi ứng dụng tải, thì menu điều hướng thích hợp và các màn hình được hiển thị dựa trên vai trò của người dùng. *[REQ-020]*
  - **Data Inputs & Field Validations**: Không có.

- **[REQ-021]** Thông báo đẩy trên di động: Là một người dùng đã đăng ký, tôi muốn nhận thông báo đẩy trên thiết bị di động cho xác nhận điểm danh, thông báo mới và tin nhắn nhắc nhở.
  - **Acceptance Criteria**:
    - Cho trước một sự kiện backend kích hoạt một thông báo đẩy, khi mã thông báo thiết bị được đăng ký, thì thông báo được chuyển qua Firebase Cloud Messaging (FCM) hoặc APNs. *[REQ-021]*
  - **Data Inputs & Field Validations**:
    - Mã thông báo thiết bị, Nền tảng (iOS/Android).

### 2.11 Bản địa hóa và SEO

- **[REQ-022]** Phát hiện ngôn ngữ mặc định: Là một khách truy cập, tôi muốn hệ thống sử dụng tùy chọn ngôn ngữ đã lưu trước đó, nếu không có, sử dụng cài đặt ngôn ngữ của trình duyệt để có trải nghiệm cá nhân hóa.
  - **Acceptance Criteria**:
    - Cho trước một người dùng truy cập trang web, khi hệ thống đánh giá ngôn ngữ, thì nó chọn ngôn ngữ đã lưu nếu có; nếu không, sử dụng tiêu đề Accept‑Language; giao diện người dùng được cập nhật tương ứng. *[REQ-022]*
  - **Data Inputs & Field Validations**: Không có.

- **[REQ-023]** SEO đa ngôn ngữ: Hệ thống phải hỗ trợ SEO cho ít nhất ba ngôn ngữ: tiếng Anh, tiếng Việt, tiếng Tây Ban Nha; mỗi trang phải bao gồm thẻ meta ngôn ngữ-specific và các liên kết hreflang.
  - **Acceptance Criteria**:
    - Cho trước một trang được yêu cầu với một ngôn ngữ cụ thể, khi trang được hiển thị, thì HTML bao gồm một thẻ <html lang='en'> và các liên kết hreflang trỏ đến các phiên bản ngôn ngữ thay thế. *[REQ-023]*
  - **Data Inputs & Field Validations**: Mã ngôn ngữ (en, vi, es).

### 2.12 Báo cáo và phân tích

- **[REQ-024]** Tạo báo cáo điểm danh: Là một quản trị viên, tôi muốn tạo một báo cáo điểm danh hàng ngày cho một trung tâm (CSV) hiển thị trạng thái hiện diện của từng học viên.
  - **Acceptance Criteria**:
    - Cho trước một quản trị viên chọn một trung tâm và khoảng thời gian, khi yêu cầu báo cáo được thực hiện, thì một tệp CSV được tạo với các cột: Tên học viên, Tên khóa học, Ngày điểm danh, Trạng thái. *[REQ-024]*
  - **Data Inputs & Field Validations**:
    - Khoảng thời gian: ngày bắt đầu ≤ ngày kết thúc, tối đa 30 ngày.

- **[REQ-025]** Bảng điều khiển tóm tắt đăng ký: Là một Quản trị viên trung tâm, tôi muốn một bảng điều khiển thời gian thực tóm tắt tổng số học viên, khóa học hoạt động và các buổi học sắp tới.
  - **Acceptance Criteria**:
    - Cho trước một quản trị viên mở bảng điều khiển, khi dữ liệu làm mới, thì các thẻ hiển thị tổng số học viên, khóa học hoạt động, các buổi học sắp tới (trong 7 ngày tới). *[REQ-025]*
  - **Data Inputs & Field Validations**: Khoảng thời gian làm mới có thể cấu hình (mặc định 15 phút).

## 3. EXCEPTION FLOWS & EDGE CASES

- **[EXC-001]** Network & Connectivity Drops During QR Scan:
  - Nếu một học viên quét QR nhưng mạng không khả dụng, khi ứng dụng thử lại yêu cầu sau khi kết nối lại, thì điểm danh được ghi lại khi dịch vụ khả dụng.

- **[EXC-002]** Duplicate Attendance Submission:
  - Nếu cùng một học viên quét cùng một mã QR của khóa học nhiều lần trong cùng một ngày, khi hệ thống phát hiện trùng lặp, thì nó trả về phản hồi thành công với cờ ‘đã ghi’ và không tạo hàng bổ sung.

- **[EXC-003]** Failed Notification Delivery:
  - Khi một thông báo đẩy không thể gửi (ví dụ: mã thông báo thiết bị không hợp lệ), thì hệ thống ghi lại thất bại và lên lịch thử lại tối đa ba lần trước khi đánh dấu là thất bại.

- **[EXC-004]** Invalid Input Validation (e.g., malformed email, missing required fields):
  - Nếu xác thực thất bại khi gửi biểu mẫu, khi lỗi được trả về cho người dùng, thì một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu sửa.

- **[EXC-005]** System Recovery After Outage:
  - Nếu dịch vụ trở nên không khả dụng, khi nó khôi phục, thì bất kỳ quét điểm danh chờ xử lý nào được xử lý theo thứ tự FIFO và người dùng nhận được thông báo về các sự kiện đã khôi phục.

## 4. NON-FUNCTIONAL REQUIREMENTS

- **[NFR-001]** Metrics Hiệu suất:
  - Các API cốt lõi (xác thực, điểm danh qua QR, danh sách khóa học) phải hoàn tất trong vòng 200 ms trung bình.
  - Các truy vấn cơ sở dữ liệu phải được lập chỉ mục để hỗ trợ khả năng đọc trong vòng dưới một giây cho tối đa 10.000 người dùng đồng thời.

- **[NFR-002]** Khả năng sẵn sàng:
  - Mục tiêu đạt 99,9 % thời gian hoạt động hàng năm; SLA bao gồm khả năng tự động chuyển đổi qua các cụm GKE.

- **[NFR-003]** Bảo mật:
  - Tất cả dữ liệu truyền qua phải sử dụng TLS 1.3; mã hóa AES‑256 khi lưu trữ.
  - Mã thông báo JWT truy cập hết hạn sau 15 phút; mã thông báo làm mới có hiệu lực 7 ngày.
  - Thực hiện các biện pháp đối phó OWASP Top 10 (SQL injection, XSS, CSRF).

- **[NFR-004]** Khả năng mở rộng và sẵn sàng:
  - Chia tỷ lệ ngang cho các dịch vụ Quarkus qua Kubernetes HPA dựa trên CPU > 70 % hoặc độ trễ yêu cầu > 300 ms.
  - Sao chép PostgreSQL để đọc cho khối lượng công việc báo cáo.

- **[NFR-005]** Kích thước Docker Image:
  - Kích thước base image < 200 MB; final image < 500 MB.

- **[NFR-006]** Logging & Audit:
  - Tất cả hành động người dùng (thay đổi vai trò, bản ghi điểm danh, thông báo) phải được ghi lại với dấu thời gian, ID người dùng và chi tiết hành động; nhật ký được lưu giữ trong 1 năm.

- **[NFR-007]** Hỗ trợ đa ngôn ngữ:
  - Các chuỗi giao diện người dùng phải được ngoại vị hóa; hỗ trợ tiếng Anh, tiếng Việt, tiếng Tây Ban Nha; chuyển đổi ngôn ngữ mà không cần tải lại trang nơi khả thi.

- **[NFR-008]** Tuân thủ GDPR/CCPA:
  - Xóa dữ liệu cá nhân theo yêu cầu của người dùng; xuất dữ liệu ở định dạng JSON; quản lý sự đồng ý cho truyền thông tiếp thị.

- **[NFR-009]** Sao lưu và khôi phục sau thảm họa:
  - Sao lưu PostgreSQL hàng ngày (toàn bộ); khả năng khôi phục tại một thời điểm nhất định lên đến 24 giờ; sao lưu cụm GKE đến khu vực riêng biệt.

## 5. PRELIMINARY DATA DICTIONARY

| Thực thể | Trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|--------|-------|------------|------------|-------------|
| Người dùng | user_id | UUID | PK, not null | Định danh duy nhất |
| | email | VARCHAR(255) | not null, unique | Định danh đăng nhập chính |
| | password_hash | CHAR(60) | not null | Băm bcrypt |
| | full_name | VARCHAR(100) | not null | Tên thật |
| | role_id | SMALLINT | FK → Roles.role_id | Vai trò được chỉ định |
| | provider | ENUM('local','firebase','google','facebook') | default 'local' | Nhà cung cấp xác thực |
| | created_at | TIMESTAMP | not null, default now() | Thời điểm tạo tài khoản |
| | updated_at | TIMESTAMP | not null, default now() | Lần cập nhật cuối |
| Trung tâm | center_id | UUID | PK, not null | Định danh duy nhất |
| | name | VARCHAR(100) | not null | Tên trung tâm |
| | address | VARCHAR(255) | not null | Địa chỉ thực tế |
| | tax_id | VARCHAR(20) | unique, not null | Mã số thuế |
| | contact_phone | VARCHAR(20) | optional | Số điện thoại liên hệ |
| | contact_email | VARCHAR(100) | optional | Email liên hệ |
| Khóa học | course_id | UUID | PK, not null | Định danh duy nhất |
| | title | VARCHAR(150) | not null | Tên khóa học |
| | description | TEXT | optional | Mô tả chi tiết |
| | start_date | DATE | not null | Ngày bắt đầu khóa học |
| | end_date | DATE | not null | Ngày kết thúc khóa học |
| | teacher_id | UUID | FK → Users.user_id | Giáo viên được chỉ định |
| | max_students | INT | default 30 | Sức chứa |
| Đăng ký | enrollment_id | UUID | PK, not null | Định danh duy nhất |
| | student_id | UUID | FK → Users.user_id | Học viên đăng ký |
| | course_id | UUID | FK → Courses.course_id | Khóa học |
| | enrollment_date | TIMESTAMP | default now() | Thời điểm đăng ký |
| Điểm danh | attendance_id | UUID | PK, not null | Định danh duy nhất |
| | student_id | UUID | FK → Users.user_id | Học viên có mặt |
| | course_id | UUID | FK → Courses.course_id | Khóa học |
| | attendance_date | DATE | not null | Ngày điểm danh |
| | timestamp | TIMESTAMP | default now() | Thời điểm ghi chính xác |
| Thẻ hội viên | card_id | UUID | PK, not null | Định danh duy nhất |
| | student_id | UUID | FK → Users.user_id | Chủ sở hữu |
| | issue_date | DATE | not null | Ngày phát hành thẻ |
| | validity_days | INT | not null | Tổng số ngày hiệu lực |
| | remaining_days | INT | computed | Số ngày còn lại đến hết hạn |
| Thông báo | notification_id | UUID | PK, not null | Định danh duy nhất |
| | user_id | UUID | FK → Users.user_id (optional) | Đối tượng mục tiêu |
| | group_zalo | VARCHAR(50) | optional | Nhóm Zalo mục tiêu |
| | message | TEXT | not null | Nội dung thông báo |
| | sent_at | TIMESTAMP | default now() | Thời điểm gửi |
| | delivered | BOOLEAN | default false | Trạng thái giao hàng |
| Vai trò | role_id | SMALLINT | PK | Định danh vai trò |
| | name | VARCHAR(30) | unique, not null | Tên vai trò |
| | description | VARCHAR(200) | optional | Mô tả vai trò |
| Khuyến mãi | promo_id | UUID | PK, not null | Định danh duy nhất |
| | code | VARCHAR(30) | unique | Mã khuyến mãi |
| | discount_percent | SMALLINT | not null | Phần trăm chiết khấu |
| | start_date | DATE | optional | Ngày bắt đầu khuyến mãi |
| | end_date | DATE | optional | Ngày kết thúc khuyến mãi |
| | description | TEXT | optional | Chi tiết khuyến mãi |
| Thông báo | announcement_id | UUID | PK, not null | Định danh duy nhất |
| | title | VARCHAR(150) | not null | Tiêu đề |
| | content | TEXT | not null | Nội dung |
| | start_date | DATE | optional | Ngày hiệu lực bắt đầu |
| | end_date | DATE | optional | Ngày hiệu lực kết thúc |
| Cài đặt hệ thống | setting_key | VARCHAR(50) | PK | Khóa cấu hình |
| | setting_value | TEXT | not null | Giá trị cấu hình |
| | description | VARCHAR(200) | optional | Ý nghĩa của cài đặt |
