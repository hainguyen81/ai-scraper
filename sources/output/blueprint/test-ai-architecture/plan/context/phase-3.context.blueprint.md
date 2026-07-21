# PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
- **Deliver a production‑ready, multi‑language Next.js front‑end** that powers both the web portal and the native mobile experience (iOS/Android) for the membership‑hub application.  
- **Implement core user journeys**:  
  1. **Authentication** – internal email/password login and external OAuth providers (Firebase, Google, Facebook) with seamless token handling and session management.  
  2. **Dashboard & Member Management** – list, search, filter, and view member profiles, including remaining validity days.  
  3. **QR‑Based Attendance** – scan QR codes to record daily attendance, handle duplicate scans gracefully, and reflect status instantly.  
  4. **Notifications** – push notifications via mobile app, Zalo SMS/WhatsApp, and in‑app alerts for attendance events.  
  5. **Localization & SEO** – detect user locale (stored preference → browser → default), render appropriate language, and generate SEO‑friendly meta tags for all pages.  
- **Ensure cross‑platform consistency** between web and mobile UI, leveraging Next.js’s hybrid capabilities (e.g., `next/router`, `next/link`, `next/image`).  
- **Integrate with the Quarkus back‑end** via standardized REST/GraphQL endpoints (e.g., `/api/auth`, `/api/members`, `/api/attendance`, `/api/notifications`).  
- **Establish a testable, maintainable codebase** with clear separation of concerns, component libraries, and automated linting/formatting.  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
```
src/
├─ components/          # Reusable UI atoms, molecules, organisms
│   ├─ Auth/
│   ├─ Member/
│   ├─ Attendance/
│   └─ Notifications/
├─ pages/               # Next.js pages (web) + mobile‑specific routes
│   ├─ en/              # Language‑specific page tree
│   └─ vi/              # Example: Vietnamese locale (extend as needed)
│   ├─ index.tsx
│   ├─ login.tsx
│   ├─ dashboard.tsx
│   ├─ members/[id].tsx
│   └─ attendance.tsx
├─ api/                 # Client‑side API helpers (fetch wrappers)
│   ├─ auth.ts
│   ├─ members.ts
│   ├─ attendance.ts
│   └─ notifications.ts
├─ lib/                 # Localization, constants, utilities
│   ├─ i18n.ts
│   ├─ config.ts
│   └─ qr.ts            # QR scanning utilities (react-qr-reader)
├─ hooks/               # Custom React hooks (useAuth, useAttendance, etc.)
├─ styles/              # Global CSS, Tailwind config, theme
├─ types/               # TypeScript interfaces for all payloads
└─ utils/               # General helpers (date formatting, token handling)
package.json
next.config.js
tsconfig.json
eslint.config.js
...
```
**Allowed external endpoints (to be consumed by the front‑end):**  
- `GET /api/auth/me` – current user info (internal & external auth)  
- `POST /api/auth/login` – email/password login  
- `POST /api/auth/social/{provider}` – OAuth redirect/callback handling  
- `GET /api/members` / `GET /api/members/{id}` – member list & details  
- `POST /api/attendance/scan` – QR attendance submission (expects `{memberId, qrCode}`)  
- `GET /api/attendance/{memberId}/daily` – fetch today’s attendance status  
- `POST /api/notifications` – trigger push/Zalo notification (`{memberId, message}`)  

All API calls must be wrapped with error handling, token refresh, and loading states.

## 3. Dedicated Sub-Agent Functional Directives
| Sub‑Agent | Specific Tasks & Deliverables for Phase 3 |
|-----------|-------------------------------------------|
| **Coder** | 1. Scaffold Next.js project with TypeScript, Tailwind CSS, and i18n‑next. <br>2. Implement locale detection logic (`lib/i18n.ts`) that respects stored user preference → browser Accept‑Language → default (`en`). <br>3. Build authentication UI (login form + social buttons) and integrate with `/api/auth/*` endpoints; manage JWT/session via `next-auth` or custom cookie store. <br>4. Create reusable component library (Auth, Member Card, QR Scanner, Notification badge) using Tailwind + Headless UI. <br>5. Develop QR scanning flow using `react-qr-reader`; on success, call `/api/attendance/scan` and display immediate feedback (attendance recorded, remaining days). <br>6. Implement member dashboard with list view, search/filter, and “remaining validity days” calculation (frontend formatting). <br>7. Add push notification integration (Firebase Cloud Messaging) and Zalo API calls for SMS/WhatsApp; expose a generic `notify()` helper. <br>8. Write SEO meta components (`next/head`) per page, generating `<title>`, `<meta name="description">`, and hreflang tags for multilingual pages. <br>9. Set up CI linting (ESLint, Prettier) and commit linting rules. |
| **Tester** | 1. Design UI test suite (Playwright) covering login flows, QR scan success/failure, attendance duplicate handling, and notification delivery. <br>2. Create i18n tests to verify correct locale rendering and hreflang links. <br>3. Perform accessibility audits (axe) on all pages; fix WCAG AA violations. <br>4. Execute integration tests against mocked Quarkus endpoints (using MSW or similar) to validate API contracts. <br>5. Document test results and maintain a test‑coverage threshold (≥80% for new code). |
| **Reviewer** | 1. Conduct code‑review passes on all Coder PRs focusing on security (no hard‑coded credentials, safe redirect URIs), coding standards, and i18n best practices. <br>2. Validate SEO implementation (title, description, Open Graph, hreflang). <br>3. Approve component library usage and ensure consistent design tokens. |
| **DevOps** | 1. Prepare Docker base image for Next.js front‑end (`Dockerfile` in `frontend/`), including build‑time environment variables for API endpoints and Firebase keys. <br>2. Configure GitHub Actions workflow that builds the image, runs linting, unit tests, and deploys to GKE namespace `membership-hub-frontend` (optional for this phase – mainly artifact generation). |
| **Manager** | 1. Track progress against Phase 3 objectives, ensure daily stand‑ups capture blockers. <br>2. Validate that all functional requirements (auth, QR attendance, notifications, i18n, SEO) are met before sign‑off. |

## 4. Phase Definition of Done (DoD)
- **Functional**  
  - All authentication methods (email/password + Firebase/Google/Facebook) work end‑to‑end, with proper session persistence across page reloads.  
  - Member dashboard displays a searchable, filterable list of members with accurate “remaining validity days” calculations.  
  - QR scanning successfully records attendance via the back‑end API; duplicate scans on the same day are ignored without error.  
  - Notifications are triggered for attendance events and delivered via mobile push, Zalo SMS/WhatsApp, and in‑app alerts.  
  - Multi‑language support is functional: locale detection, UI translation, hreflang SEO tags, and correct language‑specific routes.  
  - SEO meta tags (title, description, Open Graph, Twitter Card, hreflang) are present on every page.  

- **Technical**  
  - Codebase follows project‑wide linting, formatting, and TypeScript strictness rules.  
  - Component library is reusable, documented, and tested.  
  - All API calls are wrapped with error handling, loading states, and token refresh logic.  
  - Docker image for the front‑end builds successfully and contains only production assets.  

- **Quality & Compliance**  
  - UI tests, i18n tests, accessibility audits, and integration tests pass with ≥80% coverage on new code.  
  - Security review sign‑off: no hardcoded secrets, safe OAuth redirect URIs, and proper CSP headers (via Next.js config).  
  - Documentation (README, component stories, API usage) is updated for the new front‑end modules.  

- **Delivery**  
  - All Phase 3 artifacts (source code, Docker image, test reports, documentation) are committed to the repository and ready for Phase 4 QA hand‑off.  

When **all** the above criteria are satisfied, Phase 3 is complete and the project progresses to Phase 4 (Testing & Quality Assurance).