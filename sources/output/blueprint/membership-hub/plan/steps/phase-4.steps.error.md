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
          "desc": "Triển khai schema cơ sở dữ liệu cho bảng Enrollments với các trường: `enrollment_id` (UUID, PK), `student_id` (UUID, FK), `course_id` (UUID, FK), `enrollment_date` (TIMESTAMP), `status` (ENUM: ACTIVE, CANCELLED, COMPLETED), `created_at` (TIMESTAMP), `updated_at` (TIMESTAMP). Áp dụng các ràng buộc toàn vẹn dữ liệu: `student_id` và `course_id` không được trùng lặp cho cùng một học viên trong cùng một khóa học (UNIQUE constraint). Đảm bảo schema tuân thủ [DAT-005].",
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
          "desc": "Triển khai schema cơ sở dữ liệu cho bảng Attendance với các trường: `attendance_id` (UUID, PK), `enrollment_id` (UUID, FK), `scan_time` (TIMESTAMP), `qr_code_hash` (VARCHAR, UNIQUE), `location_id` (UUID), `status` (ENUM: PRESENT, ABSENT, LATE), `created_at` (TIMESTAMP). Áp dụng ràng buộc idempotent: `qr_code_hash` phải là duy nhất để ngăn chặn duplicate scans. Đảm bảo schema tuân thủ [DAT-006].",
          "targeted_tags": [
            "[DAT-006]"
          ],
          "components": [
            "./sources/backend.membershiphub.attendance/attendances.sql"
          ]
        },
        {
          "id": "D1_ST3",
          "agent": "Coder",
          "desc": "Triển khai schema cơ sở dữ liệu cho bảng StudentCards với các trường: `card_id` (UUID, PK), `student_id` (UUID, FK), `card_number` (VARCHAR, UNIQUE), `issue_date` (DATE), `expiry_date` (DATE), `status` (ENUM: ACTIVE, EXPIRED, REVOKED), `created_at` (TIMESTAMP), `updated_at` (TIMESTAMP). Áp dụng ràng buộc: `expiry_date` phải lớn hơn `issue_date`. Đảm bảo schema tuân thủ [DAT-007].",
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
          "desc": "Triển khai `EnrollmentService` với các phương thức sau:\n- `enrollStudent(UUID studentId, UUID courseId)`: Ghi danh học viên vào khóa học với validation nghiêm ngặt (kiểm tra học viên đã tồn tại, khóa học còn chỗ, học viên chưa ghi danh). Sử dụng `@Transactional` để đảm bảo tính toàn vẹn dữ liệu.\n- `scanQRCode(UUID enrollmentId, String qrCodeHash, UUID locationId)`: Xử lý điểm danh QR với logic idempotent (kiểm tra `qrCodeHash` đã tồn tại trước khi tạo bản ghi mới). Ném ngoại lệ `DuplicateScanException` nếu phát hiện duplicate scan.\n- `handleNetworkException(Exception ex)`: Xử lý ngoại lệ network bằng cách retry tối đa 3 lần với khoảng thời gian chờ 1 giây giữa các lần retry. Nếu thất bại, ghi log lỗi và ném `NetworkException`.\nĐảm bảo tất cả các phương thức tuân thủ [REQ-010], [REQ-011], [REQ-012], [REQ-013], [EXC-001], [EXC-002], [NFR-001], [NFR-003].",
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
          "desc": "Triển khai `StudentCardService` với các phương thức sau:\n- `getStudentCard(UUID studentId)`: Lấy thông tin thẻ hội viên của học viên, bao gồm trạng thái thẻ và ngày hết hạn. Ném ngoại lệ `StudentCardNotFoundException` nếu không tìm thấy thẻ.\n- `renewStudentCard(UUID studentId, LocalDate newExpiryDate)`: Gia hạn thẻ hội viên với validation nghiêm ngặt (kiểm tra thẻ còn hiệu lực, `newExpiryDate` phải lớn hơn ngày hết hạn hiện tại). Sử dụng `@Transactional` để đảm bảo tính toàn vẹn dữ liệu.\n- `revokeStudentCard(UUID studentId)`: Thu hồi thẻ hội viên và cập nhật trạng thái thành `REVOKED`.\nĐảm bảo tất cả các phương thức tuân thủ [REQ-014], [REQ-015], [NFR-003].",
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
          "desc": "Xây dựng bộ kiểm thử tích hợp cho `EnrollmentService` và `StudentCardService` với các kịch bản sau:\n- **Kiểm thử ghi danh học viên**: Đảm bảo học viên có thể ghi danh vào khóa học, kiểm tra validation (học viên đã tồn tại, khóa học còn chỗ).\n- **Kiểm thử điểm danh QR idempotent**: Đảm bảo không có bản ghi trùng lặp khi quét cùng một mã QR nhiều lần. Sử dụng `Testcontainers` để mô phỏng cơ sở dữ liệu.\n- **Kiểm thử xử lý ngoại lệ network**: Mô phỏng lỗi network và kiểm tra cơ chế retry (tối đa 3 lần).\n- **Kiểm thử quản lý thẻ hội viên**: Đảm bảo thẻ có thể được gia hạn và thu hồi, kiểm tra validation cho ngày hết hạn.\n- **Kiểm thử duplicate scans**: Đảm bảo hệ thống ném `DuplicateScanException` khi phát hiện duplicate scan.\nĐảm bảo độ phủ mã ≥85% và tuân thủ [REQ-010], [REQ-011], [REQ-012], [REQ-013], [EXC-001], [EXC-002].",
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
            "INTEGRATION_SCOPE;./sources/backend.membershiphub.attendance/enrollmentservice-integration-test.java"
          ]
        },
        {
          "id": "D3_ST2",
          "agent": "Doc",
          "desc": "Biên soạn tài liệu kỹ thuật cho module ghi danh và điểm danh, bao gồm:\n- **API Documentation**: Tài liệu OpenAPI cho các endpoint `POST /api/v1/enrollments`, `POST /api/v1/attendance/scan`, `GET /api/v1/studentcards/{studentId}`, `POST /api/v1/studentcards/{studentId}/renew`. Bao gồm request/response payload schemas, error status codes, và ví dụ.\n- **Schema Documentation**: Tài liệu chi tiết về các bảng `Enrollments`, `Attendance`, `StudentCards` với các trường, ràng buộc, và mối quan hệ.\n- **Hướng dẫn triển khai**: Hướng dẫn chi tiết về cách triển khai module, bao gồm cấu hình cơ sở dữ liệu, biến môi trường, và các bước khởi động dịch vụ.",
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
                    "desc": "Triển khai schema cơ sở dữ liệu cho bảng Enrollments với các trường: `enrollment_id` (UUID, PK), `student_id` (UUID, FK), `course_id` (UUID, FK), `enrollment_date` (TIMESTAMP), `status` (ENUM: ACTIVE, CANCELLED, COMPLETED), `created_at` (TIMESTAMP), `updated_at` (TIMESTAMP). Áp dụng các ràng buộc toàn vẹn dữ liệu: `student_id` và `course_id` không được trùng lặp cho cùng một học viên trong cùng một khóa học (UNIQUE constraint). Đảm bảo schema tuân thủ [DAT-005].",
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
                    "desc": "Triển khai schema cơ sở dữ liệu cho bảng Attendance với các trường: `attendance_id` (UUID, PK), `enrollment_id` (UUID, FK), `scan_time` (TIMESTAMP), `qr_code_hash` (VARCHAR, UNIQUE), `location_id` (UUID), `status` (ENUM: PRESENT, ABSENT, LATE), `created_at` (TIMESTAMP). Áp dụng ràng buộc idempotent: `qr_code_hash` phải là duy nhất để ngăn chặn duplicate scans. Đảm bảo schema tuân thủ [DAT-006].",
                    "targeted_tags": [
                        "[DAT-006]"
                    ],
                    "components": [
                        "./sources/backend.membershiphub.attendance/attendances.sql"
                    ]
                },
                {
                    "id": "D1_ST3",
                    "agent": "Coder",
                    "desc": "Triển khai schema cơ sở dữ liệu cho bảng StudentCards với các trường: `card_id` (UUID, PK), `student_id` (UUID, FK), `card_number` (VARCHAR, UNIQUE), `issue_date` (DATE), `expiry_date` (DATE), `status` (ENUM: ACTIVE, EXPIRED, REVOKED), `created_at` (TIMESTAMP), `updated_at` (TIMESTAMP). Áp dụng ràng buộc: `expiry_date` phải lớn hơn `issue_date`. Đảm bảo schema tuân thủ [DAT-007].",
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
                    "desc": "Triển khai `EnrollmentService` với các phương thức sau:\n- `enrollStudent(UUID studentId, UUID courseId)`: Ghi danh học viên vào khóa học với validation nghiêm ngặt (kiểm tra học viên đã tồn tại, khóa học còn chỗ, học viên chưa ghi danh). Sử dụng `@Transactional` để đảm bảo tính toàn vẹn dữ liệu.\n- `scanQRCode(UUID enrollmentId, String qrCodeHash, UUID locationId)`: Xử lý điểm danh QR với logic idempotent (kiểm tra `qrCodeHash` đã tồn tại trước khi tạo bản ghi mới). Ném ngoại lệ `DuplicateScanException` nếu phát hiện duplicate scan.\n- `handleNetworkException(Exception ex)`: Xử lý ngoại lệ network bằng cách retry tối đa 3 lần với khoảng thời gian chờ 1 giây giữa các lần retry. Nếu thất bại, ghi log lỗi và ném `NetworkException`.\nĐảm bảo tất cả các phương thức tuân thủ [REQ-010], [REQ-011], [REQ-012], [REQ-013], [EXC-001], [EXC-002], [NFR-001], [NFR-003].",
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
                    "desc": "Triển khai `StudentCardService` với các phương thức sau:\n- `getStudentCard(UUID studentId)`: Lấy thông tin thẻ hội viên của học viên, bao gồm trạng thái thẻ và ngày hết hạn. Ném ngoại lệ `StudentCardNotFoundException` nếu không tìm thấy thẻ.\n- `renewStudentCard(UUID studentId, LocalDate newExpiryDate)`: Gia hạn thẻ hội viên với validation nghiêm ngặt (kiểm tra thẻ còn hiệu lực, `newExpiryDate` phải lớn hơn ngày hết hạn hiện tại). Sử dụng `@Transactional` để đảm bảo tính toàn vẹn dữ liệu.\n- `revokeStudentCard(UUID studentId)`: Thu hồi thẻ hội viên và cập nhật trạng thái thành `REVOKED`.\nĐảm bảo tất cả các phương thức tuân thủ [REQ-014], [REQ-015], [NFR-003].",
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
                    "desc": "Xây dựng bộ kiểm thử tích hợp cho `EnrollmentService` và `StudentCardService` với các kịch bản sau:\n- **Kiểm thử ghi danh học viên**: Đảm bảo học viên có thể ghi danh vào khóa học, kiểm tra validation (học viên đã tồn tại, khóa học còn chỗ).\n- **Kiểm thử điểm danh QR idempotent**: Đảm bảo không có bản ghi trùng lặp khi quét cùng một mã QR nhiều lần. Sử dụng `Testcontainers` để mô phỏng cơ sở dữ liệu.\n- **Kiểm thử xử lý ngoại lệ network**: Mô phỏng lỗi network và kiểm tra cơ chế retry (tối đa 3 lần).\n- **Kiểm thử quản lý thẻ hội viên**: Đảm bảo thẻ có thể được gia hạn và thu hồi, kiểm tra validation cho ngày hết hạn.\n- **Kiểm thử duplicate scans**: Đảm bảo hệ thống ném `DuplicateScanException` khi phát hiện duplicate scan.\nĐảm bảo độ phủ mã ≥85% và tuân thủ [REQ-010], [REQ-011], [REQ-012], [REQ-013], [EXC-001], [EXC-002].",
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
                        "INTEGRATION_SCOPE;./sources/backend.membershiphub.attendance/enrollmentservice-integration-test.java"
                    ]
                },
                {
                    "id": "D3_ST2",
                    "agent": "Doc",
                    "desc": "Biên soạn tài liệu kỹ thuật cho module ghi danh và điểm danh, bao gồm:\n- **API Documentation**: Tài liệu OpenAPI cho các endpoint `POST /api/v1/enrollments`, `POST /api/v1/attendance/scan`, `GET /api/v1/studentcards/{studentId}`, `POST /api/v1/studentcards/{studentId}/renew`. Bao gồm request/response payload schemas, error status codes, và ví dụ.\n- **Schema Documentation**: Tài liệu chi tiết về các bảng `Enrollments`, `Attendance`, `StudentCards` với các trường, ràng buộc, và mối quan hệ.\n- **Hướng dẫn triển khai**: Hướng dẫn chi tiết về cách triển khai module, bao gồm cấu hình cơ sở dữ liệu, biến môi trường, và các bước khởi động dịch vụ.",
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
