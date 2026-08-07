# Phase 4: <!--PHASE_NAME_START-->Triển khai hệ thống thông báo đa kênh, khuyến mãi và chatbot AI cùng giao diện di động<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **Mã Blueprint** | ARCH-20260807134137 |
| **Tên Dự án** | membership-hub |
| **Giai đoạn** | 4 |
| **Tên Giai đoạn** | <!--PHASE_NAME_START-->Triển khai hệ thống thông báo đa kênh, khuyến mãi và chatbot AI cùng giao diện di động<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn 4 tập trung vào việc triển khai các dịch vụ thông báo đa kênh (FCM/APNs, Zalo), quản lý khuyến mãi và thông báo, tích hợp chatbot AI, và phát triển lõi giao diện người dùng di động. Các thành phần chính bao gồm các thực thể, controller, service, DTO, exception handler, cấu hình Firebase và Zalo, Dockerfile, manifest Kubernetes, và các tài liệu kiến trúc chi tiết. Bảo mật OWASP, RBAC, JWT, và các biện pháp bảo vệ dữ liệu được áp dụng xuyên suốt.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Giờ** | 2026/08/07 13:41:37 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và Mục tiêu của Giai đoạn

Giai đoạn 4 thực hiện triển khai toàn bộ chức năng thông báo đa kênh, quản lý khuyến mãi và thông báo, tích hợp chatbot AI, và phát triển giao diện người dùng di động. Các thành phần chính bao gồm: thực thể Notification, Promotion, Announcement; các controller, service, DTO và exception handler tương ứng; cấu hình Firebase Cloud Messaging và Zalo API; Dockerfile đa giai đoạn cho dịch vụ; manifest Kubernetes với HPA; tài liệu kiến trúc chi tiết; và các kiểm thử tích hợp. Mọi giao diện API phải tuân thủ chuẩn REST, bảo mật JWT, RBAC, và OWASP Top 10. Các yêu cầu bảo mật bao gồm mã hóa TLS 1.3, bảo vệ dữ liệu nhạy cảm, và ghi nhật ký audit.

## 2. Phạm vi Kỹ thuật & Ranh giới Thư mục

| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/backend/org/nlh4j/saas/membershiphub/notification/` | Thực thể, controller, service, DTO, exception handler cho thông báo |
| `./sources/backend/org/nlh4j/saas/membershiphub/promotion/` | Thực thể, controller, service, DTO cho khuyến mãi |
| `./sources/backend/org/nlh4j/saas/membershiphub/announcement/` | Thực thể, controller, service, DTO cho thông báo |
| `./sources/backend/org/nlh4j/saas/membershiphub/chatbot/` | Service, controller cho chatbot AI |
| `./sources/frontend/mobile/src/services/` | Service JavaScript cho thông báo di động |
| `./sources/infra/notification-management/Dockerfile` | Dockerfile đa giai đoạn |
| `./sources/infra/gcp/firebase-config.yaml` | Cấu hình Firebase Cloud Messaging |
| `./sources/infra/gcp/zalo-api-credentials.json` | Credentials Zalo API |
| `./sources/infra/k8s/notification-deployment.yaml` | Manifest Kubernetes cho dịch vụ |
| `./sources/docs/Phase4_Architecture.md` | Tài liệu kiến trúc chi tiết |

**Endpoint Routing (REST) – JSON Contract**

```json
{
  "endpoints": [
    {
      "path": "/api/v1/notifications",
      "method": "POST",
      "request": {
        "userId": "UUID",
        "groupZalo": "string",
        "message": "string"
      },
      "response": {
        "notificationId": "UUID",
        "sentAt": "TIMESTAMP"
      }
    },
    {
      "path": "/api/v1/promotions",
      "method": "POST",
      "request": {
        "code": "string",
        "discountPercent": "SMALLINT",
        "startDate": "DATE",
        "endDate": "DATE",
        "description": "string"
      },
      "response": {
        "promoId": "UUID"
      }
    },
    {
      "path": "/api/v1/announcements",
      "method": "POST",
      "request": {
        "title": "string",
        "content": "string",
        "startDate": "DATE",
        "endDate": "DATE"
      },
      "response": {
        "announcementId": "UUID"
      }
    },
    {
      "path": "/api/v1/chatbot/query",
      "method": "POST",
      "request": {
        "userId": "UUID",
        "query": "string"
      },
      "response": {
        "answer": "string",
        "escalated": "boolean"
      }
    },
    {
      "path": "/api/v1/mobile/notifications/register",
      "method": "POST",
      "request": {
        "deviceToken": "string",
        "platform": "string"
      },
      "response": {
        "registered": "boolean"
      }
    }
  ]
}
```

**Exception Handler – EXC-003**

```text
* Xử lý lỗi gửi thông báo không thành công (ví dụ: device token không hợp lệ). Hệ thống ghi log lỗi, lên lịch thử lại tối đa 3 lần, sau đó đánh dấu là thất bại và thông báo cho admin.
```

## 3. Hướng dẫn chức năng dành cho các tác nhân phụ

- **Coder**: Phát triển mã nguồn Java và JavaScript cho backend và frontend, triển khai các thực thể, controller, service, DTO, exception handler, và cấu hình. Không viết test hoặc manifest.
- **Tester**: Viết JUnit5, integration tests, và kiểm thử hiệu năng cho các endpoint. Không sửa mã nguồn.
- **Doc**: Soạn thảo tài liệu kiến trúc chi tiết, schema, và hướng dẫn triển khai. Đảm bảo tài liệu nằm trong `./sources/docs/`.
- **Reviewer**: Kiểm tra mã, bảo mật OWASP, và sửa lỗi biên dịch.
- **Docker**: Xây dựng Dockerfile đa giai đoạn, tối ưu kích thước, và đẩy image.
- **GCP**: Cấu hình Firebase và Zalo, đẩy image lên Google Artifact Registry.
- **GKE**: Tạo manifest Kubernetes, HPA, và triển khai dịch vụ.

## 4. Định nghĩa Hoàn thành Giai đoạn

- Tất cả các yêu cầu [REQ-016] đến [REQ-020] được triển khai đầy đủ.
- Mọi endpoint tuân thủ chuẩn REST, bảo mật JWT, RBAC, và OWASP Top 10.
- Độ phủ test ít nhất 85 % cho các module chính.
- Tất cả tag ID được ánh xạ và kiểm tra 100 %.
- Hệ thống ghi nhật ký audit đầy đủ và bảo mật dữ liệu.
- Đóng gói Docker < 500 MB, triển khai trên GKE với HPA.
- Tài liệu kiến trúc, schema, và hướng dẫn triển khai hoàn chỉnh.

## 5. LỊCH THỰC HIỆN KIẾT TRÚC NGÀY BỞI NGÀY

### 🌤️ NGÀY 1: <!--DAY_HEADER_START-->THIẾT LẬP VÀ TẠO CÁC THÀNH PHẦN THÔNG BÁO<!--DAY_HEADER_END-->

#### 📝 TẠO TÀI LIỆU KIẾT TRÚC GIAI ĐOẠN 1.1: 
##### Doc
##### Target Path: `./sources/docs/Phase4_Architecture.md`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [ARC-009], [ARC-010], [DAT-008], [DAT-009], [EXC-003]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Soạn thảo tài liệu chi tiết bao gồm mô hình dữ liệu, sơ đồ ER, API contract, exception handler, cấu hình Firebase và Zalo, Dockerfile, manifest Kubernetes, và hướng dẫn triển khai. Đảm bảo ghi chú các ràng buộc, khóa ngoại, và biện pháp bảo mật OWASP.

#### 📝 TRIỂN KHAI VÀ TẠO THỰC THỂ VÀ SERVICE THÔNG BÁO 1.2: 
##### Coder
##### Target Path: `./sources/backend/org/nlh4j/saas/membershiphub/notification/NotificationEntity.java, ./sources/backend/org/nlh4j/saas/membershiphub/notification/NotificationController.java, ./sources/backend/org/nlh4j/saas/membershiphub/notification/NotificationService.java, ./sources/backend/org/nlh4j/saas/membershiphub/notification/NotificationDTO.java, ./sources/backend/org/nlh4j/saas/membershiphub/notification/NotificationExceptionHandler.java, ./sources/backend/org/nlh4j/saas/membershiphub/promotion/PromotionEntity.java, ./sources/backend/org/nlh4j/saas/membershiphub/promotion/PromotionController.java, ./sources/backend/org/nlh4j/saas/membershiphub/promotion/PromotionService.java, ./sources/backend/org/nlh4j/saas/membershiphub/promotion/PromotionDTO.java, ./sources/backend/org/nlh4j/saas/membershiphub/promotion/PromotionExceptionHandler.java, ./sources/backend/org/nlh4j/saas/membershiphub/announcement/AnnouncementEntity.java, ./sources/backend/org/nlh4j/saas/membershiphub/announcement/AnnouncementController.java, ./sources/backend/org/nlh4j/saas/membershiphub/announcement/AnnouncementService.java, ./sources/backend/org/nlh4j/saas/membershiphub/announcement/AnnouncementDTO.java, ./sources/backend/org/nlh4j/saas/membershiphub/announcement/AnnouncementExceptionHandler.java, ./sources/backend/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java, ./sources/backend/org/nlh4j/saas/membershiphub/chatbot/ChatbotController.java, ./sources/backend/org/nlh4j/saas/membershiphub/chatbot/ChatbotDTO.java, ./sources/frontend/mobile/src/services/NotificationService.js`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [DAT-008], [DAT-009], [EXC-003], [ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Triển khai các thực thể, controller, service, DTO và exception handler cho Notification, Promotion, Announcement và Chatbot. Đảm bảo các endpoint tuân thủ contract JSON, bảo mật JWT, RBAC, và OWASP. Cấu hình Firebase Cloud Messaging và Zalo API trong các service. Đảm bảo exception handler EXC-003 được triển khai.

#### 📝 KIỂM THỬ TÍNH NĂNG THÔNG BÁO 1.3: 
##### Tester
##### Target Path: `INTEGRATION_SCOPE;./sources/backend/tests/integration/NotificationIntegrationTest.java, INTEGRATION_SCOPE;./sources/backend/tests/integration/PromotionIntegrationTest.java, INTEGRATION_SCOPE;./sources/backend/tests/integration/AnnouncementIntegrationTest.java, INTEGRATION_SCOPE;./sources/backend/tests/integration/ChatbotIntegrationTest.java`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [EXC-003]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Viết các test tích hợp kiểm tra tính toàn vẹn dữ liệu, phản hồi HTTP, và exception handling. Đảm bảo độ phủ test ≥ 85 % và kiểm tra bảo mật OWASP.

#### 📝 XÂY DỰNG DOCKERFILE 1.4: 
##### Docker
##### Target Path: `./sources/infra/notification-management/Dockerfile`
##### Traceability Tag Tokens: <!--START_TAGS-->[ARC-009], [ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Xây dựng Dockerfile đa giai đoạn sử dụng Quarkus runtime, sao chép mã nguồn đã biên dịch, thiết lập người dùng không đặc quyền, expose port 8080, tối ưu kích thước < 500 MB. Đẩy image lên DockerHub.

#### 📝 CẤU HÌNH FIREBASE VÀ ZALO 1.5: 
##### GCP
##### Target Path: `./sources/infra/gcp/firebase-config.yaml, ./sources/infra/gcp/zalo-api-credentials.json`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-020], [ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Tạo file YAML cấu hình Firebase Cloud Messaging với khóa server, và file JSON lưu trữ credentials API Zalo. Đẩy vào Google Secret Manager, thiết lập IAM cho dịch vụ thông báo, và xác thực OAuth2 cho Zalo.

#### 📝 TẠO MANIFEST KUBERNETES 1.6: 
##### GKE
##### Target Path: `./sources/infra/k8s/notification-deployment.yaml`
##### Traceability Tag Tokens: <!--START_TAGS-->[ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Xây dựng manifest Kubernetes với Deployment, Service, Ingress TLS, HPA dựa trên CPU > 70 % hoặc latency > 300 ms. Định nghĩa environment variables cho Firebase và Zalo.

#### 📝 XEM XÉT BẢN ĐIỀU BẢO 1.7: 
##### Reviewer
##### Target Path: `./sources/backend/org/nlh4j/saas/membershiphub/notification/NotificationService.java, ./sources/backend/org/nlh4j/saas/membershiphub/promotion/PromotionService.java, ./sources/backend/org/nlh4j/saas/membershiphub/announcement/AnnouncementService.java, ./sources/backend/org/nlh4j/saas/membershiphub/chatbot/ChatbotService.java`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Kiểm tra mã nguồn, bảo mật OWASP, xác thực JWT, RBAC, và kiểm tra các exception handler. Đề xuất sửa lỗi và tối ưu.

### 🌤️ NGÀY 2: <!--DAY_HEADER_START-->TƯƠNG TÁC VÀ ĐĂNG KÝ HÀNG HÓA VÀ CHATBOT<!--DAY_HEADER_END-->

#### 📝 TƯƠNG TÁC VÀ ĐĂNG KÝ HÀNG HÓA 2.1: 
##### Coder
##### Target Path: `./sources/frontend/mobile/src/services/NotificationService.js`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-020], [ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Triển khai service JavaScript cho mobile, đăng ký device token, gửi request POST `/api/v1/mobile/notifications/register`. Đảm bảo xử lý token, retry logic, và bảo mật JWT.

#### 📝 KIỂM THỬ ĐĂNG KÝ HÀNG HÓA 2.2: 
##### Tester
##### Target Path: `INTEGRATION_SCOPE;./sources/frontend/tests/integration/NotificationServiceTest.js`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-020]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Viết test unit cho NotificationService.js, kiểm tra đăng ký token, retry logic, và xử lý lỗi.

#### 📝 XÂY DỰNG VÀ ĐĂNG LỚP HÌNH 2.3: 
##### Docker
##### Target Path: `./sources/infra/notification-management/Dockerfile`
##### Traceability Tag Tokens: <!--START_TAGS-->[ARC-009], [ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Xây dựng và đẩy image đã được build từ ngày 1, kiểm tra kích thước < 500 MB.

#### 📝 ĐĂNG LỚP HÌNH VÀ TRIỂN HÀNH 2.4: 
##### GCP
##### Target Path: `./sources/infra/gcp/firebase-config.yaml, ./sources/infra/gcp/zalo-api-credentials.json`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-020], [ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Đẩy image lên Google Artifact Registry, cấu hình IAM, và xác thực dịch vụ.

#### 📝 CẬP NHẬT MANIFEST VÀ HPA 2.5: 
##### GKE
##### Target Path: `./sources/infra/k8s/notification-deployment.yaml`
##### Traceability Tag Tokens: <!--START_TAGS-->[ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Cập nhật manifest với phiên bản mới, kiểm tra HPA, và triển khai lên cluster GKE.

#### 📝 XEM XÉT BẢN ĐIỀU BẢO VÀ ĐÁNH GIÁ 2.6: 
##### Reviewer
##### Target Path: `./sources/backend/org/nlh4j/saas/membershiphub/notification/NotificationService.java, ./sources/frontend/mobile/src/services/NotificationService.js`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Kiểm tra bảo mật, hiệu năng, và tuân thủ OWASP. Đề xuất tối ưu.

#### 📝 CẬP NHẬT TÀI LIỆU KIẾT TRÚC 2.7: 
##### Doc
##### Target Path: `./sources/docs/Phase4_Architecture.md`
##### Traceability Tag Tokens: <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [ARC-010]<!--END_TAGS-->
##### Low-Level Technical Task Instruction: Cập nhật tài liệu kiến trúc với các thay đổi triển khai, cấu hình, và hướng dẫn triển khai cuối cùng. Đảm bảo tài liệu phản ánh đúng trạng thái cuối cùng của hệ thống.