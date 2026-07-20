# PHASE 5 CONTEXT BLUEPRINT: test‑ai‑architecture  

## 1. Phase Operational Scope & Objectives  
| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| **Security Hardening** | Implement Zero‑Trust guardrails (OPA Gatekeeper policies, Binary Authorization, secret management, mTLS via Istio). | 0 critical/high security findings in automated scans; all policies pass CI gate. |
| **Autoscaling & Resilience** | Configure HPA/Cluster‑Autoscaler, pod‑disruption‑budgets, and graceful shutdown hooks for all micro‑services. | 99.9 % availability in simulated traffic spikes; CPU/Memory ≤ 70 % at peak load. |
| **Observability Stack** | Deploy Prometheus, Grafana, OpenTelemetry collectors, and ELK logging; create dashboards for QR‑scan latency, notification delivery, and tenant‑level throughput. | End‑to‑end latency ≤ 200 ms (QR scan → notification) 95 % of the time; alerting on SLA breach within 1 min. |
| **Chaos‑Engineered Load Testing** | Run k6 / Locust scenarios that simulate 10 k concurrent learners across 20 tenants, inject pod failures, network latency, and Kafka broker loss. | No data loss, idempotent attendance; system recovers < 30 s after fault injection. |
| **Production Deployment** | Execute a blue‑green (or canary) rollout to GKE using Argo CD/Flux, with automated rollback on health‑check failure. | Deployment success rate ≥ 99 %; MTTR < 10 min for any rollback. |
| **Documentation & Handover** | Produce run‑books for incident response, scaling procedures, and compliance audit (GDPR, SOC‑2). | Documentation reviewed and approved by Reviewer; stored in `docs/production/`. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Area | Repository Path | Allowed Modifications | Public / Internal Endpoints |
|------|----------------|-----------------------|-----------------------------|
| **Infrastructure as Code** | `infra/terraform/` – GCP project, VPC, IAM, CloudSQL, GKE cluster | Add/modify Terraform modules for autoscaling, node‑pools, IAM bindings | N/A |
| **Kubernetes Manifests** | `k8s/helm/` – Helm charts for each service (`attendance-service`, `notification-service`, `gateway`, `opa-gatekeeper`) | Update values for resources, HPA, pod‑disruption‑budget, liveness/readiness probes | N/A |
| **OPA Policies** | `security/opa/` – Rego files (`gatekeeper/`, `binary-authz/`) | Add new policies for tenant isolation, rate‑limit, JWT scopes | N/A |
| **Observability Config** | `observability/prometheus/`, `observability/grafana/`, `observability/otel/` | Add scrape configs, dashboard JSON, OpenTelemetry SDK init code | N/A |
| **Load‑Test Scripts** | `tests/load/k6/` – `scenario-*.js` | Create/adjust scripts for multi‑tenant traffic, fault injection | N/A |
| **CI/CD Pipelines** | `.github/workflows/` – `ci.yml`, `cd.yml` | Add steps for policy enforcement, image signing, canary promotion | N/A |
| **Service Code (Read‑only for this phase)** | `services/attendance/`, `services/notification/` – existing Quarkus source | **No functional changes** – only add instrumentation hooks, health‑check endpoints (`/healthz`, `/readyz`) | `GET /api/v1/attendance/healthz`, `GET /api/v1/notification/readyz` |
| **Monitoring Endpoints** | `services/*/src/main/java/.../metrics/` – Micrometer/OpenTelemetry exporters | Add metric tags (`tenant_id`, `locale`) | N/A |
| **Documentation** | `docs/production/` – run‑books, SOPs | Write/format markdown files | N/A |

> **Strict Boundary Rule:** No changes to core business logic (attendance calculation, QR handling) are permitted in Phase 5. All modifications must be confined to the directories listed above.

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Tasks (ordered) | Deliverable Artefacts |
|-----------|----------------|-----------------------|
| **Coder** | 1. Instrument all Quarkus services with OpenTelemetry (trace IDs, span attributes `tenant_id`, `user_id`). <br>2. Expose `/healthz` and `/readyz` endpoints with proper status codes. <br>3. Add Prometheus Micrometer metrics for `attendance_scans_total`, `notification_sent_total`, and latency histograms. <br>4. Refactor Helm values to include resource limits, HPA rules, and pod‑disruption‑budget. <br>5. Create Helm sub‑chart `observability` that deploys Prometheus‑Operator, Grafana, and OTEL collector as a sidecar. | - Updated source files under `services/*/src/main/java/.../metrics/` <br>- New Helm chart `observability/` <br>- PR with instrumentation changes |
| **Tester** | 1. Write integration tests (Quarkus `@QuarkusTest`) that verify health/readiness endpoints return `200`. <br>2. Develop contract tests (Pact) for `attendance-service` → `notification-service` Kafka messages, ensuring required headers (`tenant_id`, `trace_id`). <br>3. Implement end‑to‑end k6 scripts that: <br>&nbsp;&nbsp;a. Simulate QR scans across 20 tenants. <br>&nbsp;&nbsp;b. Validate that duplicate scans on the same day are idempotent. <br>&nbsp;&nbsp;c. Assert latency < 200 ms and correct metric increments. <br>4. Add Grafana dashboard JSON validation tests (ensure panels exist). | - `tests/integration/health-readiness-test.java` <br>- `tests/pact/attendance-notification.pact.json` <br>- `tests/load/k6/scenario-multi-tenant.js` <br>- `observability/grafana/dashboards/attendance.json` |
| **Reviewer** | 1. Perform static code analysis (SonarQube) on instrumentation changes; enforce no new critical issues. <br>2. Run OPA policy linting (`opa test`) against all new Rego files. <br>3. Validate Helm chart lint (`helm lint`) and Helm test hooks. <br>4. Conduct security review of image build (ensure Cosign signatures, no critical CVEs via Trivy). <br>5. Sign‑off on compliance checklist (Zero‑Trust, GDPR tenant isolation, audit‑log forwarding). | - Review comments on PRs <br>- Signed-off checklist document `docs/production/compliance-checklist.md` |
| **DevOps (Deployer)** | 1. Extend GitHub Actions `cd.yml` to include: <br>&nbsp;&nbsp;a. OPA Gatekeeper policy enforcement as a pre‑deployment gate. <br>&nbsp;&nbsp;b. Cosign verification of Docker images. <br>&nbsp;&nbsp;c. Canary rollout steps using Argo CD `ApplicationSet`. <br>2. Configure GKE node‑pool autoscaling policies (CPU target 60 %). <br>3. Deploy Prometheus‑Operator, Grafana, and OTEL collector via Helm in the `observability` namespace. <br>4. Set up alerting rules in Prometheus for: <br>&nbsp;&nbsp;a. Attendance latency SLA breach. <br>&nbsp;&nbsp;b. Kafka consumer lag > 5000 msgs. <br>&nbsp;&nbsp;c. Pod restarts > 3 in 5 min. <br>5. Execute blue‑green deployment to production; verify traffic shift and rollback on any health‑check failure. | - Updated GitHub Actions workflow files <br>- Helm release manifests applied to GKE (recorded in `deployment/` logs) <br>- PrometheusRule CRDs `observability/prometheus/rules.yaml` <br>- Deployment run‑book `docs/production/deployment-runbook.md` |

## 4. Phase Definition of Done (DoD)  
The phase is considered **Done** when **all** items below are satisfied and signed off by the **Manager**:

1. **Security & Compliance**  
   - All OPA Gatekeeper policies pass (`opa eval` returns no violations).  
   - Binary Authorization enforced; every image in Artifact Registry is signed and verified.  
   - No critical/high findings from Trivy, SonarQube, or dependency scanning.  

2. **Scalability & Resilience**  
   - HPA rules are active; `kubectl get hpa` shows target CPU 60 % and max replicas ≥ 10 per service.  
   - Pod‑Disruption‑Budgets allow at least 1‑pod availability during node upgrades.  
   - Chaos test reports: system recovers from pod kill, network latency, and Kafka broker loss within 30 s, with zero data loss.  

3. **Observability**  
   - Prometheus scrapes all services; metrics `attendance_scans_total`, `notification_sent_total`, and latency histograms are visible.  
   - Grafana dashboards load without errors and display real‑time data for at least 3 tenants.  
   - OpenTelemetry traces appear in the chosen backend (e.g., Google Cloud Trace) with correct `tenant_id` and `trace_id` propagation.  

4. **CI/CD Pipeline**  
   - GitHub Actions pipeline runs end‑to‑end on the `main` branch: lint → test → image build → sign → policy gate → canary deploy → promotion.  
   - Any pipeline failure blocks merge; all successful runs are recorded in the pipeline dashboard.  

5. **Load‑Test Validation**  
   - k6 script `scenario-multi-tenant.js` completes with < 5 % errors.  
   - Recorded average latency ≤ 200 ms; 95 th percentile ≤ 250 ms.  
   - Duplicate QR scans on the same day are deduplicated (verified via Kafka audit topic).  

6. **Documentation & Handover**  
   - Run‑books for **Incident Response**, **Scaling**, and **Compliance Auditing** are stored under `docs/production/` and reviewed by Reviewer.  
   - All new Helm charts, OPA policies, and monitoring configs are version‑controlled with proper `README.md` explaining usage.  

7. **Production Release**  
   - Blue‑green (or canary) deployment completed; traffic switched to the new version with no user‑visible downtime.  
   - Health endpoints (`/healthz`, `/readyz`) return `200` for all pods.  
   - Manager signs off after a 24‑hour observation window with no SLA breaches.  

*Only when every bullet above is verified and the sign‑off is recorded does Phase 5 close, allowing the project to move to post‑launch support.*