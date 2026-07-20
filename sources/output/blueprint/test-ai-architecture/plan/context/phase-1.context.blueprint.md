# PHASE 1 CONTEXT BLUEPRINT: test‑ai‑architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| **Validate Core Business Assumptions** | Confirm that the QR‑attendance flow, multi‑center data model, and omni‑channel notification pipeline can be realized with the chosen stack (Quarkus, Kafka, PostgreSQL, GKE). | PoC records a single attendance per learner per day, decrements remaining membership days, and enqueues a notification message. |
| **Define Bounded‑Contexts & Domain Model** | Produce a Context‑Map (Domain‑Driven Design) that isolates **Learner**, **Center**, **Attendance**, **Membership**, **Notification**, and **Auth** contexts. | Reviewed diagram approved by Manager & Reviewer. |
| **Prototype Critical Path** | Build a minimal end‑to‑end prototype: <br>1. **Auth** (email + password) → JWT <br>2. **QR Scan** (simulated HTTP call) → **Attendance Service** writes to PostgreSQL and publishes to Kafka <br>3. **Notification Service** consumes Kafka, calls a stub Zalo API and a mock FCM endpoint. | Automated integration test passes: attendance persisted once per day, membership days decremented, notification payload emitted. |
| **Establish Security & Compliance Foundations** | Demonstrate TLS everywhere, secret‑less configuration (Secret Manager), and basic OPA policy for API gateway. | No plaintext secrets in repo; `curl -k https://...` succeeds with valid cert; OPA gate denies unauthenticated request. |
| **Set Up CI/CD Skeleton** | GitHub Actions workflow that builds a **Quarkus** native image (optional GraalVM), runs unit tests, builds a Docker image, scans with Trivy, and pushes to Artifact Registry. | Workflow passes on every push to `main`. |
| **Document Architecture Decisions** | ADRs for **Event Streaming**, **Multi‑Tenant DB**, **i18n detection**, and **Container Image Strategy**. | ADRs stored in `docs/adr/` and linked from the README. |

> **Gate‑Go/No‑Go** – At the end of Phase 1 the Manager, Reviewer, and Tester jointly sign‑off if **all** success metrics are met and the Global Guardrails (Section 2 of the Global Context) are satisfied.

---

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Allowed Repository Path | Example Files | Public API Endpoints (prototype) |
|------|--------------------------|---------------|-----------------------------------|
| **Auth Service** | `services/auth/` | `src/main/java/.../AuthResource.java`, `src/main/resources/application.yml` | `POST /api/v1/auth/login` (email/password) <br> `POST /api/v1/auth/firebase` (token exchange) |
| **Attendance Service** | `services/attendance/` | `AttendanceResource.java`, `AttendanceProcessor.java`, `src/main/resources/application.yml` | `POST /api/v1/attendance/scan` (payload: `{ learnerId, qrCode, timestamp }`) |
| **Notification Service** | `services/notification/` | `NotificationConsumer.java`, `ZaloClientStub.java`, `FCMClientStub.java` | **No public HTTP** – consumes Kafka topic `attendance.events`. |
| **Domain Model (shared)** | `libs/domain/` | `Learner.java`, `Center.java`, `Membership.java`, `Attendance.java` | – |
| **Infrastructure as Code** | `infra/helm/` | `auth/values.yaml`, `attendance/values.yaml`, `notification/values.yaml` | – |
| **CI/CD** | `.github/workflows/` | `ci-build.yml`, `ci-security.yml` | – |
| **Documentation & ADRs** | `docs/` | `adr/001-event-streaming.md`, `architecture-overview.md` | – |
| **Mock External APIs** | `mocks/` | `zalo-mock/`, `fcm-mock/` (simple Express servers) | `POST /mock/zalo/send` <br> `POST /mock/fcm/push` |

**Endpoint Security** – All HTTP endpoints must require a valid **Bearer JWT** signed by the Auth Service’s private key. The JWT must contain a `role` claim (`ADMIN`, `STAFF`, `LEARNER`).  

**Network Boundaries** –  
* Services run in the same GKE namespace `phase1‑sandbox`.  
* Kafka broker reachable only via internal ClusterIP service `kafka-svc`.  
* Mock APIs exposed via `NodePort` **only** on the CI runner network (not internet‑facing).  

**File‑level Guardrails** –  
* No `.env` or secret files committed.  
* All configuration values that are secrets must be referenced via `${SM://path/to/secret}` (Secret Manager placeholder).  

---

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Concrete Tasks for Phase 1 | Deliverables (artifact path) | Acceptance Criteria |
|-----------|----------------------------|------------------------------|---------------------|
| **Coder** | 1. Scaffold Quarkus Maven modules for `auth`, `attendance`, `notification`. <br>2. Implement JWT generation & verification (Auth). <br>3. Create PostgreSQL schema (Flyway scripts) for `learners`, `centers`, `memberships`, `attendance_logs`. <br>4. Wire Attendance Service to publish `AttendanceRecorded` events to Kafka. <br>5. Build Dockerfiles (multi‑stage, non‑root user) for each service. | `services/auth/`, `services/attendance/`, `services/notification/`, `infra/helm/`, `db/migrations/V1__init.sql` | Unit tests ≥ 80 % coverage; Docker images build locally without errors; `docker run` starts and health‑checks succeed. |
| **Tester** | 1. Write JUnit tests for Auth login flow and Attendance idempotency. <br>2. Create Postman collection for the three public endpoints. <br>3. Develop an integration test (using Testcontainers) that spins up PostgreSQL + Kafka, runs a full scan → attendance → notification flow. <br>4. Execute OWASP Dependency‑Check on the Maven dependencies. | `services/**/src/test/java/`, `test/postman/attendance.postman_collection.json` | All tests pass on CI; integration test asserts exactly one `attendance_logs` row per learner per day; Dependency‑Check reports no CVE > 7.0. |
| **Reviewer** | 1. Validate that all Dockerfiles use a minimal base (e.g., `gcr.io/distroless/java17`). <br>2. Ensure OpenAPI spec (`openapi.yaml`) matches implemented endpoints and includes JWT security scheme. <br>3. Verify OPA policy file (`policy/auth.rego`) denies requests without `Authorization` header. <br>4. Review ADRs for completeness and rationale. | `docs/openapi.yaml`, `policy/auth.rego`, `docs/adr/` | No critical style violations; OPA policy passes `opa eval` test suite; ADRs signed off in PR comments. |
| **DevOps (Docker / Deployer)** | 1. Configure GitHub Actions workflow `ci-build.yml` to: <br>   - Run `mvn clean verify` <br>   - Build native image (optional) <br>   - Build Docker image, tag with `${{ github.sha }}` <br>   - Scan with Trivy, fail on HIGH+ vulnerabilities <br>   - Push to Artifact Registry `asia-south1-docker.pkg.dev/<project>/phase1-sandbox/<service>` <br>2. Create a minimal Helm chart (`infra/helm/attendance/Chart.yaml`) with values for image repository, replicaCount=1, resource limits. <br>3. Deploy the three services to a **GKE Autopilot** cluster in a temporary `phase1‑sandbox` namespace using `helm upgrade --install`. <br>4. Set up a basic Prometheus scrape config for the services (via ServiceMonitor). | `.github/workflows/ci-build.yml`, `infra/helm/attendance/`, `k8s/monitoring/prometheus.yaml` | CI pipeline passes on every push; Helm release reports `STATUS: deployed`; Pods run as non‑root; Prometheus metrics endpoint returns 200. |
| **Security (optional sub‑agent)** | 1. Generate self‑signed TLS certs for local dev and store them in Secret Manager placeholders. <br>2. Add `Istio` sidecar injection annotation to the namespace (for later phases). | `infra/istio/namespace.yaml` | `kubectl get namespace phase1-sandbox -o yaml` shows `istio-injection: enabled`. |

*All sub‑agents must log their daily progress in the shared Confluence page `Phase 1 – Discovery & Architecture Validation` and update the Kanban board in Jira (Epic **PH1‑DISCOVERY**).*

---

## 4. Phase Definition of Done (DoD)  

The Phase 1 increment is considered **Done** when **all** of the following conditions are satisfied:

1. **Functional PoC**  
   * A learner can authenticate via email/password and receive a signed JWT.  
   * A QR‑scan request (POST `/api/v1/attendance/scan`) creates **exactly one** attendance record for the day, decrements the learner’s `remaining_days`, and publishes an `AttendanceRecorded` event to Kafka.  
   * The Notification Service consumes the event and successfully calls both mock Zalo and mock FCM endpoints (verified by logs).  

2. **Architecture Artefacts**  
   * Context‑Map diagram (`docs/architecture/context-map.png`).  
   * ADRs for Event Streaming, Multi‑Tenant DB, i18n detection, and Container Image Strategy stored under `docs/adr/`.  

3. **Code Quality & Security**  
   * Unit test coverage ≥ 80 % for new code.  
   * No **critical** or **high** vulnerabilities reported by Trivy or OWASP Dependency‑Check.  
   * All secrets referenced via Secret Manager placeholders; no plaintext secrets in repo.  

4. **CI/CD Pipeline**  
   * GitHub Actions workflow `ci-build.yml` runs on every push to `main` and completes all stages (build, test, scan, push).  
   * Docker images are published to Artifact Registry with immutable digests.  

5. **Infrastructure Deployment**  
   * Helm releases for `auth`, `attendance`, and `notification` are deployed to GKE `phase1‑sandbox` namespace and report `READY` status.  
   * Pods run as non‑root, use the minimal Distroless base image, and expose health‑check endpoints (`/q/health`).  

6. **Observability & Logging**  
   * Prometheus scrapes `/metrics` from each service; a Grafana dashboard (`docs/grafana/phase1-dashboard.json`) shows request latency and error rate.  
   * All request/response logs are shipped to Cloud Logging with appropriate labels (`service=attendance`).  

7. **Compliance Gate**  
   * Reviewer signs off that the implementation adheres to every Guardrail in **Section 2 – Global Guardrails & Enterprise Compliance Standards** (data encryption, RBAC, audit logging, etc.).  

8. **Stakeholder Sign‑off**  
   * Manager, Reviewer, and Tester collectively approve the Phase 1 deliverables in Jira (transition to **Done**).  

Once the above DoD checklist is fully satisfied, the team may proceed to **Phase 2 – Core Platform Build (MVP)**.