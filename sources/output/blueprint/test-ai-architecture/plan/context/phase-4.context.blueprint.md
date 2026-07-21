# PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
| Item | Description |
|------|-------------|
| **Goal** | Validate that the membership‑hub application meets functional, non‑functional, security, and compliance requirements through a comprehensive testing regimen. |
| **Key Objectives** | 1. **Functional correctness** – Verify attendance QR scanning, user authentication (email/password + Firebase/Google/Facebook), multi‑center data isolation, expiration‑day calculation, and notification delivery (SMS/Zalo/app). <br>2. **Performance & Scalability** – Confirm that Quarkus services, Kafka streams, and Postgres queries sustain expected load and scale horizontally in GKE. <br>3. **Security & Compliance** – Execute penetration, OWASP, GDPR/CCPA data‑privacy, and token‑handling tests; enforce least‑privilege access controls. <br>4. **Quality Assurance** – Achieve ≥ 90 % unit‑test coverage, end‑to‑end UI test pass rate, and automated regression suite execution. <br>5. **Observability** – Validate logging, metrics, and alerting pipelines (Cloud Logging, Cloud Monitoring) are correctly instrumented and produce actionable data. |
| **Time Box** | Maximum 7 calendar days (Day 15‑21 of the overall project). Work stops as soon as the core technical objectives are satisfied. |
| **Deliverables** | • Test suite (unit, integration, UI, security, performance). <br>• Test‑environment artifacts (Docker Compose/K8s manifests for test clusters). <br>• CI/CD test‑pipeline configuration (GitHub Actions / Cloud Build). <br>• Test‑execution reports and defect‑tracking logs. <br>• Monitoring & logging validation report. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Category | Path / Endpoint | Rationale |
|----------|----------------|-----------|
| **Backend Test Sources** | `src/test/java/` (Quarkus) <br> `src/test/resources/` (Kafka fixtures, DB scripts) | Unit & integration tests for core services (AuthService, AttendanceService, NotificationService, CenterService). |
| **Frontend Test Sources** | `frontend/tests/` (Next.js unit & integration) <br> `frontend/e2e/` (Cypress) | UI and API contract validation for web & PWA. |
| **Mobile Test Sources** | `mobile/tests/` (React‑Native/Expo unit) <br> `mobile/e2e/` (Detox) | Multi‑platform UI and offline‑first behavior. |
| **Security Test Harness** | `security/` (OWASP ZAP scripts, token‑validation tests) | Automated security scanning. |
| **Performance Test Harness** | `performance/` (k6 scripts targeting `/api/attendance/*`, `/api/auth/*`, Kafka topics) | Load & stress validation. |
| **Compliance Test Harness** | `compliance/` (GDPR/CCPA data‑export/import tests, consent‑management checks) | Regulatory validation. |
| **CI/CD Test Config** | `.github/workflows/test.yml` <br> `docker-compose.test.yml` <br> `k8s/test/` (GKE test namespace manifests) | Automated test execution in isolated environments. |
| **Logging & Metrics** | `src/main/resources/logback.xml` <br> `src/main/resources/application.yml` (metrics endpoints) | Ensure observability instrumentation. |
| **API Endpoints (tested)** | `POST /api/auth/login` <br> `POST /api/auth/register` <br> `POST /api/attendance/qr/scan` <br> `GET /api/attendance/{id}/validity` <br> `POST /api/notifications/send` <br> `GET /api/centers/{id}/students` | Core business functions. |
| **Kafka Topics (tested)** | `attendance-events` <br> `notification-events` | Event‑driven flows. |
| **Database Schemas (tested)** | `src/main/resources/db/migration/V*__*.sql` (Flyway) | Data‑migration and schema integrity. |

*Only the above directories and endpoints are in scope for Phase 4. Any test or artifact outside these boundaries must be deferred to later phases.*

## 3. Dedicated Sub-Agent Functional Directives
| Sub‑Agent | Specific Tasks (ordered by priority) |
|-----------|----------------------------------------|
| **Manager** | • Finalize test strategy and acceptance criteria. <br> • Approve test‑environment provisioning (GKE test cluster, test DB snapshots). <br> • Track progress against DoD and raise blockers. |
| **Coder** | • Implement unit tests for `AuthService`, `AttendanceService`, `NotificationService`, and `CenterService` (target ≥ 90 % line coverage). <br> • Write integration tests that spin up Kafka (using `kafka-test-container`) and Postgres (using `testcontainers`) to verify end‑to‑end event flow. <br> • Add contract tests (Pact) for `/api/auth/*` and `/api/attendance/*` endpoints. <br> • Integrate test coverage reporting (Jacoco, Istanbul) into CI pipeline. |
| **Tester** | • Design exploratory test cases for QR scanning edge‑cases (duplicate scans, expired tokens). <br> • Create UI/E2E test suites (Cypress + Detox) covering multi‑language locale detection and notification delivery. <br> • Execute security scans (OWASP ZAP) and log findings; remediate high‑severity issues. <br> • Run performance scripts (k6) to validate throughput under simulated load (target < 200 ms p95 latency). <br> • Validate GDPR/CCPA compliance (data export, consent revocation). |
| **Reviewer** | • Conduct peer review of all test code (coding standards, naming, documentation). <br> • Verify test isolation (no side‑effects between test runs). <br> • Approve test‑environment manifests and CI configuration. |
| **DevOps** | • Provision a dedicated GKE test namespace (`membership-hub-test`) with autoscaling enabled. <br> • Deploy test‑ready Docker images (built with `docker build -t membership-hub:test .`) to the test cluster. <br> • Configure CI pipeline to trigger on PR merge, run unit/integration/UI/security/performance tests, and publish artifacts. <br> • Set up Cloud Logging & Monitoring dashboards for test environment; validate that logs contain request IDs, error traces, and metric exports. |
| **All Agents (collaborative)** | • Ensure test data is sanitized and does not leak PII (GDPR). <br> • Maintain a shared test‑defect board (Jira) with clear acceptance criteria. <br> • Document any assumptions or limitations in a `TEST-README.md` placed in the root of the repository. |

## 4. Phase Definition of Done (DoD)
- **Functional Testing** – All core API endpoints (`/api/auth/*`, `/api/attendance/*`, `/api/notifications/*`, `/api/centers/*`) pass automated integration tests; QR scanning logic correctly handles duplicates and expiration; notification delivery (SMS/Zalo/app) is verified via mock services.
- **Unit Testing** – ≥ 90 % line coverage across all backend services; all unit tests pass in CI; coverage reports are attached to the build artifact.
- **UI/UX Testing** – End‑to‑end test suites (Cypress + Detox) execute without failures across supported locales; multi‑language SEO meta‑tags are validated; locale detection works as per requirement (user preference → browser → default).
- **Security & Compliance** – OWASP ZAP scan reports no high‑severity vulnerabilities; token handling follows JWT best practices; GDPR/CCPA test scripts confirm data export, consent management, and PII deletion; all security findings are closed or accepted with mitigation.
- **Performance** – k6 load tests meet SLA (< 200 ms p95 latency, ≥ 1000 RPS) under simulated traffic; no memory leaks detected; performance baselines documented.
- **Observability** – Cloud Logging captures all request/response logs, error traces, and audit events; Cloud Monitoring dashboards display key metrics (CPU, memory, Kafka lag, error rate); alerts are configured for error thresholds.
- **CI/CD Validation** – Automated test pipeline runs successfully on a clean environment; all test artifacts (reports, coverage) are stored and accessible; pipeline fails fast on any test failure or coverage drop.
- **Documentation** – `TEST-README.md` includes test execution instructions, environment setup, and known limitations; test results are summarized in a `TEST-REPORT.pdf` attached to the phase deliverable.
- **Approval** – Manager, Reviewer, and DevOps sign off that the above criteria are satisfied; no open critical defects remain that would block progression to Phase 5.

*When all DoD items are met, the Phase 4 work is considered complete and the output is frozen.*