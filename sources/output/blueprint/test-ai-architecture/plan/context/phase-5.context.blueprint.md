<think>
Here's a thinking process:

1.  **Analyze User Input:**
   - **Project Name:** `membership-hub` (but context title is `test-ai-architecture`)
   - **Task:** Detail **PHASE 5 OUT OF 5**
   - **Global Context & Raw Requirements:** Provided in the prompt. Key points:
     - Web admin + Mobile student app
     - Backend: Quarkus, Kafka, PostgreSQL, scalable, Docker, GCP/GKE
     - Auth: Internal (email/pass) + External (Firebase, Google, Facebook)
     - Multi-tenant: Supports multiple training centers
     - Attendance: QR check-in, idempotent per day, shows remaining validity days
     - Notifications: Zalo (phone & group), Mobile push
     - Mobile: Next.js frontend, multi-language, iOS/Android builds
     - SEO: Multi-language SEO for web & mobile
     - Locale: User preference > browser/device locale
   - **Required Output Structure:**
     ```
     # PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture
     ## 1. Phase Operational Scope & Objectives
     ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
     ## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
     ## 4. Phase Definition of Done (DoD)
     ```

2.  **Determine Phase 5 Focus:**
   - Since it's Phase 5 out of 5, it should be the final phase: Production Deployment, Observability, Performance Optimization, Security Hardening, CI/CD Automation, and Handover/Documentation.
   - It must align with the global context (GCP/GKE, Docker, Quarkus, Kafka, Next.js, multi-tenant, auth, attendance, notifications, i18n/SEO).
   - I need to strictly isolate development boundaries so sub-agents never overlap.

3.  **Draft - Section by Section:**

   *## 1. Phase Operational Scope & Objectives*
   - Focus: Production readiness, GKE deployment, CI/CD pipeline finalization, observability stack, performance tuning, security hardening, and operational handover.
   - Objectives:
     - Deploy fully containerized architecture to GKE with autoscaling & high availability.
     - Finalize CI/CD pipelines (build, test, security scan, deploy, rollback).
     - Implement comprehensive observability (metrics, logging, tracing, alerting).
     - Conduct load/stress testing & performance optimization for Quarkus, Kafka, Postgres, Next.js.
     - Harden security (WAF, secrets management, RBAC, audit trails, compliance checks).
     - Deliver production-ready documentation & runbooks.

   *## 2. Allowed Technical Scope & Directory Boundaries*
   - Need to define strict boundaries for files, paths, endpoints, and infrastructure components to prevent overlap.
   - Structure:
     - `/infra/gke/` (Helm charts, K8s manifests, networking, ingress, autoscaling)
     - `/infra/cicd/` (GitHub Actions/GitLab CI, Docker build pipelines, security scanning)
     - `/infra/observability/` (Prometheus, Grafana, OpenTelemetry, ELK/Loki, alerting rules)
     - `/backend/quarkus/` (Production configs, health checks, metrics endpoints, Kafka consumer tuning)
     - `/frontend/nextjs/` (Production build optimization, SEO metadata finalization, i18n routing, PWA/native build configs)
     - `/security/` (WAF rules, secret rotation, RBAC policies, audit logging)
     - `/docs/` (Runbooks, architecture diagrams, deployment guides, monitoring dashboards)
   - Boundaries: Explicitly state what each agent can touch. No cross-phase feature development. Only production hardening, deployment, and observability.

   *## 3. Dedicated Sub-Agent Functional Directives*
   - Need specific tasks for Coder, Tester, Reviewer, DevOps (Docker/Deployer merged into DevOps per prompt, but I'll keep it aligned with the requested names: Coder, Tester, Reviewer, DevOps).
   - *Coder*: Focus on production-ready code adjustments only. Implement health/readiness probes, OpenTelemetry instrumentation, Kafka consumer tuning, Next.js production build optimization, i18n/SEO finalization, locale fallback logic verification. NO new features.
   - *Tester*: Focus on production validation. Load/stress testing (k6/Locust), chaos engineering (network/partition failures), E2E production smoke tests, notification delivery validation (Zalo/Push), multi-tenant isolation verification, SEO/i18n crawl tests.
   - *Reviewer*: Focus on production readiness audit. Security compliance (OWASP, CIS benchmarks), performance bottleneck analysis, architecture alignment check, CI/CD pipeline review, observability coverage validation, rollback strategy approval.
   - *DevOps*: Focus on GKE deployment & infrastructure. Helm chart finalization, GKE cluster provisioning, autoscaling (HPA/VPA), ingress/WAF configuration, secret management (GCP Secret Manager), CI/CD pipeline execution, monitoring/alerting setup, disaster recovery runbooks.

   *## 4. Phase Definition of Done (DoD)*
   - Clear, measurable criteria for phase completion.
   - Infrastructure: GKE cluster live, HPA/VPA configured, ingress/WAF active, secrets managed.
   - CI/CD: Fully automated pipeline (build → test → scan → deploy → rollback), zero manual steps.
   - Observability: Metrics, logs, traces centralized, dashboards live, alerting rules configured & tested.
   - Performance: Load test passes (e.g., 95th percentile < 200ms, Kafka lag < 100, DB connection pool optimized).
   - Security: Pen test passed, secrets rotated, RBAC enforced, audit logs active, compliance verified.
   - Documentation: Runbooks, architecture diagrams, monitoring guides, deployment procedures complete.
   - Sign-off: All sub-agents confirm boundaries respected, no feature creep, production-ready state achieved.

4.  **Refine & Align with Constraints:**
   - Check against raw requirements: GCP/GKE, Docker, Quarkus, Kafka, Postgres, Next.js, multi-tenant, auth, attendance, notifications, i18n/SEO, locale detection. All are addressed in the context of Phase 5 (production hardening, deployment, observability, validation).
   - Check structure: Matches exactly.
   - Check boundaries: Explicitly isolated. No overlap. Each agent has strict scope.
   - Tone: Elite Solution Architect. Precise, technical, authoritative.
   - Language: English (as requested/implied by prompt structure).

   I'll draft it carefully, ensuring technical depth and strict adherence to the prompt. I'll make sure the boundaries are crystal clear to prevent sub-agent overlap. I'll use precise paths, endpoints, and configuration scopes. I'll align everything with the global context.

   Self-Correction/Verification during drafting:
   - The prompt says "Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)". I'll stick to these 4.
   - I need to ensure the directory boundaries explicitly map to the tech stack (Quarkus, Kafka, Postgres, Next.js, GKE, Docker).
   - I'll add specific endpoints/paths for observability, health checks, and production configs.
   - I'll emphasize that Phase 5 is strictly for production readiness, deployment, and observability. NO new business logic.
   - I'll ensure the DoD is measurable and verifiable.

   Structure looks solid. I'll generate the response now. 
   Output matches the required format exactly. Technical depth is high. Boundaries are strict. Aligns with all raw requirements in the context of Phase 5.✅
   Proceed. 
   Output Generation. 
   [Done] 
   *Self-Correction/Note during thought*: 
   The prompt says "Isolate development boundaries so sub-agents never overlap." I will explicitly define file/path/endpoint boundaries per agent and state cross-contamination rules. I'll also ensure the tech stack references (Quarkus, Kafka, Postgres, Next.js, GKE, Docker) are correctly scoped to Phase 5 activities (production hardening, deployment, observability, validation). All good. 
   Output matches response. 
   Proceeds. 
   [Output Generation] -> *See response.* 
   *(Note: I will maintain the exact markdown structure requested.)*
   `# PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture`
   `## 1. Phase Operational Scope & Objectives`
   `## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)`
   `## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)`
   `## 4. Phase Definition of Done (DoD)`
   All sections will be filled with precise, architect-level content.✅
   Ready. 
   [Output Generation] -> *Proceeds.*
</think>

# PHASE 5 CONTEXT BLUEPRINT: test-ai-architecture

## 1. Phase Operational Scope & Objectives
**Phase 5** is strictly a **Production Readiness,