# PHASE 4 CONTEXT BLUEPRINT: test‑ai‑architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| **Global SEO Enablement** | Render every public page (center landing, course catalog, blog, login, registration) with **server‑side rendering (SSR)**, locale‑specific URLs (`/en/…`, `/vi/…`, `/zh/…`), dynamic sitemaps, and **JSON‑LD** structured data for centers, courses, and events. | Google Lighthouse SEO score **≥ 80** for each supported locale; sitemap crawled without errors in Google Search Console. |
| **Full Internationalization (i18n) Hardening** | Consolidate all UI strings into locale JSON bundles, implement **next‑i18next** middleware for locale detection (user‑saved preference → cookie → browser/device locale), and enforce fallback hierarchy. | 100 % of UI text externalized; automated test verifies correct locale rendering for at least **3** languages. |
| **Compliance & Security Hardening** | Apply **OPA/Gatekeeper** policies, enforce **Istio mTLS**, rotate secrets via **Secret Manager**, add GDPR/PDPA data‑subject‑request (DSR) endpoints, and embed audit‑log hooks for attendance & notification events. | No critical findings in Snyk/Trivy scans; DSR endpoint passes OWASP ASVS L2 test; audit logs immutable for ≥ 1 year. |
| **Observability & Performance Tuning for SEO** | Instrument Next.js pages and Quarkus services with **OpenTelemetry**, expose **Prometheus** metrics for page‑load time, TTFB, and API latency; configure **Cloud CDN** for static assets. | 95th‑percentile page TTFB **≤ 200 ms**; API latency **≤ 200 ms** under 5 k concurrent users. |
| **Documentation & Governance** | Update architecture diagrams, runbooks, and compliance checklists; create a **Phase‑4 Release Playbook** for go/no‑go gate. | Release Playbook approved by Manager, Reviewer, and Tester; documentation versioned in `docs/phase4/`. |

---

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Allowed Path / Package | Example Files | Public API Endpoints (REST) |
|-------|------------------------|---------------|-----------------------------|
| **Web Front‑end (Next.js)** | `frontend/` <br>• `pages/` (SSR pages) <br>• `components/` <br>• `i18n/` (locale JSON) <br>• `next.config.js` (i18n, rewrites) | `pages/[locale]/center/[slug].tsx` <br>`i18n/en/common.json` | **GET** `/api/seo/sitemap.xml` <br>**GET** `/api/seo/robots.txt` |
| **Mobile Front‑end (React Native via Expo)** | `mobile/` <br>• `src/locales/` <br>• `src/screens/` | `src/locales/vi/strings.ts` | No public HTTP endpoints – consumes same backend APIs as web. |
| **Backend Services (Quarkus)** | `services/` <br>• `auth/` <br>• `learner/` <br>• `attendance/` <br>• `notification/` <br>• `compliance/` | `attendance/src/main/java/.../AttendanceResource.java` <br>`compliance/src/main/java/.../DataSubjectRequestResource.java` | **POST** `/api/v1/attendance/scan` <br>**GET** `/api/v1/attendance/{learnerId}/summary` <br>**POST** `/api/v1/compliance/dsr` |
| **Infrastructure / IaC** | `infra/` <br>• `helm/` (charts) <br>• `k8s/` (manifests) <br>• `opa/` (policy files) | `helm/membership-hub/values.yaml` <br>`opa/policies/ingress.rego` | N/A (applies to cluster resources) |
| **Observability** | `observability/` <br>• `otel/` (collector config) <br>• `prometheus/` (rules) | `otel/collector-config.yaml` <br>`prometheus/rules.yaml` | N/A |
| **Security / Secrets** | `secrets/` (never committed – referenced via Secret Manager) | *No source files* – runtime injection only | N/A |
| **Documentation** | `docs/phase4/` | `seo-guidelines.md` <br>`compliance-checklist.md` | N/A |

> **Boundary Rule:** No code outside the listed directories may be modified in Phase 4. All new files must reside under the appropriate path above.  

---

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Concrete Tasks for Phase 4 | Acceptance Artifacts |
|-----------|----------------------------|----------------------|
| **Coder** | 1. Implement **SSR** for all public pages using `getServerSideProps` and locale‑aware routing. <br>2. Add **next‑i18next** middleware (`middleware.ts`) to resolve locale precedence (user‑saved → cookie → Accept‑Language). <br>3. Create **SEO components** (`<Head>` tags, JSON‑LD generator) and expose `/api/seo/sitemap.xml` & `/api/seo/robots.txt`. <br>4. Develop **GDPR/PDPA DSR endpoint** (`/api/v1/compliance/dsr`) with request validation, audit logging, and data export (CSV/JSON). <br>5. Harden backend services: enable **Istio mTLS** client‑side config, add OPA policy checks (`@Inject OpaClient`). <br>6. Add **OpenTelemetry** instrumentation to Quarkus (`quarkus-opentelemetry`) and Next.js (`@opentelemetry/sdk-node`). | - PR with updated `frontend/` and `services/compliance/` code. <br>- Unit tests ≥ 80 % coverage for new modules. |
| **Tester** | 1. Write **Cypress** e2e tests for locale detection (switch language, reload, verify URL). <br>2. Create **Lighthouse CI** job to assert SEO score ≥ 80 per locale. <br>3. Develop **Postman** collection for DSR flow (request, verify data deletion/export). <br>4. Execute **OWASP ZAP** scan on new endpoints; log any findings. <br>5. Load‑test `/api/v1/attendance/scan` under SEO‑enabled traffic using **k6** (simulate 5 k concurrent users). | - Cypress test suite in `frontend/tests/`. <br>- Lighthouse report artifacts. <br>- ZAP scan report with zero critical issues. |
| **Reviewer** | 1. Validate that all UI strings are externalized; run `i18n-lint` script. <br>2. Review OPA policies for **ingress** and **data‑subject‑request** compliance. <br>3. Ensure Dockerfiles use **distroless** base, non‑root user, and that image tags are immutable digests. <br>4. Confirm that **Secret Manager** references replace any hard‑coded secrets. <br>5. Approve PR only after SonarQube quality gate passes (no new bugs/vulnerabilities). | - Review checklist signed off in PR comments. <br>- SonarQube badge attached to PR. |
| **DevOps / Deployer** | 1. Extend **Helm chart** with new ConfigMaps for SEO (`seo-config.yaml`) and OPA policies (`opa-policy.yaml`). <br>2. Add **Kubernetes NetworkPolicy** to restrict ingress to `/api/v1/compliance/*` to internal services only. <br>3. Configure **Cloud CDN** for `frontend/.next/static/` and `public/` assets via GCP Load Balancer. <br>4. Update **Argo CD** Application manifests to include `phase4` overlay (`values-phase4.yaml`). <br>5. Implement **Canary rollout** for SEO changes using Argo Rollouts (5 % → 100 %). <br>6. Create **Prometheus alerts** for page‑load‑time > 300 ms and for any OPA policy violation. | - Updated Helm chart in `infra/helm/`. <br>- Argo CD diff showing new overlay. <br>- Canary rollout manifest (`rollout.yaml`). <br>- Alert rules in `observability/prometheus/`. |

---

## 4. Phase Definition of Done (DoD)  

The phase is considered **Done** when **all** items below are satisfied and signed off by the Manager, Reviewer, and Tester:

1. **Functional**  
   - All public pages render server‑side with correct locale‑specific URLs and meta tags.  
   - SEO endpoints (`/sitemap.xml`, `/robots.txt`) return valid XML/robots content for every supported language.  
   - Data‑subject‑request API fully functional, audited, and returns correct data export.  
   - Internationalization detection respects the hierarchy (saved preference → cookie → browser/device).  

2. **Quality & Testing**  
   - Cypress e2e suite passes on Chrome, Firefox, and mobile emulation.  
   - Lighthouse CI reports **≥ 80** SEO score for each locale.  
   - Unit test coverage for new code **≥ 80 %**; integration tests for DSR pass.  
   - OWASP ZAP scan reports **zero** critical/high findings on new endpoints.  

3. **Security & Compliance**  
   - OPA policies enforced (gatekeeper logs show no violations).  
   - Istio mTLS enabled for all inter‑service traffic; verification via `istioctl authn tls-check`.  
   - No secrets hard‑coded; all secret references point to GCP Secret Manager.  
   - Docker images built from **distroless** base, scanned with Trivy, and stored with immutable digest.  

4. **Observability & Performance**  
   - OpenTelemetry traces visible in Cloud Trace for both web and backend requests.  
   - Prometheus metrics for page TTFB and API latency exported; alerts configured.  
   - Load test shows **≤ 200 ms** 95th‑percentile latency under 5 k concurrent users.  

5. **Deployment & Release**  
   - Helm chart version bumped (`appVersion: 4.0.0`) and deployed via Argo CD with successful canary promotion.  
   - Cloud CDN correctly caches static assets; verified via `curl -I` headers (`x-cache: HIT`).  
   - Release Playbook documented in `docs/phase4/release-playbook.md` and approved.  

6. **Documentation & Governance**  
   - Architecture diagram updated to include SEO & compliance components.  
   - Runbooks for DSR handling and OPA policy updates published.  
   - All changes recorded in the project changelog (`CHANGELOG.md`) with a **Phase 4** entry.  

> **Go/No‑Go Gate:** If any single DoD item is missing or fails verification, the phase is **No‑Go** and must be re‑worked before proceeding to Phase 5.