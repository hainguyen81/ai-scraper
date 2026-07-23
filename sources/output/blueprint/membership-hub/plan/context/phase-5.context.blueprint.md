# PHASE 5 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement comprehensive security hardening and production deployment for the membership‑hub platform. This phase delivers OWASP A01‑A07 controls (access control, authentication, session management, data encryption, input validation, logging, and security misconfiguration), enforces Argon2 password hashing, token revocation, and audit logging, and establishes a CI/CD pipeline with automated security scanning. The deliverables include hardened Quarkus services, secure Docker images, GCP Cloud Build pipelines, GKE manifests, and end‑to‑end test coverage that validates all security controls and deployment integrity. The phase concludes with a production‑ready sign‑off.

## 2. Allowed Technical Scope & Directory Boundaries
- `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` – Core business logic, security filters, authentication services, audit interceptors.  
- `./sources/backend/src/main/resources/` – Application YAML/ properties (security config, datasource).  
- `./sources/backend/src/main/docker/` – Multi‑stage Dockerfile with non‑root user and scanning step.  
- `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/` – Unit & integration test suites.  
- `./sources/backend/cloudbuild.yaml` – GCP Cloud Build pipeline definition.  
- `./sources/backend/k8s/` – GKE deployment, service, and config maps.  
- `./sources/backend/scripts/` – Deployment and verification scripts.  
- `./sources/frontend/tests/` – UI/E2E security tests (if needed).  
- `./sources/` – Root for any generated documentation or sign‑off files.  

All paths are absolute to the workspace and strictly under `./sources/`. Java source files must follow the package layout `org/nlh4j/saas/membershiphub`.

## 3. Dedicated Sub-Agent Functional Directives
- **Coder:** Implement OWASP security filters, Argon2 password hashing, token revocation, audit logging interceptor, and update Dockerfile security best practices.  
- **Reviewer:** Validate OWASP compliance, review Argon2 and audit implementations, approve Dockerfile security hardening, and conduct final security scan verification.  
- **Docker:** Produce hardened multi‑stage Dockerfile with non‑root user, minimal layers, and integrated scanning (e.g., Trivy).  
- **GCP:** Define Cloud Build pipeline (`cloudbuild.yaml`) that builds, scans, and pushes Docker images to Artifact Registry.  
- **GKE:** Create Kubernetes deployment and service manifests that enforce resource limits, pod security policies, and proper tenant isolation.  
- **Manager:** Orchestrate CI/CD triggers, execute deployment to GKE, run integration tests, and generate production readiness sign‑off documentation.  
- **Tester:** Write unit tests for Argon2 and token revocation, execute integration/E2E security tests, and verify audit logging coverage.

## 4. Phase Definition of Done (DoD)
- OWASP scan passes with zero high‑severity findings.  
- Argon2 password hashing and token revocation functional; unit test coverage ≥ 80 % for security modules.  
- Audit logging interceptor captures all authentication and authorization events; logs stored immutably.  
- Dockerfile includes non‑root user, layer caching, and automated security scan; image passes Trivy with no critical CVEs.  
- Cloud Build pipeline defined, triggers on code push, builds, scans, and deploys to GKE automatically.  
- GKE manifests enforce resource quotas, pod security policies, and tenant isolation (`tenant_id`).  
- End‑to‑end integration/E2E test suite passes (security endpoints, audit verification, token revocation).  
- Production readiness sign‑off document generated and approved by Manager, Reviewer, and Tester.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: OWASP Security Hardening & Dockerfile Security Baseline
#### SUB‑TASK 1.1: Implement OWASP Security Filters in Quarkus
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/OwaspSecurityFilter.java
    *   **Architectural Requirements:**
        *   Add Quarkus `HttpInterceptor` to enforce access control (role‑based checks per tenant), input validation (JSR‑380), and CSRF protection.
        *   Integrate OWASP `Cryptography` utilities for AES‑256 PII encryption at rest.
        *   Apply parameterized queries via Panache to prevent SQL injection.
        *   Ensure all security controls are scoped to the current `tenant_id` for multi‑tenant isolation.

#### SUB‑TASK 1.2: Review OWASP Filter Implementation
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/OwaspSecurityFilter.java
    *   **Architectural Requirements:**
        *   Verify that all OWASP A01‑A07 controls are addressed per the design in SUB‑TASK 1.1.
        *   Confirm tenant filtering is applied consistently across all endpoints.
        *   Validate that PII encryption keys are managed via GCP Secret Manager.

#### SUB‑TASK 1.3: Create Hardened Multi‑Stage Dockerfile
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Use `java:21-jdk-slim` as base, copy Maven wrapper and pom, perform offline Maven build.
        *   Switch to a non‑root user (`appuser`) for runtime.
        *   Add `trivy` or `grype` scan step in the build stage to fail on critical CVEs.
        *   Include `jlink` to produce a custom runtime for reduced attack surface.
        *   Expose port `8080` and set health‑check endpoint (`/q/health`).

### DAY 2: Authentication Hardening, Token Revocation & Audit Logging
#### SUB‑TASK 2.1: Implement Argon2 Password Hashing Service
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/Argon2PasswordService.java
    *   **Architectural Requirements:**
        *   Use `org.apache.commons.codec.digest.Argon2` with configurable salt length and memory.
        *   Store hashed passwords in the user table; never store plain text or weak hashes.
        *   Provide `verify(String password, String hash)` method.
        *   Integrate with Quarkus security realm for password validation.

#### SUB‑TASK 2.2: Add Audit Logging Interceptor for Auth Events
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/interceptor/AuditLoggingInterceptor.java
    *   **Architectural Requirements:**
        *   Implement `ContainerRequestFilter` to capture login attempts, token issuance, revocation, and role changes.
        *   Log tenant‑scoped user actions with timestamps, IP, and user agent.
        *   Write logs to GCP Cloud Logging via structured JSON; ensure immutable storage.
        *   Include correlation ID for traceability across services.

#### SUB‑TASK 2.3: Write Unit Tests for Argon2 Hashing & Token Revocation
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/Argon2PasswordService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/security/Argon2PasswordServiceTest.java
    *   **Architectural Requirements:**
        *   Test hash generation, verification, and resistance to brute‑force (salt uniqueness).
        *   Validate token revocation endpoint returns `204` on successful logout.
        *   Ensure audit logs contain expected fields for each auth event.

#### SUB‑TASK 2.4: Review Audit Logging Implementation
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/interceptor/AuditLoggingInterceptor.java
    *   **Architectural Requirements:**
        *   Confirm all authentication and authorization events are intercepted.
        *   Verify log format complies with GCP Cloud Logging structured JSON schema.
        *   Validate tenant isolation of logs (no cross‑tenant leakage).

### DAY 3: CI/CD Pipeline Definition & GKE Deployment Manifests
#### SUB‑TASK 3.1: Update Dockerfile with Security Scan Step
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Insert a dedicated `SCAN` stage that runs `trivy fs --severity HIGH,CRITICAL .` on the built image.
        *   Fail the build if any HIGH or CRITICAL vulnerabilities are found.
        *   Tag the final image with `${PROJECT_ID}/membership-hub:${COMMIT_SHA}`.

#### SUB‑TASK 3.2: Define GCP Cloud Build Pipeline
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/cloudbuild.yaml
    *   **Architectural Requirements:**
        *   Trigger on `main` branch push.
        *   Steps: `mvn clean package`, `docker build`, `trivy scan`, `docker push` to Artifact Registry.
        *   Include `gcloud run deploy` or `gcloud kubernetes deploy` step to GKE.
        *   Store build logs and images in specified GCP project/region.

#### SUB‑TASK 3.3: Create GKE Deployment & Service Manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/k8s/deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy Quarkus pod with image `${PROJECT_ID}/membership-hub:${COMMIT_SHA}`.
        *   Set resource limits (`cpu: 250m`, `memory: 512Mi`) and pod security policy that runs as non‑root.
        *   Include `tenant_id` label for multi‑tenant routing.
        *   Configure liveness and readiness probes (`/q/health`).

#### SUB‑TASK 3.4: Manager Orchestrates CI/CD and Deploys to GKE
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/scripts/deploy.sh
    *   **Architectural Requirements:**
        *   Execute `gcloud builds submit --config=cloudbuild.yaml`.
        *   Wait for build completion and image push.
        *   Apply Kubernetes manifests (`kubectl apply -f k8s/`).
        *   Verify deployment status (`kubectl get deployments membership-hub`).
        *   Trigger integration test suite post‑deployment.

### DAY 4: End‑to‑End Security Verification & Production Sign‑Off
#### SUB‑TASK 4.1: Run Integration/E2E Security Test Suite
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/security.spec.ts
    *   **Architectural Requirements:**
        *   Execute UI tests covering login with internal email/password (Argon2), OAuth2 redirects, token revocation logout, and role‑based access controls.
        *   Validate audit log presence via backend API calls.
        *   Confirm that unauthorized endpoints return `403` for mismatched tenants.

#### SUB‑TASK 4.2: Perform Final Security Scan Verification
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Review Trivy scan report attached to the Docker image.
        *   Ensure no HIGH or CRITICAL vulnerabilities remain post‑build.
        *   Sign off on Dockerfile compliance.

#### SUB‑TASK 4.3: Generate Production Readiness Sign‑Off Document
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/phase5-readiness-signoff.md
    *   **Architectural Requirements:**
        *   Summarize OWASP hardening status, test results, scan outcomes, and deployment verification.
        *   Include quantitative metrics: unit test coverage ≥ 80 %, zero high‑severity CVEs, audit log retention configured.
        *   Provide approval signatures from Coder, Reviewer, and Tester.
        *   Mark phase complete and ready for production traffic.