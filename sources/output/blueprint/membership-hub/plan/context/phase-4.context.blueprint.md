# Giai đoạn 4: <!--PHASE_NAME_START-->Xây dựng giao diện người dùng và ứng dụng di động<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Sơ đồ** | ARCH-20260805161738 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng giao diện người dùng và ứng dụng di động<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng giao diện người dùng và ứng dụng di động<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/05 16:17:38 |
| **Tác giả** | Kiến trúc hệ thống doanh nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban quản lý kỹ thuật |

## 1. Phạm vi hoạt động và mục tiêu của giai đoạn
Giai đoạn này tập trung vào việc xây dựng giao diện người dùng và ứng dụng di động. Các giao diện này bao gồm các tính năng như chatbot, giao diện người dùng di động, thông báo đẩy và hỗ trợ đa ngôn ngữ.

## 2. Phạm vi kỹ thuật và biên giới thư mục được phép (Tệp, đường dẫn và điểm cuối)
- `./sources/frontend`
- `./sources/mobile`

## 3. Hướng dẫn chức năng chuyên dụng của Sub-Agent
*   **Coder**: Hoạt động như một Nhà phát triển Ứng dụng Cấp cao/Chuyên gia. Trách nhiệm triển khai mã nguồn ứng dụng thuần túy trên cả dịch vụ backend và ứng dụng frontend/mobile. Cấm viết bộ kiểm tra hoặc biểu hiện cơ sở hạ tầng.
*   **Tester**: Hoạt động như một Trưởng/Chuyên gia QC/QA. Chuyên về kỹ thuật bộ kiểm tra, xác nhận và cổng chất lượng. Trách nhiệm tạo ra JUnit, bộ kiểm tra tích hợp, kiểm tra tự động E2E và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã nguồn sản xuất.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, sửa chữa lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Doc**: Hoạt động như một Nhà viết tài liệu kỹ thuật cấp cao và Kiến trúc hệ thống doanh nghiệp. Chuyên về biên soạn các tài liệu kỹ thuật Markdown toàn diện, tham chiếu lược đồ, bản đồ hệ thống và danh mục kiến trúc. Mỗi tệp tài liệu được tạo ra phải nằm nghiêm ngặt trong bố cục lưu trữ tập trung: `./sources/docs/`.
<!-- START_COMMAND_DIRECTIVE_DO_NOT_DISPLAY
[CRITIAL COMMAND:
    # MANDATORY AGENT DOC ALLOCATION MANDATE (CRITICAL GATE):
    - You are STRICTLY FORBIDDEN from omitting or dropping the 'Doc' agent from any computed phase.
    - For EVERY calculated phase, on **Day 1** of that phase, you MUST explicitly allocate a foundational system documentation task to the **Doc** agent. This task MUST require the 'Doc' agent to map out the architecture, endpoints, database schemas, or deployment topology blueprints corresponding to the active stack of that phase.
    - Failing to allocate the 'Doc' agent on Day 1 of any phase triggers a catastrophic engineering contract violation.
]
END_COMMAND_DIRECTIVE_DO_NOT_DISPLAY-->
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác minh lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm xây dựng biểu hiện triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng microservices vào các cụm GKE hoạt động.

## 4. Định nghĩa Hoàn thành Giai đoạn (DoD)
- Xây dựng giao diện người dùng và ứng dụng di động hoàn thành.
- Tất cả các yêu cầu chức năng được xác định trong giai đoạn này đã được triển khai và kiểm tra.
- Tất cả các yêu cầu bảo mật OWASP đã được tuân thủ.
- Tất cả các bài kiểm tra đơn vị và tích hợp đã được thực hiện và vượt qua.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ Ngày 1: <!--DAY_HEADER_START-->XÂY DỰNG GIAO DIỆN NGƯỜI DÙNG VÀ ỨNG DỤNG DI ĐỘNG<!--DAY_HEADER_END-->

#### 📝 Công việc con 1.1: Triển khai giao diện người dùng và ứng dụng di động
##### Sub-Agent được chỉ định: Coder
##### Thành phần và yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/frontend`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [DAT-011]<!--END_TAGS-->

#### 📝 Công việc con 1.2: Viết các bài kiểm tra đơn vị và tích hợp cho giao diện người dùng và ứng dụng di động
##### Sub-Agent được chỉ định: Tester
##### Thành phần và yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/frontend;./sources/frontend/src/test/java/org/nlh4j/saas/membershiphub/frontend/FrontendServiceTest.java`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]<!--END_TAGS-->

#### 📝 Công việc con 1.3: Đánh giá mã nguồn và đảm bảo tuân thủ các tiêu chuẩn lập trình
##### Sub-Agent được chỉ định: Reviewer
##### Thành phần và yêu cầu kỹ thuật mục tiêu:
* **Đường dẫn mục tiêu:** `./sources/frontend`
* **Token Tag Tính theo dõi:** <!--START_TAGS-->[REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023]<!--END_TAGS-->