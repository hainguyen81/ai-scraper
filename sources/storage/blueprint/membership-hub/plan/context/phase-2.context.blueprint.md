# PHASE 2 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Develop a cross‑platform mobile application using Next.js that enables students to check‑in via QR code and view their membership status (remaining validity days, card UI).  
- Implement unit tests for all mobile app components to guarantee functional correctness and OWASP‑compliant handling of user input and API calls.  
- Produce comprehensive technical documentation covering project structure, API contracts, and testing strategies.

## 2. Allowed Technical Scope & Directory Boundaries
- **Frontend source tree:** `./sources/frontend/`  
  - `./sources/frontend/src/` – React/Next.js source (pages, components, hooks)  
  - `./sources/frontend/src/pages/` – Next.js page routes (`./sources/frontend/src/pages/checkin.tsx`, `./sources/frontend/src/pages/dashboard.tsx`)  
  - `./sources/frontend/src/components/` – UI primitives (`MembershipCard.tsx`, `QRScanner.tsx`)  
  - `./sources/frontend/src/services/` – API client (`api.ts`)  
  - `./sources/frontend/src/tests/` – Jest/React‑Testing‑Library unit tests  
  - `./sources/frontend/public/` – static assets (QR code icons, app icons)  
- **Backend API contracts (read‑only scope for this phase):**  
  - `POST /api/v1/centers/{centerId}/students/{studentId}/checkin` – triggers student check‑in  
  - `GET /api/v1/centers/{centerId}/students/{studentId}/membership` – returns membership status and remaining days  
- All paths must respect the `./sources/` root and the `./sources/frontend/` prefix.

## 3. Dedicated Sub-Agent Functional Directives
- **coder:** Build the Next.js mobile front‑end, implement QR‑based check‑in UI, membership card display, and client‑side API integration. Ensure OWASP‑compliant input validation, secure storage of tenant identifiers, and AES‑256 encryption for sensitive PII on the client side.  
- **tester:** Author unit tests for page components, service calls, and validation logic. Achieve ≥ 90 % line coverage and enforce security‑focused test cases (e.g., malformed QR payloads, tenant‑id tampering).  
- **doc:** Generate end‑to‑end technical documentation (architecture diagram, API contract spec, README, and test‑report summary) stored under `./sources/frontend/docs/`.

## 4. Phase Definition of Done (DoD)
- Mobile app runs locally, supports QR check‑in and displays membership validity.  
- All unit tests pass with ≥ 90 % coverage on `./sources/frontend/src/`.  
- OWASP A01–A09 controls are embedded (input validation, tenant isolation, encrypted storage, secure headers).  
- Documentation assets exist in `./sources/frontend/docs/` and are referenced from `./sources/frontend/README.md`.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Initialize Next.js mobile app and create core UI components
#### SUB‑TASK 1.1: Scaffold Next.js project and define page routes for check‑in and dashboard
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/package.json`
    * **Architectural Requirements:**
        * Use Next.js 13+ with App Router; set `reactStrictMode` true.  
        * Configure `eslint` with OWASP security lint rules.  
        * Include `tailwindcss` for responsive mobile UI.  
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [REQ-002], [ARC-002]

#### SUB‑TASK 1.2: Create check‑in page with QR scanner and status display
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/pages/checkin.tsx`
    * **Architectural Requirements:**
        * Implement a functional component that renders a QR scanner (using `react-qr-reader`).  
        * On successful scan, invoke `api.checkIn(centerId, studentId, qrPayload)` with tenant‑scoped `centerId`.  
        * Validate QR payload format (UUID) and enforce OWASP A03:2021 (Injection) via regex.  
        * Store scanned result in secure local storage using AES‑256 (key derived from environment variable).  
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [REQ-002], [ARC-002]

#### SUB‑TASK 1.3: Create membership dashboard page for status and validity
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/pages/dashboard.tsx`
    * **Architectural Requirements:**
        * Render `MembershipCard` component populated by `api.getMembership(centerId, studentId)`.  
        * Display remaining validity days with a countdown timer.  
        * Apply tenant isolation: ensure `centerId` is taken from authenticated context, not user‑modifiable.  
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [REQ-002], [ARC-002]

#### SUB‑TASK 1.4: Document project architecture and API contracts
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/docs/architecture.md`
    * **Architectural Requirements:**
        * Include diagram of Next.js mobile app flow, QR check‑in process, and API endpoints.  
        * List request/response schemas for `/api/v1/centers/{centerId}/students/{studentId}/checkin` and `/api/v1/centers/{centerId}/students/{studentId}/membership`.  
        * Note OWASP security controls applied (input validation, encryption, tenant isolation).  
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [REQ-002], [ARC-002], [NFR-003]

#### SUB‑TASK 1.5: Write unit tests for check‑in page and membership card
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/pages/checkin.tsx;./sources/frontend/src/tests/pages/checkin.test.tsx`
    * **Architectural Requirements:**
        * Use Jest + React‑Testing‑Library to render page, simulate QR scan, and verify API call.  
        * Mock `api.checkIn` and assert correct tenant parameters.  
        * Include security test for malformed QR payload (reject with validation error).  
    * **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        * **Targeted Tag IDs:** [ARC-002], [NFR-003]

Phase 2 objectives are fully satisfied on Day 1; no further daily logs are required.