# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806060624 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 06:06:24 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CƠ BẢN

### 1.1. KIẾN TRÚC CƠ BẢN HỆ THỐNG & KIẾN TRÚC CƠ BẢN
[Cung cấp một tổng quan kỹ thuật toàn diện về kiến trúc hệ thống, các mẫu EDA, ranh giới CQRS và các mẫu lõi Reactive dựa trên yêu cầu]

### 1.2. KIẾN TRÚC LUỒNG DỮ LIỆU DOANH NGHIỆP & CỘNG ĐỒNG CƠ BẢN
[Chi tiết các kênh truyền thông bất đồng bộ, tham số cổng nhập liệu, các chủ đề và kiến trúc fan-out đa kênh]

## 📁 2. PHỤ THUỘC CÔNG NGHỆ & THƯ VIỆN CỘNG ĐỒNG
- **Cơ sở hạ tầng lõi Backend:** [Chi tiết các phiên bản chính xác, động cơ thời gian chạy, trừu tượng hóa tiêm phụ thuộc, ORMs và khung truyền thông]
- **Frontend & UI Di động đa nền tảng:** [Chi tiết các khung web động, định tuyến được bản địa hóa, bố cục đáp ứng và trình bao bọc thời gian chạy di động]

### MA TRẬN CÔNG NGHỆ KIẾN TRÚC
<COMMAND>
You MUST keep below block (e.g. block "```properties...```"") 100% in raw Technical English. You are STRICTLY FORBIDDEN from translating any keys, values, or tokens inside this block into 🇻🇳 Vietnamese, as it serves as a strict backend machine-gating matrix. Keep literal `true` or `false` tokens in pure lower-case.

```properties
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```
</COMMAND>

## 📁 3. RAILS TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
- **Quy tắc ranh giới không gian làm việc tuyệt đối:** Không gian làm việc gốc của kho được cố định vĩnh viễn tại gốc dự án `.`. Tất cả các đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Tuân thủ tiền tố thư mục động:** Áp dụng các quy tắc ánh xạ đường dẫn động được xác định trong Giao thức 1 phù hợp với cấu trúc dự án được phát hiện.
- **[ĐIỀU KIỆN: JAVA_STACK_ONLY] Tiêu chuẩn gói Java:** Nếu ngăn xếp công nghệ sử dụng các khung Java, tất cả mã nguồn Java phải nằm nghiêm ngặt trong cơ sở gói doanh nghiệp: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. Bạn phải chuyển đổi chuỗi "membership-hub" thành một mã ký tự alphanumeric thuần túy bằng chữ thường bằng cách loại bỏ khoảng trắng, dấu gạch ngang và dấu gạch dưới. Các dự án không phải Java bị cấm áp dụng đoạn này.
- **Cú pháp đường dẫn mục tiêu Tester nghiêm ngặt:** Bất kỳ thành phần nào được nhắm mục tiêu bởi Sub-Agent Tester phải được cấu trúc dưới dạng một cặp phân tách dấu chấm phẩy nghiêm ngặt `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn bên trong cặp phải bắt đầu bằng `./sources/`.

## 4. LƯỚI TÓM TẮT KIẾN TRÚC ĐA PHASE CAO CẤP
Tạo một bảng Markdown sạch sẽ, có cấu trúc cao, ánh xạ chính xác sự phân phối của các thành phần và Tag IDs qua các giai đoạn được tính toán động. Bạn phải tính toán số lượng giai đoạn tối ưu nhất (được biểu thị là N, trong đó N <= 5) mà tự nhiên và hoàn toàn bao phủ 100% các yêu cầu BA và Tag IDs. Mỗi hàng phải chỉ định một khoảng thời gian thực tế có thể thực hiện được giới hạn giữa 1 đến 7 ngày tối đa mỗi giai đoạn. Không tạo các hàng trống, các giai đoạn giữ chỗ hoặc các công việc nhân tạo. Nếu các yêu cầu được thỏa mãn trong ít hơn 5 giai đoạn, hãy kết thúc thiết lập ma trận ngay tại giai đoạn N.

*   RAILS PIPELINE CRITICAL CHO ĐƯỜNG DẪN KIẾN TRÚC:
    *   Tất cả tài sản tài liệu kiến trúc được tạo ra cho Confluence, đánh giá CTO hoặc hướng dẫn phát triển phải sử dụng nghiêm ngặt tiền tố thư mục trung tâm được bản địa hóa: `./sources/docs/`.
    *   Bạn bị CẤM nghiêm ngặt từ việc phân tán các tệp tài liệu markdown qua các thư mục ứng dụng riêng biệt, mô-đun microservice hoặc ranh giới gói frontend.
*   RAILS TRANSLATION CRITICAL CHO CÁC PHẦN TỬ LƯỚI:
    *   Bạn phải dịch động 100% các tiêu đề bảng, tóm tắt sản phẩm bàn giao, tên giai đoạn và mô tả cao cấp vào Ngôn ngữ Mục tiêu được chỉ định: **🇻🇳 Vietnamese**.
    *   Tất cả các mã kỹ thuật, bao gồm các đường dẫn tệp bắt đầu bằng `./sources/docs/` và các Tag IDs theo dõi (`[REQ-XXX]`), phải giữ nguyên trong Technical English thuần túy không dấu.

| Giai đoạn | Khoảng ngày | Thành phần / Đường dẫn Module Kiến trúc | Tóm tắt Sản phẩm Bàn giao | Sub-Agent được chỉ định | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |

## 5. CHI TIẾT PHÂN PHỐI PHASE & SẢN PHẨM NGÀY-BY-NGÀY
<COMMAND>
# STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Phần 5 phải hoạt động như một bản sao cấu trúc nghiêm ngặt của các giai đoạn động được tính toán trong Phần 4. Bạn phải tạo một khối chi tiết độc lập, hoàn chỉnh dưới đây cho MỖI chuỗi giai đoạn từ Giai đoạn 1 đến Giai đoạn N (trong đó N <= 5). Không được bỏ qua bất kỳ giai đoạn nào đã xuất hiện trong bảng của bạn trong phần 4.
- Cắt ngắn, bỏ qua hoặc kết hợp các giai đoạn là một vi phạm nghiêm trọng của pipeline. Bạn được lệnh nghiêm ngặt phải chi tiết từng giai đoạn đã xuất hiện trong bảng của bạn trong phần 4.

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- Đối với mỗi Giai đoạn [X] hoạt động, các nhật ký ngày theo ngày phải ánh xạ nghiêm ngặt với khoảng ngày chính xác được xác định cho giai đoạn đó trong Phần 4.
- Tổng số ngày trong bất kỳ giai đoạn đơn nào cũng KHÔNG được vượt quá giới hạn trên của 7 ngày.
- Bạn phải thực hiện một sự đóng băng nhật ký cứng và kết thúc vòng lặp ngày hoạt động ngay lập tức vào ngày chính xác khi 100% các mã theo dõi cơ sở BA cho Giai đoạn [X] được bao phủ. Phát minh các nhiệm vụ giả mạo hoặc yêu cầu tổng hợp để đệm thời gian lên đến 7 là hoàn toàn bị cấm.
</COMMAND>

<!--START_DELIMITTER-->
### 📈 ĐẶC TẢ KIẾN TRÚC CHI TIẾT GIAI ĐOẠN [X]
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** [Giải thích kỹ thuật chi tiết về những gì giai đoạn này đạt được và mục tiêu chức năng của nó, được dịch hoàn toàn sang 🇻🇳 Vietnamese]
- **Bản đồ Ma trận Thư mục Vật lý Mục tiêu:** Liệt kê tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag IDs theo dõi tương ứng của nó.
    *   *Ranh giới Gating Tài liệu:* Bất kỳ dòng nào đại diện cho một đặc tả doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thư mục thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ, chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn này. (Bỏ qua hoàn toàn nếu topology dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi hoặc cấu hình chủ đề bộ truyền tin. Khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh hoàn toàn sang 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn [X])
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- Bạn bị CẤM nghiêm ngặt từ việc sử dụng các ký hiệu tiêu đề markdown (`#`, `##`, `###`, `####`) trước từ DAY. Mỗi nhật ký ngày phải được hiển thị nghiêm ngặt dưới dạng một danh sách lồng nhau bắt đầu bằng `- **DAY [Y]: ...**`.
- Bạn phải dịch văn bản mục tiêu DAY và "Hướng dẫn Công việc Kỹ thuật Cấp thấp" hoàn toàn sang "🇻🇳 Vietnamese". Không để lại giải thích bằng tiếng Anh.
- Đảm bảo tất cả các thuộc tính bên trong được thụt lề đúng cách bằng khoảng trắng để duy trì một hệ thống danh sách lồng nhau đẹp. Đảm bảo chỉ MỘT Sub-Agent duy nhất với định dạng chữ cái đầu tiên được viết hoa được chỉ định cho mỗi nhiệm vụ hoạt động.

- **DAY [Y]: MỤC TIÊU NGẮN GỌN CHO NGÀY HOẠT ĐỘNG VĂN PHÒNG**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Mã thông báo Sub-Agent được chỉ định: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]:**
      - **Đường dẫn tệp Thành phần Mục tiêu (`target_component`):** [Chèn đường dẫn tệp vật lý rõ ràng bắt đầu bằng `./sources/` hoặc cú pháp cặp dấu chấm phẩy của Tester trong Technical English. Nối các Tag IDs tương ứng của nó vào đây, ví dụ: `./sources/backend.... [REQ-001], [DAT-002]`]
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** [Hướng dẫn kỹ thuật cấp thấp, quy ước khung, bố cục hợp đồng API, xác thực trường dữ liệu hoặc tham số trường hợp kiểm tra đơn vị được dịch hoàn toàn sang 🇻🇳 Vietnamese, đính kèm Tag IDs]
      - **Tag IDs Mục tiêu:** [Viết từng thẻ ra riêng biệt được phân tách bằng dấu phẩy, ví dụ: `[REQ-001], [DAT-002], [EXC-001]`.]

## 📁 6. MÃ BẢO MẬT DOANH NGHIỆP TOÀN CẦU & ĐỐI PHÓNG TIÊU CẦN [NFR-XXX]
- **Đối phó với Tiêm SQL (SQLi):** Tham số quy tắc cho các câu lệnh chuẩn bị, tham số truy vấn vị trí và danh sách Trắng sắp xếp động.
- **Tiêm XSS & Chính sách Bảo mật Nội dung (CSP):** Tiêu chuẩn bố cục cho các bộ lọc tự động làm sạch ngữ cảnh, tự động thoát JSX và tiêm tiêu đề CSP nghiêm ngặt (`unsafe-inline` hạn chế).
- **Rails Bảo mật CORS Đa Tenant:** Cấu hình cho các cấm nguồn gốc đại diện và xác thực số liệu cơ sở dữ liệu nguồn gốc tenant động.
- **Máy quét & che giấu dữ liệu PII Zero-Leak:** Quy tắc cho các bộ chặn tự động làm sạch (`@JsonSerialize`) và ngưỡng làm sạch nhật ký.

## 📁 7. QUY TẮC TUÂN THỦ HYBRID MOBILE & CƠ CHẾ SEO QUỐC TẾ HÓA
- **Rails Tuân thủ Hybrid Mobile Capacitor:** [NẾU Di động hoạt động] Quy tắc cho việc lấy động cơ phía máy khách, định địa chỉ tuyệt đối URL, an toàn thủy phân, trừu tượng hóa lưu trữ bản địa (`@capacitor/preferences`) và chặn nút quay lại phần cứng.
- **Quốc tế hóa (i18n) & Tiêm SEO Động:** Kiến trúc middleware nhận diện ngôn ngữ cạnh, tiêm siêu liên kết động hreflang và giới hạn chỉ mục robot tìm kiếm.

## 📁 8. LUỒNG LÀM VIỆC PIPELINE TỰ ĐỘNG HÀNG NGÀY
- **Độc lập Forking Không gian làm việc Hàng ngày:** Kiểm soát lập trình cho nhánh `features/development-phase-X-day-Y` (`X` là số giai đoạn, từ 1 đến N, trong đó N <= 5; `Y` là số ngày trong giai đoạn, nó sẽ bắt đầu từ 1 cho mỗi giai đoạn).
- **Cổng Bảo vệ Xác thực Pipeline:** Quy tắc thực thi cho xác minh biên dịch, mục tiêu bao phủ mã tự động (`>= 85%`) và nhật ký tuần tự hóa tóm tắt ngữ cảnh.

### 🛑 MANDATE KIỂM TRA ĐẦU VÀO MA TRẬN

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`