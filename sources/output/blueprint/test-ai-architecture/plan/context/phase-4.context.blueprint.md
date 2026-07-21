# PHASE 4 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
- **Validate End‑to‑End Functionality** – Confirm that all core business capabilities (membership management, QR‑based attendance, multi‑center support, multi‑language UI, SEO metadata, and cross‑platform authentication) operate as specified.
- **Ensure Security & Compliance** – Verify that authentication flows (email/password, Firebase, Google, Facebook) meet security best practices, GDPR/CCPA data‑handling rules, and token management standards.
- **Performance & Reliability Testing** – Stress‑test critical paths (attendance QR scan, messaging delivery, user login) to confirm scalability and acceptable response times under load.
- **Quality Gates** – Achieve ≥ 90 % unit test coverage for backend services, ≥ 80 % component coverage for Next.js front‑end, and full integration test coverage for Kafka‑Postgres event pipelines.
- **Documentation & Sign‑off** – Produce test artifacts (test plans, execution reports, defect logs) and obtain formal sign‑off from Tester, Reviewer, and Manager before proceeding to deployment.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
```
src/
  main/
    java/
      com/membership/
        backend/
          controller/          # REST controllers (e.g., /api/v1/members, /api/v1/attendance/qr)
          service/              # Business logic (MembershipService, AttendanceService, AuthService)
          repository/           # JPA repositories (MemberRepository, AttendanceRepository)
          kafka/                # Kafka producers/consumers (AttendanceEventProducer, NotificationConsumer)
          config/               # Security, JWT, OAuth2 (Firebase, Google, Facebook) configs
    test/
      java/
        com/membership/
          backend/            # Unit & integration tests for controllers, services, repositories, Kafka
      resources/
        application-test.yml # Test‑specific Spring config (datasource, Kafka embedded broker)
  frontend/
    nextjs/
      pages/                 # /members, /attendance, /auth, /dashboard
      components/            # Reusable UI (LanguageSwitcher, QRScanner, NotificationBanner)
      lib/                   # i18n utilities, SEO helpers
      __tests__/             # Jest unit/component tests
      cypress/               # End‑to‑end UI tests (covers multi‑language navigation, auth flows)
  mobile/
    nextjs-mobile/          # React‑Native/Expo wrapper using same Next.js codebase
    __tests__/              # Detox/Unit tests for iOS/Android
  docker/
    Dockerfile.*           # Build images for backend, frontend, mobile
  k8s/                     # Helm charts / Kustomize overlays for GKE deployment
  docs/                    # Test plans, API specs, security checklists
```
**Key Endpoints to Test**
- `POST /api/v1/auth/internal` (email/password)
- `POST /api/v1/auth/external/{provider}` (Firebase, Google, Facebook OAuth2 callbacks)
- `GET /api/v1/members/{id}` (member profile)
- `POST /api/v1/attendance/qr` (QR scan → attendance record)
- `GET /api/v1/centers/{centerId}/members` (list members for a center)
- `GET /api/v1/notifications` (fetch push/Zalo messages)
- `GET /api/v1/health` (liveness/readiness probes)

**Kafka Topics**
- `attendance-events` (produced on QR scan)
- `notification-events` (produced for SMS/Zalo/app push)

**Database Schemas**
- `member` (id, email, name, center_id, locale, etc.)
- `attendance` (id, member_id, attendance_date, center_id)
- `notification` (id, member_id, channel, payload, sent_at)

## 3. Dedicated Sub-Agent Functional Directives
| Sub‑Agent | Specific Tasks & Deliverables |
|-----------|------------------------------|
| **Coder** | • Write unit tests for all Quarkus services, repositories, and Kafka producers/consumers using JUnit 5 & Mockk.<br>• Implement integration tests that spin up an embedded PostgreSQL and Kafka (using Testcontainers).<br>• Add contract tests (Pact) for external authentication providers.<br>• Create Next.js component unit tests (Jest) and Cypress end‑to‑end scenarios covering multi‑language UI, QR scanner flow, and notification display.<br>• Ensure test code follows project coding standards (spotless, sonarqube). |
| **Tester** | • Design a comprehensive Test Plan covering functional, security (OWASP), performance (load‑testing with k6), and compliance (GDPR/CCPA) test cases.<br>• Execute the test suite in a CI pipeline (GitHub Actions) and capture results, failures, and performance metrics.<br>• Log defects in the issue tracker, prioritize them, and verify fixes.<br>• Produce a Test Execution Report with coverage metrics, pass/fail ratios, and risk assessment. |
| **Reviewer** | • Conduct peer review of all test code, test plans, and defect reports against coding standards and security guidelines.<br>• Validate that test coverage meets the ≥ 90 % (backend) / ≥ 80 % (frontend) thresholds.<br>• Approve test artifacts before they are promoted to production‑ready status. |
| **DevOps** | • Set up a dedicated test environment in GCP (GKE cluster, Cloud SQL, Pub/Sub) using Terraform/Kustomize.<br>• Configure CI/CD pipelines to automatically spin up test containers, run unit/integration/e2e tests, and publish test reports.<br>• Implement monitoring (Prometheus/Grafana) and logging (ELK) for test runs to capture performance bottlenecks.<br>• Ensure rollback capability if test failures block promotion. |
| **Manager** | • Oversee Phase‑4 progress, ensure all sub‑agents stay within the 7‑day window.<br>• Validate that the Phase Definition of Done (DoD) is met before authorizing transition to Phase 5.<br>• Coordinate stakeholder sign‑off (Security, Compliance, Product). |

## 4. Phase Definition of Done (DoD)
- **Test Coverage**: ≥ 90 % unit test coverage for all Quarkus backend code; ≥ 80 % component coverage for Next.js front‑end; full integration test coverage for Kafka‑Postgres event flows.
- **Functional Validation**: All core user journeys (member registration, login via any provider, QR attendance, notification delivery via SMS/Zalo/app) pass automated tests.
- **Security Verification**: Authentication tokens are correctly validated, password hashing meets bcrypt/Argon2 standards, OAuth2 redirects are safe, and GDPR/CCPA data‑handling checks (data export, consent) are validated.
- **Performance Benchmarks**: Load tests confirm ≤ 200 ms average response time for attendance QR scan and ≤ 500 ms for login under expected traffic; no memory leaks detected.
- **Test Artifacts**: Complete Test Plan, Execution Report, Defect Log (all resolved), and Coverage Reports are archived in the project’s artifact repository.
- **Review Sign‑off**: Tester, Reviewer, and DevOps have signed off on the test results and environment readiness.
- **No Open Blocking Issues**: All critical defects identified during Phase 4 are either fixed or documented with an acceptable risk mitigation plan.
- **Ready for Deployment**: The application meets all Phase 4 quality gates, and the transition hand‑off to Phase 5 (Deployment & Monitoring) is formally approved.