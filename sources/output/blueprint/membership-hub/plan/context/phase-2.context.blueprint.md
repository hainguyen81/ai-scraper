# PHASE 2 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement the complete user authentication experience for the membership‑hub platform within the allocated Phase 2 window. This includes:

- **User Registration** – capture email/password (or social) with strict validation, hash passwords, issue a JWT (15‑min expiry) and create a local user record with the default “Student” role (REQ‑001).  
- **Social Authentication** – integrate Firebase, Google, and Facebook OAuth2 flows, exchange provider tokens for user info, map or create local accounts, and return JWT tokens (REQ‑002).  
- **User Role Assignment** – expose an admin‑driven endpoint to change a user’s role (System Admin, Center Admin, Manager, Teacher, Student) and enforce the new permissions immediately (REQ‑003).  
- **Frontend‑Backend Integration** – connect the Next.js UI to the auth services, manage bearer‑token state, and provide seamless login/register UI with error handling.  
- **OWASP & Non‑Functional Compliance** – apply input validation, parameterized queries, password hashing, JWT best‑practice, CSRF tokens, XSS prevention, and audit logging. Ensure GDPR/CCPA data‑handling rules (consent, deletion, export) are respected (NFR‑003, NFR‑008).  

All artifacts must be confined to the `./sources/` workspace boundary and follow the mandatory path prefixes (`./sources/frontend/`, `./sources/backend/`, `./sources/docs/`).

## 2. Allowed Technical Scope & Directory Boundaries
- **Frontend** – `./sources/frontend/` (React/Next.js pages, components, services, tests).  
- **Backend** – `./sources/backend/` (Java/Quarkus or Spring Boot services, following the `/org/nlh4j/saas/<lowercase‑token>/` package layout).  
- **Documentation** – `./sources/docs/` (Markdown specifications, architecture diagrams, security notes).  
- **Endpoints** – All auth APIs are REST under `/api/auth/*` (e.g., `POST /api/auth/register`, `POST /api/auth/login`, `POST /api/auth/social/{provider}`).  
- **Testing** – Unit tests reside under `./sources/backend/src/test/...`; UI/integration tests under `./sources/frontend/tests/`.  

No other directories or root‑level files are permitted.

## 3. Dedicated Sub-Agent Functional Directives
- **Coder** – Build the registration/login UI components, backend auth services, and enforce OWASP mitigations (input validation, password hashing, JWT handling, tenant_id scoping, CSRF tokens). Ensure GDPR fields are handled per consent.  
- **Doc** – Produce comprehensive documentation: authentication flow diagrams, API request/response schemas, security considerations, and OWASP compliance notes. Store all docs under `./sources/docs/`.  
- **Tester** – Write unit tests for registration/login services and integration tests for end‑to‑end auth flows. Include security‑focused tests (SQL injection attempts, XSS payloads, CSRF bypass) and verify error handling per EXC‑004.  

All sub‑tasks must reference the exact BA tag IDs from the raw requirements and stay within the `./sources/` boundary.

## 4. Phase Definition of Done (DoD)
- **Functional** – All registration, login, and social auth endpoints return valid JWTs, enforce role assignment, and respect multi‑tenancy (`tenant_id`).  
- **Security** – OWASP Top 10 mitigations applied (parameterized queries, password hashing, JWT expiry, CSRF tokens, XSS prevention). GDPR/CCPA data‑handling controls implemented.  
- **Testing** – Unit test coverage for auth modules ≥ 80 % (or defined metric), integration tests pass, security tests confirm no injection/CSRF vulnerabilities.  
- **Documentation** – Authentication flow, API spec, and security‑consideration documents created and reviewed.  
- **Compliance** – All referenced BA tags (`[REQ-001]`, `[REQ-002]`, `[REQ-003]`, `[EXC-004]`, `[DAT-001]`, `[DAT-008]`, `[NFR-003]`, etc.) are fully addressed.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Implement registration UI and initial documentation
#### SUB-TASK 1.1: Build frontend registration page with validation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/pages/RegisterPage.tsx
* **Architectural Requirements:**
  * Implement form fields for email, password, terms acceptance.
  * Apply client‑side validation matching REQ‑001 rules (email format, password complexity).
  * Integrate API call to `POST /api/auth/register` and handle JWT storage (http‑only cookies or secure localStorage).
  * Enforce CSRF token inclusion in request headers.
  * Log registration attempts for audit (NFR‑006).
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [EXC-004], [DAT-001], [NFR-003]

#### SUB-TASK 1.2: Document authentication flow overview
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/docs/authentication-flow.md
* **Architectural Requirements:**
  * Provide step‑by‑step flow from user registration to JWT issuance.
  * Include request/response schemas for `POST /api/auth/register`.
  * Highlight OWASP mitigations (input validation, password hashing, CSRF).
  * Reference GDPR/CCPA data handling notes.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [EXC-004], [DAT-001], [DAT-008], [NFR-003]

#### SUB-TASK 1.3: Write unit test for registration service
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/authservice/AuthService.java;./sources/backend/src/test/java/org/nlh4j/saas/authservice/AuthServiceTest.java
* **Architectural Requirements:**
  * Implement test cases covering successful registration, duplicate email, invalid password, and malformed input.
  * Verify password hashing (bcrypt) and JWT token generation with 15‑min expiry.
  * Assert that validation errors return appropriate HTTP status codes.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [EXC-004], [DAT-001], [NFR-003]

### DAY 2: Implement login UI, API spec, and integration testing
#### SUB-TASK 2.1: Build frontend login page with token management
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/pages/LoginPage.tsx
* **Architectural Requirements:**
  * Create email/password input fields with client‑side validation.
  * Integrate `POST /api/auth/login` and store JWT (secure, http‑only).
  * Implement logout that clears token and redirects.
  * Add CSRF token handling for state‑changing actions.
  * Log login attempts for audit (NFR‑006).
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [REQ-002], [EXC-004], [DAT-001], [NFR-003]

#### SUB-TASK 2.2: Document auth API specification
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/docs/auth-api-spec.md
* **Architectural Requirements:**
  * Detail all `/api/auth/*` endpoints (register, login, social/{provider}).
  * Include request/response payloads, HTTP status codes, and error formats.
  * Highlight security headers, JWT validation, and rate‑limiting considerations.
  * Reference OWASP and GDPR compliance notes.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [EXC-004], [DAT-001], [DAT-008], [NFR-003]

#### SUB-TASK 2.3: Perform end‑to‑end integration test for authentication flows
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/auth.integration.spec.ts
* **Architectural Requirements:**
  * Simulate user registration, login, and social auth (mock provider).
  * Verify JWT receipt, token expiration, and protected route access.
  * Validate error handling for invalid credentials and duplicate accounts.
  * Include security checks for CSRF and XSS in request/response.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [EXC-004], [DAT-001], [DAT-008], [NFR-003]

### DAY 3: Implement backend auth services and security documentation
#### SUB-TASK 3.1: Develop backend registration & login service layer
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/authservice/AuthService.java
* **Architectural Requirements:**
  * Implement `register(UserRegistrationDto)` – validate inputs, hash password (bcrypt), persist `Users` record with role “Student”, generate JWT (15‑min) and refresh token (7‑day).
  * Implement `login(AuthenticationDto)` – verify credentials, issue JWT/refresh, enforce multi‑tenancy `tenant_id` scoping.
  * Use parameterized queries to prevent SQL injection.
  * Include audit logging for registration/login events (NFR‑006).
  * Apply OWASP mitigations: input sanitization, rate limiting, secure password storage.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [REQ-002], [REQ-003], [EXC-004], [DAT-001], [DAT-008], [NFR-003]

#### SUB-TASK 3.2: Update security considerations documentation
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/docs/security-considerations.md
* **Architectural Requirements:**
  * Detail JWT handling, token rotation, and expiry policies.
  * Document password hashing algorithm and salt management.
  * Outline input validation and CSRF protection implementation.
  * Include OWASP Top 10 mapping for auth module.
  * Reference GDPR/CCPA data‑protection measures (consent, deletion).
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [NFR-003], [EXC-004], [DAT-001], [DAT-008]

#### SUB-TASK 3.3: Write unit test for login service
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/loginservice/LoginService.java;./sources/backend/src/test/java/org/nlh4j/saas/loginservice/LoginServiceTest.java
* **Architectural Requirements:**
  * Test successful authentication, invalid credentials, locked account scenarios.
  * Verify JWT payload claims and expiry.
  * Ensure password verification uses constant‑time comparison.
  * Validate error responses for malformed input.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-001], [REQ-002], [EXC-004], [DAT-001], [NFR-003]