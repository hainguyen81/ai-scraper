# SOFTWARE REQUIREMENTS SPECIFICATION: financial-reconciliation

## 1. PROJECT OVERVIEW & GLOBAL ARCHITECTURE

### Product Objectives & Core Values
- [ARC-021] **Global Tech Stack Constraints & Infrastructure Blueprint**: Lightweight monolithic architecture, Spring Boot 3.x, Java 17/21 LTS, PostgreSQL/MySQL, HTML5/Thymeleaf/Tailwind CSS, Alibaba EasyExcel with SAX-based streaming, Spring Batch & `@Async` for background processing, drag-and-drop file ingestion.

### Target User Personas
- C‑level executives ( initiators, dashboard consumers )
- Operations managers ( session oversight, report generation )
- Data analysts ( variance review, export for audit )
- System auditors ( compliance, log review )

### Global Role‑Based Access Control (RBAC) Matrix
- [ARC-001] SuperAdmin → FileUpload
- [ARC-002] SuperAdmin → ViewSessionList
- [ARC-003] SuperAdmin → RunReconciliation
- [ARC-004] SuperAdmin → ViewDashboard
- [ARC-005] SuperAdmin → ExportReport
- [ARC-006] SuperAdmin → ManageUsers
- [ARC-007] SuperAdmin → ConfigureSettings
- [ARC-008] SuperAdmin → ViewAuditLogs
- [ARC-009] OperationsManager → FileUpload
- [ARC-010] OperationsManager → ViewSessionList
- [ARC-011] OperationsManager → RunReconciliation
- [ARC-012] OperationsManager → ViewDashboard
- [ARC-013] OperationsManager → ExportReport
- [ARC-014] Analyst → ViewSessionList
- [ARC-015] Analyst → ViewDashboard
- [ARC-016] Analyst → ExportReport
- [ARC-017] Auditor → ViewSessionList
- [ARC-018] Auditor → ViewDashboard
- [ARC-019] Auditor → ExportReport
- [ARC-020] Auditor → ViewAuditLogs

### Enterprise Architectural Compliance
- [ARC-022] Zero Application‑Level Loops: All bulk analytical work is delegated to native SQL set operations; Java threads never iterate over enterprise data sets.
- [ARC-023] Non‑Blocking Non‑Leaking Thread Models: File upload handlers release worker threads within < 200 ms; heavy ingestion runs in isolated background processes.
- [ARC-024] Guaranteed Low Memory Footprint: SAX‑based EasyExcel prevents `OutOfMemoryError`; legacy Apache POI usage is prohibited.

## 2. ENHANCED EPIC MODULES

### 2.1 Data Ingestion Module

#### Core Functional Requirements
- [REQ-001] As a C‑level executive, I want to upload marketplace and logistics ledger files to initiate a reconciliation session, so that automated variance analysis can commence.

#### Acceptance Criteria & Interactions
- Given the user is authenticated and holds the **FileUpload** permission, when the user selects and drops Excel/CSV files for both ledgers, then a new **ReconciliationSession** is created with status **PROCESSING** and a **SessionId** is returned.
- Given a session exists with status **PROCESSING**, when the background worker completes file parsing via EasyExcel, then the session status updates to **COMPLETED** and aggregated metrics are stored.

#### Module Exception Flows
- [EXC-001] Uploaded file format invalid or corrupted → session status **FAILED** with detailed error payload.
- [EXC-004] File size exceeds allowed limit (e.g., > 500 MB) → reject with **PAYLOAD_TOO_LARGE** error.

#### Module Localized Data Dictionary
- [DAT-001] **TempShopeeOrder**
```mermaid
erDiagram
    ReconciliationSession {
        bigint id PK "Primary key identifier for the session"
        varchar userId "" "User identifier who initiated the session"
        timestamp createdAt "" "Timestamp when the session was created"
        varchar status "" "Current status of the session (PENDING, PROCESSING, COMPLETED, FAILED)"
        decimal totalDiscrepancyAmount "" "Total discrepancy amount (Financial Leakage Metric X)"
        decimal totalHoldingAmount "" "Total holding amount (Escrow Tracking Metric Y)"
        decimal totalSafeAmount "" "Total safe amount (Safe Realized Income Metric Z)"
    }
    TempShopeeOrder {
        bigint id PK "Primary key identifier for the Shopee order record"
        bigint sessionId FK "" "Foreign key referencing ReconciliationSession.id"
        varchar orderId "" "Unique order identifier from marketplace"
        decimal shopFee "" "Platform‑calculated shipping fee"
        varchar orderStatus "" "Order status from marketplace"
        decimal payoutAmount "" "Payout amount associated with the order"
    }
    TempLogisticsOrder {
        bigint id PK "Primary key identifier for the logistics order record"
        bigint sessionId FK "" "Foreign key referencing ReconciliationSession.id"
        varchar orderId "" "Unique order identifier from carrier"
        decimal shippingFee "" "Actual carrier‑charged shipping fee"
        varchar deliveryStatus "" "Delivery status from logistics provider"
    }
    ReconciliationSession ||--o{ TempShopeeOrder : "sessionId"
    ReconciliationSession ||--o{ TempLogisticsOrder : "sessionId"
```
- [DAT-002] **TempLogisticsOrder**
```mermaid
erDiagram
    ReconciliationSession {
        bigint id PK "Primary key identifier for the session"
        varchar userId "" "User identifier who initiated the session"
        timestamp createdAt "" "Timestamp when the session was created"
        varchar status "" "Current status of the session (PENDING, PROCESSING, COMPLETED, FAILED)"
        decimal totalDiscrepancyAmount "" "Total discrepancy amount (Financial Leakage Metric X)"
        decimal totalHoldingAmount "" "Total holding amount (Escrow Tracking Metric Y)"
        decimal totalSafeAmount "" "Total safe amount (Safe Realized Income Metric Z)"
    }
    TempShopeeOrder {
        bigint id PK "Primary key identifier for the Shopee order record"
        bigint sessionId FK "" "Foreign key referencing ReconciliationSession.id"
        varchar orderId "" "Unique order identifier from marketplace"
        decimal shopFee "" "Platform‑calculated shipping fee"
        varchar orderStatus "" "Order status from marketplace"
        decimal payoutAmount "" "Payout amount associated with the order"
    }
    TempLogisticsOrder {
        bigint id PK "Primary key identifier for the logistics order record"
        bigint sessionId FK "" "Foreign key referencing ReconciliationSession.id"
        varchar orderId "" "Unique order identifier from carrier"
        decimal shippingFee "" "Actual carrier‑charged shipping fee"
        varchar deliveryStatus "" "Delivery status from logistics provider"
    }
    ReconciliationSession ||--o{ TempShopeeOrder : "sessionId"
    ReconciliationSession ||--o{ TempLogisticsOrder : "sessionId"
```
- [DAT-003] **ReconciliationSession**
```mermaid
erDiagram
    ReconciliationSession {
        bigint id PK "Primary key identifier for the session"
        varchar userId "" "User identifier who initiated the session"
        timestamp createdAt "" "Timestamp when the session was created"
        varchar status "" "Current status of the session (PENDING, PROCESSING, COMPLETED, FAILED)"
        decimal totalDiscrepancyAmount "" "Total discrepancy amount (Financial Leakage Metric X)"
        decimal totalHoldingAmount "" "Total holding amount (Escrow Tracking Metric Y)"
        decimal totalSafeAmount "" "Total safe amount (Safe Realized Income Metric Z)"
    }
```

### 2.2 Reconciliation Engine Module

#### Core Functional Requirements
- [REQ-002] As a system user, I want the platform to automatically process uploaded files and generate variance calculations, so that discrepancies are identified without manual intervention.

#### Acceptance Criteria & Interactions
- Given a session exists with status **PROCESSING**, when the native SQL variance query executes, then the system updates **ReconciliationSession** totals based on computed variances.
- Given variance calculation completes, when the session status updates, then the session is marked **COMPLETED**.

#### Module Exception Flows
- [EXC-002] Duplicate order IDs across streams within same session → conflict flagged, session status **PARTIAL**.
- [EXC-005] Database constraint violation during variance insertion → session status **FAILED** with detailed error log.

#### Module Localized Data Dictionary
- [DAT-004] **TempShopeeOrder**
```mermaid
erDiagram
    ReconciliationSession {
        bigint id PK "Primary key identifier for the session"
        varchar userId "" "User identifier who initiated the session"
        timestamp createdAt "" "Timestamp when the session was created"
        varchar status "" "Current status of the session (PENDING, PROCESSING, COMPLETED, FAILED)"
        decimal totalDiscrepancyAmount "" "Total discrepancy amount (Financial Leakage Metric X)"
        decimal totalHoldingAmount "" "Total holding amount (Escrow Tracking Metric Y)"
        decimal totalSafeAmount "" "Total safe amount (Safe Realized Income Metric Z)"
    }
    TempShopeeOrder {
        bigint id PK "Primary key identifier for the Shopee order record"
        bigint sessionId FK "" "Foreign key referencing ReconciliationSession.id"
        varchar orderId "" "Unique order identifier from marketplace"
        decimal shopFee "" "Platform‑calculated shipping fee"
        varchar orderStatus "" "Order status from marketplace"
        decimal payoutAmount "" "Payout amount associated with the order"
    }
    TempLogisticsOrder {
        bigint id PK "Primary key identifier for the logistics order record"
        bigint sessionId FK "" "Foreign key referencing ReconciliationSession.id"
        varchar orderId "" "Unique order identifier from carrier"
        decimal shippingFee "" "Actual carrier‑charged shipping fee"
        varchar deliveryStatus "" "Delivery status from logistics provider"
    }
    ReconciliationSession ||--o{ TempShopeeOrder : "sessionId"
    ReconciliationSession ||--o{ TempLogisticsOrder : "sessionId"
```
- [DAT-005] **TempLogisticsOrder**
```mermaid
erDiagram
    ReconciliationSession {
        bigint id PK "Primary key identifier for the session"
        varchar userId "" "User identifier who initiated the session"
        timestamp createdAt "" "Timestamp when the session was created"
        varchar status "" "Current status of the session (PENDING, PROCESSING, COMPLETED, FAILED)"
        decimal totalDiscrepancyAmount "" "Total discrepancy amount (Financial Leakage Metric X)"
        decimal totalHoldingAmount "" "Total holding amount (Escrow Tracking Metric Y)"
        decimal totalSafeAmount "" "Total safe amount (Safe Realized Income Metric Z)"
    }
    TempShopeeOrder {
        bigint id PK "Primary key identifier for the Shopee order record"
        bigint sessionId FK "" "Foreign key referencing ReconciliationSession.id"
        varchar orderId "" "Unique order identifier from marketplace"
        decimal shopFee "" "Platform‑calculated shipping fee"
        varchar orderStatus "" "Order status from marketplace"
        decimal payoutAmount "" "Payout amount associated with the order"
    }
    TempLogisticsOrder {
        bigint id PK "Primary key identifier for the logistics order record"
        bigint sessionId FK "" "Foreign key referencing ReconciliationSession.id"
        varchar orderId "" "Unique order identifier from carrier"
        decimal shippingFee "" "Actual carrier‑charged shipping fee"
        varchar deliveryStatus "" "Delivery status from logistics provider"
    }
    ReconciliationSession ||--o{ TempShopeeOrder : "sessionId"
    ReconciliationSession ||--o{ TempLogisticsOrder : "sessionId"
```
- [DAT-006] **ReconciliationSession**
```mermaid
erDiagram
    ReconciliationSession {
        bigint id PK "Primary key identifier for the session"
        varchar userId "" "User identifier who initiated the session"
        timestamp createdAt "" "Timestamp when the session was created"
        varchar status "" "Current status of the session (PENDING, PROCESSING, COMPLETED, FAILED)"
        decimal totalDiscrepancyAmount "" "Total discrepancy amount (Financial Leakage Metric X)"
        decimal totalHoldingAmount "" "Total holding amount (Escrow Tracking Metric Y)"
        decimal totalSafeAmount "" "Total safe amount (Safe Realized Income Metric Z)"
    }
```

### 2.3 Executive Dashboard Module

#### Core Functional Requirements
- [REQ-003] As a C‑level executive, I want to view the executive financial dashboard summarizing leaked, escrow, and safe capital, so that I can monitor financial health.

#### Acceptance Criteria & Interactions
- Given a valid **sessionId**, when the executive accesses the dashboard, then the UI renders three metric cards: **Leaked Capital (X)**, **Escrow Capital (Y)**, **Safe Income (Z)** fetched from **ReconciliationSession**.
- Given the export action is triggered, when the user selects CSV/Excel format, then the system generates a downloadable report with detailed discrepancy records.

#### Module Exception Flows
- [EXC-003] Session not found or unauthorized access → HTTP **404** / **403** with error payload.
- [EXC-001] Invalid export format requested → reject with **BAD_REQUEST**.

#### Module Localized Data Dictionary
- [DAT-007] **ReconciliationSession**
```mermaid
erDiagram
    ReconciliationSession {
        bigint id PK "Primary key identifier for the session"
        varchar userId "" "User identifier who initiated the session"
        timestamp createdAt "" "Timestamp when the session was created"
        varchar status "" "Current status of the session (PENDING, PROCESSING, COMPLETED, FAILED)"
        decimal totalDiscrepancyAmount "" "Total discrepancy amount (Financial Leakage Metric X)"
        decimal totalHoldingAmount "" "Total holding amount (Escrow Tracking Metric Y)"
        decimal totalSafeAmount "" "Total safe amount (Safe Realized Income Metric Z)"
    }
```

## 3. GLOBAL NON‑FUNCTIONAL REQUIREMENTS

- [NFR-001] **Performance Metrics**: End‑to‑end processing latency < 5 seconds for files up to 500 MB; throughput > 10 000 rows/second; real‑time session status updates via WebSocket.
- [NFR-002] **Security**: AES‑256 encryption at rest; TLS 1.3 for all in‑transit traffic; JWT‑based authentication with OAuth2 resource servers; role‑based access control enforced at API gateway; comprehensive audit logging; OWASP Top 10 mitigation (SQL injection, XSS, insecure deserialization).
- [NFR-003] **Scalability & Multi‑Tenant Isolation**: Stateless services horizontally scalable; database schemas partitioned by tenant ID; shared infrastructure with isolated schemas; auto‑scaling based on CPU/memory metrics.
- [NFR-004] **Availability & Reliability**: 99.9 % SLA; active‑passive failover across regions; health‑check endpoints; automatic retry for transient failures; circuit‑breaker patterns for downstream APIs.
- [NFR-005] **Compliance & Data Governance**: GDPR‑aligned data handling; configurable data residency; immutable audit trails retained ≥ 7 years; export capabilities for regulatory requests; data masking for PII in reports.