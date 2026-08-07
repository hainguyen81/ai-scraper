# Giai đoạn 2: Quản lý trung tâm

## 📊 Kiểm Soát Tài Liệu

| Mục | Chi Tiết |
| :--- | :--- |
| **ID Bản vẽ** | ARCH-20260807172813 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Quản lý trung tâm<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng CRUD trung tâm, kiểm tra tính duy nhất của taxId và phân quyền quản trị trung tâm.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 17:28:13 |
| **Tác giả** | Kiến Trúc Hệ Thống Doanh Nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban Quản Trị Kỹ Thuật |

## 1. Phạm Vi Hoạt Động & Mục Tiêu Của Giai Đoạn
Giai đoạn này tập trung vào việc triển khai CRUD trung tâm, kiểm tra tính duy nhất của taxId và phân quyền quản trị trung tâm. Các yêu cầu bao gồm xem danh sách trung tâm, tạo/cập nhật/xóa trung tâm và phân quyền quản trị trung tâm.

## 2. Phạm Vi Kỹ Thuật & Ranh Giới Thư Mục (Tệp, đường dẫn và điểm cuối)
- ./sources/backend/center/ (Coder) – [REQ-004], [REQ-005], [REQ-006], [DAT-003]
- ./sources/docs/ (Doc) – tài liệu quản lý trung tâm

## 3. Hướng Dẫn Chức Năng Cụ Thể Cho Các Đặc Sỹ Phụ
*   **Coder**: Hoạt động như một Lập Trình Viên Ứng Dụng Cấp Cao/Chuyên Gia. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và ứng dụng khách frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu hạ tầng.
* **Tester**: Hoạt động như một Trưởng/Chuyên Gia Kiểm Chất/QA. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng kiểm tra chất lượng. Trách nhiệm là tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con nhiệm vụ liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất ra chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà Viết Kỹ Thuật Chuyên Gia và Kiến Trúc Hệ Thống Doanh Nghiệp. Chuyên về biên soạn tài liệu Kỹ Thuật Chi Tiết, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp công nghệ hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác nhận lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng dịch vụ microservices vào các cụm GKE hoạt động.

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)
- Triển khai hoàn chỉnh các dịch vụ CRUD trung tâm, kiểm tra tính duy nhất của taxId và phân quyền quản trị trung tâm.
- Kiểm tra và xác nhận các yêu cầu chức năng cốt lõi.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Triển khai danh sách trung tâm, tạo trung tâm và kiểm tra xung đột taxId<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 1.1: [Triển khai danh sách trung tâm, tạo trung tâm và kiểm tra xung đột taxId]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/center/CenterController.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-004], [REQ-005], [DAT-003]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai CenterController với endpoint GET /centers trả về danh sách; POST /centers chấp nhận request body, xác thực tính duy nhất của taxId (throw ConflictException), lưu vào bảng CENTERS; thêm validation cho các trường bắt buộc; trả về response với các trường phù hợp.

* **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003]:**
```sql
CREATE TABLE CENTERS (
    centerId UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    taxId VARCHAR(13) NOT NULL UNIQUE,
    contactPhone VARCHAR(20),
    contactEmail VARCHAR(255)
);
```

* **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006]:**
```json
// GET /api/v1/centers
// Response: [{ "centerId": "uuid", "name": "Center A", "address": "Hanoi", "taxId": "1234567890123", "contactPhone": "+84123456789", "contactEmail": "center@example.com" }]

// POST /api/v1/centers
{
  "name": "Center B",
  "address": "Ho Chi Minh",
  "taxId": "9876543210987",
  "contactPhone": "+84987654321",
  "contactEmail": "centerB@example.com"
}

// PUT /api/v1/centers/{centerId}
{
  "name": "Center B Updated",
  "address": "Ho Chi Minh City",
  "taxId": "9876543210987",
  "contactPhone": "+84987654321",
  "contactEmail": "centerB@example.com"
}

// DELETE /api/v1/centers/{centerId}
```

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Triển khai phân quyền quản trị trung tâm<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 2.1: [Triển khai phân quyền quản trị trung tâm]
##### Đặc Sỹ Phụ Được Phân Công: Doc
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/CenterManagementGuide.md
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-006], [DAT-003]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Soạn thảo tài liệu hướng dẫn quản lý trung tâm bao gồm quy trình gán người dùng làm Center Admin, quy trình thu hồi quyền; tham chiếu các Tag IDs [REQ-006], [DAT-003]; thêm các đoạn mã API ví dụ.