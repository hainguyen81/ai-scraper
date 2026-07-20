# PHASE 5 CONTEXT BLUEPRINT: test‑ai‑architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| **Production‑grade deployment** | Deploy the full stack (Quarkus services, Kafka, PostgreSQL, Next.js web, React‑Native mobile) to a **regional GKE Autopilot cluster** with zero‑downtime upgrade capability. | 99.9 % availability over a 30‑day observation window; no ≥ 5 min outage during rollout. |
| **GitOps & CI/CD maturity** | Codify Helm charts, Kustomize overlays, and Argo CD applications; enforce automated image promotion (dev → staging → prod) with canary & blue‑green strategies. | 100 % of releases pass automated gate (unit, integration, security, performance) before promotion. |
| **Observability & Alerting** | Implement end‑to‑end tracing (OpenTelemetry), metrics (Prometheus), logs (Stackdriver), and dashboards (Grafana) for all services, including QR‑attendance latency, notification delivery rates, and mobile‑app crash‑free sessions. | SLA: 95th‑percentile API latency ≤ 200 ms; alert on error‑rate > 1 % within 2 min. |
| **Disaster Recovery & Backup** | Configure CloudSQL automated backups + cross‑region read replica; Kafka MirrorMaker2 for multi‑region topic replication; periodic restore drills. | Successful restore of latest backup within 30 min; DR drill pass rate ≥ 95 %. |
| **Governance & Compliance Automation** | Enforce OPA Gatekeeper policies, Istio mTLS, secret rotation via Secret Manager, and immutable audit logging for authentication, attendance, and notification events. | Zero critical findings in Snyk/Trivy scans; audit logs retained ≥ 1 year and tamper‑evident. |
| **Feature‑flag & Continuous Improvement** | Integrate a lightweight feature‑flag service (e.g., Unleash) to allow safe rollout of new UI/notification capabilities without redeploy. | Feature flag toggles can be changed in < 5 seconds and are reflected in live traffic. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Repository / Directory | Allowed Files / Paths | Public API Endpoints (base) |
|------|------------------------|----------------------|-----------------------------|
| **Backend (Quarkus)** | `backend/` | `src/main/java/**`, `src/main/resources/application.yml`, `src/main/resources/META-INF/resources/**`, `Dockerfile`, `pom.xml`, `flyway/**` | `https://api.<domain>/v1/auth/**`<br>`https://api.<domain>/v1/learners/**`<br>`https://api.<domain>/v1/attendance/**`<br>`https://api.<domain>/v1/notifications/**` |
| **Event Streaming** | `infra/kafka/` | `kafka-topics.yaml`, `kafka-connect/**`, `schema-registry/**` | N/A (internal topics: `attendance-events`, `notification-queue`, `analytics-stream`) |
| **Database** | `infra/postgres/` | `sql/**` (DDL, seed), `flyway/**` (migration scripts) | N/A (access via backend services only) |
| **Web Front‑end (Next.js)** | `frontend/web/` | `pages/**`, `components/**`, `public/**`, `next.config.js`, `i18n/**`, `Dockerfile` | `https://<domain>/` (SSR pages) – locale‑prefixed routes e.g., `/en/dashboard`, `/vi/qr-scan` |
| **Mobile Front‑end (React Native)** | `frontend/mobile/` | `src/**`, `app.json`, `expo/**`, `i18n/**`, `Dockerfile` (for Expo web build) | N/A (bundled app) – uses same API base as web (`https://api.<domain>/v1/...`) |
| **GitOps / Helm** | `infra/helm/` | `charts/**`, `values-prod.yaml`, `values-staging.yaml`, `ArgoCD/**` | N/A (Argo CD sync endpoint) |
| **Observability** | `infra/monitoring/` | `prometheus/**`, `grafana/**`, `otel-collector/**` | N/A |
| **Security / Policies** | `infra/policies/` | `opa/**`, `istio/**`, `secret-manager/**` | N/A |

> **Boundary Rule:** Sub‑agents must **only modify files within their designated directory**. No cross‑directory edits unless explicitly coordinated through a **Manager‑approved change request**.

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Core Tasks for Phase 5 | Deliverable Artifacts |
|-----------|------------------------|-----------------------|
| **Coder** | 1. Refactor all Quarkus services to expose **health‑check** (`/q/health/live`, `/q/health/ready`) and **metrics** (`/q/metrics`).<br>2. Convert Dockerfiles to **multi‑stage GraalVM native builds** (optional fallback to JVM).<br>3. Add **OpenTelemetry instrumentation** (HTTP, gRPC, Kafka) and export to GCP Trace.<br>4. Implement **feature‑flag checks** (`FeatureToggle.isEnabled("new‑notification‑format")`).<br>5. Ensure **i18n strings** are externalized in `frontend/**/i18n/*.json` and referenced via `next-i18next`. | Updated `Dockerfile`s, `application.yml` with OTEL config, new `src/main/java/.../HealthResource.java`, `feature-toggle` module, i18n JSON files. |
| **Tester** | 1. Write **end‑to‑end (E2E) Cypress** tests covering login (email/Firebase), QR‑attendance idempotency, and locale‑aware UI rendering.<br>2. Create **k6 performance scripts** simulating 5 k concurrent users across 3 centers, measuring latency & error‑rate.<br>3. Add **Chaos Monkey** (Litmus) scenarios for pod‑kill, network‑latency, and Kafka broker failure; verify auto‑recovery.<br>4. Validate **disaster‑recovery restore** scripts (PostgreSQL dump restore, Kafka MirrorMaker failover). | `cypress/integration/**.spec.js`, `k6/scripts/load-test.js`, `litmus/chaos‑experiments.yaml`, DR test report (PDF). |
| **Reviewer** | 1. Enforce **OPA Gatekeeper** policies: no privileged containers, image tag must be a digest, required labels (`app.kubernetes.io/name`, `environment`).<br>2. Run **static analysis** (SonarQube) on Java & TypeScript; reject any new **critical** issues.<br>3. Verify **Helm chart linting** (`helm lint`) and that values files do not contain hard‑coded secrets.<br>4. Approve **canary release** PRs only after successful E2E & performance test results are attached. | Review checklist, OPA policy compliance report, SonarQube quality gate screenshot, Helm lint output. |
| **DevOps (Deployer)** | 1. Create **Argo CD Application** manifests for `prod` and `staging` environments, with **automated sync** and **health checks**.<br>2. Define **Helm values** for autoscaling (CPU target 70 %), pod disruption budgets, and **PodSecurityPolicy** replacements via Gatekeeper.<br>3. Set up **Prometheus ServiceMonitors** for each micro‑service and **Grafana dashboards** (API latency, attendance count, notification delivery).<br>4. Configure **Google Cloud Build** triggers: `dev → staging` (canary), `staging → prod` (blue‑green).<br>5. Implement **secret rotation pipeline** (Cloud Scheduler → Cloud Functions) that updates Secret Manager and rolls out new env vars without downtime. | `ArgoCD/production.yaml`, `helm/values-prod.yaml`, `prometheus/servicemonitor.yaml`, `grafana/dashboards/*.json`, Cloud Build YAML files, secret‑rotation script. |

## 4. Phase Definition of Done (DoD)  

- **Infrastructure**  
  - GKE regional Autopilot cluster (2‑zone) fully provisioned and **Argo CD** syncing all Helm releases.  
  - All services reachable via the documented public API endpoints with **TLS 1.3** enforced.  
  - Istio mTLS enabled cluster‑wide; OPA Gatekeeper policies passing for every pod.  

- **Deployment**  
  - Docker images built as **GraalVM native** (or JVM fallback) and stored in **Artifact Registry** with immutable digests.  
  - Canary rollout of the latest version completed; 100 % of traffic shifted to stable after automated health verification.  

- **Observability**  
  - Prometheus scraping confirmed for every service; Grafana dashboards display real‑time metrics.  
  - OpenTelemetry traces appear in **Google Cloud Trace** for a sample request flow (login → QR scan → notification).  

- **Reliability**  
  - Automated backup schedule active; latest backup restored in a test environment with **data integrity check** passed.  
  - Chaos tests executed with **no data loss** and automatic recovery within defined SLO (≤ 30 s).  

- **Security & Compliance**  
  - No critical vulnerabilities reported by **Trivy** and **Snyk** scans.  
  - All audit logs (auth, attendance, notifications) are immutable in **Cloud Logging** with retention ≥ 365 days.  
  - GDPR/PDPA data‑subject request endpoint (`/v1/users/{id}/data‑export`) functional and tested.  

- **Quality Assurance**  
  - 100 % of **Cypress E2E** tests pass on both web and mobile builds.  
  - **k6** load test meets SLA: 95th‑percentile latency ≤ 200 ms, error rate < 1 % at 5 k concurrent users.  

- **Documentation & Handover**  
  - Runbooks for **deployment**, **disaster recovery**, **feature‑flag management**, and **incident response** stored in Confluence and linked from the repo README.  
  - All code reviewed and approved by **Reviewer**; PRs merged with **“Ready for Production”** label.  

> **Go/No‑Go Gate:** The Manager, Reviewer, and Tester must sign off on the above criteria. Only after collective approval does the phase transition to “Production Live”.