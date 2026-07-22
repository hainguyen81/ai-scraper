# PHASE 4 CONTEXT BLUEPRINT: financial-reconciliation
## 1. Phase Operational Scope & Objectives
- **Executive Dashboard UI** – Render a session‑driven view that surfaces the three C‑level KPI cards (Leaked Capital, Escrow/Holding Capital, Settled/Safe Capital) by reading `ReconciliationSession` metrics.  
- **Leakage Inventory Grid** – Display detailed variance rows (order ID, platform fee, carrier fee, variance amount) in a responsive data‑grid with inline CSV/Excel export buttons.  
- **Session Management & Real‑Time Status** – Provide session filtering (dropdown of existing sessions), auto‑refresh (WebSocket or polling), and a live status indicator (PENDING → PROCESSING → COMPLETED/FAILED).  
- **Export Integrity** – Implement streaming export endpoints that generate deterministic CSV or Excel files, include session metadata, and validate row counts against the DB before streaming to the client.  
- **Security & Performance** – Ensure all UI endpoints are protected by Spring Security RBAC, CSRF‑protected, and meet sub‑500 ms dashboard load latency. Export must be memory‑efficient (no full result‑set materialisation).  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Layer | Path / File | Responsibility |
|-------|-------------|----------------|
| **Controller** | `src/main/java/com/example/finrecon/controller/DashboardController.java` | Expose REST endpoints: <br>• `GET /dashboard/{sessionId}` (renders Thymeleaf view) <br>• `GET /api/dashboard/{sessionId}/metrics` (JSON KPI payload) <br>• `GET /api/dashboard/{sessionId}/leakage` (JSON variance rows) <br>• `GET /export/{sessionId}` (streams CSV/Excel; query `?format=csv|excel`) <br>• `GET /ws/sessions` (WebSocket for status push – optional) |
| **Service** | `src/main/java/com/example/finrecon/service/DashboardService.java` | Business logic: <br>• `getSessionMetrics(Long sessionId)` – calls native SQL to fetch `totalDiscrepancyAmount`, `totalHoldingAmount`, `totalSafeAmount` <br>• `getLeakageRows(Long sessionId)` – executes the native variance query from Phase 3 <br>• `exportLeakage(Long sessionId, ExportFormat format)` – streams CSV (via `StreamingResponseBody`) or Excel (via EasyExcel `ExcelWriter`) |
| **Repository** | Existing `ReconciliationSessionRepository`, `TempShopeeOrderRepository`, `TempLogisticsOrderRepository` | Provide native `@Query` methods used by `DashboardService`. No new repository interfaces required. |
| **View (Thymeleaf)** | `src/main/resources/templates/dashboard.html` | Main dashboard page; includes partials and JavaScript for filtering, refresh, and export. |
| | `src/main/resources/templates/partials/kpi-card.html` | Reusable KPI card component. |
| | `src/main/resources/templates/partials/leakage-table.html` | Data‑grid for leakage rows with inline export buttons. |
| | `src/main/resources/templates/partials/session-status.html` | Live session status indicator. |
| **Static / CSS** | `src/main/resources/static/css/dashboard.css` (optional – can reference CDN Tailwind) | Responsive styling; Tailwind classes used throughout templates. |
| **WebSocket Config** | `src/main/java/com/example/finrecon/config/WebSocketConfig.java` | Optional bean to enable `/ws/sessions` for real‑time session status pushes. |
| **Security** | Existing `SecurityConfig.java` | Ensure dashboard and export endpoints require `ROLE_ANALYST` or `ROLE_ADMIN`. |
| **Testing** | `src/test/java/com/example/finrecon/controller/DashboardControllerTest.java` <br>`src/test/java/com/example/finrecon/service/DashboardServiceTest.java` | Unit / integration tests for controller and service layers. |
| **DevOps** | `docker/` – Dockerfile may need to copy new static resources. <br>`github-actions/` – add UI linting, security scan, and integration test steps. | Build, scan, push, and promote container images. |

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)

### Coder
1. **Implement `DashboardController`**  
   - Define REST endpoints as listed.  
   - Use `@PreAuthorize("hasAnyRole('ROLE_ANALYST','ROLE_ADMIN')")` for security.  
   - Return `ModelAndView` for `/dashboard/{sessionId}` that injects sessionId and metrics into Thymeleaf.  
   - For `/api/dashboard/{sessionId}/metrics` and `/api/dashboard/{sessionId}/leakage` return `ResponseEntity<JsonNode>` or DTOs.  
   - For `/export/{sessionId}` set `Content-Type` appropriately and stream the file using `StreamingResponseBody` (CSV) or `ExcelWriter` (Excel) – ensure the stream is closed cleanly.  

2. **Create `DashboardService`**  
   - Write native SQL queries (reuse Phase 3) as `@Query` methods: <br>• `findMetricsBySessionId` → returns `Object[]` with three amounts. <br>• `findLeakageBySessionId` → returns list of `LeakageRowDto` (orderId, platformCalculatedFee, carrierActualFee, varianceAmount). <br>• `exportLeakage` delegates to repository method that returns `InputStream`/`Stream<T>` for CSV/Excel generation.  
   - Ensure **no Java loops** over bulk data – all aggregation must be done in SQL.  
   - Add validation that the session exists and is `COMPLETED` before exposing data.  

3. **Build Thymeleaf UI**  
   - `dashboard.html`: <br>• Include session filter dropdown (populate via `/api/sessions` – existing endpoint). <br>• Include KPI card partial. <br>• Include leakage table partial. <br>• Include session‑status partial with JavaScript polling/WebSocket subscription. <br>• Use Tailwind utility classes for responsive layout. <br>• Add CSRF token meta tag (`_csrf`).  
   - `partials/kpi-card.html`: Simple card with title, value, optional trend icon.  
   - `partials/leakage-table.html`: <br>• Use Bootstrap DataTable (or plain HTML + JS) to render rows. <br>• Add “Export CSV” and “Export Excel” buttons that call `/export/{sessionId}?format=csv` / `?format=excel`. <br>• Show loading spinner on export.  
   - `partials/session-status.html`: Display current status badge; if WebSocket connected, update in real‑time; otherwise poll `/api/session/{sessionId}/status`.  

4. **WebSocket Support (optional but recommended)**  
   - Implement `WebSocketConfig` to register `/ws/sessions`. <br>• Add a simple `SessionStatusMessage` DTO. <br>• Create a `SessionStatusService` that publishes status changes (could reuse existing session update logic). <br>• Client‑side JavaScript subscribes to `/ws/sessions` and updates the status UI.  

5. **Security & Validation**  
   - Ensure all endpoints enforce appropriate roles. <br>• Add `@RequestParam` validation for export format (enum `CSV`, `EXCEL`). <br>• Sanitise sessionId path variable (Spring converts to Long). <br>• Add audit logging for export requests (log user, sessionId, format, row count).  

6. **Testing**  
   - Write unit tests for `DashboardService` (mock repository, verify native SQL calls). <br>• Write controller integration tests (`@WebMvcTest`) covering happy path and error cases (session not found, unauthorized). <br>• Write export tests that verify file content matches DB row count and format.  

### Tester
1. **Integration Test Suite**  
   - **Controller Tests**: Verify status codes, JSON structure of `/api/dashboard/{sessionId}/metrics` and `/api/dashboard/{sessionId}/leakage`. <br>• Verify export endpoint returns correct `Content-Disposition` and file type. <br>• Verify security: 403 for insufficient roles.  
   - **Service Tests**: Mock repositories and assert that native SQL queries are invoked (use `@Sql` or verify count).  
   - **UI Functional Tests** (if using Selenium): Navigate to dashboard, select a session, assert KPI cards populated, assert leakage rows displayed, trigger export and verify downloaded file.  
2. **Performance & Load Tests**  
   - Simulate a session with >100 k variance rows. <br>• Measure dashboard load time (target <500 ms). <br>• Measure export generation time (target <2 s) and memory usage (ensure no OOM).  
3. **Guardrail Compliance Checks**  
   - Verify no Java loops over `TempShopeeOrder`/`TempLogisticsOrder` in `DashboardService`. <br>• Verify export streams data (check that `StreamingResponseBody` is used, not `ByteArrayOutputStream`).  
4. **Security Testing**  
   - Run OWASP ZAP against the new UI endpoints. <br>• Verify CSRF tokens present in forms. <br>• Verify session fixation protections.  
5. **Sign‑off** – Provide test execution report and approve Phase 4 readiness.  

### Reviewer
1. **Architectural Review**  
   - Confirm that all calculations are performed via native SQL (no loops). <br>• Validate that the UI layer does not contain business logic.  
2. **Security Review**  
   - Ensure RBAC, CSRF, and input validation are applied to all new endpoints. <br>• Review export file content for accidental leakage of sensitive data (e.g., raw fees).  
3. **Code Quality Review**  
   - Check Thymeleaf syntax, CSS naming conventions, and JavaDoc. <br>• Verify that any new dependencies (e.g., EasyExcel for export) are declared with appropriate version constraints.  
4. **Export Integrity Review**  
   - Confirm that exported files include session metadata (sessionId, export timestamp, user) and are deterministic (sorted by orderId). <br>• Validate that row count matches DB count before streaming.  
5. **Sign‑off** – Approve changes for promotion.  

### DevOps
1. **Container Updates**  
   - Update Dockerfile to copy any new static resources (`src/main/resources/static/`). <br>• Ensure EasyExcel dependency is present (already in Phase 2).  
2. **CI/CD Pipeline Enhancements**  
   - Add steps for UI linting (e.g., `npm lint` if using custom scripts). <br>• Include integration test execution in the build matrix. <br>• Add security scan for UI (e.g., `npm audit`).  
3. **Monitoring & Observability**  
   - Expose Prometheus metrics for dashboard endpoint latency (`dashboard_latency_seconds`) and export duration (`export_duration_seconds`). <br>• Update Grafana dashboards to show KPI card values and export success rate.  
4. **Staging Deployment**  
   - Build new image, push to artifact registry, promote via ArgoCD to staging. <br>• Run end‑to‑end smoke tests: upload a sample Excel, trigger reconciliation, navigate to dashboard, verify KPI cards, trigger export, validate file.  
5. **Documentation**  
   - Update run‑books with steps for troubleshooting dashboard UI issues and export failures. <br>• Document any new WebSocket endpoints for operations.  

## 4. Phase Definition of Done (DoD)

- **Functional Completion**  
  - Executive dashboard renders three KPI cards with correct values per session.  
  - Leakage inventory data‑grid displays all variance rows and supports inline CSV/Excel export.  
  - Session filtering, auto‑refresh (WebSocket/polling), and live status indicator operate as intended.  
  - Export endpoints produce deterministic, audit‑ready files (including session metadata, row count validation) and stream directly to the client.  

- **Technical Compliance**  
  - **Zero Application‑Level Loops** – All bulk calculations are performed via native SQL queries; `DashboardService` contains no iterative loops over `TempShopeeOrder`/`TempLogisticsOrder`.  
  - **Memory‑Efficient Export** – Export uses `StreamingResponseBody` (CSV) or EasyExcel `ExcelWriter` with streaming to avoid loading entire result sets into JVM memory.  
  - **Performance** – Dashboard load < 500 ms; export generation < 2 s for 100 k rows; upload latency remains < 200 ms (already satisfied).  
  - **Security** – All UI endpoints protected by Spring Security RBAC; CSRF tokens present; input validation and sanitisation applied; export files do not contain raw sensitive data beyond intended fields.  

- **Quality & Testing**  
  - Unit & integration test coverage ≥ 80 % for new controller/service code.  
  - Automated test suite passes in CI pipeline.  
  - Performance and guardrail tests pass (no loops, memory limits).  
  - Security scan results cleared.  

- **Operational Readiness**  
  - Docker image built, CI/CD pipeline updated, and artifact promoted to staging.  
  - Prometheus/Grafana dashboards include metrics for dashboard latency and export duration; alerts configured for failures.  
  - Run‑books and documentation for dashboard usage, export integrity, and troubleshooting are complete.  

- **Sign‑offs**  
  - **Coder** delivers implemented components with unit/integration tests.  
  - **Tester** executes and signs off test suite, performance, and security validations.  
  - **Reviewer** approves architectural, security, and export integrity compliance.  
  - **DevOps** deploys to staging, runs smoke tests, and confirms observability setup.  

When all above criteria are satisfied, Phase 4 deliverables are considered complete and the Manager may approve progression to Phase 5.