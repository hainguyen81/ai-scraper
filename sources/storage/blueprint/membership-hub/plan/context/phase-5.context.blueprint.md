# PHASE 5 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Phase 5 finalizes the membership-hub platform by executing a comprehensive multi-tenant security audit and deploying the fully integrated application to Google Kubernetes Engine (GKE). The phase focuses on validating tenant isolation, ensuring OWASP A02 compliance for PII encryption at the application layer, and establishing production-grade infrastructure with proper ingress routing and scalability configurations. This phase ensures all functional and non-functional requirements related to security, deployment, and operational readiness are met before go-live.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Security Audit Files:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/` (Java entities, services, repositories)
- **Frontend Security Audit Files:** `./sources/frontend/src/components/`, `./sources/frontend/src/pages/` (React components handling PII)
- **Infrastructure Deployment Files:** `./sources/infra/gke/` (Dockerfiles, Kubernetes manifests, ingress configurations)
- **API Endpoints:** All REST endpoints under `/api/` (e.g., `/api/attendance`, `/api/users`) for multi-tenant leak validation
- **Database Schema Files:** `./sources/backend/src/main/resources/db/migration/` (Flyway/Vert.x schema scripts)

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for coder, tester, reviewer, doc, docker, GKE)
- **reviewer:** Execute static code analysis and security linting on individual Java/TypeScript files to validate tenant isolation and PII encryption. Strictly prohibited from targeting directories.
- **docker:** Author and optimize multi-stage Docker configurations for backend and frontend, ensuring image size compliance (<500 MB).
- **GKE:** Deploy Kubernetes manifests to GKE cluster, configure ingress routing rules, and set up horizontal pod autoscaling (HPA) based on CPU/latency metrics.
- **doc:** Generate technical audit reports and deployment runbooks placed under `./sources/docs/security/` and `./sources/docs/deployment/`.

## 4. Phase Definition of Done (DoD)
- Multi-tenant data leak audit completes with zero critical vulnerabilities detected.
- OWASP A02 validation confirms all PII fields encrypted using AES-256 at application layer.
- GKE deployment successful with all services running, ingress routing operational, and HPA configured.
- Allocated requirements [NFR-002], [EXC-003], [NFR-003], [ARC-005] show 100% test coverage and compliance.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: MULTI-TENANT SECURITY AUDIT & PII ENCRYPTION VALIDATION

#### SUB-TASK 1.1: Execute static code analysis on Java services handling tenant_id scope enforcement
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java`
    *   **Architectural Requirements:**
        *   Validate all database queries include `tenant_id` filter in WHERE clauses.
        *   Ensure no raw SQL concatenation; use only parameterized queries.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-002], [ARC-001]

#### SUB-TASK 1.2: Audit frontend components for PII exposure in API calls
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/src/components/MemberCard.tsx`
    *   **Architectural Requirements:**
        *   Confirm all PII (email, full_name) encrypted before transmission via HTTPS.
        *   Validate no sensitive data stored in browser local storage unencrypted.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [EXC-003]

#### SUB-TASK 1.3: Generate multi-tenant audit report
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/docs/security/multi-tenant-audit-report.md`
    *   **Architectural Requirements:**
        *   Include findings from reviewer tasks with severity ratings.
        *   Document encryption methods used for PII fields.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-002], [NFR-003]

### DAY 2: GKE DEPLOYMENT CONFIGURATION & INGRESS SETUP

#### SUB-TASK 2.1: Create optimized multi-stage Dockerfile for backend
##### Assigned Sub-Agent: docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/infra/gke/backend/Dockerfile`
    *   **Architectural Requirements:**
        *   Use JVM slim base image to keep size <200 MB.
        *   Include health checks and non-root user execution.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-005], [ARC-005]

#### SUB-TASK 2.2: Deploy Kubernetes manifests with HPA configuration
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/infra/gke/production/deployment.yaml`
    *   **Architectural Requirements:**
        *   Configure HPA to scale based on CPU >70% or latency >300 ms.
        *   Set resource limits and requests for all containers.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-004], [ARC-005]

#### SUB-TASK 2.3: Set up ingress routing with TLS termination
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/infra/gke/production/ingress.yaml`
    *   **Architectural Requirements:**
        *   Configure TLS 1.3 with GCP-managed certificates.
        *   Route `/api/*` to backend services and `/*` to frontend.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [NFR-004]