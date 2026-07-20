# PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture  

## 1. Phase Operational Scope & Objectives  

| Goal | Description | Success Indicator |
|------|-------------|--------------------|
| **Multilingual Web Portal** | Deliver a Next.js (React) web application that serves administrators, teachers, and staff. Must expose SEO‑friendly language sub‑paths (`/en/`, `/vi/`, …) and generate correct `hreflang` tags. | All public pages render with correct language content and SEO meta tags; Lighthouse SEO score ≥ 90. |
| **Cross‑Platform Mobile App** | Build a React‑Native (Expo) mobile application sharing the same component library as the web portal. Supports iOS & Android, QR‑code scanning for attendance, push notifications via FCM, and Zalo‑SMS fallback. | QR‑check‑in works on both platforms; push notification receipt rate ≥ 95 %. |
| **Internationalization (i18n) Engine** | Implement deterministic locale detection: **user‑saved preference → cookie → `Accept‑Language` header → default `en`**. Provide runtime locale switch without full page reload. | Locale resolves correctly in 99 % of manual test matrix (different browsers, devices, logged‑in/out). |
| **QR Attendance Flow** | Mobile app scans a QR code, calls the backend `/attendance/checkin` endpoint, receives idempotent response, and displays remaining membership days. | Attendance API returns `200 OK` with `daysRemaining` and UI updates instantly; duplicate scans on same day are ignored. |
| **Notification Integration** | After successful check‑in, trigger: <br>• Firebase Cloud Messaging (FCM) push to the device <br>• Zalo Business API SMS to the learner’s phone <br>• Zalo group message to the center’s group. | End‑to‑end test shows all three channels fire within 2 seconds of check‑in. |
| **CI/CD & Quality Gates** | Extend the existing pipeline to lint, type‑check, run unit & e2e tests, and produce a Docker multi‑stage image (Node → native‑bundle). Deploy to GKE `frontend` namespace via Helm. | Pipeline passes all gates on every PR; image size ≤ 120 MB; zero‑downtime rollout. |
| **Accessibility Compliance** | Ensure WCAG 2.1 AA compliance for both web and mobile UI components. | Automated axe‑core audit ≤ 5 issues; manual review sign‑off. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Area | Allowed Path / File Pattern | Reason / Guardrail |
|------|-----------------------------|--------------------|
| **Next.js Web Source** | `frontend/web/**` (root of repo) | Isolated from mobile code; only web‑specific pages (`pages/**/*.tsx`). |
| **React‑Native Mobile Source** | `frontend/mobile/**` (Expo project) | Separate Metro bundler config; shares `components/` via a symlink or npm workspace. |
| **Shared UI Library** | `frontend/shared/**` (React components, hooks, i18n config) | Enforced by `eslint-plugin-import` to prevent cross‑import of backend code. |
| **i18n Resources** | `frontend/**/locales/{en,vi,es,fr}/**.json` | Must be pure JSON, no executable code (guardrail: Trivy scans for secrets). |
| **API Client** | `frontend/**/src/api/**.ts` | Calls only whitelisted backend endpoints (see below). |
| **Backend Endpoints Used by Front‑End** | - `POST /api/v1/attendance/checkin`  <br> - `GET /api/v1/membership/{learnerId}` <br> - `GET /api/v1/tenants/{tenantId}/i18n` (optional) | All endpoints must be documented in OpenAPI spec; versioned under `/api/v1/`. |
| **Static Assets** | `frontend/web/public/**` & `frontend/mobile/assets/**` | Served via CDN; no sensitive data. |
| **Dockerfile** | `frontend/Dockerfile` (multi‑stage) | Must use `node:18-alpine` base, then `npm run build && npm prune --production`. |
| **Helm Chart** | `infra/charts/frontend/**` | Namespace: `frontend`; resource quotas enforced per tenant via `values.yaml`. |
| **CI/CD Config** | `.github/workflows/frontend.yml` | Includes lint, type‑check, unit, Cypress (web) & Detox (mobile) jobs, Docker build, Argo CD sync. |
| **Testing Artifacts** | `frontend/tests/**` (unit), `frontend/e2e/**` (Cypress), `frontend/mobile-e2e/**` (Detox) | Must achieve coverage thresholds defined in `jest.config.js`. |
| **Accessibility Tests** | `frontend/tests/a11y/**` | Run with `axe-core/playwright`. |

> **Note:** No front‑end code may read/write directly to `src/main/resources/**` (backend) or `infra/**` (IaC) – any cross‑layer interaction must go through the defined REST/GraphQL APIs.

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Core Tasks for Phase 3 | Deliverable Artifacts | Guardrail Checks |
|-----------|------------------------|-----------------------|------------------|
| **Coder** | 1. Scaffold Next.js monorepo with `web`, `mobile`, `shared`. <br>2. Implement locale detection middleware (`middleware.ts`). <br>3. Build QR‑scanner screen using Expo Camera, integrate with backend `/attendance/checkin`. <br>4. Create membership‑days card component showing decrement logic. <br>5. Wire FCM token registration and Zalo API call via backend event (publish to `notification` Kafka topic). <br>6. Add SEO meta tags (`next/head`) and `hreflang` links per page. <br>7. Write TypeScript types for all API contracts (generated from OpenAPI). | - PRs with updated `frontend/` tree <br>- Updated `README.md` with build/run instructions <br>- `openapi-client.ts` generated file | - ESLint + Prettier (no errors) <br>- TypeScript `noImplicitAny` <br>- Hadolint on Dockerfile <br>- Trivy scan (no secrets) |
| **Tester** | 1. Unit tests for locale middleware, API client, UI components (Jest + React Testing Library). <br>2. Cypress end‑to‑end flow: language switch → QR scan → membership days update → notification toast. <br>3. Detox mobile flow: launch app, change language, scan QR (mock camera), verify push notification receipt (FCM mock). <br>4. Accessibility audit using `axe-core/playwright` on key pages and mobile screens. <br>5. Performance budget checks (page load < 2 s on 3G). | - `frontend/tests/` coverage report <br>- `frontend/e2e/` Cypress video & screenshots <br>- `frontend/mobile-e2e/` Detox logs <br>- `a11y-report.html` | - Coverage ≥ 80 % (lines) <br>- No critical accessibility violations <br>- Cypress test flakiness < 5 % |
| **Reviewer** | 1. Validate that all new dependencies are approved (internal allow‑list). <br>2. Verify i18n JSON files contain no embedded secrets (run `git‑secret` scan). <br>3. Confirm that every new API call matches the OpenAPI spec (use `swagger‑cli validate`). <br>4. Ensure Docker image size ≤ 120 MB and base image is `node:18-alpine`. <br>5. Check that Helm values enforce `resourceQuota` per tenant. | - PR review comments <br>- Approval checklist (attached as `REVIEW_CHECKLIST.md`) | - SonarQube quality gate ≥ A <br>- Checkov IaC scan passes <br>- No new high‑severity vulnerabilities (Trivy). |
| **DevOps (Deployer)** | 1. Extend `frontend/Dockerfile` to multi‑stage build, push to Artifact Registry (`gcr.io/<project>/frontend`). <br>2. Update Helm chart `infra/charts/frontend` with new image tag, health‑check endpoint (`/healthz`). <br>3. Configure Argo CD Application `frontend` targeting `frontend` namespace, enable automated sync with manual approval for prod. <br>4. Add Prometheus metrics exporter (`next-exporter`) for page‑render latency and locale switch count. <br>5. Set up GKE `ResourceQuota` objects per tenant (via Terraform module `tenant_quota`). | - Updated Docker image in Artifact Registry <br>- Helm chart version bump (`Chart.yaml`) <br>- Argo CD Application manifest (`argocd-apps.yaml`) <br>- Terraform plan/apply output for quotas | - Image scan (Trivy) passes <br>- Helm lint (`helm lint`) succeeds <br>- Argo CD health checks green <br>- GKE pod security policies enforced (no privileged containers). |

## 4. Phase Definition of Done (DoD)  

The phase is considered **Done** only when **all** items below are satisfied and signed off by the **Manager** and **Reviewer**:

1. **Feature Completion**  
   - Web portal and mobile app fully functional with multilingual UI, QR attendance, membership‑day display, and notification triggers.  
   - Locale detection works as defined in the hierarchy and persists user preference.  

2. **Quality Gates**  
   - Linting, type‑checking, and static analysis all pass with **no errors**.  
   - Unit test coverage ≥ 80 % (lines) and integration/E2E pass ≥ 95 % on the latest commit.  
   - Accessibility audit reports ≤ 5 minor issues, 0 critical.  

3. **Security & Guardrail Compliance**  
   - No secrets in repository (verified by secret‑scan).  
   - Docker image scanned with Trivy shows **no** HIGH or CRITICAL CVEs.  
   - All new API calls conform to the OpenAPI contract; no undocumented endpoints.  
   - Resource quotas applied per tenant; Istio policies unchanged (still enforced).  

4. **Observability & Monitoring**  
   - Prometheus metrics for page render latency and locale switches are exposed and visible in Grafana dashboards.  
   - Health‑check endpoint (`/healthz`) returns 200 within 2 seconds.  

5. **Documentation**  
   - README updated with **local development**, **Docker build**, **Kubernetes deployment**, and **testing** instructions.  
   - i18n contribution guide added (`docs/i18n.md`).  
   - Run‑book for QR‑check‑in flow and notification fallback documented (`docs/runbooks/attendance.md`).  

6. **Deployment**  
   - Image successfully deployed to the **staging** GKE cluster (`frontend` namespace) via Argo CD with zero downtime.  
   - Manual approval performed and image promoted to **production** environment; rollout completed within 5 minutes.  

7. **Stakeholder Sign‑off**  
   - Product Owner (Manager) confirms UI/UX meets design specs (Figma).  
   - Security Officer validates guardrail compliance report.  

Once the above criteria are met, the Phase Gate Review is closed, and the project proceeds to **Phase 4 – Notification Engine & Business Rules**.