# PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture  

## 1. Phase Operational Scope & Objectives  

| Goal | Description | Success Indicator |
|------|-------------|--------------------|
| **Requirement Validation & Traceability** | Capture all functional & non‑functional requirements from the Raw Requirements and map them to the Global Context. Produce a Requirement Traceability Matrix (RTM). | RTM approved by **Manager**; 100 % coverage of listed requirements. |
| **Multi‑Tenant Data Model Definition** | Design the logical schema that isolates each learning center (`tenant_id`) and supports user‑type segregation (internal admin vs. external federated). Include Row‑Level Security (RLS) policies for PostgreSQL. | Entity‑Relationship diagram + RLS policy scripts reviewed and signed‑off. |
| **High‑Level Architecture Blueprint** | Produce a system‑context diagram and component diagram covering: Quarkus services, Kafka topics, PostgreSQL, Keycloak/Firebase, Next.js web & mobile, GKE deployment topology, and external Zalo Business API. | Architecture diagram stored in the repository; Reviewer confirms alignment with Global Guardrails. |
| **Baseline Infrastructure as Code (IaC)** | Scaffold Terraform modules for: <br>• GCP VPC, subnets, IAM service accounts <br>• GKE cluster (regional, multi‑zone) <br>• CloudSQL (PostgreSQL) with TimescaleDB extension <br>• Secret Manager integration <br>Provide a `main.tf` that can be applied in a **dev** environment. | `terraform init && terraform apply -var env=dev` succeeds without errors; no policy violations from Checkov. |
| **CI/CD Skeleton** | Create GitHub Actions workflow that performs: <br>1️⃣ Lint (prettier/ESLint, hadolint) <br>2️⃣ Unit test placeholder <br>3️⃣ Build a **multi‑stage Dockerfile** (Quarkus native image) <br>4️⃣ Push image to Artifact Registry <br>5️⃣ Deploy Helm chart to the **dev** namespace via Argo CD (GitOps). | Pipeline runs end‑to‑end on a fresh commit; all jobs pass; Argo CD shows a healthy sync. |
| **Guardrail Integration** | Embed automated checks for: <br>• OWASP Top 10 (via ZAP baseline scan) <br>• Secret leakage (Trivy) <br>• Terraform policy compliance (Checkov) <br>• Code quality gate (SonarQube). | Any violation fails the pipeline; alerts sent to Slack channel. |
| **Documentation Foundations** | Populate Confluence (or Markdown repo) with: <br>• Project charter <br>• Glossary of tenant‑related terms <br>• On‑boarding guide for new developers (local dev setup). | Documentation reviewed and approved; links added to repository README. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Area | Allowed Files / Paths | Prohibited / Out‑of‑Scope (Phase 1) |
|------|----------------------|--------------------------------------|
| **Terraform IaC** | `infra/terraform/` <br>• `main.tf` <br>• `variables.tf` <br>• `outputs.tf` <br>• `modules/**` (vpc, gke, cloudsql) | Production‑only modules, cross‑region replication configs. |
| **Kubernetes Manifests** | `infra/helm/` <br>• `Chart.yaml` <br>• `values-dev.yaml` (dev namespace) <br>• `templates/**` (deployment, service, ingress) | `values-prod.yaml` or any `namespace: prod` definitions. |
| **CI/CD Pipelines** | `.github/workflows/ci-cd.yml` <br>• `scripts/lint.sh`, `scripts/build.sh` | Separate release pipelines for canary/blue‑green (out‑of‑scope). |
| **Docker** | `docker/Dockerfile.quarkus` (multi‑stage) <br>• `docker/.dockerignore` | Dockerfiles for auxiliary services (e.g., Zalo connector) – to be added in later phases. |
| **Architecture Docs** | `docs/architecture/` <br>• `high‑level-arch.md` <br>• `tenant‑model.md` <br>• `rtm.xlsx` | Detailed API spec (OpenAPI) – scheduled for Phase 2. |
| **Source Code (placeholder)** | `src/` (empty packages for now) – only to host **README** and **package.json** for future Next.js code. | Any actual business logic implementation (attendance, auth) – belongs to Phase 2. |
| **API Endpoints (design only)** | Documented in `docs/api/phase1-endpoints.md` (e.g., `/health`, `/ready`, `/api/v1/tenant/{id}` placeholder). | Real endpoint implementations; they will be coded in Phase 2. |
| **Testing Artifacts** | `tests/unit/` (empty) <br>• `tests/integration/` (empty) | Performance / load testing scripts – scheduled for Phase 5. |

**Network / Service Endpoint Constraints (dev environment)**  

| Service | Hostname (dev) | Port | Protocol |
|---------|----------------|------|----------|
| GKE Ingress (API) | `api.dev.test-ai-architecture.internal` | 443 | HTTPS (mTLS enforced by Istio) |
| PostgreSQL (CloudSQL) | `postgres-dev.test-ai-architecture.internal` | 5432 | TLS |
| Kafka (Confluent) | `kafka-dev.test-ai-architecture.internal` | 9092 | TLS |
| Keycloak | `auth.dev.test-ai-architecture.internal` | 8443 | HTTPS |
| Zalo Mock (later) | N/A | N/A | N/A |

Only the above hostnames may be referenced in Terraform or Helm values for Phase 1.

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Concrete Tasks (Phase 1) | Deliverable(s) | Acceptance Criteria |
|-----------|--------------------------|----------------|---------------------|
| **Manager** | • Conduct kickoff meeting with stakeholders (Vietnamese & English). <br>• Approve RTM and Architecture Blueprint. | Meeting minutes, signed RTM, approved architecture diagram. | All stakeholders sign‑off; no open comments > 48 h. |
| **Coder** | • Scaffold the repository structure (`infra/`, `docker/`, `src/`, `docs/`). <br>• Write Terraform modules for VPC, GKE, CloudSQL. <br>• Draft Helm chart skeleton (Chart.yaml, values‑dev.yaml, basic Deployment/Service). <br>• Create placeholder Quarkus project (`pom.xml`) with no code (just to generate native image). | Git commits with clear messages, PR opened for review. | `terraform validate` passes; `helm lint` passes; Dockerfile builds locally. |
| **Tester** | • Define test plan for Phase 1 (infrastructure validation, CI pipeline health). <br>• Implement automated smoke tests: <br> - `curl https://api.dev.../health` returns 200. <br> - Terraform plan produces expected resources. <br>• Set up ZAP baseline scan against the dev ingress. | `tests/smoke/health_test.sh`, `tests/security/zap-baseline.sh`, test plan markdown. | All smoke tests run in CI and succeed; ZAP report contains **0** high/critical findings. |
| **Reviewer** | • Perform code review on Terraform, Helm, Dockerfile, CI workflow. <br>• Run static analysis tools (Checkov, hadolint, SonarQube) and verify no blocker issues. <br>• Validate that all Guardrails (GDPR, Zero‑Trust, RLS placeholders) are documented. | Review comments resolved, approval label on PR. | No “Changes Requested” after final review; all automated policy checks green. |
| **DevOps (Docker & Deployer combined)** | • Write multi‑stage Dockerfile that compiles Quarkus to a GraalVM native image and copies only the binary to the final stage (scratch). <br>• Configure GitHub Action to push the image to **Artifact Registry** (`asia-south1-docker.pkg.dev/.../membership-hub`). <br>• Set up Argo CD Application manifest pointing to the Helm chart in the repo, targeting the `dev` namespace. | `docker/Dockerfile.quarkus`, CI workflow step `build-and-push`, `argocd-app.yaml`. | Image size ≤ 150 MB; Argo CD shows **Synced** and **Healthy** after pipeline run. |
| **Security (cross‑cutting)** | • Integrate Trivy scan in CI after image build. <br>• Add secret scanning step (GitHub secret scanning). | CI job `security-scan.yml`. | Pipeline fails on any CVE > 7 days old or any hard‑coded secret. |

All agents must tag their work with the Phase 1 label (`phase-1`) and reference the issue tracker ticket `PH1-001`.

## 4. Phase Definition of Done (DoD)  

The Phase 1 is considered **Done** when **all** of the following conditions are met:

1. **Documentation**  
   - Requirement Traceability Matrix (RTM) completed and approved.  
   - High‑level architecture diagram and tenant data‑model diagram stored in `docs/architecture/`.  
   - README contains clear onboarding steps for local development (Terraform, Docker, CI).  

2. **Infrastructure**  
   - Terraform `dev` environment can be provisioned from scratch (`terraform apply -var env=dev`) with **0** errors.  
   - GKE cluster, CloudSQL instance, and IAM service accounts are created in the **dev** GCP project.  
   - Row‑Level Security policies are defined (even if not yet enforced by code).  

3. **CI/CD Pipeline**  
   - GitHub Actions workflow runs automatically on every push to `main`.  
   - Lint, unit‑test placeholder, Docker build, Trivy scan, ZAP baseline, Terraform validate, Helm lint, and Argo CD sync steps all **pass**.  
   - Image is stored in Artifact Registry and deployed to the `dev` namespace via Argo CD with **Healthy** status.  

4. **Guardrail Compliance**  
   - All automated policy checks (Checkov, SonarQube, Trivy, ZAP) report **no** blocker findings.  
   - No secrets are present in the repository (verified by secret‑scan).  

5. **Testing**  
   - Smoke tests for `/health` and `/ready` endpoints succeed in the deployed dev environment.  
   - Security baseline scan reports **0** high/critical issues.  

6. **Review & Sign‑off**  
   - All PRs related to Phase 1 have **Approved** reviews from at least one **Reviewer** and one **Security** reviewer.  
   - **Manager** signs off on the Phase Gate Review checklist (attached as `docs/phase-gate/PH1-gate.md`).  

7. **Readiness for Phase 2**  
   - Repository tags the commit with `v0.1.0-alpha` and creates a GitHub Release draft.  
   - Backlog items for Phase 2 (core backend, identity service) are created in the project board and linked to the Phase 1 release.  

When the above criteria are satisfied, the Phase 1 team may merge the final `main` branch, promote the Helm chart to the **staging** environment, and schedule the Phase 2 kickoff.