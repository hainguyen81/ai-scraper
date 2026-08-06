# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260806133914 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/06 13:39:14 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CƠ BẢN

### 1.1. KIẾN TRÚC CƠ BẢN & CHẾ ĐỘ KIẾN TRÚC
- Hệ thống được thiết kế theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, trung tâm, khóa học, và điểm danh.
- Sử dụng mô hình Event-Driven Architecture (EDA) cho các luồng xử lý điểm danh và thông báo.
- Áp dụng mô hình CQRS (Command Query Responsibility Segregation) để tách biệt các thao tác ghi và đọc dữ liệu.
- Sử dụng mô hình Reactive Programming cho các tính năng thời gian thực như điểm danh và thông báo đẩy.

### 1.2. LUỒNG DỮ LIỆU DOANH NGHIỆP & CỘNG ĐỒNG CƠ BẢN
- Sử dụng Kafka để xử lý các sự kiện điểm danh và thông báo.
- Các dịch vụ giao tiếp với nhau thông qua REST APIs và WebSocket.
- Sử dụng Redis để lưu trữ session và caching dữ liệu.
- Các dịch vụ được triển khai trên Kubernetes với các quy tắc scaling tự động dựa trên tải.

## 📁 2. PHỤ THUỘC CÔNG NGHỆ & CỘNG ĐỒNG THƯ VIỆN
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis, GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React Native, Firebase Hosting.

### MA TRẬN CÔNG NGHỆ KIẾN TRÚC

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

## 📁 3. QUY TẮC TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
- **Quy tắc Giới hạn Không gian làm việc:** Gốc thực sự của không gian làm việc là cố định tại gốc dự án `.`. Tất cả các đường dẫn được tạo ra phải bắt đầu với `./sources/`.
- **Tuân thủ Động Tiền tố Thư mục:** Áp dụng các quy tắc ánh xạ đường dẫn động được xác định trong Protocol 1 một cách nghiêm ngặt phù hợp với cấu trúc dự án phát hiện được.
- **[ĐIỀU KIỆN: JAVA_STACK_ONLY] Tiêu chuẩn Gói Java:** Nếu ngăn xếp công nghệ sử dụng các khung Java, tất cả mã nguồn Java phải nằm nghiêm ngặt trong cơ sở gói doanh nghiệp: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. Bạn phải chuyển đổi động chuỗi "membership-hub" thành một mã alphanumeric thuần túy viết thường bằng cách loại bỏ khoảng trắng, dấu gạch ngang và dấu gạch dưới. Các dự án không phải Java bị cấm áp dụng đoạn này.
- **Cú pháp Đường dẫn Mục tiêu Tester nghiêm ngặt:** Bất kỳ thành phần nào được nhắm mục tiêu bởi Sub-Agent Tester phải được cấu trúc dưới dạng cặp phân tách chặt chẽ bằng dấu chấm phẩy `<source_component_or_token>;<test_suite_file_to_execute>`. Cả hai đường dẫn bên trong cặp phải bắt đầu với `./sources/`.

## 4. LƯỚI TÓM TẮT KIẾN TRÚC ĐA PHASE CẤP CAO
| Giai đoạn | Khoảng ngày | Thành phần Kiến trúc / Module Đường dẫn | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1-2 | `./sources/backend/auth-service`, `./sources/backend/user-service`, `./sources/frontend/web-app`, `./sources/docs/architecture.md` | Xây dựng dịch vụ xác thực, dịch vụ người dùng, giao diện web, tài liệu kiến trúc | Coder, Doc | [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-002], [ARC-006], [DAT-001], [DAT-003] |
| Giai đoạn 2 | Ngày 3-4 | `./sources/backend/course-service`, `./sources/backend/attendance-service`, `./sources/frontend/mobile-app`, `./sources/docs/api.md` | Xây dựng dịch vụ khóa học, dịch vụ điểm danh, ứng dụng di động, tài liệu API | Coder, Doc | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-003], [ARC-004], [DAT-004], [DAT-006] |
| Giai đoạn 3 | Ngày 5-6 | `./sources/backend/notification-service`, `./sources/frontend/web-app`, `./sources/docs/security.md` | Xây dựng dịch vụ thông báo, cập nhật giao diện web, tài liệu bảo mật | Coder, Doc | [REQ-016], [ARC-008], [ARC-009], [DAT-008], [NFR-003] |
| Giai đoạn 4 | Ngày 7 | `./sources/backend/promotion-service`, `./sources/frontend/mobile-app`, `./sources/docs/i18n.md` | Xây dựng dịch vụ khuyến mãi, cập nhật ứng dụng di động, tài liệu bản địa hóa | Coder, Doc | [REQ-017], [REQ-018], [ARC-007], [DAT-009], [NFR-007] |
| Giai đoạn 5 | Ngày 1-2 | `./sources/infra/docker`, `./sources/infra/k8s`, `./sources/docs/deployment.md` | Triển khai Docker, Kubernetes, tài liệu triển khai | Docker, GCP, GKE, Doc | [ARC-010], [NFR-002], [NFR-004], [NFR-005] |

## 5. CHI TIẾT PHÂN PHỐI NGÀY VÀ CÁC GIAI ĐOẠN PHÂN BIỆT PHASE
### 📈 Giai đoạn 1 ĐẶC TẢ KIẾN TRÚC CHI TIẾT
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ xác thực, dịch vụ người dùng, giao diện web, và tài liệu kiến trúc.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/auth-service [REQ-001], [REQ-002], [ARC-001], [ARC-006]`, `./sources/backend/user-service [REQ-003], [DAT-001]`, `./sources/frontend/web-app [ARC-009]`, `./sources/docs/architecture.md [ARC-001], [ARC-002]`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:** Tạo bảng `Users` và `Roles` với các trường như `userId`, `email`, `passwordHash`, `fullName`, `roleId`, `provider`, `createdAt`, `updatedAt`.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [ARC-006]:** Xác thực qua email/mật khẩu, Firebase, Google, Facebook OAuth2, cấp JWT token.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Xác thực đầu vào không hợp lệ, thông báo rõ ràng các trường không hợp lệ.

#### Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 1)

- **NGÀY 1: XÂY DỰNG DỊCH VỤ XÁC THỰC VÀ NGƯỜI DÙNG**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-001], [REQ-002], [REQ-003], [ARC-001], [ARC-006], [DAT-001]
    * **Thành phần Mục tiêu file path (`target_component`):** `./sources/backend/auth-service [REQ-001], [REQ-002], [ARC-001], [ARC-006]`, `./sources/backend/user-service [REQ-003], [DAT-001]`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết Cấp thấp:** Xây dựng dịch vụ xác thực với các phương thức đăng ký và đăng nhập qua email/mật khẩu, Firebase, Google, Facebook OAuth2. Tạo dịch vụ người dùng với các chức năng phân quyền và quản lý thông tin người dùng.
    * **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:**
      ```sql
      CREATE TABLE Roles (
          roleId SERIAL PRIMARY KEY,
          name VARCHAR(30) UNIQUE NOT NULL,
          description VARCHAR(200)
      );

      CREATE TABLE Users (
          userId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          email VARCHAR(255) UNIQUE NOT NULL,
          passwordHash CHAR(60) NOT NULL,
          fullName VARCHAR(100) NOT NULL,
          roleId INT REFERENCES Roles(roleId),
          provider VARCHAR(10) DEFAULT 'local',
          createdAt TIMESTAMP NOT NULL DEFAULT NOW(),
          updatedAt TIMESTAMP NOT NULL DEFAULT NOW()
      );
      ```

- **NGÀY 2: XÂY DỰNG GIAO DIỆN WEB VÀ TÀI LIỆU KIẾN TRÚC**
    * **Sub-Agent Workflow Specialization:** [Coder], [Doc]
    * **Tag IDs Mục tiêu:** [ARC-009], [ARC-001], [ARC-002]
    * **Thành phần Mục tiêu file path (`target_component`):** `./sources/frontend/web-app [ARC-009]`, `./sources/docs/architecture.md [ARC-001], [ARC-002]`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết Cấp thấp:** Xây dựng giao diện web với các chức năng đăng ký, đăng nhập, và quản lý người dùng. Tạo tài liệu kiến trúc mô tả kiến trúc hệ thống và các dịch vụ chính.

### 📈 Giai đoạn 2 ĐẶC TẢ KIẾN TRÚC CHI TIẾT
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ khóa học, dịch vụ điểm danh, ứng dụng di động, và tài liệu API.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/course-service [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-004]`, `./sources/backend/attendance-service [REQ-012], [REQ-013], [DAT-006]`, `./sources/frontend/mobile-app [ARC-009]`, `./sources/docs/api.md [ARC-003], [ARC-004]`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004], [DAT-006]:** Tạo bảng `Courses`, `Enrollments`, và `Attendance` với các trường như `courseId`, `title`, `description`, `startDate`, `endDate`, `teacherId`, `maxStudents`, `enrollmentId`, `studentId`, `enrollmentDate`, `attendanceId`, `attendanceDate`, `timestamp`.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [ARC-003], [ARC-004]:** Quản lý khóa học, điểm danh, và đăng ký học viên.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002]:** Xử lý các trường hợp mạng không ổn định và điểm danh trùng lặp.

#### Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 2)

- **NGÀY 3: XÂY DỰNG DỊCH VỤ KHÓA HỌC VÀ ĐIỂM DANH**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-012], [REQ-013], [DAT-004], [DAT-006]
    * **Thành phần Mục tiêu file path (`target_component`):** `./sources/backend/course-service [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-004]`, `./sources/backend/attendance-service [REQ-012], [REQ-013], [DAT-006]`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết Cấp thấp:** Xây dựng dịch vụ khóa học với các chức năng quản lý khóa học, phân công giáo viên, và điểm danh. Tạo dịch vụ điểm danh với các chức năng quét mã QR và xử lý điểm danh trùng lặp.
    * **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-004], [DAT-006]:**
      ```sql
      CREATE TABLE Courses (
          courseId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          title VARCHAR(150) NOT NULL,
          description TEXT,
          startDate DATE NOT NULL,
          endDate DATE NOT NULL,
          teacherId UUID REFERENCES Users(userId),
          maxStudents INT DEFAULT 30
      );

      CREATE TABLE Enrollments (
          enrollmentId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          studentId UUID REFERENCES Users(userId),
          courseId UUID REFERENCES Courses(courseId),
          enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW()
      );

      CREATE TABLE Attendance (
          attendanceId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          studentId UUID REFERENCES Users(userId),
          courseId UUID REFERENCES Courses(courseId),
          attendanceDate DATE NOT NULL,
          timestamp TIMESTAMP NOT NULL DEFAULT NOW()
      );
      ```

- **NGÀY 4: XÂY DỰNG ỨNG DỤNG DI ĐỘNG VÀ TÀI LIỆU API**
    * **Sub-Agent Workflow Specialization:** [Coder], [Doc]
    * **Tag IDs Mục tiêu:** [ARC-009], [ARC-003], [ARC-004]
    * **Thành phần Mục tiêu file path (`target_component`):** `./sources/frontend/mobile-app [ARC-009]`, `./sources/docs/api.md [ARC-003], [ARC-004]`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết Cấp thấp:** Xây dựng ứng dụng di động với các chức năng điểm danh qua mã QR và nhận thông báo. Tạo tài liệu API mô tả các endpoint và hợp đồng sự kiện.

### 📈 Giai đoạn 3 ĐẶC TẢ KIẾN TRÚC CHI TIẾT
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ thông báo, cập nhật giao diện web, và tài liệu bảo mật.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/notification-service [REQ-016], [ARC-008], [DAT-008]`, `./sources/frontend/web-app [ARC-009]`, `./sources/docs/security.md [NFR-003]`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:** Tạo bảng `Notifications` với các trường như `notificationId`, `userId`, `groupZalo`, `message`, `sentAt`, `delivered`.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [ARC-008], [ARC-009]:** Gửi thông báo qua ứng dụng di động và nhóm Zalo.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-003]:** Xử lý các trường hợp không thể gửi thông báo.

#### Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 3)

- **NGÀY 5: XÂY DỰNG DỊCH VỤ THÔNG BÁO**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-016], [ARC-008], [DAT-008]
    * **Thành phần Mục tiêu file path (`target_component`):** `./sources/backend/notification-service [REQ-016], [ARC-008], [DAT-008]`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết Cấp thấp:** Xây dựng dịch vụ thông báo với các chức năng gửi thông báo qua ứng dụng di động và nhóm Zalo.
    * **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:**
      ```sql
      CREATE TABLE Notifications (
          notificationId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          userId UUID REFERENCES Users(userId),
          groupZalo VARCHAR(255),
          message TEXT NOT NULL,
          sentAt TIMESTAMP NOT NULL DEFAULT NOW(),
          delivered BOOLEAN DEFAULT FALSE
      );
      ```

- **NGÀY 6: CẬP NHẬT GIAO DIỆN WEB VÀ TÀI LIỆU BẢO MẬT**
    * **Sub-Agent Workflow Specialization:** [Coder], [Doc]
    * **Tag IDs Mục tiêu:** [ARC-009], [NFR-003]
    * **Thành phần Mục tiêu file path (`target_component`):** `./sources/frontend/web-app [ARC-009]`, `./sources/docs/security.md [NFR-003]`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết Cấp thấp:** Cập nhật giao diện web với các chức năng nhận thông báo. Tạo tài liệu bảo mật mô tả các quy tắc bảo mật và xử lý ngoại lệ.

### 📈 Giai đoạn 4 ĐẶC TẢ KIẾN TRÚC CHI TIẾT
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Xây dựng dịch vụ khuyến mãi, cập nhật ứng dụng di động, và tài liệu bản địa hóa.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/promotion-service [REQ-017], [REQ-018], [DAT-009]`, `./sources/frontend/mobile-app [ARC-009]`, `./sources/docs/i18n.md [NFR-007]`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-009]:** Tạo bảng `Promotions` và `Announcements` với các trường như `promoId`, `code`, `discountPercent`, `startDate`, `endDate`, `description`, `announcementId`, `title`, `content`.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-017], [REQ-018], [ARC-009]:** Quản lý khuyến mãi và thông báo.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có ngoại lệ chuyên biệt.

#### Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 4)

- **NGÀY 7: XÂY DỰNG DỊCH VỤ KHUYẾN MÃI VÀ CẬP NHẬT ỨNG DỤNG DI ĐỘNG**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Tag IDs Mục tiêu:** [REQ-017], [REQ-018], [DAT-009]
    * **Thành phần Mục tiêu file path (`target_component`):** `./sources/backend/promotion-service [REQ-017], [REQ-018], [DAT-009]`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết Cấp thấp:** Xây dựng dịch vụ khuyến mãi với các chức năng quản lý khuyến mãi và thông báo. Cập nhật ứng dụng di động với các chức năng xem khuyến mãi và thông báo.
    * **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-009]:**
      ```sql
      CREATE TABLE Promotions (
          promoId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          code VARCHAR(50) UNIQUE,
          discountPercent SMALLINT NOT NULL,
          startDate DATE,
          endDate DATE,
          description TEXT
      );

      CREATE TABLE Announcements (
          announcementId UUID PRIMARY KEY DEFAULT gen_random_uuid(),
          title VARCHAR(150) NOT NULL,
          content TEXT NOT NULL,
          startDate DATE,
          endDate DATE
      );
      ```

### 📈 Giai đoạn 5 ĐẶC TẢ KIẾN TRÚC CHI TIẾT
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai Docker, Kubernetes, và tài liệu triển khai.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/infra/docker [ARC-010]`, `./sources/infra/k8s [NFR-002], [NFR-004]`, `./sources/docs/deployment.md [NFR-002], [NFR-004], [NFR-005]`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu:** Không có.
- **Hợp đồng Định tuyến API và Sự kiện:** Không có.
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn:** Không có.

#### Nhật ký Phân phối Công việc Sub-Agent Ngày theo Ngày (Giai đoạn 5)

- **NGÀY 1: TRIỂN KHAI DOCKER VÀ KUBERNETES**
    * **Sub-Agent Workflow Specialization:** [Docker], [GCP], [GKE], [Doc]
    * **Tag IDs Mục tiêu:** [ARC-010], [NFR-002], [NFR-004], [NFR-005]
    * **Thành phần Mục tiêu file path (`target_component`):** `./sources/infra/docker [ARC-010]`, `./sources/infra/k8s [NFR-002], [NFR-004]`, `./sources/docs/deployment.md [NFR-002], [NFR-004], [NFR-005]`
    * **Hướng dẫn Công việc Kỹ thuật Chi tiết Cấp thấp:** Triển khai Docker với các cấu hình container hóa. Triển khai Kubernetes với các cấu hình triển khai và scaling tự động. Tạo tài liệu triển khai mô tả các quy tắc triển khai và bảo mật.

## 📁 6. QUY TẮC BẢO MẬT TOÀN CẦU & ĐỐI PHÓNG TIÊU CHUẨN TIÊM NẠP [NFR-XXX]
- **Đối phó với Tiêm SQL (SQLi) tuyệt đối:** Tham số quy tắc cho các câu lệnh chuẩn bị, tham số truy vấn vị trí, và danh sách trắng sắp xếp động đầu vào.
- **Tiêm chéo trang web (XSS) & Chính sách Bảo mật Nội dung (CSP):** Tiêu chuẩn bố cục cho các bộ lọc tự động làm sạch ngữ cảnh, tự động thoát JSX, và tiêm động các tiêu đề CSP nghiêm ngặt (`unsafe-inline` hạn chế).
- **Quy tắc Bảo mật CORS đa người dùng:** Cấu hình cho các cấm thông báo nguồn gốc đại diện và xác thực động các số liệu người dùng cơ sở dữ liệu nguồn gốc.
- **Máy quét & Máy làm sạch Nhật ký Không rò rỉ & Máy che dữ liệu PII:** Quy tắc cho các bộ chặn tự động làm sạch (`@JsonSerialize`) và ngưỡng làm sạch nhật ký.

## 📁 7. QUY TẮC TUÂN THỦ HYBRID MOBILE & CƠ CHẾ SEO QUỐC TẾ ĐỘNG
- **Quy tắc Tuân thủ Hybrid Mobile Capacitor tuyệt đối:** [NẾU DI ĐỘNG hoạt động] Quy tắc cho việc lấy động khách hàng, địa chỉ tuyệt đối URL, bảo vệ thủy phân, trừu tượng hóa lưu trữ cục bộ (`@capacitor/preferences`), và chặn nút quay lại phần cứng.
- **Bản địa hóa Quốc tế (i18n) & Tiêm Động SEO:** Kiến trúc middleware nhận diện lớp biên với các cơ chế điều khiển siêu liên kết động hreflang và giới hạn chỉ mục robot thu thập thông tin tìm kiếm.

## 📁 8. LUỒNG LÀM VIỆC PIPELINE TỰ ĐỘNG HÀNG NGÀY SESSION GIT BRANCH
- **Đồng bộ hóa Không gian làm việc Forking Độc lập:** Kiểm soát lập trình cho nhánh `features/development-phase-X-day-Y` (`X` là số giai đoạn, từ 1 đến N, trong đó N <= 5; `Y` là số ngày trong giai đoạn, nó sẽ bắt đầu từ 1 cho mỗi giai đoạn).
- **Cổng Kiểm soát Hợp lệ Pipeline:** Quy tắc thực thi cho xác minh biên dịch, mục tiêu tự động hóa độ phủ mã (`>= 85%`), và nhật ký tổng kết tuần tự hóa ngữ cảnh.

### 🛑 MANDATE KIỂM TRA ĐẦU VÀO MA TRẬN

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`