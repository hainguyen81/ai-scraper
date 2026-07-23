# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement a native mobile experience that mirrors the admin web UI while providing student‑centric features:

- **Next.js‑based mobile UI** (iOS/Android via Capacitor) with role‑based routing, responsive design, and the same i18n/SEO stack as the web front‑end.  
- **In‑app QR scanner** that invokes the existing backend QR attendance service (single‑day flag) and updates the student’s card UI in real time.  
- **Student card UI** displaying remaining effective days, supporting manual day‑extension (enrollment) and reflecting attendance‑driven decrements.  
- **Push notification handling** (FCM/APNs) with automatic token registration, secure storage, and delivery of attendance, announcement, and promotion alerts.  
- **Mobile‑specific i18n & SEO** (hreflang, locale detection from device settings) and a lightweight Docker image for CI/CD that packages the mobile build artifacts for deployment on GCP GKE.  
- **Docker multi‑stage image** for the mobile build pipeline, ready for artifact registry push and GKE rollout.  

All work must stay within the `./sources/` workspace boundary, obey OWASP hardening (secure token storage, tenant isolation, parameterized calls), and be fully tested with unit and integration suites.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Frontend Mobile Root:** `./sources/frontend/mobile/`
- **Mobile Source Tree:**  
  - `./sources/frontend/mobile/src/`  
  - `./sources/frontend/mobile/src/components/`  
  - `./sources/frontend/mobile/src/services/`  
  - `./sources/frontend/mobile/src/pages/`  
  - `./sources/frontend/mobile/src/locales/` (i18n resources)  
  - `./sources/frontend/mobile/public/` (manifest, icons)  
- **Configuration & Build:**  
  - `./sources/frontend/mobile/capacitor.config.json`  
  - `./sources/frontend/mobile/package.json`  
  - `./sources/frontend/mobile/tsconfig.json`  
- **Docker Artifacts:**  
  - `./sources/frontend/mobile/Dockerfile`  
  - `./sources/frontend/mobile/.dockerignore`  
- **Test Assets (Unit):**  
  - `./sources/frontend/mobile/src/components/__tests__/StudentCard.test.tsx`  
  - `./sources/frontend/mobile/src/components/__tests__/QRScanner.test.tsx`  
  - `./sources/frontend/mobile/src/services/__tests__/PushNotificationService.test.tsx`  
- **Test Assets (Integration / E2E):**  
  - `./sources/frontend/mobile/e2e/attendance.spec.ts`  
  - `./sources/frontend/mobile/e2e/push.spec.ts`  
  - `./sources/frontend/mobile/e2e/fullflow.spec.ts`  
- **Allowed Backend Endpoints (mobile consumption):**  
  - `POST /api/v1/attendance/scan` (QR attendance)  
  - `GET /api/v1/students/{studentId}/card` (remaining days)  
  - `POST /api/v1/students/{studentId}/enroll` (day extension)  
  - `POST /api/v1/mobile/register-token` (push token registration)  
  - `GET /api/v1/i18n/{lang}` (i18n payload)  

All paths must be absolute to the workspace and prefixed with `./sources/`. No files may be placed directly under the repository root.

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE, Manager)
- **Coder:** Implement all mobile UI components, services, i18n/SEO configuration, QR scanner integration, attendance API calls, student card logic, push registration, enrollment flow, and Capacitor plugins. Embed OWASP‑required secure storage (encrypted push token) and tenant‑aware API calls.  
- **Tester:** Write unit tests for UI components and services; create integration/E2E tests for attendance scanning, push notification delivery, and end‑to‑end student workflows. Use the strict `<source>;<test>` syntax for unit tests and `INTEGRATION_SCOPE;<test>` for cross‑component flows.  
- **Reviewer:** Perform security and code reviews, validating OWASP A01‑A07 controls (input validation, tenant filtering, token encryption, secure API communication) and ensuring all generated paths comply with the `./sources/` boundary.  
- **Docker:** Craft a multi‑stage Dockerfile that builds Node.js, Capacitor, and native mobile assets, producing a lightweight image ready for artifact registry. Include `.dockerignore` to exclude build‑time artifacts.  
- **GCP:** Push the resulting Docker image to Google Artifact Registry and configure IAM permissions for GKE service accounts.  
- **GKE:** Update the existing GKE deployment manifests to roll out the mobile frontend service, applying the correct container image and resource limits.  
- **Manager:** Orchestrate the phase, verify that every sub‑task’s target paths are correctly placed under `./sources/`, coordinate hand‑offs, and ensure the Phase Definition of Done (DoD) is met before progression.

## 4. Phase Definition of Done (DoD)
- **Functional Delivery:**  
  - Mobile UI mirrors admin screens with role‑based routing.  
  - QR scanner successfully triggers attendance API and updates card UI.  
  - Student card displays accurate remaining days (attendance‑decremented + manual enrollment).  
  - Push notification registration, token storage, and receipt handling functional on both Android and iOS.  
  - Enrollment flow creates/updates student records and triggers push/announcement.  
  - Mobile‑specific i18n/SEO (hreflang, locale detection) fully operational.  
- **Containerization:**  
  - Docker multi‑stage image built, tagged, and pushed to GCP Artifact Registry.  
  - GKE deployment updated and service reachable.  
- **Quality & Security:**  
  - Unit test coverage ≥ 80 % for all mobile source files.  
  - All integration/E2E tests passing.  
  - OWASP A01‑A07 controls validated (input sanitization, tenant isolation, encrypted token storage, parameterized API calls).  
  - No files generated outside `./sources/`.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Mobile Project Scaffold & i18n/SEO Setup
#### SUB‑TASK 1.1: Create mobile project structure and Capacitor configuration
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/`
    *   **Architectural Requirements:** Initialize Next.js project with Capacitor integration, generate `capacitor.config.json` defining appId, appName, and platform targets (ios, android). Ensure all source files are placed under `./sources/frontend/mobile/src`.  
    *   **Security Enforcement:** No hardcoded credentials; all environment variables for API endpoints must be injected via `.env` files (never committed).  

#### SUB‑TASK 1.2: Configure mobile‑specific i18n and SEO
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/next-i18next.config.js`
    *   **Architectural Requirements:** Extend web i18n config with mobile‑only locale detection (device settings → navigator.language → fallback). Generate hreflang `<link>` tags in `<Head>` for each supported language.  
    *   **Security Enforcement:** Validate locale input against allowed list to prevent injection.  

#### SUB‑TASK 1.3: Review mobile scaffold for OWASP compliance and path correctness
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/`
    *   **Architectural Requirements:** Verify all generated files respect the `./sources/` boundary, no direct root artifacts, and that environment variables are not exposed in source code.  
    *   **Security Enforcement:** Confirm secure storage pattern for any future tokens (encrypted via `secure-electron-store` or native Keychain).  

### DAY 2: QR Scanner & Attendance Integration
#### SUB‑TASK 2.1: Implement QRScanner component using Capacitor Camera plugin
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/src/components/QRScanner.tsx`
    *   **Architectural Requirements:** Use `@capacitor/camera` to capture image, decode QR via `cordova-plugin-qrscanner` or a client‑side library, expose `scan()` method returning scanned payload.  
    *   **Security Enforcement:** Validate scanned payload format (alphanumeric, length limits) before API call.  

#### SUB‑TASK 2.2: Create AttendanceService to invoke backend attendance endpoint
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/src/services/AttendanceService.ts`
    *   **Architectural Requirements:** Implement `scanAttendance(studentId: string, qrPayload: string): Promise<void>` using `fetch` with tenant header (`x-tenant-id`) derived from JWT. Handle 409 (already scanned today) gracefully.  
    *   **Security Enforcement:** Enforce tenant filtering via JWT claim; use parameterized fetch (no string interpolation).  

#### SUB‑TASK 2.3: Unit test QRScanner component
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/src/components/QRScanner.tsx;./sources/frontend/mobile/src/components/__tests__/QRScanner.test.tsx`
    *   **Architectural Requirements:** Mock Capacitor Camera plugin and verify scan method triggers decode.  

#### SUB‑TASK 2.4: Integration test for attendance API flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/mobile/e2e/attendance.spec.ts
    *   **Architectural Requirements:** Simulate end‑to‑end QR scan, call `AttendanceService`, assert backend response and UI state update.  

### DAY 3: Student Card UI, Push Registration & Enrollment Flow
#### SUB‑TASK 3.1: Implement StudentCard component displaying remaining days
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/src/components/StudentCard.tsx`
    *   **Architectural Requirements:** Consume `GET /api/v1/students/{studentId}/card` via a custom hook; render days left, apply countdown styling, allow manual enrollment via a modal.  
    *   **Security Enforcement:** Include tenant header; sanitize studentId (UUID format).  

#### SUB‑TASK 3.2: Implement PushNotificationService for token registration and handling
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/src/services/PushNotificationService.ts`
    *   **Architectural Requirements:** Register with FCM (Android) / APNs (iOS) using `@capacitor/push-notifications`. Store token encrypted in native secure storage; expose `register()` and `onNotification()` methods.  
    *   **Security Enforcement:** Encrypt token before persistence (AES‑256 with app‑specific key); rotate key per tenant if multi‑tenant.  

#### SUB‑TASK 3.3: Implement enrollment page and day‑extension logic
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/src/pages/enrollment.tsx`
    *   **Architectural Requirements:** Form to select additional days, POST to `/api/v1/students/{studentId}/enroll`. Show confirmation and update StudentCard via event bus.  
    *   **Security Enforcement:** Validate day count (1‑365), enforce tenant header, CSRF token if applicable.  

#### SUB‑TASK 3.4: Unit test StudentCard component
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/src/components/StudentCard.tsx;./sources/frontend/mobile/src/components/__tests__/StudentCard.test.tsx`
    *   **Architectural Requirements:** Mock attendance API response and verify days rendering.  

#### SUB‑TASK 3.5: Unit test PushNotificationService
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/src/services/PushNotificationService.ts;./sources/frontend/mobile/src/services/__tests__/PushNotificationService.test.tsx`
    *   **Architectural Requirements:** Stub native plugins, assert token encryption and registration call.  

#### SUB‑TASK 3.6: Security review of push token storage
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/src/services/PushNotificationService.ts`
    *   **Architectural Requirements:** Validate encryption implementation, key management, and secure storage usage.  
    *   **Security Enforcement:** Ensure token is not logged or stored in plain text; key is not hard‑coded.  

### DAY 4: Dockerization, CI/CD & Final Sign‑off
#### SUB‑TASK 4.1: Create multi‑stage Dockerfile for mobile build
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/Dockerfile`
    *   **Architectural Requirements:** Stage 1 – Node.js build (`npm ci`, `next build`, `capacitor build`), Stage 2 – Minimal runtime image (`nginx` or `serve`) copying compiled assets and native binaries. Include `.dockerignore` to exclude `node_modules`, `.git`, and build artifacts.  
    *   **Security Enforcement:** Use non‑root user, minimal layers, scan for vulnerabilities (`trivy`).  

#### SUB‑TASK 4.2: Push Docker image to GCP Artifact Registry
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/Dockerfile`
    *   **Architectural Requirements:** Build image with `gcloud builds submit --tag <region>-docker.pkg.dev/<project>/mobile-app:latest`. Configure IAM service account with `artifactregistry.images.create` permission.  
    *   **Security Enforcement:** Ensure build service account has least‑privilege access; tag image with commit SHA for traceability.  

#### SUB‑TASK 4.3: Update GKE deployment manifest for mobile frontend
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/k8s/mobile-deployment.yaml`
    *   **Architectural Requirements:** Define Deployment with container image `<region>-docker.pkg.dev/<project>/mobile-app:latest`, resource limits, environment variables for API endpoints, and tenant‑aware secret mounts.  
    *   **Security Enforcement:** Apply PodSecurityPolicy or Seccomp profile; enforce `readOnlyRootFilesystem` where possible.  

#### SUB‑TASK 4.4: End‑to‑end test suite for full mobile workflow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/mobile/e2e/fullflow.spec.ts
    *   **Architectural Requirements:** Simulate login (mock auth), QR scan, attendance submission, push token registration, enrollment, and verification of UI updates.  

#### SUB‑TASK 4.5: Final phase sign‑off and compliance validation
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/mobile/`
    *   **Architectural Requirements:** Verify all files reside under `./sources/`, confirm Docker image built and pushed, ensure GKE deployment applied, and that all unit/integration tests pass.  
    *   **Security Enforcement:** Run OWASP ZAP scan against deployed mobile backend endpoints, validate tenant isolation, and confirm encrypted token storage.  

---