# PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
- **Deploy** the Quarkus‑Kafka‑Postgres backend and Next.js mobile/web frontend to **Google Cloud Platform (GCP) – GKE** using Docker containers.  
- **Configure** a production‑grade Kubernetes environment (namespaces, Ingress, Service‑Mesh if needed) with **horizontal pod autoscaling**, **liveness/readiness probes**, and **network policies** for security.  
- **Implement** comprehensive **monitoring & logging** (Prometheus + Grafana dashboards, Cloud Logging, distributed tracing) to guarantee observability, performance tracking, and rapid incident response.  
- **Secure** the deployment with **IAM**, **TLS/SSL**, and **compliance checks** (GDPR/CCPA) – encryption at rest/in‑transit, audit logs, and secret management (Secret Manager).  
- **Validate** high‑availability, scalability, and end‑to‑end functionality through smoke, load, and security tests.  
- **Document** deployment procedures, run‑books, and handover artifacts for ongoing operations.  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
```
project-root/
├─ backend/                     # Quarkus services
│  ├─ src/main/java/...         # Business logic, Kafka producers/consumers
│  ├─ src/main/resources/...    # Application.yml, schema.sql
│  ├─ src/main/docker/         # Dockerfile (multi‑stage)
│  └─ src/main/kubernetes/     # K8s deployment/service manifests
├─ frontend/                    # Next.js (web + mobile)
│  ├─ src/                      # React components, i18n, SEO
│  ├─ public/                   # Static assets
│  ├─ Dockerfile                # Multi‑stage for Node.js
│  └─ src/main/kubernetes/     # K8s frontend service
├─ docker/                      # Shared build scripts, docker‑compose for local CI
├─ k8s/                         # Helm charts / raw manifests for GKE
│  ├─ charts/
│  │  ├─ backend/
│  │  └─ frontend/
│  └─ monitoring/               # PrometheusRule, GrafanaDashboard YAMLs
├─ monitoring/                  # Prometheus config, alerting rules
├─ docs/                        # Deployment guides, run‑books
└─ ci-cd/                       # GitHub Actions workflows (build, test, deploy)
```
- **Endpoints** to be exposed (via Ingress):
  - `https://api.membership-hub.example.com/` (Quarkus REST API)
  - `https://app.membership-hub.example.com/` (Next.js web UI)
  - `https://mobile.membership-hub.example.com/` (PWA for mobile)
- **Health / Metrics** endpoints:
  - `/q/health` (Quarkus liveness/readiness)
  - `/metrics` (Prometheus metrics)
  - `/ping` (frontend health check)

## 3. Dedicated Sub-Agent Functional Directives
### Manager
- Finalize **deployment acceptance criteria** with product owner and security/compliance teams.  
- Coordinate **go‑live checklist** and schedule **post‑deployment review** with stakeholders.  

### Coder
- Produce **production‑ready Dockerfiles** for Quarkus (Java 21, GraalVM optional) and Next.js (Node 20) – multi‑stage, minimal layers.  
- Add **observability hooks**: expose `/metrics`, `/health`, and OpenTelemetry instrumentation for tracing.  
- Commit **K8s manifests** (Deployment, Service, Ingress, HPA, NetworkPolicy) to `src/main/kubernetes/` and `k8s/charts/`.  
- Ensure **configuration** (DB connection, Kafka bootstrap, Firebase/Google/Facebook auth credentials) is injected via **Secret Manager** or environment variables – no hard‑coded secrets.  
- Run **local Docker Compose** smoke test against a temporary GKE sandbox to verify container startup and health endpoints.  

### Tester
- Design **deployment smoke tests** (curl `/q/health`, `/metrics` on each service).  
- Execute **load tests** (k6 or Locust) against the deployed API to validate HPA behavior and throughput.  
- Perform **security scans** (Trivy for images, OWASP ZAP for runtime) and verify **network policies** block unintended pod communication.  
- Validate **end‑to‑end user flows** (login internal/Firebase/Google/Facebook → QR check‑in → notification) against the live environment.  
- Capture **monitoring alerts** and confirm they fire correctly for failures.  

### Reviewer
- Conduct **code review** of all Dockerfiles, K8s manifests, and CI/CD pipeline scripts for adherence to enterprise coding standards and security best practices.  
- Verify **Helm chart versioning**, `values.yaml` templating, and that all secrets are referenced via `SecretRef`.  
- Approve **observability configurations** (PrometheusRule, GrafanaDashboard) for completeness and naming conventions.  

### DevOps
- Provision **GKE cluster** (or reuse existing) with **node pools** tuned for the workload (e.g., balanced CPU/memory).  
- Apply **Kubernetes configurations**:
  - Namespace `membership-hub-prod`.
  - Deploy via **Helm** (or `kubectl apply`) using charts under `k8s/charts/`.
  - Configure **Ingress** (Google Cloud HTTP(S) LB) with **cert‑manager** for automated TLS.
  - Set up **Horizontal Pod Autoscaler** based on CPU/Memory metrics.
  - Enforce **Network Policies** to isolate backend, frontend, and database pods.
- Install **monitoring stack**:
  - Deploy **Prometheus Operator** and **Grafana** via Helm.
  - Import **pre‑built dashboards** from `k8s/monitoring/` and add custom panels for business metrics (e.g., attendance count, login attempts).
  - Define **Alertmanager** rules for pod restarts, high latency, and database connection errors.
- Integrate **Cloud Logging**: forward container logs to **Stackdriver** via sidecar or GKE logging agent.
- Set up **CI/CD pipeline** (GitHub Actions) that:
  - Runs unit & integration tests.
  - Builds and pushes Docker images to **Artifact Registry**.
  - Triggers **Helm upgrade** on the GKE cluster with rollback capability.
- Perform **post‑deployment validation**: verify all services are reachable, health checks pass, autoscaling triggers, and monitoring dashboards are populated.
- Document **run‑books** (restart procedures, scaling actions, log analysis) in `docs/` and share with operations team.  

## 4. Phase Definition of Done (DoD)
- ✅ All Docker images built, scanned, and pushed to GCP Artifact Registry.  
- ✅ Backend and frontend services deployed in GKE, with **ready** Ingress URLs (`api`, `app`, `mobile`).  
- ✅ **Liveness** and **readiness** probes configured and passing for every pod.  
- ✅ **Horizontal Pod Autoscaler** active and tested under load.  
- ✅ **Network policies** applied and validated (no cross‑namespace pod exposure).  
- ✅ **TLS/SSL** enabled via cert‑manager; domain certificates installed.  
- ✅ **IAM** and **Secret Manager** policies secured; no plaintext credentials in repo.  
- ✅ **Monitoring** stack operational:
  - Prometheus scrapes metrics from all services.  
  - Grafana dashboards display key business and infrastructure metrics.  
  - Alertmanager rules firing for critical events.  
- ✅ **Logging** flowing to Cloud Logging; structured log format for audit and debugging.  
- ✅ **Security & compliance** scans passed (Trivy, OWASP ZAP, GDPR/CCPA checks).  
- ✅ **Smoke, load, and end‑to‑end tests** executed and all passed.  
- ✅ **Documentation** (deployment guides, run‑books, monitoring dashboards) completed and stored in `docs/`.  
- ✅ **Stakeholder sign‑off** obtained; project manager confirms readiness for production go‑live.  

*Phase 5 is complete when every item above is verified and signed off.*