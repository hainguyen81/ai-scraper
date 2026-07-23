# PHASE 3 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement Teacher, Center, Promotions & Announcements management capabilities for the multi‑tenant SaaS platform. This phase delivers:

* **Teacher CRUD & Course Assignment** – Create/Read/Update/Delete teacher records, assign/unassign teachers to courses, and emit real‑time notifications to teachers via Zalo groups and mobile push.  
* **Center Management UI** – System‑Admin‑only console for listing, editing, and assigning Admins/Managers to centers; tenant‑isolated data access.  
* **Promotions Management** – Full lifecycle (create/edit/delete) of promotional programs with validity windows; broadcast to all non‑System‑Admin roles.  
* **Announcements Management** – Parallel CRUD for admin announcements with validity windows; same broadcast semantics as promotions.  
* **Dashboard Integration** – Consolidated view of today’s courses/teachers, student card remaining days, active promotions/announcements; auto‑refresh every 15 min driven by environment variable.  
* **Broadcast Notification Service** – Unified backend service that pushes messages to Zalo groups and mobile push (FCM/WebSocket) for all relevant role groups.  
* **Integration Test Coverage** – End‑to‑end verification of promotion/announcement triggers, tenant isolation, and notification delivery.

All components must obey OWASP hardening (parameterized queries, tenant_id isolation, AES‑256‑GCM PII encryption where applicable) and follow the Java package convention `org.nlh4j.saas.membershiphub`.

## 2. Allowed Technical Scope & Directory Boundaries
* **Backend Service** – Single monolithic service named `membership-hub`.  
  * `./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/` – Java domain models, services, controllers.  
  * `./sources/backend/membership-hub/src/main/resources/` – Quarkus config, schema migrations (Flyway/Liquibase).  
  * `./sources/backend/membership-hub/src/test/java/org/nlh4j/saas/membershiphub/` – Unit/Integration test suites.  
  * `./sources/backend/membership-hub/Dockerfile` – Multi‑stage container image.  
  * `./sources/backend/membership-hub/src/main/docker/` – Optional Kafka/connect configs.  

* **Frontend Web & Mobile Apps** – Unified Next.js codebase.  
  * `./sources/frontend/src/` – React components, pages, i18n resources, state (React‑Query).  
  * `./sources/frontend/src/components/` – Role‑based UI guards, dashboard, teacher/center/promotion/announcement forms.  
  * `./sources/frontend/src/services/` – API client, WebSocket/FCM bridges, notification stream.  
  * `./sources/frontend/src/tests/` – Jest/React‑Testing‑Library unit & integration tests.  
  * `./sources/frontend/Dockerfile` – Container image for web/mobile serving.  

* **DevOps & Orchestration** –  
  * `./sources/backend/membership-hub/k8s/` – GKE Deployment, Service, Ingress, HPA manifests.  
  * `./sources/frontend/k8s/` – Corresponding frontend service definitions.  
  * `./sources/infra/` – GCP Cloud Build pipelines, IAM policies, Service Accounts, Artifact Registry configs.  

All paths are absolute to the workspace root and strictly under `./sources/`.

## 3. Dedicated Sub-Agent Functional Directives
* **Coder** – Implement domain entities, Spring‑Boot (Quarkus) services, REST controllers, notification dispatch logic, and frontend React components. Inject OWASP compliance (parameterized queries, tenant_id filtering, AES‑256‑GCM for PII).  
* **Tester** – Write unit tests for service logic and integration/E2E tests for promotion/announcement workflows; use `INTEGRATION_SCOPE` where tests span multiple components.  
* **Docker** – Update multi‑stage Dockerfiles for backend and frontend, ensure proper JVM/Memory settings, and add health‑check probes.  
* **GCP** – Create/ amend Cloud Build triggers, IAM Service Accounts, and Artifact Registry repositories; configure GKE namespace and resource quotas.  
* **GKE** – Produce Kubernetes manifests for deployments, services, ingress, and HPA; embed tenant‑aware resource limits.  
* **Manager** – Oversee cross‑component integration, validate tenant isolation, and ensure all generated artifacts conform to the `./sources/` boundary rule.

## 4. Phase Definition of Done (DoD)
* All Teacher, Center, Promotion, and Announcement CRUD operations functional with proper role‑based access control.  
* Backend services secured with OWASP A01‑A09 controls (parameterized queries, tenant isolation, encryption).  
* Frontend UI mirrors admin functionality, respects role guards, and supports multi‑language SEO.  
* Dashboard auto‑refreshes every 15 min via environment‑driven interval; displays required aggregates.  
* Broadcast notification pipeline successfully pushes to Zalo groups and mobile push for all targeted roles.  
* 100 % unit test coverage for new backend services; integration/E2E test suites pass for promotion/announcement triggers.  
* Docker images built, GKE deployments ready, and GCP CI/CD pipelines updated.  
* All artifacts placed under `./sources/` with correct Java package layout (`org.nlh4j.saas.membershiphub`).  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Teacher CRUD & Course Assignment
#### SUB‑TASK 1.1: Implement Teacher Entity & Repository
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/domain/Teacher.java
    *   **Architectural Requirements:**
        *   Annotate with `@TenantEntity` discriminator (`tenant_id` column) and `@EncryptedField` for PII fields (e.g., SSN).  
        *   Use Lombok `@Data`/`@Entity`; enforce `@Size`/`@Email` validation per OWASP A03.  
        *   Implement `equals`/`hashCode` based on composite key (`id`, `tenantId`).  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/repository/TeacherRepository.java
    *   **Architectural Requirements:**
        *   Extend `JpaRepository<Teacher, Long>`; add custom query methods filtered by `tenantId`.  
        *   Use `@Query` with parameter binding to prevent injection.  
        *   Include tenant isolation via `@TenantFilter` annotation.  

#### SUB‑TASK 1.2: Create Teacher Service & REST Controller
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/TeacherService.java
    *   **Architectural Requirements:**
        *   Implement CRUD methods (`createTeacher`, `updateTeacher`, `deleteTeacher`).  
        *   Apply `@Transactional` with read‑only flags where appropriate.  
        *   Enforce business rule: teacher can only belong to a single center per tenant.  
        *   Log all changes via `@AuditLog` for OWASP A12.  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/controller/TeacherController.java
    *   **Architectural Requirements:**
        *   Expose `POST /api/teachers`, `PUT /api/teachers/{id}`, `DELETE /api/teachers/{id}`.  
        *   Validate request payloads with `@Valid`.  
        *   Return `201/200/404` with appropriate `ResponseEntity`.  
        *   Include `X-Tenant-ID` header validation.  

#### SUB‑TASK 1.3: Write Unit Tests for Teacher Service
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/TeacherService.java;./sources/backend/membership-hub/src/test/java/org/nlh4j/saas/membershiphub/service/TeacherServiceTest.java
    *   **Architectural Requirements:**
        *   Cover happy path and edge cases (duplicate email, invalid tenant).  
        *   Mock `TeacherRepository` and verify tenant isolation.  
        *   Assert encryption usage for PII fields via mock verification.  

### DAY 2: Teacher‑Course Assignment & Notifications
#### SUB‑TASK 2.1: Implement Course‑Teacher Join Entity & Service
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/domain/CourseTeacher.java
    *   **Architectural Requirements:**
        *   Composite primary key (`courseId`, `teacherId`, `tenantId`).  
        *   `@TenantEntity` and `@CreatedBy` audit fields.  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/TeacherCourseService.java
    *   **Architectural Requirements:**
        *   Methods `assignTeacherToCourse`, `unassignTeacher`.  
        *   Emit `TeacherAssignedEvent` to Kafka topic `teacher-assignments`.  
        *   Validate overlapping assignments per tenant.  

#### SUB‑TASK 2.2: Create Notification Dispatcher for Teacher Assignments
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java
    *   **Architectural Requirements:**
        *   Consume `TeacherAssignedEvent` via SmallRye Kafka.  
        *   Build payload with tenant‑specific Zalo group ID and FCM token.  
        *   Use `@Transactional` for atomic send; implement retry logic.  
        *   Log all outbound notifications for audit (OWASP A12).  

#### SUB‑TASK 2.3: Frontend Teacher Assignment UI Component
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/teacher/TeacherAssignmentForm.tsx
    *   **Architectural Requirements:**
        *   Form fields: Select Teacher, Select Course (filtered by tenant).  
        *   Role guard: only Admin/Manager can assign.  
        *   i18n support with `useTranslation`.  
        *   Submit calls `POST /api/teacher-courses`.  

#### SUB‑TASK 2.4: Integration Test for Assignment Notification Flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/teacherAssignment.spec.ts
    *   **Architectural Requirements:**
        *   Simulate admin user login, assign teacher to course, verify Kafka event emission (mock).  
        *   Assert notification service receives event and triggers push (mock).  
        *   Validate UI reflects assignment instantly.  

### DAY 3: Center Management UI (System Admin Only)
#### SUB‑TASK 3.1: Define Center Entity & Repository
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/domain/Center.java
    *   **Architectural Requirements:**
        *   `@TenantEntity` with `tenantId` discriminator.  
        *   Fields: name, address, phone, taxId (encrypted).  
        *   Validation: non‑blank name, regex phone.  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/repository/CenterRepository.java
    *   **Architectural Requirements:**
        *   JpaRepository with tenant‑filtered queries.  
        *   Custom `findByTenantId` method.  

#### SUB‑TASK 3.2: Implement Center Service & REST Endpoints
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/CenterService.java
    *   **Architectural Requirements:**
        *   CRUD operations (`createCenter`, `updateCenter`, `deleteCenter`).  
        *   Assign/unassign Admin/Manager via dedicated methods.  
        *   Enforce that only System‑Admin can modify centers (`@PreAuthorize("hasRole('SYSADMIN')")`).  
        *   Log all changes.  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/controller/CenterController.java
    *   **Architectural Requirements:**
        *   Expose `GET /api/centers`, `POST /api/centers`, `PUT /api/centers/{id}`, `DELETE /api/centers/{id}`.  
        *   Return paginated results with `Pageable`.  
        *   Include `X-Tenant-ID` validation; filter results by tenant unless SYSADMIN.  

#### SUB‑TASK 3.3: Frontend Center Management Page
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/pages/center/CenterManagement.tsx
    *   **Architectural Requirements:**
        *   Table listing centers with edit/delete actions.  
        *   Modal for adding/editing centers.  
        *   Dropdown to assign/unassign Admin/Manager (only visible to SYSADMIN).  
        *   Role guard: hide component if not SYSADMIN.  
        *   i18n and SEO meta tags via `_app` wrapper.  

#### SUB‑TASK 3.4: Unit Tests for Center Service
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/CenterService.java;./sources/backend/membership-hub/src/test/java/org/nlh4j/saas/membershiphub/service/CenterServiceTest.java
    *   **Architectural Requirements:**
        *   Verify tenant isolation in CRUD operations.  
        *   Assert authorization checks block non‑SYSADMIN users.  
        *   Mock repository calls and verify correct logging.  

### DAY 4: Promotions Management
#### SUB‑TASK 4.1: Create Promotion Entity & Repository
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/domain/Promotion.java
    *   **Architectural Requirements:**
        *   `@TenantEntity` with fields: name, description, conditionJson (encrypted), startDate, endDate (nullable).  
        *   Validation: startDate ≤ endDate if provided.  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/repository/PromotionRepository.java
    *   **Architectural Requirements:**
        *   JpaRepository with tenant filter; add `findActivePromotions(LocalDate date)`.  

#### SUB‑TASK 4.2: Implement Promotion Service & Broadcast Logic
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/PromotionService.java
    *   **Architectural Requirements:**
        *   CRUD methods (`createPromotion`, `updatePromotion`, `deletePromotion`).  
        *   On create/update, emit `PromotionEvent` to Kafka topic `promotions`.  
        *   Validate promotion windows against current date; enforce tenant isolation.  
        *   Use `@Transactional` and audit logging.  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/listener/PromotionEventListener.java
    *   **Architectural Requirements:**
        *   Consume `PromotionEvent`; trigger broadcast to all roles except SYSADMIN via `NotificationService`.  

#### SUB‑TASK 4.3: Frontend Promotions Management UI
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/promotion/PromotionForm.tsx
    *   **Architectural Requirements:**
        *   Form fields for name, description, condition, start/end dates.  
        *   Role guard: Admin/Manager only.  
        *   Submit calls `POST/PUT /api/promotions`.  
        *   Show validation errors with i18n.  

#### SUB‑TASK 4.4: Integration Test for Promotion Broadcast
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/promotionBroadcast.spec.ts
    *   **Architectural Requirements:**
        *   Simulate creation of a promotion, verify Kafka event emission (mock).  
        *   Confirm notification service receives event and sends push to target roles.  
        *   Assert UI updates reflect new promotion instantly.  

### DAY 5: Announcements Management
#### SUB‑TASK 5.1: Define Announcement Entity & Repository
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/domain/Announcement.java
    *   **Architectural Requirements:**
        *   `@TenantEntity` with fields: title, content (encrypted), startDate, endDate (nullable).  
        *   Validation similar to Promotion.  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/repository/AnnouncementRepository.java
    *   **Architectural Requirements:**
        *   JpaRepository with tenant filter; add `findActiveAnnouncements(LocalDate date)`.  

#### SUB‑TASK 5.2: Implement Announcement Service & Event Emission
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/AnnouncementService.java
    *   **Architectural Requirements:**
        *   CRUD methods (`createAnnouncement`, `updateAnnouncement`, `deleteAnnouncement`).  
        *   Emit `AnnouncementEvent` to Kafka topic `announcements`.  
        *   Enforce tenant isolation and audit logging.  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/listener/AnnouncementEventListener.java
    *   **Architectural Requirements:**
        *   Consume `AnnouncementEvent`; delegate broadcast via `NotificationService`.  

#### SUB‑TASK 5.3: Frontend Announcements Management UI
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/announcement/AnnouncementForm.tsx
    *   **Architectural Requirements:**
        *   Form fields for title, content, dates.  
        *   Role guard: Admin/Manager only.  
        *   Submit calls `POST/PUT /api/announcements`.  

#### SUB‑TASK 5.4: Unit Tests for Announcement Service
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/AnnouncementService.java;./sources/backend/membership-hub/src/test/java/org/nlh4j/saas/membershiphub/service/AnnouncementServiceTest.java
    *   **Architectural Requirements:**
        *   Verify CRUD operations and event emission.  
        *   Validate tenant filtering and encryption of content.  

### DAY 6: Dashboard Integration & Auto‑Refresh
#### SUB‑TASK 6.1: Create Dashboard Service Aggregator
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/service/DashboardService.java
    *   **Architectural Requirements:**
        *   Methods: `getTodayCourses`, `getTodayTeachers`, `getStudentCardDays`, `getActivePromotions`, `getActiveAnnouncements`.  
        *   All queries filtered by authenticated tenant (or SYSADMIN bypass).  
        *   Use native SQL/JPQL for performance; avoid in‑memory loops.  
        *   Return DTOs with encrypted fields where needed.  

#### SUB‑TASK 6.2: Implement Dashboard REST Endpoint
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/controller/DashboardController.java
    *   **Architectural Requirements:**
        *   Expose `GET /api/dashboard`.  
        *   Inject `X-Tenant-ID` header; enforce role‑based visibility.  
        *   Cache response for 5 minutes using Quarkus cache annotation.  

#### SUB‑TASK 6.3: Frontend Dashboard Component with Auto‑Refresh
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/dashboard/Dashboard.tsx
    *   **Architectural Requirements:**
        *   Fetch data from `/api/dashboard` using React‑Query.  
        *   Implement auto‑refresh based on environment variable `DASHBOARD_REFRESH_INTERVAL` (default 90000ms).  
        *   Role‑specific rendering: student sees card days; admin/manager sees course/teacher lists.  
        *   Integrate i18n and SEO meta tags.  

#### SUB‑TASK 6.4: Integration Test for Dashboard Data Consistency
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/dashboard.spec.ts
    *   **Architectural Requirements:**
        *   Simulate logged‑in user, verify dashboard fields populate correctly.  
        *   Mock auto‑refresh timer and assert data re‑fetches.  
        *   Validate tenant isolation (different tenants see different data).  

### DAY 7: Final Integration, Security Hardening & Production Prep
#### SUB‑TASK 7.1: Update Backend Dockerfile & Health Checks
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/Dockerfile
    *   **Architectural Requirements:**
        *   Multi‑stage build: Maven compile → slim JRE.  
        *   Add JVM flags for memory limits (`-Xmx512m`).  
        *   Include health‑check endpoint (`/q/health`).  
        *   Set non‑root user for security.  

#### SUB‑TASK 7.2: Update Frontend Dockerfile & Nginx Config
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/Dockerfile
    *   **Architectural Requirements:**
        *   Node‑alpine build stage → production optimized.  
        *   Use Nginx for static serving; configure proxy to backend.  
        *   Add security headers (CSP, HSTS).  

#### SUB‑TASK 7.3: Create GKE Deployment YAMLs
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/k8s/Deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy backend as `membership-hub` with resource limits (CPU/Memory).  
        *   Include `env` for `TENANT_ID`, `DASHBOARD_REFRESH_INTERVAL`.  
        *   Add `readinessProbe`/`livenessProbe` using `/q/health`.  
        *   Use `imagePullSecrets` for Artifact Registry.  
*   **Target Path:** ./sources/frontend/k8s/Deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy Next.js as `membership-hub-frontend`.  
        *   Configure HPA based on CPU utilization.  

#### SUB‑TASK 7.4: Update GCP CI/CD Pipeline Config
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/infra/cloudbuild.yaml
    *   **Architectural Requirements:**
        *   Define steps: Maven build → Docker build (backend) → Docker build (frontend) → push to Artifact Registry.  
        *   Include `substitutions` for `PROJECT_ID`, `LOCATION`.  
        *   Trigger on `main` branch; apply GKE deployments via `kubectl`.  

#### SUB‑TASK 7.5: Security Review & OWASP Hardening Checklist
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/config/SecurityConfig.java
    *   **Architectural Requirements:**
        *   Enable CSRF protection (`@EnableWebSecurity`).  
        *   Configure CORS per tenant origins.  
        *   Implement rate‑limiting using Quarkus `RateLimit` interceptor.  
        *   Enforce password policy with Argon2id hashing.  
        *   Set JWT token expiration and revocation list.  
*   **Target Path:** ./sources/backend/membership-hub/src/main/java/org/nlh4j/saas/membershiphub/util/AesEncryptionUtil.java
    *   **Architectural Requirements:**
        *   Provide AES‑256‑GCM utility for PII fields.  
        *   Centralize key management via GCP Secret Manager.  

#### SUB‑TASK 7.6: End‑to‑End Integration Test Suite
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/e2e/fullFlow.spec.ts
    *   **Architectural Requirements:**
        *   Simulate System‑Admin login, create a center, assign admin, add teacher, assign to course, create promotion, create announcement.  
        *   Verify each step triggers appropriate Kafka events and notifications (mock).  
        *   Validate tenant isolation across created entities.  
        *   Assert UI reflects all changes in real time.  

#### SUB‑TASK 7.7: Manager Orchestration Validation
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/infra/phase3-orchestration.md
    *   **Architectural Requirements:**
        *   Document day‑by‑day task completion, agent assignments, and target paths.  
        *   Capture any deviations from the `./sources/` boundary rule and corrective actions.  
        *   Provide sign‑off checklist confirming all Phase 3 objectives met, OWASP compliance, and test coverage.