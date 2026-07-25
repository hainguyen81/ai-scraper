## 1. PROJECT OVERVIEW
- Product Objectives & Core Values
   - Tối ưu hoá giá bán dựa trên AI, đồng bộ tồn kho thời gian thực, lên lịch quảng cáo đa kênh.
   - Đảm bảo sự đơn giản, hiệu quả, bảo mật.
- Target User Personas
   - Chủ shop nhỏ (1-10 SKU), người mới bắt đầu, startup thương mại điện tử.
- Role-Based Access Control (RBAC) Matrix
   - Admin: Quản lý hệ thống, cấu hình kênh, xem báo cáo.
   - Merchant: Quản lý sản phẩm, giá, chiến dịch, xem KPI.
   - Analyst: Xem báo cáo chi tiết, xuất dữ liệu.

## 2. FUNCTIONAL REQUIREMENTS
**Epic Module: Autonomous Pricing Engine**
- Feature: AI Pricing Suggestion
   - User Story: As a Merchant I want to receive daily suggested price ranges for each SKU so that I can stay competitive.
   - Acceptance Criteria:
     Given the system has been seeded with competitor data for the last 7 days, when the pricing engine runs at 03:00 AM, then the system should generate price suggestions within 30 seconds and store them in the database.
   - Data Inputs & Field Validations:
     - SKU_ID (string, not null, uuid), Current_Price (decimal, >=0), Competitor_Prices (array of decimal, length >=1), Demand_Score (decimal, 0-1).

**Epic Module: Inventory Sync**
- Feature: Real-Time Stock Sync
   - User Story: As a Merchant I want the inventory levels to sync automatically from my ERP/API so that I never oversell.
   - Acceptance Criteria:
     Given the ERP pushes a stock update payload, when the webhook is received, then the system updates the SKU stock within 5 seconds and logs the change.
   - Data Inputs & Field Validations:
     - SKU_ID, Stock_Quantity (int, >=0), Updated_At (datetime, UTC).

**Epic Module: Advertising Scheduler**
- Feature: Drag‑and‑Drop Campaign Builder
   - User Story: As a Merchant I want to drag and drop ad creatives into a timeline so that I can schedule posts across Instagram, Facebook, and Google Shopping.
   - Acceptance Criteria:
     Given a campaign timeline layout, when the user drops an image, then the system validates the image size (<5MB) and schedule time (>=current time), stores the plan, and triggers API calls at scheduled time.
   - Data Inputs & Field Validations:
     - Campaign_ID, Platform (enum), Creative_File (image/jpeg/png), Start_Time, End_Time, Target_Audience (json).

**Epic Module: User Management**
- Feature: OAuth2 + MFA
   - User Story: As an Admin I want to enforce MFA for all users so that the system remains secure.
   - Acceptance Criteria:
     Given a user in state 'PENDING_MFA', when the user completes MFA, then the account is set to ACTIVE and access token is issued.
   - Data Inputs & Field Validations:
     - User_ID Mik, Email, Password (hashed, bcrypt), Phone_Number (E.164), MFA_Method (sms/email).

**Epic Module: Analytics Dashboard**
- Feature: KPI Reporting
   - User Story: As a Merchant I want to view daily sales, conversion, and ROI metrics so that I can adjust strategies.
   - Acceptance Criteria:
     Given the last 30 days of data, when the dashboard loads, then it displays charts within 2 seconds and allows export to CSV.
   - Data Inputs & Field Validations:
     - Sale_Amount (decimal), Order_Count (int), Campaign_ID, Date.

## 3. EXCEPTION FLOWS & EDGE CASES
- Network & Connectivity Drops
   - The system retries failed API calls up to 3 times with exponential backoff (1s, 2s, 4s). If still failing, queues the request in a durable queue for later.
- Invalid Inputs & Concurrency Issues
   - All inputs are validated server‑side; duplicate SKU updates are serialized via optimistic locking (version field). On conflict, return 409 Conflict.
- System Recovery & Error Notifications
   - Errors trigger alerts to DevOps via Slack & email; the system logs are stored in a central audit log.

## 4. NON-FUNCTIONAL REQUIREMENTS
- Performance Metrics
   - API response time <= 200 ms for 95% of requests.
   - Pricing engine recomputes all SKUs within 5 minutes.
- Security
   - Data at rest encrypted with AES-256.
   - Token based auth (JWT) with 24h expiry, refresh tokens 30 days.
   - OWASP Top 10 controls: XSS, CSRF, Injection mitigated.
- Scalability & Availability
   - Auto‑scaling groups with min 2 nodes, max 10.
   - 99.9% uptime SLA, graceful failover across 2 AZs.

## 5. PRELIMINARY DATA DICTIONARY
- **Table: Users**
   - user_id (UUID, PK, NOT NULL)
   - email (VARCHAR(255), UNIQUE, NOT NULL)
   - password_hash (VARCHAR(255), NOT NULL)
   - phone_number (VARCHAR(20))
   - role (ENUM('Admin','Merchant','Analyst'))
   - status (ENUM('ACTIVE','PENDING_MFA','INACTIVE'))
   - created_at (TIMESTAMP, NOT NULL)
- **Table: Products**
   - sku_id (UUID, PK, NOT NULL)
   - merchant_id (UUID, FK to Users, NOT NULL)
   - title (VARCHAR(255), NOT NULL)
   - description (TEXT)
   - price (DECIMAL(10,2), NOT NULL)
   - stock_quantity (INT, NOT NULL)
   - updated_at (TIMESTAMP, NOT NULL)
- **Table: Price_Suggestions**
   - suggestion_id (UUID, PK)
   - sku_id (UUID, FK, NOT NULL)
   - suggested_price (DECIMAL(10,2), NOT NULL)
   - confidence_score (DECIMAL(5,4) NOT NULL)
   - generated_at (TIMESTAMP, NOT NULL)
- **Table: Campaigns**
   - campaign_id (UUID, PK)
   - merchant_id (UUID, FK, NOT NULL)
   - platform (ENUM('Instagram','Facebook','GoogleShopping'))
   - status (ENUM('DRAFT','SCHEDULED','RUNNING','COMPLETED'))
   - start_time (TIMESTAMP, NOT NULL)
   - end_time (TIMESTAMP, NOT NULL)
   - creative_file (VARCHAR(255), NOT NULL)
   - target_audience (JSON)
   - created_at (TIMESTAMP, NOT NULL)
- **Table: Audits**
   - audit_id (UUID, PK)
   - user_id (UUID, FK)
   - action (VARCHAR(50), NOT NULL)
   - target_table (VARCHAR(50))
   - target_id (UUID)
   - payload (JSON)
   - timestamp (TIMESTAMP, NOT NULL)
