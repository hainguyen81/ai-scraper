# PHASE 3 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement the complete front‑end and mobile user interfaces for the membership‑hub system. This includes:
- Building a Next.js web application with multi‑language support (i18n), role‑based navigation, and SEO‑optimized meta tags per locale.
- Developing a Capacitor‑based mobile app (iOS/Android) that mirrors the web UI, supports push notifications, and shares the same i18n and AI CSKH chat widget.
- Embedding an AI‑powered chat widget for instant assistance across all roles.
- Implementing Server‑Sent Events (SSE) for real‑time dashboard updates (15‑minute intervals) and handling Zalo group & FCM push notifications.
- Enforcing OWASP A01‑A07 controls (XSS mitigation via CSP, input sanitization, secure headers, tenant‑aware routing) and ensuring all UI components respect role‑based access (System Admin, Admin, Manager, Teacher, Student).
- Packaging both front‑ends into Docker images and preparing Kubernetes manifests for deployment on GCP GKE.

## 2. Allowed Technical Scope & Directory Boundaries
All artifacts must reside under `./sources/` with the following strict layout:

```
./sources/frontend/web/
├── src/
│   ├── pages/               # Next.js pages (or app/)
│   ├── components/          # Reusable UI components (Layout, AIWidget, etc.)
│   ├── lib/                 # i18n, SSE, SEO, push utilities
│   └── i18n/                # Locale resources
├── public/
├── next.config.js
├── tsconfig.json
└── Dockerfile

./sources/frontend/mobile/
├── src/
│   ├── app/                # React Native / Next.js mobile entry
│   ├── components/
│   └── lib/
├── capacitor.config.json
├── tsconfig.json
└── Dockerfile

./sources/backend/k8s/
├── frontend-deployment.yaml
└── frontend-service.yaml
```

No files may be generated outside `./sources/`. Java source files are not part of this phase, so the Java package rule does not apply.

## 3. Dedicated Sub-Agent Functional Directives
- **Coder**: Implement all source code, configuration, and container definitions for web and mobile front‑ends. Inject OWASP security controls (CSP headers, input sanitization, tenant‑aware routing) into component designs.
- **Tester**: Create unit and integration test suites that validate i18n, role‑based UI rendering, AI widget interactions, SSE connectivity, and push notification flows. Use the strict `<source>;<test>` syntax for unit tests and `INTEGRATION_SCOPE;<test>` for cross‑component E2E tests.
- **Reviewer**: Perform security and code reviews on all front‑end components, ensuring OWASP compliance, proper tenant isolation in routing, and secure handling of user‑provided data.
- **Docker**: Produce optimized multi‑stage Dockerfiles for the web and mobile builds, ensuring minimal image size and inclusion of necessary runtime dependencies.
- **GCP / GKE**: Generate Kubernetes deployment and service manifests that define the front‑end services, include required environment variables (e.g., `TENANT_ID`, `NOTIFICATION_ENDPOINTS`), and enforce resource limits.
- **Manager**: Coordinate the overall integration, verify that all sub‑agent outputs are correctly wired, and run a final smoke test to confirm end‑to‑end functionality before phase hand‑off.

## 4. Phase Definition of Done (DoD)
- All web and mobile UI screens (Center, Course, Teacher, Student, Promotions, Announcements, Dashboard) are implemented with role‑based visibility.
- i18n is fully functional: locale detection (user preference → browser → default), per‑language SEO meta tags, and translated UI strings.
- AI CSKH chat widget is integrated, functional, and accessible to all roles.
- SSE service provides real‑time dashboard updates at the configured interval; push notifications for Zalo groups and FCM are wired.
- OWASP A01‑A07 controls are embedded (CSP, XSS protection, secure headers, tenant‑aware routing, input validation).
- Comprehensive unit test coverage for i18n, components, SSE, and AI widget; integration/E2E tests verify end‑to‑end user flows.
- Docker images for web and mobile are built and pass security scanning.
- Kubernetes manifests are ready for deployment on GCP GKE with proper tenant isolation and resource definitions.
- Final smoke test passes, confirming all Phase 3 requirements are satisfied.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Foundational Front‑End Scaffolding & i18n Setup
#### SUB-TASK 1.1: Create Next.js web app skeleton and i18n infrastructure
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/web/src/pages/_app.tsx
    *   **Architectural Requirements:**
        *   Initialize Next.js app with `NextIntlProvider` for i18n, import global CSS, and embed a `<Layout>` component that enforces role‑based routing.
        *   Implement OWASP‑compliant meta tags via `<Head>` (Content‑Security‑Policy, X‑Frame‑Options) and sanitize any user‑provided locale query parameters.
*   **Target Path:** ./sources/frontend/web/src/pages/_document.tsx
    *   **Architectural Requirements:**
        *   Override `Document.getInitialProps` to inject tenant‑aware `tenant_id` into HTML attributes for logging and security auditing.
*   **Target Path:** ./sources/frontend/web/src/lib/i18n.ts
    *   **Architectural Requirements:**
        *   Configure `next-i18next` with resources for `en`, `vi`, etc., and implement locale detection middleware (user pref → browser → default) as per requirements.
        *   Apply input validation on locale strings to prevent injection.
*   **Target Path:** ./sources/frontend/web/src/middleware.ts
    *   **Architectural Requirements:**
        *   Detect request locale, set `x-tenant-id` header based on authenticated user’s tenant, and enforce CSP via `next-headers`.
#### SUB-TASK 1.2: Write unit tests for i18n detection and middleware
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/web/src/lib/i18n.ts;./sources/frontend/web/src/lib/i18n.test.ts
    *   **Architectural Requirements:**
        *   Verify locale resolution logic matches the priority order (user pref → browser → default).
        *   Ensure tenant isolation by checking that `tenant_id` is correctly propagated in request headers.
*   **Target Path:** ./sources/frontend/web/src/middleware.ts;./sources/frontend/web/src/middleware.test.ts
    *   **Architectural Requirements:**
        *   Test CSP header injection and locale header setting for various incoming request scenarios.
#### SUB-TASK 1.3: Build Docker image for the web front‑end
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/web/Dockerfile
    *   **Architectural Requirements:**
        *   Use Node‑20 Alpine base, install dependencies via `--prefer-offline`, run `next build`, and set production `NODE_ENV`.
        *   Include security best‑practice: non‑root user, minimal layers, and explicit `CVP` (Content Security Policy) headers in `nginx` config if used.

### DAY 2: Role‑Based UI Components, AI Chat Widget, SSE & SEO
#### SUB-TASK 2.1: Implement core layout and role‑based navigation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/web/src/components/Layout.tsx
    *   **Architectural Requirements:**
        *   Render navigation links filtered by `user.role` (System Admin, Admin, Manager, Teacher, Student) per requirement matrix.
        *   Enforce OWASP A03 (Injection) by sanitizing all navigation parameters and A05 (Broken Access Control) via role checks.
        *   Include `<MetaTags>` component for page‑specific SEO.
#### SUB-TASK 2.2: Develop AI CSKH chat widget component
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/web/src/components/AIWidget.tsx
    *   **Architectural Requirements:**
        *   Integrate with AI service endpoint, provide real‑time message handling, and enforce input sanitization to prevent XSS (OWASP A01).
        *   Implement responsive design and accessibility attributes.
#### SUB-TASK 2.3: Create SSE service for dashboard real‑time updates
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/web/src/lib/sse.ts
    *   **Architectural Requirements:**
        *   Establish EventSource connection to `/api/dashboard/stream`, handle reconnection logic, and parse JSON events.
        *   Apply tenant‑aware headers (`x-tenant-id`) for security.
*   **Target Path:** ./sources/frontend/web/src/lib/seo.ts
    *   **Architectural Requirements:**
        *   Generate `<title>` and meta description per locale using `next-seo` or equivalent.
        *   Ensure no duplicate meta tags and validate Open Graph tags for each language.
#### SUB-TASK 2.4: Security review of front‑end components
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/web/src/components/Layout.tsx
    *   **Architectural Requirements:**
        *   Verify role‑based access control logic, confirm tenant isolation, and validate CSP header injection.
*   **Target Path:** ./sources/frontend/web/src/components/AIWidget.tsx
    *   **Architectural Requirements:**
        *   Confirm input sanitization, output encoding, and rate‑limiting of AI requests to mitigate abuse.
#### SUB-TASK 2.5: Unit tests for AI widget and SSE
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/web/src/components/AIWidget.tsx;./sources/frontend/web/src/components/AIWidget.test.tsx
    *   **Architectural Requirements:**
        *   Simulate user messages, verify response parsing, and ensure sanitized output.
*   **Target Path:** ./sources/frontend/web/src/lib/sse.ts;./sources/frontend/web/src/lib/sse.test.ts
    *   **Architectural Requirements:**
        *   Mock EventSource, test reconnection flows, and confirm tenant header inclusion.

### DAY 3: Mobile App Build, Push Notifications, and Deployment Manifests
#### SUB-TASK 3.1: Scaffold Capacitor mobile app with mirrored UI
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/app/_layout.tsx
    *   **Architectural Requirements:**
        *   Set up React Native / Next.js mobile entry, wrap with `RoleProvider`, and implement responsive layout for iOS/Android.
        *   Enforce OWASP A05 by validating deep‑link parameters used for navigation.
*   **Target Path:** ./sources/frontend/mobile/src/components/AIWidget.tsx
    *   **Architectural Requirements:**
        *   Port web AI widget with mobile‑optimized styling, integrate with native push notification bridge.
*   **Target Path:** ./sources/frontend/mobile/src/lib/push.ts
    *   **Architectural Requirements:**
        *   Register FCM token, handle incoming push notifications, and forward them to Zalo group messaging via backend API.
#### SUB-TASK 3.2: Build Docker image for mobile front‑end
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/Dockerfile
    *   **Architectural Requirements:**
        *   Use Node‑20 Alpine, install Capacitor CLI, build the mobile bundle, and include `capacitord` runtime for native plugins.
        *   Apply non‑root user and minimal layers for security.
#### SUB-TASK 3.3: Generate Kubernetes manifests for front‑end services
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/k8s/frontend-deployment.yaml
    *   **Architectural Requirements:**
        *   Define Deployment with container image referencing the built web Docker image.
        *   Include environment variables: `TENANT_ID`, `NOTIFICATION_WEBHOOK`, `SSE_ENDPOINT`, `AI_SERVICE_URL`.
        *   Apply resource limits, liveness/readiness probes, and securityContext (runAsNonRoot).
*   **Target Path:** ./sources/backend/k8s/frontend-service.yaml
    *   **Architectural Requirements:**
        *   Expose service on port 80, label with app=membership-hub-frontend, and attach appropriate Ingress rules for multi‑tenant routing.
#### SUB-TASK 3.4: Execute final integration smoke test
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/web/tests/smoke.spec.ts
    *   **Architectural Requirements:**
        *   Navigate through each role‑protected page, verify i18n locale switching, confirm AI widget renders, and assert SSE connection establishment.
        *   Validate push notification registration on mobile (if mobile test environment available).
        *   Capture any OWASP violations via automated security scanner integration.