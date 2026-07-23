# PHASE 5 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Finalize the membership-hub application by completing end‑to‑end integration between the Java‑Quarkus backend and the Next.js mobile/web frontend, implement comprehensive testing (unit, integration, and E2E), containerize both stacks, provision Google Cloud Platform resources, orchestrate deployment on Google Kubernetes Engine, and achieve a production‑ready, multi‑tenant, multilingual solution ready for go‑live.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Java artifacts** must reside under `./sources/backend/` and follow the package layout `org.nlh4j.saas.membership-hub`.
- **Frontend Next.js artifacts** must reside under `./sources/frontend/`.
- **Container definitions** (`Dockerfile`s) are allowed directly under `./sources/backend/Dockerfile` and `./sources/frontend/Dockerfile`.
- **Configuration & deployment manifests** may be placed under `./sources/backend/src/main/resources/` (e.g., `gcp-config.yml`) or `./sources/frontend/infrastructure/` (e.g., `k8s‑backend.yaml`).
- **Test artifacts** must match the strict tester syntax: `<source path>;<test path>` for unit tests; `INTEGRATION_SCOPE;<e2e test path>` for cross‑component tests.
- **All REST endpoints** are defined in the backend controllers under `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/controller/`.
- **Event‑driven components** (Kafka producers/consumers) reside under `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/event/`.

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE)
- **Coder Agent** – Implement missing integration services, API client utilities, and finalize UI components that bind to backend endpoints. Ensure all new code adheres to the enterprise package mapping and follows Quarkus/Next.js best practices.
- **Tester Agent** – Author and execute unit tests for newly added services/controllers and Playwright/E2E tests for cross‑tenant workflows. Use the semi‑colon syntax for unit test pairs and `INTEGRATION_SCOPE` for integration/E2E suites.
- **Reviewer Agent** – Perform static analysis, verify package‑to‑path compliance, validate Docker and Kubernetes manifests, and confirm that all architectural requirements (security, multi‑tenant isolation, language detection) are satisfied.
- **Docker Agent** – Produce multi‑stage, secure Dockerfiles for backend and frontend, incorporate appropriate build arguments, and embed health‑check probes.
- **GCP Agent** – Provision required GCP services (Cloud SQL, Cloud Storage, IAM service accounts, Pub/Sub topics) using declarative YAML configurations placed under `./sources/backend/src/main/resources/gcp/`.
- **GKE Agent** – Generate Kubernetes Deployment, Service, and Ingress manifests for both backend and frontend, define resource limits, auto‑scaling, and integrate with the CI/CD pipeline.

## 4. Phase Definition of Done (DoD)
- All backend integration services and controllers are implemented, unit‑tested (>90% coverage), and integrated with Kafka event streams.
- Frontend UI components (Dashboard, StudentCard, enrollment flows) are fully functional, multilingual, and connected to REST APIs; UI tests pass.
- Docker images build successfully for both stacks, include security best‑practices, and are pushed to Google Artifact Registry.
- GCP resources (IAM, Cloud SQL, Storage, Pub/Sub) are declared, validated, and ready for GKE consumption.
- GKE manifests are applied, services are reachable via Ingress, and rolling updates are automated.
- End‑to‑end integration and E2E tests execute without failures, covering tenant isolation, role‑based access, QR attendance, notifications, and multilingual SEO.
- Static code review passes, all package‑to‑path mappings are correct, and compliance checklists are signed off.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Consolidate Backend Integration Services
#### SUB‑TASK 1.1: Implement Enrollment & Student Management Services
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/EnrollmentService.java
    *   **Architectural Requirements:**
        *   Implement CRUD operations for student enrollment, linking students to courses and handling payment status.
        *   Emit Kafka events on enrollment creation for downstream notification services.
        *   Ensure transaction boundaries and rollback on payment failure.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/StudentService.java
    *   **Architectural Requirements:**
        *   Provide methods to retrieve student profile, active course list, and remaining validity days.
        *   Support QR‑attendance marking with idempotent daily flag.
        *   Integrate with notification service via event channel.

#### SUB‑TASK 1.2: Create REST Controllers for Student & Enrollment APIs
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/controller/StudentController.java
    *   **Architectural Requirements:**
        *   Expose endpoints: `GET /students/{id}`, `PUT /students/{id}/extend`, `POST /students/{id}/attendance`.
        *   Validate request payloads against defined DTOs.
        *   Return appropriate HTTP status codes and error payloads.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/controller/EnrollmentController.java
    *   **Architectural Requirements:**
        *   Expose endpoints: `POST /enrollments`, `GET /enrollments/{id}`, `DELETE /enrollments/{id}`.
        *   Enforce role‑based access (Admin, Manager, Student).
        *   Emit Kafka event on successful enrollment.

#### SUB‑TASK 1.3: Write Unit Tests for New Services & Controllers
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/EnrollmentService.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/EnrollmentServiceTest.java
    *   **Architectural Requirements:**
        *   Verify enrollment creation, payment validation, and Kafka event emission.
        *   Ensure transaction rollback on payment exception.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/controller/StudentController.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/controller/StudentControllerTest.java
    *   **Architectural Requirements:**
        *   Validate REST endpoint request handling, role‑based security, and QR attendance idempotency.

### DAY 2: Finalize Frontend Integration & UI Components
#### SUB‑TASK 2.1: Build Dashboard Component with Real‑Time Metrics
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/Dashboard.tsx
    *   **Architectural Requirements:**
        *   Display today’s course schedule, active teachers, and enrollment counts.
        *   Integrate with backend `/courses/today` and `/students/count` endpoints.
        *   Implement auto‑refresh every 15 seconds via `setInterval`.
        *   Support multilingual i18n using Next.js `useTranslation`.

#### SUB‑TASK 2.2: Implement StudentCard UI for Validity & Extension
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/StudentCard.tsx
    *   **Architectural Requirements:**
        *   Show student name, remaining validity days, and QR code for attendance.
        *   Provide “Extend” button that calls `/students/{id}/extend` API.
        *   Display toast notifications for success/failure using React‑Toastify.
        *   Respect user locale for date formatting.

#### SUB‑TASK 2.3: Create API Client Utility for Consistent Requests
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/services/api.ts
    *   **Architectural Requirements:**
        *   Centralize base URL and authentication headers.
        *   Export generic `httpGet`, `httpPost`, `httpPut`, `httpDelete` helpers.
        *   Include error handling and automatic token refresh.

#### SUB‑TASK 2.4: Write Playwright E2E Tests for Dashboard & StudentCard
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/dashboard.spec.ts
    *   **Architectural Requirements:**
        *   Navigate to dashboard as Admin, verify course list and metrics.
        *   Log in as Student, inspect StudentCard validity display.
        *   Trigger extension API and confirm UI update.
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/studentCard.spec.ts
    *   **Architectural Requirements:**
        *   Test QR attendance flow via mocked backend.
        *   Validate multilingual locale switching.

### DAY 3: Containerize Backend & Frontend
#### SUB‑TASK 3.1: Create Multi‑Stage Dockerfile for Backend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/Dockerfile
    *   **Architectural Requirements:**
        *   Use `maven:3.9-jdk-21` for building Quarkus app.
        *   Copy `pom.xml`, source, compile, package, then stage in `ubi9/openjdk-21`.
        *   Set JVM flags for optimal memory (`-Xmx512m`).
        *   Include health‑check endpoint `/q/health`.

#### SUB‑TASK 3.2: Create Multi‑Stage Dockerfile for Frontend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/Dockerfile
    *   **Architectural Requirements:**
        *   Use `node:20-alpine` for building Next.js.
        *   Install dependencies, build static assets, serve via `nginx:alpine`.
        *   Copy built output to nginx html directory.
        *   Expose port `3000` and define `nginx -g 'daemon off;'` as entrypoint.

### DAY 4: Provision GCP Resources
#### SUB‑TASK 4.1: Declare IAM Service Accounts & Roles
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/gcp/iam-config.yaml
    *   **Architectural Requirements:**
        *   Define service account `membership-hub-sa` with roles `CloudSQLAdmin`, `StorageObjectViewer`, `Pub/SubAdmin`.
        *   Attach least‑privilege policies for each tenant namespace.
        *   Include annotation for workload identity mapping to GKE service account.

#### SUB‑TASK 4.2: Define Cloud SQL Instance & Database Schema
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/gcp/cloudsql-instance.yaml
    *   **Architectural Requirements:**
        *   Provision a PostgreSQL instance with `pg_repack` extension enabled.
        *   Set automatic backups, point‑in‑time recovery, and private IP.
        *   Tag instance with project `membership-hub` and environment `prod`.

#### SUB‑TASK 4.3: Create Pub/Sub Topics for Event Streaming
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/gcp/pubsub-topics.yaml
    *   **Architectural Requirements:**
        *   Declare topics `enrollment-events`, `attendance-events`, `notification-events`.
        *   Set retention policy of 7 days, enable message ordering where needed.

### DAY 5: Deploy to GKE
#### SUB‑TASK 5.1: Generate Kubernetes Deployments for Backend
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/infrastructure/k8s/backend-deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy container image `gcr.io/<project>/membership-hub-backend:latest`.
        *   Use 2 replicas, resource limits `cpu: 500m, memory: 1Gi`.
        *   Mount Cloud SQL proxy sidecar with secret for DB credentials.
        *   Define environment variables for Kafka bootstrap servers and GCP project.

#### SUB‑TASK 5.2: Generate Kubernetes Deployments for Frontend
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/infrastructure/k8s/frontend-deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy container image `gcr.io/<project>/membership-hub-frontend:latest`.
        *   Use 3 replicas, resource limits `cpu: 250m, memory: 512Mi`.
        *   Expose port `3000`, configure liveness and readiness probes.
        *   Include ConfigMap for Next.js environment variables (e.g., API base URL).

#### SUB‑TASK 5.3: Create Ingress & Service Definitions
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/infrastructure/k8s/ingress.yaml
    *   **Architectural Requirements:**
        *   Define Ingress `membership-hub-ingress` with TLS enabled.
        *   Path prefixes: `/api/*` → backend service, `/*` → frontend service.
        *   Set `nginx.ingress.kubernetes.io/rate-limit` to 100r/s per IP.
*   **Target Path:** ./sources/frontend/infrastructure/k8s/backend-service.yaml
    *   **Architectural Requirements:**
        *   ClusterIP service exposing backend on port `8080`.
        *   Add `sessionAffinity` to stick HTTP sessions to same node.
*   **Target Path:** ./sources/frontend/infrastructure/k8s/frontend-service.yaml
    *   **Architectural Requirements:**
        *   ClusterIP service exposing frontend on port `80`.

### DAY 6: Execute Integration & E2E Test Suite
#### SUB‑TASK 6.1: Run Backend Unit Tests
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/EnrollmentService.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/EnrollmentServiceTest.java
    *   **Architectural Requirements:**
        *   Verify all test cases pass, coverage >90%.
        *   Ensure Kafka event mocking validates event payload schema.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/controller/StudentController.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/controller/StudentControllerTest.java
    *   **Architectural Requirements:**
        *   Validate role‑based access control logic.
        *   Confirm QR attendance idempotency.

#### SUB‑TASK 6.2: Run Frontend Unit Tests (React)
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/Dashboard.tsx;./sources/frontend/tests/components/Dashboard.test.tsx
    *   **Architectural Requirements:**
        *   Test rendering of metrics, mock API calls, and i18n locale switching.
*   **Target Path:** ./sources/frontend/src/components/StudentCard.tsx;./sources/frontend/tests/components/StudentCard.test.tsx
    *   **Architectural Requirements:**
        *   Verify extension button triggers correct API call.
        *   Validate QR code generation and copy to clipboard.

#### SUB‑TASK 6.3: Execute Cross‑Component Integration & E2E Tests
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts
    *   **Architectural Requirements:**
        *   Simulate login as System Admin, Admin, Manager, Teacher, Student.
        *   Verify navigation permissions and UI elements per role.
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/enrollmentFlow.spec.ts
    *   **Architectural Requirements:**
        *   End‑to‑end test: Admin creates course, Manager assigns student, Student enrolls, attendance marked via QR, notification sent to mobile app.
        *   Validate data persistence in Cloud SQL via backend assertions.
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/multilingual.spec.ts
    *   **Architectural Requirements:**
        *   Switch locale, confirm UI strings, SEO meta tags, and hreflang links.

### DAY 7: Final Review & Sign‑off
#### SUB‑TASK 7.1: Static Code Analysis & Package Compliance
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/EnrollmentService.java
    *   **Architectural Requirements:**
        *   Verify package declaration matches `org.nlh4j.saas.membership-hub`.
        *   Check for unused imports, potential security vulnerabilities.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/controller/StudentController.java
    *   **Architectural Requirements:**
        *   Ensure all REST endpoints follow RESTful conventions.
        *   Validate input validation annotations (e.g., `@NotNull`).
*   **Target Path:** ./sources/frontend/src/components/Dashboard.tsx
    *   **Architectural Requirements:**
        *   Confirm component naming follows PascalCase.
        *   Verify prop types are defined and used correctly.
*   **Target Path:** ./sources/frontend/src/components/StudentCard.tsx
    *   **Architectural Requirements:**
        *   Check accessibility attributes (aria‑labels) for screen readers.
        *   Ensure i18n keys are consistent across files.

#### SUB‑TASK 7.2: Docker & Kubernetes Manifest Validation
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/Dockerfile
    *   **Architectural Requirements:**
        *   Confirm multi‑stage build reduces final image size (< 150 MB).
        *   Validate that non‑root user is used for runtime.
*   **Target Path:** ./sources/frontend/Dockerfile
    *   **Architectural Requirements:**
        *   Ensure Node.js build dependencies are removed in final stage.
        *   Verify health‑check endpoint is correctly defined.
*   **Target Path:** ./sources/frontend/infrastructure/k8s/backend-deployment.yaml
    *   **Architectural Requirements:**
        *   Validate resource requests/limits are set.
        *   Ensure liveness/readiness probes have correct paths.
*   **Target Path:** ./sources/frontend/infrastructure/k8s/ingress.yaml
    *   **Architectural Requirements:**
        *   Confirm TLS secret reference exists.
        *   Verify path rules route traffic to correct services.

#### SUB‑TASK 7.3: GCP Resource Verification
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/gcp/iam-config.yaml
    *   **Architectural Requirements:**
        *   Ensure service account keys are not hardcoded.
        *   Validate role assignments align with principle of least privilege.
*   **Target Path:** ./sources/backend/src/main/resources/gcp/cloudsql-instance.yaml
    *   **Architectural Requirements:**
        *   Confirm private IP is set and no public access is enabled.
        *   Verify backup configuration includes daily snapshots.
*   **Target Path:** ./sources/backend/src/main/resources/gcp/pubsub-topics.yaml
    *   **Architectural Requirements:**
        *   Ensure topics are created in the correct GCP project and region.
        *   Validate retention policy matches data retention requirements.

#### SUB‑TASK 7.4: End‑to‑End Test Summary & Sign‑off
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts
    *   **Architectural Requirements:**
        *   Review test logs for any authentication bypass attempts.
        *   Confirm all role‑based UI restrictions are enforced.
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/enrollmentFlow.spec.ts
    *   **Architectural Requirements:**
        *   Validate that QR attendance is idempotent across multiple scans.
        *   Ensure notification events are emitted to Pub/Sub and received by mock listener.
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/multilingual.spec.ts
    *   **Architectural Requirements:**
        *   Verify hreflang tags are correctly set in HTML `<head>`.
        *   Confirm SEO metadata is present for each language variant.

**Phase 5 Complete.** All deliverables are finalized, tested, and ready for production deployment.