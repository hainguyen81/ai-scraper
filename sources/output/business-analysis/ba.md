{
  "project_names": {
    "technical_codename": "membership-hub",
    "descriptive_name": "Nền tảng quản lý hội viên đa trung tâm",
    "brand_name": "HubMember"
  },
  "srs_content_markdown": "## 1. TỔNG QUAN DỰ ÁN & KIẾN TRÚC TOÀN CẦU
- Mục tiêu sản phẩm & giá trị cốt lõi:
  - Cung cấp một nền tảng thống nhất để quản lý hội viên trên nhiều trung tâm.
  - Cho phép theo dõi điểm danh thời gian thực thông qua quét mã QR.
  - Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
  - Hỗ trợ truyền thông đa kênh (web, di động, nhóm Zalo).
  - Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.
- Đối tượng người dùng:
  - Quản trị viên hệ thống (super‑user toàn cầu)
  - Quản trị viên trung tâm (quản lý cấp trung tâm)
  - Quản lý (phó quản trị, quyền hạn giới hạn)
  - Giáo viên (chỉ đọc lịch học)
  - Học viên (duyệt khóa học, đăng ký, xem thẻ hội viên)
  - Người dùng ứng dụng di động (cùng các vai trò, giao diện phản hồi)
- Ma trận RBAC toàn cầu:
  - [ARC-001] Quản trị viên hệ thống: toàn quyền trên tất cả các trung tâm.
  - [ARC-002] Quản trị viên trung tâm: toàn quyền trong trung tâm của mình, không ảnh hưởng các trung tâm khác.
  - [ARC-003] Quản lý: có thể tạo thông báo, quản lý học viên, chỉ định học viên hiện có vào khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
  - [ARC-004] Giáo viên: xem khóa học của mình, danh sách học viên, lịch trình; chỉ đọc.
  - [ARC-005] Học viên: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày hiệu lực còn lại), gia hạn thẻ.
- Kiến trúc công nghệ & ràng buộc hạ tầng:
  - [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT với hạn dùng 15 phút và refresh token.
  - [ARC-007] Luồng xử lý QR điểm danh: ứng dụng di động quét QR, gửi studentID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
  - [ARC-008] Luồng truyền thông thông báo: hệ thống kích hoạt push notification đến ứng dụng di động và đăng tải lên nhóm Zalo được chỉ định cho thông báo, chỉ định khóa học và cảnh báo điểm danh.
  - [ARC-009] Tích hợp backend ứng dụng di động: Next.js frontend tiêu thụ REST APIs; xác thực qua bearer token; hỗ trợ lưu trữ ngoại tuyến cho trường hợp kết nối hạn chế.

## 2. QUẢN LÝ NGƯỜI DÙNG
### 2.1 Đăng ký người dùng
- **[REQ-001]** Đăng ký người dùng: Là một người dùng tiềm năng, tôi muốn đăng ký bằng email và mật khẩu (hoặc nhà cung cấp xã hội) để có thể có một tài khoản trong hệ thống.
  - **Tiêu chí chấp nhận**:
    - Giả sử người dùng cung cấp một email duy nhất, một mật khẩu mạnh, và đồng ý với điều khoản, khi họ gửi biểu mẫu đăng ký, sau đó hệ thống xác thực đầu vào, tạo một bản ghi người dùng mới với vai trò ‘Học viên’ (hoặc ‘Giáo viên’ nếu được mời), và trả về phản hồi thành công với một JWT token. *[REQ-001]*
  - **Dữ liệu đầu vào & xác thực trường**:
    - Email: bắt buộc, tối đa 255 ký tự, phải chứa một ‘@’ và phần tên miền (ví dụ: user@example.com). Phải duy nhất.
    - Mật khẩu: bắt buộc, tối thiểu 8 ký tự, ít nhất một chữ hoa, một chữ thường, một chữ số, một ký tự đặc biệt.
    - Điều khoản: ô kiểm bắt buộc.

### 2.2 Xác thực xã hội
- **[REQ-002]** Xác thực xã hội: Là một người dùng, tôi muốn đăng nhập/đăng ký bằng Firebase, Google, hoặc Facebook OAuth để có thể tận dụng thông tin xác thực hiện có.
  - **Tiêu chí chấp nhận**:
    - Giả sử người dùng chọn một nhà cung cấp, khi họ xác thực qua cửa sổ popup của nhà cung cấp, sau đó hệ thống nhận một mã OAuth2, trao đổi mã để lấy thông tin người dùng, tạo hoặc cập nhật bản ghi người dùng cục bộ, và cấp một JWT token. *[REQ-002]*
  - **Dữ liệu đầu vào & xác thực trường**: mã thông báo nhà cung cấp, hình ảnh hồ sơ tùy chọn.

### 2.3 Phân quyền vai trò người dùng
- **[REQ-003]** Phân quyền vai trò người dùng: Là một quản trị viên, tôi muốn chỉ định hoặc thay đổi vai trò của một người dùng (Quản trị viên hệ thống, Quản trị viên trung tâm, Quản lý, Giáo viên, Học viên) để các quyền hạn được thực thi chính xác.
  - **Tiêu chí chấp nhận**:
    - Giả sử một quản trị viên chọn một người dùng và một vai trò mới, khi việc chỉ định được xác nhận, sau đó vai trò của người dùng được cập nhật, và các quyền hạn tương ứng được áp dụng ngay lập tức. *[REQ-003]*
  - **Dữ liệu đầu vào & xác thực trường**: ô chọn vai trò, bản ghi nhật ký bắt buộc.

## 3. QUẢN LÝ TRUNG TÂM
### 3.1 Xem danh sách trung tâm
- **[REQ-004]** Xem danh sách trung tâm: Là bất kỳ người dùng đã xác thực, tôi muốn xem danh sách tất cả các trung tâm với địa chỉ, mã số thuế, và liên hệ quản trị viên để có thể xác định các trung tâm liên quan.
  - **Tiêu chí chấp nhận**:
    - Giả sử một người dùng điều hướng đến trang Trung tâm, khi yêu cầu hoàn tất, sau đó một bảng các trung tâm (Tên, Địa chỉ, Mã số thuế, Liên hệ quản trị viên) được hiển thị. *[REQ-004]*
  - **Dữ liệu đầu vào & xác thực trường**: Không có (chỉ đọc).

### 3.2 Tạo/Sửa/Xóa trung tâm
- **[REQ-005]** Tạo/Sửa/Xóa trung tâm: Là một Quản trị viên hệ thống, tôi muốn thêm, chỉnh sửa, hoặc xóa một bản ghi trung tâm để thông tin trung tâm luôn được cập nhật.
  - **Tiêu chí chấp nhận**:
    - Giả sử một Quản trị viên hệ thống cung cấp tên trung tâm, địa chỉ, mã số thuế, điện thoại liên hệ và email, khi hành động lưu được thực thi, sau đó trung tâm được lưu trữ và xuất hiện trong danh sách; nếu mã số thuế trùng lặp, thao tác thất bại với lỗi xung đột. *[REQ-005]*
  - **Dữ liệu đầu vào & xác thực trường**:
    - Tên: bắt buộc, tối đa 100 ký tự.
    - Địa chỉ: bắt buộc, tối đa 255 ký tự.
    - Mã số thuế: bắt buộc, số, 10‑13 chữ số, duy nhất.
    - Điện thoại liên hệ: tùy chọn, có thể bao gồm +, chữ số, khoảng trắng, dấu gạch ngang, ngoặc đơn.
    - Email liên hệ: tùy chọn, phải là định dạng email hợp lệ.

### 3.3 Phân quyền quản trị viên trung tâm
- **[REQ-006]** Phân quyền quản trị viên trung tâm: Là một Quản trị viên hệ thống, tôi muốn chỉ định hoặc hủy chỉ định một người dùng làm Quản trị viên trung tâm cho một trung tâm cụ thể để phân quyền quản trị.
  - **Tiêu chí chấp nhận**:
    - Giả sử một Quản trị viên hệ thống chọn một người dùng và một trung tâm, khi hành động chỉ định được xác nhận, sau đó vai trò của người dùng được thiết lập thành ‘Quản trị viên trung tâm’ và ID trung tâm được ghi lại; thao tác hủy chỉ định đảo ngược thao tác. *[REQ-006]*
  - **Dữ liệu đầu vào & xác thực trường**: ID người dùng, ID trung tâm.

## 4. QUẢN LÝ KHÓA HỌC
### 4.1 Xem danh sách khóa học
- **[REQ-007]** Xem danh sách khóa học: Là bất kỳ người dùng đã xác thực, tôi muốn xem tất cả các khóa học với lịch học và giáo viên được chỉ định để có thể duyệt các khóa học được cung cấp.
  - **Tiêu chí chấp nhận**:
    - Giả sử một người dùng truy cập trang Khóa học, khi yêu cầu hoàn tất, sau đó một lưới hiển thị CourseID, Tiêu đề, Ngày bắt đầu, Ngày kết thúc, Tên giáo viên được hiển thị. *[REQ-007]*
  - **Dữ liệu đầu vào & xác thực trường**: Không có.

### 4.2 Tạo/Sửa/Xóa khóa học (Tránh xung đột)
- **[REQ-008]** Tạo/Sửa/Xóa khóa học (Tránh xung đột): Là một Quản trị viên hệ thống hoặc Quản trị viên trung tâm, tôi muốn quản lý các khóa học (thêm, chỉnh sửa, xóa) trong khi đảm bảo không có lịch học trùng lặp cho cùng một giáo viên hoặc địa điểm.
  - **Tiêu chí chấp nhận**:
    - Giả sử một quản trị viên cung cấp CourseTitle, StartDate, EndDate, TeacherID, khi hành động lưu được kích hoạt, sau đó hệ thống xác thực rằng giáo viên không được lên lịch cho một khóa học khác chồng lấn các ngày này; nếu xung đột, một lỗi được trả về; nếu không, khóa học được lưu trữ. *[REQ-008]*
  - **Dữ liệu đầu vào & xác thực trường**:
    - Tiêu đề: bắt buộc, tối đa 150 ký tự.
    - Ngày bắt đầu/Ngày kết thúc: bắt buộc, Ngày kết thúc >= Ngày bắt đầu.
    - TeacherID: bắt buộc, khóa ngoại.
    - Logic kiểm tra chồng lấn được thực thi ở cấp DB/trigger.

### 4.3 Chỉ định giáo viên cho khóa học
- **[REQ-009]** Chỉ định giáo viên cho khóa học: Là một Quản trị viên hệ thống, tôi muốn chỉ định hoặc hủy chỉ định giáo viên cho khóa học để cập nhật trách nhiệm giảng dạy.
  - **Tiêu chí chấp nhận**:
    - Giả sử một quản trị viên chọn một khóa học và một giáo viên, khi hành động chỉ định được thực thi, sau đó ánh xạ giáo viên-khóa học được tạo và một thông báo được xếp hàng cho ứng dụng di động của giáo viên; thao tác hủy chỉ định xóa ánh xạ. *[REQ-009]*
  - **Dữ liệu đầu vào & xác thực trường**: CourseID, TeacherID (phải tồn tại).

## 5. ĐĂNG KÝ & GHI DÁNH HỌC VIÊN
### 5.1 Duyệt khóa học
- **[REQ-010]** Duyệt khóa học: Là một Học viên, tôi muốn duyệt các khóa học có sẵn (loại trừ các khóa học mà tôi đã đăng ký) để có thể chọn các khóa học để tham gia.
  - **Tiêu chí chấp nhận**:
    - Giả sử một Học viên đăng nhập và điều hướng đến trang Duyệt Khóa học, khi yêu cầu hoàn tất, sau đó một danh sách các khóa học với sức chứa và lịch học được hiển thị, loại trừ các khóa học mà học viên đã có bản ghi đăng ký. *[REQ-010]*
  - **Dữ liệu đầu vào & xác thực trường**: Không có.

### 5.2 Đăng ký khóa học
- **[REQ-011]** Đăng ký khóa học: Là một Học viên, tôi muốn đăng ký cho một khóa học (hiện có hoặc mới), điều này tự động tạo một tài khoản Học viên nếu chưa có, và chỉ định học viên vào khóa học.
  - **Tiêu chí chấp nhận**:
    - Giả sử một Học viên chọn một khóa học và gửi đăng ký, khi backend xử lý yêu cầu, sau đó một bản ghi đăng ký mới được tạo; nếu học viên chưa có tài khoản cục bộ, một tài khoản được tạo với vai trò ‘Học viên’; một thông báo được xếp hàng cho ứng dụng di động của học viên và nhóm Zalo của trung tâm. *[REQ-011]*
  - **Dữ liệu đầu vào & xác thực trường**:
    - CourseID: bắt buộc, phải là khóa học đang hoạt động.
    - StudentID: được suy ra từ token xác thực (hoặc tạo trên‑the‑fly).

## 6. ĐIỂM DANH & QUÉT QR
### 6.1 Ghi lại điểm danh bằng QR
- **[REQ-012]** Ghi lại điểm danh bằng QR: Là một Học viên (qua ứng dụng di động), tôi muốn quét một mã QR tại điểm danh để điểm danh của tôi được ghi lại cho ngày hiện tại.
  - **Tiêu chí chấp nhận**:
    - Giả sử một Học viên mở máy quét, quét một mã QR hợp lệ của khóa học và xác nhận điểm danh, khi API nhận payload, sau đó hệ thống xác thực mối quan hệ học viên‑khóa học, tạo một bản ghi Điểm danh với timestamp, và trả về phản hồi thành công; các lần quét trùng lặp trong cùng một ngày bị bỏ qua. *[REQ-012]*
  - **Dữ liệu đầu vào & xác thực trường**:
    - Payload QR: chuỗi base64 chứa studentID và courseID.
    - Xác thực: học viên phải được ghi danh vào khóa học cho ngày đó.

### 6.2 Idempotency điểm danh
- **[REQ-013]** Idempotency điểm danh: Dịch vụ điểm danh phải đảm bảo rằng nhiều lần quét từ cùng một học viên cho cùng một khóa học trong cùng một ngày tạo ra một bản ghi điểm danh duy nhất.
  - **Tiêu chí chấp nhận**:
    - Giả sử một học viên quét QR hai lần trong vòng một phút, khi dịch vụ xử lý cả hai yêu cầu, sau đó chỉ một hàng điểm danh được tạo; các yêu cầu tiếp theo trả về thành công với một cờ ‘đã ghi’.
  - **Dữ liệu đầu vào & xác thực trường**: Khóa chính tổng hợp (StudentID, CourseID, Ngày).

## 7. QUẢN LÝ THẺ HỌVIÊN
### 7.1 Hiển thị hiệu lực thẻ
- **[REQ-014]** Hiển thị hiệu lực thẻ: Là một Học viên, tôi muốn xem thẻ hội viên của mình hiển thị ngày hiệu lực còn lại để biết khi nào cần gia hạn.
  - **Tiêu chí chấp nhận**:
    - Giả sử một Học viên mở trang Thẻ, khi yêu cầu tải, sau đó giao diện hiển thị tổng số ngày hiệu lực, ngày đã sử dụng, và ngày còn lại; dữ liệu được suy ra từ thực thể StudentCard.
  - **Dữ liệu đầu vào & xác thực trường**: Không có (chỉ đọc).

### 7.2 Gia hạn thẻ
- **[REQ-015]** Gia hạn thẻ: Là một Học viên, tôi muốn gia hạn thẻ hội viên của mình bằng cách thanh toán một khoản phí, điều này cập nhật ngày kết thúc.
  - **Tiêu chí chấp nhận**:
    - Giả sử một Học viên chọn một khoảng thời gian gia hạn (ví dụ: 30 ngày), xác nhận thanh toán, khi dịch vụ thanh toán xác nhận thành công, sau đó ngày kết thúc của StudentCard được mở rộng thêm số ngày đã chọn và một thông báo xác nhận được gửi.
  - **Dữ liệu đầu vào & xác thực trường**:
    - RenewalDays: số nguyên, 1‑365.
    - Tích hợp cổng thanh toán yêu cầu (ngoài phạm vi).

## 8. THÔNG BÁO & TRUYỀN THÔNG
### 8.1 Kích hoạt thông báo
- **[REQ-016]** Kích hoạt thông báo: Khi một quản trị viên tạo một thông báo, chỉ định một giáo viên cho một khóa học, hoặc đăng ký một học viên, hệ thống phải tạo một thông báo cho ứng dụng di động của học viên và đăng tải lên nhóm Zalo được chỉ định cho thông báo, chỉ định khóa học và cảnh báo điểm danh.
  - **Tiêu chí chấp nhận**:
    - Giả sử một quản trị viên thực hiện một hành động yêu cầu thông báo, khi hành động được lưu, sau đó một bản ghi Thông báo được tạo, một payload thông báo push được xếp hàng cho ứng dụng di động, và một tin nhắn văn bản được gửi đến nhóm chat Zalo. *[REQ-016]*
  - **Dữ liệu đầu vào & xác thực trường**: Đối tượng mục tiêu (học viên, giáo viên, nhóm), nội dung thông báo, phương tiện tùy chọn.

## 9. QUẢN LÝ KHUYẾN MÃI & THÔNG BÁO
### 9.1 Quản lý khuyến mãi
- **[REQ-017]** Quản lý khuyến mãi: Là một Quản trị viên trung tâm hoặc Quản lý, tôi muốn tạo, chỉnh sửa, hoặc xóa các khuyến mãi (giảm giá, ưu đãi) với ngày bắt đầu/kết thúc để học viên có thể xem các ưu đãi áp dụng.
  - **Tiêu chí chấp nhận**:
    - Giả sử một quản trị viên cung cấp PromotionName, mô tả, điều kiện, startDate, endDate, khi lưu, sau đó khuyến mãi xuất hiện trong danh sách hiển thị cho học viên; nếu endDate bị bỏ qua, khuyến mãi được coi là vĩnh viễn. *[REQ-017]*
  - **Dữ liệu đầu vào & xác thực trường**:
    - Tên: bắt buộc, tối đa 100 ký tự.
    - Ngày bắt đầu/Ngày kết thúc: tùy chọn, định dạng YYYY‑MM‑DD.
    - Mô tả: tối đa 500 ký tự.

### 9.2 Quản lý thông báo
- **[REQ-018]** Quản lý thông báo: Là một Quản trị viên trung tâm hoặc Quản lý, tôi muốn tạo, chỉnh sửa, hoặc xóa các thông báo với ngày hết hạn tùy chọn để phát sóng cho tất cả người dùng.
  - **Tiêu chí chấp nhận**:
    - Giả sử một quản trị viên nhập AnnouncementTitle, nội dung, hết hạn tùy chọn, khi lưu, sau đó thông báo được hiển thị trên toàn trang web; nếu hết hạn được đặt, nó tự động biến mất sau ngày đó. *[REQ-018]*
  - **Dữ liệu đầu vào & xác thực trường**:
    - Tiêu đề: bắt buộc, tối đa 150 ký tự.
    - Nội dung: bắt buộc, tối đa 2000 ký tự.

## 10. CHATBOT DỊCH VỤ KHÁCH HÀNG AI
### 10.1 Tích hợp chatbot AI
- **[REQ-019]** Tích hợp chatbot AI: Là bất kỳ người dùng, tôi muốn tương tác với một chatbot AI có thể trả lời các câu hỏi phổ biến về khóa học, giáo viên, trung tâm, và trạng thái tài khoản.
  - **Tiêu chí chấp nhận**:
    - Giả sử một người dùng mở cửa sổ chat, khi họ đặt câu hỏi, sau đó AI trả về một câu trả lời phù hợp hoặc chuyển đến hỗ trợ con người nếu độ tin cậy thấp. *[REQ-019]*
  - **Dữ liệu đầu vào & xác thực trường**: Văn bản đầu vào, thời gian chờ phiên.

## 11. TÍNH NĂNG ỨNG DỤNG DI ĐỘNG
### 11.1 Giao diện người dùng vai trò trên di động
- **[REQ-020]** Giao diện người dùng vai trò trên di động: Là một người dùng di động, tôi muốn một giao diện phản hồi phản ánh chức năng web cho vai trò được chỉ định của tôi (Học viên, Giáo viên, Quản trị, v.v.).
  - **Tiêu chí chấp nhận**:
    - Giả sử một người dùng đăng nhập trên Android hoặc iOS, khi ứng dụng tải, sau đó menu điều hướng và các màn hình thích hợp được hiển thị dựa trên vai trò của người dùng. *[REQ-020]*
  - **Dữ liệu đầu vào & xác thực trường**: Không có.

### 11.2 Thông báo đẩy trên di động
- **[REQ-021]** Thông báo đẩy trên di động: Là một người dùng đã đăng ký, tôi muốn nhận thông báo đẩy trên thiết bị di động của mình cho các xác nhận điểm danh, thông báo mới, và tin nhắn nhắc nhở.
  - **Tiêu chí chấp nhận**:
    - Giả sử một sự kiện backend kích hoạt một thông báo, khi token thiết bị được đăng ký, sau đó thông báo được phân phối qua Firebase Cloud Messaging (FCM) hoặc APNs. *[REQ-021]*
  - **Dữ liệu đầu vào & xác thực trường**: DeviceToken, Platform (iOS/Android).

## 12. BẢN ĐỊNH LOCALIZATION & SEO
### 12.1 Phát hiện ngôn ngữ mặc định
- **[REQ-022]** Phát hiện ngôn ngữ mặc định: Là một khách truy cập, tôi muốn hệ thống sử dụng ngôn ngữ ưu tiên đã lưu của tôi, rơi về cài đặt ngôn ngữ trình duyệt, để có một trải nghiệm cá nhân hóa.
  - **Tiêu chí chấp nhận**:
    - Giả sử một người dùng truy cập trang web, khi hệ thống đánh giá ngôn ngữ, sau đó nó chọn ngôn ngữ đã lưu nếu có; nếu không, sử dụng tiêu đề Accept‑Language; giao diện cập nhật tương ứng. *[REQ-022]*
  - **Dữ liệu đầu vào & xác thực trường**: Không có.

### 12.2 SEO đa ngôn ngữ
- **[REQ-023]** SEO đa ngôn ngữ: Nền tảng phải hỗ trợ SEO cho ít nhất tiếng Anh, tiếng Việt, và tiếng Tây Ban Nha; mỗi trang phải bao gồm các thẻ meta ngôn ngữ cụ thể và các liên kết hreflang.
  - **Tiêu chí chấp nhận**:
    - Giả sử một trang được yêu cầu với một ngôn ngữ cụ thể, khi trang được render, sau đó HTML bao gồm một thẻ <html lang='en'> và các liên kết hreflang trỏ đến các phiên bản ngôn ngữ thay thế. *[REQ-023]*
  - **Dữ liệu đầu vào & xác thực trường**: Mã ngôn ngữ (en, vi, es).

## 13. BÁO CÁO & PHÂN TÍCH
### 13.1 Tạo báo cáo điểm danh
- **[REQ-024]** Tạo báo cáo điểm danh: Là một quản trị viên, tôi muốn tạo một báo cáo điểm danh hàng ngày cho một trung tâm (CSV) hiển thị tình trạng điểm danh của từng học viên.
  - **Tiêu chí chấp nhận**:
    - Giả sử một quản trị viên chọn một trung tâm và khoảng thời gian, khi báo cáo được yêu cầu, sau đó một tệp CSV được tạo với các cột: Tên học viên, Tên khóa học, Ngày điểm danh, Trạng thái. *[REQ-024]*
  - **Dữ liệu đầu vào & xác thực trường**:
    - Khoảng thời gian: bắt đầu ≤ kết thúc, tối đa 30 ngày.

### 13.2 Bảng điều khiển tóm tắt đăng ký
- **[REQ-025]** Bảng điều khiển tóm tắt đăng ký: Là một Quản trị viên trung tâm, tôi muốn một bảng điều khiển thời gian thực tóm tắt tổng số học viên, khóa học đang hoạt động, và các phiên học sắp tới.
  - **Tiêu chí chấp nhận**:
    - Giả sử một quản trị viên mở bảng điều khiển, khi dữ liệu được làm mới, sau đó các thẻ hiển thị totalStudents, activeCourses, upcomingSessions (7 ngày tới). *[REQ-025]*
  - **Dữ liệu đầu vào & xác thực trường**: Khoảng thời gian làm mới có thể cấu hình (mặc định 15 phút).

## 14. LUỒNG NGOẠI LE & TRƯỜNG HỢP ĐẶC BIỆT
- **[EXC-001]** Mất mạng & ngắt kết nối trong khi quét QR:
  - Nếu một học viên quét một QR nhưng mạng không khả dụng, khi ứng dụng thử lại yêu cầu sau khi kết nối lại, sau đó điểm danh được ghi lại khi dịch vụ có thể truy cập.
- **[EXC-002]** Gửi điểm danh trùng lặp:
  - Nếu cùng một học viên quét cùng một mã QR khóa học nhiều lần trong cùng một ngày, khi hệ thống phát hiện trùng lặp, sau đó nó trả về một phản hồi thành công chỉ ra ‘đã ghi’ và không tạo các hàng bổ sung.
- **[EXC-003]** Gửi thông báo thất bại:
  - Khi một thông báo đẩy không thể được gửi (ví dụ: token thiết bị không hợp lệ), sau đó hệ thống ghi lại lỗi và lên lịch một lần thử lại lên đến ba lần trước khi đánh dấu là thất bại.
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: email sai định dạng, thiếu trường bắt buộc):
  - Nếu xác thực thất bại trên gửi biểu mẫu, khi lỗi được trả về cho người dùng, sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.
- **[EXC-005]** Khôi phục hệ thống sau sự cố:
  - Nếu dịch vụ không khả dụng, khi nó khôi phục, sau đó bất kỳ quét QR điểm danh đang chờ xử lý được xử lý theo thứ tự FIFO, và người dùng nhận được một thông báo về các sự kiện đã khôi phục.

## 15. YÊU CẦU KHÔNG CHỨC NĂNG TOÀN CẦU
- **[NFR-001]** Chỉ số hiệu năng:
  - Các phản hồi API cốt lõi (xác thực, ghi điểm danh, danh sách khóa học) phải hoàn tất trong vòng 200 ms trung bình.
  - Các truy vấn cơ sở dữ liệu phải được lập chỉ mục để hỗ trợ đọc trong vòng dưới một giây cho tối đa 10.000 người dùng đồng thời.
- **[NFR-002]** Khả năng sẵn sàng:
  - Mục tiêu 99,9% thời gian hoạt động hàng năm; SLA bao gồm khả năng chuyển đổi tự động qua các cluster GKE.
- **[NFR-003]** Bảo mật:
  - Tất cả dữ liệu trong quá trình truyền phải sử dụng TLS 1.3; mã hóa AES‑256 khi lưu trữ.
  - JWT access token hết hạn sau 15 phút; refresh token có 7 ngày hiệu lực.
  - Thực hiện các biện pháp bảo vệ OWASP Top 10 (SQL injection, XSS, CSRF).
- **[NFR-004]** Khả năng mở rộng & tính sẵn sàng:
  - Mở rộng theo chiều ngang các dịch vụ Quarkus qua Kubernetes HPA dựa trên CPU > 70% hoặc độ trễ yêu cầu > 300 ms.
  - PostgreSQL read replicas cho khối lượng công việc báo cáo.
- **[NFR-005]** Kích thước hình ảnh Docker:
  - Hình ảnh cơ sở < 200 MB; hình ảnh cuối cùng < 500 MB.
- **[NFR-006]** Ghi nhật ký & kiểm toán:
  - Tất cả các hành động người dùng (thay đổi vai trò, bản ghi điểm danh, thông báo) phải được ghi nhật ký với dấu thời gian, ID người dùng, và chi tiết hành động; nhật ký được lưu trữ trong 1 năm.
- **[NFR-007]** Hỗ trợ đa ngôn ngữ:
  - Chuỗi UI phải được bên ngoài hóa; hỗ trợ tiếng Anh, tiếng Việt, tiếng Tây Ban Nha; chuyển đổi ngôn ngữ mà không cần tải lại trang web nếu có thể.
- **[NFR-008]** Tuân thủ GDPR/CCPA:
  - Xóa dữ liệu cá nhân theo yêu cầu của người dùng; xuất dữ liệu ở định dạng JSON; quản lý sự đồng ý cho truyền thông tiếp thị.
- **[NFR-009]** Sao lưu & khôi phục sau thảm họa:
  - Sao lưu PostgreSQL đầy đủ hàng ngày; khả năng phục hồi tại một thời điểm nhất định lên đến 24 giờ; sao lưu cluster GKE sang khu vực riêng biệt.

## 16. BẢNG TRA CỨU DỮ LIỆU (DAT)
**[DAT-001]** Bảng Users:
- user_id: UUID, PK, không null, mô tả: Định danh duy nhất
- email: VARCHAR(255), không null, duy nhất, mô tả: Địa chỉ email đăng nhập
- password_hash: CHAR(60), không null, mô tả: Băm bcrypt
- full_name: VARCHAR(100), không null, mô tả: Tên thật
- role_id: SMALLINT, FK → Roles.role_id, mô tả: Vai trò được chỉ định
- provider: ENUM('local','firebase','google','facebook'), mặc định 'local', mô tả: Nhà cung cấp xác thực
- created_at: TIMESTAMP, không null, mặc định now(), mô tả: Thời điểm tạo tài khoản
- updated_at: TIMESTAMP, không null, mặc định now(), mô tả: Thời điểm cập nhật cuối

**[DAT-002]** Bảng Centers:
- center_id: UUID, PK, không null, mô tả: Định danh duy nhất
- name: VARCHAR(100), không null, mô tả: Tên trung tâm
- address: VARCHAR(255), không null, mô tả: Địa chỉ vật lý
- tax_id: VARCHAR(20), duy nhất, không null, mô tả: Số nhận dạng thuế
- contact_phone: VARCHAR(20), tùy chọn, mô tả: Số điện thoại liên hệ
- contact_email: VARCHAR(100), tùy chọn, mô tả: Email liên hệ

**[DAT-003]** Bảng Courses:
- course_id: UUID, PK, không null, mô tả: Định danh duy nhất
- title: VARCHAR(150), không null, mô tả: Tên khóa học
- description: TEXT, tùy chọn, mô tả: Mô tả chi tiết
- start_date: DATE, không null, mô tả: Ngày bắt đầu khóa học
- end_date: DATE, không null, mô tả: Ngày kết thúc khóa học
- teacher_id: UUID, FK → Users.user_id, mô tả: Giáo viên được chỉ định
- max_students: INT, mặc định 30, mô tả: Sức chứa

**[DAT-004]** Bảng Enrollments:
- enrollment_id: UUID, PK, không null, mô tả: Định danh duy nhất
- student_id: UUID, FK → Users.user_id, mô tả: Học viên ghi danh
- course_id: UUID, FK → Courses.course_id, mô tả: Khóa học
- enrollment_date: TIMESTAMP, mặc định now(), mô tả: Khi ghi danh

**[DAT-005]** Bảng Attendance:
- attendance_id: UUID, PK, không null, mô tả: Định danh duy nhất
- student_id: UUID, FK → Users.user_id, mô tả: Học viên có mặt
- course_id: UUID, FK → Courses.course_id, mô tả: Khóa học
- attendance_date: DATE, không null, mô tả: Ngày điểm danh
- timestamp: TIMESTAMP, mặc định now(), mô tả: Thời điểm chính xác ghi lại

**[DAT-006]** Bảng StudentCards:
- card_id: UUID, PK, không null, mô tả: Định danh duy nhất
- student_id: UUID, FK → Users.user_id, mô tả: Chủ sở hữu
- issue_date: DATE, không null, mô tả: Ngày phát hành thẻ
- validity_days: INT, không null, mô tả: Tổng số ngày hiệu lực
- remaining_days: INT, tính toán, mô tả: Số ngày còn lại

**[DAT-007]** Bảng Notifications:
- notification_id: UUID, PK, không null, mô tả: Định danh duy nhất
- user_id: UUID, FK → Users.user_id, tùy chọn, mô tả: Người dùng mục tiêu
- group_zalo: VARCHAR(50), tùy chọn, mô tả: Nhóm Zalo mục tiêu
- message: TEXT, không null, mô tả: Nội dung thông báo
- sent_at: TIMESTAMP, mặc định now(), mô tả: Khi gửi
- delivered: BOOLEAN, mặc định false, mô tả: Trạng thái phân phối

**[DAT-008]** Bảng Roles:
- role_id: SMALLINT, PK, mô tả: Định danh vai trò
- name: VARCHAR(30), duy nhất, không null, mô tả: Tên vai trò
- description: VARCHAR(200), tùy chọn, mô tả: Mô tả vai trò

**[DAT-009]** Bảng Promotions:
- promo_id: UUID, PK, không null, mô tả: Định danh duy nhất
- code: VARCHAR(30), duy nhất, mô tả: Mã giảm giá
- discount_percent: SMALLINT, không null, mô tả: Tỷ lệ phần trăm giảm giá
- start_date: DATE, tùy chọn, mô tả: Ngày bắt đầu khuyến mãi
- end_date: DATE, tùy chọn, mô tả: Ngày kết thúc khuyến mãi
- description: TEXT, tùy chọn, mô tả: Chi tiết khuyến mãi

**[DAT-010]** Bảng Announcements:
- announcement_id: UUID, PK, không null, mô tả: Định danh duy nhất
- title: VARCHAR(150), không null, mô tả: Tiêu đề
- content: TEXT, không null, mô tả: Nội dung
- start_date: DATE, tùy chọn, mô tả: Ngày hiệu lực bắt đầu
- end_date: DATE, tùy chọn, mô tả: Ngày hiệu lực kết thúc

**[DAT-011]** Bảng SystemSettings:
- setting_key: VARCHAR(50), PK, mô tả: Khóa cấu hình
- setting_value: TEXT, không null, mô tả: Giá trị cấu hình
- description: VARCHAR(200), tùy chọn, mô tả: Ý nghĩa của cài đặt
"
}