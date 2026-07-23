# PHASE 5 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- **End‑to‑End Integration Testing:** Build and execute comprehensive integration test suites that validate all cross‑service flows (student enrollment, course assignment, QR attendance, point accrual, multi‑tenant notifications, promotion/announcement broadcasting, and AI chat widget interactions).  
- **Multi‑Tenant Data Leakage Validation:** Develop automated audit scripts to verify tenant isolation across all data access paths, ensuring `tenant_id` filtering is enforced and no cross‑center data leakage occurs.  
- **OWASP Hardening Implementation:** Enforce input validation, output encoding, AES‑256‑GCM PII encryption, Argon2id password hashing, parameterized queries, injection defenses, and robust authentication failure handling across the Quarkus backend.  
- **Containerization & Multi‑Stage Docker Builds:** Produce production‑ready Dockerfiles for the Java backend (`./sources/backend/Dockerfile`) and the Next.js frontend (`./sources/frontend/Dockerfile`) with minimal image layers and security best‑practices.  
- **GKE Production Deployment:** Generate Kubernetes manifests (Deployments, Services, Ingress, HPA, ConfigMaps, Secrets) under `./sources/` for both backend and frontend services, integrated with auto‑scaling and resource limits.  
- **GCP Infrastructure & CI/CD:** Define IAM policies, service accounts, Cloud Storage buckets, and Cloud Build pipelines to automate build, test, and deploy workflows.  
- **Monitoring & Performance Validation:** Instrument Prometheus/Grafana monitoring, run scaling tests, and verify performance metrics meet SLA targets.  
- **Final Sign‑Off:** Achieve 100 % requirement coverage, secure artifact generation, and complete security audit clearance.

## 2. Allowed Technical Scope & Directory Boundaries
- **Backend Java Sources:** `./sources/backend/src/main/java/org/nlh4j/saas/membershippub/` (all service, security, validation, encryption, and utility classes).  
- **Backend Tests:** `./sources/backend/src/test/java/org/nlh4j/saas/membershippub/` (unit, integration, and security audit tests).  
- **Frontend Sources:** `./sources/frontend/src/` (Next.js pages, components, API routes, i18n resources).  
- **Frontend Tests:** `./sources/frontend/tests/` (Cypress/E2E specs, Jest unit tests).  
- **Docker Files:** `./sources/backend/Dockerfile`, `./sources/frontend/Dockerfile`.  
- **Kubernetes Manifests:** `./sources/gke/` (backend‑deployment.yaml, frontend‑deployment.yaml, service.yaml, ingress.yaml, hpa.yaml, configmap.yaml, secret.yaml).  
- **GCP Infrastructure:** `./sources/gcp/` (iam-policy.yaml, service‑account.yaml, storage‑buckets.yaml, cloudbuild.yaml).  
- **Monitoring & Profiling:** `./sources/monitoring/` (prometheus‑config.yaml, grafana‑dashboard.json).  
- **Phase Documentation:** `./sources/phase5-signoff.md`.

## 3. Dedicated Sub-Agent Functional Directives
- **Coder:** Implement OWASP hardening utilities (AES‑256‑GCM encryption, Argon2id password hashing, input validation filters, parameterized query helpers), create integration test suite skeletons, and develop tenant‑isolation audit scripts.  
- **Tester:** Execute integration test suites, run performance & scaling tests, validate monitoring stack, and perform security audit test runs.  
- **Reviewer:** Conduct multi‑tenant data leakage audits, verify OWASP compliance of all code changes, and approve security hardening artifacts.  
- **Docker:** Craft multi‑stage Dockerfiles with non‑root user, slimmed‑down base images, and security labels; build and push images to Artifact Registry.  
- **GCP:** Define IAM roles, service accounts with least‑privilege, Cloud Storage buckets for artifacts, and Cloud Build triggers for CI/CD pipelines.  
- **GKE:** Generate Kubernetes Deployment, Service, Ingress, HPA, ConfigMap, and Secret manifests; configure resource requests/limits and auto‑scaling policies.  
- **Manager:** Orchestrate the overall Phase 5 workflow, coordinate agent hand‑offs, ensure all artifacts are placed under `./sources/`, and produce the final sign‑off documentation confirming 100 % coverage and audit clearance.

## 4. Phase Definition of Done (DoD)
- **Integration Coverage:** All core business flows exercised by integration tests; test pass rate ≥ 99 %.  
- **Security Hardening:** OWASP top‑10 controls implemented (input validation, encryption, password hashing, parameterized queries, injection defense, auth failure handling).  
- **Tenant Isolation:** Automated leakage audit passes with zero cross‑tenant data exposure.  
- **Container Images:** Successful build of backend and frontend Docker images, scanned and compliant with vulnerability thresholds.  
- **GKE Deployments:** All Kubernetes manifests applied, services reachable, HPA functional, resource limits enforced.  
- **GCP Infrastructure:** IAM policies applied, service accounts scoped, Cloud Build pipeline triggers functional, artifact storage operational.  
- **Monitoring & Performance:** Prometheus metrics collected, Grafana dashboards populated, scaling tests meet target latency and throughput.  
- **Sign‑Off:** Phase 5 sign‑off document generated under `./sources/phase5-signoff.md` with checklist confirming all above milestones and 100 % requirement coverage.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Integration Test Suite Construction & OWASP Hardening

#### SUB-TASK 1.1: Implement OWASP Hardening Utilities (Encryption, Password Hashing, Input Validation)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershippub/security/EncryptionService.java
    *   **Architectural Requirements:**
        *   Provide AES‑256‑GCM encryption/decryption methods for PII fields with key management via GCP Secret Manager.
        *   Enforce OWASP A03:2021 – Injection by using parameterized queries via Hibernate native query interfaces.
        *   Implement Argon2id password hashing with salt length ≥ 16 bytes and iteration count ≥ 3 × 2⁸.
        *   Add request/response validation filters that reject malformed JSON and enforce max payload size.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershippub/security/PasswordService.java
    *   **Architectural Requirements:**
        *   Centralize Argon2id hashing for all user credentials; integrate with Quarkus security event listeners.
        *   Store hash with salt and version; enforce minimum work factor per OWASP guidelines.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershippub/filter/InputValidationFilter.java
    *   **Architectural Requirements:**
        *   Apply OWASP input validation patterns (SQL injection, XSS, LDAP injection) using Jakarta Validation API.
        *   Log validation failures for audit; return 400 with generic error messages.

#### SUB-TASK 1.2: Create Integration Test Suite for Core Business Flows
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/test/java/org/nlh4j/saas/membershippub/integration/MembershipHubIntegrationTest.java
    *   **Architectural Requirements:**
        *   Use Testcontainers to spin PostgreSQL and Kafka for isolated integration testing.
        *   Validate student enrollment → point accrual (10 pts) flow.
        *   Verify QR attendance endpoint idempotency and remaining‑days calculation.
        *   Test promotion/announcement broadcast to tenant groups and mobile push.
        *   Include security checks for tenant isolation (ensure data of tenant‑A not accessible by tenant‑B).

#### SUB-TASK 1.3: Execute Integration Test Suite
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membershippub/integration/MembershipHubIntegrationTest.java
    *   **Architectural Requirements:**
        *   Run the suite against a temporary GKE cluster using KinD; capture pass/fail metrics.
        *   Ensure all tenant‑isolation assertions pass; report any leakage.

#### SUB-TASK 1.4: Perform Multi‑Tenant Data Leakage Audit
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/test/java/org/nlh4j/saas/membershippub/security/TenantIsolationAuditTest.java
    *   **Architectural Requirements:**
        *   Write queries that attempt cross‑tenant access on each entity (centers, users, courses, enrollments, attendance, points, promotions, announcements).
        *   Assert that all such queries return zero rows, confirming `tenant_id` filtering enforcement.
        *   Generate a compliance report stored in `./sources/tenant‑leakage‑report.json`.

### DAY 2: Containerization, GKE Deployment, GCP Infrastructure & Final Sign‑Off

#### SUB-TASK 2.1: Build Multi‑Stage Dockerfiles for Backend & Frontend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/Dockerfile
    *   **Architectural Requirements:**
        *   Use `eclipse-temurin:17-jdk-alpine` as base; copy Maven wrapper and project; run `mvn package -DskipTests`; create a distroless runtime image with non‑root user.
        *   Include security labels (`org.opencontainers.image.base.name`, `org.nlh4j.saas.security=true`).
*   **Target Path:** ./sources/frontend/Dockerfile
    *   **Architectural Requirements:**
        *   Use `node:20-alpine` as builder; install dependencies, build Next.js app; copy to nginx Alpine image; expose port 80; run as non‑root user.
        *   Apply `nginx` security hardening (disable unnecessary modules, limit CPU/Memory).

#### SUB-TASK 2.2: Generate GKE Deployment Manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/gke/backend-deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy Quarkus app with 3 replicas, resource requests/limits (CPU 500m/1000m, Memory 1Gi/2Gi).
        *   Use `imagePullSecrets` for Artifact Registry authentication.
        *   Include liveness/readiness probes.
*   **Target Path:** ./sources/gke/frontend-deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy Next.js via nginx with 2 replicas, similar resource limits.
        *   Mount ConfigMap for environment variables (e.g., `APP_ENV`, `LOCALE_DEFAULT`).
*   **Target Path:** ./sources/gke/service.yaml
    *   **Architectural Requirements:**
        *   Expose backend on port 8080, frontend on port 80; set appropriate `sessionAffinity` for tenant sticky sessions.
*   **Target Path:** ./sources/gke/ingress.yaml
    *   **Architectural Requirements:**
        *   Define Ingress with TLS, host rules for `membership-hub.internal` and `membership-hub.com`.
*   **Target Path:** ./sources/gke/hpa.yaml
    *   **Architectural Requirements:**
        *   Configure Horizontal Pod Autoscaler based on CPU and custom metrics (e.g., Kafka lag).

#### SUB-TASK 2.3: Define GCP IAM, Service Accounts & Cloud Build Pipelines
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/gcp/iam-policy.yaml
    *   **Architectural Requirements:**
        *   Create service accounts `backend-sa` and `frontend-sa` with roles `CloudDeployer`, `ArtifactRegistry.Writer`, `CloudSQL.User`, `Pub/Sub.Publisher`, `Pub/Sub.Subscriber`.
        *   Enforce least‑privilege; attach `tenant‑specific` role constraints.
*   **Target Path:** ./sources/gcp/service-account-backend.yaml
    *   **Architectural Requirements:**
        *   Define JSON key template for backend service account; store in Secret Manager.
*   **Target Path:** ./sources/gcp/service-account-frontend.yaml
    *   **Architectural Requirements:**
        *   Define JSON key template for frontend service account; store in Secret Manager.
*   **Target Path:** ./sources/gcp/cloudbuild.yaml
    *   **Architectural Requirements:**
        *   Trigger builds on source changes; steps: `mvn clean package`, `docker build -f ./sources/backend/Dockerfile`, `docker build -f ./sources/frontend/Dockerfile`, push to Artifact Registry, invoke Cloud Deploy release.

#### SUB-TASK 2.4: Run Performance & Scaling Tests, Validate Monitoring Stack
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/backend/tests/PerformanceTest.java
    *   **Architectural Requirements:**
        *   Simulate concurrent enrollment and attendance requests (e.g., 500 RPS) using Gatling.
        *   Measure response times, error rates, and throughput; assert p95 < 200 ms.
*   **Target Path:** INTEGRATION_SCOPE;./sources/monitoring/prometheus-config.yaml
    *   **Architectural Requirements:**
        *   Define metrics for Quarkus (JVM, HTTP, Kafka) and Next.js (request duration, error rate).
*   **Target Path:** INTEGRATION_SCOPE;./sources/monitoring/grafana-dashboard.json
    *   **Architectural Requirements:**
        *   Create panels for active tenants, enrollment rate, attendance count, point accrual, and AI chat usage.

#### SUB-TASK 2.5: Produce Phase 5 Sign‑Off Documentation
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/phase5-signoff.md
    *   **Architectural Requirements:**
        *   Summarize all completed sub‑tasks, list passed test suites, confirm OWASP hardening checklist items.
        *   Attach links to Docker images in Artifact Registry, GKE deployment URLs, and monitoring dashboards.
        *   Declare 100 % requirement coverage and security audit clearance.