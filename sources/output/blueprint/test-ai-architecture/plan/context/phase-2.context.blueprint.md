# PHASE 2 CONTEXT BLUEPRINT: test‑ai‑architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Indicator |
|-----------|-------------|--------------------|
| **Authentication Service** | Implement a unified identity layer that supports: <br>• Native email + password (hashed with Argon2) <br>• Firebase Auth federation <br>• Google & Facebook OIDC federation <br>All users (internal staff & learners) are represented in a single `users` table with a `tenant_id` discriminator. | Successful login via any provider; JWT access token issued with `tenant_id` claim. |
| **Tenant‑Aware Core Backend** | Build the first Quarkus microservice **membership‑service** that exposes: <br>• Attendance‑record API (idempotent daily check‑in) <br>• Membership‑day calculation endpoint (remaining days) <br>All data scoped by `tenant_id` using PostgreSQL Row‑Level Security (RLS). | 100 % of API calls respect tenant isolation; unit‑test coverage ≥ 80 %. |
| **Event‑Driven Pipeline** | Define Kafka topics and producers/consumers for: <br>• `attendance.events` (check‑in events) <br>• `notification.events` (down‑stream to Zalo & FCM) <br>Ensure exactly‑once semantics via idempotent keys. | No duplicate attendance records; consumer lag < 5 seconds in staging. |
| **Docker & CI/CD Foundations** | Create a multi‑stage Dockerfile that builds a **GraalVM native image** of the Quarkus service, pushes to Artifact Registry, and is referenced by the Helm chart. Integrate into GitHub Actions → Cloud Build → Argo CD pipeline. | Native image ≤ 150 MB; CI pipeline passes all static analysis, SAST, container scan, and auto‑deploys to `dev` namespace. |
| **Observability & Guardrail Hooks** | Instrument the service with OpenTelemetry (metrics, traces) and emit structured logs (JSON) to Cloud Logging. Add runtime checks for GDPR consent flag on every user‑related request. | Traces visible in Cloud Trace; alerts fire on missing consent flag. |
| **Phase Gate Deliverables** | • Architecture diagram of auth & attendance flow <br>• Terraform module for Kafka & PostgreSQL <br>• Helm chart values for `membership-service` <br>• API contract (OpenAPI 3.0) <br>• Test suite (unit + contract) | All artifacts stored in the `phase‑2/` folder and pass review. |

---

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

```
/infra
│   ├─ terraform/
│   │   ├─ main.tf                # GKE cluster, VPC, CloudSQL, Kafka (Confluent) resources
│   │   ├─ variables.tf
│   │   └─ outputs.tf
│   └─ helm/
│       └─ membership-service/
│           ├─ Chart.yaml
│           ├─ values.yaml
│           └─ templates/
│               ├─ deployment.yaml
│               ├─ service.yaml
│               └─ configmap.yaml
/src
│   └─ membership-service/
│       ├─ src/main/java/com/company/membership/
│       │   ├─ Application.java                     # Quarkus entry point
│       │   ├─ config/
│       │   │   └─ JwtConfig.java
│       │   ├─ model/
│       │   │   ├─ User.java
│       │   │   ├─ Attendance.java
│       │   │   └─ Tenant.java
│       │   ├─ repository/
│       │   │   ├─ UserRepository.java
│       │   │   └─ AttendanceRepository.java
│       │   ├─ service/
│       │   │   ├─ AuthService.java
│       │   │   ├─ AttendanceService.java
│       │   │   └─ MembershipCalcService.java
│       │   ├─ resource/
│       │   │   ├─ AuthResource.java                # /api/v1/auth/*
│       │   │   ├─ AttendanceResource.java         # /api/v1/attendance/*
│       │   │   └─ MembershipResource.java         # /api/v1/membership/*
│       │   └─ kafka/
│       │       ├─ AttendanceProducer.java
│       │       └─ NotificationConsumer.java
│       └─ src/main/resources/
│           ├─ application.properties               # Quarkus config (dev)
│           ├─ application-prod.yaml                # Prod overrides
│           └─ META-INF/
│               └─ openapi.yaml                     # OpenAPI spec
/docker
│   └─ Dockerfile                                 # Multi‑stage GraalVM native build
/.github
│   └─ workflows/
│       └─ ci.yml                                 # Lint, unit, contract, SAST, Trivy, Build & Push
/ops
    └─ argo/
        └─ app.yaml                               # Argo CD Application manifest
```

### Public REST Endpoints (base `/api/v1/`)  

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| `POST` | `/auth/login` | Email/password login → returns JWT | Public |
| `POST` | `/auth/firebase` | Firebase ID token exchange → JWT | Public |
| `GET`  | `/auth/providers` | List enabled OIDC providers (Google, Facebook) | Public |
| `POST` | `/attendance/checkin` | Idempotent daily QR check‑in (payload: `{ "qrToken": "...", "tenantId": "..." }`) | Bearer JWT |
| `GET`  | `/attendance/today` | Returns today’s attendance status for caller | Bearer JWT |
| `GET`  | `/membership/remaining` | Returns remaining membership days for caller | Bearer JWT |
| `GET`  | `/healthz` | Liveness/Readiness probe | Public |

### Kafka Topics (namespace `membership-hub`)  

| Topic | Purpose | Key | Value Schema |
|-------|---------|-----|--------------|
| `attendance.events` | Publish each successful check‑in | `{tenantId}:{userId}:{date}` | `{ "userId": "...", "tenantId": "...", "date": "YYYY-MM-DD", "qrToken": "..."}`
| `notification.events` | Down‑stream for Zalo & FCM notifications | `{tenantId}:{userId}` | `{ "userId": "...", "tenantId": "...", "type": "CHECKIN", "payload": {...} }`

---

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Primary Tasks (Phase 2) | Artefacts to Produce | Guardrail Checks |
|-----------|--------------------------|----------------------|------------------|
| **Coder** | • Scaffold Quarkus project with Maven (Java 17). <br>• Implement `AuthService` (email/password, Firebase token exchange, OIDC redirects). <br>• Implement `AttendanceService` with idempotent check‑in logic (use Redis cache or DB unique constraint). <br>• Add `MembershipCalcService` that decrements remaining days based on attendance history. <br>• Write OpenAPI annotations for all endpoints. <br>• Add PostgreSQL RLS policies (`tenant_id` filter) and migration scripts (Flyway). | - Source code under `/src/membership-service/` <br>- Flyway SQL files under `src/main/resources/db/migration/` <br>- OpenAPI spec (`openapi.yaml`) | • Static analysis (SonarQube ≥ A) <br>• Dependency check (OWASP Dependency‑Check) <br>• No hard‑coded secrets (use `${SECRET}` placeholders) |
| **Tester** | • Unit tests for Auth, Attendance, Membership services (JUnit 5 + Mockito). <br>• Contract tests using **Karate** against the generated OpenAPI spec. <br>• Integration test that spins up an in‑memory Kafka (Testcontainers) and PostgreSQL, verifies idempotent check‑in and event publishing. <br>• Security test: ensure JWT without `tenant_id` claim is rejected. | - `src/test/java/...` with ≥ 80 % coverage reports (JaCoCo). <br>- `contract/attendance.feature` & `contract/auth.feature`. | • Test coverage threshold enforced in CI <br>• OWASP ZAP baseline scan on the running dev service (no high‑risk findings) |
| **Reviewer** | • Review PRs for code style (Google Java Format), architectural compliance (tenant isolation, GDPR consent check). <br>• Validate OpenAPI spec matches implementation (diff tool). <br>• Approve Terraform changes only after `terraform validate` and `plan` review. <br>• Ensure Dockerfile passes `hadolint` and final image size ≤ 150 MB. | - Review comments on GitHub PRs <br>- Signed off checklist (Guardrail‑Compliance‑Checklist.md) | • No critical findings after static analysis <br>• All required CI checks (SAST, container scan) must be green before merge |
| **DevOps (Deployer)** | • Write Terraform module for GKE, CloudSQL (PostgreSQL), and Confluent‑Kafka (or GKE‑based Strimzi). <br>• Create Helm chart values for resource limits, Istio sidecar injection, and secret references (Google Secret Manager). <br>• Extend GitHub Actions workflow: <br>   1. Lint → Test → Build native image → Push to Artifact Registry. <br>   2. Run `helm lint` and `helm template` sanity check. <br>   3. Deploy to `dev` namespace via Argo CD (auto‑sync). <br>• Configure OpenTelemetry exporter to Cloud Trace & Metrics. | - Terraform files under `/infra/terraform/` <br>- Helm chart under `/infra/helm/membership-service/` <br>- GitHub Actions workflow `.github/workflows/ci.yml` | • `terraform fmt` & `terraform validate` pass <br>• Helm chart passes `helm lint` <br>• Deployment health checks (`/healthz`) succeed > 99 % of pods within 2 min |
| **Docker** *(optional sub‑agent if split)* | • Author multi‑stage Dockerfile: <br>   `FROM quay.io/quarkus/ubi-quarkus-maven:22.3-java17 AS build` → native compile <br>   `FROM registry.access.redhat.com/ubi8/ubi-minimal` → copy native binary. <br>• Run `hadolint` and `docker buildx` for multi‑arch (linux/amd64, linux/arm64). | - `Dockerfile` in `/docker/` <br>- Build logs archived as CI artifacts | • Final image ≤ 150 MB, CVE scan (Trivy) reports no critical vulnerabilities |

---

## 4. Phase Definition of Done (DoD)  

The Phase 2 gate is considered **passed** only when **all** items below are satisfied:

1. **Functional Completeness**  
   - All REST endpoints listed in Section 2 are implemented, documented, and return the expected HTTP status codes.  
   - Attendance check‑in is idempotent (multiple identical QR scans on the same day do not create duplicate rows).  
   - Membership‑day calculation correctly reflects days remaining after each successful check‑in.  

2. **Tenant & Privacy Guardrails**  
   - PostgreSQL RLS policies enforce `tenant_id` isolation for every table (`users`, `attendance`, `membership`).  
   - Every request that accesses personal data validates the user’s GDPR consent flag; missing consent results in `403 Forbidden`.  

3. **Event‑Driven Reliability**  
   - Kafka topics `attendance.events` and `notification.events` exist with correct replication factor (≥ 3).  
   - Producer publishes with exactly‑once semantics; consumer acknowledges only after successful DB transaction.  

4. **Quality Metrics**  
   - Unit test coverage ≥ 80 % (JaCoCo).  
   - Contract test suite passes against the generated OpenAPI spec.  
   - Static analysis (SonarQube) score ≥ A, no blocker issues.  
   - Container image size ≤ 150 MB, Trivy scan reports **no critical** CVEs.  

5. **CI/CD & Deployability**  
   - GitHub Actions pipeline runs end‑to‑end without manual intervention and reaches the **Deploy to Dev** stage.  
   - Helm chart installs cleanly on a fresh GKE namespace (`membership-hub-dev`).  
   - All pods report `Ready` and pass `/healthz` within 2 minutes of rollout.  

6. **Observability & Monitoring**  
   - OpenTelemetry traces appear in Cloud Trace for at least one request per endpoint.  
   - Metrics (request count, latency, Kafka consumer lag) are visible in Cloud Monitoring dashboards.  

7. **Documentation & Knowledge Transfer**  
   - Architecture diagram (PlantUML or Lucidchart) uploaded to Confluence and linked in the repo README.  
   - README contains: build instructions, local dev setup (Docker Compose with Kafka & Postgres), and how to run the test suite.  
   - Runbook for “Attendance Check‑in Failure” and “Kafka Consumer Lag Alert” added to `/ops/runbooks/`.  

8. **Phase Gate Review Sign‑off**  
   - Manager and Reviewer have signed the **Phase 2 Gate Checklist** (stored as `phase