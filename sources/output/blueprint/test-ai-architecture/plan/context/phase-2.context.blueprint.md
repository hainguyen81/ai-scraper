# PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture  

## 1. Phase Operational Scope & Objectives  

| Aspect | Description |
|--------|-------------|
| **Phase Goal** | Deliver the **Core Backend & Identity Service** that enables tenant‑aware authentication, user provisioning, JWT issuance, and the first version of the attendance API (QR‑scan entry point). |
| **Business Value** | - Allows administrators and learners to log in via internal email/password **or** federated providers (Firebase, Google, Facebook). <br> - Provides a secure, multi‑tenant identity layer that will be reused by every front‑end (web portal & mobile app). <br> - Exposes a **RESTful attendance endpoint** that records a daily attendance event, updates the learner’s remaining membership days, and publishes an immutable event to Kafka for downstream notification pipelines. |
| **Key Deliverables** | 1. **Firebase‑Auth Bridge Service** – a Quarkus micro‑service that validates Firebase ID tokens, maps them to internal user records, and issues signed JWTs containing tenant, role, and scope claims. <br>2. **User Management Service** – CRUD APIs for internal users (email/password) with password hashing (bcrypt‑scrypt), password reset flow, and role‑based access control. <br>3. **Attendance Service** – idempotent `POST /api/v1/attendance/scan` that: <br>   - Accepts QR payload (tenantId, learnerId, timestamp). <br>   - Checks/creates a daily attendance record (one per learner per day). <br>   - Decrements the learner’s remaining membership days atomically. <br>   - Emits an `attendance.recorded` event to a **tenant‑scoped Kafka topic**. <br>4. **Database Schema** – PostgreSQL with **row‑level security (RLS)** and a **tenant_id** column on every table; migration scripts (Flyway). <br>5. **Infrastructure as Code** – Terraform modules for GKE namespace, ServiceAccount, CloudSQL instance, and Kafka (Strimzi) deployment. <br>6. **CI/CD pipeline** – GitHub Actions workflow that builds a **multi‑stage Docker image**, runs static analysis (SonarQube, Trivy), signs the image (Cosign), pushes to Artifact Registry, and triggers a Helm upgrade to a **dev** GKE cluster. |
| **Success Metrics** | - **Authentication latency** ≤ 120 ms (JWT issuance). <br> - **Attendance API latency** ≤ 200 ms (including DB transaction). <br> - **Unit / contract test coverage** ≥ 80 % for new services. <br> - **Zero critical CVEs** in produced container images. <br> - **OPA policy compliance** passes 100 % of automated checks. |
| **Stakeholder Review** | End of Phase 2 a **Phase Review** demo is presented to the Manager, Security Officer, and Product Owner. Acceptance criteria are captured in the **Phase Definition of Done** (see §4). |

---

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Repository Path | Allowed Files / Artifacts | Public Endpoints (base URL = `https://api.<project>.example.com`) |
|-------|-----------------|---------------------------|---------------------------------------------------------------|
| **Auth Bridge** | `services/auth-bridge/` | `src/main/java/**`, `src/main/resources/application.yaml`, `Dockerfile`, `pom.xml`, `src/test/**` | `POST /auth/token` – exchange Firebase ID token for internal JWT <br> `GET /auth/me` – introspect JWT (protected) |
| **User Management** | `services/user-service/` | Same structure as above. | `POST /api/v1/users` – create internal user (admin only) <br> `GET /api/v1/users/{id}` – read <br> `PUT /api/v1/users/{id}` – update <br> `DELETE /api/v1/users/{id}` – delete |
| **Attendance** | `services/attendance-service/` | Same structure as above. | `POST /api/v1/attendance/scan` – QR scan payload (tenantId, learnerId, qrHash, timestamp) |
| **Database Migrations** | `infra/db/migrations/` | Flyway SQL scripts (`V1__init.sql`, `V2__add_user_table.sql`, …) | N/A (executed on CloudSQL startup) |
| **Kafka Topics** | `infra/kafka/` | Helm values for Strimzi, topic definitions (`attendance-<tenantId>`). | N/A (internal) |
| **Terraform IaC** | `infra/terraform/` | `main.tf`, `variables.tf`, `outputs.tf`, module directories (`gke/`, `cloudsql/`, `kafka/`). | N/A |
| **CI/CD** | `.github/workflows/` | `ci.yml`, `cd.yml` (build, scan, sign, deploy). | N/A |
| **Security Policies** | `infra/opa/` | Rego files (`auth.rego`, `tenant_isolation.rego`). | N/A |

> **Boundary Rules**  
> - No code may be added outside the listed service directories.  
> - Front‑end (Next.js / React Native) is **out of scope** for Phase 2 and must not be modified.  
> - All new endpoints must be versioned under `/api/v1/` and must include the `X-Tenant-ID` header (validated by OPA).  

---

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Primary Tasks (specific to Phase 2) | Acceptance Artifacts |
|-----------|--------------------------------------|----------------------|
| **Coder** | 1. Implement **Firebase‑Auth Bridge**: verify Firebase token via Google SDK, map to internal `users` table, generate signed JWT (RS256) with claims `sub`, `tenant_id`, `roles`, `scopes`. <br>2. Build **User Service**: password hashing (bcrypt‑scrypt), email verification flow, role‑based CRUD endpoints, RLS policies in PostgreSQL. <br>3. Develop **Attendance Service**: idempotent scan handling, atomic decrement of `membership_days`, Kafka producer (`attendance.recorded`). <br>4. Write Flyway migrations for all new tables and RLS policies. <br>5. Create Dockerfiles (multi‑stage, GraalVM native optional) and Helm charts (`auth-bridge`, `user-service`, `attendance-service`). | - Pull request with compiled code, unit tests, and successful `mvn verify`. <br> - Docker image pushed to Artifact Registry (tagged `dev-<commit>`). |
| **Tester** | 1. Unit tests for each service (JUnit + Mockito). <br>2. Contract tests using **Pact** for JWT issuance and attendance event schema. <br>3. Integration tests with Testcontainers: spin up PostgreSQL + Kafka, run end‑to‑end flow (auth → attendance). <br>4. Security tests: verify OPA denies requests missing `X‑Tenant‑ID` or with wrong scopes. <br>5. Load test script (k6) to simulate 200 concurrent QR scans and assert < 200 ms latency. | - `target/pact` contracts published to Pact broker. <br> - CI pipeline reports ≥ 80 % coverage and all tests passing. |
| **Reviewer** | 1. Perform **static code analysis** (SonarQube) and ensure no blocker issues. <br>2. Review PRs for **security** (JWT signing, password storage, SQL injection protection). <br>3. Validate **OPA policies** are enforced (run `opa test`). <br>4. Confirm **Terraform** plan matches architecture diagram and does not create stray resources. | - Signed-off PRs with review comments resolved. <br> - SonarQube quality gate passed. |
| **DevOps (Deployer)** | 1. Author Terraform modules to provision GKE namespace `membership-hub-dev`, CloudSQL instance, and Strimzi Kafka operator. <br>2. Configure **Secret Manager** entries for DB credentials, JWT private key, Firebase service account. <br>3. Set up **GitHub Actions** workflow: lint → unit → build → Trivy scan → Cosign sign → push → Helm upgrade. <br>4. Implement **ArgoCD** Application manifests for continuous delivery to the dev cluster. <br>5. Create Prometheus ServiceMonitors for the three services and expose `/metrics`. | - Terraform `apply` completes without drift. <br> - CI/CD pipeline runs end‑to‑end on every push to `feature/phase2-*`. <br> - Services reachable via the defined endpoints and return 200 health checks. |

---

## 4. Phase Definition of Done (DoD)  

The Phase 2 is considered **Done** when **all** items below are satisfied and signed off by the **Manager** during the Phase Review:

1. **Functional**  
   - Auth Bridge issues a valid JWT for any Firebase ID token and for internal email/password login.  
   - User Service supports full CRUD with role‑based access (admin vs. learner).  
   - Attendance Service records exactly one attendance per learner per calendar day, updates `membership_days` atomically, and publishes a correctly‑structured Kafka event.  

2. **Non‑Functional**  
   - Average response latency ≤ 120 ms (auth) and ≤ 200 ms (attendance) under 200 concurrent users (k6 test).  
   - Unit + integration test coverage ≥ 80 % and all CI checks (SonarQube, Trivy, OPA) pass.  
   - Docker images are ≤ 150 MB (native) or ≤ 300 MB (JVM) and have **0 critical** CVEs.  
   - Images are signed with **Cosign** and stored in Artifact Registry.  

3. **Security & Compliance**  
   - All inbound traffic to services uses **mTLS** (Istio) and JWT verification.  
   - PostgreSQL RLS enforces tenant isolation; attempts to access another tenant’s data are blocked (verified via integration test).  
   - OPA Gatekeeper policies are deployed and enforced on the dev namespace.  

4. **Infrastructure**  
   - Terraform state is stored remotely (GCS bucket) and locked via DynamoDB‑style lock (GCS object lock).  
   - GKE namespace, ServiceAccounts, and Secrets are provisioned exactly as defined in `infra/terraform/`.  
   - Helm releases are at version `0.2.0` (or higher) and show **READY** status for all three services.  

5. **Observability**  
   - `/metrics` endpoint exposed and scraped by Prometheus; Grafana dashboard shows request latency, error rate, and Kafka lag.  
   - OpenTelemetry instrumentation emits traces that appear in the Jaeger UI for a sample QR‑scan flow.  

6. **Documentation**  
   - API specification (OpenAPI 3.0) for all new endpoints committed to `docs/openapi/`.  
   - README in each service directory with build, run, and local testing instructions.  
   - Architecture decision record (ADR) documenting the choice of JWT claim design and idempotent attendance handling.  

7. **Sign‑off**  
   - Manager records **Phase Review** minutes, attaches the signed checklist, and updates the project roadmap to move to Phase 3.  

*Only after every bullet above is verified will the project be allowed to progress to Phase 3 (Front‑end & QR Attendance Flow).*