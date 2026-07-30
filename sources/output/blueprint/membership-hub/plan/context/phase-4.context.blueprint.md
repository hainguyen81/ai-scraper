# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement the frontend user experience for **course browsing, enrollment, and student card management** as defined by requirements [REQ‑010] through [REQ‑015] and role [ARC‑004] (Student). This includes building reusable UI components, integrating with the existing backend APIs for course listings, enrollment creation, and student‑card data retrieval/renewal, and ensuring OWASP‑aligned security controls (input validation, CSRF tokens, tenant isolation). Concurrently, generate comprehensive technical documentation and execute end‑to‑end integration tests to validate the full workflow and security posture.

## 2. Allowed Technical Scope & Directory Boundaries
- **Frontend source tree**
  - `./sources/frontend/src/pages/course-browse.tsx`
  - `./sources/frontend/src/pages/enrollment.tsx`
  - `./sources/frontend/src/pages/student-card/renew.tsx`
  - `./sources/frontend/src/components/CourseBrowse.tsx`
  - `./sources/frontend/src/components/StudentCard.tsx`
  - `./sources/frontend/src/components/EnrollmentForm.tsx`
  - `./sources/frontend/src/components/CardRenewal.tsx`
  - `./sources/frontend/docs/` (markdown specifications)
  - `./sources/frontend/tests/` (integration test suites)
- **Backend API contracts (read‑only scope for integration)**
  - `./sources/backend/src/routes/course.ts`
  - `./sources/backend/src/routes/enrollment.ts`
  - `./sources/backend/src/routes/studentCard.ts`
  - `./sources/backend/src/services/courseService.ts`
  - `./sources/backend/src/services/enrollmentService.ts`
  - `./sources/backend/src/services/studentCardService.ts`
- **REST/GraphQL endpoints** (allowed for this phase)
  - `GET /api/courses` – returns course list (REQ‑007, REQ‑010)
  - `POST /api/enrollments` – creates enrollment (REQ‑011)
  - `GET /api/student-cards/{studentId}` – retrieves card data (REQ‑014)
  - `PUT /api/student-cards/{cardId}/renew` – extends validity (REQ‑015)

All paths must reside under `./sources/` and adhere to the project’s Node.js/Next.js conventions.

## 3. Dedicated Sub-Agent Functional Directives
- **Coder Agent**
  - Develop all UI components listed above using Next.js/React, TypeScript, and Material‑UI (or equivalent).  
  - Integrate components with the backend APIs, handling JWT authentication, tenant_id context, and CSRF protection.  
  - Enforce OWASP mitigations: parameterized queries on backend (handled by services), client‑side input sanitization, XSS prevention via `dangerouslySetInnerHTML` guards, and CSRF tokens for state‑changing actions.  
  - Implement multi‑language i18n for English, Vietnamese, and Spanish (REQ‑022, REQ‑023).  
  - Ensure GDPR/CCPA compliance by not exposing PII beyond required fields and supporting data export (NFR‑008).

- **Doc Agent**
  - Produce markdown specifications for each UI component, detailing purpose, props, API contracts, data flow, security considerations, and references to requirement tags.  
  - Store documentation under `./sources/frontend/docs/`.  
  - Include OWASP compliance notes and tenant isolation guidance.

- **Tester Agent**
  - Write integration test suites that simulate a Student role, authenticate via JWT, and exercise the full end‑to‑end flows for course browsing, enrollment, card display, and renewal.  
  - Validate API responses, UI rendering, tenant isolation, and security controls (input validation, CSRF).  
  - Use `INTEGRATION_SCOPE` syntax for multi‑component verification and ensure test coverage aligns with the functional requirements.

## 4. Phase Definition of Done (DoD)
- **Functional Completion**
  - All four UI components (CourseBrowse, StudentCard, EnrollmentForm, CardRenewal) are fully implemented, responsive, and i18n‑ready.  
  - Each component integrates with its respective backend API, handling authentication, tenant context, and error states.  
  - Documentation files exist for each component under `./sources/frontend/docs/`.  
- **Security & Compliance**
  - OWASP Top 10 mitigations are embedded: input validation, output encoding, CSRF tokens, and tenant isolation (`tenant_id`).  
  - All user‑provided data is validated per requirement specifications (EXC‑004).  
  - JWT tokens include 15‑minute expiry and refresh logic (ARC‑006).  
- **Testing & Quality**
  - End‑to‑end integration tests for each workflow pass (100 % pass rate).  
  - Test suites cover the required tag IDs and verify security controls.  
  - Code coverage for frontend components ≥ 80 % (as reported by test runner).  
- **Delivery**
  - All artifacts are committed to the repository under the `./sources/` boundary with correct file paths.  
  - No duplicate or placeholder files remain; the workspace is clean and ready for Phase 5.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: IMPLEMENT COURSE BROWSING UI AND STUDENT CARD DISPLAY

#### SUB-TASK 1.1: Develop CourseBrowse component for student course listing
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/CourseBrowse.tsx
* **Architectural Requirements:**
  * Render a responsive grid of courses fetched via `GET /api/courses`.  
  * Include search/filter fields with client‑side validation (EXC‑004).  
  * Integrate CSRF token for any future enrollment actions.  
  * Apply OWASP XSS mitigation by sanitizing any user‑provided filter text.  
  * Enforce tenant isolation by attaching the authenticated `tenant_id` to API requests.  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-010], [REQ-007], [ARC-004], [DAT-003], [EXC-004]

#### SUB-TASK 1.2: Develop StudentCard component for validity display
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/StudentCard.tsx
* **Architectural Requirements:**
  * Fetch student card data via `GET /api/student-cards/{studentId}`.  
  * Compute and display remaining validity days using server‑provided `remaining_days`.  
  * Implement client‑side validation for any future renewal input (EXC‑004).  
  * Secure API calls with JWT and tenant context.  
  * Ensure PII is not logged or exposed beyond required fields (NFR‑008).  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-014], [ARC-004], [DAT-006], [EXC-004]

#### SUB-TASK 1.3: Create technical documentation for CourseBrowse and StudentCard
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/docs/course-browse.md
* **Architectural Requirements:**
  * Document component purpose, props, state management, and API contract.  
  * Include security considerations: tenant isolation, CSRF usage, OWASP mitigations.  
  * Reference requirement tags and data dictionary entries ([DAT-003], [DAT-006]).  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-010], [REQ-014], [ARC-004], [DAT-003], [DAT-006]

### DAY 2: IMPLEMENT ENROLLMENT FLOW AND CARD RENEWAL

#### SUB-TASK 2.1: Develop EnrollmentForm component for student course registration
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/EnrollmentForm.tsx
* **Architectural Requirements:**
  * Provide a form for selecting a course and submitting enrollment via `POST /api/enrollments`.  
  * Validate required fields and enforce business rule that a student cannot enroll in duplicate courses (EXC‑004).  
  * Include CSRF token for submission.  
  * Use JWT authentication and tenant context for the request.  
  * Integrate with the CourseBrowse component for course selection.  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-011], [REQ-010], [ARC-004], [DAT-004], [EXC-004]

#### SUB-TASK 2.2: Develop CardRenewal component for membership extension
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/CardRenewal.tsx
* **Architectural Requirements:**
  * Offer a UI for selecting renewal days (1‑365) and initiating payment (stubbed).  
  * Validate renewal days input per requirement (EXC‑004).  
  * Call `PUT /api/student-cards/{cardId}/renew` with CSRF protection.  
  * Update local card state and display confirmation notification.  
  * Ensure tenant isolation and PII protection.  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-015], [ARC-004], [DAT-006], [EXC-004]

#### SUB-TASK 2.3: Update technical documentation for enrollment and renewal
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/docs/enrollment.md
* **Architectural Requirements:**
  * Document EnrollmentForm and CardRenewal component designs, API payloads, and error handling.  
  * Include security notes: CSRF, input validation, tenant isolation.  
  * Reference relevant data dictionaries ([DAT-004], [DAT-006]) and requirement tags.  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-011], [REQ-015], [ARC-004], [DAT-004], [DAT-006]

### DAY 3: INTEGRATION TESTING OF FRONTEND‑BACKEND WORKFLOWS

#### SUB-TASK 3.1: End‑to‑end integration test for course browsing
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/CourseBrowse.tsx;./sources/frontend/tests/course-browse.spec.ts
* **Architectural Requirements:**
  * Authenticate as a Student ([ARC-004]), fetch courses via `GET /api/courses`, verify UI renders list.  
  * Validate tenant isolation by checking that only courses for the authenticated tenant appear.  
  * Assert OWASP XSS protections by ensuring filter input is properly escaped.  
  * Confirm API response matches data dictionary ([DAT-003]) and requirement ([REQ-010], [REQ-007]).  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-010], [REQ-007], [ARC-004], [DAT-003], [EXC-004]

#### SUB-TASK 3.2: End‑to‑end integration test for enrollment
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/EnrollmentForm.tsx;./sources/frontend/tests/enrollment.spec.ts
* **Architectural Requirements:**
  * Simulate student login, select a course, submit enrollment via `POST /api/enrollments`.  
  * Verify enrollment record creation in backend ([DAT-004]) and receipt of success notification.  
  * Validate input sanitization and CSRF token handling.  
  * Ensure duplicate enrollment is rejected per EXC‑004.  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-011], [REQ-010], [ARC-004], [DAT-004], [EXC-004]

#### SUB-TASK 3.3: End‑to‑end integration test for student card display
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/StudentCard.tsx;./sources/frontend/tests/student-card.spec.ts
* **Architectural Requirements:**
  * Authenticate Student, request card data via `GET /api/student-cards/{studentId}`.  
  * Verify UI displays total validity, days used, and remaining days per [DAT-006].  
  * Confirm PII is encrypted at rest (AES‑256) and only necessary fields are exposed (NFR‑003).  
  * Validate tenant isolation and GDPR compliance (NFR‑008).  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-014], [ARC-004], [DAT-006], [EXC-004]

#### SUB-TASK 3.4: End‑to‑end integration test for card renewal
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/components/CardRenewal.tsx;./sources/frontend/tests/card-renewal.spec.ts
* **Architectural Requirements:**
  * Login as Student, initiate renewal with valid days, mock payment success.  
  * Verify backend updates `StudentCards` end date and logs the action (NFR‑006).  
  * Confirm notification is queued for the student (REQ‑016).  
  * Validate CSRF token and input validation (EXC‑004).  
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-015], [ARC-004], [DAT-006], [EXC-004]