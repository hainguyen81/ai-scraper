```text```json
{
  "phase_id": 4,
  "phase_name": "attendance_enrollment_module",
  "phase_description": "Triển khai module ghi danh học viên, điểm danh QR, và quản lý thẻ hội viên với service điểm danh QR idempotent, xử lý ngoại lệ network và duplicate scans, và tích hợp với hệ thống thông báo",
  "project_name": "membership-hub",
  "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
  "source_target_dir": "sources/",
  "days": [
    {
      "day": 1,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "NGÀY 7: TRIỂN KHAI SERVICE GHI DANH HỌC VIÊN VÀ ĐIỂM DANH QR",
      "sub_tasks": [
        {
          "id": "D1_ST1",
          "agent": "Coder",
          "desc": "Triển khai schema cơ sở dữ liệu cho bảng Enrollments với các trường: enrollment_id (UUID, PK), student_id (UUID, FK), course_id (UUID, FK), enrollment_date (TIMESTAMP), status (ENUM: ACTIVE, CANCELLED, COMPLETED), created_at (TIMESTAMP), updated_at (TIMESTAMP). Áp dụng các ràng buộc toàn vẹn dữ liệu bao gồm khóa ngoại, kiểm tra trạng thái hợp lệ, và chỉ mục cho các truy vấn thường xuyên. Đảm bảo schema tuân thủ chuẩn [DAT-005].",
          "targeted_tags": [
            "[DAT-005]"
          ],
          "components": [
            "./sources/backend.membershiphub.attendance/enrollments.sql"
          ]
        },
        {
          "id": "D1_ST2",
          "agent": "Coder",
          "desc": "Triển khai schema cơ sở dữ liệu cho bảng Attendance với các trường: attendance_id (UUID, PK), enrollment_id (UUID, FK), scan_time (TIMESTAMP), scan_location (GEOMETRY), qr_code_hash (VARCHAR, UNIQUE), status (ENUM: PRESENT, LATE, ABSENT), created_at (TIMESTAMP). Áp dụng ràng buộc idempotent trên trường qr_code_hash để ngăn chặn duplicate scans. Đảm bảo schema tuân thủ chuẩn [DAT-006] và tích hợp xử lý ngoại lệ network [EXC-001].",
          "targeted_tags": [
            "[DAT-006]",
            "[EXC-001]"
          ],
          "components": [
            "./sources/backend.membershiphub.attendance/attendances.sql"
          ]
        },
        {
          "id": "D1_ST3",
          "agent": "Coder",
          "desc": "Triển khai schema cơ sở dữ liệu cho bảng StudentCards với các trường: card_id (UUID, PK), student_id (UUID, FK), issue_date (TIMESTAMP), expiry_date (TIMESTAMP), status (ENUM: ACTIVE, EXPIRED, REVOKED), barcode (VARCHAR, UNIQUE), created_at (TIMESTAMP), updated_at (TIMESTAMP). Áp dụng ràng buộc kiểm tra ngày hết hạn và trạng thái hợp lệ. Đảm bảo schema tuân thủ chuẩn [DAT-007].",
          "targeted_tags": [
            "[DAT-007]"
          ],
          "components": [
            "./sources/backend.membershiphub.attendance/studentcards.sql"
          ]
        },
        {
          "id": "D1_ST4",
          "agent": "Coder",
          "desc": "Triển khai EnrollmentService với các phương thức sau:\n- `enrollStudent(UUID studentId, UUID courseId)`: Ghi danh học viên vào khóa học với validation nghiêm ngặt (kiểm tra tồn tại khóa học, trạng thái học viên, trùng lặp ghi danh).\n- `scanQRCode(UUID enrollmentId, String qrCodeHash, Geometry scanLocation)`: Xử lý điểm danh QR với logic idempotent (kiểm tra trùng lặp qr_code_hash), xử lý ngoại lệ network (retry mechanism với exponential backoff), và cập nhật trạng thái điểm danh.\n- `getEnrollmentStatus(UUID enrollmentId)`: Lấy trạng thái ghi danh hiện tại.\nĐảm bảo tất cả các phương thức tuân thủ [REQ-010], [REQ-011], [REQ-012], [REQ-013], [ARC-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003]. Sử dụng @Transactional cho các thao tác ghi và @Valid cho validation.",
          "targeted_tags": [
            "[REQ-010]",
            "[REQ-011]",
            "[REQ-012]",
            "[REQ-013]",
            "[DAT-005]",
            "[DAT-006]",
            "[DAT-007]",
            "[ARC-007]",
            "[EXC-001]",
            "[EXC-002]",
            "[NFR-001]",
            "[NFR-003]"
          ],
          "components": [
            "./sources/backend.membershiphub.attendance/enrollment-service.java"
          ]
        }
      ]
    },
    {
      "day": 2,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "NGÀY 8: TRIỂN KHAI SERVICE QUẢN LÝ THẺ HỘI VIÊN VÀ GIA HẠN",
      "sub_tasks": [
        {
          "id": "D2_ST1",
          "agent": "Coder",
          "desc": "Triển khai StudentCardService với các phương thức sau:\n- `issueStudentCard(UUID studentId)`: Phát hành thẻ hội viên mới với barcode duy nhất, ngày hết hạn mặc định (1 năm kể từ ngày phát hành), và trạng thái ACTIVE.\n- `renewStudentCard(UUID cardId)`: Gia hạn thẻ hội viên với ngày hết hạn mới (1 năm kể từ ngày hiện tại) và cập nhật trạng thái thành ACTIVE. Áp dụng validation kiểm tra trạng thái thẻ hiện tại (chỉ cho phép gia hạn nếu trạng thái là ACTIVE hoặc EXPIRED).\n- `revokeStudentCard(UUID cardId)`: Thu hồi thẻ hội viên và cập nhật trạng thái thành REVOKED.\n- `getStudentCard(UUID studentId)`: Lấy thông tin thẻ hội viên hiện tại của học viên.\nĐảm bảo tất cả các phương thức tuân thủ [REQ-014], [REQ-015], [DAT-007], [NFR-003]. Sử dụng @Transactional cho các thao tác ghi và @Valid cho validation.",
          "targeted_tags": [
            "[REQ-014]",
            "[REQ-015]",
            "[DAT-007]",
            "[NFR-003]"
          ],
          "components": [
            "./sources/backend.membershiphub.attendance/studentcard-service.java"
          ]
        }
      ]
    },
    {
      "day": 3,
      "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
      "context_section": "NGÀY 9: VIẾT BỘ KIỂM TRA TÍCH HỢP CHO GHI DANH, ĐIỂM DANH, VÀ THẺ",
      "sub_tasks": [
        {
          "id": "D3_ST1",
          "agent": "Tester",
          "desc": "Xây dựng bộ kiểm thử tích hợp cho EnrollmentService với các kịch bản sau:\n- Kiểm thử happy path cho ghi danh học viên và điểm danh QR.\n- Kiểm thử xử lý ngoại lệ network (mô phỏng lỗi kết nối cơ sở dữ liệu và retry mechanism).\n- Kiểm thử logic idempotent cho điểm danh QR (đảm bảo không có bản ghi trùng lặp khi quét cùng một mã QR nhiều lần).\n- Kiểm thử validation cho các trường hợp dữ liệu không hợp lệ (ví dụ: ghi danh vào khóa học không tồn tại, học viên không tồn tại).\n- Kiểm thử tích hợp với StudentCardService cho các kịch bản liên quan đến thẻ hội viên.\nSử dụng Testcontainers để thiết lập môi trường kiểm thử với cơ sở dữ liệu PostgreSQL thực tế. Đảm bảo độ phủ mã ≥85% và tất cả các yêu cầu [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [ARC-007], [EXC-001], [EXC-002] được kiểm tra.",
          "targeted_tags": [
            "[REQ-010]",
            "[REQ-011]",
            "[REQ-012]",
            "[REQ-013]",
            "[DAT-005]",
            "[DAT-006]",
            "[DAT-007]",
            "[ARC-007]",
            "[EXC-001]",
            "[EXC-002]"
          ],
          "components": [
            "INTEGRATION_SCOPE;./sources/backend.membershiphub.attendance/enrollment-service.java",
            "./sources/backend.membershiphub.attendance/enrollmentservice-integration-test.java"
          ]
        },
        {
          "id": "D3_ST2",
          "agent": "Tester",
          "desc": "Xây dựng bộ kiểm thử tích hợp cho StudentCardService với các kịch bản sau:\n- Kiểm thử happy path cho phát hành, gia hạn và thu hồi thẻ hội viên.\n- Kiểm thử validation cho các trường hợp dữ liệu không hợp lệ (ví dụ: gia hạn thẻ không tồn tại, thu hồi thẻ đã bị thu hồi).\n- Kiểm thử tích hợp với EnrollmentService cho các kịch bản liên quan đến ghi danh và điểm danh.\nSử dụng Testcontainers để thiết lập môi trường kiểm thử với cơ sở dữ liệu PostgreSQL thực tế. Đảm bảo độ phủ mã ≥85% và tất cả các yêu cầu [REQ-014], [REQ-015], [DAT-007], [NFR-003] được kiểm tra.",
          "targeted_tags": [
            "[REQ-014]",
            "[REQ-015]",
            "[DAT-007]",
            "[NFR-003]"
          ],
          "components": [
            "INTEGRATION_SCOPE;./sources/backend.membershiphub.attendance/studentcard-service.java",
            "./sources/backend.membershiphub.attendance/studentcardservice-integration-test.java"
          ]
        },
        {
          "id": "D3_ST3",
          "agent": "Doc",
          "desc": "Biên soạn tài liệu kỹ thuật cho module ghi danh và điểm danh bao gồm:\n- API documentation với OpenAPI/Swagger cho tất cả các endpoint: `GET /api/v1/courses/browse`, `POST /api/v1/enrollments`, `POST /api/v1/attendance/scan`, `GET /api/v1/studentcards/{studentId}`, `POST /api/v1/studentcards/{studentId}/renew`.\n- Schema documentation cho các bảng Enrollments, Attendance, StudentCards với mô tả chi tiết từng trường, ràng buộc và chỉ mục.\n- Hướng dẫn triển khai module bao gồm cấu hình cơ sở dữ liệu, biến môi trường và các bước khởi động dịch vụ.\n- Tài liệu về cơ chế xử lý ngoại lệ network và logic idempotent cho điểm danh QR.",
          "targeted_tags": [
            "[REQ-010]",
            "[REQ-011]",
            "[REQ-012]",
            "[REQ-013]",
            "[REQ-014]",
            "[REQ-015]",
            "[DAT-005]",
            "[DAT-006]",
            "[DAT-007]"
          ],
          "components": [
            ".ai/.plan/.context/phase-4.context.blueprint.md"
          ]
        }
      ]
    }
  ]
}
``````
-------------------------------------------------
```text{
    "phase_id": 4,
    "phase_name": "attendance_enrollment_module",
    "phase_description": "Triển khai module ghi danh học viên, điểm danh QR, và quản lý thẻ hội viên với service điểm danh QR idempotent, xử lý ngoại lệ network và duplicate scans, và tích hợp với hệ thống thông báo",
    "project_name": "membership-hub",
    "global_context_file": ".ai/.context/membership-hub.global.blueprint.md",
    "source_target_dir": "sources/",
    "objectives": [],
    "days": [
        {
            "day": 1,
            "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
            "context_section": "NGÀY 7: TRIỂN KHAI SERVICE GHI DANH HỌC VIÊN VÀ ĐIỂM DANH QR",
            "sub_tasks": [
                {
                    "id": "D1_ST1",
                    "agent": "Coder",
                    "desc": "Triển khai schema cơ sở dữ liệu cho bảng Enrollments với các trường: enrollment_id (UUID, PK), student_id (UUID, FK), course_id (UUID, FK), enrollment_date (TIMESTAMP), status (ENUM: ACTIVE, CANCELLED, COMPLETED), created_at (TIMESTAMP), updated_at (TIMESTAMP). Áp dụng các ràng buộc toàn vẹn dữ liệu bao gồm khóa ngoại, kiểm tra trạng thái hợp lệ, và chỉ mục cho các truy vấn thường xuyên. Đảm bảo schema tuân thủ chuẩn [DAT-005].",
                    "targeted_tags": [
                        "[DAT-005]"
                    ],
                    "components": [
                        "./sources/backend.membershiphub.attendance/enrollments.sql"
                    ]
                },
                {
                    "id": "D1_ST2",
                    "agent": "Coder",
                    "desc": "Triển khai schema cơ sở dữ liệu cho bảng Attendance với các trường: attendance_id (UUID, PK), enrollment_id (UUID, FK), scan_time (TIMESTAMP), scan_location (GEOMETRY), qr_code_hash (VARCHAR, UNIQUE), status (ENUM: PRESENT, LATE, ABSENT), created_at (TIMESTAMP). Áp dụng ràng buộc idempotent trên trường qr_code_hash để ngăn chặn duplicate scans. Đảm bảo schema tuân thủ chuẩn [DAT-006] và tích hợp xử lý ngoại lệ network [EXC-001].",
                    "targeted_tags": [
                        "[DAT-006]",
                        "[EXC-001]"
                    ],
                    "components": [
                        "./sources/backend.membershiphub.attendance/attendances.sql"
                    ]
                },
                {
                    "id": "D1_ST3",
                    "agent": "Coder",
                    "desc": "Triển khai schema cơ sở dữ liệu cho bảng StudentCards với các trường: card_id (UUID, PK), student_id (UUID, FK), issue_date (TIMESTAMP), expiry_date (TIMESTAMP), status (ENUM: ACTIVE, EXPIRED, REVOKED), barcode (VARCHAR, UNIQUE), created_at (TIMESTAMP), updated_at (TIMESTAMP). Áp dụng ràng buộc kiểm tra ngày hết hạn và trạng thái hợp lệ. Đảm bảo schema tuân thủ chuẩn [DAT-007].",
                    "targeted_tags": [
                        "[DAT-007]"
                    ],
                    "components": [
                        "./sources/backend.membershiphub.attendance/studentcards.sql"
                    ]
                },
                {
                    "id": "D1_ST4",
                    "agent": "Coder",
                    "desc": "Triển khai EnrollmentService với các phương thức sau:\n- `enrollStudent(UUID studentId, UUID courseId)`: Ghi danh học viên vào khóa học với validation nghiêm ngặt (kiểm tra tồn tại khóa học, trạng thái học viên, trùng lặp ghi danh).\n- `scanQRCode(UUID enrollmentId, String qrCodeHash, Geometry scanLocation)`: Xử lý điểm danh QR với logic idempotent (kiểm tra trùng lặp qr_code_hash), xử lý ngoại lệ network (retry mechanism với exponential backoff), và cập nhật trạng thái điểm danh.\n- `getEnrollmentStatus(UUID enrollmentId)`: Lấy trạng thái ghi danh hiện tại.\nĐảm bảo tất cả các phương thức tuân thủ [REQ-010], [REQ-011], [REQ-012], [REQ-013], [ARC-007], [EXC-001], [EXC-002], [NFR-001], [NFR-003]. Sử dụng @Transactional cho các thao tác ghi và @Valid cho validation.",
                    "targeted_tags": [
                        "[REQ-010]",
                        "[REQ-011]",
                        "[REQ-012]",
                        "[REQ-013]",
                        "[DAT-005]",
                        "[DAT-006]",
                        "[DAT-007]",
                        "[ARC-007]",
                        "[EXC-001]",
                        "[EXC-002]",
                        "[NFR-001]",
                        "[NFR-003]"
                    ],
                    "components": [
                        "./sources/backend.membershiphub.attendance/enrollment-service.java"
                    ]
                }
            ]
        },
        {
            "day": 2,
            "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
            "context_section": "NGÀY 8: TRIỂN KHAI SERVICE QUẢN LÝ THẺ HỘI VIÊN VÀ GIA HẠN",
            "sub_tasks": [
                {
                    "id": "D2_ST1",
                    "agent": "Coder",
                    "desc": "Triển khai StudentCardService với các phương thức sau:\n- `issueStudentCard(UUID studentId)`: Phát hành thẻ hội viên mới với barcode duy nhất, ngày hết hạn mặc định (1 năm kể từ ngày phát hành), và trạng thái ACTIVE.\n- `renewStudentCard(UUID cardId)`: Gia hạn thẻ hội viên với ngày hết hạn mới (1 năm kể từ ngày hiện tại) và cập nhật trạng thái thành ACTIVE. Áp dụng validation kiểm tra trạng thái thẻ hiện tại (chỉ cho phép gia hạn nếu trạng thái là ACTIVE hoặc EXPIRED).\n- `revokeStudentCard(UUID cardId)`: Thu hồi thẻ hội viên và cập nhật trạng thái thành REVOKED.\n- `getStudentCard(UUID studentId)`: Lấy thông tin thẻ hội viên hiện tại của học viên.\nĐảm bảo tất cả các phương thức tuân thủ [REQ-014], [REQ-015], [DAT-007], [NFR-003]. Sử dụng @Transactional cho các thao tác ghi và @Valid cho validation.",
                    "targeted_tags": [
                        "[REQ-014]",
                        "[REQ-015]",
                        "[DAT-007]",
                        "[NFR-003]"
                    ],
                    "components": [
                        "./sources/backend.membershiphub.attendance/studentcard-service.java"
                    ]
                }
            ]
        },
        {
            "day": 3,
            "context_file": ".ai/.plan/.context/phase-4.context.blueprint.md",
            "context_section": "NGÀY 9: VIẾT BỘ KIỂM TRA TÍCH HỢP CHO GHI DANH, ĐIỂM DANH, VÀ THẺ",
            "sub_tasks": [
                {
                    "id": "D3_ST1",
                    "agent": "Tester",
                    "desc": "Xây dựng bộ kiểm thử tích hợp cho EnrollmentService với các kịch bản sau:\n- Kiểm thử happy path cho ghi danh học viên và điểm danh QR.\n- Kiểm thử xử lý ngoại lệ network (mô phỏng lỗi kết nối cơ sở dữ liệu và retry mechanism).\n- Kiểm thử logic idempotent cho điểm danh QR (đảm bảo không có bản ghi trùng lặp khi quét cùng một mã QR nhiều lần).\n- Kiểm thử validation cho các trường hợp dữ liệu không hợp lệ (ví dụ: ghi danh vào khóa học không tồn tại, học viên không tồn tại).\n- Kiểm thử tích hợp với StudentCardService cho các kịch bản liên quan đến thẻ hội viên.\nSử dụng Testcontainers để thiết lập môi trường kiểm thử với cơ sở dữ liệu PostgreSQL thực tế. Đảm bảo độ phủ mã ≥85% và tất cả các yêu cầu [REQ-010], [REQ-011], [REQ-012], [REQ-013], [DAT-005], [DAT-006], [DAT-007], [ARC-007], [EXC-001], [EXC-002] được kiểm tra.",
                    "targeted_tags": [
                        "[REQ-010]",
                        "[REQ-011]",
                        "[REQ-012]",
                        "[REQ-013]",
                        "[DAT-005]",
                        "[DAT-006]",
                        "[DAT-007]",
                        "[ARC-007]",
                        "[EXC-001]",
                        "[EXC-002]"
                    ],
                    "components": [
                        "INTEGRATION_SCOPE;./sources/backend.membershiphub.attendance/enrollment-service.java",
                        "./sources/backend.membershiphub.attendance/enrollmentservice-integration-test.java"
                    ]
                },
                {
                    "id": "D3_ST2",
                    "agent": "Tester",
                    "desc": "Xây dựng bộ kiểm thử tích hợp cho StudentCardService với các kịch bản sau:\n- Kiểm thử happy path cho phát hành, gia hạn và thu hồi thẻ hội viên.\n- Kiểm thử validation cho các trường hợp dữ liệu không hợp lệ (ví dụ: gia hạn thẻ không tồn tại, thu hồi thẻ đã bị thu hồi).\n- Kiểm thử tích hợp với EnrollmentService cho các kịch bản liên quan đến ghi danh và điểm danh.\nSử dụng Testcontainers để thiết lập môi trường kiểm thử với cơ sở dữ liệu PostgreSQL thực tế. Đảm bảo độ phủ mã ≥85% và tất cả các yêu cầu [REQ-014], [REQ-015], [DAT-007], [NFR-003] được kiểm tra.",
                    "targeted_tags": [
                        "[REQ-014]",
                        "[REQ-015]",
                        "[DAT-007]",
                        "[NFR-003]"
                    ],
                    "components": [
                        "INTEGRATION_SCOPE;./sources/backend.membershiphub.attendance/studentcard-service.java",
                        "./sources/backend.membershiphub.attendance/studentcardservice-integration-test.java"
                    ]
                },
                {
                    "id": "D3_ST3",
                    "agent": "Doc",
                    "desc": "Biên soạn tài liệu kỹ thuật cho module ghi danh và điểm danh bao gồm:\n- API documentation với OpenAPI/Swagger cho tất cả các endpoint: `GET /api/v1/courses/browse`, `POST /api/v1/enrollments`, `POST /api/v1/attendance/scan`, `GET /api/v1/studentcards/{studentId}`, `POST /api/v1/studentcards/{studentId}/renew`.\n- Schema documentation cho các bảng Enrollments, Attendance, StudentCards với mô tả chi tiết từng trường, ràng buộc và chỉ mục.\n- Hướng dẫn triển khai module bao gồm cấu hình cơ sở dữ liệu, biến môi trường và các bước khởi động dịch vụ.\n- Tài liệu về cơ chế xử lý ngoại lệ network và logic idempotent cho điểm danh QR.",
                    "targeted_tags": [
                        "[REQ-010]",
                        "[REQ-011]",
                        "[REQ-012]",
                        "[REQ-013]",
                        "[REQ-014]",
                        "[REQ-015]",
                        "[DAT-005]",
                        "[DAT-006]",
                        "[DAT-007]"
                    ],
                    "components": [
                        ".ai/.plan/.context/phase-4.context.blueprint.md"
                    ]
                }
            ]
        }
    ],
    "phase_idx": 4,
    "phase_context_file": ".ai/.plan/.context/phase-4.context.blueprint.md"
}```
-------------------------------------------------
