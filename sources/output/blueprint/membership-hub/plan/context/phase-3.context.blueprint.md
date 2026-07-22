<think>
Here's a thinking process:

1.  **Analyze User Input:**
    - **Project Name:** membership-hub
    - **Phase:** 3 out of 5
    - **Global Context:** Provided in detail. Covers tech stack (Java 17, Quarkus, Kafka, PostgreSQL, Next.js, Tailwind, i18n, Firebase/Google/FB OAuth, Zalo/FCM notifications, AI chat), guardrails (package paths, workspace boundaries, tester syntax, performance rules, phase discipline 1-7 days, security/roles, observability), sub-agent personas (Manager, Coder, Tester, Reviewer, DevOps), and a 5-phase plan.
    - **Phase 3 Specifics (from Global Context):**
        - Duration: 3-5 days
        - Backend: Course, Teacher, Student management services; Enrollment & registration logic (auto-create accounts); QR attendance capture (Kafka event, atomic daily flag); StudentCard expiry calculation (native DB function); Promotion & Announcement services.
        - Frontend/Mobile: Center Management screens; Course Management UI; Student enrollment forms & search; Mobile app screens mirroring web (profile, card view, enrollment).
        - Objective: Build core business logic, enrollment workflow, attendance tracking, and corresponding UI forms.
    - **Raw Requirements:** Detailed list of features including multi-center management, QR attendance (daily flag), student card expiry, Zalo/FCM notifications, Next.js frontend with i18n, SEO, role-based screens (SysAdmin, Admin, Manager, Teacher, Student), course/teacher/student management, promotions, announcements, AI chat, mobile app mirroring web.
    - **Constraints:** Strict 1-7 day limit per phase. Stop when core objectives are met. Output must follow a specific Markdown structure. Day-by-day logs must group by Day -> Sub-Task -> Agent -> Target Path -> Requirements. Tester syntax must be `<source>;<test>` or `INTEGRATION_SCOPE;<test>`. Paths must start with `./sources/backend/` or `./sources/frontend/`. Package: `org.nlh4j.saas.membershiphub`.

2.  **Deconstruct Phase 3 Requirements & Map to Days:**
    Phase 3 covers: Course/Teacher/Student management, Enrollment/Registration, QR Attendance, StudentCard expiry, Promotions/Announcements, and corresponding UI (Center, Course, Student, Mobile screens).
    Duration: 3-5 days. I'll aim for 4 days to comfortably cover everything without exceeding the 7-day limit, aligning with the "3-5 days" guideline.
    I need to break it down day-by-day, assigning tasks to Coder, Tester, Reviewer, DevOps as appropriate, strictly following the path and syntax rules.

    *Day 1: Core Domain Services & Data Models (Backend) + UI Shell for Management (Frontend)*
    - Backend: Course, Teacher, Student entities & repositories. Service layer for CRUD. Native DB function for card expiry.
    - Frontend: Center Management screens, Course Management UI skeleton.
    - Tester: Unit tests for services.
    - Reviewer: Static analysis on paths & package structure.

    *Day 2: Enrollment Workflow & Account Auto-Creation (Backend) + Enrollment Forms (Frontend)*
    - Backend: Enrollment service, auto-create Student/Teacher accounts, Kafka event producers for enrollment.
    - Frontend: Student enrollment forms, search components, mobile profile/card view.
    - Tester: Unit tests for enrollment logic.
    - Reviewer: Check Kafka integration & path compliance.

    *Day 3: QR Attendance & Notification Triggers (Backend) + Mobile Sync & i18n (Frontend)*
    - Backend: QR attendance capture service (atomic daily flag via DB/Kafka), notification service integration (Zalo/FCM triggers on attendance/enrollment).
    - Frontend: Mobile app screens mirroring web, i18n locale detection/storage, responsive layouts.
    - Tester: Integration tests for attendance & notifications.
    - Reviewer: Performance check (no large loops, native SQL).

    *Day 4: Promotions/Announcements & Role-Based UI Guards (Backend/Frontend) + Final Phase Validation*
    - Backend: Promotion & Announcement services, role-based access filters for Phase 3 endpoints.
    - Frontend: Promotion/Announcement UI, role-based routing/guards for new screens, SEO metadata setup.
    - Tester: Integration/E2E tests for full workflow.
    - DevOps: Docker multi-stage updates, environment config for dashboard interval (though dashboard is Phase 4, I'll stick to Phase 3 scope: Kafka topics, DB migrations).
    - Reviewer: Final compliance sign-off.

    Wait, the prompt says Phase 3 duration is 3-5 days. I'll structure it as 4 days to be safe and thorough. I must strictly follow the output format.

3.  **Draft - Section by Section (Mental Refinement):**

    *## 1. Phase Operational Scope & Objectives*
    - Focus: Core business logic implementation (Course, Teacher, Student, Enrollment, QR Attendance, StudentCard, Promotions, Announcements).
    - UI: Center management, course scheduling, enrollment forms, mobile mirroring, i18n locale handling.
    - Backend: Quarkus services, Kafka event streaming for attendance/enrollment, native PostgreSQL functions for card expiry, atomic daily attendance flags.
    - Frontend: Next.js pages/components, Tailwind UI, role-based routing, mobile responsive layouts.
    - Objective: Deliver fully functional CRUD & workflow services for core domains, integrate Kafka for event-driven attendance/notifications, and deploy corresponding web/mobile UI screens with i18n support.

    *## 2. Allowed Technical Scope & Directory Boundaries*
    - Backend: `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/...` (services, resources, entities, kafka producers/consumers, native SQL functions)
    - Frontend: `./sources/frontend/src/...` (pages, components, i18n, mobile layouts)
    - Tests: `./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/...`
    - Strictly NO paths outside `./sources/backend/` or `./sources/frontend/`.
    - Package: `org.nlh4j.saas.membershiphub`

    *## 3. Dedicated Sub-Agent Functional Directives*
    - Coder: Implement services, resources, entities, Kafka streams, Next.js pages/components, i18n middleware, mobile layouts.
    - Tester: Write unit tests for services, integration tests for Kafka/DB workflows, use exact syntax.
    - Reviewer: Audit code for guardrails (no in-memory loops, native SQL, path correctness, role enforcement).
    - DevOps: Update Dockerfiles, Kafka topic configs, DB migration scripts, environment variables for phase 3.

    *## 4. Phase Definition of Done (DoD)*
    - All Phase 3 backend services implemented & tested.
    - Kafka topics for attendance/enrollment configured & consumed.
    - Native DB function for card expiry deployed.
    - Frontend screens for Center, Course, Student, Enrollment, Mobile profile/card complete.
    - i18n locale detection & storage functional.
    - All unit/integration tests pass.
    - Reviewer sign-off on compliance.

    *## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS*
    I will structure Days 1-4. Each day will have sub-tasks for Coder, Tester, Reviewer, DevOps as needed. I must strictly follow the target path syntax.

    *Day 1: Core Domain Models & Management Services*
    - Coder: Entities (Course, Teacher, Student, Enrollment, StudentCard, Promotion, Announcement), Repositories, CRUD Services, Native DB function for card expiry.
    - Coder (Frontend): Center Management UI, Course Management UI skeleton.
    - Tester: Unit tests for services.
    - Reviewer: Path & package audit.

    *Day 2: Enrollment Workflow & Account Provisioning*
    - Coder: Enrollment service, auto-create Student/Teacher accounts, Kafka producers for enrollment events.
    - Coder (Frontend): Student enrollment forms, search components, mobile profile/card view.
    - Tester: Unit tests for enrollment & account creation.
    - Reviewer: Kafka integration & security audit.

    *Day 3: QR Attendance & Notification Triggers*
    - Coder: QR attendance service (atomic daily flag via DB upsert/Kafka), notification trigger integration (Zalo/FCM stubs for attendance/enrollment).
    - Coder (Frontend): Mobile app screens mirroring web, i18n locale detection/storage, responsive layouts.
    - Tester: Integration tests for attendance & notifications.
    - Reviewer: Performance & streaming audit.

    *Day 4: Promotions/Announcements & Role-Based UI Guards*
    - Coder: Promotion & Announcement services, role-based access filters for Phase 3 endpoints.
    - Coder (Frontend): Promotion/Announcement UI, role-based routing/guards, SEO metadata setup.
    - Tester: Integration/E2E tests.
    - DevOps: Docker multi-stage updates, Kafka topic configs, DB migrations.
    - Reviewer: Final compliance sign-off.