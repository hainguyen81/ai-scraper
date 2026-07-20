# PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Indicator |
|-----------|-------------|--------------------|
| **Production‑grade hardening** | Apply enterprise‑grade security, observability, and compliance controls across all services (backend, frontend, infra). | All guardrail checks (GDPR, OWASP, ISO‑27001, etc.) pass in CI/CD and runtime alerts are zero. |
| **Performance & scalability validation** | Load‑test the end‑to‑end attendance‑to‑notification flow at pilot‑scale (≥ 5 centers, 10 k concurrent users). | ≤ 200 ms 95th‑percentile response time, Kafka lag < 5 seconds, CPU ≤ 70 % under load. |
| **Tenant isolation & multi‑tenant ops** | Verify logical isolation (RLS, namespace quotas) and enable per‑tenant configuration UI. | No cross‑tenant data leakage in automated penetration tests; tenant‑specific branding works in UI. |
| **Monitoring, alerting & run‑books** | Deploy OpenTelemetry, Cloud Operations dashboards, SLO/SLA alerts, and create run‑books for incident response, DSAR, and rollback. | SLO ≥ 99.5 % availability, documented run‑books stored in Confluence, alerts fire on simulated failures. |
| **Pilot rollout & go‑live checklist** | Release MVP to 2‑3 pilot learning centers, collect feedback, and finalize production cut‑over plan. | Pilot centers report ≥ 90 % satisfaction, all checklist items signed‑off by Manager & Reviewer. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Repository / Directory | Allowed Files / Paths | Public API Endpoints (base) |
|------|------------------------|----------------------|-----------------------------|
| **Backend (Quarkus)** | `backend/` | `src/main/java/com/membershiphub/**`, `src/main/resources/application.yml`, `Dockerfile.native`, `pom.xml` | `POST /api/v1/attendance/checkin`<br>`GET /api/v1/members/{memberId}/balance`<br>`GET /api/v1/tenants/{tenantId}/config` |
| **Identity Service** | `identity/` | `keycloak/realm.json`, `firebase-config.json`, `Dockerfile` | `POST /auth/login` (email/password)<br>`POST /auth/oauth/{provider}` |
| **Notification Engine** | `notification/` | `src/main/java/com/membershiphub/notification/**`, `zalo-config.yaml`, `Dockerfile.native` | `POST /notify/member/{memberId}` (internal use only) |
| **Web / Mobile Front‑end (Next.js)** | `frontend/` | `pages/**`, `components/**`, `i18n/**`, `next.config.js`, `Dockerfile` | `GET /{locale}/login`<br>`GET /{locale}/dashboard`<br>`GET /{locale}/member/[id]` |
| **Infrastructure as Code** | `infra/` | `terraform/**`, `helm/**`, `k8s/**`, `cloudbuild.yaml` | N/A (IaC only) |
| **Observability** | `observability/` | `otel-collector-config.yaml`, `prometheus/**`, `grafana/**` | N/A |
| **Security / Guardrails** | `security/` | `policies/opa.rego`, `istio/**`, `cloudarmor/**` | N/A |

**Endpoint security constraints** – All external endpoints must enforce:  

* mTLS via Istio for service‑to‑service calls.  
* OAuth2 access token (Keycloak) with `aud=membership-hub` and max age 15 min.  
* Rate‑limit 100 rps per tenant (Istio `quota` policy).  

## 3. Dedicated Sub‑Agent Functional Directives  

### Coder  
1. **Security hardening** – Add Istio `RequestAuthentication` and `AuthorizationPolicy` for every microservice; configure Cloud Armor edge policies (IP allowlist, bot mitigation).  
2. **RLS implementation** – Write PostgreSQL Row‑Level Security policies (`tenant_id` filter) for `attendance`, `members`, `audit_log`. Add migration scripts under `backend/src/main/resources/db/migration/`.  
3. **Audit logging** – Emit immutable audit events to a dedicated Kafka topic `audit.events`; ensure each event is signed with Cloud KMS key.  
4. **Performance tweaks** – Enable Quarkus reactive PostgreSQL client, tune Kafka consumer `max.poll.records`, add GraalVM native image flags for low‑latency start‑up.  
5. **Documentation** – Update `README.md` and `docs/architecture.md` with production hardening steps and run‑book links.  

### Tester  
1. **Security test suite** – Run OWASP ZAP scans against all public endpoints; validate CSP, HSTS, X‑Frame‑Options, and CSRF tokens.  
2. **Compliance validation** – Execute automated GDPR/CCPA checks: verify hashed PII storage, consent flag presence, DSAR endpoint response format.  
3. **Load & stress testing** – Use JMeter to simulate 10 k concurrent users across 5 tenants; capture response times, Kafka lag, DB connection pool saturation.  
4. **Tenant isolation tests** – Attempt cross‑tenant data access via API and direct DB queries; ensure RLS blocks all unauthorized reads/writes.  
5. **End‑to‑end mobile flow** – Run Detox scripts for QR check‑in, membership‑day decrement, and push/Zalo notification receipt on both iOS and Android simulators.  

### Reviewer  
1. **Guardrail gate** – Verify that every PR includes:  
   * SonarQube quality gate ≥ A.  
   * Trivy container scan (no CVE ≥ 7).  
   * Checkov IaC scan (no policy violations).  
2. **Architecture compliance** – Confirm that new services respect the “single‑tenant identifier” pattern and that Helm charts include `resourceQuota` per namespace.  
3. **Code review checklist** – Ensure: input validation, proper exception handling, logging with correlation IDs, and no hard‑coded secrets.  
4. **Sign‑off** – Provide formal “Phase 5 Guardrail Compliance” approval in the PR description.  

### DevOps (Deployer)  
1. **Helm & Terraform promotion** – Apply `helm upgrade --install` for production release; run `terraform apply -target=module.gke` only if infra changes.  
2. **Canary rollout** – Deploy new version to 10 % of pods behind an Istio virtual service; monitor SLOs for 15 min before full rollout.  
3. **Observability stack** – Deploy OpenTelemetry Collector, configure Cloud Trace & Metrics exporters, create Grafana dashboards for: attendance latency, notification success rate, Kafka consumer lag, RLS audit counts.  
4. **Backup & DR** – Enable automated CloudSQL point‑in‑time recovery (PITR) and configure GKE multi‑zone node pools; test failover by simulating zone outage.  
5. **Run‑book publishing** – Populate Confluence pages with: incident response flow, DSAR handling procedure, rollback steps, and post‑mortem template.  

## 4. Phase Definition of Done (DoD)  

- **Guardrails**: All static analysis (SonarQube, Trivy, Checkov) pass; no critical or high findings.  
- **Security**: OWASP ZAP score ≤ 5 % risk; Istio mTLS enabled for 100 % of internal traffic; Cloud Armor policies live.  
- **Compliance**: GDPR/CCPA audit logs verified; DSAR API returns correct data within 48 h; RLS policies enforced (tested).  
- **Performance**: Load test meets SLA (≤ 200 ms 95th‑pct, Kafka lag < 5 s) and passes stress threshold (no crashes at 2× load).  
- **Observability**: End‑to‑end tracing visible for all request paths; alerts configured for latency > 300 ms, error rate > 1 %, audit‑log write failure.  
- **Documentation**: All run‑books, architecture diagrams, and deployment guides updated and reviewed.  
- **Pilot Acceptance**: Two pilot centers have signed off on functional and non‑functional criteria; feedback incorporated.  
- **Release**: Helm chart version `v5.0.0` deployed to production namespace `membership-hub-prod`; all pods healthy, zero‑downtime confirmed.  

*When all items above are satisfied and the Phase Gate Review (Manager + Reviewer) signs off, Phase 5 is considered complete.*