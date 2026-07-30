# PHASE 5 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Phase 5 executes the final security hardening and production deployment for the membership‑hub platform. It consists of two tightly scoped work‑streams:
- **Security Audit & Encryption Validation (Reviewer):** Perform a comprehensive multi‑tenant leak audit across the source code base, validate OWASP A02 PII application‑layer encryption, and ensure all data‑handling components comply with GDPR/CCPA encryption mandates.
- **Infrastructure Deployment (Docker & GKE):** Build a multi‑stage Docker image that respects size constraints (< 500 MB) and security best‑practices, then deploy the image to Google Kubernetes Engine, configuring Ingress routing with TLS and enforcing the defined RBAC/tenant isolation policies.

The phase delivers a production‑ready, audited, and compliant stack ready for go‑live.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Source Code Audit Scope:** All `.java`, `.ts`, `.py`, `.go` files under `./sources/` (e.g., `./sources/backend/`, `./sources/frontend/`). No files outside `./sources/` may be accessed for audit.
- **Docker Build Scope:** Configuration assets under `./sources/infra/docker/` (e.g., `Dockerfile`, `docker-compose.yml`, build scripts). No root‑level Dockerfiles or CI configs.
- **GKE Deployment Scope:** Kubernetes manifests under `./sources/infra/gke/` (e.g., `deployment.yaml`, `service.yaml`, `ingress.yaml`). No external Helm charts or cloud‑provider plugin files.
- **Endpoint Validation:** The audit must verify REST endpoints defined in `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/controller/` and `./sources/frontend/src/api/` for proper tenant isolation and PII encryption headers.

## 3. Dedicated Sub-Agent Functional Directives
- **Reviewer Agent:** Conducts static code analysis, security linting, and OWASP A02 validation on a single source file. Must enforce multi‑tenant `tenant_id` scoping, verify AES‑256 encryption usage for PII fields, and ensure no hard‑coded credentials or debug statements exist. Output must be a pass/fail report linked to the exact file path.
- **Docker Agent:** Constructs a multi‑stage Docker image that layers build, test, and runtime stages. Must keep base image < 200 MB, final image < 500 MB, include non‑root user, health‑check endpoints, and embed security labels (e.g., `runAsNonRoot:true`). The image is tagged and pushed to the artifact repository.
- **GKE Agent:** Applies Kubernetes manifests from `./sources/infra/gke/` to a GKE cluster, configures Ingress with TLS certificates, sets resource quotas, and validates tenant‑aware RBAC policies. Must ensure all services expose the required REST endpoints and that the cluster meets the 99.9 % availability SLA via node pooling and auto‑healing.

## 4. Phase Definition of Done (DoD)
- **Security Audit Completed:** Zero critical findings; all OWASP A02 controls satisfied; PII encryption verified across the audited file; multi‑tenant leak checks passed.
- **Docker Image Built & Pushed:** Image size < 500 MB; security best‑practices applied; image successfully pushed to registry; image digest recorded.
- **GKE Deployment Live:** All services deployed; Ingress routing rules active; TLS certificates provisioned; cluster health checks passing; tenant isolation confirmed via RBAC; 99.9 % uptime target validated via GKE autoscaling metrics.
- **Compliance Documentation:** Reviewer’s audit report, Docker security scan results, and GKE deployment manifest versions stored under `./sources/` for audit trail.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: SECURITY AUDIT & ENCRYPTION VALIDATION
#### SUB‑TASK 1.1: Conduct OWASP A02 PII encryption validation on the core encryption service
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/PiiEncryptionService.java`
* **Architectural Requirements:**
  * Implement AES‑256 in GCM mode for all PII fields; store keys in a secret manager with rotation policy.
  * Ensure all encryption/decryption calls are wrapped in try‑catch blocks with logging per NFR‑006.
  * Apply multi‑tenant `tenant_id` scoping to encryption keys to isolate data per center.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [NFR-002], [EXC-003]

### DAY 2: INFRASTRUCTURE DEPLOYMENT
#### SUB‑TASK 2.1: Build and push multi‑stage Docker image with security hardening
##### Assigned Sub-Agent: docker
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/docker/Dockerfile`
* **Architectural Requirements:**
  * Use a minimal base image (e.g., `eclipse-temurin:21-jdk-alpine`) for the build stage; copy Maven/Gradle wrapper and source, run tests, package.
  * In the runtime stage, copy only the packaged JAR/WAR and a non‑root user; set `USER=1001`.
  * Include a health‑check endpoint (`/actuator/health`) and enforce `readOnlyRootFilesystem:true`.
  * Generate a SBOM and scan for vulnerabilities; fail build on high‑severity findings.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [NFR-003], [ARC-005]

#### SUB‑TASK 2.2: Deploy to GKE and configure Ingress routing with TLS
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/gke/deployment.yaml`
* **Architectural Requirements:**
  * Apply manifests using `kubectl apply -f ./sources/infra/gke/` targeting the production namespace.
  * Configure Ingress (`./sources/infra/gke/ingress.yaml`) with `tls` block referencing managed certificates for *.membershiphub.com.
  * Enable HPA based on CPU > 70 % and latency > 300 ms per NFR‑004.
  * Validate tenant isolation by checking that each ServiceAccount has `rbac.authorization.k8s.io/role-ref` to the appropriate Center‑Admin role.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [NFR-003], [ARC-005]