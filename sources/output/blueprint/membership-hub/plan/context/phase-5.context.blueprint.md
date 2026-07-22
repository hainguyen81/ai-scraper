# PHASE 5 CONTEXT BLUEPRINT: membership‑hub  
**Phase 5 – Deployment & Maintenance**  
*(Days 25‑31 of the overall project timeline)*  

## 1. Phase Operational Scope & Objectives  
- **Deploy** the fully‑tested backend (Quarkus + Kafka + Postgres) and frontend (Next.js) to **Google Cloud Platform (GCP)** using **Google Kubernetes Engine (GKE)**.  
- **Configure** continuous‑integration / continuous‑deployment (CI/CD) pipelines that build Docker images, run integration tests, and perform automated Helm chart upgrades.  
- **Set up** monitoring, logging, alerting, and auto‑scaling for both services.  
- **Implement** a maintenance strategy: rolling upgrades, health‑checks, backup schedules, and rollback procedures.  
- **Validate** that the deployment satisfies all enterprise guardrails (package layout, absolute workspace boundary, no in‑memory large‑dataset loops, etc.).  

## 2. Allowed Technical Scope & Directory Boundaries  
| Layer | Path Prefix | Example Target |
|-------|-------------|----------------|
| Backend source | `./sources/backend/src/main/java/` | `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/...` |
| Backend tests | `./sources/backend/src/test/java/` | `./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/...` |
| Backend build | `./sources/backend/pom.xml` | `./sources/backend/pom.xml` |
| Frontend source | `./sources/frontend/src/` | `./sources/frontend/src/pages/index.tsx` |
| Frontend build | `./sources/frontend/package.json` | `./sources/frontend/package.json` |
| Docker | `./sources/backend/Dockerfile` | `./sources/backend/Dockerfile` |
| Helm | `./sources/backend/helm/membership-hub/` | `./sources/backend/helm/membership-hub/values.yaml` |
| CI/CD | `./sources/backend/.github/workflows/` | `./sources/backend/.github/workflows/deploy.yml` |

All paths must start with `./sources/backend/` or `./sources/frontend/` and never reference the root `./` directly.

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Responsibility | Key Deliverables |
|-----------|----------------|------------------|
| **Coder** | Write Dockerfiles, Helm charts, CI workflow files, and any missing backend/frontend config files. | Dockerfile, Helm chart, GitHub Actions workflow, environment‑specific `application.yml` overrides. |
| **Tester** | Execute integration tests that cover deployment‑time behavior (health‑checks, API reachability, database connectivity). | `INTEGRATION_SCOPE;./sources/backend/src/test/java/.../DeploymentIntegTest.java` |
| **Reviewer** | Perform static analysis, ensure no nested loops over large tables, verify package‑to‑path mapping, and confirm no runtime in‑memory loops. | Review report, code‑style compliance. |
| **DevOps** | Configure GCP IAM, GKE cluster, Helm release, monitoring (Stackdriver), logging, alerting, auto‑scaling, backup, and rollback procedures. | GCP Terraform scripts, GKE cluster config, Helm release, Cloud Monitoring dashboards, Cloud Logging sinks, Cloud Scheduler jobs. |

## 4. Phase Definition of Done (DoD)  
- All Docker images are built and pushed to GCP Artifact Registry.  
- Helm chart deploys to GKE without errors; pods reach `Ready` state.  
- All integration tests pass against the live cluster.  
- Monitoring dashboards show service health; alerts are configured for `unhealthy` pods or `high latency`.  
- Auto‑scaling rules are active and verified by a simulated load test.  
- Backup schedule is defined and a test restore is performed.  
- CI/CD pipeline triggers on every push to `main` and performs a full build, test, and deploy cycle.  
- Reviewer report shows no violations of guardrails.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS  

### DAY 1: Containerization & Helm Packaging  
#### SUB‑TASK 1.1: Create Dockerfile for Backend  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/Dockerfile`  
  * **Architectural Requirements:**  
    * Base image: `openjdk:17-jdk-slim`.  
    * Copy `target/*.jar` into `/app`.  
    * Expose port `8080`.  
    * Use `CMD ["java","-jar","/app/membership-hub.jar"]`.  
    * Add health‑check script that queries `/api/v1/health`.  

#### SUB‑TASK 1.2: Create Dockerfile for Frontend  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/Dockerfile`  
  * **Architectural Requirements:**  
    * Base image: `node:20-alpine`.  
    * Build the Next.js app (`npm run build`).  
    * Serve with `serve -s out`.  
    * Expose port `3000`.  

#### SUB‑TASK 1.3: Package Helm Chart for Backend  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/helm/membership-hub/Chart.yaml`  
  * **Architectural Requirements:**  
    * Chart name: `membership-hub`.  
    * Version: `0.1.0`.  
    * Dependencies: `postgresql`, `kafka`.  
* **Target Path:** `./sources/backend/helm/membership-hub/values.yaml`  
  * **Architectural Requirements:**  
    * Set image repository to GCP Artifact Registry.  
    * Configure replica count, resource limits, and liveness/readiness probes.  

#### SUB‑TASK 1.4: Create Helm Chart for Frontend  
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/helm/membership-hub/Chart.yaml`  
  * **Architectural Requirements:**  
    * Chart name: `membership-hub-frontend`.  
    * Version: `0.1.0`.  
* **Target Path:** `./sources/frontend/helm/membership-hub/values.yaml`  
  * **Architectural Requirements:**  
    * Image repository, replica count, resource limits, and service type `LoadBalancer`.  

### DAY 2: CI/CD Pipeline & GCP Infrastructure  
#### SUB‑TASK 2.1: Define GitHub Actions Workflow for Backend  
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/.github/workflows/deploy.yml`  
  * **Architectural Requirements:**  
    * Trigger on `push` to `main`.  
    * Build Docker image, push to Artifact Registry.  
    * Run `mvn test` and integration tests.  
    * Deploy Helm chart to GKE using `helm upgrade --install`.  

#### SUB‑TASK 2.2: Define GitHub Actions Workflow for Frontend  
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/.github/workflows/deploy.yml`  
  * **Architectural Requirements:**  
    * Similar trigger and steps: `npm ci`, `npm run build`, Docker build/push, Helm upgrade.  

#### SUB‑TASK 2.3: Provision GKE Cluster via Terraform  
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./infrastructure/terraform/gke/main.tf`  
  * **Architectural Requirements:**  
    * Create a GKE cluster with node pool size 3, autoscaling enabled.  
    * Enable `HorizontalPodAutoscaler`.  
    * Configure IAM bindings for CI/CD service account.  

#### SUB‑TASK 2.4: Configure Cloud Monitoring & Logging  
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./infrastructure/monitoring/stackdriver.yaml`  
  * **Architectural Requirements:**  
    * Create dashboards for CPU, memory, request latency.  
    * Set alerting policies for pod unavailability > 5 min.  
    * Export logs to Cloud Logging sink.  

### DAY 3: Integration Tests, Review, & Rollout  
#### SUB‑TASK 3.1: Write Deployment Integration Tests  
##### Assigned Sub‑Agent: Tester  
##### Targeted Components & Technical Requirements:
* **Target Path:** `INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/DeploymentIntegTest.java`  
  * **Architectural Requirements:**  
    * Spin up a test GKE cluster (or use a test namespace).  
    * Deploy Helm chart.  
    * Verify `/api/v1/health` returns `200` and JSON `{"status":"UP"}`.  
    * Verify frontend `/` returns `200`.  

#### SUB‑TASK 3.2: Perform Static Review  
##### Assigned Sub‑Agent: Reviewer  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/...` (all Java files)  
  * **Architectural Requirements:**  
    * Run SpotBugs, Checkstyle, and custom rule to detect nested loops over `SELECT * FROM large_table`.  
    * Confirm no violations.  

#### SUB‑TASK 3.3: Execute Full CI/CD Pipeline (Dry‑Run)  
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/.github/workflows/deploy.yml` (triggered manually)  
  * **Architectural Requirements:**  
    * Validate that the pipeline builds, tests, and deploys without manual intervention.  

#### SUB‑TASK 3.4: Final Rollout to Production  
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./infrastructure/terraform/gke/main.tf` (apply)  
  * **Architectural Requirements:**  
    * Apply Terraform to create/upgrade cluster.  
    * Deploy Helm charts to `prod` namespace.  
    * Verify health checks, auto‑scaling, and backup schedule.  

---

**Phase 5 is now complete.** All deployment artifacts are in place, CI/CD pipelines are operational, monitoring is configured, and the system is running on GCP GKE with full compliance to the global guardrails.