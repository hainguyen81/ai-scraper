```text```json
{
  "phase_id": 3,
  "phase_name": "course_management_module",
  "phase_description": "Triển khai module quản lý khóa học bao gồm danh sách khóa học công khai, CRUD khóa học với kiểm tra xung đột lịch giảng, gán giáo viên, và tích hợp với RBAC cho Manager và System/Center Admin",
  "project_name": "membership-hub",
  "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "NGÀY 5: TRIỂN KHAI SERVICE QUẢN LÝ KHÓA HỌC VÀ LOGIC TRÁNH XUNG ĐỘT",
      "sub_tasks": [
        {
          "id": "D1_ST1",
          "agent": "Coder",
          "desc": "Triển khai schema cơ sở dữ liệu cho bảng Courses với các ràng buộc toàn vẹn dữ liệu bao gồm: khóa chính, khóa ngoại (nếu có), các ràng buộc CHECK cho định dạng dữ liệu, và các chỉ mục tối ưu hóa truy vấn. Đảm bảo schema tuân thủ yêu cầu [DAT-004] và tương thích với JPA/Hibernate. Schema phải bao gồm các trường: course_id (UUID), title (varchar), description (text), start_date (timestamp), end_date (timestamp), max_students (integer), teacher_id (UUID, nullable), status (enum: DRAFT, PUBLISHED, CANCELLED), created_at (timestamp), updated_at (timestamp).",
          "targeted_tags": [
            "[DAT-004]"
          ],
          "components": [
            "./sources/backend.membershiphub.course/courses.sql"
          ]
        },
        {
          "id": "D1_ST2",
          "agent": "Coder",
          "desc": "Triển khai lớp CourseService với các phương thức CRUD đầy đủ cho quản lý khóa học, bao gồm: createCourse(), getCourseById(), updateCourse(), deleteCourse(), và listAllCourses(). Thực hiện validation nghiêm ngặt cho tất cả đầu vào sử dụng @Valid và xử lý ngoại lệ tùy chỉnh. Triển khai logic kiểm tra xung đột lịch giảng bằng cách so sánh khoảng thời gian của khóa học mới với các khóa học hiện có của cùng giáo viên. Sử dụng @Transactional cho tất cả các thao tác ghi và @PreAuthorize để kiểm tra quyền truy cập theo RBAC (chỉ System Admin và Center Admin có thể tạo/cập nhật/xóa khóa học). Đảm bảo tuân thủ các yêu cầu [REQ-007], [REQ-008], [REQ-009], [NFR-001], [NFR-002].",
          "targeted_tags": [
            "[REQ-007]",
            "[REQ-008]",
            "[REQ-009]",
            "[DAT-004]",
            "[ARC-003]",
            "[NFR-001]",
            "[NFR-002]"
          ],
          "components": [
            "./sources/backend.membershiphub.course/course-service.java"
          ]
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
      "context_section": "NGÀY 6: VIẾT BỘ KIỂM TRA CHO CÁC CHỨC NĂNG QUẢN LÝ KHÓA HỌC",
      "sub_tasks": [
        {
          "id": "D2_ST1",
          "agent": "Tester",
          "desc": "Xây dựng bộ kiểm thử tích hợp cho các API CRUD khóa học và logic kiểm tra xung đột lịch giảng. Sử dụng JUnit 5 và Testcontainers để kiểm thử với cơ sở dữ liệu thực tế. Bao gồm các trường hợp kiểm thử sau:\n\n1. **Happy Path Tests**:\n   - Tạo khóa học thành công với dữ liệu hợp lệ\n   - Lấy thông tin khóa học theo ID\n   - Cập nhật khóa học thành công\n   - Xóa mềm khóa học\n   - Lấy danh sách tất cả khóa học\n\n2. **Validation Tests**:\n   - Từ chối khóa học với ngày kết thúc trước ngày bắt đầu\n   - Từ chối khóa học với số lượng sinh viên tối đa âm\n   - Từ chối khóa học với tiêu đề trống\n\n3. **Conflict Detection Tests**:\n   - Từ chối khóa học mới khi trùng lịch với khóa học hiện có của cùng giáo viên\n   - Cho phép khóa học mới khi không trùng lịch\n\n4. **Authorization Tests**:\n   - Từ chối yêu cầu tạo khóa học từ người dùng không có quyền\n   - Từ chối yêu cầu cập nhật khóa học từ người dùng không có quyền\n\n5. **Edge Cases**:\n   - Xử lý khóa học với ngày bắt đầu và kết thúc giống nhau\n   - Xử lý khóa học với giáo viên null\n\nĐảm bảo độ phủ mã đạt ≥85% cho tất cả các dịch vụ và tuân thủ các yêu cầu [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003].",
          "targeted_tags": [
            "[REQ-007]",
            "[REQ-008]",
            "[REQ-009]",
            "[DAT-004]",
            "[ARC-003]"
          ],
          "components": [
            "INTEGRATION_SCOPE;./sources/backend.membershiphub.course/courseservice-integration-test.java"
          ]
        }
      ]
    }
  ]
}
``````
-------------------------------------------------
```text{
    "phase_id": 3,
    "phase_name": "course_management_module",
    "phase_description": "Triển khai module quản lý khóa học bao gồm danh sách khóa học công khai, CRUD khóa học với kiểm tra xung đột lịch giảng, gán giáo viên, và tích hợp với RBAC cho Manager và System/Center Admin",
    "project_name": "membership-hub",
    "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
    "source_target_dir": "sources/",
    "objectives": [],
    "days": [
        {
            "day": 1,
            "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
            "context_section": "NGÀY 5: TRIỂN KHAI SERVICE QUẢN LÝ KHÓA HỌC VÀ LOGIC TRÁNH XUNG ĐỘT",
            "sub_tasks": [
                {
                    "id": "D1_ST1",
                    "agent": "Coder",
                    "desc": "Triển khai schema cơ sở dữ liệu cho bảng Courses với các ràng buộc toàn vẹn dữ liệu bao gồm: khóa chính, khóa ngoại (nếu có), các ràng buộc CHECK cho định dạng dữ liệu, và các chỉ mục tối ưu hóa truy vấn. Đảm bảo schema tuân thủ yêu cầu [DAT-004] và tương thích với JPA/Hibernate. Schema phải bao gồm các trường: course_id (UUID), title (varchar), description (text), start_date (timestamp), end_date (timestamp), max_students (integer), teacher_id (UUID, nullable), status (enum: DRAFT, PUBLISHED, CANCELLED), created_at (timestamp), updated_at (timestamp).",
                    "targeted_tags": [
                        "[DAT-004]"
                    ],
                    "components": [
                        "./sources/backend.membershiphub.course/courses.sql"
                    ]
                },
                {
                    "id": "D1_ST2",
                    "agent": "Coder",
                    "desc": "Triển khai lớp CourseService với các phương thức CRUD đầy đủ cho quản lý khóa học, bao gồm: createCourse(), getCourseById(), updateCourse(), deleteCourse(), và listAllCourses(). Thực hiện validation nghiêm ngặt cho tất cả đầu vào sử dụng @Valid và xử lý ngoại lệ tùy chỉnh. Triển khai logic kiểm tra xung đột lịch giảng bằng cách so sánh khoảng thời gian của khóa học mới với các khóa học hiện có của cùng giáo viên. Sử dụng @Transactional cho tất cả các thao tác ghi và @PreAuthorize để kiểm tra quyền truy cập theo RBAC (chỉ System Admin và Center Admin có thể tạo/cập nhật/xóa khóa học). Đảm bảo tuân thủ các yêu cầu [REQ-007], [REQ-008], [REQ-009], [NFR-001], [NFR-002].",
                    "targeted_tags": [
                        "[REQ-007]",
                        "[REQ-008]",
                        "[REQ-009]",
                        "[DAT-004]",
                        "[ARC-003]",
                        "[NFR-001]",
                        "[NFR-002]"
                    ],
                    "components": [
                        "./sources/backend.membershiphub.course/course-service.java"
                    ]
                }
            ]
        },
        {
            "day": 2,
            "context_file": ".ai/.plan/.context/phase-3.context.blueprint.md",
            "context_section": "NGÀY 6: VIẾT BỘ KIỂM TRA CHO CÁC CHỨC NĂNG QUẢN LÝ KHÓA HỌC",
            "sub_tasks": [
                {
                    "id": "D2_ST1",
                    "agent": "Tester",
                    "desc": "Xây dựng bộ kiểm thử tích hợp cho các API CRUD khóa học và logic kiểm tra xung đột lịch giảng. Sử dụng JUnit 5 và Testcontainers để kiểm thử với cơ sở dữ liệu thực tế. Bao gồm các trường hợp kiểm thử sau:\n\n1. **Happy Path Tests**:\n   - Tạo khóa học thành công với dữ liệu hợp lệ\n   - Lấy thông tin khóa học theo ID\n   - Cập nhật khóa học thành công\n   - Xóa mềm khóa học\n   - Lấy danh sách tất cả khóa học\n\n2. **Validation Tests**:\n   - Từ chối khóa học với ngày kết thúc trước ngày bắt đầu\n   - Từ chối khóa học với số lượng sinh viên tối đa âm\n   - Từ chối khóa học với tiêu đề trống\n\n3. **Conflict Detection Tests**:\n   - Từ chối khóa học mới khi trùng lịch với khóa học hiện có của cùng giáo viên\n   - Cho phép khóa học mới khi không trùng lịch\n\n4. **Authorization Tests**:\n   - Từ chối yêu cầu tạo khóa học từ người dùng không có quyền\n   - Từ chối yêu cầu cập nhật khóa học từ người dùng không có quyền\n\n5. **Edge Cases**:\n   - Xử lý khóa học với ngày bắt đầu và kết thúc giống nhau\n   - Xử lý khóa học với giáo viên null\n\nĐảm bảo độ phủ mã đạt ≥85% cho tất cả các dịch vụ và tuân thủ các yêu cầu [REQ-007], [REQ-008], [REQ-009], [DAT-004], [ARC-003].",
                    "targeted_tags": [
                        "[REQ-007]",
                        "[REQ-008]",
                        "[REQ-009]",
                        "[DAT-004]",
                        "[ARC-003]"
                    ],
                    "components": [
                        "INTEGRATION_SCOPE;./sources/backend.membershiphub.course/courseservice-integration-test.java"
                    ]
                }
            ]
        }
    ],
    "phase_idx": 3,
    "phase_context_file": ".ai/.plan/.context/phase-3.context.blueprint.md"
}```
-------------------------------------------------
