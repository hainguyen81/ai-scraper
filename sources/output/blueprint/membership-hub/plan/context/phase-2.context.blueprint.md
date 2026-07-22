<think>
Here's a thinking process:

1.  **Analyze User Input:**
    - **Project Name:** membership-hub
    - **Task:** Detail **PHASE 2 OUT OF 5**
    - **Global Context:** Provided in detail. Covers tech stack (Java 17, Quarkus, Kafka, PostgreSQL, Next.js, Tailwind, i18n, Firebase/Google/FB OAuth, JWT, Zalo API, FCM, AI chat, GCP/GKE), guardrails (package paths, workspace boundaries, tester syntax, performance rules, phase discipline 1-7 days, security/roles, observability), sub-agent personas (Manager, Coder, Tester, Reviewer, DevOps), and a 5-phase plan.
    - **Phase 2 Specifics (from Global Context):**
        - Duration: 2-4 days
        - Backend: User service (JWT, role mapping, password hashing), OAuth adapters (Firebase, Google, FB), Kafka producers/consumers for user & enrollment events, Notification service (Zalo API, FCM), Authorization filter & security config.
        - Frontend/Mobile: Admin web layout (sidebar, header, role-specific menus), Mobile app shell (Next.js hybrid), Multi-language support (locale storage, fallback), Responsive dashboard skeleton.
        - Objective: Implement identity & access, event streaming, and notification backbone; deliver UI shell for both web and mobile.
    - **Raw Requirements:** Covers web/mobile, Java/Quarkus/Kafka/Postgres/GCP, auth (internal + OAuth), multi-center management, QR attendance, student card expiry, Zalo/FCM notifications, Next.js frontend, i18n/SEO, dashboard with real-time updates (15 min env config), course/teacher/student management, promotions/announcements, AI chat, role-based screens (SysAdmin, Admin, Manager, Teacher, Student).
    - **Constraints:** Strict 1-7 day limit per phase. Stop when core objectives met. Day-by-day logs required. Strict path syntax (`./sources/backend/...`, `./sources/frontend/...`). Tester syntax: `<source>;<test>` or `INTEGRATION_SCOPE;<test>`. Group by Day -> Sub-Task -> Agent -> Target Path -> Requirements.
    - **Output Format:** Must follow the exact Markdown structure provided.

2.  **Deconstruct Phase 2 Requirements & Map to Days:**
    - Phase 2 Duration: 2-4 days. I'll aim for 3 days to comfortably cover all backend/frontend/notification/auth/Kafka tasks without exceeding limits.
    - **Day 1:** Core Auth & Security Backend + Frontend Shell & i18n Setup
    - **Day 2:** OAuth Adapters, Kafka Event Streaming, Notification Service (Zalo/FCM)
    - **Day 3:** Role-Based UI Layouts, Dashboard Skeleton, Integration Testing & Review
    - Let's align strictly with the prompt's structure and constraints.

    *Day 1 Focus:* User service (JWT, password hashing, role mapping), Security config/filter, Frontend shell (Next.js layout, sidebar/header), i18n middleware.
    *Day 2 Focus:* OAuth adapters (Firebase, Google, FB), Kafka producers/consumers for user/enrollment events, Notification service (Zalo API, FCM).
    *Day 3 Focus:* Role-specific menus, Dashboard skeleton (env-driven refresh), Integration tests, Reviewer sign-off, DevOps pipeline stubs for this phase.

    I need to ensure all paths start with `./sources/backend/` or `./sources/frontend/`.
    Package: `org.nlh4j.saas.membershiphub`
    Paths will look like: `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/auth/UserService.java`
    Frontend: `./sources/frontend/src/app/layout.tsx`, etc.

3.  **Draft - Section by Section (Mental Refinement):**

    **## 1. Phase Operational Scope & Objectives**
    - Implement identity & access management (JWT, password hashing, role mapping).
    - Integrate OAuth providers (Firebase, Google, Facebook).
    - Establish Kafka event streaming for user & enrollment lifecycle events.
    - Build notification backbone (Zalo group API, FCM push).
    - Deliver responsive UI shell (web admin layout, mobile app shell) with i18n middleware and role-based routing guards.
    - Duration: 3 Days.

    **## 2. Allowed Technical Scope & Directory Boundaries**
    - Backend: `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/auth/`, `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/security/`, `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/events/`, `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/notification/`, `./sources/backend/src/main/resources/`
    - Frontend: `./sources/frontend/src/app/`, `./sources/frontend/src/components/`, `./sources/frontend/src/i18n/`, `./sources/frontend/src/lib/`
    - Strictly no cross-phase leakage. Focus only on Phase 2 deliverables.

    **## 3. Dedicated Sub-Agent Functional Directives**
    - **Coder:** Implement auth services, OAuth adapters, Kafka streams, notification services, Next.js layout, i18n, role guards.
    - **Tester:** Write unit tests for auth/OAuth/Kafka/notification logic. Integration tests for API endpoints. Use strict syntax.
    - **Reviewer:** Audit security config, JWT handling, Kafka backpressure, i18n fallback logic, path compliance.
    - **DevOps:** Configure environment variables for OAuth, Kafka, Zalo/FCM, dashboard refresh interval. Setup CI/CD stubs for Phase 2.

    **## 4. Phase Definition of Done (DoD)**
    - JWT issuance & validation working with role mapping.
    - OAuth flows (Firebase, Google, FB) successfully exchange tokens.
    - Kafka topics for `user.created`, `enrollment.updated` functional.
    - Zalo & FCM notification dispatch verified.
    - Web admin layout & mobile shell responsive with i18n detection.
    - All unit/integration tests pass. Reviewer sign-off obtained.

    **## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS**
    *Need to structure exactly as requested.*
    I will create Day 1, Day 2, Day 3. Each day has sub-tasks assigned to specific agents. Each sub-task has target paths and architectural requirements.

    *Day 1: Identity Core & UI Shell Foundation*
    - Sub-Task 1.1: Coder - User Service & JWT/Security Config
    - Sub-Task 1.2: Coder - Frontend Shell & i18n Middleware
    - Sub-Task 1.3: Tester - Auth & Routing Unit Tests
    - Sub-Task 1.4: Reviewer - Security & Path Compliance Audit

    *Day 2: OAuth Integration & Event/Notification Backbone*
    - Sub-Task 2.1: Coder - OAuth Adapters & Kafka Event Producers/Consumers
    - Sub-Task 2.2: Coder - Notification Service (Zalo & FCM)
    - Sub-Task 2.3: Tester - OAuth & Kafka Integration Tests
    - Sub-Task 2.4: DevOps - Environment Config & CI/CD Pipeline Stub

    *Day 3: Role-Based UI Layouts & Dashboard Skeleton*
    - Sub-Task 3.1: Coder - Admin Layout, Role Menus & Dashboard Skeleton
    - Sub-Task 3.2: Tester - UI Component & API Integration Tests
    - Sub-Task 3.3: Reviewer - Final Phase 2 Compliance Sign-off
    - Sub-Task 3.4: Manager - Dependency Validation & Phase Closure

    Now, I will flesh out each sub-task with the exact required format, ensuring paths match the global context (`org.nlh4j.saas.membershiphub`, `./sources/backend/...`, `./sources/frontend/...`), and requirements align with Phase 2 scope.

    *Self-Correction/Verification during drafting:*
    - Check path syntax: Must be `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/...`
    - Check tester syntax: `<source>;<test>` or `INTEGRATION_SCOPE;<test>`
    - Check phase duration: 3 days (within 1-7 limit)
    - Check scope: Matches Phase 2 exactly.
    - Ensure no overlap with Phase 1 (scaffolding, basic CRUD) or Phase 3 (course/teacher/student management, QR, etc.).
    - I will carefully construct the markdown to match the prompt's template exactly.

    Let's draft carefully. 
    Structure:
    # PHASE 2 CONTEXT BLUEPRINT: membership-hub
    ## 1. Phase Operational Scope & Objectives
    ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
    ## 3. Dedicated Sub-Agent Functional Directives
    ## 4. Phase Definition of Done (DoD)
    ## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS