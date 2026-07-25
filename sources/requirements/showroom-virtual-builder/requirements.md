## 1. PROJECT OVERVIEW
- **Product Objectives & Core Values**
  1. Cho phép doanh nghiệp nhỏ tạo showroom 3D thực tế ảo nhanh chóng, không cần viết code.
  2. Cung cấp trải nghiệm khách hàng trực quan, tăng tỷ lệ chuyển đổi bán hàng.
  3. Đảm bảo tính bảo mật dữ liệu, tuân thủ tiêu chuẩn bảo mật thông tin.
- **Target User Personas**
  1. *Chủ cửa hàng bán lẻ*: doanh nghiệp bán lẻ truyền thống muốn trưng bày sản phẩm trực tuyến.
  2. *Công ty nội thất*: doanh nghiệp muốn chia sẻ bộ sưu tập nội thất 3D.
  3. *Nhà sản xuất hàng thủ công*: cần nền tảng trưng bày sản phẩm đa dạng.
- **Role-Based Access Control (RBAC) Matrix**
  | Role | Dashboard | Asset Management | 3D Builder | AI Chatbot | Integration | Analytics |
  |------|-----------|------------------|------------|------------|-------------|-----------|
  | SuperAdmin headline | Full | Full | Full | Full | Full | Full |
  | Admin | Full | Full | Full | Full | Read | Read |
  | Editor | Read | Full | Full | Read | Read | Read |
  | Viewer | Read | Read | Read | Read | Read | Read |

## 2. FUNCTIONAL REQUIREMENTS
### Epic 1: User Management
- **User Story**: As a SuperAdmin, I want to create, edit, and delete user accounts so that I can control access.
- **Acceptance Criteria**:
  - Given a SuperAdmin is logged in, when I navigate to the user cookware, then I can create a new user with a unique email.
  - Given a user account, when I assign a role, then the system updates permissions accordingly.
  - Given a user is deleted, then all associated sessions are invalidated within 5 seconds.
- **Data Inputs & Field Validations**:
  - Email: required, unique, regex `^[\w.-]+@[\w.-]+\.\w{2,}$`.
  - Password: required, min 12 chars, includes upper, lower, digit, special.
  - Role: required, enum {SuperAdmin, Admin, Editor, Viewer}.
  - Audit fields: created_at, updated_at, created_by, updated_by.

### Epic 2: Asset Upload
- **User Story**: As an Editor, I want to upload product images so that I can add them to the showroom.
- **Acceptance Criteria**:
  - Given a user with Editor role, when I upload an image > 5MB, then the system rejects with error code 413.
  - Given an image format unsupported (e.g., .tiff), then the system rejects with error code 415.
  - Given a valid image PNG/JPG, then the system stores it in S3 with a unique UUID key.
- **Data Inputs & Field Validations**:
  - File: required, mime type JPEG|PNG, size ≤ 5MB.
  - Metadata: title (max 256 chars), description (max 1024 chars), tags (≤  gotas 10).

### Epic 3: 3D Space Builder
- **User Story**: As an Editor, I want to arrange uploaded assets in a 3D grid so that I can design the showroom layout.
- **Acceptance Criteria**:
  - Given the builder UI, when I drag an asset onto the canvas, then the system reserves the position within 200ms.
  - Given I rotate an asset, then the new orientation is persisted within 500ms.
  - Given I save layout, then the system writes JSON representation to database with versioning.
- **Data Inputs & Field Validations**:
  - Position: x, y, z coordinates, float, range [-50, 50].
  - Rotation: yaw, pitch, roll нуж float, range [0, 360].
  - Scale: float ≥ 0.1, ≤ 10.

### Epic 4: AI Chatbot Integration
- **User Story**: As a Viewer, I want to ask questions about products and receive suggestions, so I can make informed decisions.
- **Acceptance Criteria**:
  - Given a chat window, when a user sends a query, then theiseerde AI processes within 2 seconds and returns a response.
  - Given the AI identifies a product, then it highlights the 3D asset in the showroom.
  - Given the AI fails, then the system logs the error with stack trace and notifies the admin.
- **Data Inputs & Field Validations**:
  - Query: required, max 512 chars.
  - Session ID: required, UUID.

### Epic 5: Integration & Embedding
- **User Story**: As a SuperAdmin, I want to generate an embed code so that my website can display the showroom.
- **Acceptance Criteria**:
  - Given a showroom ID, when I request embed code, then the system returns a script tag with a unique token.
  - The token expires after 30 days unless refreshed by the owner.
  - The embed renders on any responsive web page within 800ms.
- **Data Inputs & Field Validations**:
  - Showroom ID: required, UUID.
  - Referrer: optional, validated against whitelisted domains.

### Epic 6: Analytics & Reporting
- **User Story**: As an Admin, I want to view visitor metrics so that I can optimize showroom performance.
- **Acceptance Criteria**:
  - Given a date range, when I request report, then the system returns metrics within 500ms.
  - Report includes: page views, unique visitors, average engagement time, conversion rate.
- **Data Inputs & Field Validations**:
  - Date range: start_date ≤ end_date, max span 90 days.
  - Granularity: daily, weekly, monthly.

## 3. EXCEPTION FLOWS & EDGE CASES
- **Network & Connectivity Drops**
  - The client retries failed requests up to 3 times with exponential backoff (initial 1s, max 8s). If all retries fail, the system displays a user‑friendly error and logs the incident.
- **Invalid Inputs & Concurrency Issues**
  - When simultaneous edits occur onقاط layout, the system implements optimistic locking using version numbers. If a conflict is detected, the user receives a merge prompt.
  - Input sanitization prevents XSS: alldaan fields are encoded server‑side.
- **System Recovery & Error Notifications**
  - Critical failures trigger an incident ticket in ServiceNow with severity level 1. The system auto‑restarts affected microservices via Kubernetes liveness probes.
  - Audit logs capture every state change: user actions, errors, system shredded.

## 4. NON-FUNCTIONAL REQUIREMENTS
- **Performance Metrics**
  - First Byte (F1B) for embed script ≤ 200ms under 95th percentile.
  - Asset upload 90th percentile ≤ 3s.
  - AI response time ≤ 2s for 95% of requests.
- **Security**
  - All REST endpoints use HTTPS with TLS 1.3.
  - JWT tokens signed with RS256, 24h expiry, refresh token 30 days.
  - Data at rest encrypted with AES‑256.
  - OWASP ASVS Level 3 compliance, including input validation, session management, and privilege separation.
- **Scalability & Availability**
  - System deployed in AWS Multi‑AZ, with auto‑scaling groups for API, frontend, and AI services.
  - 99.9% uptime SLA. RTO ≤ 15min, RPO ≤ 5min.
  - CDN caching for static assets, with 24h TTL.

## 5. PRELIMINARY DATA DICTIONARY
- **users**
  - id: UUID, PK, NOT NULL.
  - email: VARCHAR(256), UNIQUE, NOT NULL.
  - password_hash: CHAR(64), NOT NULL.
  - role: ENUM('SuperAdmin','Admin','Editor','Viewer'), NOT NULL.
  - created_at: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP.
  - updated_at: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP.
  - created_by: UUID, FK to users.id.
  - updated_by: UUID, FK to users.id.

- **assets**
  - id: UUID, PK, NOT NULL.
  - user_id: UUID, FK to users.id, NOT NULL.
  - title: VARCHAR(256), NOT NULL.
  - description: TEXT.
  - tags: JSONB.
  - s3_key: VARCHAR(512), NOT NULL.
  - mime_type: VARCHAR(50), NOT NULL.
  - size_bytes: BIGINT, NOT NULL.
  - created_at: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP.

- **showrooms**
  - id: UUID, PK prom.
  - owner_id: UUID, FK to users.id, NOT NULL.
  - name: VARCHAR(256), NOT NULL.
  - description: TEXT.
  - layout_json: JSONB, NOT NULL.
  - version: INT, NOT NULL, DEFAULT 1.
  - created_at: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP.

- **chat_sessions**
  - id: UUID, PK, NOT NULL.
  - showroom_id: UUID, FK to showrooms.id, NOT NULL.
  - user_id: UUID, FK to users.id.
  - token: CHAR(256), UNIQUE, NOT NULL.
  - expires_at: TIMESTAMP, NOT NULL.
  - created_at: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP.

- **audit_logs**
  - id: BIGSERIAL, PK, NOT NULL.
  - user_id: UUID, FK to users.id.
  - action: VARCHAR(256), NOT NULL.
  - entity: VARCHAR(128), NOT NULL.
  - entity_id: UUID.
  - metadata: JSONB.
  - timestamp: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP.
