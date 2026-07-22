# PHASE 2 CONTEXT BLUEPRINT: financial-reconciliation
## 1. Phase Operational Scope & Objectives
- **Async Ingestion Pipeline** – Build a non‑blocking file‑upload flow that returns immediately with a `SessionId` and launches background processing.
- **Session Management** – Create, persist, and update `ReconciliationSession` lifecycle (`PENDING` → `PROCESSING` → `COMPLETED`/`FAILED`).
- **Spring Batch with EasyExcel** – Use SAX‑based `EasyExcel` readers to stream Shopee and Logistics Excel files into session‑partitioned staging tables (`temp_shopee_orders`, `temp_logistics_orders`).
- **Background Worker** – `@Async` service that starts the batch job and updates session status.
- **UI & Real‑Time Feedback** – Thymeleaf page (`upload.html`) with drag‑&‑drop upload, client‑side polling of `/session/{sessionId}` for status updates.
- **Guardrail Enforcement** – Sub‑200 ms upload response, zero Java loops over bulk data, memory‑efficient streaming, file‑size/MIME validation, session isolation via foreign keys.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Layer | Path / Endpoint | Description |
|-------|----------------|-------------|
| **Controller** | `src/main/java/com/finrec/reconciliation/controller/UploadController.java` | `@RestController` with `@PostMapping("/upload")` returning `{sessionId, status}`. |
| **Service** | `src/main/java/com/finrec/reconciliation/service/IngestionService.java` | Orchestrates async batch launch, updates `ReconciliationSession`. |
| **Batch Config** | `src/main/java/com/finrec/reconciliation/batch/ReconciliationBatchConfig.java` | Defines Spring Batch job, steps, `EasyExcel` readers for Shopee & Logistics. |
| **Processors** | `src/main/java/com/finrec/reconciliation/batch/processor/ShopeeOrderItemProcessor.java` <br> `src/main/java/com/finrec/reconciliation/batch/processor/LogisticsOrderItemProcessor.java` | Simple POJO mappers (no loops). |
| **Writers** | `src/main/java/com/finrec/reconciliation/repository/TempShopeeOrderRepository.java` <br> `src/main/java/com/finrec/reconciliation/repository/TempLogisticsOrderRepository.java` | `JpaRepository` extending `JpaRepository<TempShopeeOrder, Long>` etc. |
| **Entities** | `src/main/java/com/finrec/reconciliation/model/` (existing `ReconciliationSession`, `TempShopeeOrder`, `TempLogisticsOrder`) | No changes required. |
| **UI** | `src/main/resources/templates/upload.html` <br> `src/main/resources/static/js/upload.js` | Drag‑&‑drop zone, Axios POST to `/upload`, polling `/session/{sessionId}`. |
| **Config** | `src/main/resources/application.yml` | `spring.batch.job.enabled=false`, file‑size limits, async pool sizes. |
| **Tests** | `src/test/java/com/finrec/reconciliation/...` | Unit & integration tests for controller, service, batch, UI. |
| **CI/CD** | `.github/workflows/ci.yml` | Build, static analysis, unit tests, Docker build, push. |
| **Docker** | `Dockerfile` (project root) | Multi‑stage build, copy JAR, set JVM opts. |
| **Observability** | `src/main/java/com/finrec/reconciliation/metrics/MetricsService.java` (stub) <br> `src/main/resources/logback.xml` (ELK placeholders) | Basic Prometheus metrics & logging. |
| **Guardrail Config** | `pom.xml` / `build.gradle` | Declare `easyexcel` dependency, exclude `poi`. <br> `sonar-project.properties` with rule set for loops. |

**Endpoints**
- `POST /upload` – accepts multipart `marketplaceFile` and `logisticsFile`. Returns `201 Created` with JSON `{ "sessionId": 42, "status": "PENDING" }`.
- `GET /session/{sessionId}` – returns current session status and optional progress details (used by UI polling).

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
### Coder
- Implement `UploadController`:
  - Validate incoming files (size ≤ 100 MB, MIME `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, non‑empty).
  - Create `ReconciliationSession` entity with status `PENDING`, persist via `SessionRepository`.
  - Invoke `@Async` `IngestionService.startBatch(sessionId, marketplaceFile, logisticsFile)` and return immediate response.
- Build `IngestionService`:
  - Expose `CompletableFuture<Void> processFiles(Long sessionId, MultipartFile marketplace, MultipartFile logistics)`.
  - Update session status to `PROCESSING` before launching batch; set to `COMPLETED`/`FAILED` after job completion.
- Configure Spring Batch (`ReconciliationBatchConfig`):
  - Two independent steps: **ShopeeStep** and **LogisticsStep**.
  - Use `EasyExcel` `ExcelReader` with `SAXReader` and `Sheet` for each file type.
  - Map rows to `TempShopeeOrder` / `TempLogisticsOrder` via simple `ItemProcessor` (no loops, just field mapping).
  - Writers are `JpaItemWriter` backed by the respective repositories.
- Ensure **zero‑loop guardrail**:
  - No `for/while` over `TempShopeeOrder` or `TempLogisticsOrder` in any service or processor.
  - All bulk calculations delegated to native SQL (future Phase 3).
- Create UI (`upload.html` + `upload.js`):
  - Drag‑&‑drop zone, file inputs, submit via Axios.
  - Poll `/session/{sessionId}` every 2 s, display status and progress.
- Write **unit tests** for controller (mock service), service (mock batch), and batch components (integration with sample Excel files).
- Enforce dependency check: only `easyexcel` version ≥ 3.3.0; reject `poi` > 2.0.

### Tester
- Design JUnit 5 test suite:
  - `UploadControllerIT` – file validation, session creation, async trigger verification.
  - `IngestionServiceTest` – mock batch launch, verify status transitions.
  - `BatchIntegrationTest` – run real Spring Batch job with tiny Excel files; assert rows written to staging tables.
  - `PerformanceTest` – simulate 10 MB Excel file, measure upload response (<200 ms) and memory usage (no OOM).
  - `GuardrailTest` – static analysis check for prohibited loops, dependency check for Apache POI.
- Execute tests in CI; fail build on any guardrail violation or performance breach.
- Document test results and sign off readiness for Phase 3.

### Reviewer
- Conduct architectural review of async pipeline:
  - Verify session isolation (FK constraints), correct use of EasyExcel, compliance with zero‑loops guardrail.
- Validate security:
  - Ensure CSRF protection on Thymeleaf forms, placeholder JWT auth, input sanitization.
- Approve code changes after CI passes and test suite passes.
- Sign off Phase 2 deliverables.

### DevOps
- Update `Dockerfile` (multi‑stage) and set JVM memory limits.
- Extend `github/workflows/ci.yml`:
  - Build (Maven/Gradle).
  - Static analysis (SonarQube) with loop‑detection rules.
  - Run unit & integration tests.
  - Build Docker image, push to artifact registry.
- Add stubbed Prometheus metrics (`/actuator/metrics`) and Grafana dashboard template.
- Configure centralized logging (`logback.xml`) with ELK placeholders.
- Provision staging environment (K8s/VM) with DB credentials, async thread‑pool size.
- Verify deployed service meets SLA (upload <200 ms) and logs show session creation & batch start.

### Manager
- Review Phase 2 scope, resource allocation, and timeline.
- Approve go/no‑go to Phase 3 after Coder, Tester, Reviewer, and DevOps sign‑offs.

## 4. Phase Definition of Done (DoD)
- **Functional**
  - `POST /upload` returns `{sessionId, status}` within **<200 ms**.
  - Background Spring Batch job automatically processes both Shopee and Logistics Excel files using **EasyExcel SAX streaming**.
  - Staging tables populated with records correctly **partitioned by `session_id`**.
  - Session lifecycle transitions (`PENDING` → `PROCESSING` → `COMPLETED`/`FAILED`) reflected in DB.
  - Thymeleaf UI (`upload.html`) provides drag‑&‑drop upload and **real‑time polling** of session status.
  - File validation enforces **size ≤ 100 MB**, correct MIME type, non‑empty content.
  - All bulk data handling respects **zero‑loop guardrail**; calculations remain native SQL (future Phase).
  - Guardrail compliance verified by static analysis (no loops, EasyExcel only, sub‑200 ms response).

- **Quality & Testing**
  - Full unit test coverage for controller, service, batch components, and validation logic.
  - Integration test confirming end‑to‑end ingestion and session completion.
  - Performance test confirming upload response <200 ms and stable memory usage for max‑size files.
  - Guardrail test suite passes (no prohibited loops, clean dependency check).

- **Documentation & Sign‑off**
  - Code reviewed and approved by **Reviewer**.
  - CI/CD pipeline updated and **passing** for Phase 2 artifacts.
  - DevOps environment provisioned with monitoring stubs and logging.
  - **Manager** sign‑off on Phase 2 deliverables.

When **all DoD items** are satisfied, the Phase is complete and the team proceeds to **Phase 3**.