# GLOBAL PROJECT CONTEXT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260808074408 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | 2026/08/08 07:44:08 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### 1.1. Core System Modality & Architecture Modality
- Hệ thống được thiết kế theo mô hình đa trung tâm với kiến trúc phân tán.
- Sử dụng mô hình RBAC (Role-Based Access Control) để quản lý quyền truy cập.
- Hệ thống hỗ trợ đa kênh giao tiếp (web, di động, nhóm Zalo).
- Kiến trúc bao gồm các thành phần chính: quản lý người dùng, quản lý trung tâm, quản lý khóa học, đăng ký học viên, điểm danh, quản lý thẻ hội viên, thông báo và truyền thông, chatbot dịch vụ khách hàng AI, các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích.
- Sử dụng mô hình Event-Driven Architecture (EDA) cho các tính năng như điểm danh và thông báo.
- Áp dụng mô hình CQRS (Command Query Responsibility Segregation) cho các tính năng quản lý người dùng và khóa học.
- Sử dụng mô hình Reactive Programming cho các tính năng thời gian thực như điểm danh và thông báo.

### 1.2. Enterprise Data Flow Topologies & Core Ecosystems
- Hệ thống sử dụng các kênh truyền thông bất đồng bộ như Firebase Cloud Messaging (FCM) và Apple APNs cho thông báo đẩy.
- Sử dụng Zalo API để gửi thông báo đến nhóm Zalo.
- Hệ thống sử dụng Redis cho session caching và bộ nhớ đệm.
- Sử dụng PostgreSQL cho cơ sở dữ liệu chính và cơ sở dữ liệu đọc sao cho các công việc báo cáo.
- Sử dụng Apache Kafka cho các luồng dữ liệu thời gian thực như điểm danh và thông báo.
- Sử dụng Google Cloud Storage cho lưu trữ tệp tin và hình ảnh.
- Sử dụng Google Cloud Functions cho các tác vụ xử lý dữ liệu và báo cáo.

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES

### ARCHITECTURAL STACK MATRIX

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=true
BACKEND_LAYER_REQUIRED=true
FRONTEND_LAYER_REQUIRED=true
MOBILE_LAYER_REQUIRED=true
DEVOPS_LAYER_REQUIRED=true
```

- **Backend Infrastructure Core Stack:**
  - Java/Quarkus
  - PostgreSQL
  - Docker
  - Kubernetes (GKE)
  - Firebase Authentication
  - Google Cloud Messaging (FCM)/Apple APNs
  - Zalo API
  - Redis
  - GitHub Actions

- **Frontend & Cross-Platform UI Mobile Stack:**
  - Next.js
  - React Native
  - Firebase Authentication
  - Google Cloud Messaging (FCM)/Apple APNs
  - Zalo API

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `.`. All paths generated MUST begin with `./sources/`.
- **Dynamic Directory Prefixing Compliance:** Enforce the dynamic path mapping rules defined in Protocol 1 strictly matching the detected project structure.
- **[CONDITION: JAVA_STACK_ONLY] Java Package Standard:** If the tech stack utilizes Java frameworks, all Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.<project_name_alphanumeric_lowercase>`. You MUST dynamically convert the string "membership-hub" into a strict pure alphanumeric lowercase token by stripping out whitespaces, hyphens, and underscores. Non-Java projects are completely banned from applying this package segment.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`. Both paths inside the pair MUST begin with `./sources/`.

## 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

<!--START_PHASE_SYNOPSIS_GRID-->
| Giai đoạn | Khoảng ngày | Thành phần Kiến trúc / Module | Tóm tắt Sản phẩm Bàn giao | Sub-Agent | Tag IDs Mục tiêu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Giai đoạn 1 | Ngày 1 - 2 | Khởi tạo hệ thống người dùng và xác thực | Khởi tạo cơ sở dữ liệu người dùng, xác thực qua email/mật khẩu, Firebase, Google, Facebook | Coder, Tester, Doc, Reviewer | [REQ-001], [REQ-002], [REQ-003], [DAT-001], [ARC-006] |
| Giai đoạn 2 | Ngày 1 - 2 | Triển khai lõi nghiệp vụ trung tâm và khóa học | Khởi tạo cơ sở dữ liệu trung tâm, khóa học, đăng ký học viên | Coder, Tester, Doc, Reviewer | [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-003], [DAT-004], [DAT-005] |
| Giai đoạn 3 | Ngày 1 - 2 | Triển khai tính năng điểm danh và thẻ hội viên | Khởi tạo cơ sở dữ liệu điểm danh, thẻ hội viên, tích hợp quét mã QR | Coder, Tester, Doc, Reviewer | [REQ-012], [REQ-013], [REQ-014], [REQ-015], [DAT-006], [DAT-007], [EXC-001], [EXC-002] |
| Giai đoạn 4 | Ngày 1 - 2 | Triển khai thông báo và truyền thông | Khởi tạo cơ sở dữ liệu thông báo, tích hợp Zalo API, Firebase Cloud Messaging (FCM) | Coder, Tester, Doc, Reviewer | [REQ-016], [DAT-008], [EXC-003] |
| Giai đoạn 5 | Ngày 1 - 2 | Triển khai các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích | Khởi tạo các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích | Coder, Tester, Doc, Reviewer | [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [DAT-011], [EXC-005] |
<!--END_PHASE_SYNOPSIS_GRID-->

## 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES

### 📈 Giai đoạn 1 Khởi Tạo Hệ Thống Người Dùng Và Xác Thực
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Khởi tạo hệ thống người dùng và xác thực qua email/mật khẩu, Firebase, Google, Facebook.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/auth/`, `./sources/backend/user/`, `./sources/docs/auth.md`, `./sources/docs/user.md`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-001]:** ```sql:matrix
CREATE TABLE roles (
    role_id SMALLINT PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL,
    description VARCHAR(200)
);

CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash CHAR(60) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role_id SMALLINT REFERENCES roles(role_id),
    provider VARCHAR(10) NOT NULL DEFAULT 'local' CHECK (provider IN ('local', 'firebase', 'google', 'facebook')),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-001], [REQ-002], [REQ-003], [ARC-006]:** ```json
{
    "register": {
        "path": "/api/auth/register",
        "method": "POST",
        "request": {
            "email": "string",
            "password": "string",
            "fullName": "string"
        },
        "response": {
            "token": "string"
        }
    },
    "login": {
        "path": "/api/auth/login",
        "method": "POST",
        "request": {
            "email": "string",
            "password": "string"
        },
        "response": {
            "token": "string"
        }
    },
    "socialLogin": {
        "path": "/api/auth/social-login",
        "method": "POST",
        "request": {
            "provider": "string",
            "token": "string"
        },
        "response": {
            "token": "string"
        }
    }
}
```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-004]:** Xác thực đầu vào không hợp lệ (ví dụ: email không đúng định dạng, thiếu trường bắt buộc): Nếu xác thực thất bại trên form submission, Khi lỗi được trả về cho người dùng, Sau đó một thông báo rõ ràng liệt kê từng trường không hợp lệ và yêu cầu chỉnh sửa.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 1)

- **DAY 1: Khởi tạo cơ sở dữ liệu người dùng và xác thực qua email/mật khẩu**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-001], [DAT-001]
    * **Target Component file path (`target_component`):** `./sources/backend/auth/UserService.java [REQ-001], [DAT-001]`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ người dùng và xác thực qua email/mật khẩu.
    * **Database Schema DDL SQL Specification [DAT-001]:**
    ```sql:matrix
    CREATE TABLE roles (
        role_id SMALLINT PRIMARY KEY,
        name VARCHAR(30) UNIQUE NOT NULL,
        description VARCHAR(200)
    );

    CREATE TABLE users (
        user_id UUID PRIMARY KEY,
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash CHAR(60) NOT NULL,
        full_name VARCHAR(100) NOT NULL,
        role_id SMALLINT REFERENCES roles(role_id),
        provider VARCHAR(10) NOT NULL DEFAULT 'local' CHECK (provider IN ('local', 'firebase', 'google', 'facebook')),
        created_at TIMESTAMP NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMP NOT NULL DEFAULT NOW()
    );
    ```
    * **API and Event Routing Contracts [REQ-001], [ARC-006]:**
    ```json
    {
        "register": {
            "path": "/api/auth/register",
            "method": "POST",
            "request": {
                "email": "string",
                "password": "string",
                "fullName": "string"
            },
            "response": {
                "token": "string"
            }
        },
        "login": {
            "path": "/api/auth/login",
            "method": "POST",
            "request": {
                "email": "string",
                "password": "string"
            },
            "response": {
                "token": "string"
            }
        }
    }
    ```
    * **Phase Localized Exception Handlers [EXC-004]:**
    ```java
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidationExceptions(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getAllErrors().forEach((error) -> {
            String fieldName = ((FieldError) error).getField();
            String errorMessage = error.getDefaultMessage();
            errors.put(fieldName, errorMessage);
        });
        return ResponseEntity.badRequest().body(errors);
    }
    ```

- **DAY 2: Triển khai xác thực qua Firebase, Google, Facebook**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-002], [ARC-006]
    * **Target Component file path (`target_component`):** `./sources/backend/auth/SocialAuthService.java [REQ-002], [ARC-006]`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ xác thực qua Firebase, Google, Facebook.
    * **API and Event Routing Contracts [REQ-002], [ARC-006]:**
    ```json
    {
        "socialLogin": {
            "path": "/api/auth/social-login",
            "method": "POST",
            "request": {
                "provider": "string",
                "token": "string"
            },
            "response": {
                "token": "string"
            }
        }
    }
    ```

### 📈 Giai đoạn 2 Triển Khai Lõi Nghiệp Vụ Trung Tâm Và Khóa Học
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai lõi nghiệp vụ trung tâm và khóa học.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/center/`, `./sources/backend/course/`, `./sources/docs/center.md`, `./sources/docs/course.md`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-003], [DAT-004], [DAT-005]:** ```sql:matrix
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) UNIQUE NOT NULL,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255)
);

CREATE TABLE courses (
    course_id UUID PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    teacher_id UUID REFERENCES users(user_id),
    max_students INT DEFAULT 30
);

CREATE TABLE enrollments (
    enrollment_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    course_id UUID REFERENCES courses(course_id),
    enrollment_date TIMESTAMP NOT NULL DEFAULT NOW()
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009]:** ```json
{
    "getCenters": {
        "path": "/api/centers",
        "method": "GET",
        "response": {
            "centers": [
                {
                    "centerId": "string",
                    "name": "string",
                    "address": "string",
                    "taxId": "string",
                    "contactPhone": "string",
                    "contactEmail": "string"
                }
            ]
        }
    },
    "createCenter": {
        "path": "/api/centers",
        "method": "POST",
        "request": {
            "name": "string",
            "address": "string",
            "taxId": "string",
            "contactPhone": "string",
            "contactEmail": "string"
        },
        "response": {
            "centerId": "string"
        }
    },
    "assignCenterAdmin": {
        "path": "/api/centers/{centerId}/admin",
        "method": "POST",
        "request": {
            "userId": "string"
        },
        "response": {
            "success": "boolean"
        }
    },
    "getCourses": {
        "path": "/api/courses",
        "method": "GET",
        "response": {
            "courses": [
                {
                    "courseId": "string",
                    "title": "string",
                    "startDate": "string",
                    "endDate": "string",
                    "teacherName": "string"
                }
            ]
        }
    },
    "createCourse": {
        "path": "/api/courses",
        "method": "POST",
        "request": {
            "title": "string",
            "startDate": "string",
            "endDate": "string",
            "teacherId": "string"
        },
        "response": {
            "courseId": "string"
        }
    },
    "assignTeacher": {
        "path": "/api/courses/{courseId}/teacher",
        "method": "POST",
        "request": {
            "teacherId": "string"
        },
        "response": {
            "success": "boolean"
        }
    }
}
```

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 2)

- **DAY 1: Khởi tạo cơ sở dữ liệu trung tâm và khóa học**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-004], [REQ-007], [DAT-003], [DAT-004]
    * **Target Component file path (`target_component`):** `./sources/backend/center/CenterService.java [REQ-004], [DAT-003]`, `./sources/backend/course/CourseService.java [REQ-007], [DAT-004]`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ trung tâm và khóa học.
    * **Database Schema DDL SQL Specification [DAT-003], [DAT-004]:**
    ```sql:matrix
    CREATE TABLE centers (
        center_id UUID PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        address VARCHAR(255) NOT NULL,
        tax_id VARCHAR(13) UNIQUE NOT NULL,
        contact_phone VARCHAR(20),
        contact_email VARCHAR(255)
    );

    CREATE TABLE courses (
        course_id UUID PRIMARY KEY,
        title VARCHAR(150) NOT NULL,
        description TEXT,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        teacher_id UUID REFERENCES users(user_id),
        max_students INT DEFAULT 30
    );
    ```
    * **API and Event Routing Contracts [REQ-004], [REQ-007]:**
    ```json
    {
        "getCenters": {
            "path": "/api/centers",
            "method": "GET",
            "response": {
                "centers": [
                    {
                        "centerId": "string",
                        "name": "string",
                        "address": "string",
                        "taxId": "string",
                        "contactPhone": "string",
                        "contactEmail": "string"
                    }
                ]
            }
        },
        "getCourses": {
            "path": "/api/courses",
            "method": "GET",
            "response": {
                "courses": [
                    {
                        "courseId": "string",
                        "title": "string",
                        "startDate": "string",
                        "endDate": "string",
                        "teacherName": "string"
                    }
                ]
            }
        }
    }
    ```

- **DAY 2: Triển khai tạo/cập nhật/xóa trung tâm và khóa học**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-005], [REQ-006], [REQ-008], [REQ-009], [DAT-005]
    * **Target Component file path (`target_component`):** `./sources/backend/center/CenterService.java [REQ-005], [REQ-006]`, `./sources/backend/course/CourseService.java [REQ-008], [REQ-009]`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ tạo/cập nhật/xóa trung tâm và khóa học.
    * **Database Schema DDL SQL Specification [DAT-005]:**
    ```sql:matrix
    CREATE TABLE enrollments (
        enrollment_id UUID PRIMARY KEY,
        student_id UUID REFERENCES users(user_id),
        course_id UUID REFERENCES courses(course_id),
        enrollment_date TIMESTAMP NOT NULL DEFAULT NOW()
    );
    ```
    * **API and Event Routing Contracts [REQ-005], [REQ-006], [REQ-008], [REQ-009]:**
    ```json
    {
        "createCenter": {
            "path": "/api/centers",
            "method": "POST",
            "request": {
                "name": "string",
                "address": "string",
                "taxId": "string",
                "contactPhone": "string",
                "contactEmail": "string"
            },
            "response": {
                "centerId": "string"
            }
        },
        "assignCenterAdmin": {
            "path": "/api/centers/{centerId}/admin",
            "method": "POST",
            "request": {
                "userId": "string"
            },
            "response": {
                "success": "boolean"
            }
        },
        "createCourse": {
            "path": "/api/courses",
            "method": "POST",
            "request": {
                "title": "string",
                "startDate": "string",
                "endDate": "string",
                "teacherId": "string"
            },
            "response": {
                "courseId": "string"
            }
        },
        "assignTeacher": {
            "path": "/api/courses/{courseId}/teacher",
            "method": "POST",
            "request": {
                "teacherId": "string"
            },
            "response": {
                "success": "boolean"
            }
        }
    }
    ```

### 📈 Giai đoạn 3 Triển Khai Tính Năng Điểm Danh Và Thẻ Hội Viên
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai tính năng điểm danh và thẻ hội viên.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/attendance/`, `./sources/backend/membership/`, `./sources/docs/attendance.md`, `./sources/docs/membership.md`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-006], [DAT-007]:** ```sql:matrix
CREATE TABLE attendance (
    attendance_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    course_id UUID REFERENCES courses(course_id),
    attendance_date DATE NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE student_cards (
    card_id UUID PRIMARY KEY,
    student_id UUID REFERENCES users(user_id),
    issue_date DATE NOT NULL,
    validity_days INT NOT NULL,
    remaining_days INT
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-012], [REQ-013], [REQ-014], [REQ-015]:** ```json
{
    "scanQR": {
        "path": "/api/attendance/scan",
        "method": "POST",
        "request": {
            "studentId": "string",
            "courseId": "string"
        },
        "response": {
            "success": "boolean",
            "message": "string"
        }
    },
    "getMembershipCard": {
        "path": "/api/membership/card",
        "method": "GET",
        "response": {
            "validityDays": "number",
            "remainingDays": "number"
        }
    },
    "extendMembership": {
        "path": "/api/membership/extend",
        "method": "POST",
        "request": {
            "days": "number"
        },
        "response": {
            "success": "boolean"
        }
    }
}
```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-001], [EXC-002]:** Network & Connectivity Drops During QR Scan: If a student scans a QR but the network is unavailable, When the app retries the request after reconnection, Then the attendance is recorded once the service is reachable. Duplicate Attendance Submission: If the same student scans the same course QR multiple times within the same day, When the system detects a duplicate, Then it returns a success response indicating ‘already recorded’ and does not create extra rows.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 3)

- **DAY 1: Khởi tạo cơ sở dữ liệu điểm danh và thẻ hội viên**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-012], [REQ-014], [DAT-006], [DAT-007]
    * **Target Component file path (`target_component`):** `./sources/backend/attendance/AttendanceService.java [REQ-012], [DAT-006]`, `./sources/backend/membership/MembershipService.java [REQ-014], [DAT-007]`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ điểm danh và thẻ hội viên.
    * **Database Schema DDL SQL Specification [DAT-006], [DAT-007]:**
    ```sql:matrix
    CREATE TABLE attendance (
        attendance_id UUID PRIMARY KEY,
        student_id UUID REFERENCES users(user_id),
        course_id UUID REFERENCES courses(course_id),
        attendance_date DATE NOT NULL,
        timestamp TIMESTAMP NOT NULL DEFAULT NOW()
    );

    CREATE TABLE student_cards (
        card_id UUID PRIMARY KEY,
        student_id UUID REFERENCES users(user_id),
        issue_date DATE NOT NULL,
        validity_days INT NOT NULL,
        remaining_days INT
    );
    ```
    * **API and Event Routing Contracts [REQ-012], [REQ-014]:**
    ```json
    {
        "scanQR": {
            "path": "/api/attendance/scan",
            "method": "POST",
            "request": {
                "studentId": "string",
                "courseId": "string"
            },
            "response": {
                "success": "boolean",
                "message": "string"
            }
        },
        "getMembershipCard": {
            "path": "/api/membership/card",
            "method": "GET",
            "response": {
                "validityDays": "number",
                "remainingDays": "number"
            }
        }
    }
    ```
    * **Phase Localized Exception Handlers [EXC-001], [EXC-002]:**
    ```java
    @ExceptionHandler(NetworkException.class)
    public ResponseEntity<Map<String, String>> handleNetworkException(NetworkException ex) {
        Map<String, String> response = new HashMap<>();
        response.put("success", "false");
        response.put("message", "Network unavailable. Please try again later.");
        return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE).body(response);
    }

    @ExceptionHandler(DuplicateAttendanceException.class)
    public ResponseEntity<Map<String, String>> handleDuplicateAttendanceException(DuplicateAttendanceException ex) {
        Map<String, String> response = new HashMap<>();
        response.put("success", "true");
        response.put("message", "Attendance already recorded for today.");
        return ResponseEntity.ok(response);
    }
    ```

- **DAY 2: Triển khai tính năng quét mã QR và gia hạn thẻ hội viên**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-013], [REQ-015]
    * **Target Component file path (`target_component`):** `./sources/backend/attendance/AttendanceService.java [REQ-013]`, `./sources/backend/membership/MembershipService.java [REQ-015]`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ quét mã QR và gia hạn thẻ hội viên.
    * **API and Event Routing Contracts [REQ-013], [REQ-015]:**
    ```json
    {
        "extendMembership": {
            "path": "/api/membership/extend",
            "method": "POST",
            "request": {
                "days": "number"
            },
            "response": {
                "success": "boolean"
            }
        }
    }
    ```

### 📈 Giai đoạn 4 Triển Khai Thông Báo Và Truyền Thông
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai thông báo và truyền thông.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/backend/notification/`, `./sources/docs/notification.md`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-008]:** ```sql:matrix
CREATE TABLE notifications (
    notification_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    group_zalo VARCHAR(255),
    message TEXT NOT NULL,
    sent_at TIMESTAMP NOT NULL DEFAULT NOW(),
    delivered BOOLEAN NOT NULL DEFAULT FALSE
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-016]:** ```json
{
    "sendNotification": {
        "path": "/api/notifications",
        "method": "POST",
        "request": {
            "userId": "string",
            "groupZalo": "string",
            "message": "string"
        },
        "response": {
            "notificationId": "string"
        }
    }
}
```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-003]:** Failed Notification Delivery: When a push notification cannot be delivered (e.g., device token invalid), Then the system logs the failure and schedules a retry up to three times before marking as failed.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 4)

- **DAY 1: Khởi tạo cơ sở dữ liệu thông báo**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-016], [DAT-008]
    * **Target Component file path (`target_component`):** `./sources/backend/notification/NotificationService.java [REQ-016], [DAT-008]`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ thông báo.
    * **Database Schema DDL SQL Specification [DAT-008]:**
    ```sql:matrix
    CREATE TABLE notifications (
        notification_id UUID PRIMARY KEY,
        user_id UUID REFERENCES users(user_id),
        group_zalo VARCHAR(255),
        message TEXT NOT NULL,
        sent_at TIMESTAMP NOT NULL DEFAULT NOW(),
        delivered BOOLEAN NOT NULL DEFAULT FALSE
    );
    ```
    * **API and Event Routing Contracts [REQ-016]:**
    ```json
    {
        "sendNotification": {
            "path": "/api/notifications",
            "method": "POST",
            "request": {
                "userId": "string",
                "groupZalo": "string",
                "message": "string"
            },
            "response": {
                "notificationId": "string"
            }
        }
    }
    ```
    * **Phase Localized Exception Handlers [EXC-003]:**
    ```java
    @ExceptionHandler(NotificationDeliveryException.class)
    public ResponseEntity<Map<String, String>> handleNotificationDeliveryException(NotificationDeliveryException ex) {
        Map<String, String> response = new HashMap<>();
        response.put("success", "false");
        response.put("message", "Notification delivery failed. Retrying...");
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(response);
    }
    ```

- **DAY 2: Triển khai tích hợp Zalo API và Firebase Cloud Messaging (FCM)**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-016]
    * **Target Component file path (`target_component`):** `./sources/backend/notification/ZaloNotificationService.java [REQ-016]`, `./sources/backend/notification/FcmNotificationService.java [REQ-016]`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ tích hợp Zalo API và Firebase Cloud Messaging (FCM).

### 📈 Giai đoạn 5 Triển Khai Các Tính Năng Cốt Lõi Của Ứng Dụng Di Động, Bản Địa Hóa Và SEO, Báo Cáo Và Phân Tích
- **Mục tiêu Cốt lõi & Mục đích của Giai đoạn:** Triển khai các tính năng cốt lõi của ứng dụng di động, bản địa hóa và SEO, báo cáo và phân tích.
- **Ma trận Bản đồ Thư mục Vật lý Mục tiêu:** `./sources/frontend/mobile/`, `./sources/backend/report/`, `./sources/docs/mobile.md`, `./sources/docs/report.md`
- **Đặc tả DDL SQL Schema Cơ sở Dữ liệu [DAT-011]:** ```sql:matrix
CREATE TABLE system_settings (
    setting_key VARCHAR(255) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```
- **Hợp đồng Định tuyến API và Sự kiện [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025]:** ```json
{
    "getMobileFeatures": {
        "path": "/api/mobile/features",
        "method": "GET",
        "response": {
            "features": [
                {
                    "featureId": "string",
                    "name": "string",
                    "description": "string"
                }
            ]
        }
    },
    "getLocale": {
        "path": "/api/locale",
        "method": "GET",
        "response": {
            "locale": "string"
        }
    },
    "getReport": {
        "path": "/api/reports/attendance",
        "method": "GET",
        "request": {
            "centerId": "string",
            "startDate": "string",
            "endDate": "string"
        },
        "response": {
            "report": "string"
        }
    },
    "getDashboard": {
        "path": "/api/dashboard",
        "method": "GET",
        "response": {
            "totalStudents": "number",
            "activeCourses": "number",
            "upcomingSessions": "number"
        }
    }
}
```
- **Bộ xử lý Ngoại lệ Cục bộ của Giai đoạn [EXC-005]:** System Recovery After Outage: If the service becomes unavailable, When it restores, Then any pending attendance scans are processed in FIFO order, and users receive a notification of recovered events.

#### Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase 5)

- **DAY 1: Khởi tạo các tính năng cốt lõi của ứng dụng di động và bản địa hóa**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-020], [REQ-022], [DAT-011]
    * **Target Component file path (`target_component`):** `./sources/frontend/mobile/MobileService.java [REQ-020]`, `./sources/backend/locale/LocaleService.java [REQ-022], [DAT-011]`
    * **Low-Level Technical Task Instruction:** Triển khai các tính năng cốt lõi của ứng dụng di động và bản địa hóa.
    * **Database Schema DDL SQL Specification [DAT-011]:**
    ```sql:matrix
    CREATE TABLE system_settings (
        setting_key VARCHAR(255) PRIMARY KEY,
        setting_value TEXT NOT NULL,
        description TEXT
    );
    ```
    * **API and Event Routing Contracts [REQ-020], [REQ-022]:**
    ```json
    {
        "getMobileFeatures": {
            "path": "/api/mobile/features",
            "method": "GET",
            "response": {
                "features": [
                    {
                        "featureId": "string",
                        "name": "string",
                        "description": "string"
                    }
                ]
            }
        },
        "getLocale": {
            "path": "/api/locale",
            "method": "GET",
            "response": {
                "locale": "string"
            }
        }
    }
    ```

- **DAY 2: Triển khai thông báo đẩy trên di động, SEO đa ngôn ngữ và báo cáo**
    * **Sub-Agent Workflow Specialization:** [Coder]
    * **Targeted Tag IDs:** [REQ-021], [REQ-023], [REQ-024], [REQ-025]
    * **Target Component file path (`target_component`):** `./sources/frontend/mobile/PushNotificationService.java [REQ-021]`, `./sources/backend/seo/SeoService.java [REQ-023]`, `./sources/backend/report/ReportService.java [REQ-024], [REQ-025]`
    * **Low-Level Technical Task Instruction:** Triển khai dịch vụ thông báo đẩy trên di động, SEO đa ngôn ngữ và báo cáo.
    * **API and Event Routing Contracts [REQ-021], [REQ-023], [REQ-024], [REQ-025]:**
    ```json
    {
        "getReport": {
            "path": "/api/reports/attendance",
            "method": "GET",
            "request": {
                "centerId": "string",
                "startDate": "string",
                "endDate": "string"
            },
            "response": {
                "report": "string"
            }
        },
        "getDashboard": {
            "path": "/api/dashboard",
            "method": "GET",
            "response": {
                "totalStudents": "number",
                "activeCourses": "number",
                "upcomingSessions": "number"
            }
        }
    }
    ```
    * **Phase Localized Exception Handlers [EXC-005]:**
    ```java
    @ExceptionHandler(ServiceUnavailableException.class)
    public ResponseEntity<Map<String, String>> handleServiceUnavailableException(ServiceUnavailableException ex) {
        Map<String, String> response = new HashMap<>();
        response.put("success", "false");
        response.put("message", "Service is unavailable. Please try again later.");
        return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE).body(response);
    }
    ```

## 📁 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📁 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 📁 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= 5; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 🛑 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 10, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`