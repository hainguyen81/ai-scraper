# PHASE 4 CONTEXT BLUEPRINT: test‑ai‑architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Metric |
|-----------|-------------|----------------|
| **Implement Notification Engine** | Build a **Kafka‑driven** notification service that consumes attendance events, de‑duplicates them, and dispatches **FCM push**, **Zalo SMS**, and **Zalo group** messages. | 99.9 % delivery success for events processed in the pipeline (as measured by Kafka consumer lag & external API ACK). |
| **Integrate Zalo Business API** | Wrap Zalo’s REST endpoints (message, group‑send) behind a **Quarkus** client with retry & circuit‑breaker logic. | < 2 % failure rate after retries; circuit‑breaker opens only under sustained > 5 % error. |
| **Idempotent Attendance Logic** | Ensure a learner’s daily QR scan creates **exactly one attendance record** per tenant/day, regardless of multiple scans. | Duplicate‑attendance rate < 0.1 % (validated by integration tests). |
| **Secure, Auditable Messaging** | All outbound messages are logged to an **append‑only Kafka topic `notification‑audit`** and to **Cloud Audit Logs** with immutable timestamps. | 100 % of sent messages have a corresponding audit record. |
| **Observability & SLA** | End‑to‑end latency **QR scan → notification** ≤ 200 ms (95th percentile) with OpenTelemetry traces exported to GCP Trace. | Grafana dashboard shows latency ≤ 200 ms after load‑test (10 k scans/min). |
| **CI/CD Hardened Delivery** | Container image built with **multi‑stage Docker**, scanned (Trivy), signed (Cosign), and deployed via **ArgoCD** using Helm chart versioned `notification-service`. | 0 critical CVEs, image size ≤ 150 MB (native) or ≤ 300 MB (JVM), 100 % automated rollout success. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Allowed Path / Package | Description | Public Endpoint |
|-------|------------------------|-------------|-----------------|
| **Quarkus Service** | `src/main/java/com/membershiphub/notification/` | Core notification micro‑service code. | `POST /api/v1/attendance/events` **(internal only)** – Kafka producer (already exists). <br> `GET /api/v1/notifications/health` – health check. |
| **Kafka Consumers** | `src/main/java/com/membershiphub/notification/kafka/` | `AttendanceConsumer` (listens on `attendance-events`), `NotificationAuditProducer` (writes to `notification-audit`). |
| **Zalo Client** | `src/main/java/com/membershiphub/notification/integrations/zalo/` | Wrapper around Zalo Business API (`ZaloMessageClient`, `ZaloGroupClient`). |
| **FCM Client** | `src/main/java/com/membershiphub/notification/integrations/fcm/` | `FcmPushClient` using Firebase Admin SDK. |
| **Domain Model** | `src/main/java/com/membershiphub/notification/model/` | `AttendanceEvent`, `NotificationPayload`, `ZaloMessage`, `PushMessage`. |
| **Configuration** | `src/main/resources/application.yaml` | Tenant‑aware Kafka topics, Zalo credentials (Secret Manager reference), FCM service account path, retry policies, OPA scopes. |
| **Docker** | `Dockerfile.notification` (multi‑stage) | Builds native GraalVM image (optional) or JVM image; includes `cosign` verification step in CI. |
| **Helm Chart** | `helm/notification-service/` | `values.yaml` (image, replicaCount, resources, podSecurity, networkPolicy). |
| **OpenTelemetry** | `src/main/java/com/membershiphub/notification/otel/` | `TracingConfig` (auto‑instrumentation). |
| **Test Suite** | `src/test/java/com/membershiphub/notification/` | Unit, contract (Pact), integration (Testcontainers Kafka + Postgres), end‑to‑end (Cypress for mobile push verification). |
| **CI/CD** | `.github/workflows/notification-ci.yml` | Build → Trivy scan → Cosign sign → Push to Artifact Registry → ArgoCD sync. |

**Forbidden Scope for Phase 4**  
- Any changes to **user‑management** (`/auth/`), **tenant provisioning**, or **frontend** code.  
- Modifications to **core Kafka topics** other than `attendance-events`, `notification-events`, `notification-audit`.  
- Direct DB schema migrations (handled in Phase 2).  

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Tasks (ordered) | Artefacts / Deliverables |
|-----------|-----------------|--------------------------|
| **Coder** | 1. Scaffold `notification-service` module (Maven/Gradle) under `membership-hub/notification`. <br>2. Implement `AttendanceConsumer` with **exact‑once** processing using Kafka **transactional producer** for audit events. <br>3. Build idempotent attendance handler: query Postgres `attendance` table (row‑level security) → if record exists for tenant+learner+date, skip; else create and compute remaining days. <br>4. Develop `ZaloMessageClient` & `ZaloGroupClient` using **Feign** (or RestEasy) with **Resilience4j** retry & circuit‑breaker. <br>5. Implement `FcmPushClient` via Firebase Admin SDK. <br>6. Wire OpenTelemetry tracing (span names: `attendance.consume`, `notification.send.zalo`, `notification.send.fcm`). <br>7. Add configuration validation (MicroProfile Config) and OPA scope checks (`notification:send`). <br>8. Write Dockerfile (`Dockerfile.notification`) with GraalVM native image option, multi‑stage, and `ENTRYPOINT ["./notification-service"]`. | - Source code in paths above.<br>- `README.md` with run‑local instructions (Docker Compose with Kafka, Postgres, Zalo mock server). |
| **Tester** | 1. Unit tests for each client (mock Zalo/Firebase endpoints). <br>2. Contract tests (Pact) for Zalo Business API (request/response schemas). <br>3. Integration test using **Testcontainers**: spin up Kafka, Postgres, publish an `AttendanceEvent`, assert a single `notification‑audit` record and successful external calls (mocked). <br>4. End‑to‑end test script (`e2e/notification-flow.sh`) that triggers a QR‑scan simulation via the existing attendance API, then verifies push via Firebase emulator and Zalo mock. <br>5. Load test scenario (`k6/notification-load.js`) – 10 k scans/min for 5 min, capture latency & error rates. <br>6. Security test: attempt to send a notification with an invalid JWT → expect 403 (OPA). | - `src/test/...` files.<br>- `pact/` contracts.<br>- `k6/` scripts.<br>- Test report (JUnit XML) uploaded as CI artifact. |
| **Reviewer** | 1. Perform **static analysis** with SonarQube (quality gate ≥ A). <br>2. Verify **OPA policies** are referenced in code (`@RolesAllowed("notification:send")`). <br>3. Review Dockerfile for best‑practice (non‑root user, minimal layers). <br>4. Ensure **dependency versions** are up‑to‑date; no known CVEs (via Dependabot). <br>5. Confirm **audit logging**: every outbound message writes to `notification-audit` and Cloud Audit Logs (check logger config). <br>6. Approve **Helm chart** values: resource limits, pod security standards, network policies restricting egress to Zalo & FCM endpoints only. | - PR review checklist completed.<br>- Signed off OPA policy diff.<br>- SonarQube report link. |
| **DevOps / Deployer** (named **Deployer** in persona list) | 1. Add CI workflow `.github/workflows/notification-ci.yml` – steps: build, unit test, Trivy scan, Cosign sign, push to Artifact Registry, trigger ArgoCD sync. <br>2. Create Helm release `notification-service` in `helm/notification-service/` with values for **auto‑scaling** (HPA based on CPU & Kafka consumer lag). <br>3. Define **Kubernetes NetworkPolicy** allowing egress only to `*.zalo.me:443` and `fcm.googleapis.com:443`. <br>4. Configure **Binary Authorization** policy to require Cosign signatures. <br>5. Set up **Prometheus ServiceMonitor** and **Grafana dashboard** (latency, consumer lag, error rate). <br>6. Add **Alertmanager** rule: `notification_service_latency_seconds > 0.2` for 5m → page. <br>7. Perform a **blue‑green rollout** in a staging GKE cluster, run the full integration test suite, then promote to production. | - CI YAML file.<br>- Helm chart (templates, values).<br>- K8s manifests (NetworkPolicy, ServiceMonitor, HPA).<br>- Grafana dashboard JSON.<br>- Release notes documenting version bump. |

## 4. Phase Definition of Done (DoD)  

The phase is considered **Done** when **all** items below are satisfied and signed off by the **Manager**:

1. **Functional**  
   - Attendance events processed exactly once per tenant/day.  
   - Push notification (FCM) and Zalo message (individual & group) are sent for every successful attendance.  
   - Idempotency verified by integration test (multiple scans → single attendance record).  

2. **Non‑Functional**  
   - End‑to‑end latency ≤ 200 ms (95th percentile) under load‑test target.  
   - Delivery success rate ≥ 99.9 % for both channels.  
   - No critical CVEs in the container image; image size ≤ 150 MB (native) or ≤ 300 MB (JVM).  

3. **Compliance & Security**  
   - All outbound calls are logged to `notification-audit` Kafka topic and Cloud Audit Logs.  
   - OPA policies enforce `notification:send` scope; unauthorized attempts return 403.  
   - TLS 1.3 enforced for all inbound/outbound traffic; secrets sourced from Secret Manager.  

4. **Observability**  
   - OpenTelemetry spans exported; Grafana dashboard shows real‑time latency, consumer lag, error rates.  
   - Alerting rules are active and tested (triggered on simulated failure).  

5. **Quality Assurance**  
   - Unit coverage ≥ 80 %; integration coverage ≥ 70 %.  
   - SonarQube quality gate passed (no blocker/critical issues).  
   - All contract tests (Pact) verified against mock Zalo server.  

6. **CI/CD**  
   - Pipeline runs automatically on PR merge, produces signed image, and deploys to **staging** GKE cluster without manual intervention.  
   - Blue‑green promotion to **production** completed, with zero‑downtime verification (health endpoint 200 OK).  

7. **Documentation**  
   - Updated `README.md` with local dev, deployment, and troubleshooting sections.  
   - Architecture diagram (notification flow) added to Confluence and linked in the repo.  
   - Helm chart README includes values explanation and upgrade notes.  

8. **Sign‑off**  
   - Manager signs the **Phase 4 Review Checklist** confirming all above criteria.  
   - Reviewer signs off on code quality and security compliance.  
   - Deployer signs off on successful production rollout and monitoring configuration.  

*Only after the above sign‑offs is the project allowed to proceed to Phase 5 (Scaling, Observability & Production Roll‑out).*