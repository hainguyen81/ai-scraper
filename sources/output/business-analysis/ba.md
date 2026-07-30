{
  "project_names": {
    "technical_codename": "membership-hub",
    "descriptive_name": "Unified Membership Management Platform",
    "brand_name": "MembHub"
  },
  "srs_content_markdown": "## 1. PROJECT OVERVIEW
- **Product Objectives & Core Values**
  - Cung cấp một nền tảng thống nhất để quản lý hội viên đa trung tâm.
  - Cho phép theo dõi điểm danh thời gian thực thông qua quét mã QR.
  - Cung cấp thẻ hội viên kỹ thuật số với tính năng đếm ngày hiệu lực.
  - Hỗ trợ liên lạc đa kênh (web, mobile, nhóm Zalo).
  - Giá trị cốt lõi: độ tin cậy, khả năng mở rộng, bảo mật, tính thân thiện với người dùng, hỗ trợ đa ngôn ngữ.

- **Nhóm người dùng mục tiêu**
  - Quản trị viên hệ thống (siêu người dùng toàn cầu)
  - Quản trị viên trung tâm (quản lý cấp trung tâm)
  - Quản lý (phụ trách, quyền hạn giới hạn)
  - Giáo viên (chỉ xem lịch học)
  - Học viên (duyệt khóa học, đăng ký, xem thẻ hội viên)
  - Người dùng ứng dụng di động (giống như các vai trò trên, giao diện phản hồi)

- **Ma trận kiểm soát quyền truy cập dựa trên vai trò (RBAC)**
  - [ARC-001] Quản trị viên hệ thống: toàn quyền trên tất cả các trung tâm.
  - [ARC-002] Quản trị viên trung tâm: toàn quyền trong trung tâm của mình, không thể ảnh hưởng đến các trung tâm khác.
  - [ARC-003] Quản lý: có thể tạo thông báo, quản lý học viên, chỉ định học viên hiện có cho khóa học, xem danh sách khóa học, không thể chỉnh sửa khóa học hoặc chỉ định giáo viên.
  - [ARC-004] Giáo viên: xem khóa học của mình, danh sách học viên, lịch trình; chỉ đọc.
  - [ARC-005] Học viên: duyệt khóa học, đăng ký khóa học mới, xem thẻ hội viên (ngày hiệu lực còn lại), gia hạn thẻ.

- **Lưu đồ kiến trúc & luồng dữ liệu (các luồng chính)**
  - [ARC-006] Luồng xác thực: hỗ trợ email/mật khẩu, Firebase, Google, Facebook qua OAuth2; cấp JWT token có hiệu lực 15 phút và token làm mới.
  - [ARC-007] Luồng xử lý điểm danh QR: ứng dụng di động quét QR, gửi student ID và timestamp đến backend; dịch vụ xác thực và ghi lại điểm danh một cách idempotent.
  - [ARC-008] Luồng gửi thông báo: hệ thống gửi push notification đến ứng dụng di động và đăng thông báo lên nhóm Zalo được chỉ định cho thông báo, chỉ định khóa học và cảnh báo điểm danh.
  - [ARC-009] Luồng tích hợp backend ứng dụng di động: frontend Next.js tiêu thụ REST APIs; xác thực qua bearer token; hỗ trợ caching ngoại tuyến cho trường hợp mất kết nối mạng.

## 2. FUNCTIONAL REQUIREMENTS

### 2.1 Quản lý người dùng
- **[REQ-001]** Đăng ký người dùng: Là một người dùng tiềm năng, tôi muốn đăng ký bằng email và mật khẩu (hoặc nhà cung cấp xã hội) để có thể tạo tài khoản trong hệ thống.
  - **Tiêu chí chấp nhận**:
    - Giả sử người dùng cung cấp email duy nhất, mật khẩu mạnh và đồng ý với điều khoản, khi họ gửi biểu mẫu đăng ký, thì hệ thống xác thực đầu vào, tạo bản ghi người dùng mới với vai trò ‘Học viên’ (hoặc ‘Giáo viên’ nếu được mời) và trả về phản hồi thành công kèm token JWT. *[REQ-001]*
  - **Dữ liệu đầu vào & quy tắc xác thực**:
    - Email: bắt buộc, tối đa 255 ký tự, phải chứa đúng một ký tự ‘@’ và một phần miền (ví dụ: user@example.com). Phải là duy nhất.
    - Mật khẩu: bắt buộc, tối thiểu 8 ký tự, ít nhất một chữ hoa, một chữ thường, một chữ số, một ký tự đặc biệt.
    - Điều khoản: bắt buộc tích vào ô.

- **[REQ-002]** Xác thực xã hội: Là một người dùng, tôi muốn đăng nhập/đăng ký bằng Firebase, Google hoặc OAuth Facebook để có thể sử dụng các thông tin đăng nhập hiện có.
  - **Tiêu chí chấp nhận**:
    - Giả sử người dùng chọn một nhà cung cấp xã hội, khi họ xác thực qua cửa sổ bật lên của nhà cung cấp, thì hệ thống nhận mã OAuth2, trao đổi mã để lấy thông tin người dùng, tạo hoặc cập nhật bản ghi người dùng cục bộ và cấp token JWT. *[REQ-002]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: token nhà cung cấp, tùy chọn ảnh hồ sơ.

- **[REQ-003]** Gán vai trò người dùng: Là một quản trị viên, tôi muốn chỉ định hoặc thay đổi vai trò của một người dùng (Quản trị viên hệ thống, Quản trị viên trung tâm, Quản lý, Giáo viên, Học viên) để các quyền được thực thi chính xác.
  - **Tiêu chí chấp nhận**:
    - Giả sử quản trị viên chọn một người dùng và vai trò mới, khi hành động được xác nhận, thì cột vai trò của người dùng được cập nhật và các quyền tương ứng được áp dụng ngay lập tức. *[REQ-003]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: dropdown vai trò, bắt buộc ghi nhật ký kiểm toán.

### 2.2 Quản lý trung tâm
- **[REQ-004]** Xem danh sách trung tâm: Là bất kỳ người dùng đã xác thực, tôi muốn xem danh sách tất cả các trung tâm kèm theo địa chỉ, mã số thuế và liên hệ quản trị viên để có thể xác định các trung tâm có liên quan.
  - **Tiêu chí chấp nhận**:
    - Giả sử người dùng truy cập trang Trung tâm, khi yêu cầu hoàn tất, thì một bảng các trung tâm (Tên, Địa chỉ, Mã số thuế, Liên hệ quản trị viên) được hiển thị. *[REQ-004]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Không có (chỉ đọc).

- **[REQ-005]** Tạo/Cập nhật/Xóa trung tâm: Là một Quản trị viên hệ thống, tôi muốn thêm, chỉnh sửa hoặc xóa một bản ghi trung tâm để thông tin trung tâm được cập nhật.
  - **Tiêu chí chấp nhận**:
    - Giả sử Quản trị viên hệ thống cung cấp tên trung tâm, địa chỉ, mã số thuế, số điện thoại liên hệ và email, khi hành động lưu được thực hiện, thì trung tâm được lưu trữ và xuất hiện trong danh sách; nếu mã số thuế trùng lặp, thao tác thất bại với lỗi xung đột. *[REQ-005]*
  - **Dữ liệu đầu vào & quy tắc xác thực**:
    - Tên: bắt buộc, tối đa 100 ký tự.
    - Địa chỉ: bắt buộc, tối đa 255 ký tự.
    - Mã số thuế: bắt buộc, dạng số, 10‑13 chữ số, duy nhất.
    - Số điện thoại liên hệ: tùy chọn, có thể bao gồm +, chữ số, dấu cách, dấu gạch ngang, ngoặc đơn.
    - Email liên hệ: tùy chọn, phải có định dạng email hợp lệ.

- **[REQ-006]** Chỉ định quản trị viên trung tâm: Là một Quản trị viên hệ thống, tôi muốn chỉ định hoặc hủy chỉ định một người dùng làm Quản trị viên trung tâm cho một trung tâm cụ thể để phân quyền quản trị.
  - **Tiêu chí chấp nhận**:
    - Giả sử Quản trị viên hệ thống chọn một người dùng và một trung tâm, khi hành động chỉ định được xác nhận, thì vai trò của người dùng được đặt là ‘Quản trị viên trung tâm’ và ID trung tâm được ghi lại; thao tác hủy chỉ định đảo ngược hành động. *[REQ-006]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: ID người dùng, ID trung tâm.

### 2.3 Quản lý khóa học
- **[REQ-007]** Xem danh sách khóa học: Là bất kỳ người dùng đã xác thực, tôi muốn xem tất cả các khóa học kèm theo lịch học và giáo viên được chỉ định để có thể duyệt các khóa học được cung cấp.
  - **Tiêu chí chấp nhận**:
    - Giả sử người dùng truy cập trang Khóa học, khi yêu cầu hoàn tất, thì một lưới hiển thị CourseID, Tiêu đề, Ngày bắt đầu, Ngày kết thúc, Tên giáo viên được hiển thị. *[REQ-007]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Không có.

- **[REQ-008]** Tạo/Cập nhật/Xóa khóa học (tránh xung đột): Là một Quản trị viên hệ thống hoặc Quản trị viên trung tâm, tôi muốn quản lý khóa học (thêm, chỉnh sửa, xóa) trong khi đảm bảo không có lịch học trùng lặp cho cùng một giáo viên hoặc địa điểm.
  - **Tiêu chí chấp nhận**:
    - Giả sử quản trị viên cung cấp CourseTitle, StartDate, EndDate, TeacherID, khi hành động lưu được kích hoạt, thì hệ thống xác thực rằng giáo viên không có lịch học khác chồng lấn lên các ngày này; nếu xung đột, lỗi được trả về; nếu không, khóa học được lưu trữ. *[REQ-008]*
  - **Dữ liệu đầu vào & quy tắc xác thực**:
    - Tiêu đề: bắt buộc, tối đa 150 ký tự.
    - StartDate/EndDate: bắt buộc, EndDate >= StartDate.
    - TeacherID: bắt buộc, khóa ngoại.
    - Logic kiểm tra chồng lấn được thực thi ở mức DB/trigger.

- **[REQ-009]** Chỉ định giáo viên cho khóa học: Là một Quản trị viên hệ thống, tôi muốn chỉ định hoặc hủy chỉ định giáo viên cho khóa học để cập nhật trách nhiệm giảng dạy.
  - **Tiêu chí chấp nhận**:
    - Giả sử quản trị viên chọn một khóa học và một giáo viên, khi hành động chỉ định được thực hiện, thì bản đồ khóa học-giáo viên được tạo và một thông báo được xếp hàng cho ứng dụng di động của giáo viên; thao tác hủy chỉ định xóa bản đồ. *[REQ-009]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: CourseID, TeacherID (phải tồn tại).

### 2.4 Đăng ký và ghi danh của học viên
- **[REQ-010]** Duyệt khóa học: Là một Học viên, tôi muốn duyệt các khóa học có sẵn (trừ các khóa học đã đăng ký) để có thể chọn các khóa học để tham gia.
  - **Tiêu chí chấp nhận**:
    - Giả sử Học viên đăng nhập và truy cập trang Duyệt khóa học, khi yêu cầu hoàn tất, thì một danh sách các khóa học kèm theo sức chứa và lịch học được hiển thị, loại trừ các khóa học mà học viên đã có bản ghi đăng ký. *[REQ-010]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Không có.

- **[REQ-011]** Đăng ký khóa học của học viên: Là một Học viên, tôi muốn đăng ký một khóa học (tồn tại hoặc mới), điều này tự động tạo một tài khoản học viên nếu không có, và chỉ định học viên cho khóa học.
  - **Tiêu chí chấp nhận**:
    - Giả sử Học viên chọn một khóa học và gửi yêu cầu đăng ký, khi backend xử lý yêu cầu, thì một bản ghi đăng ký mới được tạo; nếu học viên không có tài khoản cục bộ, một tài khoản được tạo với vai trò ‘Học viên’; một thông báo được xếp hàng cho ứng dụng di động của học viên và nhóm Zalo của trung tâm. *[REQ-011]*
  - **Dữ liệu đầu vào & quy tắc xác thực**:
    - CourseID: bắt buộc, phải là khóa học đang hoạt động.
    - StudentID: được lấy từ token xác thực (hoặc được tạo trên‑the‑fly).

### 2.5 Điểm danh & quét QR
- **[REQ-012]** Chụp điểm danh QR: Là một Học viên (qua ứng dụng di động), tôi muốn quét mã QR khi bắt đầu tiết học để ghi lại điểm danh của mình trong ngày.
  - **Tiêu chí chấp nhận**:
    - Giả sử Học viên mở máy quét, quét một mã QR hợp lệ của khóa học và xác nhận điểm danh, khi API nhận được payload, thì hệ thống xác thực mối quan hệ học viên‑khóa học, tạo một bản ghi Điểm danh với timestamp và trả về phản hồi thành công; các lần quét trùng lặp trong cùng một ngày bị bỏ qua. *[REQ-012]*
  - **Dữ liệu đầu vào & quy tắc xác thực**:
    - Payload QR: chuỗi base64 chứa studentID và courseID.
    - Xác thực: học viên phải được ghi danh vào khóa học cho ngày đó.

- **[REQ-013]** Điểm danh có tính idempotent: Dịch vụ điểm danh phải đảm bảo rằng nhiều lần quét từ cùng một học viên cho cùng một khóa học trong cùng một ngày tạo ra một bản ghi điểm danh duy nhất.
  - **Tiêu chí chấp nhận**:
    - Giả sử học viên quét QR hai lần trong vòng một phút, khi dịch vụ xử lý cả hai yêu cầu, thì chỉ một hàng điểm danh được tạo; các yêu cầu tiếp theo trả về thành công với cờ ‘đã ghi’ đã xử lý. *[REQ-013]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Khóa chính tổ hợp (StudentID, CourseID, Ngày).

### 2.6 Quản lý thẻ hội viên học viên
- **[REQ-014]** Hiển thị tính hợp lệ thẻ: Là một Học viên, tôi muốn xem thẻ hội viên của mình hiển thị số ngày hiệu lực còn lại để biết khi nào cần gia hạn.
  - **Tiêu chí chấp nhận**:
    - Giả sử Học viên mở trang Thẻ, khi yêu cầu tải, thì giao diện hiển thị tổng số ngày hiệu lực, số ngày đã sử dụng và số ngày còn lại; dữ liệu được lấy từ thực thể StudentCard. *[REQ-014]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Không có (chỉ đọc).

- **[REQ-015]** Gia hạn thẻ: Là một Học viên, tôi muốn gia hạn thẻ hội viên của mình bằng cách thanh toán một khoản phí, điều này cập nhật ngày kết thúc.
  - **Tiêu chí chấp nhận**:
    - Giả sử Học viên chọn một khoảng thời gian gia hạn (ví dụ: 30 ngày), xác nhận thanh toán, khi dịch vụ thanh toán xác nhận thành công, thì EndDate của StudentCard được gia hạn thêm số ngày đã chọn và một thông báo xác nhận được gửi. *[REQ-015]*
  - **Dữ liệu đầu vào & quy tắc xác thực**:
    - RenewalDays: số nguyên, 1‑365.
    - Tích hợp cổng thanh toán (ngoài phạm vi).

### 2.7 Thông báo & liên lạc
- **[REQ-016]** Kích hoạt thông báo: Khi một quản trị viên tạo thông báo, chỉ định giáo viên cho khóa học hoặc ghi danh học viên, hệ thống phải tạo một thông báo gửi đến ứng dụng di động của học viên và đăng một thông báo lên nhóm Zalo được chỉ định.
  - **Tiêu chí chấp nhận**:
    - Giả sử quản trị viên thực hiện một hành động yêu cầu thông báo, khi hành động được lưu, thì một bản ghi Thông báo được tạo, một payload push notification được xếp hàng cho ứng dụng di động và một tin nhắn văn bản được gửi đến nhóm chat Zalo. *[REQ-016]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Đối tượng mục tiêu (học viên, giáo viên, nhóm), nội dung thông báo, tùy chọn phương tiện.

### 2.8 Quản lý khuyến mãi & thông báo
- **[REQ-017]** Quản lý khuyến mãi: Là một Quản trị viên trung tâm hoặc Quản lý, tôi muốn tạo, chỉnh sửa hoặc xóa các khuyến mãi (giảm giá, ưu đãi) với ngày bắt đầu/kết thúc để học viên có thể xem các ưu đãi áp dụng.
  - **Tiêu chí chấp nhận**:
    - Giả sử quản trị viên cung cấp PromotionName, mô tả, điều kiện, startDate, endDate, khi lưu, thì khuyến mãi xuất hiện trong danh sách hiển thị cho học viên; nếu endDate bị bỏ qua, khuyến mãi được coi là vô thời hạn. *[REQ-017]*
  - **Dữ liệu đầu vào & quy tắc xác thực**:
    - Tên: bắt buộc, tối đa 100 ký tự.
    - StartDate/EndDate: tùy chọn, định dạng YYYY‑MM‑DD.
    - Mô tả: tối đa 500 ký tự.

- **[REQ-018]** Quản lý thông báo: Là một Quản trị viên trung tâm hoặc Quản lý, tôi muốn tạo, chỉnh sửa hoặc xóa các thông báo có ngày hết hạn tùy chọn để phát sóng cho tất cả người dùng.
  - **Tiêu chí chấp nhận**:
    - Giả sử quản trị viên nhập AnnouncementTitle, nội dung, ngày hết hạn tùy chọn, khi lưu, thì thông báo được hiển thị trên toàn trang web; nếu ngày hết hạn được đặt, thông báo sẽ tự động biến mất sau ngày đó. *[REQ-018]*
  - **Dữ liệu đầu vào & quy tắc xác thực**:
    - Tiêu đề: bắt buộc, tối đa 150 ký tự.
    - Nội dung: bắt buộc, tối đa 2000 ký tự.

### 2.9 Chatbot dịch vụ khách hàng AI
- **[REQ-019]** Tích hợp chatbot AI: Là bất kỳ người dùng, tôi muốn tương tác với một chatbot AI có thể trả lời các câu hỏi phổ biến về khóa học, giáo viên, trung tâm và trạng thái tài khoản.
  - **Tiêu chí chấp nhận**:
    - Giả sử người dùng mở widget chat, khi họ hỏi một câu hỏi, thì AI trả về một câu trả lời liên quan hoặc chuyển đến hỗ trợ con người nếu độ tin cậy thấp. *[REQ-019]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Văn bản đầu vào, thời gian chờ phiên.

### 2.10 Các tính năng cốt lõi của ứng dụng di động
- **[REQ-020]** Giao diện người dùng dành riêng cho vai trò trên ứng dụng di động: Là một người dùng di động, tôi muốn một giao diện phản hồi sao chép các chức năng web cho vai trò được chỉ định (Học viên, Giáo viên, Quản trị, v.v.).
  - **Tiêu chí chấp nhận**:
    - Giả sử người dùng đăng nhập trên Android hoặc iOS, khi ứng dụng tải, thì menu điều hướng và các màn hình thích hợp được hiển thị dựa trên vai trò của người dùng. *[REQ-020]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Không có.

- **[REQ-021]** Thông báo đẩy trên di động: Là một người dùng đã đăng ký, tôi muốn nhận các thông báo đẩy trên thiết bị di động cho xác nhận điểm danh, thông báo mới và tin nhắn nhắc nhở.
  - **Tiêu chí chấp nhận**:
    - Giả sử backend kích hoạt một thông báo đẩy, khi token thiết bị được đăng ký, thì thông báo được phân phối qua Firebase Cloud Messaging (FCM) hoặc APNs. *[REQ-021]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Token thiết bị, nền tảng (iOS/Android).

### 2.11 Bản địa hóa & SEO
- **[REQ-022]** Phát hiện ngôn ngữ mặc định: Là một khách truy cập, tôi muốn hệ thống sử dụng tùy chọn ngôn ngữ đã lưu trước đó, nếu không có thì sử dụng cài đặt ngôn ngữ của trình duyệt, để có trải nghiệm được cá nhân hóa.
  - **Tiêu chí chấp nhận**:
    - Giả sử người dùng truy cập trang web, khi hệ thống đánh giá ngôn ngữ, thì nó chọn ngôn ngữ đã lưu nếu có; nếu không, nó sử dụng tiêu đề Accept‑Language; giao diện cập nhật tương ứng. *[REQ-022]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Không có.

- **[REQ-023]** SEO đa ngôn ngữ: Nền tảng phải hỗ trợ SEO cho ít nhất tiếng Anh, tiếng Việt và tiếng Tây Ban Nha; mỗi trang phải bao gồm các thẻ meta và hreflang được xác định theo ngôn ngữ.
  - **Tiêu chí chấp nhận**:
    - Giả sử một trang được yêu cầu với một ngôn ngữ cụ thể, khi trang được hiển thị, thì HTML bao gồm một thẻ `<html lang='en'>` và các liên kết hreflang trỏ đến các phiên bản ngôn ngữ thay thế. *[REQ-023]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Mã ngôn ngữ (en, vi, es).

### 2.12 Báo cáo & phân tích
- **[REQ-024]** Tạo báo cáo điểm danh: Là một quản trị viên, tôi muốn tạo một báo cáo điểm danh hàng ngày cho một trung tâm (CSV) hiển thị trạng thái điểm danh của từng học viên.
  - **Tiêu chí chấp nhận**:
    - Giả sử quản trị viên chọn một trung tâm và khoảng thời gian, khi yêu cầu báo cáo được thực hiện, thì một tệp CSV được tạo với các cột: StudentName, CourseName, AttendanceDate, Status. *[REQ-024]*
  - **Dữ liệu đầu vào & quy tắc xác thực**:
    - Khoảng thời gian: start ≤ end, tối đa 30 ngày.

- **[REQ-025]** Bảng điều khiển tóm tắt đăng ký: Là một Quản trị viên trung tâm, tôi muốn một bảng điều khiển thời gian thực tóm tắt tổng số học viên, khóa học đang hoạt động và các buổi học sắp tới.
  - **Tiêu chí chấp nhận**:
    - Giả sử quản trị viên mở bảng điều khiển, khi dữ liệu làm mới, thì các thẻ hiển thị totalStudents, activeCourses, upcomingSessions (7 ngày tới) được hiển thị. *[REQ-025]*
  - **Dữ liệu đầu vào & quy tắc xác thực**: Khoảng thời gian làm mới có thể cấu hình (mặc định 15 phút).

## 3. EXCEPTION FLOWS & EDGE CASES
- **[EXC-001]** Mất kết nối mạng trong quá trình quét QR:
  - Nếu học viên quét mã QR nhưng không có kết nối mạng, khi ứng dụng thử lại yêu cầu sau khi kết nối lại, thì điểm danh được ghi lại khi dịch vụ sẵn sàng.
- **[EXC-002]** Gửi điểm danh trùng lặp:
  - Nếu cùng một học viên quét cùng một mã QR của khóa học nhiều lần trong cùng một ngày, khi hệ thống phát hiện trùng lặp, thì nó trả về phản hồi thành công với cờ ‘đã ghi’ và không tạo thêm hàng.
- **[EXC-003]** Gửi thông báo không thành công:
  - Khi một thông báo đẩy không thể được gửi (ví dụ: token thiết bị không hợp lệ), thì hệ thống ghi lại lỗi và lên lịch thử lại tối đa ba lần trước khi đánh dấu là thất bại.
- **[EXC-004]** Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc):
  - Nếu xác thực thất bại khi gửi biểu mẫu, khi lỗi được trả về cho người dùng, thì một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.
- **[EXC-005]** Khôi phục hệ thống sau sự cố:
  - Nếu dịch vụ không khả dụng, khi nó khôi phục, thì các lần quét điểm danh chờ xử lý được xử lý theo thứ tự FIFO và người dùng nhận được thông báo về các sự kiện đã khôi phục.

## 4. NON-FUNCTIONAL REQUIREMENTS
- **[NFR-001]** Chỉ số hiệu năng:
  - Các phản hồi API cốt lõi (xác thực, chụp điểm danh QR, danh sách khóa học) phải hoàn tất trong vòng 200 ms trung bình.
  - Các truy vấn cơ sở dữ liệu phải được lập chỉ mục để hỗ trợ thời gian đọc dưới một giây cho tối đa 10 000 người dùng đồng thời.
- **[NFR-002]** Khả năng sẵn sàng:
  - Mục tiêu đạt 99,9 % thời gian hoạt động hàng năm; SLA bao gồm khả năng phục hồi tự động trên các cụm GKE.
- **[NFR-003]** Bảo mật:
  - Tất cả dữ liệu truyền qua phải sử dụng TLS 1.3; mã hóa dữ liệu ở trạng thái nghỉ với AES‑256.
  - JWT access token có hiệu lực 15 phút; refresh token có hiệu lực 7 ngày.
  - Thực hiện các biện pháp kiểm soát OWASP Top 10 (SQL injection, XSS, CSRF).
- **[NFR-004]** Khả năng mở rộng & tính khả dụng:
  - Mở rộng quy mô ngang các dịch vụ Quarkus qua Kubernetes HPA dựa trên CPU > 70 % hoặc độ trễ yêu cầu > 300 ms.
  - Bản sao đọc PostgreSQL cho workloads báo cáo.
- **[NFR-005]** Kích thước Docker Image:
  - Hình ảnh cơ sở có kích thước < 200 MB; hình ảnh cuối cùng < 500 MB.
- **[NFR-006]** Ghi nhật ký & kiểm toán:
  - Tất cả các hành động của người dùng (thay đổi vai trò, bản ghi điểm danh, thông báo) phải được ghi lại với timestamp, ID người dùng và chi tiết hành động; nhật ký được lưu trữ trong 1 năm.
- **[NFR-007]** Hỗ trợ đa ngôn ngữ:
  - Các chuỗi UI phải được ngoại phạm; hỗ trợ tiếng Anh, tiếng Việt, tiếng Tây Ban Nha; chuyển đổi ngôn ngữ mà không cần tải lại trang khi có thể.
- **[NFR-008]** Tuân thủ GDPR/CCPA:
  - Xóa dữ liệu cá nhân theo yêu cầu của người dùng; xuất dữ liệu ở định dạng JSON; quản lý sự đồng ý cho truyền thông tiếp thị.
- **[NFR-009]** Sao lưu & khôi phục thảm họa:
  - Sao lưu PostgreSQL hàng ngày đầy đủ; phục hồi tại bất kỳ điểm nào trong 24 giờ; sao lưu cụm GKE sang khu vực riêng biệt.

## 5. PRELIMINARY DATA DICTIONARY
| Thực thể | Trường | Kiểu dữ liệu | Ràng buộc | Mô tả |
|--------|------|-----------|-----------|-------------|
| Người dùng | user_id | UUID | PK, không null | Định danh duy nhất |
| | email | VARCHAR(255) | không null, duy nhất | Định danh đăng nhập chính |
| | password_hash | CHAR(60) | không null | Băm bcrypt |
| | full_name | VARCHAR(100) | không null | Tên thực |
| | role_id | SMALLINT | FK → Roles.role_id | Vai trò được chỉ định |
| | provider | ENUM('local','firebase','google','facebook') | default 'local' | Nhà cung cấp xác thực |
| | created_at | TIMESTAMP | không null, default now() | Thời điểm tạo tài khoản |
| | updated_at | TIMESTAMP | không null, default now() | Thời điểm cập nhật cuối |
| Trung tâm | center_id | UUID | PK, không null | Định danh duy nhất |
| | name | VARCHAR(100) | không null | Tên trung tâm |
| | address | VARCHAR(255) | không null | Địa chỉ vật lý |
| | tax_id | VARCHAR(20) | duy nhất, không null | Số định danh thuế |
| | contact_phone | VARCHAR(20) | tùy chọn | Số điện thoại liên hệ |
| | contact_email | VARCHAR(100) | tùy chọn | Email liên hệ |
| Khóa học | course_id | UUID | PK, không null | Định danh duy nhất |
| | title | VARCHAR(150) | không null | Tên khóa học |
| | description | TEXT | tùy chọn | Mô tả chi tiết |
| | start_date | DATE | không null | Ngày bắt đầu khóa học |
| | end_date | DATE | không null | Ngày kết thúc khóa học |
| | teacher_id | UUID | FK → Users.user_id | Giáo viên được chỉ định |
| | max_students | INT | default 30 | Sức chứa |
| Đăng ký | enrollment_id | UUID | PK, không null | Định danh duy nhất |
| | student_id | UUID | FK → Users.user_id | Học viên được ghi danh |
| | course_id | UUID | FK → Courses.course_id | Khóa học |
| | enrollment_date | TIMESTAMP | default now() | Khi ghi danh |
| Điểm danh | attendance_id | UUID | PK, không null | Định danh duy nhất |
| | student_id | UUID | FK → Users.user_id | Học viên có mặt |
| | course_id | UUID | FK → Courses.course_id | Khóa học được tham dự |
| | attendance_date | DATE | không null | Ngày điểm danh |
| | timestamp | TIMESTAMP | default now() | Thời điểm chính xác được ghi lại |
| Thẻ hội viên học viên | card_id | UUID | PK, không null | Định danh duy nhất |
| | student_id | UUID | FK → Users.user_id | Chủ sở hữu |
| | issue_date | DATE | không null | Ngày phát hành thẻ |
| | validity_days | INT | không null | Tổng số ngày hiệu lực |
| | remaining_days | INT | tính toán | Số ngày còn lại cho đến khi hết hạn |
| Thông báo | notification_id | UUID | PK, không null | Định danh duy nhất |
| | user_id | UUID | FK → Users.user_id (tùy chọn) | Đối tượng mục tiêu |
| | group_zalo | VARCHAR(50) | tùy chọn | Nhóm Zalo mục tiêu |
| | message | TEXT | không null | Nội dung thông báo |
| | sent_at | TIMESTAMP | default now() | Khi gửi |
| | delivered | BOOLEAN | default false | Trạng thái giao hàng |
| Vai trò | role_id | SMALLINT | PK | Định danh vai trò |
| | name | VARCHAR(30) | duy nhất, không null | Tên vai trò |
| | description | VARCHAR(200) | tùy chọn | Mô tả vai trò |
| Khuyến mãi | promo_id | UUID | PK, không null | Định danh duy nhất |
| | code | VARCHAR(30) | duy nhất | Mã giảm giá |
| | discount_percent | SMALLINT | không null | Phần trăm giảm giá |
| | start_date | DATE | tùy chọn | Ngày bắt đầu khuyến mãi |
| | end_date | DATE | tùy chọn | Ngày kết thúc khuyến mãi |
| | description | TEXT | tùy chọn | Chi tiết khuyến mãi |
| Thông báo | announcement_id | UUID | PK, không null | Định danh duy nhất |
| | title | VARCHAR(150) | không null | Tiêu đề |
| | content | TEXT | không null | Nội dung |
| | start_date | DATE | tùy chọn | Ngày hiệu lực bắt đầu |
| | end_date | DATE | tùy chọn | Ngày hiệu lực kết thúc |
| Cài đặt hệ thống | setting_key | VARCHAR(50) | PK | Khóa cấu hình |
| | setting_value | TEXT | không null | Giá trị cấu hình |
| | description | VARCHAR(200) | tùy chọn | Ý nghĩa của cài đặt |"
}