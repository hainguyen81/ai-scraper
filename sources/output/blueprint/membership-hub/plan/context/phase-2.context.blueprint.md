# Phase 2: <!--PHASE_NAME_START-->Triển khai quản lý trung tâm, API CRUD và schema trung tâm<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260807134137 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Triển khai quản lý trung tâm, API CRUD và schema trung tâm<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 2 tập trung vào việc triển khai quản lý trung tâm, xây dựng API CRUD, và định nghĩa schema dữ liệu cho trung tâm. Các thành phần chính bao gồm lớp thực thể `CenterEntity`, controller `CenterController`, và các endpoint REST tương ứng. Ngoài ra, giai đoạn còn bao gồm việc chuẩn bị tài liệu kiến trúc chi tiết và xây dựng Docker image cho dịch vụ trung tâm.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 13:41:37 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi thực thi và mục tiêu

Giai đoạn 2 thực hiện các nhiệm vụ sau:
- Xây dựng mô hình dữ liệu `CenterEntity` và các ràng buộc liên quan (khóa chính, khóa ngoại, kiểm tra số thuế).
- Phát triển controller `CenterController` với các endpoint CRUD và gán quản trị viên trung tâm.
- Định nghĩa và triển khai schema PostgreSQL cho bảng `centers`.
- Tạo tài liệu kiến trúc chi tiết cho giai đoạn 2, bao gồm mô hình dữ liệu, luồng API, và quy trình triển khai.
- Xây dựng Dockerfile đa giai đoạn cho dịch vụ trung tâm, tối ưu kích thước và chuẩn bị cho CI/CD.

## 2. Phạm vi kỹ thuật và ranh giới thư mục

| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/backend/org/nlh4j/saas/membershiphub/center-management/CenterEntity.java` | Lớp thực thể trung tâm |
| `./sources/backend/org/nlh4j/saas/membershiphub/center-management/CenterController.java` | Controller CRUD trung tâm |
| `./sources/backend/org/nlh4j/saas/membershiphub/center-management/CenterService.java` | Service nghiệp vụ trung tâm |
| `./sources/backend/org/nlh4j/saas/membershiphub/center-management/CenterRepository.java` | Repository JPA |
| `./sources/backend/org/nlh4j/saas/membershiphub/center-management/CenterDTO.java` | DTO trung tâm |
| `./sources/docs/Phase2_Architecture.md` | Tài liệu kiến trúc giai đoạn 2 |
| `./sources/infra/center-management/Dockerfile` | Dockerfile đa giai đoạn |
| Endpoints: `/api/v1/centers`, `/api/v1/centers/{id}`, `/api/v1/centers/assign` | API CRUD và gán quản trị viên |

## 3. Hướng dẫn chức năng của các tác nhân phụ

- **Coder**: Phát triển mã nguồn Java cho backend, bao gồm các lớp thực thể, controller, service, repository, và DTO. Không thực hiện kiểm thử hoặc cấu hình hạ tầng.
- **Tester**: Thiết kế và triển khai bộ kiểm thử JUnit5 cho các lớp thực thể và controller. Nếu phạm vi kiểm thử bao gồm nhiều lớp, sử dụng `INTEGRATION_SCOPE;./sources/backend/tests/integration/CenterIntegrationTest.java`.
- **Doc**: Soạn thảo tài liệu kiến trúc chi tiết, mô hình dữ liệu, luồng API, và quy trình triển khai. Tạo file `./sources/docs/Phase2_Architecture.md`.
- **Reviewer**: Kiểm tra mã nguồn, thực hiện phân tích tĩnh, và đảm bảo tuân thủ OWASP Top 10.
- **Docker**: Xây dựng Dockerfile đa giai đoạn cho dịch vụ trung tâm, tối ưu kích thước và chuẩn bị cho CI/CD.
- **GCP**: Không áp dụng trong giai đoạn này.
- **GKE**: Không áp dụng trong giai đoạn này.

## 4. Định nghĩa Hoàn thành (DoD)

- Tất cả yêu cầu [REQ-004], [REQ-005], [REQ-006] được triển khai đầy đủ.
- Schema PostgreSQL `centers` được tạo và kiểm tra tính toàn vẹn dữ liệu.
- API CRUD `/api/v1/centers` đáp ứng đúng định dạng JSON và bảo mật JWT.
- Tài liệu kiến trúc `Phase2_Architecture.md` hoàn chỉnh, bao gồm mô hình dữ liệu, luồng API, và quy trình triển khai.
- Docker image `center-management` được xây dựng, kích thước < 500 MB, và được đẩy lên registry.
- Độ phủ kiểm thử JUnit5 ≥ 85 % cho các lớp thực thể và controller.
- Kiểm tra OWASP: bảo vệ chống SQL injection, XSS, CSRF, và bảo mật JWT.
- Mọi tag ID được ánh xạ đầy đủ, không có tag chưa được sử dụng.

## 5. Nhật ký thực thi kiến trúc theo ngày

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->TRIỂN KHAI LỚP THỰC THỂ VÀ CONTROLLER TRUNG TÂM<!--DAY_HEADER_END-->

#### 📝 TRIỂN KHAI LỚP THỰC THỂ VÀ CONTROLLER TRUNG TÂM 1.1:
##### Được giao cho: Coder
##### Yêu cầu thành phần & kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend/org/nlh4j/saas/membershiphub/center-management/CenterEntity.java`
* **Thẻ truy xuất**: <!--START_TAGS-->[REQ-004], [DAT-003]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**:  
  - Triển khai lớp thực thể `CenterEntity` với các trường `centerId` (UUID PK), `name`, `address`, `taxId` (UNIQUE, CHECK số), `contactPhone`, `contactEmail`.  
  - Định nghĩa ràng buộc NOT NULL, UNIQUE, và CHECK `tax_id ~ '^[0-9]+$'`.  
  - Tạo controller `CenterController` với các endpoint CRUD (`GET`, `POST`, `PUT`, `DELETE`) và endpoint gán quản trị viên (`POST /assign`).  
  - Đảm bảo tất cả các endpoint bảo vệ bằng JWT và thực thi kiểm tra quyền RBAC.  
  - Thêm service `CenterService` để xử lý nghiệp vụ và repository `CenterRepository` cho truy cập JPA.  
  - Đảm bảo mã nguồn tuân thủ OWASP: sử dụng prepared statements, kiểm tra đầu vào, và mã hóa dữ liệu nhạy cảm.

* **Database Schema DDL SQL Specification [DAT-003]**:
```sql
CREATE TABLE centers (
    center_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    tax_id VARCHAR(13) NOT NULL UNIQUE,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(255),
    CONSTRAINT chk_tax_id_numeric CHECK (tax_id ~ '^[0-9]+$')
);
```

* **API and Event Routing Contracts [REQ-004], [ARC-002], [ARC-005]**:
```json
{
  "endpoints": [
    {
      "path": "/api/v1/centers",
      "method": "GET",
      "response": [
        {
          "centerId": "UUID",
          "name": "string",
          "address": "string",
          "taxId": "string",
          "contactPhone": "string",
          "contactEmail": "string"
        }
      ]
    },
    {
      "path": "/api/v1/centers",
      "method": "POST",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "centerId": "UUID"
      }
    },
    {
      "path": "/api/v1/centers/{id}",
      "method": "PUT",
      "request": {
        "name": "string",
        "address": "string",
        "taxId": "string",
        "contactPhone": "string",
        "contactEmail": "string"
      },
      "response": {
        "centerId": "UUID"
      }
    },
    {
      "path": "/api/v1/centers/{id}",
      "method": "DELETE",
      "response": {
        "centerId": "UUID"
      }
    },
    {
      "path": "/api/v1/centers/assign",
      "method": "POST",
      "request": {
        "userId": "UUID",
        "centerId": "UUID"
      },
      "response": {
        "userId": "UUID",
        "centerId": "UUID"
      }
    }
  ]
}
```

* **Phase Localized Exception Handlers [EXC-004]**:
  - Xử lý lỗi xác thực đầu vào không hợp lệ cho form tạo trung tâm (ví dụ: taxId trùng lặp, email sai định dạng). Trả về thông báo lỗi chi tiết và hướng dẫn chỉnh sửa.

#### 📝 TẠI LIỆU KIẾN TRÚC GIAI ĐOẠN 2 1.2:
##### Được giao cho: Doc
##### Yêu cầu thành phần & kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/docs/Phase2_Architecture.md`
* **Thẻ truy xuất**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**:  
  - Soạn thảo tài liệu kiến trúc chi tiết cho giai đoạn 2, bao gồm mô hình dữ liệu `CenterEntity`, luồng API CRUD, quy trình triển khai Docker, và quy trình CI/CD.  
  - Đảm bảo tài liệu tuân thủ chuẩn OWASP, bảo mật, và ghi chú các ràng buộc dữ liệu.  
  - Cung cấp sơ đồ kiến trúc, bảng dữ liệu, và mô tả chi tiết các endpoint.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->XÂY DỰNG DOCKER IMAGE CHO DỊCH VỤ TRUNG TÂM<!--DAY_HEADER_END-->

#### 📝 XÂY DỰNG DOCKER IMAGE CHO DỊCH VỤ TRUNG TÂM 2.1:
##### Được giao cho: Docker
##### Yêu cầu thành phần & kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/infra/center-management/Dockerfile`
* **Thẻ truy xuất**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006]<!--END_TAGS-->
* **Hướng dẫn công việc kỹ thuật chi tiết**:  
  - Tạo Dockerfile đa giai đoạn sử dụng Quarkus runtime, sao chép mã nguồn đã biên dịch, thiết lập người dùng không đặc quyền, expose port 8080, và tối ưu kích thước image (< 500 MB).  
  - Định nghĩa biến môi trường cho cấu hình kết nối PostgreSQL và Redis.  
  - Kiểm tra image bằng `docker build` và `docker run` trong môi trường CI.  
  - Đẩy image lên registry với tag `latest` và chuẩn bị cho triển khai trên GKE.