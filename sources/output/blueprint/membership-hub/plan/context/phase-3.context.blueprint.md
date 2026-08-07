# Giai đoạn 3: <!--PHASE_NAME_START-->Xây dựng quản lý khóa học, ghi danh, điểm danh QR và thẻ hội viên<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260807134137 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 3 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Xây dựng quản lý khóa học, ghi danh, điểm danh QR và thẻ hội viên<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 3 tập trung vào xây dựng toàn bộ mô hình dữ liệu và API cho quản lý khóa học, ghi danh học viên, điểm danh qua QR, và quản lý thẻ hội viên. Bao gồm triển khai các bảng dữ liệu courses, enrollments, attendance, member_cards, phát triển các controller, service, DTO, và các endpoint tương ứng, đồng thời triển khai exception handlers cho mất kết nối mạng và trùng lặp điểm danh. Ngoài ra, chuẩn bị tài liệu kiến trúc chi tiết cho giai đoạn này.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 13:41:37 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## Phạm vi thực thi và mục tiêu

Giai đoạn 3 thực hiện xây dựng toàn bộ mô hình dữ liệu và API cho quản lý khóa học, ghi danh học viên, điểm danh qua QR, và quản lý thẻ hội viên. Các thành phần chính bao gồm lớp thực thể CourseEntity, EnrollmentEntity, AttendanceEntity, MemberCardEntity, các controller, service, DTO, và các endpoint tương ứng. Ngoài ra, triển khai exception handlers cho mất kết nối mạng và trùng lặp điểm danh, đồng thời chuẩn bị tài liệu kiến trúc chi tiết cho giai đoạn này.

## Phạm vi kỹ thuật và ranh giới thư mục

| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseEntity.java` | Lớp thực thể khóa học |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/EnrollmentEntity.java` | Lớp thực thể ghi danh |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/AttendanceEntity.java` | Lớp thực thể điểm danh |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/MemberCardEntity.java` | Lớp thực thể thẻ hội viên |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseController.java` | Controller khóa học |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/EnrollmentController.java` | Controller ghi danh |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/AttendanceController.java` | Controller điểm danh |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/MemberCardController.java` | Controller thẻ hội viên |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseService.java` | Service khóa học |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/EnrollmentService.java` | Service ghi danh |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/AttendanceService.java` | Service điểm danh |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/MemberCardService.java` | Service thẻ hội viên |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseDTO.java` | DTO khóa học |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/EnrollmentDTO.java` | DTO ghi danh |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/AttendanceDTO.java` | DTO điểm danh |
| `./sources/backend/org/nlh4j/saas/membershiphub/course-management/MemberCardDTO.java` | DTO thẻ hội viên |
| `./sources/docs/Phase3_Architecture.md` | Tài liệu kiến trúc giai đoạn 3 |
| `./sources/backend/tests/integration/AttendanceIntegrationTest.java` | Kiểm thử tích hợp AttendanceService |

## Chỉ đạo chức năng của các tác nhân phụ

- **Coder**: Phát triển mã nguồn Java cho backend, bao gồm các lớp thực thể, controller, service, repository, và DTO. Không viết bộ kiểm thử hoặc cấu hình hạ tầng.
- **Tester**: Viết bộ kiểm thử JUnit5 và kiểm thử tích hợp cho các thành phần backend. Không sửa mã nguồn.
- **Doc**: Soạn thảo tài liệu kỹ thuật chi tiết, bao gồm mô hình dữ liệu, luồng API, exception handlers, và các thành phần quan trọng. Đảm bảo tài liệu đáp ứng chuẩn OWASP, bảo mật, và ghi chú các ràng buộc dữ liệu. Đưa ra sơ đồ kiến trúc, bảng dữ liệu, và mô tả chi tiết các endpoint.
- **Reviewer**: Kiểm tra mã nguồn, thực hiện phân tích tĩnh, và bảo mật OWASP. Đảm bảo tuân thủ các tiêu chuẩn bảo mật.
- **Docker**: Xây dựng Dockerfile đa giai đoạn cho dịch vụ backend. Tối ưu kích thước và chuẩn bị cho CI/CD.
- **GCP**: Xây dựng và đẩy image lên Google Cloud Artifact Registry. Orchestrate container environments.
- **GKE**: Xây dựng manifest Kubernetes, HPA, và triển khai microservices lên GKE.

## Định nghĩa của Giai đoạn đã hoàn thành

- Tất cả các yêu cầu [REQ-007], [REQ-010], [REQ-012] được triển khai đầy đủ.
- Các bảng dữ liệu courses, enrollments, attendance, member_cards được tạo và kiểm tra tính toàn vẹn.
- API endpoints `/api/v1/courses`, `/api/v1/enrollments`, `/api/v1/attendance/scan`, `/api/v1/membercards/{studentId}` đáp ứng đúng định dạng JSON và bảo mật JWT.
- Kiểm thử tích hợp AttendanceService đạt độ phủ ≥ 85% và kiểm tra exception handlers cho mạng offline và duplicate.
- Đảm bảo tuân thủ OWASP Top 10, bảo mật JWT, và bảo vệ dữ liệu nhạy cảm.
- Tất cả tag ID được ánh xạ đầy đủ, không có tag chưa được sử dụng.

## LỊCH THỰC HIỆN KIẾN TRÚC NGÀY BỞI NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->TRIỂN KHAI LỚP THỰC THỂ KHÓA HỌC, GHI DANH VÀ ĐIỂM DANH<!--DAY_HEADER_END-->

#### 📝 TRIỂN KHAI LỚP THỰC THỂ KHÓA HỌC, GHI DANH VÀ ĐIỂM DANH 1.1:
Triển khai lớp thực thể CourseEntity, EnrollmentEntity, AttendanceEntity, MemberCardEntity, các controller, service, DTO, và các endpoint tương ứng. Đảm bảo các ràng buộc dữ liệu, kiểm tra đầu vào, bảo mật JWT, và tuân thủ OWASP. Xây dựng exception handlers cho mất kết nối mạng và trùng lặp điểm danh.
##### Tác nhân phụ được giao: Coder
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseEntity.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/EnrollmentEntity.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/AttendanceEntity.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/MemberCardEntity.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseController.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/EnrollmentController.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/AttendanceController.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/MemberCardController.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseService.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/EnrollmentService.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/AttendanceService.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/MemberCardService.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/CourseDTO.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/EnrollmentDTO.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/AttendanceDTO.java`, `./sources/backend/org/nlh4j/saas/membershiphub/course-management/MemberCardDTO.java`
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-010], [DAT-004], [DAT-005], [DAT-006]<!--END_TAGS-->
* **Hướng dẫn công việc chi tiết:**  
  1. **Lớp thực thể**  
     - Tạo `CourseEntity.java` với các trường `courseId`, `title`, `description`, `startDate`, `endDate`, `teacherId`, `maxStudents`. Thêm ràng buộc `@NotNull`, `@Size`, `@PastOrPresent`, `@FutureOrPresent`, `@Min`, `@Max`. Định nghĩa quan hệ `@ManyToOne` tới `UserEntity` (giảng viên). Thêm `@UniqueConstraint` cho `title` nếu cần.  
     - Tạo `EnrollmentEntity.java` với các trường `enrollmentId`, `studentId`, `courseId`, `enrollmentDate`. Thêm ràng buộc `@UniqueConstraint` cho `studentId` + `courseId`. Định nghĩa quan hệ `@ManyToOne` tới `UserEntity` và `CourseEntity`.  
     - Tạo `AttendanceEntity.java` với các trường `attendanceId`, `studentId`, `courseId`, `attendanceDate`, `timestamp`. Thêm ràng buộc `@UniqueConstraint` cho `studentId` + `courseId` + `attendanceDate`. Định nghĩa quan hệ `@ManyToOne` tới `UserEntity` và `CourseEntity`.  
     - Tạo `MemberCardEntity.java` với các trường `cardId`, `studentId`, `issueDate`, `validityDays`, `remainingDays`. Thêm ràng buộc `@Check` cho `validityDays > 0` và `remainingDays >= 0`. Định nghĩa quan hệ `@ManyToOne` tới `UserEntity`.  
  2. **DTO**  
     - Tạo `CourseDTO.java`, `EnrollmentDTO.java`, `AttendanceDTO.java`, `MemberCardDTO.java` với các trường tương ứng và các annotation `@JsonProperty` khi cần.  
  3. **Service**  
     - Tạo `CourseService.java`, `EnrollmentService.java`, `AttendanceService.java`, `MemberCardService.java`. Sử dụng `@Transactional`, `@Service`. Kiểm tra đầu vào với `@Valid`. Xử lý business logic (đăng ký, ghi danh, điểm danh, gia hạn thẻ).  
  4. **Controller**  
     - Tạo `CourseController.java`, `EnrollmentController.java`, `AttendanceController.java`, `MemberCardController.java`. Sử dụng `@RestController`, `@RequestMapping`. Định nghĩa các endpoint `GET`, `POST`, `PUT`, `DELETE`, `POST /scan`. Sử dụng `@PreAuthorize` để kiểm tra RBAC.  
  5. **Exception Handling**  
     - Tạo `GlobalExceptionHandler.java` với `@ControllerAdvice`. Xử lý `MethodArgumentNotValidException`, `DataIntegrityViolationException`, `NetworkOfflineException`, `DuplicateAttendanceException`. Trả về `ResponseEntity` với mã lỗi và thông báo chi tiết.  
  6. **OWASP Compliance**  
     - Sử dụng JPA prepared statements, `@Valid`, `@Pattern` cho các trường nhập. Đánh dấu các trường nhạy cảm với `@JsonIgnore`. Đảm bảo JWT được xác thực và hết hạn đúng thời gian. Sử dụng `@Transactional` để tránh race condition.  
  7. **Logging**  
     - Sử dụng SLF4J để ghi log các hành động quan trọng và lỗi.  

#### 📝 TÀI LIỆU KIẾN TRÚC GIAI ĐOẠN 3 1.2:
Soạn thảo tài liệu kiến trúc chi tiết cho giai đoạn 3, bao gồm mô hình dữ liệu, luồng API, exception handlers, và các thành phần quan trọng. Đảm bảo tài liệu đáp ứng chuẩn OWASP, bảo mật, và ghi chú các ràng buộc dữ liệu. Đưa ra sơ đồ kiến trúc, bảng dữ liệu, và mô tả chi tiết các endpoint.
##### Tác nhân phụ được giao: Doc
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `./sources/docs/Phase3_Architecture.md`
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-007], [REQ-010], [DAT-004], [DAT-005], [DAT-006], [DAT-007]<!--END_TAGS-->
* **Hướng dẫn công việc chi tiết:**  
  1. **Mục lục**: Giới thiệu, Mô hình dữ liệu, Luồng API, Exception Handling, Bảo mật, Triển khai.  
  2. **Mô hình dữ liệu**: Sử dụng Mermaid để vẽ ER diagram cho `courses`, `enrollments`, `attendance`, `member_cards`.  
  3. **Luồng API**: Trình bày chi tiết các endpoint trong JSON contract (đính kèm dưới đây).  
  4. **Exception Handling**: Mô tả các exception handler `NetworkOfflineException`, `DuplicateAttendanceException`.  
  5. **Bảo mật**: Đề cập OWASP, JWT, TLS, RBAC.  
  6. **Triển khai**: Mô tả Docker, Kubernetes, CI/CD.  

#### 📝 Kiểm thử điểm danh QR và xử lý trùng lặp 2.1:
Xây dựng bộ kiểm thử tích hợp cho AttendanceService, bao gồm kiểm tra ghi nhận điểm danh lần đầu, phát hiện duplicate, và mô phỏng mất kết nối mạng. Đảm bảo logic idempotent và cờ duplicate được trả về chính xác. Kiểm tra exception handlers cho mạng offline và duplicate.
##### Tác nhân phụ được giao: Tester
##### Các thành phần mục tiêu & Yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu:** `INTEGRATION_SCOPE;./sources/backend/tests/integration/AttendanceIntegrationTest.java`
* **Thẻ truy xuất:** <!--START_TAGS-->[REQ-012], [DAT-006], [EXC-001], [EXC-002]<!--END_TAGS-->
* **Hướng dẫn công việc chi tiết:**  
  1. **Setup**  
     - Sử dụng `@SpringBootTest`, `@AutoConfigureMockMvc`.  
     - Tạo dữ liệu mẫu `Course`, `Student`, `Attendance` trong `@BeforeEach`.  
  2. **Scenario 1: Ghi nhận điểm danh đầu tiên**  
     - Gửi `POST /api/v1/attendance/scan` với body `{ "studentId": "...", "courseId": "...", "qrCodeData": "..." }`.  
     - Kiểm tra status 200, body chứa `attendanceId` và `duplicate: false`.  
  3. **Scenario 2: Duplicate attendance**  
     - Gửi lại cùng request trong cùng ngày.  
     - Kiểm tra status 200, body chứa `duplicate: true`.  
  4. **Scenario 3: Mất kết nối mạng**  
     - Mock `AttendanceService` để ném `NetworkOfflineException`.  
     - Kiểm tra status 503, body chứa thông báo lỗi.  
  5. **Assertions**  
     - Kiểm tra số lượng bản ghi trong DB, trường `duplicate` trong response.  
  6. **Cleanup**  
     - Xóa dữ liệu trong `@AfterEach`.  

### Database Schema DDL SQL Specification

```sql
CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID NOT NULL,
    max_students INT NOT NULL DEFAULT 30,
    CONSTRAINT fk_courses_teacher FOREIGN KEY (teacher_id) REFERENCES users(user_id),
    CONSTRAINT chk_course_dates CHECK (start_date <= end_date)
);

CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_enrollments_student FOREIGN KEY (student_id) REFERENCES users(user_id),
    CONSTRAINT fk_enrollments_course FOREIGN KEY (course_id) REFERENCES courses(course_id),
    CONSTRAINT uniq_student_course UNIQUE (student_id, course_id)
);

CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    course_id UUID NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_attendance_student FOREIGN KEY (student_id) REFERENCES users(user_id),
    CONSTRAINT fk_attendance_course FOREIGN KEY (course_id) REFERENCES courses(course_id),
    CONSTRAINT uniq_student_course_date UNIQUE (student_id, course_id, attendance_date)
);

CREATE TABLE member_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT NOT NULL,
    CONSTRAINT fk_membercard_student FOREIGN KEY (student_id) REFERENCES users(user_id),
    CONSTRAINT chk_validity_positive CHECK (validity_days > 0 AND remaining_days >= 0)
);
```

### API and Event Routing Contracts

```json
{
  "endpoints": [
    {
      "path": "/api/v1/courses",
      "method": "GET",
      "response": [
        {
          "courseId": "UUID",
          "title": "string",
          "startDate": "DATE",
          "endDate": "DATE",
          "teacherName": "string"
        }
      ]
    },
    {
      "path": "/api/v1/courses",
      "method": "POST",
      "request": {
        "title": "string",
        "description": "string",
        "startDate": "DATE",
        "endDate": "DATE",
        "teacherId": "UUID",
        "maxStudents": "INT"
      },
      "response": {
        "courseId": "UUID"
      }
    },
    {
      "path": "/api/v1/courses/{id}",
      "method": "PUT",
      "request": {
        "title": "string",
        "startDate": "DATE",
        "endDate": "DATE",
        "teacherId": "UUID"
      },
      "response": {
        "courseId": "UUID"
      }
    },
    {
      "path": "/api/v1/courses/{id}",
      "method": "DELETE",
      "response": {
        "courseId": "UUID"
      }
    },
    {
      "path": "/api/v1/enrollments",
      "method": "POST",
      "request": {
        "studentId": "UUID",
        "courseId": "UUID"
      },
      "response": {
        "enrollmentId": "UUID"
      }
    },
    {
      "path": "/api/v1/attendance/scan",
      "method": "POST",
      "request": {
        "studentId": "UUID",
        "courseId": "UUID",
        "qrCodeData": "string"
      },
      "response": {
        "attendanceId": "UUID",
        "duplicate": "boolean"
      }
    },
    {
      "path": "/api/v1/membercards/{studentId}",
      "method": "GET",
      "response": {
        "cardId": "UUID",
        "validityDays": "INT",
        "remainingDays": "INT"
      }
    },
    {
      "path": "/api/v1/membercards/renew",
      "method": "POST",
      "request": {
        "studentId": "UUID",
        "additionalDays": "INT"
      },
      "response": {
        "cardId": "UUID",
        "newRemainingDays": "INT"
      }
    }
  ]
}
```

### Phase Localized Exception Handlers

- **EXC-001**: Xử lý lỗi mất kết nối mạng trong quá trình quét QR: Khi thiết bị quét QR nhưng không có mạng, ứng dụng lưu sự kiện cục bộ và tự động đồng bộ khi kết nối được khôi phục; backend xử lý đồng bộ một cách idempotent.  
- **EXC-002**: Ngăn chặn điểm danh trùng lặp: Nếu cùng một studentId và courseId được gửi trong cùng một ngày, hệ thống trả về success với cờ duplicate=true và không tạo bản ghi mới.