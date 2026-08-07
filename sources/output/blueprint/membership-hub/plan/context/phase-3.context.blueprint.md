# Giai đoạn 3: Quản lý khóa học

## 📊 Kiểm Soát Tài Liệu

| Mục | Chi Tiết |
| :--- | :--- |
| **ID Bản vẽ** | ARCH-20260807172813 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Quản lý khóa học<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc xây dựng CRUD khóa học, kiểm tra xung đột lịch dạy của giáo viên và phân công giáo viên.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 17:28:13 |
| **Tác giả** | Kiến Trúc Hệ Thống Doanh Nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban Quản Trị Kỹ Thuật |

## 1. Phạm Vi Hoạt Động & Mục Tiêu Của Giai Đoạn
Giai đoạn này tập trung vào việc triển khai CRUD khóa học, kiểm tra xung đột lịch dạy của giáo viên và phân công giáo viên. Các yêu cầu bao gồm xem danh sách khóa học, tạo/cập nhật/xóa khóa học và phân công giáo viên vào khóa học.

## 2. Phạm Vi Kỹ Thuật & Ranh Giới Thư Mục (Tệp, đường dẫn và điểm cuối)
- ./sources/backend/course/ (Coder) – [REQ-007], [REQ-008], [REQ-009], [DAT-004]
- ./sources/docs/ (Doc) – tài liệu quản lý khóa học

## 3. Hướng Dẫn Chức Năng Cụ Thể Cho Các Đặc Sỹ Phụ
*   **Coder**: Hoạt động như một Lập Trình Viên Ứng Dụng Cấp Cao/Chuyên Gia. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và ứng dụng khách frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu hạ tầng.
* **Tester**: Hoạt động như một Trưởng/Chuyên Gia Kiểm Chất/QA. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng kiểm tra chất lượng. Trách nhiệm là tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con nhiệm vụ liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất ra chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà Viết Kỹ Thuật Chuyên Gia và Kiến Trúc Hệ Thống Doanh Nghiệp. Chuyên về biên soạn tài liệu Kỹ Thuật Chi Tiết, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp công nghệ hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác nhận lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng dịch vụ microservices vào các cụm GKE hoạt động.

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)
- Triển khai hoàn chỉnh các dịch vụ CRUD khóa học, kiểm tra xung đột lịch dạy của giáo viên và phân công giáo viên.
- Kiểm tra và xác nhận các yêu cầu chức năng cốt lõi.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Triển khai danh sách khóa học, tạo khóa học mới và kiểm tra xung đột lịch<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 1.1: [Triển khai danh sách khóa học, tạo khóa học mới và kiểm tra xung đột lịch]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/course/CourseService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-007], [REQ-008], [DAT-004]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai CourseService với findAllCourses trả về view bao gồm tên giáo viên; implement createCourse validation đảm bảo startDate <= endDate, kiểm tra xem teacherId đã có khóa học nào trùng lịch (startDate <= existing.endDate AND endDate >= existing.startDate) ném ConflictException; lưu khóa học vào bảng COURSES; trả về response DTO.

* **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004]:**
```sql
CREATE TABLE COURSES (
    courseId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    teacherId UUID NOT NULL REFERENCES USERS(userId),
    maxStudents INT NOT NULL DEFAULT 30
);
```

* **Hợp đồng Định tuyến API và Sự kiện [REQ-007], [REQ-008], [REQ-009]:**
```json
// GET /api/v1/courses
// Response: [{ "courseId": "uuid", "title": "Math 101", "startDate": "2026-09-01", "endDate": "2026-12-31", "teacherName": "Nguyen Van B" }]

// POST /api/v1/courses
{
  "title": "Physics 202",
  "description": "Advanced physics",
  "startDate": "2026-10-01",
  "endDate": "2026-12-31",
  "teacherId": "uuid-of-teacher"
}

// PUT /api/v1/courses/{courseId}/teacher
{
  "teacherId": "uuid-of-new-teacher"
}
```

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Triển khai phân công giáo viên và thông báo cho giáo viên qua ứng dụng di động<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 2.1: [Triển khai phân công giáo viên và thông báo cho giáo viên qua ứng dụng di động]
##### Đặc Sỹ Phụ Được Phân Công: Doc
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/CourseManagementGuide.md
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-009], [DAT-004]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Soạn thảo tài liệu hướng dẫn quản lý khóa học bao gồm quy trình phân công giáo viên, quy trình thu hồi phân công; tham chiếu các Tag IDs [REQ-009], [DAT-004]; thêm các đoạn mã API ví dụ.