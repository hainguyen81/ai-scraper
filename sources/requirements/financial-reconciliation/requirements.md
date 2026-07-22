# Project Name: financial-reconciliation

# PRODUCT REQUIREMENTS DOCUMENT (PRD)
## Enterprise Financial Reconciliation Micro-SaaS Platform

---

## 🎯 1. EXECUTIVE SUMMARY & BUSINESS PURPOSE

### 1.1 Problem Statement
E-commerce merchants operating at scale across major marketplaces (e.g., Shopee, TikTok Shop, Lazada) face severe operational inefficiencies and revenue leakage. Discrepancies arise frequently due to miscalculated marketplace shipping fees, untracked/lost customer returns, and complex, delayed multi-channel payout timelines. Manual verification across separate retail enterprise systems is error-prone, labor-intensive, and leads to significant financial loss.

### 1.2 Proposed Solution (MVP Scope)
The platform delivers an automated, high-throughput Micro-SaaS Financial Reconciliation Engine. To eliminate the overhead of complex, restricted marketplace API approvals during the initial market-entry phase, the Minimum Viable Product (MVP) utilizes a high-performance file-ingestion architecture. 

The system processes and cross-references two asynchronous data streams:
1. **Stream A (Marketplace Ledger):** Income/payout reports exported from the marketplace merchant administration panel.
2. **Stream B (Logistics Ledger):** Fulfillment and shipping statements provided by third-party logistics (3PL) carriers (e.g., GHN, GHTK, Viettel Post).

### 1.3 Business Value & Core Deliverables
The system algorithmically matches transaction records via unique identifiers, calculates precise bottom-line variances, and projects data onto a C-level executive dashboard showcasing:
* **Leaked Capital ($X$ USD/VND):** Unrecovered funds due to logistics or platform billing anomalies.
* **Escrow/Holding Capital ($Y$ USD/VND):** Successfully delivered orders pending platform disbursement.
* **Settled/Safe Capital ($Z$ USD/VND):** Fully reconciled transactions verified against net bank-inflows.

---

## 🛠️ 2. ENTERPRISE ARCHITECTURE & TECH STACK

To maintain a lean operational cost structure while serving high-volume data payloads, the system implements a lightweight **Monolithic Architecture** optimized for maximum memory efficiency on cost-effective virtual private servers.

* **Backend Core:** Spring Boot 3.x | Java 17 or Java 21 (LTS releases).
* **High-Throughput File Ingestion:** 
    * **Alibaba EasyExcel:** Leverages SAX-based event-driven streaming to parse large-scale datasets line-by-line. This design effectively mitigates `OutOfMemoryError` risks when dealing with files containing millions of data rows (spanning dozens of megabytes).
    * **Spring Batch / `@Async` Engine:** Handles asynchronous, background queue management for file-processing tasks, preventing user interface lockups and optimizing concurrent multi-threaded execution.
* **Database Architecture:** PostgreSQL or MySQL. Computations are pushed entirely to the database layer via native relational set-operations rather than executing resource-heavy processing in-memory within the Java Virtual Machine (JVM).
* **Frontend Layer:** HTML5, Thymeleaf, and Tailwind CSS. Provides a responsive, enterprise-ready administration panel supporting drag-and-drop file ingestion via optimized asynchronous JavaScript extensions.

---

## 📋 3. FUNCTIONAL SPECIFICATIONS & SYSTEM PROCESSES

### 3.1 Asynchronous Data Ingestion Pipeline
* **User Experience:** The system provides a unified drag-and-drop secure interface to accept both the Marketplace Ledger and the 3PL Carrier Ledger concurrently.
* **Transaction Lifecycles:** Upon execution, the ingestion API initiates a transaction state, generates a unique `SessionId` (Reconciliation Session Token), updates the session status to `PROCESSING`, and immediately frees the HTTP thread back to the user interface.
* **Background Worker:** The Spring Batch worker stream parses the incoming Excel data through `EasyExcel`, applying strict data-type normalization, and dynamically writes records into isolated staging tables partitioned by the generated `SessionId`.

### 3.2 Core Reconciliation Logic Engine
The core computation bypasses standard application-level iterations. Instead, it utilizes targeted native relational operations to cross-reference data partitions inside the database engine:
* **Shipping Fee Discrepancy Auditing:** Computes variances between the `Platform-Calculated Fee` (Marketplace side) and the `Actual Charged Fee` (3PL side) where `s.shop_fee != v.shipping_fee`.
* **State Verification Auditing:** Flags orders marked as "Delivered" on the marketplace that have missed their payout settlement windows, and audits "Returned" order statuses against physical inventory warehouse receipt registries.

### 3.3 Executive Financial Dashboard
The application compiles analytical data corresponding to the specific `SessionId` and exposes a secure view containing three high-level business metrics:
1. **Financial Leakage Inventory ($X$ Sum):** Aggregated currency loss with direct data-grid exports (Order ID, discrepancy margin) prepared for official platform dispute submissions.
2. **Escrow Tracking ($Y$ Sum):** Outstanding platform capital asset valuations currently tied up in marketplace escrow.
3. **Safe Realized Income ($Z$ Sum):** Verified error-free transaction counts confirming successful revenue realization.

---

## 🗄️ 4. CORE DATABASE & DOMAIN SCHEMA

The system models relationships using a normalized, highly indexed schema design optimized for high-speed JOIN operations:

### 4.1 Reconciliation Session Entity (`ReconciliationSession`)
Manages lifecycle monitoring, metadata tracking, and final computed financial outputs for every batch processing request.
```java
@Entity
@Table(name = "reconciliation_sessions")
public class ReconciliationSession {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "user_id", nullable = false)
    private String userId;
    
    @Column(name = "created_at", nullable = false)
    private LocalDateTime createdAt;
    
    @Enumerated(EnumType.STRING)
    @Column(name = "status", nullable = false)
    private SessionStatus status; // PENDING, PROCESSING, COMPLETED, FAILED
    
    @Column(name = "total_discrepancy_amount", precision = 15, scale = 2)
    private BigDecimal totalDiscrepancyAmount; // Financial Leakage Metric (X)
    
    @Column(name = "total_holding_amount", precision = 15, scale = 2)
    private BigDecimal totalHoldingAmount;     // Escrow Tracking Metric (Y)
    
    @Column(name = "total_safe_amount", precision = 15, scale = 2)
    private BigDecimal totalSafeAmount;        // Safe Realized Income Metric (Z)
}
```

### 4.2 Marketplace Ledger Staging Entity (`TempShopeeOrder`)
```java
@Entity
@Table(name = "temp_shopee_orders", indexes = {
    @Index(name = "idx_shopee_session_order", columnList = "session_id, order_id")
})
public class TempShopeeOrder {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "session_id", nullable = false)
    private Long sessionId; 
    
    @Column(name = "order_id", nullable = false)
    private String orderId; 
    
    @Column(name = "shop_fee", precision = 12, scale = 2)
    private BigDecimal shopFee; // Platform-Calculated Shipping Fee
    
    @Column(name = "order_status")
    private String orderStatus; 
    
    @Column(name = "payout_amount", precision = 12, scale = 2)
    private BigDecimal payoutAmount; 
}
```

### 4.3 Logistics Ledger Staging Entity (`TempLogisticsOrder`)
```java
@Entity
@Table(name = "temp_logistics_orders", indexes = {
    @Index(name = "idx_logistics_session_order", columnList = "session_id, order_id")
})
public class TempLogisticsOrder {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "session_id", nullable = false)
    private Long sessionId;
    
    @Column(name = "order_id", nullable = false)
    private String orderId;
    
    @Column(name = "shipping_fee", precision = 12, scale = 2)
    private BigDecimal shippingFee; // Actual Charged Shipping Fee by Carrier
    
    @Column(name = "delivery_status")
    private String deliveryStatus;  
}
```

---

## ⚙️ 5. OPTIMIZED NATIVE COMPUTATION LOGIC (NATIVE SQL EXECUTABLE)

This optimized, parameterized SQL statement executes directly within the database management system (DBMS) layer via Spring Data JPA `@Query` annotations. It isolates and calculates billing variances efficiently:

```sql
SELECT 
    s.order_id AS orderId, 
    s.shop_fee AS platformCalculatedFee, 
    v.shipping_fee AS carrierActualFee, 
    (s.shop_fee - v.shipping_fee) AS varianceAmount 
FROM 
    temp_shopee_orders s 
INNER JOIN 
    temp_logistics_orders v ON s.order_id = v.order_id 
WHERE 
    s.session_id = :sessionId 
    AND v.session_id = :sessionId
    AND s.shop_fee != v.shipping_fee;
```

---

## 🎯 ENTERPRISE CRITERIA FOR ARCHITECTURAL COMPLIANCE
1. **Zero Application-Level Loops on Bulk Data:** Java application threads must never run standard nested iterations over broad enterprise data sets. All heavy analytical calculations are delegated to indexed, database-native set actions.
2. **Non-Blocking Non-Leaking Thread Models:** All file upload operations must release active server worker pools within `< 200ms`. Heavy ingestion workflows run entirely inside isolated background processes.
3. **Guaranteed Low Memory Footprint:** Standard memory-mapped DOM tree models (e.g., legacy Apache POI) are strictly prohibited to prevent JVM server crashes during peak operational hours.
