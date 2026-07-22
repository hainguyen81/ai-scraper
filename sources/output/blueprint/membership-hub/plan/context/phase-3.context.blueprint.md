# PHASE 3 CONTEXT BLUEPRINT: membership-hub
## 1. Phase Operational Scope & Objectives
- **Goal:** Deliver a fully functional, responsive web and mobile front‑end for the membership‑hub platform using **Next.js** (React‑based) with **multi‑language i18n**, role‑based UI, and deep integration to the Java/Quarkus back‑end.
- **Key Deliverables**
  * UI components for **all management screens** (Center, Course, Teacher, Student, Promotions, Announcements, Dashboard) respecting the five role hierarchy (System Admin, Admin, Manager, Teacher, Student).  
  * **Authentication** support for email/password, Firebase, Google, and Facebook with automatic role‑based routing.  
  * **QR‑code attendance** scanning, real‑time attendance API calls, and visual “days‑remaining” badge for each student.  
  * **Push notifications** to the mobile app (Zalo groups & in‑app) triggered by admin/manager actions.  
  * **Responsive design** and **PWA** capabilities for iOS/Android (manifest, service worker).  
  * **SEO‑friendly multi‑language pages** (meta tags, sitemap, hreflang).  
  * **Automated testing** (unit, integration, e2e) and **code review** compliance.  
  * **Dockerized front‑end asset** ready for GKE deployment.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
```
frontend/
├─ src/
│  ├─ components/          ← Reusable UI atoms/molecules
│  ├─ pages/               ← Next.js pages (public facing & protected)
│  ├─ layouts/             ← App, Auth, Dashboard layouts
│  ├─ services/            ← API client (axios/fetch) & auth helpers
│  ├─ hooks/               ← Custom React hooks (useAuth, useQR, useNotifications)
│  ├─ utils/               ← Date formatting, QR generation, role helpers
│  ├─ i18n/                ← i18next config, resources (en, vi, …)
│  ├─ store/               ← Redux‑Toolkit or Zustand for global state
│  └─ types/               ← TypeScript interfaces for all API payloads
├─ public/
│  ├─ manifests/           ← Web app manifest & service worker
│  └─ icons/               ← SVG icons for PWA
├─ .next/                  ← Next build output (ignored by git)
├─ package.json / yarn.lock
└─ Dockerfile              ← Build stage for GKE
```
**Back‑end API endpoints (to be consumed):**
- `POST /auth/login` (email/password)  
- `POST /auth/social/{provider}` (google, facebook, firebase)  
- `GET /api/centers` – list centers (System Admin only)  
- `GET /api/courses` – list courses with teacher assignments  
- `POST /api/attendance/qr` – record attendance (QR payload)  
- `GET /api/students/{id}/card` – fetch remaining days badge  
- `POST /api/notifications` – trigger push to Zalo group & app  
- `GET /api/users/me` – current user profile with roles  

All API calls must include the **JWT access token** stored in http‑only cookies (or secure localStorage with refresh token rotation).

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
| Sub‑Agent | Core Responsibilities for Phase 3 |
|-----------|-----------------------------------|
| **Coder** | • Scaffold Next.js project with TypeScript, Tailwind CSS, and i18n. <br>• Build protected route logic, role‑based guards, and authentication flows. <br>• Implement UI components for every management screen, QR scanner, real‑time dashboard widgets, and notification center. <br>• Integrate all required back‑end APIs, handle error/state management, and write clean, documented code. |
| **Tester** | • Write unit tests (Jest/React Testing Library) for components, hooks, and utility functions. <br>• Create integration tests for API interactions ( MSW or Jest‑mocked fetch ). <br>• Perform end‑to‑end testing with Cypress covering user journeys (login, QR scan, notification trigger). <br>• Validate multi‑language rendering and responsive breakpoints. |
| **Reviewer** | • Conduct peer code reviews focusing on coding standards, security best‑practices (XSS, CSRF), accessibility (WCAG), and i18n correctness. <br>• Ensure all components have proper TypeScript typings and docstrings. <br>• Approve changes before they are merged into the main branch. |
| **DevOps** | • Create a minimal **Dockerfile** for the front‑end (e.g., using `nginx` or `node` multi‑stage). <br>• Add a CI step (GitHub Actions) that runs `npm run build`, `npm run lint`, and `npm run test`. <br>• Push the built artifact to the GKE container registry for Phase 5 deployment. |

## 4. Phase Definition of Done (DoD)
- All **protected routes** enforce role‑based access; unauthorized users are redirected appropriately.  
- **Every UI screen** listed in the raw requirements is present, functional, and visually consistent across web and mobile viewports.  
- **Multi‑language support** works end‑to‑end: locale detection, UI text switching, and SEO meta tags (hreflang).  
- **QR attendance** can be scanned, API call succeeds, and the student’s “days remaining” badge updates instantly.  
- **Push notifications** are triggered from admin/manager actions and appear in the mobile app and Zalo groups.  
- **Real‑time dashboard** refreshes every 15 seconds (configurable via env) without manual refresh.  
- **All tests pass** (unit, integration, e2e) and code coverage meets the project’s baseline (≥80 %).  
- **Code review checklist** is satisfied for every file changed.  
- **Docker image** builds cleanly and contains only production assets; CI pipeline runs successfully.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Project Scaffold & Internationalization Foundation
#### SUB‑TASK 1.1: Initialize Next.js monorepo with TypeScript, Tailwind, and i18n
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/package.json`  
    *   **Architectural Requirements:**  
        *   Add scripts: `dev`, `build`, `start`, `lint`, `test`.  
        *   Include dependencies: `next`, `react`, `react-dom`, `@types/node`, `typescript`, `tailwindcss`, `i18next`, `react-i18next`, `next-i18next`.  
*   **Target Path 2:** `frontend/next.config.js`  
    *   **Architectural Requirements:**  
        *   Configure `i18n` with supported locales (`en`, `vi`).  
        *   Set `localeDetection` to `true` (fallback to browser Accept‑Language).  
        *   Define `pages` directory for routing.  
*   **Target Path 3:** `frontend/src/i18n/index.ts`  
    *   **Architectural Requirements:**  
        *   Export `resources` object containing language JSON files (`en/common.json`, `vi/common.json`).  
        *   Configure `i18next` with `fallbackLng: 'en'`, `debug: false`, `interpolation: { escapeValue: false }`.  

#### SUB‑TASK 1.2: Create base layout & protected route guard
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/layouts/AppLayout.tsx`  
    *   **Architectural Requirements:**  
        *   Wrap children with `AuthProvider` (context for JWT, user roles).  
        *   Include a persistent navigation bar that conditionally shows links based on `user.role`.  
        *   Render a global `ToastContainer` for notification messages.  
*   **Target Path 2:** `frontend/src/lib/authGuard.ts`  
    *   **Architectural Requirements:**  
        *   Function `requireAuth(roles?: Role[])` that redirects if token missing or role not allowed.  
        *   Use `getSession()` from `next-auth`‑style logic (or custom JWT decode).  

### DAY 2: Authentication UI & Social Sign‑In Integration
#### SUB‑TASK 2.1: Build Login page with email/password and social providers
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/pages/auth/login.tsx`  
    *   **Architectural Requirements:**  
        *   Form with email, password fields, “Remember me” checkbox.  
        *   Submit calls `POST /auth/login` (axios) and stores JWT in http‑only cookie + updates auth context.  
        *   Links to `/auth/register` (if allowed) and `/auth/forgot-password`.  
        *   Social buttons for **Google**, **Facebook**, **Firebase** that redirect to `/auth/social/google` etc., handling OAuth callback via `/api/auth/callback/{provider}`.  
*   **Target Path 2:** `frontend/src/services/authService.ts`  
    *   **Architectural Requirements:**  
        *   `login(credentials)`, `socialLogin(provider, code)`, `logout()`.  
        *   Refresh token logic using `/auth/refresh` (if implemented).  

#### SUB‑TASK 2.2: Write unit tests for login component
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/pages/auth/login.test.tsx`  
    *   **Architectural Requirements:**  
        *   Mock `authService.login` and verify it’s called with correct payload.  
        *   Simulate user interactions (type, click) and assert form validation errors.  
        *   Test social button redirects (using `jest.spyOn`).  
*   **Target Path 2:** `frontend/src/services/authService.test.ts`  
    *   **Architectural Requirements:**  
        *   Verify `login` makes `POST /auth/login` with proper headers.  
        *   Ensure error handling returns appropriate rejection.  

### DAY 3: Dashboard, QR Scanner & Real‑Time Attendance
#### SUB‑TASK 3.1: Implement Dashboard widget layout
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/pages/dashboard.tsx`  
    *   **Architectural Requirements:**  
        *   Protected route (role‑based).  
        *   Four main widgets:  
          1. **Upcoming Courses** – list of courses for today with teacher.  
          2. **Attendance Summary** – chart of daily attendance % (use `/api/attendance/summary`).  
          3. **Student Card Badges** – for Student role, display remaining days (fetch `/api/students/{id}/card`).  
          4. **Promotions & Announcements** – latest entries (fetch `/api/promotions`, `/api/announcements`).  
        *   Auto‑refresh every 15 seconds via `setInterval` (interval configurable via `process.env.NEXT_PUBLIC_DASHBOARD_REFRESH_MS`).  
*   **Target Path 2:** `frontend/src/components/DashboardWidget.tsx`  
    *   **Architectural Requirements:**  
        *   Reusable component accepting `title`, `data`, `loading` props.  
        *   Use Tailwind for responsive grid.  

#### SUB‑TASK 3.2: Build QR code scanner component & attendance API integration
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/components/QRScanner.tsx`  
    *   **Architectural Requirements:**  
        *   Wrap `html5-qrcode` library to scan from device camera.  
        *   Provide `onScan(successCallback, errorCallback)`.  
        *   UI overlay with start/stop controls.  
*   **Target Path 2:** `frontend/src/pages/attendance.tsx`  
    *   **Architectural Requirements:**  
        *   Protected (Teacher/Manager/Student).  
        *   Render `<QRScanner>`; on successful scan, POST payload to `POST /api/attendance/qr` with `{ studentId, scannedCode, timestamp }`.  
        *   Show toast notification on success/failure.  
*   **Target Path 3:** `frontend/src/hooks/useAttendance.ts`  
    *   **Architectural Requirements:**  
        *   `recordAttendance(qrData)` returns Promise.  
        *   Handle 409 if already scanned today (silent).  

#### SUB‑TASK 3.3: Write integration test for attendance flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/pages/attendance.test.tsx`  
    *   **Architectural Requirements:**  
        *   Mock `html5-qrcode` to simulate a scan result.  
        *   Mock `useAttendance.recordAttendance` to resolve.  
        *   Assert that a success toast appears and scanner stops.  
*   **Target Path 2:** `frontend/src/hooks/useAttendance.test.ts`  
    *   **Architectural Requirements:**  
        *   Verify API call uses correct endpoint and includes auth token.  

### DAY 4: Role‑Based Management Screens (Center, Course, Teacher, Student, Promotions, Announcements)
#### SUB‑TASK 4.1: Create Center Management screen (System Admin only)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/pages/center/list.tsx`  
    *   **Architectural Requirements:**  
        *   Guard: only `SystemAdmin` can access.  
        *   Table displaying centers (name, address, taxId, adminContact).  
        *   CRUD buttons: **Add**, **Edit**, **Delete** – each opens a modal with form.  
        *   **Assign/Unassign Admin** dropdown per row (calls `PUT /api/centers/{id}/admin`).  
*   **Target Path 2:** `frontend/src/services/centerService.ts`  
    *   **Architectural Requirements:**  
        *   `getCenters()`, `createCenter(payload)`, `updateCenter(id, payload)`, `deleteCenter(id)`, `assignAdmin(id, adminId)`.  

#### SUB‑TASK 4.2: Build Course Management screen (Admin & Manager)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/pages/course/list.tsx`  
    *   **Architectural Requirements:**  
        *   Role guard: `Admin` or `Manager`.  
        *   Filter by center (if Manager, only own center).  
        *   Columns: Course Name, Date Range, Teacher, Capacity, Status.  
        *   Actions: **Add** (modal with date validation to avoid overlap), **Edit**, **Delete**.  
        *   **Assign Teacher** modal – dropdown of available teachers (fetch `/api/teachers`).  
        *   **Register Students** button – opens student selector (multi‑select) and triggers bulk notification.  
*   **Target Path 2:** `frontend/src/services/courseService.ts`  
    *   **Architectural Requirements:**  
        *   `getCourses(filters)`, `createCourse(payload)`, `updateCourse(id, payload)`, `deleteCourse(id)`, `assignTeacher(id, teacherId)`.  

#### SUB‑TASK 4.3: Implement Teacher Management screen (Admin & Manager)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/pages/teacher/list.tsx`  
    *   **Architectural Requirements:**  
        *   Guard: `Admin` or `Manager`.  
        *   Table: Name, Phone, CCCD, Assigned Courses (list).  
        *   CRUD buttons – **Add** (creates user with role `Teacher` and sends notification), **Edit**, **Delete**.  
        *   **Assign/Unassign Courses** multi‑select per teacher (calls `POST /api/teachers/{id}/courses`).  
*   **Target Path 2:** `frontend/src/services/teacherService.ts`  
    *   **Architectural Requirements:**  
        *   `getTeachers()`, `createTeacher(payload)`, `updateTeacher(id, payload)`, `deleteTeacher(id)`, `assignCourses(id, courseIds)`.  

#### SUB‑TASK 4.4: Build Student Management screen (Admin & Manager)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/pages/student/list.tsx`  
    *   **Architectural Requirements:**  
        *   Guard: `Admin` or `Manager`.  
        *   Table: Name, Phone, CCCD, Enrolled Courses, Remaining Days Badge.  
        *   CRUD: **Add** (creates Student account, auto‑assigns to selected course, triggers notification), **Edit**, **Delete**.  
        *   **Enroll in Course** button per row – modal with available courses.  
*   **Target Path 2:** `frontend/src/services/studentService.ts`  
    *   **Architectural Requirements:**  
        *   `getStudents(filters)`, `createStudent(payload)`, `updateStudent(id, payload)`, `deleteStudent(id)`, `enrollStudent(id, courseId)`.  

#### SUB‑TASK 4.5: Create Promotion & Announcement Management screens (Admin & Manager)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/pages/promotion/list.tsx`  
    *   **Architectural Requirements:**  
        *   Guard: `Admin` or `Manager`.  
        *   Form fields: Title, Description, Conditions, Start Date, End Date (optional).  
        *   CRUD with **Save** triggering `POST /api/promotions` and pushing notification to all roles (except SystemAdmin).  
*   **Target Path 2:** `frontend/src/pages/announcement/list.tsx`  
    *   **Architectural Requirements:**  
        *   Similar CRUD, but **Save** also triggers notification to all roles (except SystemAdmin).  
*   **Target Path 3:** `frontend/src/services/notificationService.ts`  
    *   **Architectural Requirements:**  
        *   `createPromotionNotification(payload)`, `createAnnouncementNotification(payload)`.  

#### SUB‑TASK 4.6: Write end‑to‑end tests for key management flows
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/cypress/e2e/center_management.cy.ts`  
    *   **Architectural Requirements:**  
        *   Login as SystemAdmin. <br>• Add a new center. <br>• Verify it appears in table. <br>• Edit and delete.  
*   **Target Path 2:** `frontend/cypress/e2e/course_registration.cy.ts`  
    *   **Architectural Requirements:**  
        *   Login as Manager. <br>• Select a course. <br>• Enroll a student. <br>• Assert notification appears in app (mock push).  

### DAY 5: Mobile Enhancements, SEO, CI/CD & Final Review
#### SUB‑TASK 5.1: Add PWA manifest & service worker for mobile experience
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/public/manifest.json`  
    *   **Architectural Requirements:**  
        *   Define `short_name`, `start_url`, `display`, `background_color`, `icons` (48, 72, 96, 144, 192, 256, 512).  
*   **Target Path 2:** `frontend/src/lib/sw-register.ts`  
    *   **Architectural Requirements:**  
        *   Register service worker if `window.navigator.onLine`.  
        *   Cache static assets for offline fallback (`frontend/src/pages/offline.tsx`).  

#### SUB‑TASK 5.2: Implement SEO helpers (meta tags, sitemap, hreflang)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/src/lib/seo.ts`  
    *   **Architectural Requirements:**  
        *   Function `generateSeoMetaData({ title, description, path, locale })` returns Next.js `<Head>` tags.  
        *   Include `og:image`, `twitter:card`.  
*   **Target Path 2:** `frontend/src/pages/sitemap.xml.ts` (Next.js dynamic route)  
    *   **Architectural Requirements:**  
        *   Generate XML with `<url>` entries for all i18n routes (`en/`, `vi/`).  
*   **Target Path 3:** `frontend/src/components/Hreflang.tsx`  
    *   **Architectural Requirements:**  
        *   Render `<link rel="alternate" hrefLang="en" href={`/en${router.asPath}`} />` etc.  

#### SUB‑TASK 5.3: Run linting, type checking, and test suite; fix issues
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/.eslintrc.js`  
    *   **Architectural Requirements:**  
        *   Extend `next/core-web-vitals`, `plugin:react/recommended`.  
*   **Target Path 2:** `frontend/tsconfig.json`  
    *   **Architectural Requirements:**  
        *   Set `strict` mode, `noImplicitAny`.  
*   **Target Path 3:** CI log review (GitHub Actions) – ensure `npm run lint`, `npm run type-check`, `npm run test` exit with code 0.  

#### SUB‑TASK 5.4: Build Docker image for front‑end assets
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** `frontend/Dockerfile`  
    *   **Architectural Requirements:**  
        *   Multi‑stage: `node:20-alpine` for build (`npm ci`, `npm run build`). <br>• `nginx:alpine` for runtime, copy `out` (or `.next` + `public`) into `/usr/share/nginx/html`. <br>• Expose port `80`.  
*   **Target Path 2:** `frontend/docker-compose.yml` (optional local dev)  
    *   **Architectural Requirements:**  
        *   Services: `frontend` (build), `nginx` (proxy).  

#### SUB‑TASK 5.5: Final code review & sign‑off
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path 1:** All modified source files (list in review checklist)  
    *   **Architectural Requirements:**  
        *   Verify TypeScript compliance, ESLint rules, Prettier formatting.  
        *   Confirm accessibility (ARIA labels, contrast).  
        *   Validate i18n keys exist in translation files.  
        *   Ensure no hardcoded secrets or API URLs.  
*   **Target Path 2:** `frontend/README.md` (updated)  
    *   **Architectural Requirements:**  
        *   Document environment variables, build steps, and how to run tests locally.  

--- 

**End of Phase 3 Blueprint.**