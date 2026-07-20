<think>
Here's a thinking process:

1.  **Analyze User Input:**
   - **Project Name:** `membership-hub` (but the prompt says `test-ai-architecture` for the context title, I'll stick to the requested title format)
   - **Requirements:**
     - Web for management, Mobile for students.
     - Backend: Quarkus, Kafka, PostgreSQL. Scalable, Dockerized, deployed on GCP/GKE.
     - Auth: Internal (email/password), External (Firebase, Google, Facebook). Manage internal users & external logins.
     - Multi-tenant: Supports multiple training centers simultaneously.
     - Attendance: QR code check-in. Marks attendance for the day. Multiple check-ins per day are allowed but only count as one attendance per day.
     - Post-attendance: Shows remaining validity days (like a gym pass countdown).
     - Notifications: Send via Zalo (phone number & group), plus mobile app push notifications.
     - Mobile App: Next.js frontend, multi-language support, builds for iOS & Android.
     - SEO: Multi-language SEO for both web and mobile app.
     - Locale Detection: Default to user's saved preference, else browser/device locale.
   - **Output Structure Required:**
     ```
     # PHASE 1 CONTEXT BLUEPRINT: test-ai-architecture
     ## 1. Phase Operational Scope & Objectives
     ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
     ## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
     ## 4. Phase Definition of Done (DoD)
     ```
   - **Constraint:** "Isolate development boundaries so sub-agents never overlap." This is critical. I need to define strict boundaries for each agent in Phase 1.

2.  **Deconstruct Phase 1 Requirements:**
   Phase 1 should focus on the foundation: architecture setup, multi-tenant database schema, authentication system, base Next.js/Quarkus scaffolding, Docker/GKE infrastructure, and core event-driven setup. It shouldn't dive into attendance logic, notifications, or advanced SEO/i18n yet. Those come in later phases.
   - *Scope:* Core infrastructure, multi-tenant DB design, auth provider abstraction, base Next.js/Quarkus project structure, Docker/GKE scaffolding, Kafka topic definition, locale detection foundation.
   - *Boundaries:* Strict file/path separation. Backend vs Frontend vs Infra vs Tests.
   - *Agents:* Coder (implementation), Tester (test strategy/setup), Reviewer (code/arch review), DevOps (Docker/GKE/CI-CD setup).
   - *DoD:* Clear, measurable criteria for Phase 1 completion.

3.  **Draft - Section by Section:**

   *## 1. Phase Operational Scope & Objectives*
   - Focus: Foundation & Core Architecture.
   - Objectives:
     - Establish multi-tenant PostgreSQL schema with strict data isolation.
     - Implement unified authentication gateway (Internal Email/Pass + OAuth2 for Firebase/Google/Facebook).
     - Scaffold Quarkus backend with modular architecture, Kafka producer/consumer base, and REST/GraphQL API contracts.
     - Scaffold Next.js frontend (App Router) with i18n routing foundation, locale detection logic, and PWA/native build configuration.
     - Containerize services and establish GCP/GKE deployment pipeline.
     - Define strict development boundaries to prevent agent overlap.

   *## 2. Allowed Technical Scope & Directory Boundaries*
   - Need to define exact paths, endpoints, and tech boundaries.
   - *Backend (Quarkus):* `backend/`
     - `backend/src/main/java/com/membershiphub/auth/` (Auth providers, JWT, OAuth2 config)
     - `backend/src/main/java/com/membershiphub/tenant/` (Multi-tenant resolver, RLS/schema setup)
     - `backend/src/main/java/com/membershiphub/core/` (Base entities, Kafka config, DTOs)
     - `backend/src/main/resources/db/migration/` (Flyway/Liquibase scripts)
     - Endpoints: `/api/v1/auth/*`, `/api/v1/tenant/*`, `/api/v1/health`
   - *Frontend (Next.js):* `frontend/`
     - `frontend/src/app/(auth)/` (Login/Register pages)
     - `frontend/src/app/(dashboard)/` (Web admin shell)
     - `frontend/src/app/(mobile)/` (Mobile app shell)
     - `frontend/src/i18n/` (Locale detection, routing config, message files)
     - `frontend/src/config/` (Next.js config, Expo/Capacitor setup for iOS/Android)
   - *Infrastructure/DevOps:* `infra/`
     - `infra/docker/` (Dockerfiles, docker-compose for local dev)
     - `infra/k8s/` (Helm charts, GKE manifests, ingress, secrets)
     - `infra/ci-cd/` (GitHub Actions/GitLab CI pipelines)
   - *Kafka Topics:* `membership.auth.events`, `membership.tenant.events`, `membership.system.events`
   - *Strict Boundaries Rule:* Agents must only modify files within their designated directories. Cross-boundary changes require explicit architectural approval.

   *## 3. Dedicated Sub-Agent Functional Directives*
   - Need specific tasks for Coder, Tester, Reviewer, DevOps. Ensure no overlap.
   - *Coder:*
     - Implement Quarkus auth module (JWT, OAuth2 providers, user management).
     - Implement multi-tenant resolver (header-based or subdomain-based tenant ID).
     - Scaffold Next.js app with i18n routing, locale detection fallback logic, and base UI shell.
     - Set up Kafka producer/consumer templates in Quarkus.
     - *Boundary:* `backend/src/`, `frontend/src/`, `frontend/public/`
   - *Tester:*
     - Design unit tests for auth flows, tenant isolation, and locale detection.
     - Set up integration test harness for PostgreSQL RLS/schema validation.
     - Configure E2E test framework (Playwright/Cypress) for auth & routing.
     - *Boundary:* `backend/src/test/`, `frontend/src/__tests__/`, `e2e/`
   - *Reviewer:*
     - Enforce Clean Architecture & DDD boundaries.
     - Validate security compliance (OAuth2 flows, JWT signing, secret handling).
     - Review multi-tenant data isolation strategy.
     - Audit i18n/SEO foundation for Next.js.
     - *Boundary:* Read-only access to all code, write-only to `docs/reviews/` and PR comments.
   - *DevOps:*
     - Create multi-stage Dockerfiles for Quarkus & Next.js.
     - Configure GKE cluster manifests, Helm charts, and ingress.
     - Set up CI/CD pipeline for build, test, scan, and deploy.
     - Configure GCP Secret Manager & Cloud SQL integration.
     - *Boundary:* `infra/`, `.github/workflows/`, `Dockerfile.*`, `docker-compose.*`

   *## 4. Phase Definition of Done (DoD)*
   - Clear, measurable criteria.
   - [ ] Multi-tenant PostgreSQL schema deployed with strict row-level/schema isolation.
   - [ ] Unified auth gateway operational (Internal + Firebase/Google/Facebook OAuth2).
   - [ ] Quarkus backend scaffolded with Kafka integration, health checks, and tenant resolver.
   - [ ] Next.js frontend scaffolded with i18n routing, locale detection fallback, and iOS/Android build config.
   - [ ] Docker images built, scanned, and pushed to GCR/Artifact Registry.
   - [ ] GKE deployment pipeline functional with auto-scaling & ingress configured.
   - [ ] Unit/Integration tests passing with >80% coverage on auth & tenant modules.
   - [ ] Security audit passed (JWT validation, OAuth2 state/nonce, secret management).
   - [ ] Documentation updated (API contracts, architecture diagrams, deployment runbook).
   - [ ] Zero critical/high vulnerabilities in SAST/DAST scans.

4.  **Self-Correction & Refinement (Mental Review):**
   - *Check against constraints:* "Isolate development boundaries so sub-agents never overlap." -> I've explicitly defined directory boundaries and agent scopes. I'll add a strict "Boundary Enforcement Protocol" to make it explicit.
   - *Check against requirements:* Covers Quarkus, Kafka, Postgres, GCP/GKE, Auth (internal + external), Multi-tenant, Next.js frontend, i18n, locale detection, iOS/Android build config. Phase 1 focuses on foundation, which is correct. Attendance, notifications, SEO details come later.
   - *Structure match:* Exactly matches the requested Markdown structure.
   - *Tone:* Elite Solution Architect, precise, technical, authoritative.
   - *Improvements during drafting:*
     - Make sure the directory boundaries are extremely explicit.
     - Clarify that Phase 1 does NOT implement attendance logic, notifications, or advanced SEO metadata (those are Phase 2/3).
     - Add a "Boundary Enforcement Protocol" subsection to strictly prevent overlap.
     - Ensure Kafka topics and endpoints are explicitly scoped to Phase 1.