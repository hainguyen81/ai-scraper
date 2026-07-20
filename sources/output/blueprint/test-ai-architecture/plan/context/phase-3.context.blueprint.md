# PHASE 3 CONTEXT BLUEPRINT: test‑ai‑architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| **Front‑end delivery** | Implement the **Next.js web portal** (admin view) and the **React‑Native mobile app** (learner view) with full i18n support, SEO‑friendly SSR, and QR‑code scanning capability. | • 100 % of UI screens rendered server‑side for web.<br>• Mobile app builds for iOS & Android pass Apple/Google store lint. |
| **Locale handling** | Detect and persist user language preference, falling back to browser/device locale, then to default `en‑US`. | • Locale fallback logic covered by automated tests (≥ 95 % pass). |
| **QR attendance flow** | End‑to‑end flow: QR scan → call `attendance-service` → optimistic UI update showing remaining membership days. | • End‑to‑end latency < 200 ms (measured via OpenTelemetry). |
| **Integration readiness** | Expose front‑end endpoints that the back‑end `attendance-service` and `notification-service` will consume; ensure contracts are versioned. | • Contract tests (Pact) pass with zero mismatches. |
| **CI/CD pipeline** | Add front‑end build jobs, Docker image creation, and automated deployment to a **staging GKE namespace** (`membership-hub‑stg`). | • Pipeline success rate ≥ 99 % over 5 consecutive runs. |
| **Observability hooks** | Instrument UI with OpenTelemetry (web & RN) and expose Prometheus metrics for page‑load & QR‑scan latency. | • Grafana dashboards show < 200 ms 95th‑percentile latency. |

---

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Allowed Path / Repo Root | Key Files / Artifacts | Public API Endpoints (to be consumed by back‑end) |
|-------|--------------------------|-----------------------|---------------------------------------------------|
| **Web portal (Next.js)** | `frontend/web/` | `pages/`, `components/`, `i18n/`, `next.config.js`, `next-seo.config.js`, `Dockerfile.web` | `GET /api/tenants/:tenantId/locale` (locale fetch)<br>`GET /api/attendance/:memberId/status` (remaining days) |
| **Mobile app (React Native / Expo)** | `frontend/mobile/` | `src/`, `app.json`, `i18n/`, `Dockerfile.mobile` (for Expo web preview) | `POST /api/attendance/scan` (QR payload) – called via **fetch** from RN code |
| **Shared UI library** | `frontend/shared/` | `components/`, `utils/locale.ts`, `utils/qr.ts` | N/A (internal) |
| **Static assets** | `frontend/public/` | `locales/`, `images/qr-placeholder.svg` | N/A |
| **Infrastructure as Code (IaC)** | `infra/helm/charts/membership-hub-frontend/` | `Chart.yaml`, `values.yaml`, `templates/deployment.yaml`, `templates/service.yaml` | N/A |
| **Observability** | `frontend/otel/` | `otel-config.js`, `otel-metrics.ts` | N/A |
| **Testing** | `frontend/tests/` | `cypress/`, `playwright/`, `unit/` | N/A |

> **Boundary rule:** No changes are permitted outside the `frontend/` tree or the `infra/helm/charts/membership-hub-frontend/` chart during Phase 3. All back‑end code (`src/main/java/...`) remains frozen; any required contract change must be communicated to Phase 2 owners via a **Contract Change Request** ticket.

---

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Core Tasks (specific to Phase 3) | Deliverable Artefacts | Acceptance Criteria |
|-----------|----------------------------------|-----------------------|---------------------|
| **Coder** | 1. Scaffold Next.js project with TypeScript, i18next, and `next-seo` plugin.<br>2. Implement locale detection logic (`utils/locale.ts`) that reads stored preference → browser locale → default.<br>3. Build QR‑scanner component using `expo-camera` / `react-qr-reader` that returns a JSON payload `{ tenantId, memberId, timestamp }`.<br>4. Wire UI to call `POST /api/attendance/scan` (via `fetch`) and display remaining days returned from back‑end.<br>5. Create responsive admin dashboard page showing attendance logs per center (read‑only, consumes `GET /api/attendance/:memberId/status`).<br>6. Write Dockerfile for multi‑stage build (builder → nginx static serve).<br>7. Add OpenTelemetry web instrumentation (`frontend/otel/`). | - Complete source tree under `frontend/web/` and `frontend/mobile/`.<br>- Docker images pushed to Artifact Registry (`membership-hub-web:stg`, `membership-hub-mobile:stg`).<br>- Helm chart values updated for image tags. | - `npm run lint` passes with 0 errors.<br>- `npm run build` succeeds and produces SSR output.<br>- Image size ≤ 150 MB (native) or ≤ 300 MB (JVM‑based). |
| **Tester** | 1. Write unit tests for locale utility (Jest) and QR‑scanner wrapper (Jest + React Native Testing Library).<br>2. Create Cypress end‑to‑end flow: visit web portal → set locale → scan QR (mock) → verify remaining days UI update.<br>3. Create Playwright mobile‑web test simulating RN QR scan and push‑notification mock.<br>4. Implement contract tests (Pact) for the two front‑end APIs (`GET /api/attendance/:memberId/status`, `POST /api/attendance/scan`).<br>5. Add performance test script (k6) that measures page‑load + QR‑scan latency in staging. | - `frontend/tests/unit/` suite.<br>- `frontend/tests/e2e/` Cypress & Playwright scripts.<br>- `frontend/tests/contracts/attendance.pact.json`.<br>- `frontend/tests/perf/k6-scan.js`. | - ≥ 80 % code coverage for new files.<br>- All CI test jobs pass in two consecutive runs.<br>- Performance script reports 95th‑percentile latency < 200 ms. |
| **Reviewer** | 1. Conduct PR review for every Coder commit: verify adherence to lint rules, security (no hard‑coded secrets), and UI accessibility (WCAG 2.1 AA).<br>2. Run SonarQube quality gate on the PR; ensure no new blocker/critical issues.<br>3. Validate contract files against the back‑end contract baseline; raise a **Contract Change Request** if mismatched.<br>4. Approve Helm chart changes only if they respect the naming convention (`membership-hub-frontend-<env>`). | - Review comments documented in GitHub PRs.<br>- Signed-off review checklist attached to each merged PR. | - Review turnaround ≤ 12 h.<br>- No high‑severity findings remain after merge.<br>- All contract tests pass in CI. |
| **DevOps (Deployer)** | 1. Extend the existing GitHub Actions workflow (`ci-cd.yml`) with jobs: `frontend-build-web`, `frontend-build-mobile`, `docker-push-web`, `docker-push-mobile`, `helm-deploy-staging`.<br>2. Configure **ArgoCD** application `membership-hub-frontend-stg` pointing to the Helm chart in `infra/helm/charts/membership-hub-frontend/`.<br>3. Set up **Kubernetes NetworkPolicy** to allow only ingress from the API gateway (`gateway.namespace.svc.cluster.local`) to the front‑end pods.<br>4. Add Prometheus ServiceMonitor for the front‑end pods exposing `/metrics` (via `express-prom-bundle`).<br>5. Implement a **blue‑green** deployment strategy using ArgoCD sync waves and a `canary` label for the first rollout. | - Updated `.github/workflows/ci-cd.yml`.<br>- ArgoCD Application manifest (`argocd-app-frontend-stg.yaml`).<br>- Helm values file with `image.tag` placeholders.<br>- NetworkPolicy YAML (`frontend-np.yaml`). | - Staging deployment succeeds without manual intervention.<br>- Rollback to previous version completes in < 5 min.<br>- Prometheus scrapes `/metrics` with no errors. |

---

## 4. Phase Definition of Done (DoD)  

The Phase 3 is considered **Done** when **all** of the following criteria are satisfied and signed off by the **Manager**:

1. **Functional**  
   - Web portal and mobile app are deployed to the **staging** GKE namespace and are reachable via HTTPS.  
   - QR‑attendance flow works end‑to‑end: scanning a QR updates the UI with the correct remaining membership days (validated against a seeded test tenant).  
   - Locale detection respects stored preference, browser/device locale, and default fallback; UI strings change accordingly.  

2. **Quality**  
   - Unit, integration, and contract test suites pass with ≥ 80 % coverage for new code.  
   - No SonarQube **blocker** or **critical** issues remain.  
   - Accessibility audit (axe‑core) reports no violations above WCAG AA.  

3. **Performance & Observability**  
   - OpenTelemetry traces show QR‑scan → back‑end → UI update latency ≤ 200 ms (95th percentile) in the staging Grafana dashboard.  
   - Prometheus metrics for page load time and QR‑scan latency are exposed and visualized.  

4. **Security & Compliance**  
   - All secrets are sourced from **Secret Manager**; no secret appears in source code or Docker images.  
   - Images are signed with **Cosign** and verified in the CI pipeline.  
   - NetworkPolicy restricts traffic as defined; mTLS is enforced between front‑end and API gateway.  

5. **Infrastructure**  
   - Helm chart version `0.3.0` is released to Artifact Registry and referenced in the ArgoCD Application.  
   - Blue‑green deployment to staging completed without downtime; rollback tested successfully.  

6. **Documentation**  
   - README in `frontend/` updated with build, run, and deployment instructions.  
   - Architecture diagram (updated for front‑end components) added to Confluence.  
   - End‑to‑end test scripts and contract files are version‑controlled and referenced in the project wiki.  

7. **Sign‑off**  
   - Manager records a **Phase 3 Review** meeting minutes, confirming that all acceptance criteria are met.  
   - All sub‑agents have updated their status boards (Jira) to **Done** for Phase 3 tickets.  

*Only after the above DoD checklist is fully satisfied will the project advance to Phase 4 (Notification Engine & Zalo Integration).*