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
     # PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
     ## 1. Phase Operational Scope & Objectives
     ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
     ## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
     ## 4. Phase Definition of Done (DoD)
     ```

2.  **Deconstruct & Map to Required Structure (Phase 4 Focus):**
   - The prompt asks for **PHASE 4 OUT OF 5**. I need to define what Phase 4 covers based on a logical 5-phase breakdown.
   - Typical 5-phase breakdown for this project:
     - Phase 1: Foundation & Core Architecture (DB, Multi-tenant, Auth, Base Next.js/Quarkus, Docker/GKE infra)
     - Phase 2: Attendance & Business Logic (QR, daily deduplication, validity countdown, Kafka streams)
     - Phase 3: Multi-Channel Notifications & i18n/SEO (Zalo, Push, Next.js i18n, SEO metadata, locale detection)
     - Phase 4: **Testing, Security, Performance & Optimization** (Comprehensive testing, penetration testing, load testing, compliance audit, performance tuning, observability setup)
     - Phase 5: Production Deployment & Observability (GKE rollout, CI/CD automation, monitoring/alerting, documentation, handover)
   - I'll align Phase 4 with **Testing, Security, Performance & Optimization** as it's the standard pre-production phase. I need to make sure it strictly isolates boundaries so sub-agents don't overlap.

   *Section 1: Phase Operational Scope & Objectives*
   - Focus: Rigorous validation, security hardening, performance optimization, and compliance verification before production.
   - Objectives: Achieve 90%+ test coverage, pass security/penetration tests, optimize Kafka/Quarkus/Next.js performance, validate multi-tenant isolation, ensure i18n/SEO compliance, and prepare for GKE rollout.

   *Section 2: Allowed Technical Scope & Directory Boundaries*
   - Need to define exact file paths, endpoints, and boundaries for Phase 4 to prevent overlap with other phases.
   - Backend (Quarkus): `/src/test/`, `/src/main/java/.../security/`, `/src/main/java/.../performance/`, `/src/main/resources/application-test.properties`, `/src/main/resources/application-perf.properties`
   - Frontend (Next.js): `/tests/`, `/src/i18n/`, `/src/seo/`, `/public/locales/`, `/src/app/[locale]/...` (SEO metadata validation)
   - Infrastructure/DevOps: `/infra/tests/`, `/k8s/tests/`, `/scripts/load-test/`, `/scripts/security-scan/`
   - Endpoints/Paths: Focus on test endpoints, health checks, metrics endpoints (`/q/metrics`, `/q/health`), SEO crawl paths (`/[locale]/sitemap.xml`, `/robots.txt`), notification test routes.
   - Strict boundary: No new business logic features. Only testing, security hardening, performance tuning, and compliance validation.

   *Section 3: Dedicated Sub-Agent Functional Directives*
   - Need specific tasks for Coder, Tester, Reviewer, DevOps (Docker/Deployer merged or kept separate? The prompt says "Coder, Tester, Reviewer, DevOps". I'll stick to that.)
   - *Coder*: Implement test utilities, mock services, performance profiling hooks, security middleware enhancements, i18n/SEO validation scripts. No new features.
   - *Tester*: Design & execute unit, integration, E2E, load, and security tests. Validate attendance deduplication, multi-tenant isolation, notification delivery, locale fallback, SEO metadata.
   - *Reviewer*: Audit code for security vulnerabilities, performance bottlenecks, compliance gaps, test coverage quality, and architectural consistency. Enforce guardrails.
   - *DevOps*: Container security scanning, GKE cluster autoscaling validation, CI/CD pipeline optimization, load testing infrastructure setup, observability/metrics validation.

   *Section 4: Phase Definition of Done (DoD)*
   - Clear, measurable criteria for Phase 4 completion.
   - Test coverage ≥ 90% (unit/integration), E2E pass rate 100%.
   - Security: Zero critical/high vulnerabilities, OWASP Top 10 compliance, multi-tenant data isolation verified.
   - Performance: Kafka throughput ≥ X msgs/sec, Quarkus response time < 200ms (p95), Next.js Lighthouse scores ≥ 90, SEO crawlability validated.
   - Compliance: GDPR/VN PDPL audit passed, notification delivery success rate ≥ 99%, locale fallback logic verified.
   - Artifacts: Test reports, security scan results, performance benchmarks, optimized Docker images, CI/CD pipeline ready for Phase 5.

3.  **Draft Generation (Mental Refinement & Structuring):**
   I will now write out the response strictly following the requested markdown structure. I'll ensure technical depth, precise boundaries, and alignment with the raw requirements. I'll use professional architectural language.

   *Structure Check:*
   # PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
   ## 1. Phase Operational Scope & Objectives
   ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
   ## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
   ## 4. Phase Definition of Done (DoD)

   *Content Generation (Mental):*
   - **Phase 4 Focus:** Testing, Security, Performance & Optimization. This is the standard pre-production hardening phase.
   - **Scope:** Validate all Phase 1-3 implementations. Stress-test Kafka/Quarkus/Next.js. Verify multi-tenant isolation, attendance deduplication, notification delivery, i18n/SEO, and locale detection. Harden security. Optimize performance.
   - **Boundaries:** Strictly limit to test directories, security configs, performance profiles, SEO validation scripts, and CI/CD test pipelines. No new business features.
   - **Directives:** Clear separation. Coder handles test infrastructure & profiling hooks. Tester handles execution & reporting. Reviewer handles audit & compliance. DevOps handles infra testing, scanning, & pipeline optimization.
   - **DoD:** Quantifiable metrics. Coverage, performance thresholds, security clearance, compliance sign-off, artifact readiness.

   I will now generate the response carefully, ensuring it matches the exact requested format and maintains the "Elite Solution Architect" tone with strict boundary isolation. I'll incorporate all raw requirements into the Phase 4 context where relevant (e.g., testing attendance deduplication, validating i18n/SEO, verifying notification delivery, checking multi-tenant isolation). All constraints will be explicitly stated. No fluff. Direct, technical, structured.✅
   Let's draft it. 
   Self-Correction/Verification during thought:
   - The prompt says "Isolate development boundaries so sub-agents never overlap." I must emphasize strict file/path/endpoint boundaries and clear role separation.
   - I'll map the raw requirements explicitly to Phase 4 validation targets.
   - I'll ensure the directory structure matches modern Quarkus + Next.js + Docker/GKE conventions.
   - I'll keep the tone authoritative and architectural.
   - Structure matches exactly.
   - Ready. Output matches response. 
   Proceeds. 
   [Output Generation] -> *See response.* 
   *Self-Correction/Refinement during drafting mental:*
   - Check requirement: "App mobile dùng next.js làm front end, hỗ trợ đa ngôn ngữ, build đc cho ios, android." -> Phase 4 will validate Next.js mobile build pipeline, i18n routing, and SEO metadata for mobile/web.
   - Check requirement: "Điểm danh qua QR... chỉ xem như đã điểm danh ngày hôm đó." -> Phase 4 will validate idempotency & daily deduplication logic under load.