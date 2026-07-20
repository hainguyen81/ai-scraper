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
     # GLOBAL PROJECT CONTEXT: test-ai-architecture
     ## 1. Executive Summary & Tech Stack Blueprint
     ## 2. Global Guardrails & Enterprise Compliance Standards
     ## 3. Standardized Sub-Agent Persona Definitions (Manager, Coder, Tester, Reviewer, Docker, Deployer)
     ## 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
     ```

2.  **Deconstruct & Map to Required Structure:**

   *## 1. Executive Summary & Tech Stack Blueprint*
   - Need a concise overview of the project's purpose, architecture, and tech stack.
   - Core: Multi-tenant membership management system with web admin & mobile student app.
   - Backend: Quarkus (Java/Kotlin), Kafka (event-driven messaging), PostgreSQL (relational DB).
   - Frontend: Next.js (React framework) for both Web Admin & Mobile App (via Expo/React Native or Next.js mobile capabilities? The prompt says "App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android." This implies Next.js with React Native Web or Expo Router, or perhaps Next.js for PWA + native wrappers. I'll specify Next.js + Expo/React Native for cross-platform, or Next.js App Router with mobile optimization. I'll stick to Next.js + Expo/React Native for iOS/Android builds, or Next.js PWA + Capacitor. I'll clarify it as Next.js + Expo/React Native for native builds, or Next.js App Router with mobile-first PWA + native wrappers. Actually, Next.js can build for iOS/Android via Expo Router or Capacitor. I'll specify Next.js + Expo/React Native for cross-platform mobile, or Next.js App Router with PWA + native bridges. I'll keep it aligned with the prompt: Next.js frontend, multi-language, iOS/Android builds.)
   - Auth: Internal (JWT/Session) + OAuth2 (Firebase, Google, Facebook).
   - Infra: Docker, GCP, GKE, scalable architecture.
   - Features: Multi-tenant, QR attendance, daily deduplication, validity countdown, multi-channel notifications (Zalo, Push), i18n/SEO, locale detection.

   *## 2. Global Guardrails & Enterprise Compliance Standards*
   - Need to define rules, constraints, security, compliance, and architectural principles that all agents must follow.
   - Security: OAuth2/OIDC, JWT, RBAC, data encryption (at rest & in transit), secure QR generation/validation, rate limiting.
   - Compliance: GDPR/VN Data Protection Law (personal data, phone numbers), multi-tenant data isolation (schema or row-level security).
   - Architecture: Event-driven (Kafka), microservices/modular monolith (Quarkus), stateless services, idempotent attendance processing, scalable GKE deployment.
   - Code/Dev Standards: Clean Architecture, SOLID, DDD, strict typing, comprehensive logging/metrics, CI/CD pipelines, containerization standards.
   - i18n/SEO: Next.js i18n routing, dynamic metadata, locale fallback strategy, SSR/SSG for SEO.
   - Notifications: Async processing via Kafka, retry mechanisms, Zalo API compliance, FCM/APNs for push.

   *## 3. Standardized Sub-Agent Persona Definitions*
   - Need exactly 6 personas: Manager, Coder, Tester, Reviewer, Docker, Deployer.
   - For each: Role, Responsibilities, Constraints/Guardrails, Output Format.
   - *Manager*: Oversees architecture, phase planning, requirement alignment, cross-agent coordination. Ensures multi-tenant & scalability goals are met.
   - *Coder*: Implements features per specs. Uses Quarkus, Next.js, Kafka, Postgres. Follows clean code, i18n, SEO, auth standards.
   - *Tester*: Designs unit/integration/E2E tests. Validates attendance logic, multi-tenant isolation, auth flows, notification delivery, locale/SEO.
   - *Reviewer*: Code/architecture review. Enforces guardrails, security, performance, compliance, DDD patterns.
   - *Docker*: Containerization strategy. Multi-stage builds, image optimization, security scanning, registry management.
   - *Deployer*: GCP/GKE deployment. Helm charts, CI/CD, autoscaling, monitoring, secrets management, rollback strategies.

   *## 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)*
   - Need exactly 5 phases, logical progression from foundation to production.
   - Phase 1: Foundation & Core Architecture (DB schema, multi-tenant setup, auth, base Next.js/Quarkus scaffolding, Docker/GKE infra)
   - Phase 2: Attendance & Business Logic (QR generation/validation, daily deduplication, validity countdown, Kafka event streams)
   - Phase 3: Multi-Channel Notifications & i18n/SEO (Zalo integration, Push notifications, Next.js i18n routing, SEO metadata, locale detection)
   - Phase 4: Testing, Security & Optimization (Comprehensive testing, penetration testing, performance tuning, load testing, compliance audit)
   - Phase 5: Production Deployment & Observability (GKE rollout, CI/CD automation, monitoring/alerting, documentation, handover)

3.  **Draft Generation (Mental Refinement):**
   I'll structure the output exactly as requested, ensuring technical depth, architectural rigor, and alignment with the raw requirements. I'll use precise terminology suitable for an Elite Solution Architect.

   *Section 1: Executive Summary & Tech Stack Blueprint*
   - Project: `membership-hub` (context title: `test-ai-architecture`)
   - Core: Multi-tenant membership management platform with web admin & mobile student app.
   - Backend: Quarkus (Java/Kotlin), PostgreSQL (multi-tenant via Row-Level Security or schema-per-tenant), Apache Kafka (event-driven async processing).
   - Frontend: Next.js (App Router) for Web Admin & Mobile App (Expo/React Native or Capacitor for iOS/Android builds).
   - Auth: Internal (Email/Pass + JWT) + External OAuth2 (Firebase, Google, Facebook). Unified identity provider abstraction.
   - Infra: Docker, GCP, GKE, Cloud SQL/Postgres, PubSub/Kafka bridge, Cloud Run/Managed Services.
   - Key Features: QR attendance (idempotent daily check-in), validity countdown, multi-channel notifications (Zalo SMS/Group, FCM/APNs), i18n, SEO, locale fallback.

   *Section 2: Global Guardrails & Enterprise Compliance Standards*
   - Architecture: Modular monolith/microservices boundary, event-driven, stateless, idempotent operations, multi-tenant data isolation.
   - Security: OAuth2/OIDC, JWT rotation, RBAC, encryption (TLS 1.3, AES-256), secure QR (signed tokens), rate limiting, secret management (GCP Secret Manager).
   - Compliance: GDPR/VN PDPL, data minimization, consent tracking, audit logging, tenant data segregation.
   - Dev Standards: Clean Architecture, DDD, strict typing, comprehensive logging (OpenTelemetry), metrics, tracing.
   - i18n/SEO: Next.js i18n routing, dynamic metadata, SSR/SSG, locale detection hierarchy (user preference > browser/device > default).
   - Notifications: Async Kafka consumers, retry/backoff, Zalo API compliance, FCM/APNs token management, fallback mechanisms.

   *Section 3: Standardized Sub-Agent Persona Definitions*
   - I'll define each with Role, Scope, Guardrails, and Output Expectations.
   - Manager: Architecture oversight, phase gating, requirement traceability, cross-agent sync.
   - Coder: Implementation, adheres to tech stack, clean code, i18n/SEO, auth, attendance logic.
   - Tester: Test strategy, unit/integration/E2E, coverage targets, security/performance testing.
   - Reviewer: Code/arch review, enforces guardrails, security, performance, compliance, DDD.
   - Docker: Containerization, multi-stage builds, image