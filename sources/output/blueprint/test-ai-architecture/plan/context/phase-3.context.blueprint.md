# PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
| # | Objective | Description |
|---|-----------|-------------|
| **3.1** | **Create a multi‑lingual, SEO‑ready Next.js front‑end** | Build a unified front‑end that serves both the web portal and the mobile app (iOS/Android) using a single Next.js codebase. Implement server‑side rendering (SSR) and static generation (SSG) with proper meta‑tags, sitemaps, and Open Graph for SEO in all supported languages. |
| **3.2** | **Integrate authentication flows** | • Internal email/password sign‑in / sign‑up (secure password hashing, email verification).<br>• External OAuth providers: Firebase Auth, Google, Facebook.<br>• Centralized auth state management (e.g., React Context / Zustand) with protected routes. |
| **3.3** | **Implement i18n & locale detection** | • Detect user locale: stored preference → browser Accept‑Language → fallback to `en`.<br>• Use Next.js built‑in i18n (`next-i18next` or `i18next`) with namespace‑based resource loading.<br>• Provide language switcher UI and SEO hreflang tags. |
| **3.4** | **Expose attendance & student APIs** | Consume Quarkus REST endpoints (`/api/students/*`, `/api/attendance/*`, `/api/notifications/*`) via a centralized API client. Implement QR‑scan UI that calls the attendance endpoint and displays remaining validity days. |
| **3.5** | **Add real‑time notifications & messaging** | • Push notifications to mobile devices (Firebase Cloud Messaging).<br>• Send Zalo messages to the student’s phone number and to the associated Zalo group.<br>• UI toast / in‑app alerts for immediate feedback. |
| **3.6** | **Deliver CI/CD artifacts for GKE** | Generate Docker image (`frontend:latest`) with all static assets, server‑side bundles, and i18n files. Produce a `Dockerfile` and `docker-compose.yml` (if needed) ready for the DevOps pipeline. |
| **3.7** | **Establish quality gates** | Write unit, integration, and E2E tests covering component rendering, i18n switching, auth flows, API mocking, and SEO meta‑generation. Ensure test coverage ≥ 80 % and linting/formatting compliance. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)

```
frontend/
├─ src/
│  ├─ __types/
│  ├─ components/          # Reusable UI atoms, molecules, organisms
│  ├─ pages/                # Next.js pages (e.g., /login, /students, /attendance)
│  ├─ api/                  # API client wrappers (axios/interceptors)
│  ├─ services/             # Business logic (auth, attendance, notifications)
│  ├─ hooks/                # Custom React hooks (useAuth, useQRScanner, etc.)
│  ├─ utils/                # i18n helpers, date formatting, QR generation
│  ├─ stores/               # Zustand / Recoil global state (auth, ui)
│  ├─ i18n/                 # Localization resources (en/, vi/, etc.)
│  ├─ styles/               # Global CSS, Tailwind config
│  └─ tests/                # Jest / React Testing Library unit & integration tests
├─ public/
│  ├─ manifests/            # Web App Manifest for PWA
│  └─ icons/                # Favicons, splash screens for mobile
├─ .next/                   # Next.js build output (ignored in repo)
├─ next.config.js
├─ package.json
├─ Dockerfile               # Builds image for GKE
└─ docker-compose.yml       # Optional local dev orchestration
```

**Key API Endpoints (Quarkus side – assumed)**
- `GET /api/students/{id}` – retrieve student profile
- `POST /api/attendance/scan` – QR attendance submission (body: `{studentId, timestamp}`)
- `GET /api/students/{id}/validity` – returns remaining validity days
- `POST /api/notifications/push` – send FCM notification
- `POST /api/notifications/zalo` – send Zalo message (body: `{phone, groupId, message}`)

All frontend calls must be prefixed with the base path `/api/` (Next.js rewrites or environment variable `NEXT_PUBLIC_API_URL`).

## 3. Dedicated Sub-Agent Functional Directives

### 3.1 Coder (Frontend Development)
- **Task C1.1** – Scaffold Next.js project with TypeScript, Tailwind CSS, and `next-i18next`.
- **Task C1.2** – Implement locale detection middleware (`i18nMiddleware`) that reads cookie `locale` → `Accept-Language` → default `en`.
- **Task C1.3** – Build authentication module:
  - Internal sign‑up / sign‑in forms with validation (Zod).
  - OAuth buttons linking to Firebase, Google, Facebook (use `react-firebase-ui` / `next-auth` patterns).
  - Protected route guard (`_app.tsx`) that redirects unauthenticated users.
- **Task C1.4** – Create reusable UI components: `LanguageSwitcher`, `ProtectedRoute`, `QRScanner` (using `html5-qrcode`), `ValidityBadge`, `NotificationToast`.
- **Task C1.5** – Develop `pages/`:
  - `/login` – auth entry point.
  - `/students` – list of students (admin view).
  - `/students/[id]` – student detail with validity badge.
  - `/attendance` – QR scanner UI that POSTs to `/api/attendance/scan` and shows success/feedback.
  - `/notifications` – view sent Zalo/FCM messages.
- **Task C1.6** – Write API client (`api/client.ts`) with interceptors for auth token handling and error mapping.
- **Task C1.7** – Integrate attendance flow:
  - Call `/api/attendance/scan` on successful QR read.
  - Call `/api/students/{id}/validity` to refresh badge.
  - Display real‑time feedback (toast) and update UI state.
- **Task C1.8** – Implement notification dispatch:
  - UI form to select Zalo group/phone and message.
  - Trigger `POST /api/notifications/zalo` and `POST /api/notifications/push`.
  - Show confirmation and error states.
- **Task C1.9** – Configure `next.config.js` for i18n (locales, defaultLocale, localeDetection) and SEO (`generateRobotsTxt`, `generateSitemap`).
- **Task C1.10** – Create `Dockerfile` and `docker-compose.yml` for containerizing the Next.js app (multi‑stage build, copy `package.json`, `next build`, serve with `nginx` or `node`).

### 3.2 Tester (Quality Assurance)
- **Task T1.1** – Write unit tests for utility functions (`localeDetector`, `dateFormatter`) using Jest + ts‑jest.
- **Task T1.2** – Create component unit tests (React Testing Library) for `LanguageSwitcher`, `ProtectedRoute`, `QRScanner`, `ValidityBadge`.
- **Task T1.3** – Mock API endpoints (`msw`) and test integration flows:
  - Login with internal credentials.
  - OAuth redirect simulation.
  - QR scan → attendance POST → validity GET.
  - Notification send → Zalo/FCM mock responses.
- **Task T1.4** – Develop E2E tests (Cypress) covering:
  - Multi‑language navigation (EN → VI).
  - Protected route redirection.
  - End‑to‑end attendance scanning scenario.
  - Notification sending workflow.
- **Task T1.5** – Run accessibility audits (axe) and SEO checks (crawler simulation) for each locale.
- **Task T1.6** – Generate test coverage report; ensure ≥ 80 % coverage before hand‑off.
- **Task T1.7** – Document test results and any known issues in a shared test report.

### 3.3 Reviewer (Code Review & Standards)
- **Task R1.1** – Perform static code analysis (ESLint, Prettier, SonarQube) on all committed files.
- **Task R1.2** – Review pull requests for:
  - Adherence to naming conventions (`kebab-case` for files, `camelCase` for vars).
  - Security best practices (no hard‑coded credentials, proper CORS handling).
  - i18n usage (no English literals in component files).
  - Component composition (DRY, reusable atoms).
- **Task R1.3** – Validate Docker images for size and vulnerability scanning (Trivy).
- **Task R1.4** – Approve final build artifacts and sign‑off for DevOps hand‑off.

### 3.4 DevOps (CI/CD & Deployment Prep)
- **Task D1.1** – Define GitHub Actions workflow:
  - Lint → Test → Build → Docker Build → Push to GCR.
- **Task D1.2** – Create `k8s/` manifests (Deployment, Service, Ingress) referencing the built image.
- **Task D1.3** – Set up monitoring hooks (Prometheus/Grafana) for frontend metrics (response time, error rate) and logging (ELK stack).
- **Task D1.4** – Prepare secret management (GCP Secret Manager) for OAuth credentials and Firebase keys.
- **Task D1.5** – Verify that the Docker image runs correctly in a local GKE cluster (kind) before final sign‑off.

### 3.5 Manager (Phase Oversight)
- **Task M1.1** – Track progress against the 7‑day window (Days 8‑14) and raise blockers.
- **Task M1.2** – Ensure all sub‑agent deliverables are logged in the phase‑specific artifact repository.
- **Task M1.3** – Approve transition criteria before Phase 4 kickoff.

## 4. Phase Definition of Done (DoD)

- **Functional Deliverables**
  - Fully functional Next.js front‑end serving web and mobile UI.
  - Multi‑language support with locale detection, language switcher, and hreflang SEO tags.
  - Internal & external authentication flows integrated and protected routes enforced.
  - QR‑scan attendance module that calls the Quarkus attendance endpoint and displays remaining validity days.
  - Notification module capable of sending Zalo messages and FCM push notifications.
  - All API integrations (students, attendance, notifications) mocked/functional in development.

- **Technical Artifacts**
  - `frontend/` repository with all source code, i18n resources, component library, and tests.
  - `Dockerfile` and `docker-compose.yml` ready for GKE deployment.
  - `k8s/` manifests (Deployment, Service, Ingress) generated.
  - CI/CD pipeline (GitHub Actions) defined, tested, and able to build/push Docker image to GCR.
  - Monitoring & logging configuration (Prometheus, Grafana, ELK) linked to the frontend.

- **Quality Gates**
  - Unit test coverage ≥ 80 % (Jest) and E2E test suite passing.
  - Accessibility (WCAG 2.1 AA) and SEO audits completed for each locale.
  - Code review checklist fully satisfied; no security findings.
  - Docker image scanned – no critical vulnerabilities.
  - All sub‑agent tasks documented and signed off.

- **Phase Closure**
  - All deliverables merged into the main branch, tagged with `v0.3.0-frontend`.
  - Phase‑3 retrospective completed; lessons captured for Phase 4.
  - Ready for hand‑off to **Phase 4: Testing and Quality Assurance**.

*End of Phase 3 Blueprint.*