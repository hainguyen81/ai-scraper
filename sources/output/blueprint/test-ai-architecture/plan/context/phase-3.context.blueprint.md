# PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture  

## 1. Phase Operational Scope & Objectives  

| Goal | Description | Business Value |
|------|-------------|----------------|
| **Mobile Extension** | Deliver a cross‑platform mobile application (iOS & Android) built with **React Native (Expo) + React‑Native‑for‑Web** that re‑uses the Next.js component library and i18n assets. | Learners can scan QR codes, view membership day‑counter, receive push & Zalo notifications on‑the‑go. |
| **Multi‑Center Tenant Isolation** | Implement true multi‑tenant support at the data‑layer (center_id foreign key) and optional Kubernetes namespace per center for runtime isolation. | Enables multiple education centers to operate concurrently on the same SaaS instance without data leakage. |
| **Scalable Event & Service Fabric** | Refine Kafka partitioning, consumer group design, and Horizontal Pod Autoscaling (HPA) rules to support **≥5 k concurrent active users** across at least **3 centers**. | Guarantees low latency attendance processing and notification dispatch under peak load. |
| **Zalo & Push Notification Integration** | Wire‑up **Zalo Business API** and **Firebase Cloud Messaging (FCM)** as downstream consumers of the `attendance-notify` Kafka topic. | Real‑time communication improves learner engagement and reduces missed sessions. |
| **Locale Detection & i18n Consistency** | Consolidate locale‑resolution logic (user‑profile → cookie → device/browser) into a shared library used by both Next.js web and React Native apps. | Guarantees a seamless multilingual experience across all touch‑points. |
| **Observability & Guardrail Enforcement** | Extend OpenTelemetry instrumentation to mobile SDKs, add Prometheus metrics for Kafka lag, and enforce OPA policies for tenant‑scoped API access. | Maintains compliance, performance visibility, and security posture as the system scales. |

**Success Metrics**  

- Mobile app passes **device‑farm** test matrix: iOS 14‑17, Android 10‑13, 100 % crash‑free sessions.  
- End‑to‑end attendance flow (QR → Kafka → PostgreSQL → Zalo/FCM) completes within **≤300 ms** (95th percentile) under 5 k concurrent users.  
- Multi‑tenant data isolation verified by automated integration tests (no cross‑center leakage).  
- Autoscaling reacts to CPU ≥ 70 % or Kafka lag ≥ 200 msg within **30 s**.  

---

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)  

| Layer | Repository / Directory | Allowed Files / Paths | Public API Endpoints (REST) |
|-------|------------------------|----------------------|-----------------------------|
| **Backend (Quarkus)** | `backend/` | `src/main/java/com/membershiphub/**`<br>`src/main/resources/application.yml`<br>`src/main/resources/db/migration/**`<br>`Dockerfile` | `POST /api/v1/auth/login` (internal & Firebase)<br>`GET /api/v1/centers/{centerId}/learners`<br>`POST /api/v1/attendance/scan` (QR payload)<br>`GET /api/v1/learners/{learnerId}/membership` |
| **Kafka** | `infra/kafka/` | `topics.yaml` (definition of `attendance`, `attendance-notify`, `notification-out`)<br>`consumer-config/attendance-consumer.yml` | N/A (internal) |
| **PostgreSQL / TimescaleDB** | `infra/db/` | `schema.sql`<br>`migrations/V*/**.sql` | N/A (internal) |
| **Web Front‑end (Next.js)** | `frontend/web/` | `pages/**`, `components/**`, `i18n/**`, `public/locales/**`, `next.config.js` | `GET /` (SSR home)<br>`GET /[locale]/dashboard` |
| **Mobile Front‑end (React Native)** | `frontend/mobile/` | `src/**`, `app.json`, `eas.json`, `i18n/**` (symlinked to web i18n) | N/A (client) |
| **Infrastructure as Code** | `infra/helm/` | `charts/membership-hub/**`, `values.yaml` | N/A |
| **Observability** | `infra/monitoring/` | `otel-collector-config.yaml`, `prometheus-rules.yaml` | N/A |
| **Security / Guardrails** | `security/` | `opa/policies/**`, `istio/virtualservice.yaml` | N/A |

**Endpoint Access Matrix (Tenant‑aware)**  

| Endpoint | Auth Required | Tenant Scope | Rate Limit |
|----------|---------------|--------------|------------|
| `/api/v1/attendance/scan` | JWT (internal) **or** Firebase ID token | Must include `centerId` claim matching JWT/ID token | 30 req/s per user |
| `/api/v1/learners/{id}/membership` | JWT | `centerId` claim must match learner’s center | 10 req/s |
| `/api/v1/centers/{centerId}/learners` | JWT (admin role) | Exact `centerId` path param | 5 req/s |

All new files must reside under the directories above; any deviation requires Manager approval.

---

## 3. Dedicated Sub‑Agent Functional Directives  

### Coder  
1. **Mobile App Scaffold** – Initialize Expo project, integrate `react-native-web` to share UI components with Next.js. Implement screens: **Login**, **Dashboard**, **QR Scanner**, **Membership Card**.  
2. **Locale Service** – Create `src/lib/locale.ts` exposing `detectLocale()` that follows: user‑profile → stored cookie → device locale → fallback `en-US`. Export same API for web via a shared npm package (`@membershiphub/i18n`).  
3. **Multi‑Tenant DB Layer** – Extend Flyway migrations: add `center_id UUID NOT NULL` to `learners`, `attendance`, `notifications` tables; create composite unique index on `(center_id, learner_id, attendance_date)`. Update JPA entities and repository queries to always filter by `centerId`.  
4. **Kafka Partition Strategy** – Define topic `attendance` with **3 partitions per center** (partition key = `centerId`). Update producer config in Quarkus to set `partitionKey`.  
5. **Zalo & FCM Consumers** – Implement two new Quarkus consumers (`ZaloNotifier`, `FCMNotifier`) subscribed to `attendance-notify`. Each reads tenant‑scoped config (Zalo API key, FCM server key) from Secret Manager.  
6. **Autoscaling Manifests** – Add HPA YAML in `infra/helm/charts/membership-hub/templates/hpa.yaml` with CPU target 70 % and custom metric `kafka_consumer_lag`.  
7. **Observability** – Instrument mobile SDK with OpenTelemetry (React Native auto‑instrumentation) and add custom span `qr.scan`. Export to GCP Cloud Trace via Collector sidecar.  

### Tester  
1. **End‑to‑End Mobile Flow** – Write Cypress‑compatible **Detox** tests: login → scan QR (mock camera) → verify attendance record via API → assert push notification received (FCM mock) → assert Zalo message payload in test double.  
2. **Multi‑Tenant Isolation Tests** – Create integration test suite (JUnit + Testcontainers) that spins two centers, registers learners with same email, performs attendance in each, and asserts no cross‑center data appears.  
3. **Load & Stress** – Use **k6** script to simulate 5 k concurrent mobile users scanning QR simultaneously across 3 centers; capture latency, error rate, Kafka lag.  
4. **Locale Verification** – Automated UI tests for each supported locale (vi‑VN, en‑US, zh‑CN) confirming UI strings, date formats, and SEO meta tags (via SSR).  
5. **Security Regression** – Run OWASP ZAP scan against new mobile API endpoints; ensure no new high‑severity findings.  

### Reviewer  
1. **Code Review Checklist** – Verify:  
   - All new services use **non‑root** Docker user (`USER 1001`).  
   - Secrets accessed only via **Secret Manager**; no env‑var hard‑coding.  
   - JPA queries include `centerId` filter; no raw SQL bypass.  
   - OpenAPI spec updated for new endpoints with proper request/response schemas.  
2. **Architecture Conformance** – Confirm that the mobile codebase imports the shared i18n package; no duplicate string files.  
3. **Guardrail Enforcement** – Run OPA policy checks (`opa eval`) on PR diff to ensure no violation of tenant‑scoped access or rate‑limit definitions.  
4. **Documentation** – Update `README.md` in `frontend/mobile/` with build instructions for iOS/Android, and add a **Tenant‑Isolation** section in the architecture wiki.  

### DevOps (Deployer & Docker)  
1. **Docker Image Pipeline** – Extend GitHub Actions workflow:  
   - Build **multi‑stage Dockerfile** for Quarkus native image (optional) and React Native bundle (Expo).  
   - Run **Trivy** scan; fail on CRITICAL vulnerabilities.  
   - Push images to **Artifact Registry** with tags `sha-${{ github.sha }}` and `latest`.  
2. **Helm Chart Enhancements** – Add values for `mobile.enabled` (true) and `tenantNamespaces.enabled` (true). Generate a Helm sub‑chart `mobile` that creates a Deployment with `nodeSelector` for GPU‑enabled nodes (if needed for QR scanning).  
3. **Canary Release Strategy** – Configure Argo CD ApplicationSet to roll out new mobile backend version to **10 % of pods** for each center, monitor `attendance-notify` lag, then promote.  
4. **Backup & DR** – Schedule **CloudSQL cross‑region replica** for the new `center_id`‑partitioned tables; verify point‑in‑time recovery (PITR) works for tenant data.  
5. **Monitoring Dashboards** – Add Grafana panels: `mobile_app_crash_rate`, `kafka_lag_by_center`, `hpa_current_replicas`. Set alerts for `hpa_replicas > 0 && cpu > 80%` lasting > 2 min.  

---

## 4. Phase Definition of Done (DoD)  

- **Code**: All source files compiled, unit‑tested (≥ 80 % coverage), and merged to `main` with **Reviewer** approval and OPA policy pass.  
- **Container Images**: Docker images for backend (Quarkus) and mobile (Expo) built, scanned (no critical vulns), and stored in Artifact Registry with immutable digests.  
- **Infrastructure**: Helm chart version `3.x` deployed via Argo CD to a **GKE regional cluster**; HPA, network policies, and tenant namespaces active.  
- **Functional**: End‑to‑end mobile attendance flow works for at least **3 distinct centers**; membership day‑counter updates correctly; Zalo & FCM notifications delivered (verified in test environment).  
- **Performance**: Load test (k6) shows ≤ 300 ms 95th‑percentile latency for `/attendance/scan` under 5 k concurrent users; Kafka lag < 100 msgs per partition.  
- **Security & Compliance**: OWASP ZAP scan reports **0** high‑severity issues; all secrets stored in Secret Manager; audit logs emitted to Cloud Logging with immutable retention.  
- **Internationalization**: UI renders correctly in all supported locales; SEO meta tags (`hreflang`, `canonical`, `sitemap.xml`) generated per locale; locale detection follows the defined hierarchy.  
- **Observability**: OpenTelemetry traces visible in Cloud Trace for mobile and backend; Grafana dashboards show real‑time metrics; alerts configured and tested.  
- **Documentation**: Updated architecture diagram (Phase 3 additions), README for mobile build/deploy, tenant‑isolation guide, and run‑books for scaling and disaster recovery.  

**Go/No‑Go Gate**: The Manager, Reviewer, and Tester must sign off on the checklist above. Only after sign‑off can the project proceed to Phase 4 (SEO, Internationalization & Compliance Hardening).