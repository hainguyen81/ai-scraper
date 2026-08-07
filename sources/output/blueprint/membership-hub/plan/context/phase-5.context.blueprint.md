# Phase 5: <!--PHASE_NAME_START-->Triển khai Bản địa hóa, SEO, Báo cáo, Nâng cao bảo mật, Container hóa, Triển khai và Ghi nhật ký kiểm toán<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260807134137 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 5 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Triển khai Bản địa hóa, SEO, Báo cáo, Nâng cao bảo mật, Container hóa, Triển khai và Ghi nhật ký kiểm toán<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 5 tập trung vào việc triển khai các chức năng bản địa hóa đa ngôn ngữ, tối ưu SEO, tạo báo cáo điểm danh, nâng cao bảo mật hệ thống, container hóa toàn bộ dịch vụ và triển khai lên GKE, đồng thời thiết lập ghi nhật ký kiểm toán toàn diện. Các thành phần chính bao gồm cấu hình Firebase, Zalo, các bảng dữ liệu hệ thống, cấu hình Kubernetes, và tài liệu kỹ thuật chi tiết.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 13:41:37 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu của Giai đoạn

Giai đoạn 5 thực hiện triển khai toàn bộ chức năng bản địa hóa đa ngôn ngữ (EN, VI, ES), tối ưu SEO với hreflang và meta tags, tạo báo cáo điểm danh theo ngày cho từng trung tâm, nâng cao bảo mật hệ thống theo OWASP Top 10, container hóa toàn bộ dịch vụ Quarkus, triển khai lên GKE với HPA, và thiết lập ghi nhật ký kiểm toán toàn diện. Các thành phần chính bao gồm cấu hình Firebase, Zalo, các bảng dữ liệu hệ thống, cấu hình Kubernetes, và tài liệu kỹ thuật chi tiết.

## 2. Phạm vi Kỹ thuật & Giới hạn Thư mục

| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/backend/org/nlh4j/saas/membershiphub/i18n/` | Cấu hình đa ngôn ngữ, file locale |
| `./sources/backend/org/nlh4j/saas/membershiphub/report/` | Dịch vụ tạo báo cáo điểm danh |
| `./sources/backend/org/nlh4j/saas/membershiphub/security/` | Cấu hình bảo mật, JWT, OWASP |
| `./sources/backend/org/nlh4j/saas/membershiphub/audit/` | Entity ghi nhật ký kiểm toán |
| `./sources/infra/k8s/` | Manifest Kubernetes, Deployment, Service, Ingress |
| `./sources/infra/ci-cd/` | Pipeline CI/CD |
| `./sources/docs/` | Tài liệu kỹ thuật, kiến trúc, schema |

## 3. Hướng dẫn chức năng dành cho các tác nhân phụ

- **Coder**: Phát triển mã nguồn Java/Quarkus và JavaScript/React cho backend và frontend, không viết test hoặc manifest.  
- **Tester**: Viết JUnit, integration test, E2E, kiểm thử hiệu năng, không sửa mã nguồn.  
- **Reviewer**: Kiểm tra biên dịch, phân tích tĩnh, bảo mật OWASP, sửa lỗi.  
- **Doc**: Soạn thảo tài liệu kỹ thuật, schema, API contract, cấu hình, deployment.  
- **Docker**: Xây dựng Dockerfile đa giai đoạn, tối ưu kích thước, đẩy image.  
- **GCP**: Đẩy image lên Artifact Registry, cấu hình IAM.  
- **GKE**: Xây dựng manifest Kubernetes, HPA, Ingress, triển khai.  

## 4. Định nghĩa Doanh nghiệp (DoD)

- Tất cả yêu cầu [REQ-022]–[REQ-025] được triển khai đầy đủ.  
- Mọi endpoint tuân thủ chuẩn REST, bảo mật JWT, RBAC, OWASP Top 10.  
- Độ phủ test ≥ 85 % cho các module chính.  
- Tất cả tag ID được ánh xạ và kiểm tra 100 %.  
- Kích thước Docker image < 500 MB, triển khai thành công lên GKE.  
- Ghi nhật ký audit đầy đủ, lưu trữ 1 năm.  

## 5. LỊCH THỰC HIỆN KIẾT TRÚC NGÀY BỞI NGÀY

### 🌤️ DAY 1: <!--DAY_HEADER_START-->Xây dựng manifest triển khai Kubernetes<!--DAY_HEADER_END-->

#### 📝 Xây dựng manifest triển khai Kubernetes 1.1:
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/infra/k8s/Deployment.yaml
* **Traceability Tag Tokens**: <!--START_TAGS-->[NFR-004], [NFR-005]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: Tạo file Deployment.yaml cho toàn bộ dịch vụ Quarkus, cấu hình HPA dựa trên CPU > 70% hoặc độ trễ > 300ms, thiết lập Service cho mỗi module, định nghĩa Ingress với TLS, và triển khai lên cluster GKE. Đảm bảo các biến môi trường Firebase và Zalo được inject qua ConfigMap/Secret.

### 🌤️ DAY 2: <!--DAY_HEADER_START-->Đánh giá và hardening bảo mật<!--DAY_HEADER_END-->

#### 📝 Đánh giá và hardening bảo mật 2.1:
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/backend/org/nlh4j/saas/membershiphub/security/SecurityConfig.java
* **Traceability Tag Tokens**: <!--START_TAGS-->[NFR-003], [NFR-006]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: Xem xét cấu hình bảo mật hiện tại, áp dụng OWASP Top 10: sử dụng prepared statements, bảo vệ CSRF, XSS, enforce TLS 1.3, mã hóa dữ liệu nhạy cảm, cấu hình JWT expiration 15 phút, refresh token 7 ngày, và ghi log audit cho mọi hành động quan trọng.

#### 📝 Đánh giá và hardening bảo mật 2.2:
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/backend/org/nlh4j/saas/membershiphub/audit/AuditLogEntity.java
* **Traceability Tag Tokens**: <!--START_TAGS-->[NFR-003], [NFR-006]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: Thêm entity AuditLog với các trường userId, action, timestamp, details. Đảm bảo ghi log cho mọi thay đổi role, attendance, notification, và các thao tác quan trọng. Định dạng JSON, lưu trữ trong PostgreSQL, bảo vệ dữ liệu nhạy cảm.

### 🌤️ DAY 3: <!--DAY_HEADER_START-->Tạo tài liệu kỹ thuật và tham chiếu API<!--DAY_HEADER_END-->

#### 📝 Tạo tài liệu kỹ thuật và tham chiếu API 3.1:
##### Assigned Sub-Agent: Doc
##### Targeted Components & Technical Requirements:
* **Target Path**: ./sources/docs/Phase5_Documentation.md
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-022], [REQ-023], [REQ-024], [REQ-025]<!--END_TAGS-->
* **Low-Level Technical Task Instruction**: Soạn thảo tài liệu chi tiết bao gồm mô tả hệ thống, cấu trúc dữ liệu, API contract, exception handler, cấu hình Firebase, Zalo, Dockerfile, manifest Kubernetes, và hướng dẫn triển khai. Đảm bảo tài liệu phản ánh đúng trạng thái cuối cùng của hệ thống, bao gồm các bảng dữ liệu, quy trình, và các biện pháp bảo mật.

* **Database Schema DDL SQL Specification [DAT-011]**:
```sql
CREATE TABLE system_settings (
    setting_key VARCHAR(100) PRIMARY KEY,
    setting_value TEXT NOT NULL,
    description TEXT
);
```

* **API and Event Routing Contracts [REQ-022], [REQ-023], [REQ-024]**:
```json
{
  "endpoints": [
    {
      "path": "/api/v1/i18n/{locale}",
      "method": "GET",
      "response": {
        "messages": "object"
      }
    },
    {
      "path": "/api/v1/reports/attendance",
      "method": "GET",
      "request": {
        "centerId": "UUID",
        "startDate": "DATE",
        "endDate": "DATE"
      },
      "response": {
        "fileName": "string",
        "downloadUrl": "string"
      }
    },
    {
      "path": "/api/v1/dashboard/summary",
      "method": "GET",
      "response": {
        "totalStudents": "INT",
        "activeCourses": "INT",
        "upcomingSessions": "INT"
      }
    }
  ]
}
```

* **Phase Localized Exception Handlers [EXC-005]**: Xử lý lỗi phục hồi hệ thống sau sự cố: Khi dịch vụ được khôi phục, bất kỳ quét QR chờ xử lý nào được lưu trữ sẽ được xử lý theo thứ tự FIFO; người dùng nhận được thông báo về các sự kiện điểm danh đã được khôi phục.