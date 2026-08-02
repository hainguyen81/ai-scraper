# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Kiểm soát tài liệu

| Item | Chi tiết |
| :--- | :--- |
| **Mã bản thiết kế** | ARCH-20260802161610 |
| **Tên dự án** | membership-hub |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày.Giờ** | 2026/08/02 16:16:10 |
| **Tác giả** | Kiến trúc sư hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Chờ xem xét quản lý kỹ thuật |

## 📊 1. TỔNG QUAN HỆ THỐNG & CƠ SỞ KIẾN TRÚC
### 1.1. Cơ sở hệ thống & Mô thức kiến trúc
Tổng quan kỹ thuật toàn diện về kiến trúc hệ thống cốt lõi, bao gồm các thành phần chính, mô thức kiến trúc, và các mẫu thiết kế được áp dụng.

### 1.2. Kiến trúc dòng dữ liệu doanh nghiệp & Hệ sinh thái cốt lõi
Mô tả chi tiết về các kênh thông điệp không đồng bộ, cổng nhập dữ liệu, cấu trúc chủ đề, và kiến trúc phân tán ngoài kênh.

## 📁 2. TÀI NGUYÊN CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI
- **Tầng công nghệ cơ sở hạ tầng phía sau:** Các phiên bản chính xác, môi trường chạy, trừu tượng hóa tiêm依赖, ORM, và khuôn khổ thông điệp.
- **Tầng công nghệ phía trước & Di động đa nền tảng:** Các khuôn khổ web, định tuyến địa phương hóa động, bố cục đáp ứng, và các bộ chạy thời gian đa nền tảng nếu có.

## 📁 3. HÀNG RÀO BẢO MẬT & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
- **Quy tắc biên giới không gian làm việc tuyệt đối:** True repository workspace root được cố định vĩnh viễn tại gốc dự án `..`. Tất cả đường dẫn được tạo phải bắt đầu bằng `./sources/`.
- **Quy tắc ánh xạ đường dẫn động:** Áp dụng các quy tắc ánh xạ đường dẫn động được định nghĩa trong Giao thức 1 một cách nghiêm ngặt, phù hợp với cấu trúc dự án được phát hiện.
- **[ĐIỀU KIỆN: JAVA_STACK_ONLY] Tiêu chuẩn gói Java:** Nếu công nghệ sử dụng các khuôn khổ Java, tất cả mã nguồn Java phải nằm nghiêm ngặt trong nền tảng gói doanh nghiệp: `org.nlh4j.saas.<tên_dự_án_phần_mềm_thấp_hơn>`. Bạn phải chuyển đổi động chuỗi "membership-hub" thành một token phần mềm thấp hơn nghiêm ngặt bằng cách loại bỏ khoảng trắng, dấu gạch nối, và dấu gạch dưới. Các dự án không phải Java hoàn toàn bị cấm áp dụng phân khúc gói này.
- **Cú pháp đường dẫn mục tiêu Tester nghiêm ngặt:** Bất kỳ thành phần nào được Tester Sub-Agent nhắm đến phải được cấu trúc như một cặp phân cách bằng dấu chấm phẩy nghiêm ngặt `<thành_phần_nguồn_or_token>;<tệp_đSuite_thử_nghiệm_để_thực_thi>`. Cả hai đường dẫn trong cặp phải bắt đầu bằng `./sources/`.

## 📁 4. TỔNG QUAN KIẾN TRÚC ĐA GIAI ĐOẠN
- Tạo một bảng Markdown sạch, có cấu trúc cao, ánh xạ phân phối chính xác của các thành phần và Tag IDs trên các giai đoạn được tính toán động. Bạn phải tính toán số giai đoạn tối ưu (được biểu thị bằng N, nơi N <= 5) mà tự nhiên và hoàn toàn bao phủ 100% yêu cầu BA và Tag IDs. Mỗi hàng phải chỉ định một khoảng thời gian kỹ thuật thực tế bị giới hạn giữa 1 đến 7 ngày tối đa mỗi giai đoạn. Không tạo hàng trống, giai đoạn giả, hoặc tải công việc nhân tạo. Nếu yêu cầu được thỏa mãn đầy đủ trong ít hơn 5 giai đoạn, hãy kết thúc ngay lập tức cấu hình ma trận tại giai đoạn N.
- Dịch tiêu đề phần và tiêu đề cột bảng vào tiếng Việt. Nội dung trong cột phải được dịch hoàn toàn, ngoại trừ các cột `Thành phần kiến trúc / Đường dẫn mô-đun`, `Sub-Agent được giao`, và `Tag IDs được nhắm đến`.

| Giai đoạn | Phạm vi ngày | Thành phần kiến trúc / Đường dẫn mô-đun | Tóm tắt giao hàng kỹ thuật | Sub-Agent được giao | Tag IDs được nhắm đến |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 5. CHUYÊN MÔN GIAI ĐOẠN & GIAO HÀNG HÀNG NGÀY
# 1:1 MIRROR & NGÔN NGỮ MANDATE:
- Tiêu đề phần 5 và tiêu đề con phải hoạt động như một gương cấu trúc nghiêm ngặt của các giai đoạn động được tính toán trong Phần 4. Bạn phải tạo một khối chi tiết độc lập, hoàn chỉnh dưới đây cho MỖI giai đoạn từ Giai đoạn 1 đến Giai đoạn N (nơi N <= 5).
- Việc cắt ngắn, bỏ qua, hoặc kết hợp các giai đoạn là một sự vi phạm nghiêm trọng của đường ống. Bạn được lệnh nghiêm ngặt để chi tiết hóa mọi giai đoạn đã xuất hiện trong bảng của bạn trong Phần 4.
- Bạn phải dịch tiêu đề giai đoạn, mục tiêu cốt lõi, tiêu đề nhật ký ngày, và "Hướng dẫn nhiệm vụ kỹ thuật chi tiết" hoàn toàn vào tiếng Việt. Không để lại giải thích bằng tiếng Anh.

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- Đối với mỗi Giai đoạn [X], nhật ký ngày-tanggal phải nghiêm ngặt ánh xạ đến phạm vi ngày chính xác được định nghĩa cho giai đoạn đó trong Phần 4.
- Tổng số ngày trong bất kỳ giai đoạn nào không được vượt quá giới hạn trên tuyệt đối là 7 ngày.
- Bạn phải thực hiện một sự đóng băng nhật ký cứng và kết thúc vòng lặp ngày hoạt động ngay lập tức vào ngày chính xác khi 100% mã theo dõi baseline BA cho Giai đoạn [X] được bao phủ. Việc tạo ra các nhiệm vụ giả hoặc yêu cầu tổng hợp để lấp đầy thời gian biểu lên đến 7 ngày là hoàn toàn bị cấm.

### Phase [X] Detailed Architectural Specification
- **[Dịch "Mục tiêu cốt lõi & Mục đích giai đoạn"]**: [Giải thích kỹ thuật chi tiết về những gì giai đoạn này đạt được và mục tiêu chức năng của nó được dịch sang ngôn ngữ chỉ định]
- **[Dịch "Ma trận bản đồ thư mục vật lý"]**: Liệt kê tất cả các đường dẫn tệp cụ thể dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi đường dẫn được tạo ra phải được thêm vào với các Tag IDs theo dõi trực tuyến. Giữ chúng trong tiếng Anh kỹ thuật.
- **[Dịch "Qui định DDL SQL lược đồ cơ sở dữ liệu"] [DAT-XXX]**: Cung cấp các tuyên bố DDL SQL di chuyển nguyên, hoàn chỉnh và hợp lệ chứa các cột, kiểu dữ liệu, khóa chính / khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc không null áp dụng trong phạm vi giai đoạn này. Giữ chúng trong tiếng Anh kỹ thuật. (Bỏ qua hoàn toàn nếu kiến trúc dự án không có yêu cầu cơ sở dữ liệu hoặc lớp bền).
- **Hợp đồng API và định tuyến sự kiện [REQ-XXX], [ARC-XXX]**: Tài liệu các hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ tải JSON yêu cầu / phản hồi, hoặc cấu hình chủ đề môi giới tin nhắn). Chỉ dịch các định nghĩa chức năng
- **Bộ xử lý ngoại lệ cục bộ giai đoạn [EXC-XXX]**: Chi tiết các quy tắc xác thực kinh doanh, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt đến phạm vi giai đoạn hiện tại. Dịch các quy tắc xác thực kinh doanh và mô tả lỗi.

#### 📅 Phân phối nhiệm vụ Sub-Agent ngày-tanggal (Giai đoạn [X])
# BANNED RAW HEADERS, INDENTATION & NGÔN NGỮ ENFORCEMENT:
- Bạn hoàn toàn bị cấm sử dụng các biểu tượng tiêu đề markdown (`#`, `##`, `###`, `####`) trước từ "NGÀY". Mỗi nhật ký ngày phải được hiển thị nghiêm ngặt như một điểm danh sách lồng nhau bắt đầu bằng `- **NGÀY [Y]: ...**`.
- Bạn phải dịch văn bản mục tiêu ngày và "Hướng dẫn nhiệm vụ kỹ thuật chi tiết" hoàn toàn sang tiếng Việt. Không để lại giải thích mà không dịch.
- Đảm bảo tất cả các thuộc tính bên trong được thụt lề đúng cách bằng khoảng trắng để duy trì một phân cấp danh sách lồng nhau đẹp. Đảm bảo chính xác MỘT Sub-Agent với định dạng chữ cái viết hoa đầu tiên được chỉ định cho mỗi dòng nhiệm vụ hoạt động.

- **NGÀY [Y]: [MỤC TIÊU NGẮN GON CHO NGÀY LỊCH NÀY]**
  - **[Dịch "Chuyên môn hóa luồng làm việc Sub-Agent"]**:
    * **[Token Sub-Agent được chỉ định: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]**:
      - **[Dịch "Đường dẫn tệp thành phần mục tiêu"] (`target_component`):** [Chèn đường dẫn tệp vật lý cụ thể bắt đầu bằng `./sources/` hoặc cú pháp cặp Tester trong tiếng Anh kỹ thuật. Đính kèm các Tag IDs tương ứng trực tuyến tại đây, ví dụ: `./sources/backend.... [REQ-001], [DAT-002]`]
      - **[Dịch "Hướng dẫn nhiệm vụ kỹ thuật chi tiết"]**: [Hướng dẫn kỹ thuật đầy đủ, mật độ cao, quy ước khuôn khổ, bố cục hợp đồng API, xác thực trường dữ liệu, hoặc tham số trường hợp thử nghiệm đơn vị được dịch hoàn toàn sang tiếng Việt, đính kèm Tag IDs]
      - **[Dịch "Tag IDs được nhắm đến"]**: [Viết từng thẻ riêng biệt, ngăn cách bằng dấu phẩy, ví dụ: `[REQ-001], [DAT-002], [EXC-001]`.]

## 📁 6. MÃ BẢO MẬT DOANH NGHIỆP TOÀN CẦU & BIỆN PHÁP CHỐNG TIÊM
[Translate this section header and all bullet descriptions below entirely into the specified language]
- **Biện pháp chống tiêm SQL (SQLi) tuyệt đối:** Các tham số cho các câu lệnh đã chuẩn bị, tham số truy vấn vị trí, và danh sách trắng đầu vào sắp xếp động.
- **Kịch bản XSS & Chính sách bảo mật nội dung (CSP):** Các tiêu chuẩn cho việc tự động hóa việc làm sạch ngữ cảnh, tự động thoát JSX, và việc tiêm các tiêu đề CSP nghiêm ngặt (`unsafe-inline` hạn chế).
- **Thanh ray bảo mật CORS đa thuê bao:** Các cấu hình cho việc cấm wildcard gốc và xác thực số liệu gốc thuê bao động.
- **Động cơ tẩy rửa nhật ký Zero-Leak & Máy mask dữ liệu PII:** Các quy tắc cho các bộ phận interceptors tự động (`@JsonSerialize`) và ngưỡng tẩy rửa nhật ký.

## 📁 7. QUI TẮC TUÂN THỦ DI ĐỘNG HYBRID & CƠ CHẾ SEO QUỐC TẾ
[Translate this section header and all bullet descriptions below entirely into the specified language]
- **Qui tắc tuân thủ di động Hybrid Capacitor:** [Nếu di động hoạt động] Các quy tắc cho việc lấy dữ liệu khách hàng động, địa chỉ URL tuyệt đối, các biện pháp phòng ngừa hydrat hóa, các trừu tượng lưu trữ bản địa (`@capacitor/preferences`), và việc bắt giữ nút trở lại phần cứng.
- **Quốc tế hóa (i18n) & Tiêm SEO động:** Các kiến trúc trung gian nhận dạng ngôn ngữ lớp cạnh, việc tiêm điều khiển siêu truyền thông động, và các giới hạn chỉ mục crawler tìm kiếm.

## 📁 8. LUỒNG PIPELINE TỰ ĐỘNG NGÀY GIT BRANCH
[Translate this section header and all bullet descriptions below entirely into the specified language]
- **Forking không gian làm việc hàng ngày:** Các điều khiển tạo fork chương trình cho nhánh `features/development-day-X`.
- **Cổng kiểm soát Validation Guard Pipeline:** Các quy tắc thực hiện cho việc xác minh biên dịch, mục tiêu bao phủ mã tự động (`>= 85%`), và nhật ký tổng hợp ngữ cảnh.

### 🛑 YÊU CẦU KIỂM TRA MA TRẬN
[Translate this section header into the specified language]
Ngay tại cuối cùng của văn bản tài liệu, bạn phải in một khối văn bản xác minh tính toán nghiêm ngặt bằng cách phân tích và đếm mọi chuỗi thẻ duy nhất hiện diện trong đầu ra của bạn:
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`