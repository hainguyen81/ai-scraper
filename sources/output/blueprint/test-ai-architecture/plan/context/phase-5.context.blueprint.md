# PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
- **Deploy** the Quarkus‑based backend (including Kafka connectors and PostgreSQL persistence) and the Next.js‑based mobile/web front‑end to Google Cloud Platform.
- **Containerize** all services with Docker, push images to Google Artifact Registry, and orchestrate them on a GKE cluster using Helm/Kustomize.
- **Configure** GKE networking (Ingress, Service‑Mesh if required), autoscaling policies, resource quotas, and IAM roles to meet security, GDPR/CCPA compliance, and high‑availability requirements.
- **Implement** comprehensive monitoring (Prometheus + Grafana) and centralized logging (Google Cloud Logging / Stackdriver) for both backend and frontend components.
- **Validate** end‑to‑end functionality, load‑testing, and security controls; ensure observability dashboards are operational and alert policies are defined.
- **Document** deployment procedures, monitoring dashboards, and run‑books for ongoing operations.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Path | Purpose | Example Files / Endpoints |
|------|---------|---------------------------|
| `backend/` | Quarkus source code, Kafka producers/consumers, JPA entities | `src/main/java/com/membership/…`, `src/main/resources/application.yml` |
| `frontend/` | Next.js web & mobile UI (including i18n) | `pages/…`, `components/…`, `next.config.js` |
| `docker/` | Dockerfile(s) for backend & frontend | `backend/Dockerfile`, `frontend/Dockerfile` |
| `k8s/` | Kubernetes manifests (Helm charts or Kustomize overlays) | `k8s/backend-deployment.yaml`, `k8s/frontend-ingress.yaml` |
| `monitoring/` | Prometheus configs, Grafana dashboards, alert rules | `monitoring/prometheus.yml`, `monitoring/dashboards/...` |
| `scripts/` | CI/CD pipelines (Cloud Build), deployment scripts, rollback procedures | `scripts/deploy.sh`, `scripts/ci.yaml` |
| `docs/` | Deployment run‑books, architecture diagrams, compliance checklists | `docs/DEPLOYMENT.md`, `docs/SECURITY.md` |
| `tests/` | Integration, load, and security test suites for deployment validation | `tests/deployment.test.js`, `tests/performance.jmx` |

*Only the directories above may be referenced or modified during Phase 5. No additional source trees or external repositories may be introduced.*

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)

### Coder
- **Containerization**: Write and optimize Dockerfiles for backend (`docker/backend/Dockerfile`) and frontend (`docker/frontend/Dockerfile`), ensuring multi‑stage builds, minimal image size, and proper health‑check endpoints.
- **Artifact Push**: Configure `gcloud builds submit` or GitHub Actions to build images, tag them with `gcr.io/<project>/<service>:<tag>`, and push to Google Artifact Registry.
- **Configuration**: Update `application.yml` (or equivalent) with GKE‑specific externalized properties (e.g., Kafka bootstrap servers, DB connection URLs) using Secret Manager references.
- **Code Cleanup**: Remove any local debugging stubs, ensure all external dependencies are declared, and commit final source to the repository.

### DevOps
- **Cluster Setup**: Provision a GKE Autopilot (or Standard) cluster, enable Network Policy, and install the necessary add‑ons (Secret Manager CSI driver, Cloud NAT, Cloud DNS).
- **Helm/Kustomize**: Deploy Helm charts (or Kustomize overlays) from `k8s/`:
  - Backend deployment with autoscaling (`k8s/backend-deployment.yaml`).
  - Frontend ingress with TLS (`k8s/frontend-ingress.yaml`).
  - Kafka and PostgreSQL operator installations (if using managed services).
- **CI/CD Integration**: Create a Cloud Build pipeline (`scripts/ci.yaml`) that triggers on `main` branch, runs unit tests, builds Docker images, pushes to Artifact Registry, and executes the `scripts/deploy.sh` rollout.
- **Monitoring Stack**: Deploy Prometheus operator and Grafana via Helm, import pre‑built dashboards from `monitoring/`, and configure data sources to scrape backend (`/actuator/metrics`) and frontend metrics.
- **Logging**: Enable Google Cloud Logging agent on nodes, configure log routing policies to export backend logs, and set up structured JSON logging in Quarkus.
- **Security & Compliance**:
  - Apply Pod Security Policies (or Pod Security Standards) to enforce least‑privilege.
  - Bind IAM Service Accounts to pods using Workload Identity.
  - Validate GDPR/CCPA data‑handling (e.g., encryption at rest, audit logs) via automated checks.
- **Rollback & Disaster Recovery**: Document `scripts/rollback.sh` and test a simulated failure/recovery within the 7‑day window.

### Tester
- **Smoke Tests**: Execute Postman/Newman scripts against deployed REST endpoints (e.g., `/api/members`, `/api/attendance/qr`) to confirm basic functionality.
- **Integration Tests**: Run Kafka connector verification (produce/consume) and PostgreSQL data integrity checks using test containers.
- **Load & Performance Tests**: Use k6 or JMeter to simulate concurrent attendance scans and user logins; assert response times < 200 ms for critical paths.
- **Security Tests**: Perform OWASP ZAP scans on the web UI, validate authentication flows (email/password, Firebase/Google/Facebook), and confirm that sensitive fields are not exposed in logs.
- **Monitoring Validation**: Verify that Prometheus scrapes metrics (`/actuator/metrics`, custom Kafka metrics) and that Grafana dashboards display real‑time data; test alert firing for error thresholds.
- **Compliance Checks**: Run automated tools (e.g., `grep -R "password"` in code, check for plaintext secrets) to ensure GDPR/CCPA adherence.

### Reviewer
- **Code & Manifest Review**: Conduct pairwise reviews of Dockerfile optimizations, Helm values, and Kubernetes manifests for best‑practice compliance (resource limits, liveness probes, anti‑ARP table abuse).
- **Security Review**: Validate IAM policies, Secret Manager usage, encryption keys, and ensure no hardcoded credentials exist.
- **Documentation Review**: Verify that `docs/DEPLOYMENT.md` and `docs/SECURITY.md` are up‑to‑date, include run‑books, and reference correct artifact repositories.
- **Compliance Sign‑off**: Approve that all GDPR/CCPA controls (data minimization, consent logging, data retention) are satisfied before final go‑live.

### Manager (Phase‑level oversight)
- **Progress Tracking**: Update the project board (e.g., Jira) with daily status for each sub‑agent, ensuring no phase exceeds 7 days.
- **Risk Mitigation**: Identify and log any blockers (e.g., missing Artifact Registry permissions, GKE quota limits) and coordinate resolution with DevOps.
- **Stakeholder Communication**: Provide a concise Phase‑5 completion brief to executives, highlighting deployment health, monitoring readiness, and compliance status.

## 4. Phase Definition of Done (DoD)
- **All artifacts** (Docker images, Helm charts, monitoring configs) are built, tagged, and pushed to Google Artifact Registry.
- **GKE cluster** is operational with all required services (backend, frontend, Kafka, PostgreSQL) running and reachable via Ingress.
- **Health‑check endpoints** (`/actuator/health`, custom frontend health) return `200 OK` for at least three consecutive minutes.
- **Autoscaling** policies are active (CPU, memory, custom Kafka lag metrics) and validated under load.
- **Monitoring** stack is live: Prometheus scrapes metrics, Grafana dashboards display real‑time data, and alert rules fire correctly for errors and latency.
- **Logging** is centralized: all application logs appear in Google Cloud Logging with structured fields; audit logs capture authentication events.
- **Security & compliance** are verified:
  - No plaintext secrets in repositories.
  - IAM and Pod Security policies enforce least‑privilege.
  - GDPR/CCPA controls (encryption, consent logging, data retention) are documented and tested.
- **Testing** is complete:
  - Smoke, integration, load, and security tests pass.
  - All test reports are archived in the CI/CD artifact store.
- **Documentation** is finalized:
  - `docs/DEPLOYMENT.md` and `docs/SECURITY.md` are updated and reviewed.
  - Run‑books and rollback procedures are stored in `docs/` and validated via a simulated rollback.
- **Project closure**: Phase‑5 status is marked **Complete** in the project tracker, with a formal sign‑off from Manager, DevOps, and Security Reviewer.