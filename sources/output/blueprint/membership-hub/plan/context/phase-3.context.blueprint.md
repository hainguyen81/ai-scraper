# PHASE 3 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- **Next.js Web UI Construction** – Create the admin dashboard and all management screens (Centers, Courses, Teachers, Students, Promotions, Notifications, AI CSKH chat) using Next.js SSG/SSR patterns.  
- **i18n & SEO Integration** – Configure `next-i18next` for multi‑language support (en, vi, …), generate hreflang tags, locale detection from user preference → browser → fallback, and embed SEO metadata per page.  
- **Role‑Based UI Routing & Permission Guards** – Implement a guard that reads the JWT `roles` claim and `tenant_id`, enforces the defined RBAC matrix, and redirects unauthorized users.  
- **Real‑Time Dashboard Auto‑Refresh** – Add a 15‑minute interval fetch for dashboard widgets (course count, active teachers, student day counters, promotions, announcements) using a custom React hook.  
- **API Integration** – Expose/Consume REST endpoints for QR attendance scanning, student day‑counter updates, and notification triggers (Zalo SMS, FCM push). The UI will call these endpoints to drive attendance and notification flows.  
- **Docker Multi‑Stage Build** – Produce optimized Docker images for the Quarkus backend and Next.js frontend, ready for GKE deployment.  

## 2. Allowed Technical Scope & Directory Boundaries
- **Frontend** (`./sources/frontend/`):  
  - `./sources/frontend/next-i18next.config.js` – i18n configuration.  
  - `./sources/frontend/next.config.js` – SEO & i18n routes.  
  - `./sources/frontend/pages/` – All Next.js pages (`_app.tsx`, `dashboard.tsx`, `centers.tsx`, `courses.tsx`, `teachers.tsx`, `students.tsx`, `promotions.tsx`, `notifications.tsx`, `admin/[...slug].tsx`).  
  - `./sources/frontend/components/RoleBasedGuard.tsx` – RBAC guard.  
  - `./sources/frontend/lib/api.ts` – API client for attendance & notification services.  
  - `./sources/frontend/hooks/useRealtimeDashboard.ts` – 15‑min refresh logic.  
  - `./sources/frontend/public/locales/` – translation JSON files.  
  - `./sources/frontend/tests/` – unit & integration test suites.  
- **Backend Integration** (`./sources/backend/`):  
  - `./sources/backend/src/main/java/org/nlh4j/saas/memberhub/controller/AttendanceController.java` – REST endpoints for QR scan & day‑counter.  
  - `./sources/backend/src/main/java/org/nlh4j/saas/memberhub/controller/NotificationController.java` – REST endpoints for sending notifications.  
  - `./sources/backend/src/main/java/org/nlh4j/saas/memberhub/service/AttendanceService.java` – Business logic (single‑day flag, day‑counter decrement).  
  - `./sources/backend/src/main/java/org/nlh4j/saas/memberhub/service/NotificationService.java` – Kafka publishing to `attendance`, `notifications`, `zalo-message`.  
  - `./sources/backend/src/main/java/org/nlh4j/saas/memberhub/dto/AttendanceDto.java` – Data transfer objects.  
  - `./sources/backend/src/main/java/org/nlh4j/saas/memberhub/dto/NotificationDto.java`.  
  - `./sources/backend/src/test/java/org/nlh4j/saas/memberhub/controller/AttendanceControllerTest.java` – Unit tests.  
  - `./sources/backend/src/test/java/org/nlh4j/saas/memberhub/controller/NotificationControllerTest.java`.  
- **Docker** (`./sources/backend/Dockerfile`, `./sources/frontend/Dockerfile`) – Multi‑stage images.  
- **CI/CD / GKE** (`./sources/backend/k8s/`, `./sources/frontend/k8s/`) – Deployment manifests.  

## 3. Dedicated Sub-Agent Functional Directives
- **Coder** – Implement all Next.js pages, i18n config, role‑guard component, API client, real‑time hook, and backend REST controllers/services. Embed OWASP A01 (Injection) & A03 (Sensitive Data Exposure) mitigations (parameterized queries, tenant filtering, JWT validation).  
- **Tester** – Write unit tests for `RoleBasedGuard`, `useRealtimeDashboard`, and backend controllers; write integration/E2E tests for attendance & notification flows using `INTEGRATION_SCOPE` where cross‑component verification is required.  
- **Reviewer** – Perform security review of JWT claim parsing, tenant isolation in backend APIs, and OWASP A05 (Security Misconfiguration) checks on Docker images and K8s manifests.  
- **Docker** – Craft multi‑stage Dockerfiles for Quarkus (`./sources/backend/Dockerfile`) and Next.js (`./sources/frontend/Dockerfile`), ensuring non‑root user, minimal layers, and health‑check endpoints.  
- **GCP** – Configure Cloud Build triggers that invoke the Docker builds, push images to Artifact Registry, and generate build logs.  
- **GKE** – Produce K8s deployment and service YAMLs (`./sources/backend/k8s/deployment.yaml`, `./sources/frontend/k8s/deployment.yaml`) with resource limits, pod security policies, and tenant‑aware environment variables.  
- **Manager** – Coordinate cross‑agent hand‑offs, validate that all generated paths respect `./sources/` boundaries, and ensure the Phase‑level DoD metrics are tracked.  

## 4. Phase Definition of Done (DoD)
- **UI Completion** – All admin screens (Centers, Courses, Teachers, Students, Promotions, Notifications, AI CSKH) rendered with correct RBAC guards; i18n keys present for at least two languages; hreflang tags generated.  
- **Security & Compliance** – JWT `roles`/`tenant_id` enforced; OWASP A01‑A07 checks passed (input validation, parameterized queries, encryption at rest, secure headers).  
- **Real‑Time Dashboard** – Dashboard widgets auto‑refresh every 15 minutes; API calls include tenant filtering; no in‑memory large‑dataset loops.  
- **API Integration** – Backend controllers expose `/api/attendance/scan` and `/api/notifications/send`; frontend client consumes them with proper error handling; unit test coverage ≥ 80 % for new code.  
- **Docker & Deployment** – Multi‑stage Docker images built, tagged, and pushed to GCP Artifact Registry; K8s manifests deployed to GKE with correct service accounts and IAM policies.  
- **Testing** – All unit tests passing; integration/E2E tests covering attendance scan, notification delivery, and role‑based access; test coverage ≥ 80 % for new components.  
- **CI/CD** – Cloud Build pipeline triggers on code changes, builds both Docker images, runs security scans, and deploys to GKE automatically.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Next.js Project Initialization & Docker Base Images
#### SUB-TASK 1.1: Initialize Next.js frontend with i18n and basic page scaffolding
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/next-i18next.config.js
    * **Architectural Requirements:** Configure `next-i18next` with `locales` (en, vi), `defaultLocale`, and `ns` for translation keys; embed `i18n.routing` for Next.js App Router compatibility.
* **Target Path:** ./sources/frontend/next.config.js
    * **Architectural Requirements:** Enable i18n routing (`i18n: { locales: ['en','vi'], defaultLocale: 'en', localeDetection: true }`), generate `hreflang` `<link>` tags via `asyncRewrites`, and set `experimental: { optimizeCss: true }` for performance.
* **Target Path:** ./sources/frontend/pages/_app.tsx
    * **Architectural Requirements:** Import `appWithTranslation` from `react-i18next`, wrap component with `I18nextProvider`, and include global error boundary for unauthorized access.
* **Target Path:** ./sources/frontend/pages/dashboard.tsx
    * **Architectural Requirements:** Server‑side render dashboard widgets using `getServerSideProps` with tenant‑filtered data fetch; embed `<RoleBasedGuard>` to restrict to `Admin|Manager|Teacher|Student`.
* **Target Path:** ./sources/frontend/pages/centers.tsx, ./sources/frontend/pages/courses.tsx, ./sources/frontend/pages/teachers.tsx, ./sources/frontend/pages/students.tsx, ./sources/frontend/pages/promotions.tsx, ./sources/frontend/pages/notifications.tsx
    * **Architectural Requirements:** Each page implements `getServerSideProps` with tenant isolation, uses `useTranslation` for UI strings, and includes `<RoleBasedGuard>` with appropriate allowed roles per raw requirement.
#### SUB-TASK 1.2: Create multi‑stage Dockerfiles for backend and frontend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/Dockerfile
    * **Architectural Requirements:** Multi‑stage: builder (Maven compile), runtime (distroless Java 17), expose port 8080, set non‑root user, include health‑check `curl` endpoint.
* **Target Path:** ./sources/frontend/Dockerfile
    * **Architectural Requirements:** Multi‑stage: builder (npm ci, next build), runtime (nginx serve), expose port 3000, set non‑root user, include `nginx.conf` for static assets.
#### SUB-TASK 1.3: Validate workspace path compliance and directory structure
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/
    * **Architectural Requirements:** Ensure all generated files reside strictly under `./sources/`; no files placed directly at repository root; confirm Java package token `memberhub` used for any `.java` files.

### DAY 2: Role‑Based Guard & API Integration
#### SUB-TASK 2.1: Implement RoleBasedGuard component with JWT claim validation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/components/RoleBasedGuard.tsx
    * **Architectural Requirements:** Read `jwt` from cookies, decode `roles` and `tenant_id`, compare against allowedRoles prop, redirect to `/login` if unauthorized; embed OWASP A07 (Identification & Authentication Failures) mitigation (strict JWT signature verification, token expiration check).
#### SUB-TASK 2.2: Create API client for attendance and notification services
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/lib/api.ts
    * **Architectural Requirements:** Define `fetchAttendanceScan(payload)` and `sendNotification(payload)` functions using `fetch` with tenant header `x-tenant-id`; implement retry logic and error mapping; enforce OWASP A03 (Sensitive Data Exposure) by not logging payloads.
#### SUB-TASK 2.3: Add backend REST controllers to expose attendance & notification endpoints
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/memberhub/controller/AttendanceController.java
    * **Architectural Requirements:** `@RestController @RequestMapping("/api/attendance")`, `@PostMapping("/scan"` with `@RequestBody AttendanceDto dto`, enforce `@TenantFilter` to restrict data to `dto.tenantId`, return `ResponseEntity<AttendanceDto>`, embed OWASP A01 (SQL Injection) via `@Query` parameterization.
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/memberhub/controller/NotificationController.java
    * **Architectural Requirements:** `@RestController @RequestMapping("/api/notifications")`, `@PostMapping("/send"` with `@RequestBody NotificationDto dto`, enforce tenant filtering, publish to Kafka topics `attendance`, `notifications`, `zalo-message`, embed OWASP A02 (Broken Authentication) by validating JWT `Authorization` header.
#### SUB-TASK 2.4: Write unit tests for RoleBasedGuard and API client
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/tests/roleGuard.test.tsx;./sources/frontend/tests/api.test.ts
    * **Architectural Requirements:** For RoleBasedGuard, mock JWT decode with various `roles`/`tenant_id` combos and assert navigation; for API client, mock `fetch` responses and verify correct headers and payload serialization.
#### SUB-TASK 2.5: Security review of JWT handling and tenant filtering
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/components/RoleBasedGuard.tsx, ./sources/backend/src/main/java/org/nlh4j/saas/memberhub/controller/AttendanceController.java, ./sources/backend/src/main/java/org/nlh4j/saas/memberhub/controller/NotificationController.java
    * **Architectural Requirements:** Validate JWT signature verification, token expiration, and `tenant_id` claim usage; ensure no hard‑coded credentials; confirm parameterized queries in JPA repositories; embed OWASP A05 (Security Misconfiguration) checks.

### DAY 3: Real‑Time Dashboard Refresh & Integration Tests
#### SUB-TASK 3.1: Implement useRealtimeDashboard hook for 15‑minute auto‑refresh
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/hooks/useRealtimeDashboard.ts
    * **Architectural Requirements:** `useEffect(() => { const interval = setInterval(() => { fetch('/api/dashboard')... }, 15*60*1000); return () => clearInterval(interval); }`, include tenant header, cache‑bust query param to avoid stale data.
#### SUB-TASK 3.2: Add dashboard API endpoint in backend
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/memberhub/controller/DashboardController.java
    * **Architectural Requirements:** `@RestController @RequestMapping("/api/dashboard")`, `@GetMapping` returns aggregated counts (courses today, teachers on duty, student day counters), apply tenant filter, embed OWASP A04 (Insecure Design) by limiting exposed fields.
#### SUB-TASK 3.3: Write integration test for dashboard refresh and attendance flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/dashboardRefresh.spec.ts
    * **Architectural Requirements:** Simulate user login, trigger attendance scan via API, verify dashboard widget updates within interval, assert tenant‑specific data visibility.
#### SUB-TASK 3.4: Review security of real‑time data fetching
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/hooks/useRealtimeDashboard.ts, ./sources/backend/src/main/java/org/nlh4j/saas/memberhub/controller/DashboardController.java
    * **Architectural Requirements:** Ensure no CORS misconfiguration, validate tenant header on each request, enforce rate limiting via Spring Security `HttpRateLimiter`, embed OWASP A06 (Vulnerable Components) by using latest dependency versions.

### DAY 4: Docker Image Build & CI/CD Pipeline Setup
#### SUB-TASK 4.1: Build and push Docker images to GCP Artifact Registry via Cloud Build
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/cloudbuild-backend.yaml
    * **Architectural Requirements:** Define Cloud Build step: `docker build -f ./sources/backend/Dockerfile --tag gcr.io/${PROJECT_ID}/membership-hub-backend:${SHORT_SHA} .`, `docker push`, apply `gcloud run deploy` with IAM service account.
* **Target Path:** ./sources/frontend/cloudbuild-frontend.yaml
    * **Architectural Requirements:** Similar steps for frontend image `gcr.io/${PROJECT_ID}/membership-hub-frontend:${SHORT_SHA}`.
#### SUB-TASK 4.2: Configure CI/CD triggers in repository
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** ./.github/workflows/ci-cd.yml
    * **Architectural Requirements:** Trigger on `push` to main, invoke Cloud Build for backend and frontend, wait for success, then apply K8s manifests.
#### SUB-TASK 4.3: Create K8s deployment manifests for backend and frontend
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/k8s/deployment.yaml
    * **Architectural Requirements:** `apiVersion: apps/v1`, `kind: Deployment`, container image `gcr.io/${PROJECT_ID}/membership-hub-backend:${SHORT_SHA}`, resource limits, env vars for `TENANT_ID`, `JWT_SECRET`, readiness/liveness probes.
* **Target Path:** ./sources/frontend/k8s/deployment.yaml
    * **Architectural Requirements:** Similar for Next.js, expose port 3000, mount configMap for `NEXT_PUBLIC_API_URL`, enforce pod security policy `restricted`.

### DAY 5: Security Hardening & OWASP Validation
#### SUB-TASK 5.1: Run OWASP ZAP scan against deployed services
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ZAP_SCAN_REPORT.md
    * **Architectural Requirements:** Generate scan report, remediate high‑risk findings (e.g., missing security headers, insecure cookies), update Docker images with patched base layers.
#### SUB-TASK 5.2: Apply encryption at rest for PII in PostgreSQL
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/memberhub/config/DatabaseEncryptionConfig.java
    * **Architectural Requirements:** Configure Spring Data JPA with `AES-256` column-level encryption for fields marked `@SensitiveField`, embed key management via GCP Secret Manager.
#### SUB-TASK 5.3: Validate tenant isolation across all API endpoints
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/memberhub/interceptor/TenantInterceptor.java
    * **Architectural Requirements:** Intercept all `/api/**` requests, extract `x-tenant-id` header, compare with JWT `tenant_id`, reject mismatched requests, log audit trail.

### DAY 6: End‑to‑End Testing & Performance Validation
#### SUB-TASK 6.1: Execute E2E tests for attendance scan and notification delivery
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/e2e/attendance.spec.ts
    * **Architectural Requirements:** Use Playwright to login as Student, scan QR (mock API), verify attendance flag set, check notification appears in UI and Kafka topic `attendance` is published.
#### SUB-TASK 6.2: Load test critical paths (dashboard refresh, attendance API)
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/test/java/org/nlh4j/saas/memberhub/performance/DashboardLoadTest.java
    * **Architectural Requirements:** Use JUnit 5 with `Testcontainers` PostgreSQL and Kafka, simulate 100 concurrent dashboard requests, assert response time < 200ms, ensure no memory leaks.
#### SUB-TASK 6.3: Review performance results and adjust scaling
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** PERFORMANCE_REPORT.md
    * **Architectural Requirements:** Summarize throughput, identify bottlenecks, recommend horizontal pod autoscaling rules in K8s HPA.

### DAY 7: Final Sign‑Off & Release
#### SUB-TASK 7.1: Consolidate all artifacts and generate release manifest
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** RELEASE_MANIFEST.md
    * **Architectural Requirements:** List all implemented files, Docker image digests, K8s deployment revisions, test coverage metrics, OWASP remediation status.
#### SUB-TASK 7.2: Deploy final images to GKE and verify service health
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/k8s/deployment.yaml, ./sources/frontend/k8s/deployment.yaml
    * **Architectural Requirements:** Apply `kubectl apply -f`, verify pods ready, check service endpoints, run health‑check curl against `/actuator/health`.
#### SUB-TASK 7.3: Final compliance audit
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** COMPLIANCE_AUDIT_CHECKLIST.md
    * **Architectural Requirements:** Confirm all raw requirements from Phase 3 are satisfied, OWASP A01‑A07 controls present, RBAC enforced, multi‑tenant isolation validated, i18n/SEO functional, Docker images scanned, CI/CD pipeline passes.