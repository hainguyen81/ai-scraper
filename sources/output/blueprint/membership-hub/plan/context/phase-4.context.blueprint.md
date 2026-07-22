<think>
Here's a thinking process:

1.  **Analyze User Input:**
    - **Project Name:** `membership-hub`
    - **Task:** Detail **PHASE 4 OUT OF 5**
    - **Global Context:** Provided in detail. Key points:
        - Tech Stack: Java 17, Quarkus, Kafka, PostgreSQL, Next.js, Tailwind, i18n, Firebase/Google/FB OAuth, Zalo API, FCM, AI Chat, GCP/GKE, Docker.
        - Package: `org.nlh4j.saas.membership-hub`
        - Paths: `./sources/backend/...`, `./sources/frontend/...`
        - Roles: System Admin, Admin, Manager, Teacher, Student
        - Features in Phase 4 (from context table): Role-based access control enforcement, Advanced reporting & dashboard APIs (real-time stats, interval refresh), AI CSKH integration, CI/CD pipeline stubs, Docker multi-stage builds, Full admin dashboards, Mobile push notification handling, SEO-optimized multilingual pages, AI chat widget embed.
        - Duration: 4-6 days (must be 1-7 days max)
        - Guardrails: No large in-memory loops, native SQL/Kafka for bulk, streaming parsing, strict path syntax, tester target syntax `<source>;<test>` or `INTEGRATION_SCOPE;<test>`, exact 5 phases, stop when done.
    - **Raw Requirements:** Detailed list of features. Phase 4 specifically covers:
        - Role-based access control enforcement (SysAdmin, Admin, Manager, Teacher, Student)
        - Dashboard (real-time stats, 15-min interval configurable via env)
        - AI CSKH (float chat, intent recognition for course/teacher/center queries)
        - CI/CD & Docker multi-stage builds
        - Full admin dashboards, mobile push handling, SEO multilingual pages, AI chat widget
        - Note: Some requirements from the raw list overlap with Phase 3 (enrollment, attendance, cards, notifications). Phase 4 focuses on hardening security, analytics/dashboard, AI chat, and deployment/CI-CD, plus completing responsive UI/SEO.
    - **Output Format:** Strict Markdown structure provided. Must follow exactly.
    - **Constraints:** 
        - Strict phase duration: 1-7 days. I'll aim for 5 days to match the 4-6 range.
        - Stop when done.
        - Group by Day -> Sub-Task -> Agent -> Target Path -> Requirements.
        - Path syntax: `./sources/backend/...` or `./sources/frontend/...`
        - Tester syntax: `<source>;<test>` or `INTEGRATION_SCOPE;<test>`
        - No overlap between agents. Clear boundaries.

2.  **Map Phase 4 Requirements to Days & Agents:**
    I need to distribute the Phase 4 scope across Days 1-5 (or up to 6). Let's plan for 5 days to be efficient and within bounds.
    *Day 1: RBAC Enforcement & Security Hardening (Backend)*
    *Day 2: Dashboard APIs & Real-time Refresh Logic (Backend)*
    *Day 3: AI CSKH Integration & Chat Widget (Backend + Frontend)*
    *Day 4: SEO Multilingual Pages & Mobile Push Handling (Frontend)*
    *Day 5: CI/CD Pipelines, Docker Multi-stage, & Integration Testing (DevOps + Tester)*

    Let's refine each day's tasks to strictly match the required format and ensure no agent overlap. I'll assign specific agents to specific sub-tasks per day.

    **Day 1: RBAC Enforcement & Security Hardening**
    - Coder: Implement Quarkus security filters, role-based endpoint guards, JWT role extraction, PostgreSQL role mapping tables.
    - Tester: Unit tests for RBAC filters and role mapping.
    - Reviewer: Static analysis on security configs, path validation.

    **Day 2: Dashboard APIs & Real-time Refresh Logic**
    - Coder: Dashboard REST endpoints, native SQL for stats, Kafka consumer for real-time updates, env-configurable refresh interval.
    - Tester: Unit tests for dashboard service, integration test for Kafka event consumption.
    - Reviewer: Check for in-memory loops, verify native SQL usage.

    **Day 3: AI CSKH Integration & Chat Widget**
    - Coder: AI chat REST endpoint, intent recognition service, Kafka producer for chat logs, Next.js float widget component.
    - Tester: Unit tests for AI service, integration test for chat endpoint.
    - Reviewer: Validate AI payload structure, frontend component isolation.

    **Day 4: SEO Multilingual Pages & Mobile Push Handling**
    - Coder: Next.js SEO pages (dynamic routes, i18n metadata), FCM push notification service integration, mobile offline-first service worker.
    - Tester: Unit tests for i18n middleware, integration test for FCM delivery.
    - Reviewer: Check SEO meta tags, locale fallback logic, path correctness.

    **Day 5: CI/CD Pipelines, Docker Multi-stage, & Final Validation**
    - DevOps: GitHub Actions workflow, multi-stage Dockerfile, Helm chart stubs, env var injection.
    - Tester: Integration/E2E tests for deployment pipeline, end-to-end role flow.
    - Reviewer: Final compliance audit, Docker layer optimization check.

    Now, I need to flesh out each day with the exact markdown structure, ensuring strict adherence to path syntax, agent boundaries, and technical requirements. I will carefully map the raw requirements to these days.

    *Self-Correction/Refinement during planning:*
    - Check path syntax: Must be `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/...`
    - Check tester syntax: `<source>;<test>` or `INTEGRATION_SCOPE;<test>`
    - Ensure no agent overlap: Each sub-task has exactly one agent.
    - Ensure Phase 4 scope matches context: RBAC, Dashboard, AI Chat, CI/CD, SEO, Mobile Push.
    - Duration: 5 days (fits 4-6 range).
    - I will generate exactly 5 days. Each day will have 2-3 sub-tasks assigned to different agents.
    - I must strictly follow the output template.

    Let's draft carefully.

    **Day 1: RBAC Enforcement & Security Hardening**
    - Sub-task 1.1: Coder implements Quarkus security interceptor, role hierarchy resolver, JWT claim extractor.
    - Sub-task 1.2: Tester writes unit tests for security interceptor and role resolver.
    - Sub-task 1.3: Reviewer audits security configs and path compliance.

    **Day 2: Dashboard APIs & Real-time Refresh Logic**
    - Sub-task 2.1: Coder implements DashboardResource, DashboardService with native SQL, Kafka consumer for live stats, env-config interval.
    - Sub-task 2.2: Tester writes unit tests for DashboardService, integration test for Kafka consumer.
    - Sub-task 2.3: Reviewer checks for in-memory loops, validates native SQL.

    **Day 3: AI CSKH Integration & Chat Widget**
    - Sub-task 3.1: Coder implements AIChatResource, IntentRecognitionService, Kafka producer for chat events.
    - Sub-task 3.2: Coder implements Next.js AIChatWidget component, float button, state management.
    - Sub-task 3.3: Tester writes unit tests for AI service, integration test for chat endpoint.
    *(Wait, I need to keep agents distinct per sub-task. I'll split AI backend and frontend into separate sub-tasks with different agents if needed, or just assign Coder to both but keep them separate sub-tasks. The prompt says "Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent". I'll assign Coder to backend AI, Coder to frontend AI, but that's fine. Or I can assign Tester to one, Reviewer to another. I'll stick to Coder for implementation, Tester for testing, Reviewer for audit.)*

    Let's structure Day 3:
    - 3.1: Coder (Backend AI)
    - 3.2: Coder (Frontend AI Widget)
    - 3.3: Tester (AI Backend Tests)
    - 3.4: Reviewer (AI Compliance)

    **Day 4: SEO Multilingual Pages & Mobile Push Handling**
    - 4.1: Coder (Frontend SEO & i18n)
    - 4.2: Coder (Backend FCM Service & Mobile Push)
    - 4.3: Tester (Frontend i18n & Backend FCM Tests)
    - 4.4: Reviewer (SEO & Push Compliance)

    **Day 5: CI/CD Pipelines, Docker Multi-stage, & Final Validation**
    - 5.1: DevOps (GitHub Actions & Dockerfile)
    - 5.2: DevOps (Helm Charts & GKE Configs)
    - 5.3: Tester (Integration/E2E Pipeline Tests)
    - 5.4: Reviewer (Final Audit & DoD Sign-off)

    I need to make sure the paths are exact and follow the rules. I will generate