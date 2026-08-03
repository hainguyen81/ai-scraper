# Giai đoạn 3: <!--PHASE_NAME_START-->notificationPromotionChatbot<!--PHASE_NAME_END--> | Mô tả: Triển khai và hoàn thiện các dịch vụ thông báo, khuyến mãi và chatbot, bao gồm thiết kế schema, API, logic nghiệp vụ, kiểm thử, bảo mật OWASP, và tài liệu kỹ thuật.  
## 📊 Document Control  

| Mục | Chi tiết |  
| :--- | :--- |  
| **ID Kiến trúc** | ARCH-20260803170121 |  
| **Tên dự án** | membership-hub |  
| **Giai đoạn** | 3 |  
| **Tên giai đoạn kỹ thuật** | <!--PHASE_NAME_START-->notificationPromotionChatbot<!--PHASE_NAME_END--> |  
| **Mô tả** | Triển khai và hoàn thiện các dịch vụ thông báo, khuyến mãi và chatbot, bao gồm thiết kế schema, API, logic nghiệp vụ, kiểm thử, bảo mật OWASP, và tài liệu kỹ thuật. |  
| **Phiên bản** | 1.0 (Baseline) |  
| **Ngày/Thời gian** | 2026/08/03 17:01:21 |  
| **Tác giả** | Enterprise System Architect (SA Agent) |  
| **Phê duyệt** | Pending Technical Governance Review |  

## 1. Phase Operational Scope & Objectives  
Giai đoạn 3 tập trung vào việc triển khai ba mô-đun cốt lõi:  
- **Notification**: Xây dựng dịch vụ gửi thông báo push, Zalo, và lưu trữ lịch sử thông báo, đồng thời xử lý các ngoại lệ giao tiếp mạng và retry logic.  
- **Promotion**: Thiết kế và triển khai schema khuyến mãi, API CRUD, và logic xác thực thời gian khuyến mãi, đồng thời đảm bảo tính toàn vẹn dữ liệu và bảo mật.  
- **Chatbot**: Tích hợp chatbot AI, xây dựng dịch vụ xử lý yêu cầu, lưu trữ lịch sử hội thoại, và đảm bảo tính bảo mật, tuân thủ OWASP.  
Mỗi mô-đun sẽ được triển khai theo kiến trúc microservices, sử dụng Java/Quarkus, PostgreSQL, và các công nghệ liên quan đã được xác định trong Global Context.  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  
- **Backend directories**  
  - `./sources/backend.notification/` – Service, controller, repository, DTO, exception, schema `NOTIFICATIONS`.  
  - `./sources/backend.promotion/` – Service, controller, repository, DTO, schema `PROMOTIONS`, `ANNOUNCEMENTS`.  
  - `./sources/backend.chatbot/` – Service, controller, repository, DTO, schema `CHATBOT_LOGS` (nếu có).  
- **REST API endpoints**  
  - `/api/notifications` – POST, GET, DELETE.  
  - `/api/promotions` – POST, GET, PUT, DELETE.  
  - `/api/announcements` – POST, GET, PUT, DELETE.  
  - `/api/chatbot` – POST, GET.  
- **Event routing** – Pub/Sub topics: `notifications`, `promotions`, `chatbot`.  

## 3. Dedicated Sub-Agent Functional Directives  
- **Coder**: Xây dựng lớp dịch vụ, controller, repository, DTO, exception, và schema cho từng mô-đun, đảm bảo tuân thủ OWASP (prepared statements, input validation, CSRF, rate limiting).  
- **Tester**: Viết unit test cho từng lớp dịch vụ, controller, repository, bao gồm kiểm thử ngoại lệ, tính toàn vẹn dữ liệu, và coverage ≥ 85 %.  
- **Reviewer**: Kiểm tra mã nguồn, thực hiện static analysis, xác nhận tuân thủ OWASP Top 10, tối ưu hiệu năng, và ghi nhận audit logs.  
- **Doc**: Tạo tài liệu kỹ thuật chi tiết cho từng dịch vụ, bao gồm mô tả API, schema, quy trình exception handling, và hướng dẫn triển khai.  

## 4. Phase Definition of Done (DoD)  
- Tất cả các API trả về trong < 200 ms (NFR-001).  
- Coverage 100 % cho tất cả các requirement tags (REQ-016…REQ-019).  
- Không có lỗ hổng OWASP Top 10 (đã được review và audit).  
- Tất cả tag ID được ghi nhận trong log (traceability).  
- Tài liệu kỹ thuật hoàn chỉnh, được lưu trong `./sources/backend.*/docs/`.  

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS  

### DAY 1: PHÁT TRIỂN DỊCH VỤ THÔNG BÁO  

#### SUB-TASK 1.1: Xây dựng NotificationService, controller, repository, DTO, exception, và schema NOTIFICATIONS  
##### Assigned Sub-Agent: Coder  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.notification/src/main/java/com/membershiphub/notification/NotificationService.java`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016], [ARC-008], [ARC-009], [ARC-010], [DAT-008], [EXC-003], [EXC-005]<!--END_TAGS-->  

#### SUB-TASK 1.2: Viết unit test cho NotificationService, controller, repository, exception, và schema NOTIFICATIONS  
##### Assigned Sub-Agent: Tester  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.notification/src/test/java/com/membershiphub/notification/NotificationServiceTest.java;./sources/backend.notification/src/main/java/com/membershiphub/notification/NotificationService.java`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016], [ARC-008], [ARC-009], [ARC-010], [DAT-008], [EXC-003], [EXC-005]<!--END_TAGS-->  

#### SUB-TASK 1.3: Review NotificationService, controller, repository, exception, và schema NOTIFICATIONS  
##### Assigned Sub-Agent: Reviewer  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.notification/src/main/java/com/membershiphub/notification/NotificationService.java`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016], [ARC-008], [ARC-009], [ARC-010], [DAT-008], [EXC-003], [EXC-005]<!--END_TAGS-->  

### DAY 2: PHÁT TRIỂN DỊCH VỤ KHƯƠNG MÃ VÀ CHATBOT  

#### SUB-TASK 2.1: Xây dựng PromotionService, controller, repository, DTO, exception, và schema PROMOTIONS, ANNOUNCEMENTS  
##### Assigned Sub-Agent: Coder  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.promotion/src/main/java/com/membershiphub/promotion/PromotionService.java`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-017], [REQ-018], [ARC-008], [ARC-009], [DAT-009]<!--END_TAGS-->  

#### SUB-TASK 2.2: Viết unit test cho PromotionService, controller, repository, exception, và schema PROMOTIONS, ANNOUNCEMENTS  
##### Assigned Sub-Agent: Tester  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.promotion/src/test/java/com/membershiphub/promotion/PromotionServiceTest.java;./sources/backend.promotion/src/main/java/com/membershiphub/promotion/PromotionService.java`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-017], [REQ-018], [ARC-008], [ARC-009], [DAT-009]<!--END_TAGS-->  

#### SUB-TASK 2.3: Review PromotionService, controller, repository, exception, và schema PROMOTIONS, ANNOUNCEMENTS  
##### Assigned Sub-Agent: Reviewer  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.promotion/src/main/java/com/membershiphub/promotion/PromotionService.java`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-017], [REQ-018], [ARC-008], [ARC-009], [DAT-009]<!--END_TAGS-->  

#### SUB-TASK 2.4: Xây dựng ChatbotService, controller, repository, DTO, exception, và schema CHATBOT_LOGS (nếu có)  
##### Assigned Sub-Agent: Coder  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.chatbot/src/main/java/com/membershiphub/chatbot/ChatbotService.java`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-019], [ARC-008], [ARC-009]<!--END_TAGS-->  

#### SUB-TASK 2.5: Viết unit test cho ChatbotService, controller, repository, exception, và schema CHATBOT_LOGS (nếu có)  
##### Assigned Sub-Agent: Tester  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.chatbot/src/test/java/com/membershiphub/chatbot/ChatbotServiceTest.java;./sources/backend.chatbot/src/main/java/com/membershiphub/chatbot/ChatbotService.java`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-019], [ARC-008], [ARC-009]<!--END_TAGS-->  

#### SUB-TASK 2.6: Review ChatbotService, controller, repository, exception, và schema CHATBOT_LOGS (nếu có)  
##### Assigned Sub-Agent: Reviewer  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.chatbot/src/main/java/com/membershiphub/chatbot/ChatbotService.java`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-019], [ARC-008], [ARC-009]<!--END_TAGS-->  

### DAY 3: KIỂM THỬ VÀ ĐÁNH GIÁ BẢO MẬT, TẠO TÀI LIỆU  

#### SUB-TASK 3.1: Kiểm thử tích hợp toàn bộ dịch vụ Notification, Promotion, Chatbot (API, event, exception handling)  
##### Assigned Sub-Agent: Tester  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `INTEGRATION_SCOPE`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [DAT-008], [DAT-009], [ARC-008], [ARC-009], [ARC-010], [EXC-003], [EXC-005]<!--END_TAGS-->  

#### SUB-TASK 3.2: Review toàn bộ mã nguồn, thực hiện static analysis, xác nhận tuân thủ OWASP, và ghi nhận audit logs  
##### Assigned Sub-Agent: Reviewer  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.notification/;./sources/backend.promotion/;./sources/backend.chatbot/`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [DAT-008], [DAT-009], [ARC-008], [ARC-009], [ARC-010], [EXC-003], [EXC-005]<!--END_TAGS-->  

#### SUB-TASK 3.3: Tạo tài liệu kỹ thuật chi tiết cho Notification, Promotion, Chatbot (API, schema, exception handling, deployment guide)  
##### Assigned Sub-Agent: Doc  
##### Targeted Components & Technical Requirements:  
* **Target Path:** `./sources/backend.notification/docs/NotificationService.md;./sources/backend.promotion/docs/PromotionService.md;./sources/backend.chatbot/docs/ChatbotService.md`  
* **Traceability Tag Tokens:** <!--START_TAGS-->[REQ-016], [REQ-017], [REQ-018], [REQ-019], [DAT-008], [DAT-009], [ARC-008], [ARC-009], [ARC-010], [EXC-003], [EXC-005]<!--END_TAGS-->