# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement advanced enrollment, assignment, promotion/announcement management, real‑time dashboard refresh, multi‑language SEO, Kafka‑driven notifications, tenant‑aware isolation, and push‑delivery verification. Core goals:
- Auto‑create Student and Teacher accounts during enrollment; assign teachers to courses.
- CRUD for Promotions and Announcements with expiry; trigger Zalo group + FCM push notifications on creation/update.
- Real‑time dashboard refresh every 15 min via scheduled job; include tenant‑filtered data.
- Multi‑language SEO meta tags for promotion/announcement pages (Next.js).
- Kafka event streaming for all notification payloads; verify delivery to Zalo and mobile clients.
- Advanced tenant isolation checks in repository queries; AES‑256 PII encryption for sensitive fields.
- End‑to‑end test coverage and OWASP hardening (A01‑A07) for new endpoints.

## 2. Allowed Technical Scope & Directory Boundaries
- **Backend Java (Quarkus) components**
  - `./sources/backend/src/main/java/org/nlhj/saas/membershippub/` (core services, entities, repositories)
  - `./sources/backend/src/main/resources/application.yml` (Kafka, tenant, notification configs)
  - `./sources/backend/src/test/java/org/nlhj/saas/membershippub/` (unit tests)
  - `./sources/backend/docker/` (multi‑stage Dockerfile)
- **Frontend (Next.js) components**
  - `./sources/frontend/src/pages/en/` and `./sources/frontend/src/pages/vi/` (promotion, announcement, dashboard pages with SEO)
  - `./sources/frontend/src/components/` (role‑based UI, AI chat widget)
  - `./sources/frontend/tests/` (Cypress/Playwright spec files)
- **Configuration & Integration**
  - `./sources/backend/src/main/resources/kafka/` (producer/consumer configs)
  - `./sources/backend/src/main/resources/tenancy/` (tenant isolation filters)
- **Docker / GCP / GKE**
  - `./sources/backend/docker/Dockerfile` (final image)
  - `./sources/backend/k8s/` (GKE deployment & cronjob manifests)
  - `./sources/backend/gcp/` (IAM & service‑account configs)

All paths must start with `./sources/`. No files may be placed directly under the repository root.

## 3. Dedicated Sub-Agent Functional Directives
- **Coder**: Implement enrollment service, auto‑account creation, teacher assignment, promotion/announcement CRUD, Kafka producers, scheduled dashboard refresh, tenant‑aware repository methods, AES‑256 PII encryption, parameterized queries, multi‑language SEO meta generation in Next.js.
- **Tester**: Write unit tests for enrollment, promotion, announcement services; integration tests for Kafka notification flow; UI tests for promotion/announcement pages; verify tenant isolation and delivery verification.
- **Reviewer**: Conduct OWASP compliance review (A01‑A07), validate tenant filtering, encryption usage, injection safety, and JWT token handling for new endpoints.
- **Docker**: Update multi‑stage Dockerfile to include scheduled job dependencies; add health‑check probes; ensure image size optimization.
- **GCP**: Configure Kafka connector on GCP (if using managed Kafka), set up Pub/Sub topics for notification events, define IAM roles for services, create Cloud Scheduler job for 15‑min refresh.
- **GKE**: Deploy backend and scheduled job as K8s CronJob; expose services via Ingress; configure autoscaling; apply security policies (PodSecurityPolicy).
- **Manager**: Orchestrate cross‑team integration, validate enrollment workflow end‑to‑end, confirm notification delivery to Zalo groups and mobile apps, approve production readiness sign‑off.

## 4. Phase Definition of Done (DoD)
- Enrollment creates Student/Teacher accounts with correct tenant isolation and triggers Kafka event.
- Teacher assignment to courses persists and notifies via Kafka.
- Promotion/Announcement CRUD supports multi‑language SEO meta tags; expiry logic enforced; notifications sent to Zalo groups and FCM.
- Real‑time dashboard refreshes every 15 min with tenant‑filtered data; scheduled job runs in GKE CronJob.
- All new endpoints enforce OWASP controls: parameterized queries, AES‑256 PII encryption, tenant filtering, JWT validation.
- 100 % unit test coverage for backend services; integration/E2E tests for notification flow and UI.
- Docker images built, scanned, and deployed to GKE with successful health checks.
- GCP IAM and GKE policies applied; audit logs enabled.
- Final sign‑off by Manager confirming all requirements satisfied.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Manager Student Enrollment & Auto‑Account Creation
#### SUB‑TASK 1.1: Implement Enrollment Service with Auto‑Account Creation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/EnrollmentService.java
    * **Architectural Requirements:**
        * Use Quarkus JAX‑RS @Transactional and @RolesAllowed("Manager") for endpoint security.
        * Apply tenant isolation via @TenantFilter(tenantId = "tenant_id") on repository calls.
        * Encrypt PII fields (student SSN, contact) using AES‑256 before persistence.
        * Generate Kafka event EnrollmentCreatedEvent with tenantId, studentId, courseId.
        * Auto‑create User account (role Student) with Argon2 password hash; assign to tenant.
    * **Security Enforcement:**
        * OWASP A01: Input validation & sanitization for enrollment payload.
        * OWASP A07: Use parameterized queries in Repository layer.

#### SUB‑TASK 1.2: Create Kafka Producer for Enrollment Notifications
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/kafka/EnrollmentEventProducer.java
    * **Architectural Requirements:**
        * Configure KafkaProducer with idempotent enabled and acks=all.
        * Serialize events using Jackson with tenantId header for routing.
        * Emit event to topic "enrollment-events".
    * **Security Enforcement:**
        * Ensure producer credentials are stored in application.yml (no hard‑coded secrets).

#### SUB‑TASK 1.3: Write Unit Tests for Enrollment Service & Producer
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/EnrollmentService.java;./sources/backend/src/test/java/org/nlhj/saas/membershippub/service/EnrollmentServiceTest.java
    * **Architectural Requirements:**
        * Mock Repository and KafkaProducer to verify event emission.
        * Assert tenant isolation by checking tenant_id filter usage.
        * Validate PII encryption by checking encrypted fields in persisted entity.

#### SUB‑TASK 1.4: Update Multi‑Stage Dockerfile
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/docker/Dockerfile
    * **Architectural Requirements:**
        * Add stage for building Quarkus app with Maven.
        * Include Kafka client libraries and JCA for TLS.
        * Add health‑check endpoint `/q/health`.
        * Reduce image size with jlink.

#### SUB‑TASK 1.5: Configure GCP IAM & Service Account
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/gcp/iam-config.yml
    * **Architectural Requirements:**
        * Create service account "membershiphub-kafka" with roles "Kafka Admin", "Pub/Sub Publisher".
        * Attach service account to Kubernetes service account via Workload Identity.

#### SUB‑TASK 1.6: Manager Orchestration & Validation
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/docs/enrollment-workflow.md
    * **Architectural Requirements:**
        * Document end‑to‑end enrollment flow, required permissions, and expected Kafka event structure.
        * Validate that enrollment creates student account and triggers notification.

### DAY 2: Promotion/Announcement CRUD & Multi‑Language SEO
#### SUB‑TASK 2.1: Implement Promotion & Announcement Entities & Services
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/entity/Promotion.java
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/entity/Announcement.java
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/PromotionService.java
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/AnnouncementService.java
    * **Architectural Requirements:**
        * Define @TenantEntity with tenant_id discriminator column.
        * Add expiry LocalDateTime fields; enforce validation (expiry >= now).
        * Provide CRUD methods with @RolesAllowed("Admin","Manager").
        * Emit Kafka events PromotionCreatedEvent / AnnouncementCreatedEvent.
        * Use @Transactional for atomic writes.
    * **Security Enforcement:**
        * OWASP A03: SQL injection prevention via @QueryAnnotation with parameter binding.
        * OWASP A02: Validate input length and content for XSS‑prone fields.

#### SUB‑TASK 2.2: Create Kafka Producers for Promotion & Announcement Events
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/kafka/PromotionEventProducer.java
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/kafka/AnnouncementEventProducer.java
    * **Architectural Requirements:**
        * Configure separate Kafka topics "promotion-events" and "announcement-events".
        * Include tenantId header for multi‑tenant routing.
    * **Security Enforcement:**
        * Secure producer configs via application.yml; rotate credentials via GCP Secret Manager.

#### SUB‑TASK 2.3: Implement Multi‑Language SEO Meta Tags in Next.js
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/frontend/src/pages/promotions/[id].tsx
* **Target Path:** ./sources/frontend/src/pages/announcements/[id].tsx
    * **Architectural Requirements:**
        * Generate `<meta>` tags per locale (en/vi) using `next/head`.
        * Pull promotion/announcement title, description, and expiry from API; include `og:image` if available.
        * Use `useRouter` to detect locale from URL path.
    * **Security Enforcement:**
        * Sanitize user‑provided content before embedding in meta tags to prevent XSS.

#### SUB‑TASK 2.4: Write Unit Tests for Promotion & Announcement Services
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/PromotionService.java;./sources/backend/src/test/java/org/nlhj/saas/membershippub/service/PromotionServiceTest.java
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/AnnouncementService.java;./sources/backend/src/test/java/org/nlhj/saas/membershippub/service/AnnouncementServiceTest.java
    * **Architectural Requirements:**
        * Mock repository and Kafka producers.
        * Verify expiry validation throws IllegalArgumentException.
        * Assert tenant isolation via tenant_id filter.

#### SUB‑TASK 2.5: Write Integration / UI Tests for Notification Flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/promotion.spec.ts
    * **Architectural Requirements:**
        * End‑to‑end test creating a promotion via API, verifying Kafka event triggers, and checking notification appears in UI.
        * Use Cypress fixtures for multi‑language content.

#### SUB‑TASK 2.6: Update GKE Deployment Manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/k8s/deployment.yml
    * **Architectural Requirements:**
        * Add environment variables for Kafka bootstrap servers.
        * Mount secret for GCP credentials.
        * Apply PodSecurityPolicy to enforce non‑root user.

#### SUB‑TASK 2.7: Manager Cross‑Team Validation
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/docs/promotion-announcement-validation.md
    * **Architectural Requirements:**
        * Verify CRUD endpoints respond with correct HTTP status codes.
        * Confirm notifications sent to Zalo groups and FCM via Kafka consumer logs.
        * Approve SEO meta tag generation for both languages.

### DAY 3: Real‑Time Dashboard Refresh, Advanced Tenant Isolation & Push Delivery Verification
#### SUB‑TASK 3.1: Implement Scheduled Dashboard Refresh Job
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/job/DashboardRefreshJob.java
    * **Architectural Requirements:**
        * Use Quarkus Scheduler @Scheduled(cron = "0 */15 * * * *") for 15‑min interval.
        * Aggregate tenant‑filtered counts of active courses, enrollments, upcoming announcements.
        * Store results in Redis cache key "dashboard:summary".
    * **Security Enforcement:**
        * Ensure job runs with minimal privileges; use tenantId from security context.

#### SUB‑TASK 3.2: Add Advanced Tenant Isolation Filters
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/repository/BaseRepository.java
    * **Architectural Requirements:**
        * Implement generic tenant filter method applyTenantFilter(Specification<T> spec, String tenantId).
        * Override findAll() in all entity repositories to auto‑apply filter.
    * **Security Enforcement:**
        * OWASP A01: Prevent data leakage via tenantId injection using parameterized filter.

#### SUB‑TASK 3.3: Implement Push Notification Delivery Verification
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/NotificationDeliveryVerifier.java
    * **Architectural Requirements:**
        * Call Zalo API and FCM endpoints; capture response codes.
        * Implement retry logic (max 3 attempts) with exponential backoff.
        * Log delivery status to audit table with tenantId.
    * **Security Enforcement:**
        * Store API keys in GCP Secret Manager; inject via application.yml.
        * Validate webhook signatures from Zalo to prevent spoofing.

#### SUB‑TASK 3.4: Write Unit Tests for Scheduled Job & Delivery Verifier
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/job/DashboardRefreshJob.java;./sources/backend/src/test/java/org/nlhj/saas/membershippub/job/DashboardRefreshJobTest.java
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/NotificationDeliveryVerifier.java;./sources/backend/src/test/java/org/nlhj/saas/membershippub/service/NotificationDeliveryVerifierTest.java
    * **Architectural Requirements:**
        * Mock Redis cache and scheduler trigger.
        * Verify tenant filter applied in repository calls.
        * Assert retry logic on failed external API calls.

#### SUB‑TASK 3.5: Conduct OWASP Compliance Review
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/EnrollmentService.java
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/PromotionService.java
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/AnnouncementService.java
* **Target Path:** ./sources/backend/src/main/java/org/nlhj/saas/membershippub/service/NotificationDeliveryVerifier.java
    * **Architectural Requirements:**
        * Verify parameterized queries, input validation, output encoding.
        * Confirm JWT token verification includes audience and issuer checks.
        * Ensure all sensitive fields are encrypted at rest.
    * **Security Enforcement:**
        * Document any findings and required remediation.

#### SUB‑TASK 3.6: Update Dockerfile for Scheduled Job Dependencies
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/docker/Dockerfile
    * **Architectural Requirements:**
        * Add JMX and metrics exporters (micrometer).
        * Include Redis client libraries.
        * Set JVM options for cron job isolation.

#### SUB‑TASK 3.7: Configure Cloud Scheduler & GKE CronJob
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/gcp/cloudscheduler.yml
    * **Architectural Requirements:**
        * Create Cloud Scheduler job triggering GKE CronJob "dashboard-refresh" every 15 minutes.
        * Set service account with roles "Cloud Scheduler Admin", "Kubernetes Engine Developer".

#### SUB‑TASK 3.8: GKE Deployment & Security Policies
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/k8s/cronjob.yml
    * **Architectural Requirements:**
        * Define CronJob resource with image from updated Dockerfile.
        * Apply PodSecurityPolicy restricting privileged containers.
        * Enable audit logging via GCP Cloud Audit Logs.

#### SUB‑TASK 3.9: Manager Final Sign‑Off
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path:** ./sources/backend/docs/phase4-final-signoff.md
    * **Architectural Requirements:**
        * Confirm all Phase 4 features implemented per requirements.
        * Validate end‑to‑end test results (unit, integration, UI).
        * Approve deployment to production GKE cluster.