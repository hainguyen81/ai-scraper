<think>
Here's a thinking process:

1.  **Analyze User Input:**
    - **Project Name:** membership-hub
    - **Phase:** 5 out of 5
    - **Global Context:** Provided in detail. Covers tech stack (Java 17, Quarkus, Kafka, PostgreSQL, Next.js, Tailwind, i18n, Firebase/Google/FB OAuth, Zalo/FCM notifications, AI chat, GCP/GKE deployment), guardrails (package paths, workspace boundaries, tester syntax, performance rules, phase discipline 1-7 days, security, observability), sub-agent personas (Manager, Coder, Tester, Reviewer, DevOps), and a 5-phase plan.
    - **Phase 5 Plan (from context):** Duration 5-7 days. Backend: E2E integration testing, performance tuning (native SQL, Kafka backpressure), production-grade Docker images & GKE deployment scripts, monitoring & logging config. Frontend: Polished mobile app (iOS/Android builds), final UI refinements, end-user documentation & rollout checklist, final QA sign-off and hypercare preparation.
    - **Raw Requirements:** Covers web admin + mobile app, Java 17/Quarkus/Kafka/Postgres, multi-tenant centers, QR attendance (daily flag), student card expiry, Zalo/FCM notifications, Next.js frontend with i18n & SEO, role-based access (SysAdmin, Admin, Manager, Teacher, Student), various management screens (Centers, Dashboard, Courses, Teachers, Students, Promotions, Announcements, AI Chat), mobile app mirroring web with role-based views and push notifications.
    - **Constraints:** Strict 1-7 day limit per phase. Stop immediately when objectives are met. Output must follow a specific Markdown structure. Must break down Phase 5 into DAY 1 to DAY X (max 7). Group by Day -> Sub-Task -> Agent -> Target Paths. Strict path syntax rules. Must cover both backend and frontend. Tester syntax: `<source>;<test>` or `INTEGRATION_SCOPE;<test>`.

2.  **Deconstruct Phase 5 Objectives (from Global Context & Raw Requirements):**
    - *Backend:* E2E integration testing, performance tuning (native SQL, Kafka backpressure), production Docker images, GKE deployment scripts, monitoring/logging config.
    - *Frontend:* Polished mobile app builds (iOS/Android), final UI refinements, end-user documentation, rollout checklist, final QA sign-off.
    - *Cross-cutting:* Finalize AI chat widget, ensure all role-based screens are polished, verify notification triggers (Zalo/FCM), validate QR attendance & card expiry logic, ensure i18n/SEO works, finalize CI/CD pipelines.
    - *Duration:* 5-7 days. I'll plan for exactly 5 days to stay within bounds and be efficient, aligning with the "5-7 days" range. I'll structure it as DAY 1 to DAY 5.

3.  **Map to Sub-Agents & Daily Breakdown:**
    - **DAY 1:** Performance Tuning & Native SQL Optimization (Backend) + Final UI Polish & i18n/SEO Validation (Frontend)
    - **DAY 2:** E2E Integration Testing & Kafka Backpressure Validation (Tester/Backend) + Mobile App Build Preparation (DevOps/Frontend)
    - **DAY 3:** Production Docker & GKE Deployment Scripts (DevOps) + Final QA Sign-off & Documentation (Manager/Tester)
    - **DAY 4:** Monitoring, Logging & Observability Setup (DevOps/Backend) + Hypercare Preparation & Rollout Checklist (Manager)
    - **DAY 5:** Final Integration Sweep & Go-Live Readiness (All Agents)

    Wait, I need to strictly follow the output structure and ensure each day has sub-tasks assigned to specific agents with target paths. I'll align closely with the Phase 5 plan from the context.

    Let's draft the structure carefully:
    # PHASE 5 CONTEXT BLUEPRINT: membership-hub
    ## 1. Phase Operational Scope & Objectives
    ## 2. Allowed Technical Scope & Directory Boundaries
    ## 3. Dedicated Sub-Agent Functional Directives
    ## 4. Phase Definition of Done (DoD)
    ## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS
    ### DAY 1: ...
    ### DAY 2: ...
    ### DAY 3: ...
    ### DAY 4: ...
    ### DAY 5: ...

    I need to ensure paths match the global context: `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/...` and `./sources/frontend/src/...`.
    I must use the exact tester syntax: `<source>;<test>` or `INTEGRATION_SCOPE;<test>`.
    I must cover backend and frontend in each phase/day as per constraints.
    I must strictly adhere to the 1-7 day limit. I'll use 5 days.

    Let's flesh out each section meticulously.

    **Section 1: Phase Operational Scope & Objectives**
    - Focus: Finalize production readiness, optimize performance, execute comprehensive testing, prepare deployment artifacts, and deliver polished UI/mobile builds.
    - Aligns with Phase 5 plan: E2E testing, performance tuning, Docker/GKE configs, monitoring, mobile builds, documentation, QA sign-off.

    **Section 2: Allowed Technical Scope & Directory Boundaries**
    - Backend: `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/...`, `./sources/backend/src/test/java/...`, `./sources/backend/pom.xml`, `./sources/backend/Dockerfile`, `./sources/backend/k8s/...`
    - Frontend: `./sources/frontend/src/...`, `./sources/frontend/package.json`, `./sources/frontend/Dockerfile`, `./sources/frontend/public/...`
    - Strict boundaries: No cross-phase leakage, all paths prefixed correctly.

    **Section 3: Dedicated Sub-Agent Functional Directives**
    - Coder: Finalize native SQL queries, Kafka backpressure configs, UI refinements, mobile build scripts.
    - Tester: Execute E2E suites, validate QR attendance/card expiry, test notification triggers, verify role-based access.
    - Reviewer: Audit performance rules, path compliance, security guards, i18n/SEO implementation.
    - DevOps: Multi-stage Dockerfiles, GKE Helm charts, CI/CD pipelines, monitoring/logging configs.
    - Manager: Orchestrate final QA, documentation, rollout checklist, hypercare prep.

    **Section 4: Phase Definition of Done (DoD)**
    - All E2E tests pass with >90% coverage.
    - Native SQL/Kafka optimizations validated under load.
    - Production Docker images built & pushed.
    - GKE deployment manifests ready.
    - Mobile apps (iOS/Android) compiled & signed.
    - Documentation & rollout checklist approved.
    - Zero critical/high vulnerabilities.

    **Section 5: DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS**
    I will structure Days 1-5. Each day will have sub-tasks for Coder, Tester, Reviewer, DevOps as appropriate. I'll ensure strict path syntax.

    *DAY 1: Performance Tuning & UI Polish*
    - Coder: Optimize native SQL for dashboard stats & card expiry. Refine mobile UI components.
    - Tester: Unit tests for optimized services.
    - Reviewer: Audit SQL & UI compliance.
    - DevOps: Prepare base Dockerfiles.

    *DAY 2: E2E Integration & Kafka Backpressure*
    - Coder: Implement Kafka backpressure configs & retry mechanisms.
    - Tester: E2E tests for QR attendance, notifications, enrollment.
    - Reviewer: Validate streaming & event consistency.
    - DevOps: CI/CD pipeline for testing env.

    *DAY 3: Production Artifacts & Mobile Builds*
    - Coder: Finalize AI chat widget integration & SEO meta tags.
    - Tester: Integration tests for AI & SEO routes.
    - Reviewer: Security & role enforcement audit.
    - DevOps: GKE Helm charts & multi-stage Docker builds.

    *DAY 4: Observability & Documentation*
    - Coder: Implement Micrometer metrics & structured logging.
    - Tester: Load testing & observability validation.
    - Reviewer: Compliance sign-off.
    - DevOps: Prometheus/Grafana configs, alerting rules.
    - Manager: Documentation & rollout checklist.

    *DAY 5: Final QA & Go-Live Readiness*
    - Coder: Hotfixes & final polish.
    - Tester: Final regression sweep.
    - Reviewer: Final audit.
    - DevOps: Production deployment dry-run.
    - Manager: Hypercare prep & sign-off.

    Now, I need to map these to the exact required format with precise paths and architectural requirements. I will carefully construct each sub-task.

    *Self-Correction/Refinement during thought:*
    - Check path syntax: Must be `./sources/backend/...` or `./sources/frontend/...`.
    - Check tester syntax: `<source>;<test>` or `INTEGRATION_SCOPE;<test>`.
    -