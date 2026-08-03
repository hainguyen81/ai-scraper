```text```json
{
  "phase_id": 2,
  "phase_name": "phase2_centers_courses_enrollments",
  "phase_description": "Triển khai các dịch vụ quản lý trung tâm, khóa học, ghi danh, khuyến mãi và thông báo, bao gồm thiết kế schema, API, và tuân thủ OWASP, NFR, và mapping tag đầy đủ.",
  "project_name": "membership-hub",
  "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 1: TRIỂN KHAI DỊCH VỤ TRUNG TÂM",
      "sub_tasks": [
        {
          "id": "D1_ST1",
          "agent": "Coder",
          "desc": "Triển khai endpoint CRUD cho trung tâm bao gồm các API sau:\n- `GET /api/v1/centers` – Trả về danh sách trung tâm.\n- `POST /api/v1/centers` – Tạo trung tâm mới với kiểm tra duy nhất cho trường `taxId` (áp dụng prepared statements để ngăn chặn SQL injection).\n- `PUT /api/v1/centers/{id}` – Cập nhật thông tin trung tâm.\n- `DELETE /api/v1/centers/{id}` – Xóa trung tâm.\n\nÁp dụng các biện pháp bảo mật OWASP A01-A10 bao gồm:\n- Bảo vệ dữ liệu nhạy cảm (mã hóa trường `taxId`, `contactEmail`).\n- Kiểm tra đầu vào nghiêm ngặt cho tất cả các trường.\n- Sử dụng JWT cho xác thực và phân quyền.\n- Ghi log audit cho mọi thao tác thay đổi dữ liệu (CREATE, UPDATE, DELETE).\n\nĐảm bảo tuân thủ schema DDL cho bảng `CENTERS`:\n```sql\nCREATE TABLE CENTERS (\n    centerId UUID PRIMARY KEY,\n    name VARCHAR(100) NOT NULL,\n    address VARCHAR(255) NOT NULL,\n    taxId VARCHAR(20) NOT NULL UNIQUE,\n    contactPhone VARCHAR(30),\n    contactEmail VARCHAR(255)\n);\n```",
          "targeted_tags": ["[REQ-004]", "[DAT-003]", "[NFR-002]", "[NFR-004]"],
          "components": [
            "./sources/backend.centers/org/nlh4j/sources/centers/CenterResource.java"
          ]
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 2: TRIỂN KHAI DỊCH VỤ KHÓA HỌC VÀ GHI DANH",
      "sub_tasks": [
        {
          "id": "D2_ST1",
          "agent": "Coder",
          "desc": "Triển khai endpoint CRUD cho khóa học bao gồm các API sau:\n- `GET /api/v1/courses` – Trả về danh sách khóa học.\n- `POST /api/v1/courses` – Tạo khóa học mới với kiểm tra xung đột lịch dạy (đảm bảo không có khóa học nào trùng lịch với cùng giáo viên).\n- `PUT /api/v1/courses/{id}` – Cập nhật thông tin khóa học.\n- `DELETE /api/v1/courses/{id}` – Xóa khóa học.\n\nÁp dụng các biện pháp bảo mật OWASP A01-A10 bao gồm:\n- Bảo vệ dữ liệu nhạy cảm (mã hóa trường `description`).\n- Kiểm tra đầu vào nghiêm ngặt cho tất cả các trường.\n- Sử dụng JWT cho xác thực và phân quyền.\n- Ghi log audit cho mọi thao tác thay đổi dữ liệu (CREATE, UPDATE, DELETE).\n\nĐảm bảo tuân thủ schema DDL cho bảng `COURSES`:\n```sql\nCREATE TABLE COURSES (\n    courseId UUID PRIMARY KEY,\n    title VARCHAR(150) NOT NULL,\n    description TEXT,\n    startDate DATE NOT NULL,\n    endDate DATE NOT NULL,\n    teacherId UUID NOT NULL REFERENCES USERS(userId),\n    maxStudents INT NOT NULL DEFAULT 30\n);\n```",
          "targeted_tags": ["[REQ-007]", "[DAT-004]", "[NFR-002]", "[NFR-004]"],
          "components": [
            "./sources/backend.courses/org/nlh4j/sources/courses/CourseResource.java"
          ]
        },
        {
          "id": "D2_ST2",
          "agent": "Coder",
          "desc": "Triển khai endpoint CRUD cho ghi danh bao gồm các API sau:\n- `GET /api/v1/enrollments` – Trả về danh sách ghi danh.\n- `POST /api/v1/enrollments` – Ghi danh học viên vào khóa học với kiểm tra khả năng (đảm bảo không vượt quá `maxStudents`). Tự động tạo tài khoản học viên nếu chưa tồn tại.\n\nÁp dụng các biện pháp bảo mật OWASP A01-A10 bao gồm:\n- Bảo vệ dữ liệu nhạy cảm (mã hóa trường `studentId`, `courseId`).\n- Kiểm tra đầu vào nghiêm ngặt cho tất cả các trường.\n- Sử dụng JWT cho xác thực và phân quyền.\n- Ghi log audit cho mọi thao tác thay đổi dữ liệu (CREATE).\n\nĐảm bảo tuân thủ schema DDL cho bảng `ENROLLMENTS`:\n```sql\nCREATE TABLE ENROLLMENTS (\n    enrollmentId UUID PRIMARY KEY,\n    studentId UUID NOT NULL REFERENCES USERS(userId),\n    courseId UUID NOT NULL REFERENCES COURSES(courseId),\n    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),\n    UNIQUE(studentId, courseId)\n);\n```",
          "targeted_tags": ["[REQ-010]", "[DAT-005]", "[NFR-002]", "[NFR-004]"],
          "components": [
            "./sources/backend.enrollments/org/nlh4j/sources/enrollments/EnrollmentResource.java"
          ]
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
      "context_section": "DAY 3: TRIỂN KHAI DỊCH VỤ KHUYẾN MÃI & THÔNG BÁO",
      "sub_tasks": [
        {
          "id": "D3_ST1",
          "agent": "Coder",
          "desc": "Triển khai endpoint CRUD cho khuyến mãi và thông báo bao gồm các API sau:\n- `POST /api/v1/promotions` – Tạo khuyến mãi mới.\n- `PUT /api/v1/promotions/{id}` – Cập nhật khuyến mãi.\n- `POST /api/v1/announcements` – Tạo thông báo mới.\n- `PUT /api/v1/announcements/{id}` – Cập nhật thông báo.\n\nÁp dụng các biện pháp bảo mật OWASP A01-A10 bao gồm:\n- Bảo vệ dữ liệu nhạy cảm (mã hóa trường `code`, `description`, `content`).\n- Kiểm tra đầu vào nghiêm ngặt cho tất cả các trường.\n- Sử dụng JWT cho xác thực và phân quyền.\n- Ghi log audit cho mọi thao tác thay đổi dữ liệu (CREATE, UPDATE).\n\nĐảm bảo tuân thủ schema DDL cho các bảng `PROMOTIONS` và `ANNOUNCEMENTS`:\n```sql\nCREATE TABLE PROMOTIONS (\n    promoId UUID PRIMARY KEY,\n    code VARCHAR(30) NOT NULL UNIQUE,\n    discountPercent SMALLINT NOT NULL,\n    startDate DATE,\n    endDate DATE,\n    description TEXT\n);\n\nCREATE TABLE ANNOUNCEMENTS (\n    announcementId UUID PRIMARY KEY,\n    title VARCHAR(150) NOT NULL,\n    content TEXT NOT NULL,\n    startDate DATE,\n    endDate DATE\n);\n```",
          "targeted_tags": ["[REQ-017]", "[REQ-018]", "[DAT-009]", "[NFR-002]", "[NFR-004]"],
          "components": [
            "./sources/backend.promotions/org/nlh4j/sources/promotions/PromotionResource.java"
          ]
        }
      ]
    }
  ]
}
``````
-------------------------------------------------
```text{
    "phase_id": 2,
    "phase_name": "phase2_centers_courses_enrollments",
    "phase_description": "Triển khai các dịch vụ quản lý trung tâm, khóa học, ghi danh, khuyến mãi và thông báo, bao gồm thiết kế schema, API, và tuân thủ OWASP, NFR, và mapping tag đầy đủ.",
    "project_name": "membership-hub",
    "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
    "source_target_dir": "sources/",
    "objectives": [],
    "days": [
        {
            "day": 1,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 1: TRIỂN KHAI DỊCH VỤ TRUNG TÂM",
            "sub_tasks": [
                {
                    "id": "D1_ST1",
                    "agent": "Coder",
                    "desc": "Triển khai endpoint CRUD cho trung tâm bao gồm các API sau:\n- `GET /api/v1/centers` – Trả về danh sách trung tâm.\n- `POST /api/v1/centers` – Tạo trung tâm mới với kiểm tra duy nhất cho trường `taxId` (áp dụng prepared statements để ngăn chặn SQL injection).\n- `PUT /api/v1/centers/{id}` – Cập nhật thông tin trung tâm.\n- `DELETE /api/v1/centers/{id}` – Xóa trung tâm.\n\nÁp dụng các biện pháp bảo mật OWASP A01-A10 bao gồm:\n- Bảo vệ dữ liệu nhạy cảm (mã hóa trường `taxId`, `contactEmail`).\n- Kiểm tra đầu vào nghiêm ngặt cho tất cả các trường.\n- Sử dụng JWT cho xác thực và phân quyền.\n- Ghi log audit cho mọi thao tác thay đổi dữ liệu (CREATE, UPDATE, DELETE).\n\nĐảm bảo tuân thủ schema DDL cho bảng `CENTERS`:\n```sql\nCREATE TABLE CENTERS (\n    centerId UUID PRIMARY KEY,\n    name VARCHAR(100) NOT NULL,\n    address VARCHAR(255) NOT NULL,\n    taxId VARCHAR(20) NOT NULL UNIQUE,\n    contactPhone VARCHAR(30),\n    contactEmail VARCHAR(255)\n);\n```",
                    "targeted_tags": [
                        "[REQ-004]",
                        "[DAT-003]",
                        "[NFR-002]",
                        "[NFR-004]"
                    ],
                    "components": [
                        "./sources/backend.centers/org/nlh4j/sources/centers/CenterResource.java"
                    ]
                }
            ]
        },
        {
            "day": 2,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 2: TRIỂN KHAI DỊCH VỤ KHÓA HỌC VÀ GHI DANH",
            "sub_tasks": [
                {
                    "id": "D2_ST1",
                    "agent": "Coder",
                    "desc": "Triển khai endpoint CRUD cho khóa học bao gồm các API sau:\n- `GET /api/v1/courses` – Trả về danh sách khóa học.\n- `POST /api/v1/courses` – Tạo khóa học mới với kiểm tra xung đột lịch dạy (đảm bảo không có khóa học nào trùng lịch với cùng giáo viên).\n- `PUT /api/v1/courses/{id}` – Cập nhật thông tin khóa học.\n- `DELETE /api/v1/courses/{id}` – Xóa khóa học.\n\nÁp dụng các biện pháp bảo mật OWASP A01-A10 bao gồm:\n- Bảo vệ dữ liệu nhạy cảm (mã hóa trường `description`).\n- Kiểm tra đầu vào nghiêm ngặt cho tất cả các trường.\n- Sử dụng JWT cho xác thực và phân quyền.\n- Ghi log audit cho mọi thao tác thay đổi dữ liệu (CREATE, UPDATE, DELETE).\n\nĐảm bảo tuân thủ schema DDL cho bảng `COURSES`:\n```sql\nCREATE TABLE COURSES (\n    courseId UUID PRIMARY KEY,\n    title VARCHAR(150) NOT NULL,\n    description TEXT,\n    startDate DATE NOT NULL,\n    endDate DATE NOT NULL,\n    teacherId UUID NOT NULL REFERENCES USERS(userId),\n    maxStudents INT NOT NULL DEFAULT 30\n);\n```",
                    "targeted_tags": [
                        "[REQ-007]",
                        "[DAT-004]",
                        "[NFR-002]",
                        "[NFR-004]"
                    ],
                    "components": [
                        "./sources/backend.courses/org/nlh4j/sources/courses/CourseResource.java"
                    ]
                },
                {
                    "id": "D2_ST2",
                    "agent": "Coder",
                    "desc": "Triển khai endpoint CRUD cho ghi danh bao gồm các API sau:\n- `GET /api/v1/enrollments` – Trả về danh sách ghi danh.\n- `POST /api/v1/enrollments` – Ghi danh học viên vào khóa học với kiểm tra khả năng (đảm bảo không vượt quá `maxStudents`). Tự động tạo tài khoản học viên nếu chưa tồn tại.\n\nÁp dụng các biện pháp bảo mật OWASP A01-A10 bao gồm:\n- Bảo vệ dữ liệu nhạy cảm (mã hóa trường `studentId`, `courseId`).\n- Kiểm tra đầu vào nghiêm ngặt cho tất cả các trường.\n- Sử dụng JWT cho xác thực và phân quyền.\n- Ghi log audit cho mọi thao tác thay đổi dữ liệu (CREATE).\n\nĐảm bảo tuân thủ schema DDL cho bảng `ENROLLMENTS`:\n```sql\nCREATE TABLE ENROLLMENTS (\n    enrollmentId UUID PRIMARY KEY,\n    studentId UUID NOT NULL REFERENCES USERS(userId),\n    courseId UUID NOT NULL REFERENCES COURSES(courseId),\n    enrollmentDate TIMESTAMP NOT NULL DEFAULT NOW(),\n    UNIQUE(studentId, courseId)\n);\n```",
                    "targeted_tags": [
                        "[REQ-010]",
                        "[DAT-005]",
                        "[NFR-002]",
                        "[NFR-004]"
                    ],
                    "components": [
                        "./sources/backend.enrollments/org/nlh4j/sources/enrollments/EnrollmentResource.java"
                    ]
                }
            ]
        },
        {
            "day": 3,
            "context_file": ".ai/.plan/.context/phase-2.context.blueprint.md",
            "context_section": "DAY 3: TRIỂN KHAI DỊCH VỤ KHUYẾN MÃI & THÔNG BÁO",
            "sub_tasks": [
                {
                    "id": "D3_ST1",
                    "agent": "Coder",
                    "desc": "Triển khai endpoint CRUD cho khuyến mãi và thông báo bao gồm các API sau:\n- `POST /api/v1/promotions` – Tạo khuyến mãi mới.\n- `PUT /api/v1/promotions/{id}` – Cập nhật khuyến mãi.\n- `POST /api/v1/announcements` – Tạo thông báo mới.\n- `PUT /api/v1/announcements/{id}` – Cập nhật thông báo.\n\nÁp dụng các biện pháp bảo mật OWASP A01-A10 bao gồm:\n- Bảo vệ dữ liệu nhạy cảm (mã hóa trường `code`, `description`, `content`).\n- Kiểm tra đầu vào nghiêm ngặt cho tất cả các trường.\n- Sử dụng JWT cho xác thực và phân quyền.\n- Ghi log audit cho mọi thao tác thay đổi dữ liệu (CREATE, UPDATE).\n\nĐảm bảo tuân thủ schema DDL cho các bảng `PROMOTIONS` và `ANNOUNCEMENTS`:\n```sql\nCREATE TABLE PROMOTIONS (\n    promoId UUID PRIMARY KEY,\n    code VARCHAR(30) NOT NULL UNIQUE,\n    discountPercent SMALLINT NOT NULL,\n    startDate DATE,\n    endDate DATE,\n    description TEXT\n);\n\nCREATE TABLE ANNOUNCEMENTS (\n    announcementId UUID PRIMARY KEY,\n    title VARCHAR(150) NOT NULL,\n    content TEXT NOT NULL,\n    startDate DATE,\n    endDate DATE\n);\n```",
                    "targeted_tags": [
                        "[REQ-017]",
                        "[REQ-018]",
                        "[DAT-009]",
                        "[NFR-002]",
                        "[NFR-004]"
                    ],
                    "components": [
                        "./sources/backend.promotions/org/nlh4j/sources/promotions/PromotionResource.java"
                    ]
                }
            ]
        }
    ],
    "phase_idx": 2,
    "phase_context_file": ".ai/.plan/.context/phase-2.context.blueprint.md"
}```
-------------------------------------------------
