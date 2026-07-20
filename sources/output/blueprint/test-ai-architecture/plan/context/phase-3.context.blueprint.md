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
     # PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
     ## 1. Phase Operational Scope & Objectives
     ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
     ## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
     ## 4. Phase Definition of Done (DoD)
     ```

2.  **Deconstruct & Map to Required Structure (Phase 3 Focus):**
   I need to design Phase 3 specifically. Based on the 5-phase strategy I mentally outlined earlier, Phase 3 should focus on **Multi-Channel Notifications, i18n/SEO, and Locale Detection**. This aligns perfectly with the remaining requirements that haven't been covered in foundational/attendance phases.
   Let's verify the logical flow:
   - Phase 1: Foundation, Auth, Multi-tenant DB, Base Infra
   - Phase 2: Attendance Logic, QR, Validity Countdown, Kafka Streams
   - Phase 3: Notifications (Zalo, Push), i18n/SEO, Locale Detection, Mobile/Web Integration
   - Phase 4: Testing, Security, Performance, Compliance
   - Phase 5: Production Deployment, Observability, Handover
   This makes sense. Phase 3 will handle the communication layer, internationalization, SEO, and locale management.

   *Section 1: Phase Operational Scope & Objectives*
   - Focus: Implementing the notification ecosystem (Zalo SMS/Group, Mobile Push), multi-language support (i18n), SEO optimization for web/mobile, and locale detection/fallback logic.
   - Objectives:
     - Build async notification pipeline via Kafka.
     - Integrate Zalo API for SMS & group messaging.
     - Implement FCM/APNs for mobile push notifications.
     - Configure Next.js i18n routing, dynamic metadata, and SEO strategies.
     - Implement locale detection hierarchy (user preference > device/browser > default).
     - Ensure all UI/UX components are fully localized and SEO-compliant.

   *Section 2: Allowed Technical Scope & Directory Boundaries*
   - Need to define strict boundaries to prevent overlap with other phases/agents.
   - Backend (Quarkus): `src/main/java/com/membership/notification/`, `src/main/java/com/membership/i18n/`, Kafka consumers for attendance events, Zalo API client, FCM/APNs service.
   - Frontend (Next.js): `src/i18n/`, `src/components/`, `src/app/[locale]/`, `src/lib/locale-detection.ts`, SEO metadata generators, notification UI components.
   - Paths/Endpoints: `/api/v1/notifications/send`, `/api/v1/i18n/locales`, `/api/v1/user/locale`, Kafka topics: `attendance.completed`, `notification.dispatch`, `notification.status`.
   - Strict boundaries: No DB schema changes (handled in Phase 1), no auth logic changes (Phase 1), no attendance core logic changes (Phase 2). Only consume attendance events and trigger notifications. Only handle i18n/SEO/locale.

   *Section 3: Dedicated Sub-Agent Functional Directives*
   - Need specific tasks for Coder, Tester, Reviewer, DevOps (Docker/Deployer combined or separate? The prompt says "Coder, Tester, Reviewer, DevOps". I'll stick to that).
   - *Coder*: Implement Kafka consumers for `attendance.completed`. Build Zalo API integration (SMS & Group). Implement FCM/APNs push service. Develop Next.js i18n routing, dynamic metadata, locale detection middleware. Ensure UI components consume translation keys.
   - *Tester*: Write unit tests for locale detection logic. Integration tests for Kafka consumer -> notification dispatch. Mock Zalo API & FCM/APNs. E2E tests for multi-language UI rendering & SEO metadata validation. Load test notification queue.
   - *Reviewer*: Audit Kafka consumer idempotency & retry logic. Review Zalo API compliance & rate limiting. Validate Next.js i18n routing & SEO metadata structure. Check locale fallback hierarchy implementation. Ensure no cross-phase boundary violations.
   - *DevOps*: Containerize notification services. Configure Kafka consumer groups & scaling. Set up environment variables for Zalo/FCM/APNs secrets. Implement retry/dead-letter queue (DLQ) patterns in Docker/K8s. Configure Next.js build optimizations for i18n/SEO.

   *Section 4: Phase Definition of Done (DoD)*
   - Clear, measurable criteria.
   - All notification channels (Zalo SMS, Zalo Group, Push) successfully triggered on attendance event.
   - Idempotent notification dispatch (no duplicate messages per attendance).
   - Next.js i18n routing fully functional with dynamic metadata & SEO tags.
   - Locale detection hierarchy implemented & tested.
   - All unit/integration/E2E tests pass with >85% coverage.
   - Security & compliance audit passed (rate limiting, secret management, API compliance).
   - Docker images built, scanned, and pushed to registry.
   - Documentation updated (API specs, i18n guide, notification flow).

3.  **Draft Generation (Mental Refinement & Structuring):**
   I will now write out the response strictly following the requested markdown structure. I'll ensure technical precision, architectural rigor, and strict boundary isolation as requested by the "Elite Solution Architect" persona. I'll make sure the boundaries are explicit to prevent sub-agent overlap.

   *Self-Correction/Verification during drafting:*
   - Check structure: Matches exactly.
   - Check boundaries: Explicitly defined file paths, endpoints, Kafka topics, and what is *out of scope*.
   - Check sub-agents: Coder, Tester, Reviewer, DevOps (as requested).
   - Check DoD: Measurable, testable, aligned with requirements.
   - Tech stack alignment: Quarkus, Kafka, Postgres, Next.js, GCP/GKE, Zalo, FCM/APNs, i18n, SEO, locale detection. All covered.
   - Multi-tenant consideration: Notifications must be tenant-aware. I'll add tenant context to Kafka messages and notification routing.
   - Attendance deduplication: Already handled in Phase 2, but Phase 3 must ensure notifications are also idempotent per day per student. I'll specify this.
   - Next.js mobile build: I'll note that i18n/SEO applies to both web and mobile (via Next.js App Router + Expo/Capacitor or PWA). I'll keep it framework-agnostic but aligned with Next.js i18n standards.

   Everything looks solid. I'll generate the response now. 
   Structure:
   # PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture
   ## 1. Phase Operational Scope & Objectives
   ## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
   ## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps)
   ## 4. Phase Definition of Done (DoD)
   Content will be dense, architectural, and strictly bounded.✅
   Proceed. 
   Output matches the response. 
   *Self-Correction/Note during thought*: The prompt says "Docker, Deployer" in the global context example, but in the Phase 3 output structure it says "Coder, Tester, Reviewer, DevOps". I will follow the exact Phase 3 structure requested: "Coder, Tester, Reviewer, DevOps". I'll make sure DevOps covers Docker & GKE deployment aspects for this phase.
   I will strictly adhere to the requested markdown headers.
   All requirements are mapped. Boundaries are isolated. Ready. 
   Output Generation. 
   [Output Generation] -> *Proceeds*
</think>

# PHASE 3 CONTEXT BLUEPRINT: test-ai-architecture

## 1. Phase Operational Scope & Objectives
**Primary Focus:** Multi-Channel Notification Ecosystem, Internationalization (i18n), SEO Optimization, and Locale Detection.
**Architectural Intent:** Decouple communication and localization concerns from core attendance/business logic. Implement an event-driven,