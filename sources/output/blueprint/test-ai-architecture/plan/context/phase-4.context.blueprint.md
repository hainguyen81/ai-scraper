# PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture  

## 1. Phase Operational Scope & Objectives  

| Objective | Description | Success Indicator |
|-----------|-------------|--------------------|
| **Implement Notification Engine** | Build a dedicated micro‑service that consumes attendance events from Kafka, calculates remaining membership days, and dispatches messages via **Zalo Business API**, **Firebase Cloud Messaging (FCM)**, and optional email/SMS templates. | All attendance events trigger exactly one notification per learner (idempotent) and membership‑day decrement is persisted correctly. |
| **Business Rules & Tenant‑Specific Branding** | Encode configurable rules per tenant: <br>• Membership‑day decrement policy (daily, weekly, custom). <br>• Message templates (language, placeholders, branding assets). <br>• Opt‑out / Do‑Not‑Disturb flags. | Tenant admin can edit rules via a JSON/YAML config stored in PostgreSQL `tenant_settings` and changes take effect without redeploy. |
| **Integrate with Existing Core Services** | Subscribe to the **`attendance.events`** Kafka topic, enrich payload with user profile (via Keycloak/User Service), and publish **`notification.outbound`** events for downstream analytics. | End‑to‑end flow: QR check‑in → attendance event → notification service → Zalo/FCM delivery, observable in Cloud Logging. |
| **Guardrail Compliance** | Enforce GDPR/CCPA consent checks before any personal data is sent to Zalo, apply **Istio mTLS** for inter‑service calls, and log immutable audit records. | CI pipeline blocks build on missing consent flag or failed security scan; runtime alerts fire on policy violations. |
| **Observability & Monitoring** | Export OpenTelemetry traces, Prometheus metrics (e.g., `notifications_sent_total`, `notification_failures_total`), and Cloud Logging with structured fields (`tenant_id`, `user_id`, `channel`). | Dashboards show < 5 % failure rate and latency < 200 ms for notification dispatch. |
| **Testing & Quality Gates** | Achieve ≥ 90 % unit test coverage, full contract tests against the Kafka schema, and end‑to‑end integration tests covering all three channels (Zalo, FCM, Email). | All quality gates pass in GitHub Actions; no critical findings in SonarQube or Trivy. |

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Allowed Path / Package | Example Files | Public API Endpoints (REST) |
|------|------------------------|---------------|-----------------------------|
| **Micro‑service (notification)** | `src/main/java/com/membershiphub/notification/` | `NotificationService.java`, `ZaloClient.java`, `FcmPublisher.java`, `TenantConfigProvider.java` | `POST /api/v1/notifications/preview` (admin preview of template) <br> `GET /api/v1/tenants/{tenantId}/settings` (read‑only) |
| **Domain Models** | `src/main/java/com/membershiphub/notification/model/` | `AttendanceEvent.java`, `NotificationPayload.java`, `TenantSettings.java` | – |
| **Kafka Integration** | `src/main/java/com/membershiphub/notification/kafka/` | `AttendanceConsumer.java`, `OutboundProducer.java`, `KafkaConfig.java` | – |
| **Configuration** | `src/main/resources/` | `application.yml` (Quarkus), `tenant-defaults.yaml` | – |
| **Docker** | Root `Dockerfile.notification` (multi‑stage) | `Dockerfile.notification` | – |
| **Helm Chart** | `helm/notification/` | `Chart.yaml`, `values.yaml`, `templates/deployment.yaml` | – |
| **Tests** | `src/test/java/com/membershiphub/notification/` | `NotificationServiceTest.java`, `ZaloClientIT.java`, `KafkaContractTest.java` | – |
| **OpenAPI Spec** | `src/main/resources/openapi/notification.yaml` | – | – |
| **Observability** | `src/main/java/com/membershiphub/notification/observability/` | `MetricsCollector.java`, `TracingFilter.java` | – |

**Endpoints that must **not** be modified in this phase** (owned by other phases):  

- `/api/v1/attendance/**` – attendance micro‑service (Phase 2).  
- `/api/v1/users/**` – identity service (Phase 2).  
- `/api/v1/web/**` – web portal (Phase 3).  

Any new endpoint must be versioned under `/api/v1/notifications/**` and declared in the OpenAPI spec.

## 3. Dedicated Sub‑Agent Functional Directives  

| Sub‑Agent | Concrete Tasks (ordered) | Guardrail Checks |
|-----------|--------------------------|------------------|
| **Coder** | 1. Scaffold Quarkus project under `notification` module (use Maven `quarkus-maven-plugin`). <br>2. Define Kafka consumer (`attendance.events`) with exactly‑once processing semantics (enable idempotent store using `processed_event_id` table). <br>3. Implement `MembershipDayService` that reads `users.membership_end_date` and decrements based on tenant rule. <br>4. Build `ZaloClient` using Zalo Business API (OAuth2 token refresh, rate‑limit handling). <br>5. Build `FcmPublisher` using Firebase Admin SDK (batch send, exponential back‑off). <br>6. Create `TenantConfigProvider` that loads per‑tenant JSON from PostgreSQL `tenant_settings` (cached with Caffeine, refreshed every 5 min). <br>7. Add OpenAPI annotations for admin preview endpoint. <br>8. Write Dockerfile (`Dockerfile.notification`) – multi‑stage GraalVM native image, size ≤ 150 MB. <br>9. Add Helm chart values for `resources.limits` and `resourceQuotas` per tenant namespace. | - Run **Checkov** on Helm & Terraform (no hard‑coded secrets). <br>- Run **Hadolint** on Dockerfile. <br>- Ensure all external calls (Zalo, FCM) are behind **Istio mTLS** (service mesh policy). |
| **Tester** | 1. Write unit tests for `MembershipDayService` covering all rule variations (daily, weekly, custom). <br>2. Write contract tests using **Karate** to validate Kafka schema (`attendance.events`). <br>3. Implement integration test that publishes a mock attendance event to an embedded Kafka, asserts a single outbound `notification.outbound` message and that Zalo/FCM mocks receive correct payload. <br>4. Add end‑to‑end test using **Postman/Newman** for the admin preview endpoint (template rendering, locale substitution). <br>5. Create performance test (JMeter) simulating 5 k attendance events/minute, verify latency < 200 ms. <br>6. Run accessibility scan on any admin UI generated by the preview endpoint (axe‑core). | - Enforce **OWASP ZAP** scan on any HTTP endpoint. <br>- Verify test coverage ≥ 90 % (JaCoCo). <br>- Ensure GDPR consent flag is asserted in every test case that sends personal data. |
| **Reviewer** | 1. Review PR for coding standards (Spotless, Checkstyle). <br>2. Validate that all new tables (`processed_event_id`, `notification_audit`) have **Row‑Level Security (RLS)** policies and audit triggers. <br>3. Confirm OpenAPI spec is complete and matches implementation (Swagger UI auto‑generated). <br>4. Verify that secret values (Zalo API key, Firebase service account) are referenced only via **Google Secret Manager** and injected as env vars. <br>5. Approve Helm chart after running **helm lint** and **kube-score**. <br>6. Sign‑off that all guardrails (GDPR, ISO‑27001, NIST) are satisfied; add checklist entry. | - Block merge if SonarQube quality gate < A or Trivy scan finds **CRITICAL** vulnerabilities. <br>- Ensure no hard‑coded URLs or credentials. |
| **DevOps (Deployer)** | 1. Add Helm release `notification-service` to Argo CD `applications.yaml` with automated sync policy (auto‑promote from staging to prod after manual approval). <br>2. Create Terraform module `notification` that provisions a dedicated **Kafka consumer group** and **IAM service account** with least‑privilege (publish to `notification.outbound`). <br>3. Configure **Istio VirtualService** and **DestinationRule** for mTLS, circuit‑breaker (max 5 xx errors). <br>4. Set up **PrometheusRule** alerts: `NotificationFailureRateHigh`, `NotificationLatencySLOBreached`. <br>5. Extend Cloud Logging sink to include `notification` logs with retention 365 days and KMS‑signed integrity. <br>6. Perform a blue‑green rollout in a staging namespace, run smoke tests, then promote to prod. | - CI pipeline must pass **Trivy**, **Checkov**, **Hadolint**, **SAST** before image is pushed. <br>- Deployment must respect **ResourceQuota** per tenant namespace (CPU ≤ 2, Memory ≤ 1Gi). <br>- Verify that GKE **PodSecurityPolicy** disallows privileged containers. |

## 4. Phase Definition of Done (DoD)  

- **Code & Build**  
  - All source files reside within the directories listed in Section 2.  
  - Docker image built as `gcr.io/<project-id>/notification-service:<git‑sha>` and passes Trivy scan (no HIGH/CRITICAL).  
  - Maven `quarkus:build` succeeds; native image size ≤ 150 MB.  

- **Testing**  
  - Unit test coverage ≥ 90 % (JaCoCo).  
  - Contract tests against Kafka schema pass on both local and CI Kafka clusters.  
  - Integration test suite runs in CI and reports 100 % success.  
  - Performance test shows average processing latency ≤ 200 ms under 5 k events/min.  
  - Accessibility scan on admin preview endpoint reports no WCAG 2.1 AA violations.  

- **Security & Compliance**  
  - No secrets in repo; all secret references use Google Secret Manager.  
  - RLS policies applied to new tables; audit logs are write‑once and signed with Cloud KMS.  
  - GDPR consent flag validated before any Zalo/FCM dispatch; DSAR API endpoint documented.  
  - Istio mTLS enabled for all inbound/outbound calls of the notification service.  

- **Documentation**  
  - Updated **Architecture Decision Records (ADR-04)** describing notification engine design.  
  - OpenAPI spec (`notification.yaml`) published to the API portal.  
  - Runbook includes steps for: <br>  • Rolling back the notification service <br>  • Rotating Zalo API credentials <br>  • Handling a GDPR data‑subject request for notification logs.  

- **Deployment**  
  - Helm chart version `0.3.0` deployed to **staging** namespace, passes smoke tests.  
  - Argo CD sync status **Healthy**; all resources show `Ready` condition.  
  - Prometheus alerts are active and fire test alerts successfully.  

- **Phase Gate Review**  
  - Manager and Reviewer sign‑off on the Phase Gate checklist confirming:  
    1. All guardrails (Section 2) are satisfied.  
    2. Quality gates (SonarQube ≥ A, Trivy clean, Checkov pass).  
    3. Documentation is complete and version‑controlled.  
    4. Stakeholder demo performed and acceptance criteria met.  

When all items above are verified, **Phase 4 is considered DONE** and the pipeline may promote the notification service to the **production** environment, unlocking Phase 5 (Productionization & Compliance Hardening).