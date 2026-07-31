# PHASE 5 CONTEXT BLUEPRINT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260731165119 |
| **Project Name** | membership-hub |
| **Phase** | 5 |
| **Version** | 1.0 (Baseline) |
| **Date/Time** | 2026/07/31 16:51:19 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
Phase 5 is the final integration and feature‑enrichment phase of the membership‑hub platform. It focuses on completing all remaining business capabilities that were not addressed in earlier phases: student enrollment, attendance capture, membership card lifecycle, promotion and announcement management, AI chatbot, mobile‑app role‑specific UI, push‑notification handling, localization, SEO, reporting, dashboards, and GDPR‑compliant data export. The phase also consolidates all modules, performs comprehensive security hardening, and produces full technical documentation. All new code must satisfy OWASP Top 10 mitigations, meet the performance, availability, scalability, and compliance NFRs, and achieve 100 % traceability of every tag defined in the global context.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Directory | Purpose | REST/GraphQL/Event Endpoint Patterns |
| :--- | :--- | :--- |
| `./sources/backend/student-enrollment` | Enrollment services | `/api/enrollments` (GET, POST, DELETE) |
| `./sources/backend/attendance` | Attendance capture | `/api/attendance` (POST) |
| `./sources/backend/card` | Membership card lifecycle | `/api/cards` (GET, POST) |
| `./sources/backend/notification` | Notification dispatch | `/api/notifications` (POST), `/api/notifications/push` (POST) |
| `./sources/backend/promotion` | Promotion CRUD | `/api/promotions` (GET, POST, PUT, DELETE) |
| `./sources/backend/announcement` | Announcement CRUD | `/api/announcements` (GET, POST, PUT, DELETE) |
| `./sources/backend/chatbot` | AI chatbot endpoint | `/api/chatbot/message` (POST) |
| `./sources/backend/localization` | Locale detection middleware | N/A (filter) |
| `./sources/backend/reporting` | Report generation | `/api/reports/attendance` (GET) |
| `./sources/backend/dashboard` | Dashboard data | `/api/dashboard/enrollment` (GET) |
| `./sources/backend/settings` | System settings | `/api/settings` (GET, PUT) |
| `./sources/frontend/web-app` | Web UI components | N/A (React SPA) |
| `./sources/frontend/mobile-app` | Mobile UI components | N/A (React Native) |
| `./sources/integration-tests` | End‑to‑end integration tests | N/A |
| `./sources/infra/docs` | Phase documentation | `phase5-implementation.md` |
| `./sources/ci` | CI pipeline simulation | `pipeline-sim.sh` |

All paths begin with `./sources/` and follow the Java package convention `org.nlh4j.saas.membershiphub`.

## 3. Dedicated Sub-Agent Functional Directives
| Sub-Agent | Responsibilities |
| :--- | :--- |
| **coder** | Implement business logic, REST controllers, services, and data access objects. |
| **tester** | Write and execute integration tests, ensuring functional coverage for all new APIs. |
| **reviewer** | Perform static analysis, OWASP compliance checks, and code‑quality reviews on all new source files. |
| **doc** | Compile comprehensive technical documentation, including architecture diagrams, API references, and deployment guides. |
| **docker** | (Not used in Phase 5 – infra already completed). |
| **GCP** | (Not used in Phase 5 – infra already deployed). |
| **GKE** | (Not used in Phase 5 – infra already deployed). |

## 4. Phase Definition of Done (DoD)
- All functional requirements [REQ-010]–[REQ-025] are fully implemented and pass unit/integration tests with ≥ 95 % coverage.  
- All exception flows [EXC-001]–[EXC-005] are handled with clear error responses.  
- Data dictionaries [DAT-004]–[DAT-011] are fully defined and mapped to database tables.  
- Every tag referenced in Phase 5 appears in at least one sub‑task traceability list.  
- OWASP Top 10 mitigations are applied (prepared statements, CSP headers, CSRF tokens, input validation).  
- Performance, availability, scalability, and compliance NFRs [NFR-001]–[NFR-009] are validated through load tests and security scans.  
- Full technical documentation is produced and stored in `./sources/infra/docs/phase5-implementation.md`.  
- CI pipeline simulation passes all stages (build, test, deploy, monitor).  
- Final audit confirms 100 % tag coverage and compliance.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: ENROLLMENT, ATTENDANCE, CARD, AND NOTIFICATION CORE

#### SUB-TASK 1.1: Implement Student Course Browse API
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/student-enrollment/StudentBrowseController.java`
* **Traceability Tag Tokens:** `[REQ-010], [DAT-004], [EXC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * REST controller with `@GetMapping("/api/enrollments")`.  
  * Service layer queries `Enrollments` table with pagination.  
  * Input validation via `@Valid` DTOs.  
  * Use prepared statements to prevent SQLi.  
  * Return JSON with HATEOAS links.  

#### SUB-TASK 1.2: Implement Student Course Registration API
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/student-enrollment/StudentRegistrationService.java`
* **Traceability Tag Tokens:** `[REQ-011], [DAT-004], [EXC-004], [EXC-005], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Service method `registerStudentToCourse(UUID studentId, UUID courseId)`.  
  * Transactional integrity with `@Transactional`.  
  * Conflict detection for duplicate enrollment.  
  * Audit log entry via `AuditService`.  
  * Return 201 Created with location header.  

#### SUB-TASK 1.3: Implement Attendance Capture API
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/attendance/AttendanceController.java`
* **Traceability Tag Tokens:** `[REQ-012], [DAT-005], [EXC-001], [EXC-002], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * POST `/api/attendance` accepts JSON payload `{studentId, courseId, timestamp}`.  
  * Validate enrollment via `EnrollmentRepository`.  
  * Idempotency key via composite unique constraint on `(student_id, course_id, attendance_date)`.  
  * Return 200 OK with `duplicate: true/false`.  

#### SUB-TASK 1.4: Implement Attendance Idempotency Logic
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/attendance/AttendanceService.java`
* **Traceability Tag Tokens:** `[REQ-013], [DAT-005], [EXC-002], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Check existing record before insert.  
  * Use `@Transactional` with `REPEATABLE_READ` isolation.  
  * Log duplicate attempts via `AuditService`.  

#### SUB-TASK 1.5: Implement Student Card Validity API
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/card/CardController.java`
* **Traceability Tag Tokens:** `[REQ-014], [DAT-006], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * GET `/api/cards/{studentId}` returns card status.  
  * Compute `remaining_days` via `issue_date + validity_days - current_date`.  
  * Use caching for frequent reads.  

#### SUB-TASK 1.6: Implement Card Renewal API
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/card/CardService.java`
* **Traceability Tag Tokens:** `[REQ-015], [DAT-006], [EXC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * POST `/api/cards/renew` with `{studentId, renewalDays}`.  
  * Validate `renewalDays` range 1–365.  
  * Update `validity_days` atomically.  
  * Trigger push notification via `NotificationService`.  

#### SUB-TASK 1.7: Implement Notification Trigger for Enrollment, Attendance, Card Renewal
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/notification/NotificationService.java`
* **Traceability Tag Tokens:** `[REQ-016], [DAT-007], [EXC-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Publish events to Kafka topic `notifications`.  
  * Consume events and send push via FCM/APNs.  
  * Post Zalo group messages via webhook.  
  * Retry logic with exponential back‑off.  

#### SUB-TASK 1.8: Implement Global Exception Handlers
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/common/GlobalExceptionHandler.java`
* **Traceability Tag Tokens:** `[EXC-004], [EXC-001], [EXC-002], [EXC-003], [ARC-005], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * `@ControllerAdvice` with handlers for `MethodArgumentNotValidException`, `DataIntegrityViolationException`, `RestClientException`.  
  * Return standardized error JSON with `errorCode`, `message`.  
  * Log stack trace at WARN level.  

#### SUB-TASK 1.9: Implement Logging and Audit Service
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/common/AuditService.java`
* **Traceability Tag Tokens:** `[NFR-006], [NFR-008], [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005]`
* **Architectural Requirements:**
  * Persist audit records to `audit_logs` table with `user_id`, `action`, `timestamp`, `details`.  
  * Use `@Async` to avoid blocking.  
  * Rotate logs daily, retain 365 days.  

### DAY 2: PROMOTIONS, ANNOUNCEMENTS, CHATBOT, MOBILE UI, PUSH NOTIFICATIONS, SETTINGS

#### SUB-TASK 2.1: Implement Promotion Management API
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/promotion/PromotionController.java`
* **Traceability Tag Tokens:** `[REQ-017], [DAT-009], [EXC-004], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * CRUD endpoints `/api/promotions`.  
  * Validate `discount_percent` 1–100.  
  * Store `start_date`, `end_date` with timezone awareness.  
  * Trigger notification to affected students.  

#### SUB-TASK 2.2: Implement Announcement Management API
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/announcement/AnnouncementController.java`
* **Traceability Tag Tokens:** `[REQ-018], [DAT-010], [EXC-004], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * CRUD endpoints `/api/announcements`.  
  * Optional `expiry_date` handling.  
  * Publish to all users via `NotificationService`.  

#### SUB-TASK 2.3: Implement AI Chatbot Integration Endpoint
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/chatbot/ChatbotController.java`
* **Traceability Tag Tokens:** `[REQ-019], [DAT-011], [EXC-004], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * POST `/api/chatbot/message` accepts `{sessionId, message}`.  
  * Forward to external AI service, cache responses.  
  * Return `{reply, confidence}`.  
  * If confidence < 0.4, route to human queue.  

#### SUB-TASK 2.4: Implement Mobile App Role‑Specific UI Components
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/mobile-app/src/components/RoleSpecificUI.js`
* **Traceability Tag Tokens:** `[REQ-020], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Conditional rendering based on `role` prop.  
  * Use React Navigation for role‑specific screens.  
  * Lazy load role modules to reduce bundle size.  

#### SUB-TASK 2.5: Implement Push Notification Registration Endpoint
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/notification/PushNotificationController.java`
* **Traceability Tag Tokens:** `[REQ-021], [DAT-007], [EXC-003], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * POST `/api/notifications/push/register` with `{userId, deviceToken, platform}`.  
  * Persist to `device_tokens` table.  
  * Validate token format.  

#### SUB-TASK 2.6: Implement Exception Handling for Invalid Input and Failed Notification Delivery
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/common/GlobalExceptionHandler.java` (reuse)
* **Traceability Tag Tokens:** `[EXC-004], [EXC-003], [ARC-005], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Add handlers for `IllegalArgumentException`, `NotificationDeliveryException`.  
  * Return 400 or 502 with descriptive message.  

#### SUB-TASK 2.7: Implement System Settings API
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/settings/SystemSettingsController.java`
* **Traceability Tag Tokens:** `[DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * GET `/api/settings` returns key/value pairs.  
  * PUT `/api/settings/{key}` updates value.  
  * Persist to `system_settings` table.  

### DAY 3: LOCALIZATION, SEO, REPORTING, DASHBOARD, GDPR EXPORT

#### SUB-TASK 3.1: Implement Default Locale Detection Middleware
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/localization/LocaleFilter.java`
* **Traceability Tag Tokens:** `[REQ-022], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Servlet filter that reads `Accept-Language` header or `locale` cookie.  
  * Set `LocaleContextHolder` for Spring MVC.  
  * Fallback to default `en`.  

#### SUB-TASK 3.2: Implement Multi‑Language SEO Meta Tags
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/web-app/src/components/SeoMeta.js`
* **Traceability Tag Tokens:** `[REQ-023], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Render `<html lang="...">` and `<link rel="alternate" hreflang="...">`.  
  * Use i18n library for dynamic meta content.  

#### SUB-TASK 3.3: Implement Attendance Report Generation Endpoint
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/reporting/AttendanceReportService.java`
* **Traceability Tag Tokens:** `[REQ-024], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [EXC-004], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Generate CSV with columns `StudentName, CourseName, AttendanceDate, Status`.  
  * Use streaming to avoid memory blow‑up.  
  * Validate date range ≤ 30 days.  

#### SUB-TASK 3.4: Implement Enrollment Summary Dashboard Endpoint
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/dashboard/DashboardService.java`
* **Traceability Tag Tokens:** `[REQ-025], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-009], [DAT-010], [DAT-011], [EXC-004], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-001], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Aggregated metrics: total students, active courses, upcoming sessions.  
  * Cache results for 5 min.  
  * Return JSON for frontend consumption.  

#### SUB-TASK 3.5: Implement Exception Handling for Report Input Validation
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/common/GlobalExceptionHandler.java` (reuse)
* **Traceability Tag Tokens:** `[EXC-004], [ARC-005], [NFR-003], [NFR-006], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Validate `startDate <= endDate` and range ≤ 30 days.  
  * Return 400 Bad Request with error details.  

#### SUB-TASK 3.6: Implement GDPR Data Export Endpoint
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/settings/GdprExportService.java`
* **Traceability Tag Tokens:** `[EXC-004], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Generate JSON payload of user data upon request.  
  * Encrypt file with AES‑256.  
  * Provide secure download link with signed token.  

### DAY 4: INTEGRATION TESTS, SECURITY REVIEW, DOCUMENTATION, FINAL APPROVAL

#### SUB-TASK 4.1: Write Integration Tests for All Modules
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `INTEGRATION_SCOPE;./sources/integration-tests/EnrollmentIntegrationTest.java`
* **Traceability Tag Tokens:** `[REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [ARC-011], [ARC-012], [ARC-013], [ARC-014], [ARC-015], [ARC-016], [ARC-017], [ARC-018], [ARC-019], [ARC-020], [ARC-021], [ARC-022], [ARC-023], [NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009]`
* **Architectural Requirements:**
  * Use Spring Boot Test with Testcontainers for PostgreSQL and Kafka.  
  * Mock external AI and notification services.  
  * Verify CRUD flows, idempotency, exception handling.  

#### SUB-TASK 4.2: Perform OWASP Static Analysis on All New Source Files
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/**/*.java`
* **Traceability Tag Tokens:** `[NFR-003], [NFR-006], [NFR-008], [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [ARC-011], [ARC-012], [ARC-013], [ARC-014], [ARC-015], [ARC-016], [ARC-017], [ARC-018], [ARC-019], [ARC-020], [ARC-021], [ARC-022], [ARC-023]`
* **Architectural Requirements:**
  * Run SpotBugs, SonarQube, OWASP Dependency‑Check.  
  * Ensure no high‑severity findings.  
  * Generate report and fix issues.  

#### SUB-TASK 4.3: Compile Technical Documentation for Phase 5 Modules
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/docs/phase5-implementation.md`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [ARC-011], [ARC-012], [ARC-013], [ARC-014], [ARC-015], [ARC-016], [ARC-017], [ARC-018], [ARC-019], [ARC-020], [ARC-021], [ARC-022], [ARC-023], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]`
* **Architectural Requirements:**
  * Include architecture diagram, API reference, deployment guide, security checklist.  
  * Use Markdown with code blocks for snippets.  

#### SUB-TASK 4.4: Final Approval of All Artifacts
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/docs/phase5-implementation.md;./sources/backend/**/*.java;./sources/integration-tests/**/*.java`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [ARC-011], [ARC-012], [ARC-013], [ARC-014], [ARC-015], [ARC-016], [ARC-017], [ARC-018], [ARC-019], [ARC-020], [ARC-021], [ARC-022], [ARC-023], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]`
* **Architectural Requirements:**
  * Verify all tags covered, no critical findings, documentation complete.  
  * Approve merge to main branch.  

### DAY 5: CI PIPELINE SIMULATION, FINAL AUDIT, RELEASE

#### SUB-TASK 5.1: Run Full CI Pipeline Simulation
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/ci/pipeline-sim.sh`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [ARC-011], [ARC-012], [ARC-013], [ARC-014], [ARC-015], [ARC-016], [ARC-017], [ARC-018], [ARC-019], [ARC-020], [ARC-021], [ARC-022], [ARC-023], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]`
* **Architectural Requirements:**
  * Execute build, unit tests, integration tests, static analysis, and deploy to test GKE cluster.  
  * Verify health checks, metrics, and alerting.  

#### SUB-TASK 5.2: Perform Final Audit of Tag Coverage and Compliance
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/docs/phase5-implementation.md;./sources/backend/**/*.java;./sources/integration-tests/**/*.java;./sources/ci/pipeline-sim.sh`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [ARC-011], [ARC-012], [ARC-013], [ARC-014], [ARC-015], [ARC-016], [ARC-017], [ARC-018], [ARC-019], [ARC-020], [ARC-021], [ARC-022], [ARC-023], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]`
* **Architectural Requirements:**
  * Confirm 100 % tag coverage, no critical OWASP findings, documentation completeness.  

#### SUB-TASK 5.3: Merge Changes to Main Branch and Tag Release
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/infra/docs/phase5-implementation.md;./sources/backend/**/*.java;./sources/integration-tests/**/*.java;./sources/ci/pipeline-sim.sh`
* **Traceability Tag Tokens:** `[NFR-001], [NFR-002], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-007], [NFR-008], [NFR-009], [ARC-001], [ARC-002], [ARC-003], [ARC-004], [ARC-005], [ARC-006], [ARC-007], [ARC-008], [ARC-009], [ARC-010], [ARC-011], [ARC-012], [ARC-013], [ARC-014], [ARC-015], [ARC-016], [ARC-017], [ARC-018], [ARC-019], [ARC-020], [ARC-021], [ARC-022], [ARC-023], [REQ-010], [REQ-011], [REQ-012], [REQ-013], [REQ-014], [REQ-015], [REQ-016], [REQ-017], [REQ-018], [REQ-019], [REQ-020], [REQ-021], [REQ-022], [REQ-023], [REQ-024], [REQ-025], [EXC-001], [EXC-002], [EXC-003], [EXC-004], [EXC-005], [DAT-004], [DAT-005], [DAT-006], [DAT-007], [DAT-008], [DAT-009], [DAT-010], [DAT-011]`
* **Architectural Requirements:**
  * Create Git tag `v1.0-phase5`.  
  * Push to main branch.  
  * Trigger production deployment pipeline.