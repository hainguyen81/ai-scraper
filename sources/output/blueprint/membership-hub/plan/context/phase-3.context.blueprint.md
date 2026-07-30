# PHASE 3 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Implement core attendance tracking, QR code scanning, and notification services within the backend to satisfy real‑time attendance capture, idempotency, and multi‑channel communication requirements. Deliver unit‑test coverage for these services, comprehensive technical documentation, and ensure OWASP‑aligned security controls (parameterized queries, input validation, tenant isolation, PII encryption, audit logging). The phase concludes with fully functional REST endpoints for attendance capture (`/api/attendance`), QR scanning (`/api/qr/scan`), and notification dispatch (`/api/notifications`) ready for integration with the frontend and mobile apps.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Service Directory:** `./sources/backend/src/services/`
- **Backend Model Directory:** `./sources/backend/src/models/` (inherit `[DAT-005]` and `[DAT-007]`)
- **Backend Validation/Utility Directory:** `./sources/backend/src/validators/`
- **Backend Test Directory:** `./sources/backend/tests/`
- **Backend Documentation Directory:** `./sources/backend/docs/`
- **Allowed REST Endpoints (Phase‑3 scope):**
  - `POST /api/attendance` – record attendance via QR payload
  - `POST /api/qr/scan` – decode and validate QR payload
  - `POST /api/notifications` – queue push and Zalo group messages
- **Security‑related Paths:** All file paths must be under `./sources/backend/` to enforce workspace boundary compliance.
- **No frontend, infra, or mobile code may be created in this phase.**

## 3. Dedicated Sub-Agent Functional Directives
- **coder Agent:** Develop production‑grade TypeScript services implementing attendance capture, QR validation, and notification queuing. Enforce OWASP Top 10 mitigations (SQL injection prevention via parameterized queries, XSS prevention on any UI‑related payloads, CSRF tokens for state‑changing operations), multi‑tenant `tenant_id` scoping, AES‑256 encryption for any PII in logs, and comprehensive audit logging per `[NFR-006]`. Ensure idempotent attendance handling and retry logic for notifications.
- **doc Agent:** Produce complete technical documentation for the three services, including API contracts, sequence diagrams, data models, security considerations, and deployment notes. Store artifacts under `./sources/backend/docs/` and reference the exact requirement tags for traceability.
- **tester Agent:** Write focused unit tests that achieve >90 % statement coverage for each service, covering normal flows, edge cases, and exception scenarios (`[EXC-001]`‑`[EXC-005]`). Validate idempotency, duplicate detection, and notification retry mechanisms. Use the prescribed `<source>;<test>` syntax for test target paths.

## 4. Phase Definition of Done (DoD)
- All backend services (`AttendanceService`, `QRScannerService`, `NotificationService`) are implemented, compiled, and integrated into the build.
- Unit‑test suites exist for each service, achieving ≥90 % code coverage and passing all test suites.
- OWASP controls are embedded: input validation, parameterized queries, tenant isolation, JWT‑based authz, PII encryption, and audit logs per `[NFR-006]`.
- Documentation files are generated under `./sources/backend/docs/` covering API specs, data models, and security architecture.
- REST endpoints are functional and ready for integration testing.
- No security vulnerabilities remain per static analysis (no reviewer agent required for this phase).

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Core Attendance & QR Scanning Service Implementation
#### SUB-TASK 1.1: Implement AttendanceService with Idempotent Capture Logic
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/services/AttendanceService.ts`
* **Architectural Requirements:**
  * Implement a `recordAttendance(studentId, courseId, timestamp)` method that checks existing attendance for the same student‑course‑date and returns a duplicate flag if present.
  * Use parameterized queries via the ORM/Query builder to prevent SQL injection.
  * Apply tenant isolation by filtering records with `tenant_id` from the JWT context.
  * Encrypt any PII fields in logs using AES‑256 per `[NFR-003]`.
  * Log each attendance event to the audit log per `[NFR-006]`.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-012], [REQ-013], [DAT-005], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-006]

#### SUB-TASK 1.2: Implement QRScannerService for Payload Validation and Decoding
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/services/QRScannerService.ts`
* **Architectural Requirements:**
  * Decode base64 QR payload into `studentId` and `courseId`.
  * Validate input against schema (UUID format, required fields) and enforce OWASP input validation to mitigate XSS and injection.
  * Integrate with `AttendanceService` to persist attendance after validation.
  * Handle network retry per `[EXC-001]` by implementing exponential backoff for transient failures.
  * Log QR scan attempts per `[NFR-006]`.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-012], [EXC-001], [EXC-004], [NFR-001], [NFR-003]

#### SUB-TASK 1.3: Generate Technical Documentation for Attendance & QR Services
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/docs/AttendanceAndQRArchitecture.md`
* **Architectural Requirements:**
  * Document API contracts, request/response schemas, error codes, and security considerations.
  * Include sequence diagrams illustrating QR scan → validation → attendance recording flow.
  * Reference OWASP mitigations and tenant isolation controls.
  * Provide data model excerpts for `[DAT-005]` and logging guidelines per `[NFR-006]`.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-012], [REQ-013], [DAT-005], [EXC-001], [EXC-002], [NFR-006]

### DAY 2: Notification Service Implementation & Documentation
#### SUB-TASK 2.1: Implement NotificationService for Push & Zalo Group Delivery
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/services/NotificationService.ts`
* **Architectural Requirements:**
  * Provide `notify(userId, groupZalo?, message, payload)` method that queues a notification record per `[DAT-007]`.
  * Implement push notification dispatch via FCM/APNs and synchronous Zalo HTTP POST.
  * Apply retry logic (up to 3 attempts) for failed deliveries per `[EXC-003]`.
  * Enforce rate limiting and tenant isolation on message sending.
  * Log all notification attempts and failures per `[NFR-006]`.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-016], [DAT-007], [EXC-003], [NFR-001], [NFR-003], [NFR-006]

#### SUB-TASK 2.2: Produce Notification Service Documentation
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/docs/NotificationServiceArchitecture.md`
* **Architectural Requirements:**
  * Detail notification payload schema, delivery channels, and error handling.
  * Include security considerations for token management and message content sanitization.
  * Reference `[DAT-007]` and retry policy per `[EXC-003]`.
  * Provide deployment notes for FCM/APNs credentials and Zalo API integration.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-016], [DAT-007], [EXC-003], [NFR-006]

### DAY 3: Unit Test Coverage for Attendance, QR, and Notification Services
#### SUB-TASK 3.1: Write Unit Tests for AttendanceService
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/services/AttendanceService.ts;./sources/backend/tests/AttendanceService.test.ts`
* **Architectural Requirements:**
  * Test successful attendance creation, duplicate detection, and idempotency.
  * Validate tenant isolation and input sanitization.
  * Simulate network failures and verify logging per `[NFR-006]`.
  * Ensure OWASP compliance (SQL injection prevention checks).
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-012], [REQ-013], [DAT-005], [EXC-001], [EXC-002], [NFR-001], [NFR-003], [NFR-006]

#### SUB-TASK 3.2: Write Unit Tests for QRScannerService
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/services/QRScannerService.ts;./sources/backend/tests/QRScannerService.test.ts`
* **Architectural Requirements:**
  * Validate QR payload decoding, UUID format checks, and error handling for malformed input.
  * Test retry behavior on transient failures per `[EXC-001]`.
  * Verify integration with `AttendanceService` for duplicate scan handling.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-012], [EXC-001], [EXC-004], [NFR-001], [NFR-003]

#### SUB-TASK 3.3: Write Unit Tests for NotificationService
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/services/NotificationService.ts;./sources/backend/tests/NotificationService.test.ts`
* **Architectural Requirements:**
  * Test push notification queuing, successful delivery, and retry logic for failures per `[EXC-003]`.
  * Validate Zalo group message formatting and error handling.
  * Ensure tenant isolation and rate limiting enforcement.
* **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
  * **Targeted Tag IDs:** [REQ-016], [DAT-007], [EXC-003], [NFR-001], [NFR-003], [NFR-006]