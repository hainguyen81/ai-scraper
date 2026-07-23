# PHASE 5 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- **End‑to‑End Integration Testing** – Validate API contracts, Kafka event streams (`attendance`, `notifications`, `zalo-message`), and cross‑service UI flows for both web and mobile clients.  
- **OWASP Security Hardening** – Enforce A01‑A07 controls across the Java 17 Quarkus backend: multi‑tenant `tenant_id` filtering, AES‑256 PII encryption at rest, parameterized queries, JWT signature verification, lease expiration, and revocation. Perform tenant leakage checks.  
- **Performance Profiling & Load Testing** – Instrument critical paths (QR attendance scanning, notification dispatch, student card day counter) and execute load tests to confirm sub‑second response times under peak concurrency.  
- **Production Docker Images & GKE Deployment** – Build multi‑stage Docker images for backend and frontend, push to GCP Artifact Registry, generate Kustomize/Helm manifests, and deploy to a hardened GKE cluster with network policies, pod security standards, and autoscaling.  
- **CI/CD Pipeline & Governance** – Configure GitHub Actions → Cloud Build → GKE promotion pipeline, enforce immutable infrastructure, and produce final sign‑off artifacts confirming all raw requirements are implemented, secured, and deployed.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Java Code** – `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` (service, security, config, integration)  
- **Backend Tests** – `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/` (unit, integration, load)  
- **Backend Docker** – `./sources/backend/docker/Dockerfile` (multi‑stage)  
- **Backend K8s Manifests** – `./sources/backend/k8s/deployment.yaml`, `./sources/backend/k8s/service.yaml`, `./sources/backend/k8s/ingress.yaml`  
- **Frontend Web UI** – `./sources/frontend/web/` (Next.js pages, components, i18n)  
- **Frontend Mobile UI** – `./sources/frontend/mobile/` (Capacitor/React‑Native)  
- **Frontend Tests** – `./sources/frontend/tests/` (unit, integration, e2e)  
- **CI/CD Pipelines** – `./sources/ci/` (github/workflows, cloudbuild.yaml)  
- **Observability & Config** – `./sources/config/` (application.yml, logback.xml, prometheus.yml)  
- **Documentation & Sign‑off** – `./sources/docs/phase5-signoff.md`  

All paths must be absolute to the workspace and prefixed with `./sources/`. No files may be placed directly under the repository root.

## 3. Dedicated Sub-Agent Functional Directives
- **Coder** – Implement integration test scaffolding, security filter beans, tenant‑scoped repositories, performance instrumentation (Micrometer), and finalize Docker multi‑stage builds.  
- **Tester** – Write and execute integration/E2E test suites (API contracts, Kafka streams, UI flows), load‑test scripts, and verify OWASP‑driven security assertions.  
- **Reviewer** – Conduct security code reviews, validate tenant leakage controls, audit JWT handling, and approve Docker images against compliance baselines.  
- **Docker** – Produce optimized multi‑stage Dockerfiles, define `.dockerignore`, and push images to GCP Artifact Registry.  
- **GCP** – Provision GKE cluster, configure IAM roles (`roles/container.admin`, `roles/artifactregistry.admin`), set VPC peering, and enable monitoring/logging APIs.  
- **GKE** – Apply K8s manifests, enforce PodSecurityPolicies, configure Horizontal Pod Autoscaling, and validate service connectivity.  
- **Manager** – Orchestrate cross‑agent hand‑offs, track progress against DoD, generate final sign‑off documentation, and approve production promotion.

## 4. Phase Definition of Done (DoD)
- **Integration** – All integration tests pass (100 % pass rate) covering API endpoints, Kafka topics, and UI workflows.  
- **Security** – OWASP A01‑A07 checks pass; tenant leakage scans return zero findings; JWT signatures verified; PII encrypted; parameterized queries enforced.  
- **Performance** – Load tests meet SLA (< 1 s latency at 1000 RPS); profiling shows no memory leaks; metrics exported to Prometheus.  
- **Deployment** – Docker images built, scanned, and pushed to Artifact Registry; GKE cluster operational with all manifests applied; network policies and pod security standards enforced.  
- **CI/CD** – Automated pipeline runs end‑to‑end from code commit to GKE deployment; artifact promotion approvals recorded.  
- **Sign‑off** – `phase5-signoff.md` completed, reviewed, and approved by Manager, confirming all raw requirements are fully implemented, secured, and deployed.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Establish Integration Test Harness & Security Baseline
#### SUB‑TASK 1.1: Implement Integration Test Configuration & Security Filter Beans
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/config/IntegrationTestConfig.java
    *   **Architectural Requirements:**
        *   Configure Spring Boot Test with Kafka embedded broker for `attendance`, `notifications`, `zalo-message` topics.
        *   Define `TenantSecurityFilter` bean that injects `tenant_id` into request context and enforces multi‑tenant row filtering.
        *   Embed AES‑256 encryption wrapper for PII fields in test data.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/TenantSecurityFilter.java
    *   **Architectural Requirements:**
        *   Implement OWASP A03 (Injection) mitigation via parameterized queries.
        *   Enforce JWT claim validation and lease expiration checks.
        *   Log all tenant‑scope violations for audit.

#### SUB‑TASK 1.2: Write End‑to‑End Integration Test Suite
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/integration.spec.ts
    *   **Architectural Requirements:**
        *   Simulate QR attendance scan, verify Kafka `attendance` event payload, assert student card day decrement.
        *   Validate notification dispatch to Zalo group and FCM push.
        *   Execute role‑based UI navigation for System Admin, Center Admin, Manager, Teacher, Student.
        *   Capture and assert tenant isolation for each role.

### DAY 2: Harden OWASP Controls & Validate Tenant Leakage
#### SUB‑TASK 2.1: Enforce OWASP A01‑A07 Controls in Core Services
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java
    *   **Architectural Requirements:**
        *   Use parameterized queries for all DB access.
        *   Apply AES‑256 encryption for storing attendee PII.
        *   Implement rate‑limiting per tenant using Quarkus JWT tokens.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/JwtSecurityManager.java
    *   **Architectural Requirements:**
        *   Sign JWT with RS256, enforce 15‑minute lease, support revocation list.
        *   Validate audience and issuer per tenant.

#### SUB‑TASK 2.2: Security Review & Tenant Leakage Validation
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/TenantSecurityFilter.java
    *   **Architectural Requirements:**
        *   Verify `tenant_id` is propagated to all downstream service calls.
        *   Confirm no hardcoded tenant values exist.
        *   Validate logging statements strip sensitive data.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/StudentRepository.java
    *   **Architectural Requirements:**
        *   Ensure repository methods include `tenant_id` predicate.
        *   Confirm no `@Query` overrides bypass tenant filter.

### DAY 3: Performance Instrumentation & Load Testing
#### SUB‑TASK 3.1: Instrument Critical Paths with Micrometer
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/config/MetricsConfig.java
    *   **Architectural Requirements:**
        *   Register timers for QR scan processing, notification dispatch, and student card decrement.
        *   Export metrics to Prometheus via `/metrics`.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java
    *   **Architectural Requirements:**
        *   Add `@Timed("qr.attendance")` around attendance logic.
        *   Include histogram for processing latency.

#### SUB‑TASK 3.2: Execute Load & Stress Tests
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AttendanceServiceLoadTest.java
    *   **Architectural Requirements:**
        *   Simulate 1000 concurrent QR scans, assert sub‑second response time.
        *   Verify Kafka backpressure handling and event ordering.
        *   Validate tenant isolation under load (no cross‑tenant data leakage).
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/performance.spec.ts
    *   **Architectural Requirements:**
        *   Run Lighthouse audits on web UI under simulated load.
        *   Measure mobile app cold‑start time and push notification latency.

### DAY 4: Production Docker Build, GKE Deployment & CI/CD Finalization
#### SUB‑TASK 4.1: Build Optimized Multi‑Stage Docker Images
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Stage 1 – Build with Maven (offline mode) producing `membershiphub.jar`.
        *   Stage 2 – Minimal JRE image, copy jar, apply non‑root user, drop privileges.
        *   Include JMX and Prometheus exporter ports.
*   **Target Path:** ./sources/frontend/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Multi‑stage for Next.js build, serve via Nginx, enable HTTP2 and gzip.

#### SUB‑TASK 4.2: Provision GCP Resources & IAM
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/gcp/iam-policy.yaml
    *   **Architectural Requirements:**
        *   Define IAM bindings for `cloudbuild.builder`, `artifactregistry.admin`, `container.admin`, `monitoring.admin`.
        *   Enforce least‑privilege principle per role.
*   **Target Path:** ./sources/gcp/cluster-config.yaml
    *   **Architectural Requirements:**
        *   GKE Autopilot cluster with private nodes, master authorized networks.
        *   Enable Cloud Monitoring, Logging, and Trace APIs.

#### SUB‑TASK 4.3: Deploy to GKE with Security Policies
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/k8s/deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy backend with resource limits, liveness/readiness probes.
        *   Attach PodSecurityPolicy denying privileged containers.
*   **Target Path:** ./sources/backend/k8s/service.yaml
    *   **Architectural Requirements:**
        *   Expose backend via ClusterIP, internal ingress for web UI.
*   **Target Path:** ./sources/frontend/k8s/deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy Next.js web UI with static asset caching.

#### SUB‑TASK 4.4: Finalize CI/CD Pipeline & Sign‑off
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/ci/github/workflows/promote-to-prod.yml
    *   **Architectural Requirements:**
        *   Trigger on manual approval, run Cloud Build to build Docker images, scan with Trivy, promote to Artifact Registry, deploy via kubectl using manifests from `./sources/backend/k8s/`.
*   **Target Path:** ./sources/docs/phase5-signoff.md
    *   **Architectural Requirements:**
        *   Document integration test results, security scan reports, performance metrics, Docker image digests, GKE rollout status.
        *   Include approval signatures from Coder, Tester, Reviewer, Docker, GCP, GKE.