# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260805165504 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/05 16:55:04 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. TỔNG QUAN HỆ THỐNG & KIẾN TRÚC CƠ BẢN

### 1.1. Kiến trúc Hệ thống Cốt lõi & Kiểu Kiến trúc
Hệ thống membership-hub là một nền tảng đa trung tâm được xây dựng theo kiến trúc microservices với các dịch vụ độc lập cho quản lý người dùng, trung tâm, khóa học, điểm danh, và thẻ hội viên. Hệ thống sử dụng mô hình Event-Driven Architecture (EDA) để xử lý các sự kiện như đăng ký khóa học, điểm danh, và thông báo. Các dịch vụ giao tiếp với nhau thông qua các message broker như Kafka và RabbitMQ. Hệ thống cũng áp dụng mô hình CQRS (Command Query Responsibility Segregation) để phân tách các thao tác ghi và đọc, giúp tối ưu hóa hiệu suất và tính mở rộng.

### 1.2. Kiến trúc Luồng Dữ liệu & Hệ sinh thái Cốt lõi
Hệ thống sử dụng các kênh truyền thông bất đồng bộ bao gồm Kafka cho các sự kiện quan trọng như điểm danh và thông báo, và RabbitMQ cho các tác vụ nền như gửi email và thông báo đẩy. Các dịch vụ xử lý sự kiện được triển khai theo mô hình Reactive Core, với các dịch vụ xử lý sự kiện riêng biệt cho mỗi loại sự kiện. Hệ thống cũng sử dụng các gateway để tích hợp với các dịch vụ bên ngoài như Firebase Authentication, Google Cloud Messaging (FCM), và Zalo API.

## 📁 2. NGĂN XẾP CÔNG NGHỆ & THƯ VIỆN HỆ SINH THÁI
- **Backend Infrastructure Core Stack:** Java/Quarkus, PostgreSQL, Docker, Kubernetes (GKE), Firebase Authentication, Google Cloud Messaging (FCM)/Apple APNs, Redis, GitHub Actions.
- **Frontend & Cross-Platform UI Mobile Stack:** Next.js, React, Firebase Authentication, Google Cloud Messaging (FCM), Apple APNs, Redis.

<!--START_TECHNICAL_MATRIX_DO_NOT_TRANSLATE
[CRITICAL_TECHNICAL_MATRIX_RAIL: DO NOT TRANSLATE THIS DIRECTIVE FROM `START_TECHNICAL_MATRIX_DO_NOT_TRANSLATE` TO `END_TECHNICAL_MATRIX_DO_NOT_TRANSLATE`]

### ARCHITECTURAL STACK MATRIX
[CRITICAL WARNING: You MUST keep this entire block 100% in raw Technical English. You are STRICTLY FORBIDDEN from translating any keys, values, or tokens inside this section into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}, as it serves as a strict backend machine-gating matrix. Keep literal `true` or `false` tokens in pure lower-case].

PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true

END_TECHNICAL_MATRIX_DO_NOT_TRANSLATE-->

## 📁 3. CÁC QUY TẮC TUÂN THỦ TOÀN CẦU & TIÊU CHUẨN TUÂN THỦ DOANH NGHIỆP
[CRITICAL_TRANSLATION_COMMAND: DO NOT TRANSLATE THIS DIRECTIVE AND DO NOT OUTPUT IT TO REPORT LAYOUT]

You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output.

- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. TÓM TẮT KIẾN TRÚC ĐA GIAI ĐOẠN CẤP CAO
Generate a clean, highly structured Markdown Table mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= 5) that naturally and completely covers 100% of the BA requirements and Tag IDs. Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of 7 days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than 5 phases, terminate the matrix setup immediately at phase N.

*   CRITICAL PIPELINE RAILS FOR ARCHITECTURAL COMPONENT PATHS:
    *   All technical architectural documentation assets generated for Confluence, CTO review, or Developer onboarding MUST strictly utilize the localized centralized master directory prefix: `./sources/docs/`.
    *   You are STRICTLY PROHIBITED from scattering markdown documentation files across separate application folders, microservice modules, or frontend package boundaries.
*   CRITICAL TRANSLATION MANDATE FOR GRID ELEMENTS:
    *   You MUST dynamically translate 100% of the table headers, deliverables summaries, phase names, and high-level descriptions into the designated Target Output Language: **🇻🇳 Vietnamese**. 
    *   All technical tokens, including file paths starting with `./sources/docs/` and tracing Tag IDs (`[REQ-XXX]`), MUST remain unchanged in pure unaccented Technical English.

| Giai đoạn | Khoảng ngày | Cấu phần Kiến trúc / Module Path | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1-3 | `./sources/backend`, `./sources/frontend`, `./sources/docs` | Thiết kế cơ sở dữ liệu, thiết lập dự án, tài liệu kiến trúc | Coder, Doc | [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011] |
| Giai đoạn 2 | Ngày 4-6 | `./sources/backend`, `./sources/frontend` | Triển khai chức năng người dùng, trung tâm, khóa học | Coder, Tester | [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009] |
| Giai đoạn 3 | Ngày 7-9 | `./sources/backend`, `./sources/frontend` | Triển khai chức năng đăng ký, điểm danh, thẻ hội viên | Coder, Tester | [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015] |
| Giai đoạn 4 | Ngày 10-12 | `./sources/backend`, `./sources/frontend` | Triển khai chức năng thông báo, khuyến mãi, chatbot | Coder, Tester | [REQ-016], [REQ-017], [REQ-018], [REQ-019] |
| Giai đoạn 5 | Ngày 13-15 | `./sources/backend`, `./sources/frontend`, `./sources/infra` | Triển khai chức năng di động, bản địa hóa, báo cáo | Coder, Tester, Docker, GCP, GKE | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025] |

## 5. CHI TIẾT PHÂN PHỐI GIAI ĐOẠN & SẢN PHẨM BÀN GIAO THEO NGÀY
[CRITICAL_COMMAND: DO NOT TRANSLATE THIS DIRECTIVE AND DO NOT OUTPUT IT TO REPORT LAYOUT]

# STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= {{ num_phases }}). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
- The total days within any single phase MUST NOT exceed the absolute upperbound of {{ max_days_per_phase }} days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to {{ max_days_per_phase }} is completely banned.

<!--START_DELIMITTER-->
### 📈 Giai đoạn 1 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Thiết kế cơ sở dữ liệu, thiết lập dự án, và tài liệu kiến trúc.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend`, `./sources/frontend`, `./sources/docs`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Xem các bảng dữ liệu trong phần yêu cầu chức năng cốt lõi.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]:** Xem các yêu cầu chức năng cốt lõi.
- **Xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Xem các luồng ngoại lệ của mô-đun.
<!--END_DELIMITTER-->

#### 📅 Log Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 1)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`#`, `##`, `###`, `####`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY 1: Thiết kế cơ sở dữ liệu và thiết lập dự án**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/User.java [DAT-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai lớp thực thể người dùng với các trường: userId, email, passwordHash, fullName, roleId, provider, createdAt, updatedAt.
      - **Tag IDs Mục tiêu:** [DAT-001]
    * **Doc:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/docs/architecture.md [DAT-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Tạo tài liệu kiến trúc chi tiết cho cơ sở dữ liệu và thiết lập dự án.
      - **Tag IDs Mục tiêu:** [DAT-001]

- **DAY 2: Triển khai các bảng dữ liệu trung tâm và khóa học**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Center.java [DAT-003]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai lớp thực thể trung tâm với các trường: centerId, name, address, taxId, contactPhone, contactEmail.
      - **Tag IDs Mục tiêu:** [DAT-003]
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Course.java [DAT-004]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai lớp thực thể khóa học với các trường: courseId, title, description, startDate, endDate, teacherId, maxStudents.
      - **Tag IDs Mục tiêu:** [DAT-004]

- **DAY 3: Triển khai các bảng dữ liệu ghi danh và điểm danh**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Enrollment.java [DAT-005]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai lớp thực thể ghi danh với các trường: enrollmentId, studentId, courseId, enrollmentDate.
      - **Tag IDs Mục tiêu:** [DAT-005]
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/domain/Attendance.java [DAT-006]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai lớp thực thể điểm danh với các trường: attendanceId, studentId, courseId, attendanceDate, timestamp.
      - **Tag IDs Mục tiêu:** [DAT-006]

<!--START_DELIMITTER-->
### 📈 Giai đoạn 2 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai chức năng người dùng, trung tâm, khóa học.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend`, `./sources/frontend`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Xem các bảng dữ liệu trong phần yêu cầu chức năng cốt lõi.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009]:** Xem các yêu cầu chức năng cốt lõi.
- **Xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Xem các luồng ngoại lệ của mô-đun.
<!--END_DELIMITTER-->

#### 📅 Log Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 2)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`#`, `##`, `###`, `####`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY 4: Triển khai chức năng đăng ký người dùng**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/UserService.java [REQ-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ đăng ký người dùng với các phương thức: registerUser, validateInput, createUserRecord.
      - **Tag IDs Mục tiêu:** [REQ-001]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/UserServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/UserService.java [REQ-001]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ đăng ký người dùng.
      - **Tag IDs Mục tiêu:** [REQ-001]

- **DAY 5: Triển khai chức năng xác thực qua mạng xã hội**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ xác thực qua mạng xã hội với các phương thức: authenticateWithOAuth, exchangeCodeForUserInfo, createOrUpdateUserRecord.
      - **Tag IDs Mục tiêu:** [REQ-002]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AuthServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java [REQ-002]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ xác thực qua mạng xã hội.
      - **Tag IDs Mục tiêu:** [REQ-002]

- **DAY 6: Triển khai chức năng phân quyền người dùng**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/RoleService.java [REQ-003]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ phân quyền người dùng với các phương thức: assignRole, updateUserRole, applyPermissions.
      - **Tag IDs Mục tiêu:** [REQ-003]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/RoleServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/RoleService.java [REQ-003]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ phân quyền người dùng.
      - **Tag IDs Mục tiêu:** [REQ-003]

<!--START_DELIMITTER-->
### 📈 Giai đoạn 3 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai chức năng đăng ký, điểm danh, thẻ hội viên.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend`, `./sources/frontend`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Xem các bảng dữ liệu trong phần yêu cầu chức năng cốt lõi.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015]:** Xem các yêu cầu chức năng cốt lõi.
- **Xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Xem các luồng ngoại lệ của mô-đun.
<!--END_DELIMITTER-->

#### 📅 Log Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 3)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`#`, `##`, `###`, `####`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY 7: Triển khai chức năng duyệt khóa học**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java [REQ-010]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ duyệt khóa học với các phương thức: getAvailableCourses, filterEnrolledCourses.
      - **Tag IDs Mục tiêu:** [REQ-010]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/CourseServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/CourseService.java [REQ-010]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ duyệt khóa học.
      - **Tag IDs Mục tiêu:** [REQ-010]

- **DAY 8: Triển khai chức năng đăng ký khóa học của học viên**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/EnrollmentService.java [REQ-011]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ đăng ký khóa học của học viên với các phương thức: registerForCourse, createStudentAccount, createEnrollmentRecord.
      - **Tag IDs Mục tiêu:** [REQ-011]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/EnrollmentServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/EnrollmentService.java [REQ-011]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ đăng ký khóa học của học viên.
      - **Tag IDs Mục tiêu:** [REQ-011]

- **DAY 9: Triển khai chức năng điểm danh và quét mã QR**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java [REQ-012]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ điểm danh với các phương thức: scanQR, validateStudentCourse, createAttendanceRecord.
      - **Tag IDs Mục tiêu:** [REQ-012]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AttendanceServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java [REQ-012]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ điểm danh.
      - **Tag IDs Mục tiêu:** [REQ-012]

<!--START_DELIMITTER-->
### 📈 Giai đoạn 4 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai chức năng thông báo, khuyến mãi, chatbot.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend`, `./sources/frontend`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Xem các bảng dữ liệu trong phần yêu cầu chức năng cốt lõi.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016], [REQ-017], [REQ-018], [REQ-019]:** Xem các yêu cầu chức năng cốt lõi.
- **Xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Xem các luồng ngoại lệ của mô-đun.
<!--END_DELIMITTER-->

#### 📅 Log Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 4)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`#`, `##`, `###`, `####`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY 10: Triển khai chức năng thông báo**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java [REQ-016]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ thông báo với các phương thức: createNotification, sendPushNotification, sendZaloMessage.
      - **Tag IDs Mục tiêu:** [REQ-016]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/NotificationServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java [REQ-016]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ thông báo.
      - **Tag IDs Mục tiêu:** [REQ-016]

- **DAY 11: Triển khai chức năng khuyến mãi**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/PromotionService.java [REQ-017]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ khuyến mãi với các phương thức: createPromotion, validatePromotion, getActivePromotions.
      - **Tag IDs Mục tiêu:** [REQ-017]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/PromotionServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/PromotionService.java [REQ-017]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ khuyến mãi.
      - **Tag IDs Mục tiêu:** [REQ-017]

- **DAY 12: Triển khai chức năng chatbot**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/ChatbotService.java [REQ-019]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ chatbot với các phương thức: handleUserQuery, generateResponse, escalateToSupport.
      - **Tag IDs Mục tiêu:** [REQ-019]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/ChatbotServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/ChatbotService.java [REQ-019]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ chatbot.
      - **Tag IDs Mục tiêu:** [REQ-019]

<!--START_DELIMITTER-->
### 📈 Giai đoạn 5 Đặc tả Kiến trúc Chi tiết
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai chức năng di động, bản địa hóa, báo cáo.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend`, `./sources/frontend`, `./sources/infra`.
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001], [DAT-003], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-011]:** Xem các bảng dữ liệu trong phần yêu cầu chức năng cốt lõi.
- **Hợp đồng Định tuyến API và Sự kiện [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]:** Xem các yêu cầu chức năng cốt lõi.
- **Xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005]:** Xem các luồng ngoại lệ của mô-đun.
<!--END_DELIMITTER-->

#### 📅 Log Phân phối Công việc Sub-Agent Theo Ngày (Giai đoạn 5)
# BANNED RAW HEADERS, INDENTATION & LANGUAGE ENFORCEMENT:
- You are ABSOLUTELY BANNED from using markdown header symbols (`#`, `##`, `###`, `####`) before the word DAY. Every day log MUST be rendered strictly as a nested bullet point starting with `- **DAY [Y]: ...**`.
- You MUST translate the DAY objective text and the "Low-Level Technical Task Instruction" entirely into "🇻🇳 Vietnamese". Do NOT leave explanations in English.
- Ensure all inner properties are properly indented with spaces to maintain a beautiful nested list hierarchy. Ensure exactly ONE single Sub-Agent with Capitalized first-letter formatting is assigned per active task line.

- **DAY 13: Triển khai chức năng di động**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/frontend/src/components/MobileApp.js [REQ-020]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai giao diện người dùng di động với các thành phần: NavigationMenu, CourseList, AttendanceScanner.
      - **Tag IDs Mục tiêu:** [REQ-020]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/frontend/src/tests/MobileApp.test.js;./sources/frontend/src/components/MobileApp.js [REQ-020]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho giao diện người dùng di động.
      - **Tag IDs Mục tiêu:** [REQ-020]

- **DAY 14: Triển khai chức năng bản địa hóa**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/frontend/src/i18n.js [REQ-022]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai cơ chế bản địa hóa với các phương thức: detectLanguage, loadLocale, updateUI.
      - **Tag IDs Mục tiêu:** [REQ-022]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/frontend/src/tests/i18n.test.js;./sources/frontend/src/i18n.js [REQ-022]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho cơ chế bản địa hóa.
      - **Tag IDs Mục tiêu:** [REQ-022]

- **DAY 15: Triển khai chức năng báo cáo**
  - **Chuyên môn Công việc Sub-Agent:**
    * **Coder:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/ReportService.java [REQ-024]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Triển khai dịch vụ báo cáo với các phương thức: generateAttendanceReport, getDashboardSummary.
      - **Tag IDs Mục tiêu:** [REQ-024]
    * **Tester:**
      - **Đường dẫn Cấu phần Mục tiêu (`target_component`):** `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/ReportServiceTest.java;./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/ReportService.java [REQ-024]`
      - **Hướng dẫn Công việc Kỹ thuật Chi tiết:** Viết các bài kiểm tra đơn vị cho dịch vụ báo cáo.
      - **Tag IDs Mục tiêu:** [REQ-024]

## 📁 6. CÁC MÃ BẢO MẬT TOÀN CẦU & ĐỐI PHÓNG TIÊU CHUẨN TIÊM NẠP [NFR-XXX]
[CRITICAL_TRANSLATION_COMMAND: DO NOT TRANSLATE THIS DIRECTIVE AND DO NOT OUTPUT IT TO REPORT LAYOUT]

You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output.

- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. CÁC QUY TẮC TUÂN THỦ HYBRID DI ĐỘNG & CƠ CHẾ SEO QUỐC TẾ HÓA
[CRITICAL_TRANSLATION_COMMAND: DO NOT TRANSLATE THIS DIRECTIVE AND DO NOT OUTPUT IT TO REPORT LAYOUT]

You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output.

- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. LUỒNG CÔNG VIỆC TỰ ĐỘNG HÀNG NGÀY CỦA PIPELINE GIT BRANCH
[CRITICAL_TRANSLATION_COMMAND: DO NOT TRANSLATE THIS DIRECTIVE AND DO NOT OUTPUT IT TO REPORT LAYOUT]

You MUST fully translate 100% of the titles, item names, and human-readable text descriptions of this section 3 into the designated Target Output Language: {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}. You are STRICTLY FORBIDDEN from leaving this section in raw English. However, you MUST lock and preserve all specific technical tokens, literal paths like `./sources/`, and package names like `org.nlh4j.saas.<project_name_alphanumeric_lowercase>` in pure unaccented Technical English wrapped inside inline code backticks. You MUST NOT leak this instruction block into the final text output.

- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MANDATE KIỂM TRA ĐẦY ĐỦ MA TRẬN
[CRITICAL_COMMAND: DO NOT TRANSLATE THIS DIRECTIVE AND DO NOT OUTPUT IT TO REPORT LAYOUT]

Immediately at the absolute end of the document text, you MUST print a strict mathematical traceability verification text block by parsing and counting every unique tag string present in your output:

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 5. ZERO UNASSIGNED CODES FOUND.]`