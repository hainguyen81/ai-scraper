# PHASE 3 CONTEXT BLUEPRINT: financial-reconciliation
## 1. Phase Operational Scope & Objectives
| Goal | Description |
|------|-------------|
| **Core Implementation** | Build the **Native Reconciliation Logic** that runs **exclusively via native SQL** to compute three C‑level KPI aggregates per reconciliation session: <br>1. **Leaked Capital (X)** – variance between marketplace‑calculated fees (`shop_fee`) and carrier‑charged fees (`shipping_fee`). <br>2. **Escrow/Holding Capital (Y)** – sum of `payout_amount` for orders where `order_status` = *Delivered* but `delivery_status` ≠ *Settled* (or equivalent business rule). <br>3. **Settled/Safe Capital (Z)** – sum of `payout_amount` for orders where both `order_status` and `delivery_status` indicate successful settlement. |
| **Service Exposure** | Provide a **REST‑style service** (`POST /api/sessions/{sessionId}/reconcile`) that triggers the computation for a given `sessionId`. The service must: <br>• Execute the three native SQL statements within a single transaction. <br>• Persist the resulting `totalDiscrepancyAmount`, `totalHoldingAmount`, `totalSafeAmount` back to the `ReconciliationSession` entity. <br>• Log any anomalies (missing matches, data‑type mismatches) to the centralized ELK stack. |
| **Guardrail Compliance** | • **Zero Application‑Level Loops** – All heavy calculations must be expressed as native SQL; no Java `for/while` over `TempShopeeOrder`/`TempLogisticsOrder`. <br>• **Session Isolation** – All queries are scoped to the provided `sessionId` via foreign‑key constraints. <br>• **Error Handling & Logging** – Graceful handling of `NULL`, type‑mismatch, and missing counterpart rows; audit‑ready logs. |
| **Deliverable Artifacts** | • Native SQL queries (JPA `@Query` annotated interfaces). <br>• `ReconciliationService` implementation. <br>• Updated `ReconciliationSession` fields populated. <br>• Unit & integration test coverage. <br>• CI‑verified code review sign‑off. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Layer | Path / File | Purpose |
|-------|-------------|---------|
| **Domain / Entities** | `src/main/java/com/finrec/model/ReconciliationSession.java` | Existing entity – will be updated with computed fields. |
| | `src/main/java/com/finrec/model/TempShopeeOrder.java` | Existing staging entity – read‑only for queries. |
| | `src/main/java/com/finrec/model/TempLogisticsOrder.java` | Existing staging entity – read‑only for queries. |
| **Repository / Native SQL** | `src/main/java/com/finrec/repository/NativeReconciliationRepository.java` | JPA repository exposing `@Query` methods for variance, leakage, escrow, safe calculations. |
| **Service** | `src/main/java/com/finrec/service/ReconciliationService.java` | Core service that orchestrates the three native queries and updates the session. |
| | `src/main/java/com/finrec/config/ReconciliationConfig.java` | Optional Spring config (e.g., transaction manager) – if needed. |
| **Controller** | `src/main/java/com/finrec/controller/ReconciliationController.java` | Exposes `POST /api/sessions/{sessionId}/reconcile` and `GET /api/sessions/{sessionId}/metrics`. |
| **Test – Unit** | `src/test/java/com/finrec/repository/NativeReconciliationRepositoryTest.java` | JUnit tests for native SQL queries (using an in‑memory DB). |
| | `src/test/java/com/finrec/service/ReconciliationServiceTest.java` | Integration tests for service logic, mocking repository. |
| **Test – Performance** | `src/test/java/com/finrec/performance/ReconciliationLoadTest.java` | Load test verifying sub‑200 ms response and memory usage (optional). |
| **CI / DevOps** | `Dockerfile` (root) | Existing image – new code will be built automatically. |
| | `github/workflows/ci.yml` | Existing pipeline – will run static analysis, unit tests, security scans. |
| **Logging** | `src/main/java/com/finrec/logging/ReconciliationLogger.java` (or use SLF4J) | Structured logging for anomalies. |
| **Documentation** | `docs/phase3-design.md` | Phase‑specific design notes (optional). |

**Endpoint Specification**
- `POST /api/sessions/{sessionId}/reconcile` – triggers reconciliation; returns `202 Accepted` with `sessionId`. <br>Response may include a polling link to `GET /api/sessions/{sessionId}/metrics` once completed.
- `GET /api/sessions/{sessionId}/metrics` – returns the three KPI amounts (`totalDiscrepancyAmount`, `totalHoldingAmount`, `totalSafeAmount`).

**Boundary Rules**
- **Do NOT** modify any ingestion (`/upload`), UI, or deployment files outside the scope above. <br>All changes must be confined to the paths listed. <br>Any attempt to introduce loops over staging tables will be flagged by static analysis and must be removed.

## 3. Dedicated Sub-Agent Functional Directives
| Sub‑Agent | Specific Tasks & Deliverables |
|-----------|------------------------------|
| **Coder** | 1. **Implement Native SQL Queries** – Add three `@Query` methods to `NativeReconciliationRepository`: <br>   - `List<VarianceRecord> findVariance(@Param("sessionId") Long sessionId)` (mirrors the provided SQL). <br>   - `BigDecimal calculateLeakedCapital(@Param("sessionId") Long sessionId)` (sum of variance). <br>   - `BigDecimal calculateEscrowHolding(@Param("sessionId") Long sessionId)` (business rule aggregation). <br>   - `BigDecimal calculateSafeIncome(@Param("sessionId") Long sessionId)` (successful settlement sum). <br>2. **Create `ReconciliationService`** – <br>   - `public void reconcile(Long sessionId)` that calls the four repository methods within a single `@Transactional` block. <br>   - Update `ReconciliationSession` fields with the returned aggregates. <br>   - Log each step using SLF4J (e.g., `reconLogger.info("Reconciliation completed for session {}", sessionId)`). <br>3. **Error Handling** – Wrap repository calls in try‑catch; log `ReconciliationException` for missing rows, data‑type mismatches, or constraint violations. <br>4. **Controller** – Expose the service via `ReconciliationController`. Return appropriate HTTP status codes (`202`, `200`, `500`). <br>5. **Code Quality** – Ensure **no Java loops** over `TempShopeeOrder`/`TempLogisticsOrder`. Use only native SQL. Run static analysis (SonarQube) to confirm. |
| **Tester** | 1. **Unit Tests for Native Queries** – Verify each `@Query` returns expected results using an embedded PostgreSQL (or MySQL) test DB. Include edge cases: zero variance, NULL fees, mismatched order IDs. <br>2. **Integration Tests for Service** – Mock repository calls to test service orchestration, transaction rollback, and session update logic. <br>3. **Guardrail Compliance Tests** – Write a test that scans compiled bytecode (or uses static analysis plugin) to confirm **no loops** over staging tables exist. <br>4. **Performance / Load Tests** – Simulate a session with >10 k rows (using generated CSV → Excel) and assert that the reconciliation completes within **< 500 ms** and does not cause OOM (monitor JVM memory). <br>5. **Error‑Path Tests** – Inject malformed data (e.g., non‑numeric fee) and verify graceful logging and exception handling. |
| **Reviewer** | 1. **Architectural Review** – Confirm that all calculations are performed via native SQL and that the service respects session isolation. <br>2. **Security & Guardrails** – Validate that the implementation does not introduce SQL injection risks (parameterized queries), that JWT/RBAC remains untouched, and that OWASP top‑10 checks pass. <br>3. **Code Review Checklist** – <br>   - No loops over staging tables. <br>   - All SQL is parameterized. <br>   - Logging includes sessionId and operation. <br>   - Exception handling does not leak stack traces to UI. <br>4. **Sign‑off** – Approve the changes for promotion to CI pipeline. |
| **DevOps** | 1. **Container Build** – Ensure the new Java classes are included in the existing `Dockerfile` (no changes needed if using multi‑stage build). <br>2. **CI Pipeline Update** – Add a new step in `github/workflows/ci.yml` that runs the **Phase‑3 specific tests** (unit + performance) and fails the build on any guardrail violation. <br>3. **Monitoring Integration** – Add Prometheus metrics for reconciliation latency (`reconciliation_duration_seconds`) and error rate (`reconciliation_errors_total`). <br>4. **Logging Stack** – Verify that `ReconciliationLogger` outputs JSON format compatible with ELK. <br>5. **Environment Provisioning** – No new environments required; the existing staging/production containers will pick up the updated image. |
| **Manager** | 1. **Scope Validation** – Confirm that Phase‑3 deliverables meet the **Phase Definition of Done** (see below). <br>2. **Resource Allocation** – Ensure Coder, Tester, Reviewer, and DevOps have the required time slots within the 2‑3 day window. <br>3. **Go/No‑Go Decision** – Provide final approval to proceed to Phase 4 once all sign‑offs are collected. |

## 4. Phase Definition of Done (DoD)
| Checklist Item | Verification Method |
|----------------|----------------------|
| **Native SQL Queries Implemented** | Repository contains four `@Query` methods; each method is annotated with `@Transactional(readOnly = true)` where appropriate. |
| **Service Orchestration** | `ReconciliationService.reconcile(Long sessionId)` correctly calls repository methods, updates `ReconciliationSession` fields, and commits within a single transaction. |
| **Controller Endpoints** | `POST /api/sessions/{sessionId}/reconcile` returns `202 Accepted`; `GET /api/sessions/{sessionId}/metrics` returns the three KPI amounts. |
| **Guardrail Compliance** | Static analysis (SonarQube) reports **zero loops** over `TempShopeeOrder`/`TempLogisticsOrder`; all heavy calculations are native SQL. |
| **Error Handling & Logging** | All anomalies (missing matches, type mismatches) are caught, logged via SLF4J with sessionId context, and do not propagate stack traces to the client. |
| **Unit & Integration Tests** | All tests in `NativeReconciliationRepositoryTest` and `ReconciliationServiceTest` pass > 90 % coverage; guardrail test passes. |
| **Performance Validation** | Load test with ≥10 k rows completes within **< 500 ms** and memory usage stays below the configured threshold; no OOM. |
| **Security Review** | Reviewer signs off; OWASP scan shows no new vulnerabilities; SQL injection checks pass. |
| **CI/CD Integration** | Pipeline runs Phase‑3 tests, fails on any violation, and pushes the Docker image to the artifact registry. |
| **Monitoring & Observability** | Prometheus metrics (`reconciliation_duration_seconds`, `reconciliation_errors_total`) are emitted; logs are forwarded to ELK. |
| **Documentation** | Phase‑specific design notes (`docs/phase3-design.md`) capture query logic, error codes, and assumptions. |
| **Managerial Sign‑off** | Manager confirms all above items are satisfied and authorizes transition to Phase 4. |

**Result:** Upon completion of the above checklist, the **Native Reconciliation Logic & Metric Computation** phase is considered delivered, and the project can safely advance to **Phase 4 – Executive Dashboard & Export Features**.