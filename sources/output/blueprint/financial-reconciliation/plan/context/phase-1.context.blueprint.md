# PHASE 1 CONTEXT BLUEPRINT: financial-reconciliation
## 1. Phase Operational Scope & Objectives
| Goal | Description | Success Indicator |
|------|-------------|-------------------|
| **Monolithic Skeleton** | Create a Spring Boot 3.x project with Java 17/21, core packages, and a minimal REST layer. | `mvn clean install` or `./gradlew build` succeeds; `SpringApplication` runs on `localhost:8080`. |
| **Database Schema Foundations** | Define and persist the three core tables (`reconciliation_sessions`, `temp_shopee_orders`, `temp_logistics_orders`) with proper indexes, foreign‑key constraints, and `SessionStatus` enum. | Schema migration scripts (Flyway/Liquibase) applied; tables exist in the target DB. |
| **Core Domain Entities & JPA** | Implement `ReconciliationSession`, `TempShopeeOrder`, `TempLogisticsOrder` with required fields, annotations, and JPA `@Repository` interfaces. | Entities compile, can be persisted via `save()`/`findById()`. |
| **Guardrail Enforcement** | Configure static‑analysis (SonarQube/PMD/SpotBugs) to reject: <br>• Java loops over `TempShopeeOrder`/`TempLogisticsOrder`. <br>• Any `poi` dependency. <br>• Upload response > 200 ms (monitoring stub). | Build fails on violation; CI reports clean scan. |
| **Async & Batch Infrastructure** | Provide `@Async` configuration, `AsyncConfig` bean, and a skeleton `SpringBatch` job definition (reader, writer, listener) for later Phase 2. | `Async` beans present; `Job` bean defined (no execution yet). |
| **Docker & CI Skeleton** | Create a multi‑stage `Dockerfile`, a base `Docker` image, and a GitHub Actions workflow that triggers on `push`/`pull_request` (lint → test → static analysis). | Docker image builds (`docker build -t finrec:1.0 .`); workflow file present and passes lint. |
| **Observability Stubs** | Enable Spring Boot Actuator endpoints (`/actuator/health`, `/metrics`), add minimal Prometheus configuration, and configure Logback to forward to ELK (stub). | Actuator endpoints reachable; `/metrics` returns basic JVM/HTTP metrics. |
| **Managerial Sign‑off** | All artefacts reviewed and approved by the Manager before moving to Phase 2. | Manager’s “Phase 1 Complete” comment in the project board. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
```
financial-reconciliation/
├─ src/
│  ├─ main/
│  │  ├─ java/
│  │  │  └─ com/
│  │  │     └─ finrec/
│  │  │        ├─ config/               # AsyncConfig, BatchConfig, AppConfig
│  │  │        ├─ controller/           # UploadController (stub), SessionController
│  │  │        ├─ domain/               # ReconciliationSession, TempShopeeOrder, TempLogisticsOrder
│  │  │        ├─ enum/                 # SessionStatus
│  │  │        ├─ repository/           # JpaRepositories
│  │  │        └─ security/             # SecurityConfig (JWT stub)
│  │  ├─ resources/
│  │  │  ├─ application.yml
│  │  │  ├─ static/                    # Tailwind CSS, JS (minimal)
│  │  │  └─ templates/                 # Thymeleaf UI (future phases)
│  │  └─ meta-inf/
│  └─ test/
│     └─ java/
│        └─ com/
│           └─ finrec/
│              └─ ... (unit & integration tests)
├─ src/main/resources/db/migration/   # Flyway/Liquibase scripts for schema
├─ Dockerfile                         # Multi‑stage, base image (openjdk:21-slim)
├─ docker-compose.yml                # Optional local dev stack
├─ .github/
│  └─ workflows/
│     └─ ci.yml                       # GitHub Actions pipeline
├─ pom.xml / build.gradle.kts        # Maven/Gradle with enforced deps
├─ sonar-project.properties
└─ README.md
```
### Allowed Endpoints (Phase 1)
| Method | Path | Purpose |
|--------|------|---------|
| `POST` | `/api/v1/upload` | Accepts multipart file upload; returns `SessionResponse` (sessionId, status). |
| `GET`  | `/api/v1/sessions/{id}` | Retrieves session details (status, timestamps). |
| `GET`  | `/actuator/health` | Liveness probe. |
| `GET`  | `/actuator/metrics` | Prometheus metrics stub. |

### File & Dependency Rules
* **Java version** – 17 or 21 (enforced via `maven-compiler-plugin` or `gradle.java`).
* **Core dependencies** – Spring Boot Web, Data JPA, Batch, EasyExcel, PostgreSQL driver, Lombok (optional), Spring Security (JWT stub), Spring Boot Actuator.
* **Forbidden** – `org.apache.poi` (any version > 2.0); any custom loops over bulk staging tables (enforced by static analysis).
* **Allowed file extensions** – `.java`, `.yml`, `.properties`, `.sql`, `.dockerfile`, `.yml` (CI), `.kts`/`.xml` (build), `.md`.

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)

### Coder
1. **Project Scaffold**  
   * Generate a Spring Boot 3.x monolithic project (Maven or Gradle).  
   * Set Java language level to 17/21 and configure `maven-compiler-plugin`/`java` toolchain.  

2. **Domain Model**  
   * Create `ReconciliationSession` entity with fields: `id`, `userId`, `createdAt`, `status` (`SessionStatus`), `totalDiscrepancyAmount`, `totalHoldingAmount`, `totalSafeAmount`.  
   * Create `TempShopeeOrder` and `TempLogisticsOrder` entities mirroring the PRD schema, including `sessionId` foreign key (no cascade delete yet).  
   * Add `SessionStatus` enum (`PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`).  

3. **Persistence**  
   * Implement JPA repositories (`ReconciliationSessionRepository`, `TempShopeeOrderRepository`, `TempLogisticsOrderRepository`).  
   * Add `@EntityListeners(AuditingEntityListener.class)` for `createdAt` auto‑fill.  

4. **Async & Batch Config**  
   * Provide `AsyncConfig` defining a thread pool (`taskExecutor`) with `corePoolSize=5`, `maxPoolSize=10`.  
   * Provide a skeleton `BatchConfig` bean defining a `Job` and `Step` (reader, writer, listener) – no actual reader/writer yet.  

5. **REST Layer (Stubs)**  
   * Create `UploadController` with `@PostMapping("/api/v1/upload")` accepting `MultipartFile`.  
   * Return immediate `ResponseEntity<SessionResponse>` with generated `sessionId` and status `PENDING`.  
   * Create `SessionController` with `@GetMapping("/api/v1/sessions/{id}")`.  

6. **Security & Actuator**  
   * Add `SecurityConfig` with JWT stub (empty `configure(HttpSecurity)`).  
   * Enable Spring Boot Actuator endpoints (`health`, `metrics`, `info`).  

7. **Docker & CI**  
   * Write a multi‑stage `Dockerfile` (base `openjdk:21-slim`, copy JAR, set entrypoint).  
   * Add a basic `docker-compose.yml` for local dev (optional).  

8. **Configuration**  
   * `application.yml` – set server port, datasource (PostgreSQL/MySQL URL, credentials), spring batch, logging level, actuator base path.  

9. **Static‑Analysis Enforcement**  
   * Add `sonar-project.properties` and `pom.xml`/`build.gradle` plugins for SonarQube, PMD, SpotBugs.  
   * Include rule sets that flag loops over staging entities and any `poi` dependency.  

### Tester
1. **Unit Tests**  
   * Write JUnit 5 tests for `SessionStatus` enum.  
   * Test entity constructors, getters/setters, and JPA auditing (`@CreatedDate`).  
   * Verify repository interfaces extend `JpaRepository`.  

2. **Integration Tests**  
   * Use `@DataJpaTest` to confirm schema creation (table existence, indexes).  
   * Test `AsyncConfig` thread pool properties via `@Test` on `TaskExecutor`.  

3. **Guardrail Validation**  
   * Add a static‑analysis test that fails if any source file contains `for (` or `while (` over `TempShopeeOrder` or `TempLogisticsOrder`.  
   * Ensure `pom.xml`/`build.gradle` does not include `poi` (run dependency check).  

4. **Controller Tests**  
   * Mock file upload to `/api/v1/upload` and assert `201`/`OK` with sessionId.  
   * Verify `/api/v1/sessions/{id}` returns expected fields.  

5. **Test Reporting**  
   * Ensure all tests pass before CI proceeds.  

### Reviewer
1. **Architectural Review**  
   * Verify that the monolith follows the tech‑stack blueprint (Spring Boot 3.x, EasyExcel, native SQL later).  
   * Confirm that guardrail rules are integrated into CI (static analysis, dependency check).  

2. **Security Review**  
   * Check that Spring Security configuration is present (even if stubbed) and CSRF is disabled only for API endpoints.  
   * Validate that actuator endpoints are not exposed publicly in production (plan to secure later).  

3. **Compliance Check**  
   * Ensure no `poi` dependency, no loops over bulk tables, and async upload response design is present.  

4. **Sign‑off**  
   * Provide a formal approval comment in the project tracking tool (e.g., Jira) indicating “Phase 1 architecture & code ready for development”.  

### DevOps
1. **Docker Image**  
   * Create `Dockerfile` (multi‑stage) that builds a lean JVM image, copies the built JAR, sets JVM options (`-XX:+UseContainerSupport`).  

2. **CI Pipeline Skeleton**  
   * Add `.github/workflows/ci.yml`: <br>• `checkout` <br>• `mvn clean install` (or `./gradlew build`) <br>• `dependency-check:analyze` (to enforce no `poi`) <br>• `sonarqube/scan` (with quality gate) <br>• `docker/build` (optional, push to GHCR) <br>• `kubectl apply` to a dev namespace (optional stub).  

3. **Monitoring Stubs**  
   * Enable `/actuator/metrics` and `/actuator/health`. <br>• Add minimal `application.yml` properties for Prometheus scraping (`management.metrics.export.prometheus.enabled=true`). <br>• Configure Logback to forward to a local ELK container (stub).  

4. **Environment Provision**  
   * Provide a `docker-compose.yml` that starts PostgreSQL, optional Jaeger/Elastic, and the app (for local dev).  

5. **Documentation**  
   * Draft a `README.md` outlining how to run the app locally (`docker-compose up`), build, and run tests.  

### Manager
1. **Scope Confirmation**  
   * Review Phase 1 objectives, ensure they align with the overall product roadmap.  

2. **Resource Allocation**  
   * Approve Coder, Tester, Reviewer, DevOps time allocations for Phase 1.  

3. **Go/No‑Go Decision**  
   * After all sub‑agents sign off, provide final approval to proceed to Phase 2.  

## 4. Phase Definition of Done (DoD)

| Checklist Item | Evidence |
|----------------|----------|
| **Project Build** | `mvn clean install` / `./gradlew build` succeeds with no compilation errors. |
| **Java & Dependencies** | `pom.xml`/`build.gradle` declares Spring Boot 3.x, EasyExcel, Spring Batch, JPA, PostgreSQL driver; **no** `poi` dependency. |
| **Database Schema** | Flyway/Liquibase scripts create `reconciliation_sessions`, `temp_shopee_orders`, `temp_logistics_orders` with required columns, primary keys, indexes, and foreign‑key constraints. |
| **Core Entities** | `ReconciliationSession`, `TempShopeeOrder`, `TempLogisticsOrder` and `SessionStatus` compile, have proper JPA annotations, and can be persisted via repositories. |
| **Async & Batch Infrastructure** | `AsyncConfig` bean defines a thread pool; `BatchConfig` defines a `Job` and `Step` beans (no execution yet). |
| **REST Endpoints** | `/api/v1/upload` returns a `SessionResponse` (sessionId, status) within < 200 ms (measured in test). <br> `/api/v1/sessions/{id}` returns session details. |
| **Security & Actuator** | Spring Security config present; Actuator endpoints (`/health`, `/metrics`) reachable. |
| **Docker Image** | `docker build -t finrec:1.0 .` produces an image; `docker run` starts the container and exposes port 8080. |
| **CI Pipeline** | `.github/workflows/ci.yml` runs, passes lint, unit tests, static analysis, dependency check, and SonarQube quality gate. |
| **Guardrail Enforcement** | Static analysis (SonarQube/PMD) fails the build on any loop over staging entities or presence of `poi`. |
| **Observability Stubs** | `/actuator/metrics` returns basic JVM/HTTP metrics; logging configured to forward to ELK (stub). |
| **Test Coverage** | All unit & integration tests pass; guardrail validation tests pass. |
| **Code Review** | Reviewer signs off on architecture, security, and guardrail compliance. |
| **Manager Approval** | Manager provides explicit “Phase 1 Complete” sign‑off in the project tracking tool. |

When **all** items above are satisfied, the Phase 1 deliverables are considered complete and the team may progress to **Phase 2 – Async Ingestion Pipeline & Session Management**.