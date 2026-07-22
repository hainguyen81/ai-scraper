# PHASE 5 CONTEXT BLUEPRINT: financial-reconciliation
## 1. Phase Operational Scope & Objectives
| Goal | Description |
|------|-------------|
| **Testing & Validation** | Build comprehensive unit, integration, performance, and security test suites that validate the entire reconciliation pipeline, native SQL calculations, UI dashboards, and export functionality. |
| **Security Hardening** | Apply enterprise‑grade security controls: JWT‑based authentication, RBAC, CSRF protection, input validation/sanitization, and OWASP‑aligned threat mitigation. |
| **CI/CD Finalization & Production Deployment** | Complete the GitHub Actions workflow (lint → unit → integration → security → container build → push → ArgoCD promotion), containerize the monolith, and roll out to staging → production with automated smoke and end‑to‑end checks. |
| **Observability & Run‑book Establishment** | Deploy Prometheus/Grafana dashboards, ELK stack logging, and create operational run‑books that capture health checks, alert configurations, and incident response procedures. |
| **Sign‑off & Handover** | Secure Manager approval for production release, and deliver all artefacts (code, documentation, CI/CD configs, monitoring dashboards) to the operations team. |

---

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)

### 2.1 Source Code Layout (Monolithic Spring Boot)
```
src/
  main/
    java/
      com/example/finrec/
        controller/          ← REST endpoints
        model/               ← JPA entities (ReconciliationSession, TempShopeeOrder, TempLogisticsOrder)
        repository/          ← JPA repositories + native @Query methods
        service/             ← Business logic (ReconciliationService, SessionService)
        config/              ← SecurityConfig, AsyncConfig, EasyExcel config
        batch/               ← Spring Batch jobs (FileReadConfig, FileWriteConfig)
        security/            ← JWT authentication & RBAC
        utils/               ← Common utilities (ExcelStreamUtils, SessionIdGenerator)
    resources/
      static/              ← Tailwind CSS, JS assets
      templates/           ← Thymeleaf UI pages (upload, session‑status, dashboard, export)
    config/
      application.yml      ← Spring profiles, datasource, logging, async settings
  test/
    java/
      com/example/finrec/
        controller/        ← Controller tests (MockMvc)
        service/           ← Service unit & integration tests
        batch/             ← Batch job integration tests (EasyExcel streaming)
        security/          ← Security tests (JWT, CSRF, RBAC)
        repository/        ← JPA & native SQL query tests
    resources/
      application-test.yml
```

### 2.2 Key Endpoints (must be exercised by tests & UI)
| Method | Path | Purpose |
|--------|------|---------|
| `POST` | `/api/v1/upload` | Accepts multipart file(s) (marketplace + logistics). Returns `SessionResponse {sessionId, status}`. |
| `GET` | `/api/v1/sessions/{sessionId}` | Retrieves session metadata & computed KPI totals. |
| `GET` | `/api/v1/sessions/{sessionId}/discrepancies` | Returns CSV/Excel export of leakage inventory (orderId, variance). |
| `GET` | `/dashboard` | Thymeleaf view rendering the three KPI cards and data‑grid. |
| `GET` | `/login` | OAuth2/JWT login page (if used). |
| `POST` | `/logout` | Session invalidation. |

### 2.3 CI/CD & DevOps Artefacts
```
.github/
  workflows/
    ci-cd.yml               ← Lint → Unit → Integration → Security Scan → Docker Build → Push → ArgoCD Promote
Dockerfile                ← Multi‑stage build (Maven → OpenJDK)
docker-compose.yml        ← Local dev environment (PostgreSQL + ELK)
prometheus/
  rules.yml               ← Alerting rules for latency, error‑rate, memory
grafana/
  dashboards/
    finrec-overview.json  ← C‑level KPI dashboard
logs/
  logback.xml             ← Structured JSON logging for ELK
docs/
  runbooks/
    finrec-runbook.md     ← Operational procedures
```

---

## 3. Dedicated Sub‑Agent Functional Directives

### 3.1 Coder  
| Task | Details |
|------|---------|
| **Implement Test Suites** | • Write JUnit 5 unit tests for JPA entities, repositories, and native `@Query` methods (cover edge cases, null values, data‑type mismatches).<br>• Create Spring Boot integration tests (`@SpringBootTest + TestRestTemplate`) that simulate full upload → batch processing → reconciliation flow using synthetic Excel files (≤10 MB).<br>• Add MockMvc tests for all REST endpoints (`/upload`, `/sessions/{id}`, `/discrepancies`) verifying response codes, sessionId generation, and CSV export headers. |
| **Security Hardening** | • Integrate Spring Security with JWT (HMAC‑SHA256) – configure `JwtAuthenticationFilter` and `JwtAuthorizationFilter`.<br>• Define role‑based authorities (`ROLE_ADMIN`, `ROLE_ANALYST`) and enforce `@PreAuthorize` on sensitive endpoints.<br>• Enable CSRF protection for browser sessions (`<csrf token/>` in Thymeleaf forms).<br>• Add global `@Valid` validation and custom validators for file MIME‑type, size (`≤200 MB`), and Excel sheet structure. |
| **Performance Guardrails** | • Verify that the `/upload` endpoint returns within 200 ms by adding a `@ResponseHeader` with processing time and a JUnit assertion in integration tests.<br>• Instrument EasyExcel SAX reader to log memory usage (`Instrumentation.getInstrumentation().getObjectSize`) and assert that heap growth < 50 MB for a 10 MB file.<br>• Ensure native SQL queries are indexed (create composite indexes on `session_id, order_id`). |
| **Code Quality & Guardrail Compliance** | • Run static analysis (SonarQube) to enforce “no loops over bulk data” – add a custom rule that flags `for/while` iterating over `TempShopeeOrder`/`TempLogisticsOrder` collections.<br>• Enforce dependency check to reject Apache POI (`poi>2.0`).<br>• Commit all changes with descriptive messages and include `Co-authored-by: openhands <openhands@all-hands.dev>`. |

### 3.2 Tester  
| Task | Details |
|------|---------|
| **Test Data Generation** | • Build a utility (`TestExcelGenerator`) that creates realistic marketplace and logistics Excel files (CSV‑compatible) with known variances, escrow, and safe amounts. |
| **Unit & Integration Tests** | • Execute the full test matrix (≥90 % line coverage).<br>• Validate that native SQL variance query returns expected rows for given sessionId.<br>• Simulate failure scenarios (missing file, malformed sheet, duplicate orderId) and assert proper error responses. |
| **Performance & Load Tests** | • Use `jmeter` or `gatling` to simulate concurrent uploads of 5‑10 MB files (target 10 RPS).<br>• Capture response times, memory usage, and error rates; assert upload response ≤200 ms and error‑rate <0.1 %. |
| **Security Tests** | • Run OWASP ZAP scan against the deployed staging instance (enable passive/active scans).<br>• Perform JWT token validation tests (expired, malformed, wrong signature).<br>• Test RBAC: ensure `ROLE_ANALYST` can only access `/dashboard` and `/sessions/{id}` while `ROLE_ADMIN` can also trigger re‑conciliation jobs. |
| **Test Reporting** | • Generate a test execution report (JUnit XML → Allure) and upload to CI artifact.<br>• Produce a security risk register and sign‑off checklist for Reviewer. |

### 3.3 Reviewer  
| Task | Details |
|------|---------|
| **Architectural Review** | • Verify that all heavy calculations are performed via native SQL (no loops over staging tables).<br>• Confirm that EasyExcel SAX streaming is used and Apache POI is absent. |
| **Security Review** | • Validate JWT implementation (strong secret, expiration, refresh).<br>• Check CSRF tokens are present in Thymeleaf forms.<br>• Review input sanitization and file‑type whitelisting. |
| **Compliance Check** | • Ensure guardrail rules are enforced in CI (SonarQube, dependency check).<br>• Confirm that session isolation is enforced via foreign‑key constraints on `session_id`. |
| **Sign‑off** | • Approve test results, security scan findings (no high‑severity issues), and CI/CD pipeline configuration.<br>• Provide final approval to Manager for production promotion. |

### 3.4 DevOps  
| Task | Details |
|------|---------|
| **Containerization** | • Write a multi‑stage `Dockerfile` (Maven build → slim JDK image).<br>• Include `jlink` to produce a custom runtime for reduced image size.<br>• Push image to container registry (e.g., GHCR). |
| **CI/CD Pipeline** | • Update `.github/workflows/ci-cd.yml` to include:<br>   - Static analysis (SonarQube) <br>   - Unit & integration test stages <br>   - OWASP ZAP security scan <br>   - Docker build & push <br>   - ArgoCD sync to staging (via Helm chart) <br>   - Automated smoke test (curl `/api/v1/upload` with dummy file) <br>   - Promotion to production after manual approval. |
| **Monitoring & Logging** | • Deploy Prometheus exporter (`spring-boot-actuator`).<br>• Create Grafana dashboard JSON for latency, error‑rate, memory, and upload response time.<br>• Configure ELK stack: `logback.xml` outputs structured JSON logs with fields `sessionId`, `userId`, `level`, `timestamp`. |
| **Environment Provisioning** | • Use Kubernetes manifests (`k8s/`) with `ResourceQuota`, `LimitRange`, and `NetworkPolicy` for security.<br>• Set up PostgreSQL via Helm chart with TLS encryption and backup cronjob. |
| **Run‑book Documentation** | • Draft `docs/runbooks/finrec-runbook.md` covering:<br>   - Health‑check commands (`/actuator/health`, `/api/v1/sessions/{id}`)<br>   - Alert handling (latency >500 ms, error‑rate >0.1 %)<br>   - Log analysis procedures (Kibana query for `error` and `sessionId`)<br>   - Rollback steps (ArgoCD rollback). |
| **Production Promotion** | • Trigger ArgoCD sync to production after successful staging smoke tests.<br>• Verify 99.9 % uptime via Prometheus alerts for `up` metric.<br>• Capture final deployment logs and store in artifact repository. |

### 3.5 Manager  
| Task | Details |
|------|---------|
| **Scope Confirmation** | • Validate that Phase 5 deliverables satisfy all raw requirements (async ingestion, session lifecycle, native SQL variance, KPI dashboards, export, guardrails, security, observability). |
| **Resource Allocation** | • Ensure Coder, Tester, Reviewer, and DevOps have the required time (≤7 days total) and access to CI/CD, test environments, and monitoring tools. |
| **Risk & Stakeholder Communication** | • Document any open risks (e.g., third‑party Excel parser compatibility) and mitigation plan.<br>• Provide go/no‑go decision for production release. |
| **Final Sign‑off** | • Approve Phase 5 completion and authorize transition to post‑implementation support. |

---

## 4. Phase Definition of Done (DoD)

| Area | Acceptance Criteria |
|------|----------------------|
| **Testing** | • All unit, integration, and end‑to‑end tests pass with ≥90 % coverage.<br>• Performance tests confirm upload response ≤200 ms and memory growth < 50 MB for 10 MB files.<br>• Load tests sustain ≥10 RPS with error‑rate <0.1 %. |
| **Security** | • OWASP ZAP scan reports no high‑severity vulnerabilities (medium/low accepted).<br>• JWT authentication & RBAC enforced; CSRF tokens present.<br>• Input validation blocks disallowed file types and oversized uploads. |
| **CI/CD** | • GitHub Actions workflow completes all stages (lint → test → security → build → push → ArgoCD).<br>• Docker image builds successfully and is push‑ready.<br>• Staging deployment passes automated smoke tests. |
| **Observability** | • Prometheus metrics exported (request latency, error rate, memory, session count).<br>• Grafana dashboard visualizes C‑level KPI trends and alerts on SLA breaches.<br>• ELK stack receives structured logs; Kibana queries return session‑specific error traces. |
| **Documentation** | • `docs/runbooks/finrec-runbook.md` completed with health‑check, alert, and rollback procedures.<br>• All code commits include descriptive messages and `Co-authored-by`. |
| **Production Release** | • ArgoCD promotes image to production after manual Manager approval.<br>• Post‑deployment smoke test passes (`/api/v1/upload` with dummy file, `/dashboard` loads KPI cards).<br>• 99.9 % uptime and <500 ms dashboard query latency verified via Prometheus alerts. |
| **Sign‑off** | • Coder, Tester, Reviewer, and DevOps each sign off their respective artefacts.<br>• Manager provides final approval, confirming all raw requirements are satisfied and the system is ready for operational support. |

**Result:** Phase 5 is complete, the financial‑reconciliation Micro‑SaaS platform is fully tested, hardened, deployed, and observable, meeting all enterprise guardrails and business objectives.