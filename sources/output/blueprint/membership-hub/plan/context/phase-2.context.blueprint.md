# PHASE 2 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Phase 2 focuses on implementing the core authentication and authorization system using OAuth 2.0 with JWT tokens for the backend, and developing the corresponding user interface components for login and registration on the frontend. This phase establishes secure multi-tenant access control aligned with RBAC matrix [ARC-001] to [ARC-005]. Backend implementation must support local email/password registration [REQ-001], social authentication via Firebase, Google, and Facebook OAuth2 [REQ-002], and JWT token generation/validation with 15-minute access tokens and 7-day refresh tokens [NFR-003]. Frontend must provide responsive login/registration UI with validation for email format, password strength, and terms acceptance [REQ-001], and OAuth2 provider integration flows [REQ-002]. All components must enforce TLS 1.3 [NFR-003] and prevent OWASP Top 10 vulnerabilities.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Paths:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` (Java source), `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/` (Java tests), `./sources/backend/config/` (OAuth2 configurations)
- **Frontend Paths:** `./sources/frontend/src/app/` (Next.js pages/components), `./sources/frontend/src/lib/` (authentication utilities), `./sources/frontend/src/styles/` (UI styles)
- **REST Endpoints:** `/api/auth/register` (POST), `/api/auth/login` (POST), `/api/auth/oauth/{provider}` (POST), `/api/auth/refresh` (POST), `/api/auth/logout` (POST)
- **Static Assets:** `./sources/frontend/public/` (OAuth2 provider icons/scripts)

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for coder, tester, reviewer, doc, docker, GCP, GKE)
- **coder:** Implements backend OAuth2/JWT logic and frontend UI components. Must inject parameterized queries, bcrypt password hashing, and JWT signature validation.
- **tester:** Writes unit/integration tests for authentication flows. Tests must verify token expiration, social provider integration, and input validation errors.
- **reviewer:** Performs static analysis on individual Java/TypeScript files to ensure OWASP compliance and absence of hardcoded secrets.
- **doc:** Creates technical documentation for authentication architecture, API specs, and OAuth2 setup guides. All docs must reside under `./sources/docs/`.

## 4. Phase Definition of Done (DoD)
- Backend passes all unit tests for [REQ-001], [REQ-002], [ARC-006] with 100% coverage.
- Frontend login/registration components implement all validation rules from [REQ-001].
- JWT tokens include `tenant_id` and `role` claims enforcing [ARC-001]-[ARC-005].
- OAuth2 providers (Firebase/Google/Facebook) integrated and functional.
- All code reviewed for OWASP A01, A02, A07 compliance [NFR-003].
- Documentation created for authentication flows and security protocols.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 4: BACKEND OAUTH2 PROVIDER CONFIGURATION
#### SUB-TASK 4.1: Implement OAuth2 client configurations for Firebase, Google, and Facebook
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/config/OAuth2Config.java`
    *   **Architectural Requirements:**
        *   Use Quarkus OIDC extension with `@ConfigMapping` for provider credentials
        *   Store client secrets in GCP Secret Manager with environment variable injection
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-002], [ARC-006]

#### SUB-TASK 4.2: Create social authentication service with token exchange and user profile mapping
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/SocialAuthService.java`
    *   **Architectural Requirements:**
        *   Implement idempotent user creation/update using `provider`+`provider_id` unique constraint
        *   Validate OAuth2 tokens against provider endpoints to prevent token injection
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-002], [ARC-006]

#### SUB-TASK 4.3: Write unit tests for OAuth2 configuration and token validation
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/config/OAuth2Config.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/config/OAuth2ConfigTest.java`
    *   **Architectural Requirements:**
        *   Mock provider endpoints to simulate token exchange flows
        *   Verify error handling for invalid tokens and provider outages
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-002], [NFR-003]

### DAY 5: JWT TOKEN GENERATION AND VALIDATION
#### SUB-TASK 5.1: Implement JWT token provider with tenant_id and role claims
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/JwtTokenService.java`
    *   **Architectural Requirements:**
        *   Use RSA256 signatures with keys rotated every 90 days
        *   Include `tenant_id` claim from user's center assignment for multi-tenancy
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-002], [ARC-006], [NFR-003]

#### SUB-TASK 5.2: Create authentication filter for JWT validation on protected endpoints
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/filter/AuthenticationFilter.java`
    *   **Architectural Requirements:**
        *   Validate token signature and expiration using jjwt library
        *   Reject tokens missing required claims (`tenant_id`, `role`)
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-001], [ARC-002], [NFR-003]

#### SUB-TASK 5.3: Test token generation and validation with edge cases
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/JwtTokenService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/JwtTokenServiceTest.java`
    *   **Architectural Requirements:**
        *   Verify token expiration after 15 minutes and refresh token after 7 days
        *   Test token rejection for invalid signatures and missing claims
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003]

### DAY 6: FRONTEND LOGIN AND REGISTRATION UI
#### SUB-TASK 6.1: Create responsive login form with email/password and OAuth2 provider buttons
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/app/login/page.tsx`
    *   **Architectural Requirements:**
        *   Implement real-time validation for email format and password strength
        *   Include Firebase, Google, Facebook OAuth2 buttons with provider logos
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-001], [REQ-002]

#### SUB-TASK 6.2: Build registration form with terms acceptance and validation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/app/register/page.tsx`
    *   **Architectural Requirements:**
        *   Enforce password complexity: 8+ chars, uppercase, lowercase, number, special char
        *   Require terms checkbox and provide link to terms document
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-001]

#### SUB-TASK 6.3: Implement authentication context and token management
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/lib/auth.ts`
    *   **Architectural Requirements:**
        *   Store JWT tokens in secure HTTP-only cookies
        *   Implement automatic token refresh before expiration
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [ARC-006], [NFR-003]

#### SUB-TASK 6.4: Review authentication service for security vulnerabilities
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/JwtTokenService.java`
    *   **Architectural Requirements:**
        *   Verify no hardcoded secrets or weak algorithm configurations
        *   Ensure all database queries use parameterized statements
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003]

#### SUB-TASK 6.5: Create authentication architecture documentation
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/docs/authentication-architecture.md`
    *   **Architectural Requirements:**
        *   Document OAuth2 flow diagrams and JWT claim structure
        *   Include setup instructions for each social provider
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-002], [ARC-006]