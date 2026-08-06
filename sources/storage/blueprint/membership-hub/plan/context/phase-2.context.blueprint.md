# Giai đoạn 2: <!--PHASE_NAME_START-->Xây dựng dịch vụ khóa học, điểm danh, ứng dụng di động và tài liệu API<!--PHASE_NAME_END-->

## 📊 Document Control

| Mục | Chi tiết |
| :--- | :--- |
| **ID Kiến trúc** | ARCH-20260806142442 |
| **Tên dự án** | membership-hub |
| **Giai đoạn** | 2 |
| **Tên giai đoạn** | <!--PHASE_NAME_START-->Xây dựng dịch vụ khóa học, điểm danh, ứng dụng di động và tài liệu API<!--PHASE_NAME_END--> |
| **Mô tả** | <!--PHASE_DESC_START-->Giai đoạn này tập trung vào việc triển khai các dịch vụ quản lý khóa học, điểm danh, phát triển ứng dụng di động, và tài liệu API, đồng thời đảm bảo tính toàn vẹn dữ liệu, bảo mật OWASP, và khả năng mở rộng.<!--PHASE_DESC_END--> |
| **Phiên bản** | 1.0 (Baseline) |
| **Ngày/Thời gian** | 2026/08/06 14:24:42 |
| **Tác giả** | Enterprise System Architect (SA Agent) |
| **Phê duyệt** | Pending Technical Governance Review |

## 1. Phạm vi và mục tiêu của giai đoạn
Giai đoạn 2 thực hiện toàn bộ các thành phần cần thiết để triển khai:
- Dịch vụ quản lý khóa học (course-service) với CRUD, phân công giáo viên, và kiểm tra xung đột lịch.
- Dịch vụ điểm danh (attendance-service) với quét QR, tính chất bất biến, và xử lý ngoại lệ mạng.
- Ứng dụng di động (mobile-app) tích hợp với hai dịch vụ trên, hỗ trợ đăng nhập, danh sách khóa học, và điểm danh qua QR.
- Tài liệu API (api.md) mô tả các endpoint, schema, và quy trình bảo mật.
- Đảm bảo tuân thủ OWASP Top 10, kiểm thử đầy đủ, Docker image chuẩn, và triển khai GKE.

## 2. Phạm vi kỹ thuật & ranh giới thư mục
| Đường dẫn | Mô tả |
| :--- | :--- |
| `./sources/backend/course-service` | Dịch vụ quản lý khóa học |
| `./sources/backend/attendance-service` | Dịch vụ điểm danh |
| `./sources/frontend/mobile-app` | Ứng dụng di động |
| `./sources/docs/api.md` | Tài liệu API |
| **Endpoint routing** | `/api/courses`, `/api/attendance`, `/api/mobile` (REST) |

## 3. Hướng dẫn chức năng của Sub-Agent
* **Coder**: Phát triển mã nguồn chính cho backend và frontend, không viết test hoặc cấu hình hạ tầng.  
* **Tester**: Thiết kế và thực thi bộ test JUnit, integration, E2E, và kiểm thử hiệu năng.  
* **Reviewer**: Kiểm tra biên dịch, phân tích tĩnh, sửa lỗi bảo mật OWASP, và giải quyết các blocker SonarQube.  
* **Doc**: Soạn thảo tài liệu Markdown, bản đồ ER, hợp đồng API, và kiến trúc triển khai.  
* **Docker**: Xây dựng Dockerfile đa stage, tối ưu kích thước, và đẩy image lên DockerHub.  
* **GCP**: Tự động build và đẩy image lên Google Cloud Artifact Registry, triển khai trên Cloud Run.  
* **GKE**: Xây dựng manifest Kubernetes, HPA, Helm chart, và triển khai microservices vào GKE.

## 4. Định nghĩa DoD (Definition of Done)
- Tất cả yêu cầu [REQ-004]–[REQ-009], [REQ-012]–[REQ-013] được triển khai và kiểm thử 100 % coverage.  
- Dữ liệu [DAT-004] và [DAT-006] được tạo schema, index, và kiểm tra tính toàn vẹn.  
- Tất cả các endpoint tuân thủ OWASP, mã nguồn được review và không còn lỗi bảo mật.  
- Docker image cho mỗi dịch vụ có kích thước < 500 MB, được đẩy lên DockerHub.  
- GKE deployment hoàn chỉnh với HPA, auto‑scaling, và health checks.  
- Tài liệu API (api.md) đầy đủ, được kiểm tra chính tả và cấu trúc.  
- Traceability tags được ghi đầy đủ trong mọi sub-task.

## 5. LỊCH THỰC HIỆN NGÀY ĐẾN NGÀY

### 🌤️ DAY 1: <!--DAY_HEADER_START-->Thiết lập kiến trúc, dịch vụ và tài liệu API<!--DAY_HEADER_END-->

#### 📝 Sub-Task 1.1: Tạo bản đồ kiến trúc và tài liệu API
##### Được giao cho: Doc
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/docs/api.md`
* **Traceability Tag Tokens**: <!--START_TAGS-->[ARC-003], [ARC-004], [ARC-009]<!--END_TAGS-->

#### 📝 Sub-Task 1.2: Triển khai dịch vụ khóa học (course-service)
##### Được giao cho: Coder
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend/course-service`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-004]<!--END_TAGS-->

#### 📝 Sub-Task 1.3: Triển khai dịch vụ điểm danh (attendance-service)
##### Được giao cho: Coder
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend/attendance-service`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-012], [REQ-013], [DAT-006]<!--END_TAGS-->

#### 📝 Sub-Task 1.4: Kiểm thử đơn vị cho course-service và attendance-service
##### Được giao cho: Tester
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: INTEGRATION_SCOPE;./sources/backend/course-service/src/test/java
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-006]<!--END_TAGS-->

#### 📝 Sub-Task 1.5: Review mã nguồn và bảo mật
##### Được giao cho: Reviewer
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend/course-service`, `./sources/backend/attendance-service`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-012], [REQ-013], [DAT-004], [DAT-006]<!--END_TAGS-->

#### 📝 Sub-Task 1.6: Xây dựng Docker image cho course-service và attendance-service
##### Được giao cho: Docker
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend/course-service`, `./sources/backend/attendance-service`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-006]<!--END_TAGS-->

#### 📝 Sub-Task 1.7: Triển khai lên GKE
##### Được giao cho: GKE
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/backend/course-service`, `./sources/backend/attendance-service`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-006]<!--END_TAGS-->

### 🌤️ DAY 2: <!--DAY_HEADER_START-->Phát triển ứng dụng di động và hoàn thiện tài liệu API<!--DAY_HEADER_END-->

#### 📝 Sub-Task 2.1: Tích hợp mobile-app với course-service và attendance-service
##### Được giao cho: Coder
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/frontend/mobile-app`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-012], [REQ-013], [DAT-004], [DAT-006]<!--END_TAGS-->

#### 📝 Sub-Task 2.2: Cập nhật tài liệu API (api.md) với OpenAPI spec
##### Được giao cho: Doc
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/docs/api.md`
* **Traceability Tag Tokens**: <!--START_TAGS-->[ARC-003], [ARC-004], [ARC-009]<!--END_TAGS-->

#### 📝 Sub-Task 2.3: Kiểm thử tích hợp cho mobile-app
##### Được giao cho: Tester
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: INTEGRATION_SCOPE;./sources/frontend/mobile-app/src/test/java
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-012], [REQ-013], [DAT-004], [DAT-006]<!--END_TAGS-->

#### 📝 Sub-Task 2.4: Review mã nguồn mobile-app
##### Được giao cho: Reviewer
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/frontend/mobile-app`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [REQ-012], [REQ-013], [DAT-004], [DAT-006]<!--END_TAGS-->

#### 📝 Sub-Task 2.5: Xây dựng Docker image cho mobile-app
##### Được giao cho: Docker
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/frontend/mobile-app`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-006]<!--END_TAGS-->

#### 📝 Sub-Task 2.6: Triển khai mobile-app lên GKE
##### Được giao cho: GKE
##### Thành phần mục tiêu & yêu cầu kỹ thuật:
* **Đường dẫn mục tiêu**: `./sources/frontend/mobile-app`
* **Traceability Tag Tokens**: <!--START_TAGS-->[REQ-004], [REQ-005], [REQ-006], [REQ-007], [REQ-008], [REQ-009], [DAT-004], [DAT-006]<!--END_TAGS-->