# PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| **Validate & Formalize Requirements** | Consolidate the Vietnamese‑English raw requirements into a traceability matrix, confirm multi‑tenant, QR‑attendance, and multilingual SEO expectations with stakeholders. | Completed matrix signed‑off by Product Owner (PO) and compliance lead. |
| **Define Multi‑Tenant Data & Service Model** | Design the logical data isolation strategy (row‑level security vs schema‑per‑tenant) and outline the Kafka topic topology (one topic per tenant, plus shared audit topic). | Architecture diagram approved; RLS policies documented. |
| **Establish Baseline GCP Project & IAM** | Create a dedicated GCP project “test‑ai‑architecture‑dev”, enable required APIs (GKE, CloudSQL, Artifact Registry, Secret Manager, Pub/Sub for optional Kafka), and provision initial IAM groups (dev‑team, ops‑team, security‑team). | Project created, least‑privilege IAM roles assigned, audit log enabled. |
| **Provision Minimal Infra for PoC** | Deploy a single‑node GKE cluster, a PostgreSQL instance (CloudSQL), and a Kafka broker (Strimzi operator) to host the first Quarkus microservice. | Cluster reachable, DB & Kafka pods healthy, network policies in place. |
| **Build & Publish First Docker Image** | Create a multi‑stage Dockerfile for a “hello‑world” Quarkus service (native or JVM), run Trivy scan, sign with Cosign, and push to Artifact Registry. | Image size ≤ 300 MB, 0 critical CVEs, signature verified. |
| **Set Up CI/CD Skeleton** | Configure GitHub Actions (or Cloud Build) to lint, test (unit), build Docker image, sign, and deploy to the dev GKE cluster using Helm chart placeholders. | Pipeline runs end‑to‑end on every push to `main`. |
| **Establish Governance Guardrails** | Apply OPA Gatekeeper policies for namespace naming, required labels, and disallow privileged containers; enable Binary Authorization in GKE. | Policy enforcement logs show 0 violations. |
| **Document Phase‑1 Deliverables** | Produce a concise Phase‑1 Report (architecture diagram, infra diagram, CI/CD flow, security guardrails, risk register). | Report reviewed and approved by Manager. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Allowed Repository Path | Example Files | Public API Endpoints (PoC) |
|-------|--------------------------|---------------|----------------------------|
| **Infrastructure as Code** | `infra/` | `infra/gke/cluster.yaml`, `infra/kafka/strimzi-operator.yaml`, `infra/postgres/cloudsql.tf` | N/A (IaC only) |
| **Helm Charts / K8s Manifests** | `charts/membership-hub/` | `Chart.yaml`, `values.yaml`, `templates/deployment.yaml`, `templates/service.yaml` | N/A |
| **Quarkus Service (PoC)** | `services/attendance-poc/` | `src/main/java/.../AttendanceResource.java`, `src/main/resources/application.yaml`, `Dockerfile` | `GET /api/v1/ping` (health), `POST /api/v1/attendance` (dummy payload) |
| **CI/CD Pipelines** | `.github/workflows/` or `cloudbuild.yaml` | `ci-build.yml`, `ci-deploy.yml` | N/A |
| **Security Policies** | `policy/opa/` | `gatekeeper/constraints.yaml`, `gatekeeper/templates.yaml` | N/A |
| **Documentation** | `docs/` | `Phase1-Report.md`, `Traceability-Matrix.xlsx` | N/A |

**Endpoint Constraints for Phase 1**  
- Only **internal** endpoints (health, ping, dummy attendance) are exposed.  
- All endpoints must be behind **Istio IngressGateway** with mTLS enforced.  
- Path prefix: `/api/v1/`  

**File‑Change Boundaries**  
- No modifications outside the directories listed above.  
- Front‑end code (`apps/web/`, `apps/mobile/`) is **out‑of‑scope** for Phase 1 and must remain untouched.  

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Primary Tasks (Phase 1) | Deliverables | Acceptance Criteria |
|-----------|--------------------------|--------------|---------------------|
| **Coder** | • Scaffold Quarkus Maven project (`services/attendance-poc`). <br>• Implement `AttendanceResource` with a simple in‑memory counter. <br>• Write `application.yaml` to read DB/Kafka URLs from env vars. <br>• Create multi‑stage Dockerfile (JVM base, optional GraalVM native). <br>• Add Helm chart skeleton (`charts/membership-hub`). | Source code, Dockerfile, Helm chart. | Code compiles, `mvn test` passes, Docker image builds without errors. |
| **Tester** | • Write unit tests for `AttendanceResource` (JUnit5 + RestAssured). <br>• Add contract test (Pact) for the dummy attendance endpoint. <br>• Create CI test job that fails on < 80 % coverage. | Test suite, coverage report. | All tests pass locally; CI reports ≥ 80 % line coverage. |
| **Reviewer** | • Perform security review of Dockerfile (no root user, minimal layers). <br>• Validate OPA policies are applied to the Helm release. <br>• Ensure PR includes documentation updates. | Review comments, approval sign‑off. | No high‑severity findings; PR merged within 12 h of submission. |
| **DevOps (Deployer)** | • Provision GCP project & enable APIs via Terraform (`infra/`). <br>• Deploy GKE cluster (single‑node) with network policies. <br>• Install Strimzi Kafka operator and create a test topic `attendance-test`. <br>• Set up CloudSQL PostgreSQL instance (minimal tier). <br>• Configure GitHub Actions pipeline: lint → test → build → sign → push → Helm upgrade. <br>• Enable Binary Authorization & OPA Gatekeeper. | IaC scripts, CI/CD pipeline, running cluster. | All resources created, pipeline runs end‑to‑end, no policy violations. |
| **Security (optional cross‑cutting)** | • Generate and store service account keys in Secret Manager. <br>• Verify TLS 1.3 on IngressGateway. | Secrets, TLS config. | Secrets accessible only to service accounts; TLS handshake succeeds with TLS 1.3. |

## 4. Phase Definition of Done (DoD)  

- **Documentation**: `docs/Phase1-Report.md` contains architecture diagram, infra diagram, CI/CD flowchart, and risk register; signed off by Manager.  
- **Requirement Traceability**: `docs/Traceability-Matrix.xlsx` maps every raw requirement to a Phase‑1 artifact (e.g., “multi‑tenant DB” → RLS policy doc).  
- **Infrastructure**: GCP project `test‑ai‑architecture‑dev` exists; GKE cluster, CloudSQL, and Kafka are operational; network policies and mTLS enforced.  
- **Code**: Quarkus PoC service builds, passes all unit & contract tests, Docker image ≤ 300 MB, 0 critical CVEs, signed with Cosign, pushed to Artifact Registry.  
- **Deployment**: Helm chart releases `attendance-poc` into `dev` namespace; health endpoint returns 200; Istio ingress reachable via HTTPS with mTLS.  
- **CI/CD**: GitHub Actions pipeline executes on every push, completes all stages (lint, test, build, sign, push, deploy) without failures.  
- **Security Guardrails**: OPA Gatekeeper policies enforced (no privileged containers, required labels present); Binary Authorization rejects unsigned images; audit logs enabled.  
- **Observability**: Prometheus metrics endpoint (`/q/metrics`) exposed; Grafana dashboard stub created; logs forwarded to Cloud Logging.  
- **Stakeholder Sign‑off**: Manager, Security Lead, and Product Owner have reviewed and formally approved the Phase‑1 Report.  

*Only when **all** items above are satisfied does Phase 1 achieve “Done” and the project may advance to Phase 2.*