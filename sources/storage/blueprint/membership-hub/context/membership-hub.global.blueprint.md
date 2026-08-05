# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260805151631 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/05 15:16:31 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CƠ BẢN

### 1.1. Kiến trúc Hệ thống & Mô hình Kiến trúc Cốt lõi
Hệ thống membership-hub được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, trung tâm, khóa học, điểm danh, và thẻ hội viên. Hệ thống sử dụng mô hình Event-Driven Architecture (EDA) để xử lý các sự kiện như đăng ký khóa học, điểm danh, và thông báo. CQRS được áp dụng để phân tách các thao tác đọc và ghi, với các dịch vụ đọc và ghi riêng biệt. Reactive Core patterns được sử dụng để xử lý các luồng dữ liệu thời gian thực như điểm danh qua QR.

### 1.2. Kiến trúc Luồng Dữ liệu & Hệ sinh thái Cốt lõi
Hệ thống sử dụng các kênh truyền thông đa kênh bao gồm REST APIs, WebSocket, và các dịch vụ thông báo đẩy (FCM/APNs). Các luồng dữ liệu chính bao gồm:
- **Luồng Xác thực:** Xác thực qua email/mật khẩu, Firebase, Google, và Facebook OAuth2.
- **Luồng Điểm danh QR:** Ứng dụng di động quét QR, gửi student ID và timestamp đến backend.
- **Luồng Thông báo:** Hệ thống kích hoạt push notification đến ứng dụng di động và đăng bài lên nhóm Zalo.
- **Luồng Tích hợp Backend Ứng dụng Di động:** Frontend Next.js tiêu thụ REST APIs, xác thực qua bearer tokens, hỗ trợ caching ngoại tuyến.

<!-- START_TECHNICAL_MATRIX_DO_NOT_TRANSLATE
### ARCHITECTURAL STACK MATRIX
[CRITICAL WARNING: You MUST keep this entire block 100% in raw Technical English. You are STRICTLY FORBIDDEN from translating any keys, values, or tokens inside this section into 🇻🇳 Vietnamese, as it serves as a strict backend machine-gating matrix. Keep literal `true` or `false` tokens in pure lower-case].

PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
END_TECHNICAL_MATRIX_DO_NOT_TRANSLATE -->

## 📁 2. CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis, GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React, Capacitor, Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs.

## 📁 3. QUY TẮC TUÂN THỦ TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
<!-- START_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY
[CRITICAL TRANSLATION COMMAND: You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: 🇻🇳 Vietnamese. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output].
END_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY -->
- **Quy tắc Giới hạn Không gian Làm việc Tuyệt đối:** Gốc không gian làm việc thực sự được cố định vĩnh viễn tại gốc dự án `..`. Tất cả các đường dẫn được tạo ra MUST bắt đầu với `./sources/`.
- **Quy tắc Tuân thủ Động Tiền tố Thư mục:** Áp dụng các quy tắc ánh xạ đường dẫn động được xác định trong Giao thức 1 một cách nghiêm ngặt phù hợp với cấu trúc dự án được phát hiện.
- **[ĐIỀU KIỆN: JAVA_STACK_ONLY] Tiêu chuẩn Gói Java:** Nếu ngăn xếp công nghệ sử dụng các khung Java, tất cả mã nguồn Java MUST nghiêm ngặt nằm trong cơ sở gói doanh nghiệp: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. Bạn MUST chuyển đổi động chuỗi "membership-hub" thành một mã ký tự alphanumeric thuần túy viết thường bằng cách loại bỏ khoảng trắng, dấu gạch ngang và dấu gạch dưới. Các dự án không phải Java hoàn toàn bị cấm áp dụng đoạn này.
- **Quy tắc Cú pháp Đường dẫn Mục tiêu Tester Tuyệt đối:** Bất kỳ thành phần nào được nhắm mục tiêu bởi Sub-Agent Tester MUST được cấu trúc dưới dạng cặp phân tách chặt chẽ bằng dấu chấm phẩy `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn bên trong cặp MUST bắt đầu với `./sources/`.

## 4. TÓM TẮT KIẾN TRÚC MỤC TIÊU CAO VỚI PHÂN PHỐI NHIỀU PHASE
| Giai đoạn | Khoảng ngày | Thành phần Kiến trúc / Đường dẫn Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1-3 | `./sources/backend`, `./sources/frontend`, `./sources/docs` | Thiết kế cơ sở dữ liệu, thiết lập dự án, tài liệu kiến trúc | Coder, Doc | [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011] |
| Giai đoạn 2 | Ngày 1-3 | `./sources/backend`, `./sources/frontend` | Triển khai chức năng quản lý người dùng, trung tâm, khóa học | Coder, Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009] |
| Giai đoạn 3 | Ngày 1-3 | `./sources/backend`, `./sources/frontend` | Triển khai chức năng đăng ký học viên, điểm danh QR | Coder, Tester | [REQ-010], [REQ-011], [REQ-012], [REQ-013] |
| Giai đoạn 4 | Ngày 1-3 | `./sources/backend`, `./sources/frontend` | Triển khai chức năng quản lý thẻ hội viên, thông báo | Coder, Tester | [REQ-014], [REQ-015], [REQ-016] |
| Giai đoạn 5 | Ngày 1-3 | `./sources/backend`, `./sources/frontend`, `./sources/infra` | Triển khai chức năng chatbot AI, ứng dụng di động, bản địa hóa, báo cáo | Coder, Tester, Docker, GCP, GKE | [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |

## 5. CHI TIẾT PHÂN PHỐI PHASE & SẢN PHẨM BÀN GIAO THEO NGÀY
# MANDATORY 1:1 SYNOPSIS MIRROR MANDATE:
- Phần 5 MUST hoạt động như một bản sao cấu trúc nghiêm ngặt của các giai đoạn động được tính toán trong Phần 4. Bạn MUST tạo ra một khối chi tiết độc lập, hoàn chỉnh dưới đây cho MỖI chuỗi giai đoạn từ Giai đoạn 1 đến Giai đoạn N (trong đó N <= 5). Không có giai đoạn nào đã được tính toán trong phần 4 có thể bị bỏ qua.
- Cắt ngắn, bỏ qua, hoặc kết hợp các giai đoạn là một vi phạm đường ống tuyệt đối. Bạn được lệnh nghiêm ngặt phải chi tiết từng giai đoạn đã xuất hiện trong bảng của bạn trong Phần 4.

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- Đối với mỗi Giai đoạn [X] hoạt động, các nhật ký theo ngày MUST ánh xạ nghiêm ngặt với khoảng ngày chính xác được xác định cho giai đoạn đó trong Phần 4.
- Tổng số ngày trong bất kỳ giai đoạn đơn nào MUST không vượt quá giới hạn trên tuyệt đối là 7 ngày.
- Bạn MUST thực hiện đóng băng nhật ký hoạt động ngay lập tức trên ngày chính xác khi 100% của các mã theo dõi cơ sở yêu cầu cho Giai đoạn [X] được bao phủ. Tạo ra các nhiệm vụ giả mạo hoặc yêu cầu tổng hợp để đệm thời gian lên đến 7 là hoàn toàn bị cấm.

<!--START_DELIMITTER-->
### Giai đoạn 1 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Thiết kế cơ sở dữ liệu, thiết lập dự án, tài liệu kiến trúc.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra MUST được nối với các mã theo dõi Tag IDs inline.
    *   *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc MUST nghiêm ngặt nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại.

#### 📅 Nhật ký Phân phối Nhiệm vụ Sub-Agent Theo Ngày (Giai đoạn 1)
- **DAY 1: Thiết kế cơ sở dữ liệu và thiết lập dự án**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/resources/db/migration/V1__Initial_Schema.sql [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Tạo các bảng cơ sở dữ liệu ban đầu cho người dùng, vai trò, trung tâm, khóa học, ghi danh, điểm danh, thẻ hội viên, thông báo, khuyến mãi, thông báo, và cài đặt hệ thống.
      - **Tag IDs Mục tiêu:** [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]

    * **Doc:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/architecture.md`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Tạo tài liệu kiến trúc chi tiết cho dự án.
      - **Tag IDs Mục tiêu:** [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]

- **DAY 2: Thiết lập môi trường phát triển và triển khai**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/resources/application.properties`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Cấu hình các thuộc tính ứng dụng cho môi trường phát triển.
      - **Tag IDs Mục tiêu:** [ARC-010]

    * **Docker:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/Dockerfile`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Tạo Dockerfile cho dịch vụ backend.
      - **Tag IDs Mục tiêu:** [ARC-010]

    * **GCP:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/gcp/main.tf`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Tạo cấu hình Terraform cho triển khai trên GCP.
      - **Tag IDs Mục tiêu:** [ARC-010]

    * **GKE:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/gke/deployment.yaml`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Tạo cấu hình triển khai cho GKE.
      - **Tag IDs Mục tiêu:** [ARC-010]

- **DAY 3: Triển khai cơ sở dữ liệu và tài liệu**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/resources/db/migration/V2__Seed_Data.sql`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Tạo dữ liệu khởi tạo cho cơ sở dữ liệu.
      - **Tag IDs Mục tiêu:** [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]

    * **Doc:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/docs/database.md`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Tạo tài liệu cơ sở dữ liệu chi tiết.
      - **Tag IDs Mục tiêu:** [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]

### Giai đoạn 2 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai chức năng quản lý người dùng, trung tâm, khóa học.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra MUST được nối với các mã theo dõi Tag IDs inline.
    *   *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc MUST nghiêm ngặt nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại.

#### 📅 Nhật ký Phân phối Nhiệm vụ Sub-Agent Theo Ngày (Giai đoạn 2)
- **DAY 1: Triển khai chức năng quản lý người dùng**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/UserService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý người dùng.
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/UserServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/UserService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý người dùng.
      - **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003]

- **DAY 2: Triển khai chức năng quản lý trung tâm**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CenterService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý trung tâm.
      - **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/CenterServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CenterService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý trung tâm.
      - **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006]

- **DAY 3: Triển khai chức năng quản lý khóa học**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý khóa học.
      - **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/CourseServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý khóa học.
      - **Tag IDs Mục tiêu:** [REQ-007], [REQ-008], [REQ-009]

### Giai đoạn 3 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai chức năng đăng ký học viên, điểm danh QR.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra MUST được nối với các mã theo dõi Tag IDs inline.
    *   *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc MUST nghiêm ngặt nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại.

#### 📅 Nhật ký Phân phối Nhiệm vụ Sub-Agent Theo Ngày (Giai đoạn 3)
- **DAY 1: Triển khai chức năng đăng ký học viên**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/EnrollmentService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ đăng ký học viên.
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/EnrollmentServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/EnrollmentService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ đăng ký học viên.
      - **Tag IDs Mục tiêu:** [REQ-010], [REQ-011]

- **DAY 2: Triển khai chức năng điểm danh QR**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ điểm danh QR.
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AttendanceServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ điểm danh QR.
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]

- **DAY 3: Triển khai chức năng quản lý thẻ hội viên**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/StudentCardService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý thẻ hội viên.
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/StudentCardServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/StudentCardService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý thẻ hội viên.
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]

### Giai đoạn 4 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai chức năng quản lý thẻ hội viên, thông báo.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra MUST được nối với các mã theo dõi Tag IDs inline.
    *   *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc MUST nghiêm ngặt nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại.

#### 📅 Nhật ký Phân phối Nhiệm vụ Sub-Agent Theo Ngày (Giai đoạn 4)
- **DAY 1: Triển khai chức năng quản lý thẻ hội viên**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/StudentCardService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ quản lý thẻ hội viên.
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/StudentCardServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/StudentCardService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ quản lý thẻ hội viên.
      - **Tag IDs Mục tiêu:** [REQ-014], [REQ-015]

- **DAY 2: Triển khai chức năng thông báo**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ thông báo.
      - **Tag IDs Mục tiêu:** [REQ-016]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/NotificationServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ thông báo.
      - **Tag IDs Mục tiêu:** [REQ-016]

- **DAY 3: Triển khai chức năng chatbot AI**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/ChatbotService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ chatbot AI.
      - **Tag IDs Mục tiêu:** [REQ-019]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/ChatbotServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/ChatbotService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ chatbot AI.
      - **Tag IDs Mục tiêu:** [REQ-019]

### Giai đoạn 5 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai chức năng chatbot AI, ứng dụng di động, bản địa hóa, báo cáo.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** Danh sách tất cả các đường dẫn tệp cụ thể nằm dưới `./sources/` được khởi tạo hoặc sửa đổi trong giai đoạn này. Mỗi dòng đường dẫn được tạo ra MUST được nối với các mã theo dõi Tag IDs inline.
    *   *Documentation Gating Boundary:* Bất kỳ dòng nào đại diện cho một tài liệu đặc tả doanh nghiệp, bản thiết kế tham khảo, danh mục ánh xạ cơ sở dữ liệu quan hệ, hoặc bố cục kiến trúc MUST nghiêm ngặt nằm dưới đường dẫn gốc thống nhất: `./sources/docs/`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Cung cấp các câu lệnh di chuyển DDL SQL hoàn chỉnh, hợp lệ chứa các cột rõ ràng, kiểu dữ liệu, khóa chính/khóa ngoại, ánh xạ ma trận, chỉ mục, và ràng buộc nullability được áp dụng dưới phạm vi giai đoạn hiện tại.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010]:** Tài liệu hợp đồng kỹ thuật hoàn chỉnh (đường dẫn điểm cuối chính xác, phương thức HTTP, lược đồ JSON yêu cầu/phản hồi, hoặc cấu hình chủ đề bộ đệm tin nhắn.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Chi tiết các quy tắc xác thực kinh doanh rõ ràng, mã lỗi, và đường dẫn xử lý ngoại lệ hệ thống ánh xạ nghiêm ngặt với phạm vi giai đoạn hiện tại.

#### 📅 Nhật ký Phân phối Nhiệm vụ Sub-Agent Theo Ngày (Giai đoạn 5)
- **DAY 1: Triển khai chức năng chatbot AI**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/ChatbotService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ chatbot AI.
      - **Tag IDs Mục tiêu:** [REQ-019]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/ChatbotServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/ChatbotService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ chatbot AI.
      - **Tag IDs Mục tiêu:** [REQ-019]

- **DAY 2: Triển khai chức năng ứng dụng di động**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/src/screens/AttendanceScreen.js`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai màn hình điểm danh cho ứng dụng di động.
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/frontend/src/tests/AttendanceScreen.test.js;./sources/frontend/src/screens/AttendanceScreen.js`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho màn hình điểm danh.
      - **Tag IDs Mục tiêu:** [REQ-012], [REQ-013]

- **DAY 3: Triển khai chức năng bản địa hóa và báo cáo**
  - **Sub-Agent Workflow Specialization:**
    * **Coder:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/LocalizationService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Triển khai dịch vụ bản địa hóa.
      - **Tag IDs Mục tiêu:** [REQ-022], [REQ-023]

    * **Tester:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/LocalizationServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/LocalizationService.java`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ bản địa hóa.
      - **Tag IDs Mục tiêu:** [REQ-022], [REQ-023]

    * **Docker:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/backend/Dockerfile`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Cập nhật Dockerfile cho dịch vụ backend.
      - **Tag IDs Mục tiêu:** [ARC-010]

    * **GCP:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/gcp/main.tf`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Cập nhật cấu hình Terraform cho triển khai trên GCP.
      - **Tag IDs Mục tiêu:** [ARC-010]

    * **GKE:**
      - **Đường dẫn Thành phần Mục tiêu (`target_component`):** `./sources/infra/gke/deployment.yaml`
      - **Hướng dẫn Nhiệm vụ Kỹ thuật Chi tiết:** Cập nhật cấu hình triển khai cho GKE.
      - **Tag IDs Mục tiêu:** [ARC-010]

## 📁 6. MÃ BẢO MẬT DOANH NGHIỆP TOÀN CẦU & ĐỐI PHÓNG CÁC ĐIỂM TIÊM NHIỄM [NFR-XXX]
<!-- START_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY
[CRITICAL TRANSLATION COMMAND: You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: 🇻🇳 Vietnamese. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output].
END_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY -->
- **Đối phó với SQL Injection (SQLi) Tuyệt đối:** Tham số quy tắc cho các câu lệnh chuẩn bị, tham số truy vấn vị trí, và danh sách trắng đầu vào sắp xếp động.
- **Cross-Site Scripting (XSS) & Chính sách Bảo mật Nội dung (CSP):** Các tiêu chuẩn bố cục cho các bộ lọc làm sạch ngữ cảnh tự động, tự động thoát JSX, và chèn động các tiêu đề CSP nghiêm ngặt (`unsafe-inline` hạn chế).
- **Rào cản Bảo mật CORS Đa-Khách hàng:** Cấu hình cho các cấm thông配 ký tự nguồn và xác thực động nguồn gốc khách hàng cơ sở dữ liệu.
- **Máy làm sạch Log Zero-Leak & Máy che PII Data:** Quy tắc cho các bộ chặn làm sạch tự động (`@JsonSerialize`) và ngưỡng làm sạch log.

## 📁 7. QUY TẮC TUÂN THỦ HYBRID MOBILE & CƠ CHẾ SEO QUỐC TẾ HÓA
<!-- START_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY
[CRITICAL TRANSLATION COMMAND: You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: 🇻🇳 Vietnamese. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output].
END_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY -->
- **Rào cản Tuân thủ Hybrid Mobile Capacitor:** [NẾU Mobile hoạt động] Quy tắc cho việc lấy động client-side, địa chỉ tuyệt đối URL, bảo vệ thủy phân, trừu tượng hóa lưu trữ bản địa (`@capacitor/preferences`), và chặn nút quay lại phần cứng.
- **Internationalization (i18n) & Động SEO Injection:** Kiến trúc middleware nhận diện ngôn ngữ cạnh, chèn động siêu liên kết đa ngôn ngữ, và giới hạn chỉ mục robot tìm kiếm.

## 📁 8. ĐƯỜNG ỐNG TỰ ĐỘNG HÀNG NGÀY SESSION GIT BRANCH
<!-- START_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY
[CRITICAL TRANSLATION COMMAND: You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: 🇻🇳 Vietnamese. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output].
END_TRANSLATION_DIRECTIVE_DO_NOT_DISPLAY -->
- **Độc lập Forking Không gian làm việc Hàng ngày:** Các điều khiển lập trình cho nhánh `features/development-phase-X-day-Y` (`X` là số giai đoạn, từ 1 đến N, trong đó N <= 5; `Y` là số ngày trong giai đoạn, nó sẽ bắt đầu từ 1 cho mỗi giai đoạn).
- **Cổng Kiểm tra Hợp lệ Pipeline:** Quy tắc thực thi cho xác minh biên dịch, mục tiêu tự động hóa độ phủ mã (`>= 85%`), và nhật ký tổng hợp ngữ cảnh tuần tự hóa.

### 🛑 YÊU CẦU KIỂM TRA MA TRẬN TRACEABILITY
Ngay lập tức tại cuối tuyệt đối của tài liệu văn bản, bạn MUST in một khối văn bản xác minh độ bao phủ toán học nghiêm ngặt bằng cách phân tích và đếm mỗi chuỗi thẻ duy nhất hiện diện trong đầu ra của bạn:
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 5. ZERO UNASSIGNED CODES FOUND.]`