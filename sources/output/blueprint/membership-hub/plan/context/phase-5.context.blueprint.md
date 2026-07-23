# PHASE 5 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- **Cross-System Integration (Manager):** Establish end‑to‑end data flow and request routing across all microservices (user, course, notification), frontend, and mobile components. Implement tenant‑aware context propagation, health‑check orchestration, and integration test scripts to validate functional consistency.
- **Performance Profiling (Reviewer):** Deploy a lightweight profiling utility that captures response latency, memory consumption, and thread metrics across all services. Configure thresholds, export data to monitoring (Prometheus), and enforce OWASP security hardening (parameterized queries, input validation, AES‑256 PII encryption, multi‑tenant isolation).
- **Production Deployment (GKE):** Containerize the backend services, create Docker images, and publish them to GCR. Define Kubernetes Deployments, Services, Autoscaling, and CI/CD pipelines in GitHub Actions. Deploy to GKE, run validation scripts, and ensure zero‑downtime rollout with rollback capability.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Java Services (under `./sources/backend/`):**
  - `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` – all domain, security, integration, monitoring, and repository components.
  - `./sources/backend/src/main/resources/` – configuration (integration‑flow.yml, profiling‑config.yml, application‑properties).
  - `./sources/backend/src/test/` – unit/integration test suites (if any).
  - `./sources/backend/docker/` – Dockerfile(s) for each service.
  - `./sources/backend/kubernetes/` – GKE Deployment, Service, Autoscaling, and ConfigMap manifests.
  - `./sources/backend/scripts/` – deployment, validation, and integration test orchestration scripts.
- **Frontend (under `./sources/frontend/`):** Not directly modified in Phase 5; existing Next.js/React assets remain unchanged.
- **CI/CD (under `./sources/backend/.github/workflows/`):** Deploy‑to‑GKE pipeline YAML.
- **Security Scan Reports:** `./sources/backend/security/` – OWASP scan report JSON.
- **REST/GraphQL Endpoint Patterns (allowed for integration verification):**
  - `POST /api/v1/auth/login`
  - `GET /api/v1/users/{tenantId}/{userId}`
  - `POST /api/v1/courses`
  - `GET /api/v1/courses/{tenantId}`
  - `POST /api/v1/notifications`
  - `GET /api/v1/health`
  - `GET /api/v1/metrics` (Prometheus endpoint)

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE, Manager)
- **Manager Agent:** Lead cross‑system integration orchestration, define tenant‑aware routing, create integration flow configuration, health‑check services, and integration test scripts. Ensure all integration points enforce multi‑tenant `tenant_id` scopes and secure context propagation.
- **Reviewer Agent:** Implement performance profiling utilities, configure monitoring thresholds, conduct OWASP security verification (scan for injection, XSS, CSRF, insecure deserialization), and apply security hardening (parameterized queries, input validation, AES‑256 encryption for PII, tenant isolation). Generate a security‑scan report and profiling metrics.
- **GKE Agent:** Build Docker images (`Dockerfile`), define Kubernetes manifests (Deployments, Services, Autoscaling, ConfigMaps), create CI/CD pipeline (`.github/workflows/deploy-to-gke.yml`), execute deployment to GKE, run validation scripts, and manage rollback procedures.

## 4. Phase Definition of Done (DoD)
- **Integration:** All cross‑system workflows validated via integration scripts; health‑check endpoints return `200 OK` for each service; tenant isolation verified; no functional regression.
- **Performance:** Profiling utility captures metrics; average response time ≤ 200 ms for critical endpoints; memory usage stable; profiling thresholds met; metrics exported to Prometheus and viewable.
- **Security:** OWASP scan passes with zero high‑severity findings; security‑scan report generated; all components enforce parameterized queries, input validation, AES‑256 encryption for PII, and multi‑tenant scopes; security hardening applied.
- **Deployment:** Docker images built and pushed to GCR; Kubernetes Deployments rolled out with zero‑downtime; Autoscaling configured; CI/CD pipeline executes successfully; validation scripts confirm service availability; rollback capability tested.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Establish Integration Orchestration and Container Images
#### SUB‑TASK 1.1: Create Integration Orchestrator Component
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/integration/IntegrationOrchestrator.java
    *   **Architectural Requirements:**
        *   Implement a singleton service that coordinates calls between user, course, and notification microservices.
        *   Inject tenant‑aware `tenant_id` context into each outbound request.
        *   Use reactive HTTP clients for non‑blocking integration.
        *   **OWASP Compliance:** Ensure all inter‑service calls use parameterized payloads and validate incoming data against a schema to prevent injection attacks.

#### SUB‑TASK 1.2: Build Backend Docker Image
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker/Dockerfile
    *   **Architectural Requirements:**
        *   Base image: `eclipse-temurin:17-jdk-alpine`.
        *   Copy compiled JAR (`target/*.jar`) to `/app/app.jar`.
        *   Set JVM flags for container memory limits.
        *   Expose port `8080`.
        *   Define entrypoint to run Quarkus via `java -jar /app/app.jar`.

#### SUB‑TASK 1.3: Define GKE Deployment Manifest
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/kubernetes/gke-deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy the backend as a Deployment with 3 replicas.
        *   Use the Docker image built in SUB‑TASK 1.2.
        *   Mount ConfigMap for external properties.
        *   Configure liveness and readiness probes (`/api/v1/health`).
        *   Enforce resource limits (CPU 250m, Memory 512Mi) and autoscaling policies.

### DAY 2: Deploy Integration Flow Config and Implement Profiling Utility
#### SUB‑TASK 2.1: Define Integration Flow Configuration
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/integration-flow.yml
    *   **Architectural Requirements:**
        *   Declare service endpoints, retry policies, and timeout values.
        *   Specify tenant isolation rules (header `X-Tenant-ID` propagation).
        *   Document data transformation mappings for user, course, and notification payloads.

#### SUB‑TASK 2.2: Implement Performance Profiler Utility
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/monitoring/PerformanceProfiler.java
    *   **Architectural Requirements:**
        *   Capture JVM metrics (GC time, thread count), HTTP response times, and custom business metrics.
        *   Export metrics via Prometheus `CollectorRegistry`.
        *   **OWASP Compliance:** Ensure profiler does not log sensitive data; sanitize any collected request attributes.
    *   **Security Enforcement:**
        *   Apply AES‑256 encryption for any persisted metric snapshots.
        *   Enforce role‑based access for profiler endpoints (`/api/v1/metrics` only accessible by `SysAdmin`).

#### SUB‑TASK 2.3: Configure Profiling Thresholds
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/profiling-config.yml
    *   **Architectural Requirements:**
        *   Define alert thresholds (e.g., response time > 500 ms, memory usage > 80 % of limit).
        *   Set export interval (30 seconds) and Prometheus endpoint (`http://prometheus:9090`).
    *   **OWASP Compliance:** Validate configuration file content to prevent injection of malicious YAML scripts.

### DAY 3: Health‑Check Services and Deployment Automation
#### SUB‑TASK 3.1: Create Health‑Check Service
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/integration/HealthCheckService.java
    *   **Architectural Requirements:**
        *   Expose `/api/v1/health` endpoint returning status of each downstream service.
        *   Perform tenant‑scoped checks using the `tenant_id` from request headers.
        *   Return structured JSON with overall status and per‑service details.
    *   **Security Enforcement:** Ensure health endpoint does not leak internal stack traces; return generic status codes.

#### SUB‑TASK 3.2: Define Docker Compose for Local Validation
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/docker-compose.yml
    *   **Architectural Requirements:**
        *   Define services for backend, PostgreSQL, Kafka, and Prometheus.
        *   Use environment variables for configuration (e.g., `TENANT_ID`).
        *   Ensure network isolation for backend service.

#### SUB‑TASK 3.3: Configure GKE Autoscaling
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/kubernetes/autoscaling.yaml
    *   **Architectural Requirements:**
        *   Define Horizontal Pod Autoscaler targeting CPU utilization > 70 %.
        *   Set minimum replicas to 2, maximum to 10.
        *   Bind autoscaler to the backend Deployment.

### DAY 4: Security Hardening and OWASP Verification
#### SUB‑TASK 4.1: Implement Tenant‑Aware Routing Filter
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/TenantRoutingFilter.java
    *   **Architectural Requirements:**
        *   Intercept all inbound requests, extract `X-Tenant-ID` header.
        *   Validate tenant existence and assign to security context.
        *   Propagate tenant ID to downstream service calls.
    *   **OWASP Compliance:** Sanitize tenant ID input (alphanumeric only) to prevent injection.

#### SUB‑TASK 4.2: Conduct OWASP Security Scan and Generate Report
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/security/owasp-scan-report.json
    *   **Architectural Requirements:**
        *   Run static analysis (SonarQube) and dependency check (OWASP Dependency‑Check).
        *   Capture findings, severity levels, and remediation suggestions.
    *   **OWASP Compliance:** Ensure scan includes checks for A01:2021‑Broken Access Control, A03:2021‑Injection, A07:2021‑Identification and Authentication Failures.
    *   **Security Enforcement:** Apply fixes for high‑severity issues (e.g., replace string concatenation with prepared statements, enforce password complexity).

#### SUB‑TASK 4.3: Create Secure Repository Component
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/SecureUserRepository.java
    *   **Architectural Requirements:**
        *   Use Spring Data JPA with `@Query` annotations employing named parameters.
        *   Implement method-level `@PreAuthorize("hasRole('ADMIN')")` for sensitive operations.
        *   Encrypt PII fields at rest using AES‑256 with a tenant‑specific key.
    *   **OWASP Compliance:** All queries are parameterized; no dynamic SQL concatenation.

### DAY 5: Final Integration Validation and Production Deployment
#### SUB‑TASK 5.1: Execute End‑to‑End Integration Test Suite
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/scripts/integration-test.sh
    *   **Architectural Requirements:**
        *   Invoke the IntegrationOrchestrator to simulate a full user‑course‑notification flow.
        *   Validate data consistency across services using health‑check endpoints.
        *   Assert tenant isolation by running parallel requests with different `X-Tenant-ID`s.
    *   **Security Enforcement:** Ensure test script does not expose credentials; use environment variables for secrets.

#### SUB‑TASK 5.2: Deploy to GKE via CI/CD Pipeline
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/.github/workflows/deploy-to-gke.yml
    *   **Architectural Requirements:**
        *   Trigger on `main` branch push.
        *   Build Docker image, push to GCR.
        *   Apply Kubernetes manifests (`gke-deployment.yaml`, `autoscaling.yaml`).
        *   Wait for rollout status and perform health‑check verification.
    *   **Security Enforcement:** Use workload identity for GKE service account; restrict pipeline permissions to required resources.

#### SUB‑TASK 5.3: Validate Deployment and Execute Rollback if Needed
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/scripts/validate-deployment.sh
    *   **Architectural Requirements:**
        *   Query GKE deployment status (`kubectl get deployment backend`).
        *   Hit `/api/v1/health` and `/api/v1/metrics` endpoints; verify HTTP 200 and expected metric patterns.
        *   If any check fails, trigger rollback to previous stable version (`kubectl rollout undo deployment/backend`).
    *   **Security Enforcement:** Log validation results to a secure audit bucket; ensure scripts run with least‑privilege service account.