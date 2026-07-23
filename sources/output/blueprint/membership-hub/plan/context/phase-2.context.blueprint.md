# PHASE 2 CONTEXT BLUEPRINT: membership-hub

## 1 . Phase Operational Scope & Objectives
Implement the frontend service layer using Next.js and React, delivering a multi‑tenant, responsive web UI with i18n support, role‑based access, and real‑time data binding. Build reusable component libraries, API client wrappers, and integrate security controls (OWASP XSS/CSRF mitigation, secure headers). Establish a comprehensive unit‑test suite covering components, services, and utilities to achieve >90 % coverage.

## 2 . Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- `./sources/frontend/src/pages/` – Next.js page components (`index.tsx`, `login.tsx`, `dashboard.tsx`, etc.)
- `./sources/frontend/src/components/` – Reusable UI components (`Layout.tsx`, `StudentCard.tsx`, etc.)
- `./sources/frontend/src/services/` – API client wrappers (`authService.ts`, `studentService.ts`, etc.)
- `./sources/frontend/src/lib/` – i18n configuration (`i18n.ts`), security utilities (`security.ts`)
- `./sources/frontend/public/` – static assets
- `./sources/frontend/tests/` – unit test files (`*.test.tsx`)
- `./sources/frontend/next.config.js` – Next.js configuration with i18n and security headers
- `./sources/frontend/package.json` – dependency definitions and scripts

## 3 . Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester)
- **Coder Agent**: Construct all Next.js pages, components, services, and i18n setup. Apply OWASP best‑practices: input sanitization (`DOMPurify`), CSRF tokens, Content‑Security‑Policy headers, and tenant isolation via `x‑tenant‑id`. Ensure deterministic file placement under `./sources/frontend/`.
- **Tester Agent**: Develop unit tests for each source file, pairing source and test files using the required `<source>;<test>` syntax. Validate rendering, user interactions, API calls, and security controls. Achieve >90 % coverage and include integration stubs where needed.

## 4 . Phase Definition of Done (DoD)
- All required Next.js pages and components implemented, functional, and responsive across roles.
- i18n configured for `en` and `vi` with locale detection and fallback.
- OWASP security controls applied (input sanitization, CSRF, secure headers, tenant isolation).
- Unit test suite created with >90 % coverage; all tests passing.
- All files placed under `./sources/` respecting `./sources/frontend/` prefix; no compilation errors in development mode.

## 5 . DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: IMPLEMENT CORE FRONTEND PAGES AND COMPONENTS
#### SUB‑TASK 1.1: Create Next.js app structure and i18n configuration
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/pages/_app.tsx
    *   **Architectural Requirements:**
        *   Wrap the app with `NextIntlProvider` for i18n and global error boundaries.
        *   Inject OWASP Content‑Security‑Policy (`defaultSrc: 'self'`, `scriptSrc: ['self', 'unsafe-inline']` for dev) and security headers via `next.config.js`.
        *   Provide CSRF token context for forms.
*   **Target Path:** ./sources/frontend/pages/index.tsx
    *   **Architectural Requirements:**
        *   Implement homepage with language selector linking to `/en` and `/vi`.
        *   Sanitize any user‑provided content using `DOMPurify`.
*   **Target Path:** ./sources/frontend/pages/login.tsx
    *   **Architectural Requirements:**
        *   Build login form with email/password fields; integrate with `authService`.
        *   Enforce OWASP A07 (Authentication) – password complexity and rate‑limiting handling on API side.
*   **Target Path:** ./sources/frontend/pages/dashboard.tsx
    *   **Architectural Requirements:**
        *   Role‑based rendering based on auth context (Admin, Manager, Teacher, Student).
        *   Validate query parameters using `Yup` schema.
*   **Target Path:** ./sources/frontend/next.config.js
    *   **Architectural Requirements:**
        *   Configure i18n (`locales: ['en','vi']`, `defaultLocale: 'en'`, `localeDetection: true`).
        *   Add security headers: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, CSP as defined.
*   **Target Path:** ./sources/frontend/src/components/Layout.tsx
    *   **Architectural Requirements:**
        *   Responsive navigation with role‑specific menu items.
        *   Include CSRF token in forms via context.
        *   Use `react-helmet` for meta tags per OWASP guidelines.
*   **Target Path:** ./sources