# Giai đoạn 4: Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo

## 📊 Kiểm Soát Tài Liệu

| Mục | Chi Tiết |
| :--- | :--- |
| **ID Bản vẽ** | ARCH-20260807172813 |
| **Tên Dự Án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Ghi danh, điểm danh, thẻ, thông báo, khuyến mãi, chatbot, di động, i18n, SEO, báo cáo<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo đa kênh, khuyến mãi, chatbot AI, giao diện người dùng di động, bản địa hóa & SEO, và báo cáo & phân tích.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 17:28:13 |
| **Tác giả** | Kiến Trúc Hệ Thống Doanh Nghiệp (SA Agent) |
| **Phê duyệt** | Đang chờ xem xét của Ban Quản Trị Kỹ Thuật |

## 1. Phạm Vi Hoạt Động & Mục Tiêu Của Giai Đoạn
Giai đoạn này tập trung vào việc triển khai ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo đa kênh, khuyến mãi, chatbot AI, giao diện người dùng di động, bản địa hóa & SEO, và báo cáo & phân tích. Các yêu cầu bao gồm ghi danh học viên, điểm danh QR, hiển thị thẻ hội viên, gửi thông báo đa kênh, quản lý khuyến mãi, tích hợp chatbot AI, giao diện người dùng di động, bản địa hóa & SEO, và báo cáo & phân tích.

## 2. Phạm Vi Kỹ Thuật & Ranh Giới Thư Mục (Tệp, đường dẫn và điểm cuối)
- ./sources/backend/enrollment/ (Coder) – [REQ-010], [REQ-011], [DAT-005]
- ./sources/backend/attendance/ (Coder) – [REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]
- ./sources/backend/membership/ (Coder) – [REQ-014], [REQ-015], [DAT-007]
- ./sources/backend/notification/ (Coder) – [REQ-016], [DAT-008], [EXC-003]
- ./sources/backend/promotion/ (Coder) – [REQ-017], [REQ-018], [DAT-009]
- ./sources/backend/chatbot/ (Coder) – [REQ-019]
- ./sources/frontend/app/ (Coder) – [REQ-020], [REQ-021]
- ./sources/backend/i18n/ (Coder) – [REQ-022], [REQ-023], [DAT-011]
- ./sources/backend/reporting/ (Coder) – [REQ-024], [REQ-025], [EXC-005]
- ./sources/docs/ (Doc) – tài liệu tổng quan về tất cả các module

## 3. Hướng Dẫn Chức Năng Cụ Thể Cho Các Đặc Sỹ Phụ
*   **Coder**: Hoạt động như một Lập Trình Viên Ứng Dụng Cấp Cao/Chuyên Gia. Trách nhiệm là triển khai mã nguồn ứng dụng thuần túy trên cả các dịch vụ backend và ứng dụng khách frontend/mobile. Cấm viết bộ kiểm thử hoặc biểu mẫu hạ tầng.
* **Tester**: Hoạt động như một Trưởng/Chuyên Gia Kiểm Chất/QA. Chuyên về kỹ thuật bộ kiểm thử, xác nhận và cổng kiểm tra chất lượng. Trách nhiệm là tạo các bộ kiểm thử JUnit, kiểm thử tích hợp, tự động hóa kiểm thử cuối cùng và kịch bản xác nhận hiệu suất. Cấm sửa đổi mã sản xuất ứng dụng. Nếu mục tiêu con nhiệm vụ liên quan đến phạm vi tích hợp hoặc cuối cùng nơi không có tệp mã nguồn cụ thể nào có thể bị ràng buộc, bạn PHẢI xuất ra chính xác mã thông báo `INTEGRATION_SCOPE` làm tham số đầu tiên của cặp chấm phẩy (ví dụ: `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Chức năng như một Nhà Viết Kỹ Thuật Chuyên Gia và Kiến Trúc Hệ Thống Doanh Nghiệp. Chuyên về biên soạn tài liệu Kỹ Thuật Chi Tiết, tham chiếu lược đồ, bản thiết kế hệ thống và danh mục kiến trúc doanh nghiệp phù hợp với các lớp công nghệ hoạt động. Mỗi tệp tài liệu kỹ thuật được tạo ra PHẢI được liệt kê như một thực thể đường dẫn tệp cụ thể kết thúc bằng phần mở rộng `.md` và nằm nghiêm ngặt trong bố cục lưu trữ trung tâm: `./sources/docs/`.
*   **Reviewer**: Trách nhiệm về xác nhận biên dịch, phân tích tĩnh, và vá lỗi phòng thủ. Chuyên về kiểm tra chất lượng mã, giải quyết lỗi biên dịch, khắc phục lỗ hổng bảo mật OWASP và giải quyết các chặn cổng chất lượng SonarQube.
*   **Docker**: Chuyên về container hóa, kỹ thuật Dockerfile đa giai đoạn, tối ưu hóa gói và đẩy các tài sản hình ảnh ứng dụng đã xác nhận lên DockerHub.
*   **GCP**: Chuyên về tự động hóa đám mây trong Google Cloud Platform. Trách nhiệm là xây dựng và đẩy hình ảnh lên Google Cloud Artifact Registry (GCR), và điều phối môi trường container tự nhiên trên Google Cloud Run.
*   **GKE**: Chuyên về điều phối container sản xuất bên trong Google Kubernetes Engine. Trách nhiệm là xây dựng biểu mẫu triển khai Kubernetes, điều khiển định tuyến, cấu hình HPA, biểu đồ Helm và triển khai các tải trọng dịch vụ microservices vào các cụm GKE hoạt động.

## 4. Định Nghĩa Hoàn Thành Giai Đoạn (DoD)
- Triển khai hoàn chỉnh ghi danh học viên, điểm danh QR, thẻ hội viên, thông báo đa kênh, khuyến mãi, chatbot AI, giao diện người dùng di động, bản địa hóa & SEO, và báo cáo & phân tích.
- Kiểm tra và xác nhận các yêu cầu chức năng cốt lõi.
- Đảm bảo tuân thủ các tiêu chuẩn bảo mật OWASP.
- Hoàn thành 100% ánh xạ Tag ID.

## 5. NHẬT KÝ THỰC HIỆN KIẾN TRÚC THEO NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->Triển khai ghi danh học viên, tự động tạo tài khoản học viên nếu thiếu<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 1.1: [Triển khai ghi danh học viên, tự động tạo tài khoản học viên nếu thiếu]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/enrollment/EnrollmentService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-010], [REQ-011], [DAT-005]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai EnrollmentService.createEnrollment(studentId, courseId) kiểm tra xem học viên đã ghi danh chưa, nếu chưa thì tạo bản ghi ENROLLMENTS; nếu học viên chưa có tài khoản USERS, tạo tài khoản mới với roleId = Student; sau khi ghi danh thành công, tạo bản ghi NOTIFICATIONS với message “Bạn đã ghi danh thành công vào khóa học {courseId}”; gọi async push notification qua FCM/APNs; lưu audit log.

* **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-005]:**
```sql
CREATE TABLE ENROLLMENTS (
    enrollmentId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    enrollmentDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

* **Hợp đồng Định tuyến API và Sự kiện [REQ-010], [REQ-011]:**
```json
// POST /api/v1/enrollments
{
  "studentId": "uuid",
  "courseId": "uuid"
}
```

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->Triển khai ghi nhận điểm danh QR với logic bất biến<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 2.1: [Triển khai ghi nhận điểm danh QR với logic bất biến]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/attendance/AttendanceService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-012], [REQ-013], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai AttendanceService.recordAttendance(studentId, courseId, qrData) xác thực studentId có ghi danh vào courseId, kiểm tra xem đã có ATTENDANCE cho attendanceDate hôm nay chưa; nếu đã có, trả về duplicate flag true; nếu chưa, tạo bản ghi ATTENDANCE mới; xử lý trường hợp ngoại tuyến bằng cách lưu sự kiện tạm thời vào hàng đợi (Redis) và xử lý khi kết nối lại; ném AttendanceServiceException cho các lỗi validation.

* **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006]:**
```sql
CREATE TABLE ATTENDANCE (
    attendanceId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    courseId UUID NOT NULL REFERENCES COURSES(courseId),
    attendanceDate DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

* **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013]:**
```json
// POST /api/v1/attendance/scan
{
  "studentId": "uuid",
  "courseId": "uuid",
  "qrCodeData": "base64-encoded-qr"
}
```

### 🌤️ NGÀY 3: <!--DAY_HEADER_START-->Triển khai hiển thị thẻ hội viên và chức năng gia hạn<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 3.1: [Triển khai hiển thị thẻ hội viên và chức năng gia hạn]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/membership/MembershipService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-014], [REQ-015], [DAT-007]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai MembershipService.getCard(studentId) truy vấn STUDENTCARDS, tính remainingDays = validityDays - ngày đã sử dụng; trả về DTO; implement extendCard(studentId, additionalDays) cập nhật trường remainingDays, ghi log giao dịch; tích hợp payment gateway để xử lý phí gia hạn; gửi notification cho học viên.

* **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-007]:**
```sql
CREATE TABLE STUDENTCARDS (
    cardId UUID PRIMARY KEY,
    studentId UUID NOT NULL REFERENCES USERS(userId),
    issueDate DATE NOT NULL,
    validityDays INT NOT NULL,
    remainingDays INT NOT NULL
);
```

* **Hợp đồng Định tuyến API và Sự kiện [REQ-014], [REQ-015]:**
```json
// GET /api/v1/membership/{studentId}/card
// Response: { "validityDays": 30, "remainingDays": 12 }
```

### 🌤️ NGÀY 4: <!--DAY_HEADER_START-->Triển khai dịch vụ thông báo đa kênh và xử lý lỗi giao hàng<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 4.1: [Triển khai dịch vụ thông báo đa kênh và xử lý lỗi giao hàng]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/notification/NotificationService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-016], [DAT-008], [EXC-003]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai NotificationService.sendNotification(userId, groupZalo, message) lưu vào bảng NOTIFICATIONS, gọi FCM push cho userId, gọi Zalo API để đăng bài vào groupZalo; nếu gửi thất bại, ghi log lỗi, lên lịch retry tối đa 3 lần; sau khi retry thất bại, đánh dấu delivered = false và gửi email cảnh báo quản trị.

* **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:**
```sql
CREATE TABLE NOTIFICATIONS (
    notificationId UUID PRIMARY KEY,
    userId UUID REFERENCES USERS(userId),
    groupZalo VARCHAR(100),
    message TEXT NOT NULL,
    sentAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
```

* **Hợp đồng Định tuyến API và Sự kiện [REQ-016]:**
```json
// POST /api/v1/notifications
{
  "userId": "uuid",
  "message": "Your attendance recorded"
}
```

### 🌤️ NGÀY 5: <!--DAY_HEADER_START-->Triển khai CRUD khuyến mãi và thông báo với logic tự động hết hạn<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 5.1: [Triển khai CRUD khuyến mãi và thông báo với logic tự động hết hạn]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/promotion/PromotionService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-017], [REQ-018], [DAT-009]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai PromotionService.createPromotion(payload) lưu vào bảng PROMOTIONS/ANNOUNCEMENTS; thêm validation startDate/endDate; thiết lập scheduler xóa các bản ghi đã hết hạn; implement soft-delete cho khuyến mãi; expose endpoint GET /promotions để hiển thị cho học viên.

* **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-009]:**
```sql
CREATE TABLE PROMOTIONS (
    promoId UUID PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    discountPercent SMALLINT NOT NULL,
    startDate DATE,
    endDate DATE,
    description TEXT
);

CREATE TABLE ANNOUNCEMENTS (
    announcementId UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    content TEXT NOT NULL,
    startDate DATE,
    endDate DATE
);
```

* **Hợp đồng Định tuyến API và Sự kiện [REQ-017], [REQ-018]:**
```json
// POST /api/v1/promotions
{
  "code": "SAVE20",
  "discountPercent": 20,
  "startDate": "2026-09-01",
  "endDate": "2026-12-31",
  "description": "Giảm giá 20% cho tất cả khóa học"
}

// POST /api/v1/announcements
{
  "title": "Holiday Notice",
  "content": "Hệ thống đóng cửa vào ngày 2/9",
  "startDate": "2026-08-31",
  "endDate": "2026-09-02"
}
```

### 🌤️ NGÀY 6: <!--DAY_HEADER_START-->Triển khai tích hợp chatbot AI và tài liệu hướng dẫn vận hành<!--DAY_HEADER_END-->

#### 📝 NHIỆM VỤ CON 6.1: [Triển khai tích hợp chatbot AI]
##### Đặc Sỹ Phụ Được Phân Công: Coder
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/backend/chatbot/ChatbotService.java
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Triển khai ChatbotService xử lý các truy vấn từ người dùng, trả lời các câu hỏi phổ biến về khóa học, giáo viên, trung tâm và trạng thái tài khoản.

#### 📝 NHIỆM VỤ CON 6.2: [Tạo tài liệu hướng dẫn vận hành]
##### Đặc Sỹ Phụ Được Phân Công: Doc
##### Thành Phần Mục Tiêu & Yêu Cầu Kỹ Thuật:
* **Đường dẫn mục tiêu:** ./sources/docs/ChatbotIntegrationGuide.md
* **Mã Thẻ Theo Dõi:** <!--START_TAGS-->[REQ-019]<!--END_TAGS-->
* **Hướng Dẫn Kỹ Thuật Chi Tiết:** Soạn thảo tài liệu hướng dẫn tích hợp chatbot AI bao gồm các endpoint, cách thức xử lý hội thoại, quy tắc escalation, tham chiếu các Tag IDs [REQ-019]; thêm các đoạn mã ví dụ bằng tiếng Việt.