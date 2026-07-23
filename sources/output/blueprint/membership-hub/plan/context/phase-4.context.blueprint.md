# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement a cross‑platform Next.js mobile/web front‑end that mirrors the admin UI, enforces role‑based access, supports multi‑language SEO, real‑time push notifications, QR‑based attendance scanning, and a float AI CSKH chat widget that queries backend course/teacher/center APIs. Deliver fully tested E2E UI coverage, containerized Docker images, and GKE‑ready Kubernetes manifests for production rollout.

## 2. Allowed Technical Scope & Directory Boundaries
- **Frontend source tree:** `./sources/frontend/` (Next.js 13+ app directory, TypeScript, Tailwind CSS, i18n‑next, React‑Query, WebSocket/FCM bridges, QR‑scanner library, AI SDK integration).  
- **Frontend assets:** `./sources/frontend/public/` for static assets, `./sources/frontend/src/components/`, `./sources/frontend/src/pages/`, `./sources/frontend/src/lib/`, `./sources/frontend/src/services/`, `./sources/frontend/src/hooks/`, `./sources/frontend/tests/` (E2E test suites).  
- **Backend integration points (assumed existing):** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/controller/ChatController.java` (AI chat endpoint), `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/controller/AttendanceController.java` (QR attendance), `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/controller/NotificationController.java` (push).  
- **Containerization:** `./sources/frontend/Dockerfile` (multi‑stage).  
- **CI/CD & GCP:** `./sources/ci-cd/cloudbuild.yaml`, `./sources/ci-cd/sonar-config.yml`.  
- **GKE manifests:** `./sources/k8s/frontend-deployment.yaml`, `./sources/k8s/frontend-service.yaml`, `./sources/k8s/frontend-ingress.yaml`.  
- **Ops/Orchestration:** `./sources/ops/deployment-summary.txt`.

## 3. Dedicated Sub-Agent Functional Directives
- **Coder:** Build the Next.js application, implement i18n, role guards, QR scanner, AI chat widget, notification handling, and API client integration. Enforce OWASP A01 (input validation), A03 (injection), A07 (auth) via client‑side validation, CSRF tokens, and secure API calls.  
- **Tester:** Write E2E test suites covering authentication flows, role‑based navigation, enrollment, QR scanning, AI chat queries, and push notification receipt. Use Playwright/Cypress with strict source‑test pairing.  
- **Docker:** Craft a multi‑stage Dockerfile for the Next.js frontend, optimizing for size, security (non‑root user), and GKE deployment.  
- **GCP:** Define Cloud Build pipelines (`cloudbuild.yaml`) that trigger on source changes, run tests, build Docker image, push to Artifact Registry, and invoke GKE rollout.  
- **GKE:** Produce Kubernetes Deployment, Service, and Ingress YAMLs for the frontend, including HPA, resource limits, and securityContext (non‑root).  
- **Manager:** Coordinate overall Phase‑4 delivery, validate that all artifacts exist under `./sources/`, ensure CI/CD configs are syntactically correct, and confirm that the compiled Docker image passes security scanning.

## 4. Phase Definition of Done (DoD)
- All Next.js pages and components implemented with role‑based guards, i18n, SEO meta tags, and responsive design.  
- QR scanner component functional, integrated with backend attendance endpoint.  
- Float AI chat widget connected to backend chat endpoint and displaying responses.  
- Push notification receiver (WebSocket/FCM) handling inbound messages and UI toasts.  
- Complete E2E test suite (`auth.spec.ts`, `enrollment.spec.ts`, `chat.spec.ts`, `push.spec.ts`) passing on CI.  
- Docker image built successfully (`./sources/frontend/Dockerfile`).  
- Cloud Build pipeline defined (`./sources/ci-cd/cloudbuild.yaml`) and validated.  
- GKE manifests (`frontend-deployment.yaml`, `frontend-service.yaml`, `frontend-ingress.yaml`) ready for rollout.  
- All artifacts stored under `./sources/` with correct path prefixes and Java package compliance where applicable.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Project Scaffold & Internationalization Setup
#### SUB‑TASK 1.1: Initialize Next.js app with TypeScript, Tailwind, and i18n‑next
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/next.config.js
    *   **Architectural Requirements:**
        *   Configure `i18n` with supported locales (`en`, `vi`, `zh`) and default locale detection from user profile or browser.
        *   Enable SEO `generateStaticParams` for each locale.
        *   Apply OWASP A01 input validation for locale query parameters.
*   **Target Path:** ./sources/frontend/src/lib/i18n.ts
    *   **Architectural Requirements:**
        *   Implement `NextIntlClientProvider` with `detectLocale` function that reads `user.preferredLocale` from API (JWT token) before falling back to `navigator.language`.
        *   Ensure all UI strings are extracted to JSON locale files under `./sources/frontend/public/locales/`.

#### SUB‑TASK 1.2: Create base directory structure and package.json
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/package.json
    *   **Architectural Requirements:**
        *   Define scripts: `dev`, `build`, `start`, `lint`, `test:e2e`.
        *   Include dependencies: `next`, `react`, `react-dom`, `@next/intl`, `tailwindcss`, `postcss`, `autoprefixer`, `react-query`, `socket.io-client`, `firebase`, `qrcode-react`, `@anthropic/claude` (AI SDK).
*   **Target Path:** ./sources/frontend/src/pages/_app.tsx
    *   **Architectural Requirements:**
        *   Wrap app with `NextIntlClientProvider` and `QueryClientProvider`.
        *   Implement global error boundary for OWASP A05 (security misconfiguration) handling.

#### SUB‑TASK 1.3: Draft initial Docker image for frontend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/Dockerfile
    *   **Architectural Requirements:**
        *   Use Node 20 Alpine as base.
        *   Set non‑root user (`node`).
        *   Copy `package.json` and lock, run `npm ci --only=production`.
        *   Copy source, set `NEXT_PUBLIC_API_URL` env var, expose port 3000.
        *   Add security labels (`org.opencontainers.image.created`, `org.opencontainers.image.authors`).

### DAY 2: Role‑Based UI Guards & Authentication Flow
#### SUB‑TASK 2.1: Implement RoleGuard component for route protection
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/RoleGuard.tsx
    *   **Architectural Requirements:**
        *   Read `user.roles` from JWT token (decoded client‑side) and compare against allowed roles per route.
        *   Redirect unauthenticated users to `/login` (OWASP A07).
        *   Enforce CSRF token validation for state‑changing routes via HTTP header check.

#### SUB‑TASK 2.2: Create protected route definitions
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/pages/dashboard.tsx
    *   **Architectural Requirements:**
        *   Wrap page component with `<RoleGuard allowedRoles={['ADMIN','MANAGER','TEACHER','STUDENT']} />`.
        *   Fetch user profile via `GET /api/v1/users/me` (JWT auth).
*   **Target Path:** ./sources/frontend/src/pages/courses.tsx
    *   **Architectural Requirements:**
        *   Guard with `allowedRoles:['ADMIN','MANAGER','TEACHER','STUDENT']`.
        *   Use `React‑Query` to prefetch courses list (`GET /api/v1/courses`).

#### SUB‑TASK 2.3: Write unit tests for RoleGuard logic
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/RoleGuard.tsx;./sources/frontend/tests/roleGuard.spec.ts
    *   **Architectural Requirements:**
        *   Verify role matching, redirect behavior, and unauthorized access blocking.
        *   Ensure OWASP A07 token validation is exercised.

### DAY 3: Multi‑Language UI & SEO Implementation
#### SUB‑TASK 3.1: Integrate locale switcher and persist user preference
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/LocaleSwitcher.tsx
    *   **Architectural Requirements:**
        *   Render language links that update `router.locale`.
        *   Store selected locale in user profile via `PUT /api/v1/users/preference` (JWT protected).
*   **Target Path:** ./sources/frontend/src/lib/notifications.ts
    *   **Architectural Requirements:**
        *   Subscribe to push notifications via Firebase Cloud Messaging; store token on server (`POST /api/v1/notifications/token`).

#### SUB‑TASK 3.2: Add SEO meta tags per locale
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/pages/[locale]/index.tsx
    *   **Architectural Requirements:**
        *   Use `useHead` hook to inject `<title>`, `<meta name="description">` based on locale resources.
        *   Implement Open Graph tags for shareability (OWASP A03).

#### SUB‑TASK 3.3: Write E2E tests for locale switching
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/pages/[locale]/index.tsx;./sources/frontend/tests/locale.spec.ts
    *   **Architectural Requirements:**
        *   Verify UI text updates correctly when locale changes.
        *   Confirm SEO meta tags reflect selected language.

### DAY 4: Push Notification Receiver & Display
#### SUB‑TASK 4.1: Implement WebSocket/FCM notification listener
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/lib/notifications.ts
    *   **Architectural Requirements:**
        *   Establish Socket.IO client connection to `/notifications` endpoint (JWT auth).
        *   Handle `new-notification` events and queue for UI toast display.
        *   Integrate Firebase for background push (service worker registration).
*   **Target Path:** ./sources/frontend/src/components/NotificationToast.tsx
    *   **Architectural Requirements:**
        *   Render toast notifications with auto‑dismiss.
        *   Apply OWASP A01 validation on notification payload fields.

#### SUB‑TASK 4.2: Add notification badge to navigation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/NavBar.tsx
    *   **Architectural Requirements:**
        *   Display unread notification count badge.
        *   Mark notifications as read via `PATCH /api/v1/notifications/{id}/read`.

#### SUB‑TASK 4.3: Write E2E test for push receipt
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/push.spec.ts
    *   **Architectural Requirements:**
        *   Simulate incoming notification via mock Socket.IO event.
        *   Verify toast appears and UI updates accordingly.

### DAY 5: QR Scanner Component for Attendance
#### SUB‑TASK 5.1: Integrate QR scanner library and capture scans
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/QRScanner.tsx
    *   **Architectural Requirements:**
        *   Use `html5-qrcode` library to scan student ID from camera.
        *   Emit `scan` event with scanned payload (`studentId`, `timestamp`).
        *   Validate payload format (UUID + ISO date) (OWASP A01).
*   **Target Path:** ./sources/frontend/src/pages/attendance.tsx
    *   **Architectural Requirements:**
        *   Include `<QRScanner>` component.
        *   Call `POST /api/v1/attendance/scan` with scanned data (idempotent handling).

#### SUB‑TASK 5.2: Write E2E test for QR scanning flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/QRScanner.tsx;./sources/frontend/tests/qrScanner.spec.ts
    *   **Architectural Requirements:**
        *   Mock camera input and verify scan result propagation.
        *   Assert attendance API call with correct payload.

### DAY 6: Float AI Chat Widget Integration
#### SUB‑TASK 6.1: Build AI chat widget UI and state management
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/AIChartWidget.tsx
    *   **Architectural Requirements:**
        *   Render floating button, chat window, message list.
        *   Use `React‑Query` to invoke `GET /api/v1/chat` with user query.
        *   Stream AI response via Server‑Sent Events or WebSocket.
        *   Apply OWASP A03 input validation on user messages (sanitize for injection).
*   **Target Path:** ./sources/frontend/src/services/api.ts
    *   **Architectural Requirements:**
        *   Centralized API client with interceptors for JWT token and CSRF headers.
        *   Methods: `chat(query: string)`, `getCourses()`, `getTeachers()`, `getCenters()`.

#### SUB‑TASK 6.2: Connect widget to backend chat endpoint
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/controller/ChatController.java
    *   **Architectural Requirements:**
        *   Expose `GET /api/v1/chat` returning AI response.
        *   Implement tenant isolation via `tenant_id` header (OWASP A01).
        *   Use AES‑256‑GCM for any PII in request/response.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/ChatService.java
    *   **Architectural Requirements:**
        *   Integrate AI SDK (OpenAI/Anthropic) for query processing.
        *   Log audit trail for chat interactions (OWASP A09).

#### SUB‑TASK 6.3: Write E2E test for AI chat interaction
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/AIChartWidget.tsx;./sources/frontend/tests/chat.spec.ts
    *   **Architectural Requirements:**
        *   Simulate user typing a course query, verify response display.
        *   Validate that request includes authentication token.

### DAY 7: CI/CD Pipeline, GKE Manifests & Final Verification
#### SUB‑TASK 7.1: Define Cloud Build pipeline
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/ci-cd/cloudbuild.yaml
    *   **Architectural Requirements:**
        *   Trigger on `main` branch push.
        *   Steps: `npm ci`, `npm run lint`, `npm run test:e2e`, `npm run build`, `docker build -t ...`, `docker push`.
        *   Include `gcloud deploy` step referencing GKE cluster.

#### SUB‑TASK 7.2: Create GKE deployment manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/k8s/frontend-deployment.yaml
    *   **Architectural Requirements:**
        *   Deployment with image `gcr.io/<project>/membership-hub-frontend`.
        *   Resource requests/limits, HPA based on CPU/metrics.
        *   SecurityContext `runAsNonRoot: true`, `readOnlyRootFilesystem`.
*   **Target Path:** ./sources/k8s/frontend-service.yaml
    *   **Architectural Requirements:**
        *   NodePort service exposing port 3000.
        *   Add `tenant_id` label for multi‑tenant routing.
*   **Target Path:** ./sources/k8s/frontend-ingress.yaml
    *   **Architectural Requirements:**
        *   Ingress with TLS, host `membership-hub.example.com`.
        *   Path-based routing to service.

#### SUB‑TASK 7.3: Final orchestration summary and validation
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/ops/deployment-summary.txt
    *   **Architectural Requirements:**
        *   List all generated artifacts (frontend source, Docker image, CI pipeline, K8s manifests).
        *   Confirm OWASP compliance checklist items (input validation, encryption, auth, audit logging).
        *   Verify all paths start with `./sources/` and Java package compliance (`org/nlh4j/saas/membershiphub/...`).