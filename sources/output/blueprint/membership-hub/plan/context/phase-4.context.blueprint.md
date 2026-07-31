# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260731165119 |
| **Project Name** | membership-hub |
| **Phase** | 4 |
| **Version** | 1.0 (Baseline) |
| **Date/Time** | 2026/07/31 16:51:19 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
Phase 4 is dedicated to the **infrastructure deployment and monitoring** of the membership‑hub platform. The objectives are:
- Build **container images** for backend and frontend services using secure, multi‑stage Dockerfiles that satisfy [NFR‑001] (performance) and [NFR‑002] (availability).
- Deploy the services to a **Google Kubernetes Engine (GKE)** cluster with proper resource limits, health checks, and secrets management, ensuring high‑availability and scalability.
- Configure **Prometheus** and **Grafana** for real‑time metrics collection, alerting, and dashboards, meeting [NFR‑003] (security) and [NFR‑004] (scalability & availability).
- Provide **automation scripts** (Helm charts, deployment manifests, monitoring configs) that can be versioned, reviewed, and executed in CI/CD pipelines.
- Deliver comprehensive **documentation** of the deployment process, configuration parameters, and troubleshooting guidelines.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Directory | Purpose | Allowed Files |
| :--- | :--- | :--- |
| `./sources/infra/deployment` | Dockerfiles, Kubernetes manifests, Helm charts | `Dockerfile.backend`, `Dockerfile.frontend`, `backend-deployment.yaml`, `frontend-deployment.yaml`, `helm/backend/Chart.yaml`, `helm/frontend/Chart.yaml`, `helm/backend/values.yaml`, `helm/frontend/values.yaml` |
| `./sources/infra/monitoring` | Prometheus scrape configs, Grafana dashboards, Alertmanager rules, health‑check scripts | `prometheus.yml`, `grafana-dashboard.json`, `alertmanager.yml`, `healthcheck.sh` |
| `./sources/infra/docs` | Technical documentation for infra | `infra-setup.md` |

No other directories or files outside `./sources/` are permitted for this phase.

## 3. Dedicated Sub-Agent Functional Directives
| Sub-Agent | Responsibilities |
| :--- | :--- |
| **docker** | Build and test Docker images; enforce OWASP container security best‑practice (image scanning, minimal base images). |
| **GCP** | Manage GCP resources (GKE cluster, IAM, secrets); deploy Helm charts; configure Alertmanager. |
| **GKE** | Apply Kubernetes manifests; configure autoscaling, liveness/readiness probes, resource quotas. |
| **reviewer** | Perform static analysis of Dockerfiles, Kubernetes manifests, Helm charts, and monitoring configs; validate against NFR tags. |
| **doc** | Compile end‑to‑end documentation of deployment, monitoring, and troubleshooting. |

## 4. Phase Definition of Done (DoD)
- All Docker images built and scanned with no critical vulnerabilities.  
- Kubernetes deployments deployed to GKE with at least 2 replicas, proper health checks, and autoscaling enabled.  
- Prometheus and Grafana dashboards operational, exposing metrics for backend, frontend, and cluster health.  
- Alertmanager configured with at least one rule for CPU > 70 % and latency > 300 ms.  
- All artifacts (Dockerfiles, manifests, Helm charts, monitoring configs) pass static analysis and reviewer approval.  
- Documentation `infra-setup.md` fully maps every tag `[NFR-001]`–`[NFR-004]` to its implementation.  
- 100 % traceability: every tag referenced in this phase appears in at least one sub‑task.  
- OWASP container security compliance achieved (no high‑severity findings).  
- CI/CD pipeline integration verified (build, test, deploy, monitor).  

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: CONTAINER IMAGE BUILD & REVIEW

#### SUB-TASK 1.1: Create backend Dockerfile
##### Assigned Sub-Agent: docker
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment/Dockerfile.backend`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002]`
* **Architectural Requirements:**
  * Multi‑stage build using `openjdk:17-jdk-slim` as base, `maven:3.8.6-jdk-17` for compile.  
  * Copy only compiled JAR to final image.  
  * Expose port 8080, set `ENTRYPOINT ["java","-jar","/app.jar"]`.  
  * Add `HEALTHCHECK CMD curl -f http://localhost:8080/actuator/health || exit 1`.  
  * Use `ARG` for version tagging, avoid hard‑coded secrets.  
  * Ensure image size < 200 MB, final < 500 MB.  
  * Run `trivy image` scan; no critical findings.

#### SUB-TASK 1.2: Create frontend Dockerfile
##### Assigned Sub-Agent: docker
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment/Dockerfile.frontend`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002]`
* **Architectural Requirements:**
  * Base `node:18-alpine` for build, `nginx:1.23-alpine` for runtime.  
  * Build React app with `npm ci && npm run build`.  
  * Copy `build` folder to `/usr/share/nginx/html`.  
  * Expose port 80, set `CMD ["nginx","-g","daemon off;"]`.  
  * Add `HEALTHCHECK CMD wget -qO- http://localhost/health || exit 1`.  
  * Image size < 200 MB, final < 500 MB.  
  * Run `trivy image` scan; no critical findings.

#### SUB-TASK 1.3: Static analysis of Dockerfiles
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment/Dockerfile.backend;./sources/infra/deployment/Dockerfile.frontend`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002]`
* **Architectural Requirements:**
  * Verify no `latest` tags, no `RUN apt-get update` without `--no-install-recommends`.  
  * Ensure `USER` non‑root in final stage.  
  * Confirm health‑check presence and correct endpoint.  
  * Validate environment variable usage for secrets.

### DAY 2: KUBERNETES DEPLOYMENT MANIFESTS

#### SUB-TASK 2.1: Backend deployment manifest
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment/backend-deployment.yaml`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002]`
* **Architectural Requirements:**
  * `apiVersion: apps/v1`, `kind: Deployment`.  
  * `replicas: 2`, `strategy: RollingUpdate`.  
  * `containers: image: gcr.io/<project>/backend:<tag>`.  
  * `ports: containerPort: 8080`.  
  * `livenessProbe` and `readinessProbe` on `/actuator/health`.  
  * `resources: limits: cpu: "1", memory: "512Mi"`.  
  * `envFrom: secretRef: name: backend-secrets`.  
  * `serviceAccountName: backend-sa`.  
  * `autoscaling: HorizontalPodAutoscaler` with CPU target 70 %.  

#### SUB-TASK 2.2: Frontend deployment manifest
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment/frontend-deployment.yaml`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002]`
* **Architectural Requirements:**
  * Similar structure to backend, `containerPort: 80`.  
  * `livenessProbe` on `/health`.  
  * `resources: limits: cpu: "0.5", memory: "256Mi"`.  
  * `serviceAccountName: frontend-sa`.  

#### SUB-TASK 2.3: Static analysis of deployment manifests
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment/backend-deployment.yaml;./sources/infra/deployment/frontend-deployment.yaml`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002]`
* **Architectural Requirements:**
  * Validate presence of probes, resource limits, and service accounts.  
  * Ensure no hard‑coded credentials.  
  * Check that `imagePullSecrets` reference exists.

### DAY 3: HELM CHARTS FOR DEPLOYMENT

#### SUB-TASK 3.1: Backend Helm chart
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment/helm/backend/Chart.yaml`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002]`
* **Architectural Requirements:**
  * `apiVersion: v2`, `name: backend`, `version: 0.1.0`.  
  * `values.yaml` includes image tag, replica count, resource limits, env vars.  
  * `templates/deployment.yaml` uses `{{ .Values.image.repository }}`.  
  * `templates/service.yaml` exposes port 8080.  
  * `templates/hpa.yaml` for autoscaling.  

#### SUB-TASK 3.2: Frontend Helm chart
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment/helm/frontend/Chart.yaml`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002]`
* **Architectural Requirements:**
  * Similar to backend chart, with port 80.  
  * `values.yaml` includes image tag, replica count, resource limits.  

#### SUB-TASK 3.3: Helm chart lint and review
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment/helm/backend;./sources/infra/deployment/helm/frontend`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002]`
* **Architectural Requirements:**
  * Run `helm lint` on each chart.  
  * Verify chart dependencies, required values, and templating syntax.  
  * Ensure no hard‑coded secrets in templates.

### DAY 4: MONITORING CONFIGURATION

#### SUB-TASK 4.1: Prometheus scrape config
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/monitoring/prometheus.yml`
* **Traceability Tag Tokens:** `[NFR-003], [NFR-004]`
* **Architectural Requirements:**
  * `scrape_configs` for `kubernetes-nodes`, `kubernetes-pods`, `backend-service`, `frontend-service`.  
  * `relabel_configs` to drop `kubernetes_io_hostname`.  
  * `scrape_interval: 15s`, `scrape_timeout: 10s`.  

#### SUB-TASK 4.2: Grafana dashboard JSON
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/monitoring/grafana-dashboard.json`
* **Traceability Tag Tokens:** `[NFR-003], [NFR-004]`
* **Architectural Requirements:**
  * Panels for CPU, memory, request latency, error rates for backend and frontend.  
  * Variables for namespace, environment.  
  * Time range defaults to last 1h, refresh every 30s.  

#### SUB-TASK 4.3: Monitoring config static analysis
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/monitoring/prometheus.yml;./sources/infra/monitoring/grafana-dashboard.json`
* **Traceability Tag Tokens:** `[NFR-003], [NFR-004]`
* **Architectural Requirements:**
  * Validate YAML syntax, metric naming conventions, and no duplicate job names.  
  * Ensure Grafana JSON follows schema, no missing required fields.

### DAY 5: ALERTING, HEALTH CHECKS, AND DOCUMENTATION

#### SUB-TASK 5.1: Alertmanager configuration
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/monitoring/alertmanager.yml`
* **Traceability Tag Tokens:** `[NFR-003], [NFR-004]`
* **Architectural Requirements:**
  * Alert rules for `CPU > 70%`, `Latency > 300ms`, `Pod restarts > 3`.  
  * Notification receivers: Slack webhook, email.  
  * Silence period for maintenance windows.  

#### SUB-TASK 5.2: Health‑check shell script
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/monitoring/healthcheck.sh`
* **Traceability Tag Tokens:** `[NFR-003], [NFR-004]`
* **Architectural Requirements:**
  * Checks Kubernetes node status, pod readiness, and Prometheus endpoint.  
  * Exit code 0 on success, non‑zero on failure.  
  * Log output to `/var/log/healthcheck.log`.  

#### SUB-TASK 5.3: Infra documentation compilation
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/docs/infra-setup.md`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002], [NFR-003], [NFR-004]`
* **Architectural Requirements:**
  * Sections: Docker build, Helm deployment, GKE cluster setup, Prometheus/Grafana monitoring, Alertmanager alerts, health‑check usage, troubleshooting.  
  * Include code snippets, command examples, and diagram of architecture.  
  * Reference all tag IDs with implementation file paths.  

#### SUB-TASK 5.4: Final reviewer audit
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/deployment;./sources/infra/monitoring;./sources/infra/docs`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002], [NFR-003], [NFR-004]`
* **Architectural Requirements:**
  * Verify that every artifact passes linting, scanning, and that all tags are covered.  
  * Confirm that documentation aligns with implemented artifacts.  
  * Approve final commit for CI/CD pipeline integration.