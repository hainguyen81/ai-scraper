# PHASE 2 CONTEXT BLUEPRINT: test‑ai‑architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| **Core Backend MVP** | Build the essential Quarkus micro‑services that power authentication, learner registry, attendance recording, and notification queuing. | End‑to‑end flow (login → QR scan → attendance persisted → notification queued) works in a clean‑room environment. |
| **Authentication Hub** | Implement internal email/password login **and** federated login via Firebase (Google, Facebook). Provide a unified JWT that carries role/center claims for internal services. | All four login methods return a signed JWT with correct claims; token refresh works; no plaintext secrets in repo. |
| **Multi‑Center Data Model** | Design PostgreSQL schema (with Flyway migrations) that isolates data per center while allowing a single logical tenant. | `center_id` foreign key present on every learner‑related table; queries automatically filter by tenant; data‑integrity tests pass. |
| **QR Attendance Service** | Expose a REST endpoint that receives a QR payload, validates idempotency per learner‑date, writes an attendance row, decrements remaining membership days, and publishes an event to Kafka. | Attendance recorded once per day per learner; membership day counter decrements correctly; Kafka event emitted with correct schema. |
| **Notification Pipeline (Kafka → Pub/Sub → Zalo / FCM)** | Create Kafka topics (`attendance.events`, `notification.requests`). Implement a lightweight consumer that transforms attendance events into notification requests and pushes them to Google Pub/Sub, which then triggers Cloud Functions (or a simple worker) that call Zalo API and Firebase Cloud Messaging. | At least one notification (Zalo SMS, Zalo group, push) is sent for every attendance event in a test harness; delivery success rate ≥ 95 % in simulated environment. |
| **Web Front‑end MVP (Next.js)** | Scaffold a Next.js application with: <br>• Login page (email/password + Firebase social buttons) <br>• Dashboard showing learner profile, remaining days, and a QR‑scanner component (Web‑camera based) <br>• i18n detection middleware (cookie → user‑profile → browser locale) <br>• SEO‑ready pages (`/login`, `/dashboard`, `/center/[slug]`) with `getServerSideProps` and locale‑specific meta tags. | UI renders correctly in at least two locales (en‑US, vi‑VN); SEO meta tags present; QR scanner can read a test QR code and triggers the attendance API. |
| **CI Pipeline (GitHub Actions)** | Automate: <br>1. Code lint & static analysis (SonarQube, ESLint, SpotBugs) <br>2. Unit tests (JUnit for Java, Jest for TS) <br>3. Build Docker multi‑stage images (native GraalVM optional) <br>4. Push images to Artifact Registry <br>5. Deploy to a **dev** GKE namespace using Helm values for this phase. | All pipeline stages pass on every push to `main`; Docker image size ≤ 150 MB (non‑native) or ≤ 50 MB (native). |
| **Observability Baseline** | Export Prometheus metrics from Quarkus (`quarkus-micrometer`), expose OpenTelemetry traces, and ship logs to Cloud Logging. | Grafana dashboard shows request latency < 200 ms (95th percentile) for the attendance endpoint under 500 RPS load test. |

### Phase‑2 Milestones (Gate‑Ready Deliverables)  

1. **Architecture Confirmation** – Updated context diagram, bounded‑context map, and data‑model ER diagram reviewed & approved.  
2. **Service Skeleton** – Quarkus project with modules: `auth-service`, `learner-service`, `attendance-service`, `notification-service`. All compile, containerize, and start in local Docker‑Compose.  
3. **API Contract** – OpenAPI 3.0 spec for all public endpoints, validated against generated client stubs.  
4. **End‑to‑End Demo** – Automated script that: creates a learner, logs in, scans a QR code, verifies DB row, checks Kafka topic, and confirms a mock Zalo push.  
5. **CI/CD Run** – Full pipeline execution from commit to deployment in GKE dev cluster, with Helm release `membership-hub-mvp`.  

---

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Root Directory | Key Files / Paths | Public API Endpoints (base `/api/v1`) |
|-------|----------------|-------------------|----------------------------------------|
| **Backend (Quarkus)** | `backend/` | • `pom.xml` (parent) <br>• `auth-service/` <br>• `learner-service/` <br>• `attendance-service/` <br>• `notification-service/` <br>• `src/main/resources/application.yml` <br>• `src/main/java/com/membershiphub/**` <br>• `src/main/resources/db/migration/**` (Flyway) | `POST /auth/login` <br>`POST /auth/refresh` <br>`GET  /learners/me` <br>`GET  /learners/{id}` <br>`POST /attendance/scan` (payload: `{qrToken}`) |
| **Event Streaming** | `infra/kafka/` | • `docker-compose.kafka.yml` (local dev) <br>• `schemas/attendance-event.avsc` <br>• `helm/kafka/` (optional) | N/A – internal topics: `attendance.events`, `notification.requests` |
| **Notification Workers** | `notification-worker/` | • `src/main/java/com/membershiphub/notification/**` <br>• `Dockerfile` <br>• `src/main/resources/application.yml` | Consumes `notification.requests`; publishes to Pub/Sub (`zalo-notify`, `fcm-notify`). |
| **Web Front‑end (Next.js)** | `frontend/` | • `next.config.js` <br>• `pages/` (`login.tsx`, `dashboard.tsx`, `center/[slug].tsx`) <br>• `components/QRScanner.tsx` <br>• `i18n/` (`next-i18next.config.js`, `public/locales/**`) <br>• `styles/` <br>• `Dockerfile` (multi‑stage) | N/A – static site served via GKE Ingress; API calls go to `/api/v1/*` on backend service. |
| **CI/CD** | `.github/workflows/` | • `ci.yml` (build, test, scan) <br>• `cd.yml` (helm deploy) | N/A – pipeline triggers only on `push`/`pull_request` to `main`. |
| **Helm Charts** | `helm/membership-hub/` | • `Chart.yaml` <br>• `values.yaml` (dev, prod overrides) <br>• `templates/` (deployment, service, ingress, configmap, secret) | N/A – used by Deployer. |
| **Observability** | `observability/` | • `prometheus.yml` <br>• `otel-collector-config.yaml` <br>• `grafana/dashboards/attendance.json` | N/A |

**Endpoint Access Matrix (internal only)**  

| Service | Path | Auth Required | Role(s) Allowed |
|---------|------|---------------|-----------------|
| Auth Service | `/auth/login` | ❌ | – |
| Auth Service | `/auth/refresh` | ✅ (refresh token) | – |
| Learner Service | `/learners/me` | ✅ | `learner`, `staff`, `admin` |
| Learner Service | `/learners/{id}` | ✅ | `staff`, `admin` |
| Attendance Service | `/attendance/scan` | ✅ | `staff`, `admin` |
| Notification Service | `/notifications/health` | ✅ | `admin` |

All other internal endpoints are **private** to the mesh (Istio mTLS enforced).  

---

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Primary Tasks for Phase 2 | Deliverable Artifacts | Acceptance Checks |
|-----------|---------------------------|-----------------------|-------------------|
| **Coder** | • Scaffold Quarkus multi‑module Maven project.<br>• Implement Auth Service (email/password + Firebase token verification).<br>• Design PostgreSQL schema (centers, learners, memberships, attendance).<br>• Build Attendance Service with idempotent QR logic and Kafka producer.<br>• Write Notification Service consumer that pushes to Pub/Sub.<br>• Create Next.js pages, i18n config, QR‑scanner component.<br>• Author OpenAPI spec and generate TypeScript client.<br>• Write Dockerfiles (multi‑stage, non‑root user). | - Source code in `backend/` and `frontend/`<br>- `openapi.yaml`<br>- `Dockerfile`s<br>- Helm `values-dev.yaml` | - `mvn -B verify` passes with 0 test failures.<br>- `npm test` passes.<br>- Docker images build locally and run health checks.<br>- Linting (ESLint, SpotBugs) reports no errors. |
| **Tester** | • Create unit tests for each service (JUnit 5 + Mockito).<br>• Write integration tests using Testcontainers (Postgres, Kafka).<br>• Develop end‑to‑end Cypress script that logs in, scans QR, asserts UI updates.<br>• Load‑test attendance endpoint with k6 (target 500 RPS).<br>• Validate security: attempt unauthenticated calls, verify 401/403.<br>• Verify i18n fallback logic via automated UI locale switches. | - `backend/**/src/test/java/**`<br>- `frontend/cypress/` scripts<br>- `k6/attendance-load-test.js` | - Code coverage ≥ 80 % for Java, ≥ 85 % for TS.<br>- Load test 95th‑percentile latency ≤ 200 ms.<br>- No security test yields unauthorized data leakage. |
| **Reviewer** | • Perform PR reviews for every Coder commit.<br>• Enforce guardrails: no hard‑coded secrets, proper use of `@Inject` for services, OPA policy compliance in Helm charts.<br>• Run SonarQube quality gate; reject if “blocker” issues exist.<br>• Validate OpenAPI spec matches implementation (swagger‑cli diff).<br>• Approve i18n JSON files for completeness (all keys present in each locale). | - Review comments in GitHub PRs<br>- Signed-off `CODEOWNERS` approvals | - All PRs receive **Approved** label.<br>- SonarQube Quality Gate = **Passed**.<br>- No `TODO` or `FIXME` left in production code. |
| **DevOps (Docker / Deployer)** | • Configure GitHub Actions workflow (`ci.yml`) to run lint, tests, build Docker images, scan with Trivy, push to Artifact Registry.<br>• Create Helm chart values for **dev** namespace (`membership-hub-mvp-dev`).<br>• Set up GKE dev cluster (regional, autopilot) and configure `kubectl` context.<br>• Deploy via Argo CD (or GitHub Actions `kubectl apply`) and verify health endpoints.<br>• Implement basic Prometheus scrape annotations on services.<br>• Wire up Cloud Pub/Sub subscription for notification worker (test topic). | - `.github/workflows/ci.yml` & `cd.yml`<br>- Helm chart `templates/` with proper resource limits<br>- Argo CD Application manifest (optional) | - CI pipeline completes in ≤ 15 min.<br>- Docker images scanned: **Critical** vulnerabilities = 0.<br>- Helm release `membership-hub-mvp-dev` is **Ready** (all pods Running, 1‑replica).<br>- Prometheus can scrape `/q/metrics` from each service. |
| **Security (cross‑cutting)** | • Verify TLS 1.3 termination at Ingress (GKE Ingress with Managed Certificate).<br>• Ensure OPA Gatekeeper policies block privileged containers.<br>• Confirm secret values are sourced from Secret Manager, not env files. | - OPA constraint templates<br>- GKE Ingress YAML | - `kubectl get pods -n dev -o jsonpath="{.items[*].spec.containers[*].securityContext.runAsNonRoot}"` returns `true`.<br>- `curl -k https://api.dev.example.com/health` returns valid TLS cert. |

---

## 4. Phase Definition of Done (DoD)  

The Phase 2 release is considered **Done** when **all** of the following criteria are satisfied:

1. **Functional Completeness**  
   - All MVP services (Auth, Learner, Attendance, Notification) are deployed and reachable via their documented OpenAPI endpoints.  
   - End‑to‑end user journey (login → QR scan → attendance recorded → notification queued) works in the dev GKE namespace.  
   - Web UI displays correct remaining membership days after attendance and respects locale detection hierarchy (user‑choice > browser > default).  

2. **Quality & Testing**  
   - Unit + integration test suites pass with **≥ 80 %** Java coverage and **≥ 85 %** TypeScript coverage.  
   - Load test of the attendance endpoint meets **≤ 200 ms** 95th‑percentile latency at **500 RPS**.  
   - No critical or high severity vulnerabilities reported by Trivy or Snyk.  

3. **Compliance & Guardrails**  
   - All code passes SonarQube Quality Gate (no blocker issues).  
   - No secrets are present in the repository; all runtime secrets are injected from GCP Secret Manager.  
   - Istio