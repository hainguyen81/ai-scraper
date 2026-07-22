# PHASE 5 CONTEXT BLUEPRINT: membership-hub
## 1. Phase Operational Scope & Objectives
- **Deploy** the membership‑hub application to Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE).  
- **Containerize** the Java‑17 Quarkus backend and Node‑js Next.js frontend using Docker, build multi‑stage images, and push them to a GCP Artifact Registry.  
- **Orchestrate** the release with a CI/CD pipeline (GitHub Actions / Cloud Build) that automates testing, image promotion, and K8s deployment.  
- **Instrument** application and infrastructure monitoring (Prometheus + Grafana) and centralized logging (Cloud Logging + OpenTelemetry).  
- **Validate** the release with integration, smoke, and security tests; ensure rollback capability and compliance with enterprise guardrails.  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Directory / File Pattern | Purpose |
|--------------------------|---------|
| `./docker/` | Dockerfile(s) for backend (`Dockerfile`) and frontend (`Dockerfile`) |
| `./docker/backend/` | Backend‑specific Docker build context (e.g., `Dockerfile`, `entrypoint.sh`) |
| `./docker/frontend/` | Frontend‑specific Docker build context |
| `./k8s/` | Kubernetes manifests (Deployments, Services, ConfigMaps, Secrets, Monitoring) |
| `./k8s/backend-*` | Backend K8s resources |
| `./k8s/frontend-*` | Frontend K8s resources |
| `./k8s/prometheus-*` | Prometheus deployment & service |
| `./k8s/grafana-*` | Grafana deployment, service, secret |
| `./k8s/cloud-logging-configmap.yaml` | Cloud Logging agent configuration |
| `./monitoring/` | Prometheus `prometheus.yml`, Grafana dashboard JSON, alerting rules |
| `./src/main/docker/` | Quarkus native image build options (`dockerfile-maven-plugin` config) |
| `./src/main/resources/` | OpenTelemetry configuration (`otel-config.yaml`) |
| `./src/main/java/.../HealthResource.java` | Quarkus health & metrics endpoints |
| `./src/main/java/.../PingResource.java` | Simple smoke‑test endpoint |
| `./src/test/java/.../IntegrationTest.java` | Integration tests for deployed services |
| `./ci-cd/` | CI/CD scripts (`push-to-artifact-registry.sh`, `deploy-to-gke.sh`, `smoke-test.sh`) |
| `/.github/workflows/ci-cd.yml` | GitHub Actions workflow for build, test, push, deploy |
| `./docs/deployment-guide.md` | Deployment run‑book & rollback procedures |
| `./monitoring/alerting-rules.yaml` | Prometheus alerting rules (e.g., pod restarts, high latency) |

*Only the above paths may be created, modified, or referenced during Phase 5. No additional directories or external repositories may be introduced.*

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
- **Coder** – Produce Docker images, K8s manifests, health‑check endpoints, and OpenTelemetry configs.  
- **DevOps** – Configure GCP Artifact Registry, CI/CD pipelines, GKE deployments, monitoring & logging stack, and binary authorization.  
- **Tester** – Execute integration, smoke, and performance tests against the live cluster; verify monitoring data flow.  
- **Reviewer** – Conduct security scans (Trivy), secret‑management audit, and final documentation review; approve release artifacts.  

## 4. Phase Definition of Done (DoD)
- All Docker images are built, scanned, and pushed to GCP Artifact Registry.  
- K8s manifests are applied to GKE; all pods are in **Ready** state with active Services.  
- Prometheus scrapes application metrics; Grafana dashboards display real‑time metrics and alerts are firing.  
- Cloud Logging agent collects logs; OpenTelemetry traces are exported to a collector.  
- CI/CD pipeline runs end‑to‑end, passing unit, integration, and security scans, and successfully promotes images to production.  
- Smoke and integration tests pass against the deployed environment.  
- Binary Authorization policy is enforced; no vulnerable images can be deployed.  
- Documentation (deployment guide, run‑books, rollback steps) is complete and reviewed.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: BUILD AND PUSH DOCKER IMAGES

#### SUB‑TASK 1.1: Create multi‑stage Dockerfile for Quarkus backend
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./docker/backend/Dockerfile`
    *   **Architectural Requirements:**
        *   Use OpenJDK‑17‑slim as base for staging, then a distroless image for production.
        *   Copy compiled native executable (`*.native.jar` or binary) into final image.
        *   Define `HEALTHCHECK` using `curl` against `/q/health` (readiness/liveness).
        *   Set JVM options for Quarkus (`-Dquarkus.http.host=0.0.0.0`, enable metrics endpoint `/q/metrics`).
        *   Ensure image size < 150 MB and no unnecessary packages.

#### SUB‑TASK 1.2: Create Dockerfile for Next.js frontend
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./docker/frontend/Dockerfile`
    *   **Architectural Requirements:**
        *   Base on `node:20-alpine`.
        *   Set `NODE_ENV=production`, install dependencies via `package-lock.json`.
        *   Build Next.js app (`npm run build`).
        *   Use an nginx alpine image to serve static files; expose port `80`.
        *   Add `HEALTHCHECK` endpoint (`curl -f http://localhost/`).

#### SUB‑TASK 1.3: Push images to GCP Artifact Registry
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./ci-cd/push-to-artifact-registry.sh`
    *   **Architectural Requirements:**
        *   Authenticate to GCP using a service account with `artifactregistry.images.create` permission.
        *   Tag images with `${PROJECT_ID}/${REGION}/membership-hub-backend:${IMAGE_TAG}` and `${PROJECT_ID}/${REGION}/membership-hub-frontend:${IMAGE_TAG}`.
        *   Push both images using `docker push`.
        *   Verify image existence via `gcloud artifacts docker images list`.
        *   Script must be idempotent and fail fast on any authentication or push error.

### DAY 2: DEPLOY TO GKE (K8S MANIFESTS)

#### SUB‑TASK 2.1: Backend K8s manifests (Deployment, Service, ConfigMap, Secret)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./k8s/backend-deployment.yaml`
    *   **Architectural Requirements:**
        *   Use `imagePullSecrets` referencing GCP Artifact Registry credentials.
        *   Set `replicas: 3` with `strategy: RollingUpdate`.
        *   Resource requests/limits: `cpu: 250m`, `memory: 512Mi` (limits: `cpu: 1000m`, `memory: 2Gi`).
        *   Include `readinessProbe`/`livenessProbe` targeting `/q/health` (HTTP GET).
        *   Mount ConfigMap for application properties and Secret for external credentials.
*   **Target Path 2:** `./k8s/backend-service.yaml`
    *   **Architectural Requirements:**
        *   ClusterIP service exposing port `8080`.
        *   Add `sessionAffinity: ClientIP` for sticky sessions.
*   **Target Path 3:** `./k8s/backend-configmap.yaml`
    *   **Architectural Requirements:**
        *   Include Quarkus configuration keys (`quarkus.http.port`, `quarkus.datasource.*`).
        *   Define Kafka bootstrap servers, Postgres connection details via environment variables.
*   **Target Path 4:** `./k8s/backend-secret.yaml`
    *   **Architectural Requirements:**
        *   Store GCP service account key (via Secret Manager reference) and any DB passwords.
        *   Use `type: Opaque` and enable `automountServiceAccountToken: false`.

#### SUB‑TASK 2.2: Frontend K8s manifests (Deployment, Service, ConfigMap)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./k8s/frontend-deployment.yaml`
    *   **Architectural Requirements:**
        *   Deploy with `replicas: 2`, resource requests `cpu: 200m`, `memory: 256Mi`.
        *   Use `imagePullPolicy: Always`.
        *   Include environment variables for API base URL (`/api`).
        *   Add `readinessProbe` (`/`) and `livenessProbe` (`/`).
*   **Target Path 2:** `./k8s/frontend-service.yaml`
    *   **Architectural Requirements:**
        *   NodePort service exposing port `80`.
        *   Add `externalTrafficPolicy: Cluster`.
*   **Target Path 3:** `./k8s/frontend-configmap.yaml`
    *   **Architectural Requirements:**
        *   Store Next.js environment variables (`NEXT_PUBLIC_API_URL`, `NEXT_PUBLIC_KAFKA_BROKER`).
        *   Set `maxSize` to `10Mi`.

#### SUB‑TASK 2.3: Apply K8s manifests to GKE cluster
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./ci-cd/deploy-to-gke.sh`
    *   **Architectural Requirements:**
        *   Authenticate to GKE using `gcloud container clusters get-credentials ${CLUSTER_NAME} --region ${REGION}`.
        *   Set Kubernetes namespace `membership-hub` (create if missing).
        *   Apply all manifests in order: ConfigMaps → Secrets → Deployments → Services.
        *   Wait for rollout status (`kubectl rollout status deployment/<name> --timeout=300s`).
        *   Validate service endpoints (`kubectl get svc -n membership-hub`).
        *   Script must support dry‑run flag for preview.

### DAY 3: MONITORING SETUP (PROMETHEUS + GRAFANA)

#### SUB‑TASK 3.1: Prometheus configuration (scrape jobs)
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./monitoring/prometheus-config.yaml`
    *   **Architectural Requirements:**
        *   Define `scrape_interval: 15s`.
        *   Scrape backend at `http://backend-service.membership-hub:8080/q/metrics`.
        *   Scrape frontend at `http://frontend-service.membership-hub:80/`.
        *   Include node exporter scrape (`http://node-exporter.membership-hub:9100/metrics`).
        *   Configure remote write to Cloud Monitoring (optional).
        *   Set `evaluation_interval: 15s` and retention `15d`.

#### SUB‑TASK 3.2: Deploy Prometheus via Helm (or static manifests)
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./k8s/prometheus-deployment.yaml`
    *   **Architectural Requirements:**
        *   Use `prometheus:latest` image.
        *   Mount `prometheus-config.yaml` as config map.
        *   Resource requests `cpu: 200m`, `memory: 512Mi`.
        *   Expose port `9090`.
*   **Target Path 2:** `./k8s/prometheus-service.yaml`
    *   **Architectural Requirements:**
        *   ClusterIP service port `9090`.
        *   Add `selector: app=prometheus`.

#### SUB‑TASK 3.3: Create Grafana dashboard JSON
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./monitoring/grafana-dashboard.json`
    *   **Architectural Requirements:**
        *   Include panels for CPU usage, memory consumption, HTTP request rate, Kafka topic lag, DB connections.
        *   Set data source to Prometheus.
        *   Define alerts (e.g., CPU > 80% for 5 min) linked to Prometheus alerting rules.
        *   Dashboard title `Membership Hub Overview`.

#### SUB‑TASK 3.4: Deploy Grafana with admin credentials
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./k8s/grafana-deployment.yaml`
    *   **Architectural Requirements:**
        *   Use `grafana/grafana:latest`.
        *   Mount `grafana-dashboard.json` as config map (`/etc/grafana/provisioning/dashboards`).
        *   Set admin user/password via secret `grafana-admin`.
*   **Target Path 2:** `./k8s/grafana-service.yaml`
    *   **Architectural Requirements:**
        *   NodePort service exposing port `3000`.
*   **Target Path 3:** `./k8s/grafana-secret.yaml`
    *   **Architectural Requirements:**
        *   Store `admin:password` (rotate via GCP Secret Manager if possible).
        *   Use `type: Opaque`.

### DAY 4: LOGGING AND TRACING

#### SUB‑TASK 4.1: Configure Cloud Logging agent for GKE
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./k8s/cloud-logging-configmap.yaml`
    *   **Architectural Requirements:**
        *   Include `fluent-bit` configuration to tail container logs and forward to Cloud Logging.
        *   Set `log_id` to `membership-hub-logs`.
        *   Enable parsing of JSON log format (if used).
        *   Configure `allowlist` for namespaces `membership-hub`.

#### SUB‑TASK 4.2: Enable OpenTelemetry tracing
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./src/main/resources/otel-config.yaml`
    *   **Architectural Requirements:**
        *   Exporter set to `otlp` with endpoint `https://trace.googleapis.com`.
        *   Service name `membership-hub-backend`.
        *   Include span attributes for request method, path, user ID.
*   **Target Path 2:** `./frontend/otel-config.js`
    *   **Architectural Requirements:**
        *   Configure `@opentelemetry/sdk-node` with OTLP exporter to same trace endpoint.
        *   Instrument fetch/XHR calls to backend API.

#### SUB‑TASK 4.3: Add health & metrics endpoints in backend
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./src/main/java/com/example/membershiphub/HealthResource.java`
    *   **Architectural Requirements:**
        *   Expose `GET /q/health` (Quarkus built‑in) and custom `GET /q/health/ready`.
        *   Return JSON with status `UP` when all dependencies (DB, Kafka) are reachable.
        *   Include `GET /q/metrics` for Prometheus scraping (enable `quarkus.micrometer.export.prometheus.enabled`).

### DAY 5: CI/CD PIPELINE IMPLEMENTATION

#### SUB‑TASK 5.1: Create GitHub Actions workflow
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `/.github/workflows/ci-cd.yml`
    *   **Architectural Requirements:**
        *   Trigger on `push` to `main` and `pull_request`.
        *   Jobs: `build`, `test`, `security-scan`, `push-to-registry`, `deploy`.
        *   Use `setup-java` for Java 17, `setup-node` for Node.js.
        *   Build Quarkus native image (`mvn package -Dnative`) and Next.js static build (`npm run build`).
        *   Run unit tests (`mvn test`, `npm test`).
        *   Run Trivy vulnerability scan on Dockerfiles.
        *   Authenticate to GCP via workload identity or service account key.
        *   Push images to Artifact Registry.
        *   Deploy to GKE using `deploy-to-gke.sh`.
        *   Notify Slack/Email on failure.

#### SUB‑TASK 5.2: Define environment variables for CI/CD
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `/.github/workflows/ci-cd.yml` (environment section)
    *   **Architectural Requirements:**
        *   `GCP_PROJECT`, `GCP_REGION`, `GKE_CLUSTER`, `ARTIFACT_REPO`.
        *   `DOCKER_IMAGE_BACKEND`, `DOCKER_IMAGE_FRONTEND`.
        *   `IMAGE_TAG` derived from Git SHA.
        *   `KUBECONFIG_CONTENT` (base64 encoded) for GKE access.

#### SUB‑TASK 5.3: Add smoke‑test endpoint
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./src/main/java/com/example/membershiphub/PingResource.java`
    *   **Architectural Requirements:**
        *   Expose `GET /ping` returning `{"status":"OK","timestamp":${now}}`.
        *   No authentication required.
        *   Log each request with trace ID for distributed tracing.

### DAY 6: SECURITY AND COMPLIANCE

#### SUB‑TASK 6.1: Static security scan of Dockerfiles and K8s manifests
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./docker/`
    *   **Architectural Requirements:**
        *   Run `trivy image --severity HIGH,CRITICAL --ignore-unfixed`.
        *   Fail build if any critical vulnerability found.
*   **Target Path 2:** `./k8s/`
    *   **Architectural Requirements:**
        *   Scan YAML files for hardcoded secrets using `git-secrets` or `snyk`.
        *   Ensure all `imagePullSecrets` reference existing secrets.

#### SUB‑TASK 6.2: Review secrets management
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./k8s/backend-secret.yaml`
    *   **Architectural Requirements:**
        *   Verify secret values are base64 encoded, not plaintext.
        *   Ensure secret keys are referenced via GCP Secret Manager (`externalSecrets.io`).
*   **Target Path 2:** `./k8s/frontend-secret.yaml`
    *   **Architectural Requirements:**
        *   Same checks as backend secret.

#### SUB‑TASK 6.3: Enable Google Binary Authorization
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./k8s/binary-auth-policy.yaml`
    *   **Architectural Requirements:**
        *   Define `BinaryAuthorizationPolicy` with `cluster: membership-hub`.
        *   Reference GCP resource manager `projects/${PROJECT_ID}`.
        *   Enforce `allowlist` of approved images from Artifact Registry.
        *   Set `enforcementMode: ENABLED`.

### DAY 7: VERIFICATION, ROLLBACK, AND FINAL REVIEW

#### SUB‑TASK 7.1: Run integration tests against deployed services
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./src/test/java/com/example/membershiphub/IntegrationTest.java`
    *   **Architectural Requirements:**
        *   Use `RestAssured` or `WebTestClient` to call `/ping`, `/q/health`, and a sample API (e.g., `/api/users`).
        *   Validate HTTP status codes and response schema.
        *   Include test for Kafka producer/consumer health via `/q/metrics`.
        *   All tests must be annotated `@SpringBootTest` and run with `@ActiveProfiles("test")`.

#### SUB‑TASK 7.2: Perform smoke test via kubectl exec / curl
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./ci-cd/smoke-test.sh`
    *   **Architectural Requirements:**
        *   Wait for backend pod readiness (`kubectl wait --for=condition=ready pod -l app=backend -n membership-hub --timeout=60s`).
        *   Execute `curl -f http://backend-service.membership-hub:8080/ping`.
        *   Execute `curl -f http://frontend-service.membership-hub:80/` (if static).
        *   Exit with non‑zero if any request fails.
        *   Capture logs for debugging.

#### SUB‑TASK 7.3: Validate monitoring dashboards and alerts
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./monitoring/alerting-rules.yaml`
    *   **Architectural Requirements:**
        *   Define rule `PodRestarts` (alert if pod restarts > 2 in 5 min).
        *   Define rule `HighRequestLatency` (alert if p95 latency > 2s).
        *   Ensure alerts are linked to Grafana dashboard panels.
        *   Verify alert manager configuration routes to Slack webhook.

#### SUB‑TASK 7.4: Conduct final code & documentation review
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:

*   **Target Path 1:** `./docs/deployment-guide.md`
    *   **Architectural Requirements:**
        *   Document steps to build, push, deploy, rollback, and monitor.
        *   Include commands for CI/CD pipeline, K8s manifest updates, and troubleshooting.
        *   Provide contact points for support.
*   **Target Path 2:** All previous artifacts (Dockerfiles, K8s manifests, scripts)
    *   **Architectural Requirements:**
        *   Ensure consistent naming conventions (`kebab-case` for files, `snake_case` for env vars).
        *   Verify linting (YAML, shell) passes.
        *   Confirm no leftover debug statements or commented‑out credentials.

---