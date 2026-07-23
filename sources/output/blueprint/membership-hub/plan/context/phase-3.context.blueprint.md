# PHASE 3 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Phase 3 delivers the native mobile experience for membership‑hub using a unified Next.js/React Native codebase. The implementation must provide role‑based UI, multi‑language support, QR‑based attendance capture, real‑time push notifications, and seamless integration with the existing Java/Quarkus backend services (user, course, notification APIs). All mobile components are built under the `./sources/frontend/` hierarchy, with dedicated mobile sub‑folders to keep web and app code isolated while sharing common utilities and i18n configuration. Integration testing validates end‑to‑end workflows across the mobile client, backend APIs, and external services (Zalo groups, push notification gateways). The phase concludes with a fully functional mobile app that passes OWASP‑aligned security checks and achieves ≥ 80 % integration test coverage.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- `./sources/frontend/` – root for all front‑end assets (web + mobile).  
- `./sources/frontend/mobile/` – mobile‑specific source tree.  
- `./sources/frontend/mobile/src/` – entry point (`App.js`/`_app.tsx`), navigation, and core modules.  
- `./sources/frontend/mobile/src/screens/` – role‑specific screen components (StudentDashboard, TeacherSchedule, AdminCenter, etc.).  
- `./sources/frontend/mobile/src/components/` – reusable UI primitives (QRScanner, NotificationBadge, RoleGuard, etc.).  
- `./sources/frontend/mobile/src/services/` – API client wrappers for attendance, user, course, notification endpoints (expects HTTPS, tenant_id header, JWT auth).  
- `./sources/frontend/mobile/src/utils/` – i18n configuration, secure storage helpers, QR validation, and OWASP‑compliant crypto utilities.  
- `./sources/frontend/tests/` – test suites; integration tests use the `INTEGRATION_SCOPE` token.  
- `./sources/frontend/tests/mobile.integration.spec.ts` – end‑to‑end test file verifying attendance flow, notifications, and role‑based navigation.  

*Backend API contracts are assumed to exist under `./sources/backend/...` and are referenced by the mobile services; no backend source creation is required in this phase.*

## 3. Dedicated Sub-Agent Functional Directives
- **Coder Agent** – Build the mobile application stack: project scaffolding, authentication flow, navigation, screen implementations, QR scanner integration, push‑notification handling, multi‑language i18n, and secure data storage. Embed OWASP compliance (multi‑tenancy `tenant_id` headers, AES‑256 encryption for PII, input validation, secure token storage, and parameterized API calls). Ensure all components follow the `./sources/frontend/` topology and are testable.
- **Tester Agent** – Execute integration testing for the mobile client: validate attendance QR scanning, notification delivery, role‑based UI access, and cross‑service API calls. Use the `INTEGRATION_SCOPE` token for multi‑component workflow verification. Generate a comprehensive test report meeting ≥ 80 % coverage and OWASP security validation.

## 4. Phase Definition of Done (DoD)
- **Functional Milestones**  
  - Mobile app entry point (`./sources/frontend/mobile/src/App.js`) bootstraps with role‑based router.  
  - Authentication module (`./sources/frontend/mobile/src/services/authService.js`) securely stores JWT, includes `tenant_id` header, and enforces password complexity.  
  - QR scanner component (`./sources/frontend/mobile/src/components/QRScanner.js`) validates scanned data per OWASP A03 (Injection) and triggers attendance API.  
  - Attendance service (`./sources/frontend/mobile/src/services/attendanceService.js`) calls backend `/api/v1/attendance` with encrypted payload and tenant context.  
  - Notification service (`./sources/frontend/mobile/src/services/notificationService.js`) integrates with push gateways and Zalo group APIs.  
  - Multi‑language support (`./sources/frontend/mobile/src/utils/i18n.js`) detects device locale, persists user choice, and renders UI strings.  
  - Role‑guard component (`./sources/frontend/mobile/src/components/RoleGuard.js`) enforces access per defined roles (Student, Teacher, Admin, Manager).  
- **Testing Milestones**  
  - Integration test suite (`./sources/frontend/tests/mobile.integration.spec.ts`) executes and covers attendance flow, notification delivery, and role‑based navigation (≥ 80 % feature coverage).  
  - All OWASP security checks pass (no hardcoded credentials, proper encryption, input validation, secure storage).  
- **Deliverables**  
  - Complete mobile source tree under `./sources/frontend/mobile/`.  
  - Integration test report and OWASP compliance sign‑off.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: MOBILE PROJECT SKELETON & AUTH INFRASTRUCTURE
#### SUB‑TASK 1.1: Initialize React Native project and configure Next.js hybrid structure
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/App.js
    *   **Architectural Requirements:**
        *   Set up React Native entry with Next.js App Router for hybrid rendering; define root navigation stack using React Navigation.
        *   Integrate `react-native-safe-area-context` and `react-native-screens` for native look‑and‑feel.
        *   Embed multi‑tenant `tenant_id` header injection via an Axios interceptor for all API calls.
        *   Implement JWT token storage using `react-native-secure-store` with AES‑256 encryption for sensitive fields (OWASP A02:2021 – Cryptographic Failures).
        *   Configure locale detection: read device locale, fallback to `en`, persist user preference in secure storage.

#### SUB‑TASK 1.2: Build authentication service and login screen
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/services/authService.js
    *   **Architectural Requirements:**
        *   Provide `login(credentials)` that sends POST to `/api/v1/auth/login` with `tenant_id` header and `x-client-role` header.
        *   Validate response for `access_token` and refresh token; store tokens encrypted via `react-native-secure-store`.
        *   Implement token refresh logic with automatic logout on invalid refresh.
        *   Enforce password complexity (min 8 chars, mix of letters/numbers) per OWASP A07:2021 – Identification and Authentication Failures.
        *   Log authentication events (success/failure) for audit trails.
*   **Target Path:** ./sources/frontend/mobile/src/screens/LoginScreen.js
    *   **Architectural Requirements:**
        *   Render email/password fields with client‑side validation (required, email format).
        *   Integrate OAuth buttons for Google/Facebook via Firebase Auth (use Firebase SDK, store provider tokens securely).
        *   Display loading spinner and error messages; redirect to appropriate role‑based dashboard after successful login.

### DAY 2: ROLE‑BASED NAVIGATION & CORE UI COMPONENTS
#### SUB‑TASK 2.1: Implement role‑guard and dynamic navigation based on user role
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/components/RoleGuard.js
    *   **Architectural Requirements:**
        *   Accept `allowedRoles` prop; read encrypted user role from secure storage.
        *   Redirect unauthenticated users to `/login`.
        *   Enforce role‑based access per specification (System Admin, Admin, Manager, Teacher, Student).
        *   Log unauthorized access attempts for security monitoring (OWASP A09:2021 – Security Misconfiguration).

#### SUB‑TASK 2.2: Create main dashboard screens for each role
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/screens/StudentDashboard.js
    *   **Architectural Requirements:**
        *   Display student ID, remaining class days, and QR scanner button.
        *   Integrate `QRScanner` component to capture attendance.
        *   Show push notifications list; implement swipe‑to‑dismiss.
        *   Support language toggle using i18n context.
*   **Target Path:** ./sources/frontend/mobile/src/screens/TeacherDashboard.js
    *   **Architectural Requirements:**
        *   Show schedule of assigned courses, list of enrolled students per course.
        *   Provide button to generate QR code for class session (backend endpoint `/api/v1/qr/generate`).
        *   Enforce teacher‑only access via `RoleGuard`.
*   **Target Path:** ./sources/frontend/mobile/src/screens/AdminDashboard.js
    *   **Architectural Requirements:**
        *   Render center management UI (list of centers, add/edit/delete).
        *   Access control: only System Admin and Admin roles permitted.
        *   Include navigation to Manager, Teacher, Student management screens.

#### SUB‑TASK 2.3: Build QR scanner component with secure input handling
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/components/QRScanner.js
    *   **Architectural Requirements:**
        *   Use `react-native-camera` for live preview.
        *   Parse scanned result; validate format (alphanumeric, length ≤ 64) to mitigate injection (OWASP A03).
        *   Call attendance service (`./sources/frontend/mobile/src/services/attendanceService.js`) with encrypted payload.
        *   Provide visual feedback (success/error toast) and store last scan locally (secure storage) for offline reference.

### DAY 3: ATTENDANCE, NOTIFICATIONS & BACKEND INTEGRATION
#### SUB‑TASK 3.1: Implement attendance service with tenant‑aware API calls
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/services/attendanceService.js
    *   **Architectural Requirements:**
        *   Export `scanQRCode(payload)` that POSTs to `/api/v1/attendance` with `tenant_id` header and encrypted `payload` (AES‑256).
        *   Validate server response; handle 4xx/5xx with user‑friendly alerts.
        *   Cache successful attendance locally (secure storage) for offline sync.
        *   Implement retry logic with exponential backoff for network failures.
        *   Log attendance events (including tenant_id, user_id, timestamp) for audit (OWASP A12:2023 – Security Logging).

#### SUB‑TASK 3.2: Build notification service and real‑time push handling
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/services/notificationService.js
    *   **Architectural Requirements:**
        *   Subscribe to push notification channel (React Native Push Notification) for both local and remote alerts.
        *   Forward remote notifications to Zalo group API (`/api/v1/notifications/zalo`) with tenant context.
        *   Encrypt sensitive notification payload fields (e.g., student PII) before storage.
        *   Provide `markAsRead(id)` to update local state and sync with backend.
*   **Target Path:** ./sources/frontend/mobile/src/components/NotificationBadge.js
    *   **Architectural Requirements:**
        *   Display badge count of unread notifications; update via NotificationService.
        *   Implement swipe actions to open notification details.
        *   Ensure badge UI respects accessibility and screen reader.

#### SUB‑TASK 3.3: Integrate multi‑language i18n and theme configuration
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/utils/i18n.js
    *   **Architectural Requirements:**
        *   Load resources from `./sources/frontend/mobile/src/locales/`.  
        *   Detect device locale (`react-native-device-info`); fallback to `en`.  
        *   Persist user language choice in secure storage.  
        *   Provide `useTranslation` hook for component consumption.  
*   **Target Path:** ./sources/frontend/mobile/src/components/LanguageToggle.js
    *   **Architectural Requirements:**
        *   Render a button to switch between supported locales; trigger i18n change and re‑render UI.

### DAY 4: INTEGRATION TESTING & OWASP VALIDATION
#### SUB‑TASK 4.1: Execute end‑to‑end integration test suite for mobile workflows
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/mobile.integration.spec.ts
    *   **Architectural Requirements:**
        *   Simulate login for each role (Student, Teacher, Admin) using mocked auth service.  
        *   Verify role‑guard redirects unauthorized users.  
        *   Trigger QR scan flow: invoke scanner component, mock attendance API call, assert attendance creation.  
        *   Validate notification delivery: mock push gateway and Zalo API, confirm UI update.  
        *   Test language switching: assert UI strings reflect selected locale.  
        *   Capture all network requests for tenant_id header presence and encrypted payload compliance.  
        *   Generate test report with ≥ 80 % feature coverage and flag any OWASP violations (e.g., missing tenant header, insecure storage).

#### SUB‑TASK 4.2: Perform OWASP security validation on mobile components
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/mobile/src/services/authService.js;./sources/frontend/tests/mobile.integration.spec.ts
    *   **Architectural Requirements:**
        *   Verify JWT tokens are stored encrypted (AES‑256) and not exposed in device logs.  
        *   Confirm password complexity rules enforced client‑side and transmitted securely.  
        *   Validate that all API calls include `tenant_id` header and use HTTPS.  
        *   Check QR input validation for injection attempts; ensure sanitized before API call.  
        *   Review secure storage usage (no plaintext tokens).  
        *   Document findings and ensure remediation before phase sign‑off.