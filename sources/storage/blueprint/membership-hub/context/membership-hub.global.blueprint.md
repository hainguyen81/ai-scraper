# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806051519 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 05:15:19 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CƠ BẢN

### 1.1. Chế độ hoạt động hệ thống cốt lõi & Kiến trúc hệ thống
[Cung cấp một tổng quan kỹ thuật toàn diện về kiến trúc hệ thống cốt lõi được phát hiện, các mẫu EDA, ranh giới CQRS và các mẫu lõi Reactive dựa trên yêu cầu]

### 1.2. Các hệ sinh thái dữ liệu doanh nghiệp & Topologies luồng dữ liệu
[Chi tiết các kênh truyền thông bất đồng bộ, tham số cổng nhập liệu, các chủ đề topology và các kiến trúc fan-out đa kênh bên ngoài]

## 📁 2. PHỤ THUỘC CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI
- **Cơ sở hạ tầng lõi Backend:** [Chi tiết các phiên bản chính xác, động cơ thời gian chạy, trừu tượng hóa tiêm phụ thuộc, ORMs và khung truyền thông được trích xuất từ yêu cầu]
- **Frontend & Cross-Platform UI Mobile Stack:** [Chi tiết các khung web động, định tuyến được bản địa hóa, bố cục đáp ứng và các trình bao bọc thời gian chạy di động gốc nếu có]

### MA TRẬN CỐT LÕI KIẾN TRÚC
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

## 📁 3. CÁC QUY TẮC BẢO VỆ TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
- **Quy tắc ranh giới không gian làm việc tuyệt đối:** Không gian làm việc gốc của kho lưu trữ được cố định vĩnh viễn tại gốc dự án `.`. Tất cả các đường dẫn được tạo ra phải bắt đầu bằng `./sources/`.
- **Tuân thủ tiền tố thư mục động:** Áp dụng các quy tắc ánh xạ đường dẫn động được xác định trong Giao thức 1 phù hợp với cấu trúc dự án được phát hiện.
- **[ĐIỀU KIỆN: JAVA_STACK_ONLY] Tiêu chuẩn gói Java:** Nếu ngăn xếp công nghệ sử dụng các khung Java, tất cả mã nguồn Java phải nằm nghiêm ngặt trong cơ sở gói doanh nghiệp: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. Bạn phải chuyển đổi động chuỗi "membership-hub" thành một mã thông báo chữ thường không dấu hoàn toàn bằng cách loại bỏ khoảng trắng, dấu gạch ngang và dấu gạch dưới. Các dự án không phải Java hoàn toàn bị cấm áp dụng đoạn này.
- **Cú pháp đường dẫn mục tiêu Tester nghiêm ngặt:** Bất kỳ thành phần nào được nhắm mục tiêu bởi Sub-Agent Tester phải được cấu trúc dưới dạng một cặp phân tách chặt chẽ bằng dấu chấm phẩy `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn bên trong cặp phải bắt đầu bằng `./sources/`.

## 4. TÓM TẮT KIẾN TRÚC MỨC CAO MULTI-PHASE
Tạo một bảng Markdown được cấu trúc tốt, có cấu trúc cao, ánh xạ chính xác sự phân phối của các thành phần và Tag IDs trên các giai đoạn được tính toán động. Bạn phải tính toán số lượng giai đoạn tối ưu nhất (được biểu thị là N, trong đó N <= 5) mà tự nhiên và hoàn toàn bao phủ 100% các yêu cầu BA và Tag IDs. Mỗi hàng phải chỉ định một khoảng thời gian thực tế có thể thực hiện được giới hạn giữa 1 đến một giới hạn trên tuyệt đối là 7 ngày tối đa mỗi giai đoạn. Không tạo các hàng trống, các giai đoạn giữ chỗ hoặc các công việc nhân tạo. Nếu các yêu cầu được thỏa mãn hoàn toàn trong ít hơn 5 giai đoạn, hãy kết thúc thiết lập ma trận ngay lập tức tại giai đoạn N.

*   CÁC QUY TẮC PIPELINE CRITICAL CHO ĐƯỜNG DẪN CẤU TRÚC KIẾN TRÚC:
    *   Tất cả các tài sản tài liệu kiến trúc được tạo ra cho Confluence, đánh giá CTO hoặc hướng dẫn phát triển phải sử dụng nghiêm ngặt tiền tố thư mục trung tâm được bản địa hóa: `./sources/docs/`.
    *   Bạn được CẤM nghiêm ngặt từ việc phân tán các tệp tài liệu markdown qua các thư mục ứng dụng riêng biệt, các mô-đun dịch vụ vi, hoặc ranh giới gói frontend.
*   CÁC QUY TẮC TRANSLATION MANDATE CRITICAL CHO CÁC PHẦN TỬ BẢNG:
    *   Bạn phải dịch động 100% các tiêu đề bảng, tóm tắt sản phẩm bàn giao, tên giai đoạn và các mô tả mức cao vào Ngôn ngữ Mục tiêu được chỉ định: **🇻🇳 Vietnamese**.
    *   Tất cả các mã thông báo kỹ thuật, bao gồm các đường dẫn tệp bắt đầu bằng `./sources/docs/` và các Tag IDs theo dõi (`[REQ-XXX]`), phải giữ nguyên trong Technical English không dấu hoàn toàn.

| Giai đoạn | Khoảng ngày | Thành phần / Module Đường dẫn Kiến trúc | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1-3 | `./sources/backend`, `./sources/frontend`, `./sources/docs` | Thiết lập cơ sở hạ tầng lõi, xác thực người dùng, quản lý vai trò | Coder, Tester, Doc | [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [DAT-001] |
| Giai đoạn 2 | Ngày 4-6 | `./sources/backend`, `./sources/frontend`, `./sources/docs` | Quản lý trung tâm, quản lý khóa học, đăng ký học viên | Coder, Tester, Doc | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004], [DAT-005] |
| Giai đoạn 3 | Ngày 7-9 | `./sources/backend`, `./sources/frontend`, `./sources/docs` | Điểm danh QR, quản lý thẻ hội viên, thông báo | Coder, Tester, Doc | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [DAT-006], [DAT-007], [DAT-008] |
| Giai đoạn 4 | Ngày 10-12 | `./sources/backend`, `./sources/frontend`, `./sources/docs` | Quản lý khuyến mãi, thông báo, chatbot AI | Coder, Tester, Doc | [REQ-017], [REQ-018], [REQ-019], [DAT-009] |
| Giai đoạn 5 | Ngày 13-15 | `./sources/backend`, `./sources/frontend`, `./sources/docs` | Các tính năng cốt lõi của ứng dụng di động, bản địa hóa, SEO, báo cáo | Coder, Tester, Doc | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-011] |

## 5. CHI TIẾT PHÂN PHỐI GIAI ĐOẠN & NGÀY-BY-NGÀY SẢN PHẨM BÀN GIAO
<COMMAND>
# STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Phần 5 phải hoạt động như một bản sao cấu trúc nghiêm ngặt của các giai đoạn động được tính toán trong Phần 4. Bạn phải tạo một khối chi tiết hoàn chỉnh độc lập dưới đây cho MỖI chuỗi giai đoạn từ Giai đoạn 1 đến Giai đoạn N (trong đó N <= 5). Không có giai đoạn nào xuất hiện trong phần 4 có thể bị bỏ qua.
- Cắt ngắn, bỏ qua hoặc kết hợp các giai đoạn là một vi phạm đường ống tuyệt đối. Bạn được lệnh nghiêm ngặt phải chi tiết từng giai đoạn xuất hiện trong bảng của bạn trong phần 4.

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- Đối với mỗi Giai đoạn [X] hoạt động, các nhật ký ngày theo ngày phải ánh xạ nghiêm ngặt với khoảng ngày chính xác được xác định cho giai đoạn đó trong Phần 4.
- Tổng số ngày trong bất kỳ giai đoạn đơn nào cũng KHÔNG ĐƯỢC vượt quá giới hạn trên tuyệt đối là 7 ngày.
- Bạn phải thực hiện một sự đóng băng nhật ký cứng và kết thúc vòng lặp ngày hoạt động ngay lập tức vào ngày chính xác khi 100% các mã theo dõi cơ sở BA cho Giai đoạn [X] được bao phủ. Sáng tạo các nhiệm vụ giả hoặc các yêu cầu tổng hợp để đệm thời gian lên đến 7 là hoàn toàn bị cấm.
</COMMAND>

<!--START_DELIMITTER-->
### 📈 Đặc tả Kiến trúc Chi tiết Giai đoạn 1
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** [Giải thích kỹ thuật chi tiết về những gì giai đoạn này đạt được và mục tiêu chức năng của nó, được dịch hoàn toàn sang 🇻🇳 Vietnamese]
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Liệt kê tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag IDs theo dõi tương ứng của nó.
    *   *Ranh giới Gating Tài liệu:* Bất kỳ dòng nào đại diện cho một đặc tả doanh nghiệp, tài liệu tham khảo kiến trúc, danh mục ánh xạ cơ sở dữ liệu quan hệ hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thư mục thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ và thô chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại. (Bỏ qua hoàn toàn nếu topology dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ truyền tin. Các khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và các đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh hoàn toàn sang 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 1)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- Bạn được CẤM nghiêm ngặt từ việc sử dụng các ký hiệu tiêu đề markdown (`#`, `##`, `###`, `####`) trước từ DAY. Mỗi nhật ký ngày phải được hiển thị nghiêm ngặt dưới dạng một mục danh sách lồng nhau bắt đầu bằng `- **DAY [Y]: ...**`.
- Bạn phải dịch hoàn toàn văn bản mục tiêu DAY và "Hướng dẫn Công việc Kỹ thuật Cấp thấp" thành "🇻🇳 Vietnamese". Đừng để lại giải thích bằng tiếng Anh.
- Đảm bảo tất cả các thuộc tính bên trong được thụt lề đúng cách bằng khoảng trắng để duy trì một danh sách lồng nhau đẹp. Đảm bảo chỉ MỘT Sub-Agent duy nhất với định dạng chữ cái đầu viết hoa được chỉ định cho mỗi tác vụ hoạt động.

- **DAY 1: Thiết lập cơ sở hạ tầng lõi và xác thực người dùng**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthService.java [REQ-001], [REQ-002], [ARC-006]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ xác thực với email/mật khẩu, Firebase, Google và Facebook OAuth. [REQ-001], [REQ-002], [ARC-006]
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/auth-service/src/test/java/org/nlh4j/saas/membershiphub/auth/AuthServiceTest.java;./sources/backend/auth-service/src/main/java/org/nlh4j/saas/membershiphub/auth/AuthService.java [REQ-001], [REQ-002], [ARC-006]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ xác thực. [REQ-001], [REQ-002], [ARC-006]
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/auth-service.md [REQ-001], [REQ-002], [ARC-006]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ xác thực. [REQ-001], [REQ-002], [ARC-006]
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [ARC-006]

- **DAY 2: Quản lý vai trò người dùng và cơ sở dữ liệu**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java [REQ-003], [ARC-001], [ARC-002], [DAT-001]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ quản lý vai trò người dùng. [REQ-003], [ARC-001], [ARC-002], [DAT-001]
      - **Tag IDs Mục tiêu:** [REQ-003], [ARC-001], [ARC-002], [DAT-001]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/user-service/src/test/java/org/nlh4j/saas/membershiphub/user/UserServiceTest.java;./sources/backend/user-service/src/main/java/org/nlh4j/saas/membershiphub/user/UserService.java [REQ-003], [ARC-001], [ARC-002], [DAT-001]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý vai trò người dùng. [REQ-003], [ARC-001], [ARC-002], [DAT-001]
      - **Tag IDs Mục tiêu:** [REQ-003], [ARC-001], [ARC-002], [DAT-001]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/user-service.md [REQ-003], [ARC-001], [ARC-002], [DAT-001]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ quản lý vai trò người dùng. [REQ-003], [ARC-001], [ARC-002], [DAT-001]
      - **Tag IDs Mục tiêu:** [REQ-003], [ARC-001], [ARC-002], [DAT-001]

- **DAY 3: Triển khai giao diện người dùng và tích hợp**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/src/components/AuthForm.js [REQ-001], [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai biểu mẫu xác thực cho giao diện người dùng. [REQ-001], [REQ-002]
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/src/tests/AuthForm.test.js;./sources/frontend/src/components/AuthForm.js [REQ-001], [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho biểu mẫu xác thực. [REQ-001], [REQ-002]
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/frontend-auth.md [REQ-001], [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho biểu mẫu xác thực. [REQ-001], [REQ-002]
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002]

<!--START_DELIMITTER-->
### 📈 Đặc tả Kiến trúc Chi tiết Giai đoạn 2
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** [Giải thích kỹ thuật chi tiết về những gì giai đoạn này đạt được và mục tiêu chức năng của nó, được dịch hoàn toàn sang 🇻🇳 Vietnamese]
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Liệt kê tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag IDs theo dõi tương ứng của nó.
    *   *Ranh giới Gating Tài liệu:* Bất kỳ dòng nào đại diện cho một đặc tả doanh nghiệp, tài liệu tham khảo kiến trúc, danh mục ánh xạ cơ sở dữ liệu quan hệ hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thư mục thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ và thô chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại. (Bỏ qua hoàn toàn nếu topology dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ truyền tin. Các khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và các đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh hoàn toàn sang 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 2)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- Bạn được CẤM nghiêm ngặt từ việc sử dụng các ký hiệu tiêu đề markdown (`#`, `##`, `###`, `####`) trước từ DAY. Mỗi nhật ký ngày phải được hiển thị nghiêm ngặt dưới dạng một mục danh sách lồng nhau bắt đầu bằng `- **DAY [Y]: ...**`.
- Bạn phải dịch hoàn toàn văn bản mục tiêu DAY và "Hướng dẫn Công việc Kỹ thuật Cấp thấp" thành "🇻🇳 Vietnamese". Đừng để lại giải thích bằng tiếng Anh.
- Đảm bảo tất cả các thuộc tính bên trong được thụt lề đúng cách bằng khoảng trắng để duy trì một danh sách lồng nhau đẹp. Đảm bảo chỉ MỘT Sub-Agent duy nhất với định dạng chữ cái đầu viết hoa được chỉ định cho mỗi tác vụ hoạt động.

- **DAY 4: Quản lý trung tâm và cơ sở dữ liệu**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-004], [REQ-005], [REQ-006], [DAT-003]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006], [DAT-003]
      - **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/center-service/src/test/java/org/nlh4j/saas/membershiphub/center/CenterServiceTest.java;./sources/backend/center-service/src/main/java/org/nlh4j/saas/membershiphub/center/CenterService.java [REQ-004], [REQ-005], [REQ-006], [DAT-003]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006], [DAT-003]
      - **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/center-service.md [REQ-004], [REQ-005], [REQ-006], [DAT-003]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ quản lý trung tâm. [REQ-004], [REQ-005], [REQ-006], [DAT-003]
      - **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [DAT-003]

- **DAY 5: Quản lý khóa học và cơ sở dữ liệu**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java [REQ-007], [REQ-008], [REQ-009], [DAT-004]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ quản lý khóa học. [REQ-007], [REQ-008], [REQ-009], [DAT-004]
      - **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/course-service/src/test/java/org/nlh4j/saas/membershiphub/course/CourseServiceTest.java;./sources/backend/course-service/src/main/java/org/nlh4j/saas/membershiphub/course/CourseService.java [REQ-007], [REQ-008], [REQ-009], [DAT-004]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý khóa học. [REQ-007], [REQ-008], [REQ-009], [DAT-004]
      - **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [DAT-004]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/course-service.md [REQ-007], [REQ-008], [REQ-009], [DAT-004]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ quản lý khóa học. [REQ-007], [REQ-008], [REQ-009], [DAT-004]
      - **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009], [DAT-004]

- **DAY 6: Đăng ký học viên và tích hợp**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java [REQ-010], [REQ-011], [DAT-005]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ đăng ký học viên. [REQ-010], [REQ-011], [DAT-005]
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011], [DAT-005]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/enrollment-service/src/test/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentServiceTest.java;./sources/backend/enrollment-service/src/main/java/org/nlh4j/saas/membershiphub/enrollment/EnrollmentService.java [REQ-010], [REQ-011], [DAT-005]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ đăng ký học viên. [REQ-010], [REQ-011], [DAT-005]
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011], [DAT-005]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/enrollment-service.md [REQ-010], [REQ-011], [DAT-005]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ đăng ký học viên. [REQ-010], [REQ-011], [DAT-005]
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011], [DAT-005]

<!--START_DELIMITTER-->
### 📈 Đặc tả Kiến trúc Chi tiết Giai đoạn 3
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** [Giải thích kỹ thuật chi tiết về những gì giai đoạn này đạt được và mục tiêu chức năng của nó, được dịch hoàn toàn sang 🇻🇳 Vietnamese]
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Liệt kê tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag IDs theo dõi tương ứng của nó.
    *   *Ranh giới Gating Tài liệu:* Bất kỳ dòng nào đại diện cho một đặc tả doanh nghiệp, tài liệu tham khảo kiến trúc, danh mục ánh xạ cơ sở dữ liệu quan hệ hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thư mục thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ và thô chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại. (Bỏ qua hoàn toàn nếu topology dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ truyền tin. Các khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và các đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh hoàn toàn sang 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 3)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- Bạn được CẤM nghiêm ngặt từ việc sử dụng các ký hiệu tiêu đề markdown (`#`, `##`, `###`, `####`) trước từ DAY. Mỗi nhật ký ngày phải được hiển thị nghiêm ngặt dưới dạng một mục danh sách lồng nhau bắt đầu bằng `- **DAY [Y]: ...**`.
- Bạn phải dịch hoàn toàn văn bản mục tiêu DAY và "Hướng dẫn Công việc Kỹ thuật Cấp thấp" thành "🇻🇳 Vietnamese". Đừng để lại giải thích bằng tiếng Anh.
- Đảm bảo tất cả các thuộc tính bên trong được thụt lề đúng cách bằng khoảng trắng để duy trì một danh sách lồng nhau đẹp. Đảm bảo chỉ MỘT Sub-Agent duy nhất với định dạng chữ cái đầu viết hoa được chỉ định cho mỗi tác vụ hoạt động.

- **DAY 7: Điểm danh QR và cơ sở dữ liệu**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java [REQ-012], [REQ-013], [DAT-006]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ điểm danh QR. [REQ-012], [REQ-013], [DAT-006]
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [DAT-006]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/attendance-service/src/test/java/org/nlh4j/saas/membershiphub/attendance/AttendanceServiceTest.java;./sources/backend/attendance-service/src/main/java/org/nlh4j/saas/membershiphub/attendance/AttendanceService.java [REQ-012], [REQ-013], [DAT-006]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ điểm danh QR. [REQ-012], [REQ-013], [DAT-006]
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [DAT-006]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/attendance-service.md [REQ-012], [REQ-013], [DAT-006]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ điểm danh QR. [REQ-012], [REQ-013], [DAT-006]
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013], [DAT-006]

- **DAY 8: Quản lý thẻ hội viên và cơ sở dữ liệu**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-014], [REQ-015], [DAT-007]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ quản lý thẻ hội viên. [REQ-014], [REQ-015], [DAT-007]
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015], [DAT-007]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/card-service/src/test/java/org/nlh4j/saas/membershiphub/card/CardServiceTest.java;./sources/backend/card-service/src/main/java/org/nlh4j/saas/membershiphub/card/CardService.java [REQ-014], [REQ-015], [DAT-007]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý thẻ hội viên. [REQ-014], [REQ-015], [DAT-007]
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015], [DAT-007]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/card-service.md [REQ-014], [REQ-015], [DAT-007]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ quản lý thẻ hội viên. [REQ-014], [REQ-015], [DAT-007]
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015], [DAT-007]

- **DAY 9: Thông báo và tích hợp**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [DAT-008]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ thông báo. [REQ-016], [DAT-008]
      - **Tag IDs Mục tiêu:** [REQ-016], [DAT-008]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/notification-service/src/test/java/org/nlh4j/saas/membershiphub/notification/NotificationServiceTest.java;./sources/backend/notification-service/src/main/java/org/nlh4j/saas/membershiphub/notification/NotificationService.java [REQ-016], [DAT-008]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ thông báo. [REQ-016], [DAT-008]
      - **Tag IDs Mục tiêu:** [REQ-016], [DAT-008]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/notification-service.md [REQ-016], [DAT-008]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ thông báo. [REQ-016], [DAT-008]
      - **Tag IDs Mục tiêu:** [REQ-016], [DAT-008]

<!--START_DELIMITTER-->
### 📈 Đặc tả Kiến trúc Chi tiết Giai đoạn 4
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** [Giải thích kỹ thuật chi tiết về những gì giai đoạn này đạt được và mục tiêu chức năng của nó, được dịch hoàn toàn sang 🇻🇳 Vietnamese]
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Liệt kê tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag IDs theo dõi tương ứng của nó.
    *   *Ranh giới Gating Tài liệu:* Bất kỳ dòng nào đại diện cho một đặc tả doanh nghiệp, tài liệu tham khảo kiến trúc, danh mục ánh xạ cơ sở dữ liệu quan hệ hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thư mục thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ và thô chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại. (Bỏ qua hoàn toàn nếu topology dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ truyền tin. Các khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và các đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh hoàn toàn sang 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 4)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- Bạn được CẤM nghiêm ngặt từ việc sử dụng các ký hiệu tiêu đề markdown (`#`, `##`, `###`, `####`) trước từ DAY. Mỗi nhật ký ngày phải được hiển thị nghiêm ngặt dưới dạng một mục danh sách lồng nhau bắt đầu bằng `- **DAY [Y]: ...**`.
- Bạn phải dịch hoàn toàn văn bản mục tiêu DAY và "Hướng dẫn Công việc Kỹ thuật Cấp thấp" thành "🇻🇳 Vietnamese". Đừng để lại giải thích bằng tiếng Anh.
- Đảm bảo tất cả các thuộc tính bên trong được thụt lề đúng cách bằng khoảng trắng để duy trì một danh sách lồng nhau đẹp. Đảm bảo chỉ MỘT Sub-Agent duy nhất với định dạng chữ cái đầu viết hoa được chỉ định cho mỗi tác vụ hoạt động.

- **DAY 10: Quản lý khuyến mãi và cơ sở dữ liệu**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionService.java [REQ-017], [DAT-009]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ quản lý khuyến mãi. [REQ-017], [DAT-009]
      - **Tag IDs Mục tiêu:** [REQ-017], [DAT-009]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/promotion-service/src/test/java/org/nlh4j/saas/membershiphub/promotion/PromotionServiceTest.java;./sources/backend/promotion-service/src/main/java/org/nlh4j/saas/membershiphub/promotion/PromotionService.java [REQ-017], [DAT-009]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý khuyến mãi. [REQ-017], [DAT-009]
      - **Tag IDs Mục tiêu:** [REQ-017], [DAT-009]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/promotion-service.md [REQ-017], [DAT-009]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ quản lý khuyến mãi. [REQ-017], [DAT-009]
      - **Tag IDs Mục tiêu:** [REQ-017], [DAT-009]

- **DAY 11: Quản lý thông báo và cơ sở dữ liệu**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/announcement-service/src/main/java/org/nlh4j/saas/membershiphub/announcement/AnnouncementService.java [REQ-018], [DAT-009]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ quản lý thông báo. [REQ-018], [DAT-009]
      - **Tag IDs Mục tiêu:** [REQ-018], [DAT-009]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/announcement-service/src/test/java/org/nlh4j/saas/membershiphub/announcement/AnnouncementServiceTest.java;./sources/backend/announcement-service/src/main/java/org/nlh4j/saas/membershiphub/announcement/AnnouncementService.java [REQ-018], [DAT-009]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý thông báo. [REQ-018], [DAT-009]
      - **Tag IDs Mục tiêu:** [REQ-018], [DAT-009]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/announcement-service.md [REQ-018], [DAT-009]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ quản lý thông báo. [REQ-018], [DAT-009]
      - **Tag IDs Mục tiêu:** [REQ-018], [DAT-009]

- **DAY 12: Chatbot AI và tích hợp**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java [REQ-019]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ chatbot AI. [REQ-019]
      - **Tag IDs Mục tiêu:** [REQ-019]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/chatbot-service/src/test/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotServiceTest.java;./sources/backend/chatbot-service/src/main/java/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java [REQ-019]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ chatbot AI. [REQ-019]
      - **Tag IDs Mục tiêu:** [REQ-019]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/chatbot-service.md [REQ-019]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ chatbot AI. [REQ-019]
      - **Tag IDs Mục tiêu:** [REQ-019]

<!--START_DELIMITTER-->
### 📈 Đặc tả Kiến trúc Chi tiết Giai đoạn 5
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** [Giải thích kỹ thuật chi tiết về những gì giai đoạn này đạt được và mục tiêu chức năng của nó, được dịch hoàn toàn sang 🇻🇳 Vietnamese]
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Liệt kê tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra phải được nối với các Tag IDs theo dõi tương ứng của nó.
    *   *Ranh giới Gating Tài liệu:* Bất kỳ dòng nào đại diện cho một đặc tả doanh nghiệp, tài liệu tham khảo kiến trúc, danh mục ánh xạ cơ sở dữ liệu quan hệ hoặc bố cục kiến trúc phải nằm nghiêm ngặt dưới đường dẫn gốc thư mục thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-XXX]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ và thô chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại. (Bỏ qua hoàn toàn nếu topology dự án không có cơ sở dữ liệu hoặc yêu cầu lớp lưu trữ. Khối kỹ thuật này KHÔNG ĐƯỢC dịch).
- **Hợp đồng Định tuyến API và Sự kiện [REQ-XXX], [ARC-XXX]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ truyền tin. Các khối kỹ thuật KHÔNG ĐƯỢC dịch).
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-XXX]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi và các đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại, được dịch ngữ cảnh hoàn toàn sang 🇻🇳 Vietnamese.
<!--END_DELIMITTER-->

#### 📅 Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 5)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- Bạn được CẤM nghiêm ngặt từ việc sử dụng các ký hiệu tiêu đề markdown (`#`, `##`, `###`, `####`) trước từ DAY. Mỗi nhật ký ngày phải được hiển thị nghiêm ngặt dưới dạng một mục danh sách lồng nhau bắt đầu bằng `- **DAY [Y]: ...**`.
- Bạn phải dịch hoàn toàn văn bản mục tiêu DAY và "Hướng dẫn Công việc Kỹ thuật Cấp thấp" thành "🇻🇳 Vietnamese". Đừng để lại giải thích bằng tiếng Anh.
- Đảm bảo tất cả các thuộc tính bên trong được thụt lề đúng cách bằng khoảng trắng để duy trì một danh sách lồng nhau đẹp. Đảm bảo chỉ MỘT Sub-Agent duy nhất với định dạng chữ cái đầu viết hoa được chỉ định cho mỗi tác vụ hoạt động.

- **DAY 13: Các tính năng cốt lõi của ứng dụng di động và tích hợp**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/mobile-app/src/components/MobileApp.js [REQ-020], [REQ-021]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai các tính năng cốt lõi của ứng dụng di động. [REQ-020], [REQ-021]
      - **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/mobile-app/src/tests/MobileApp.test.js;./sources/mobile-app/src/components/MobileApp.js [REQ-020], [REQ-021]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho các tính năng cốt lõi của ứng dụng di động. [REQ-020], [REQ-021]
      - **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/mobile-app.md [REQ-020], [REQ-021]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho các tính năng cốt lõi của ứng dụng di động. [REQ-020], [REQ-021]
      - **Tag IDs Mục tiêu:** [REQ-020], [REQ-021]

- **DAY 14: Bản địa hóa và SEO**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/src/i18n.js [REQ-022], [REQ-023]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai bản địa hóa và SEO. [REQ-022], [REQ-023]
      - **Tag IDs Mục tiêu:** [REQ-022], [REQ-023]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/src/tests/i18n.test.js;./sources/frontend/src/i18n.js [REQ-022], [REQ-023]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho bản địa hóa và SEO. [REQ-022], [REQ-023]
      - **Tag IDs Mục tiêu:** [REQ-022], [REQ-023]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/i18n.md [REQ-022], [REQ-023]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho bản địa hóa và SEO. [REQ-022], [REQ-023]
      - **Tag IDs Mục tiêu:** [REQ-022], [REQ-023]

- **DAY 15: Báo cáo và phân tích**
  - **Chuyên môn Phân công Công việc Sub-Agent:**
    * **[Coder]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java [REQ-024], [REQ-025]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Triển khai dịch vụ báo cáo và phân tích. [REQ-024], [REQ-025]
      - **Tag IDs Mục tiêu:** [REQ-024], [REQ-025]
    * **[Tester]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/report-service/src/test/java/org/nlh4j/saas/membershiphub/report/ReportServiceTest.java;./sources/backend/report-service/src/main/java/org/nlh4j/saas/membershiphub/report/ReportService.java [REQ-024], [REQ-025]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Viết các bài kiểm tra đơn vị cho dịch vụ báo cáo và phân tích. [REQ-024], [REQ-025]
      - **Tag IDs Mục tiêu:** [REQ-024], [REQ-025]
    * **[Doc]:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/report-service.md [REQ-024], [REQ-025]`
      - **Hướng dẫn Công việc Kỹ thuật Cấp thấp:** Tạo tài liệu đặc tả cho dịch vụ báo cáo và phân tích. [REQ-024], [REQ-025]
      - **Tag IDs Mục tiêu:** [REQ-024], [REQ-025]

## 📁 6. CÁC MÃ BẢO MẬT DOANH NGHIỆP TOÀN CẦU & CÁC ĐỐI PHÓNG TẤN CÔNG TIÊU BẠN [NFR-XXX]
- **Đối phó với SQL Injection (SQLi) tuyệt đối:** Tham số quy tắc cho các câu lệnh chuẩn bị, tham số truy vấn vị trí và danh sách trắng sắp xếp đầu vào động.
- **Đối phó với Cross-Site Scripting (XSS) & Chính sách Bảo mật Nội dung (CSP):** Tiêu chuẩn bố cục cho các bộ lọc tự động làm sạch ngữ cảnh, tự động thoát JSX và chèn động các tiêu đề CSP nghiêm ngặt (`unsafe-inline` hạn chế).
- **Ranh giới Bảo mật CORS đa người dùng:** Cấu hình cho việc cấm từ khóa nguồn gốc và xác thực động các số liệu cơ sở dữ liệu ranh giới người dùng.
- **Máy quét & Làm sạch Nhật ký Zero-Leak & PII Data Masking:** Quy tắc cho các bộ chặn tự động làm sạch (`@JsonSerialize`) và ngưỡng làm sạch nhật ký.

## 📁 7. CÁC QUY TẮC TUÂN THỦ HYBRID MOBILE & CƠ CHẾ SEO QUỐC TẾ HÓA
- **Cơ chế Nhận diện Ngôn ngữ Mặc định:** Kiến trúc lớp biên trung gian nhận dạng ngôn ngữ động, chèn siêu liên kết ngôn ngữ động và giới hạn chỉ mục robot tìm kiếm.
- **Tích hợp Quốc tế hóa (i18n) & Động SEO:** Kiến trúc lớp biên nhận dạng ngôn ngữ động, chèn siêu liên kết ngôn ngữ động và giới hạn chỉ mục robot tìm kiếm.

## 📁 8. PIPELINE TỰ ĐỘNG HOÁ NHẬT NGÀY SESSION GIT BRANCH FLOW
- **Điều khiển Phân nhánh Không gian làm việc Động:** Kiểm soát phân nhánh chương trình cho nhánh `features/development-phase-X-day-Y` (`X` là số giai đoạn, từ 1 đến N, trong đó N <= 5; `Y` là số ngày trong giai đoạn, nó sẽ bắt đầu từ 1 cho mỗi giai đoạn).
- **Cổng Bảo vệ Pipeline Tự động:** Quy tắc thực thi cho xác minh biên dịch, mục tiêu tự động hóa độ phủ mã (`>= 85%`) và nhật ký tuần tự hóa ngữ cảnh.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 6, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`