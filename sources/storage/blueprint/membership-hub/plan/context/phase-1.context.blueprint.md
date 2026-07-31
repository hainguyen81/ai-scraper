# PHASE  CONTEXT BLUEPRINT: membership-hub

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-20260731151028 |
| **Project Name** | membership-hub |
| **Version** | 1.0 (Baseline) |
| **Date/Time** | 2026/07/31 15:10:28 |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
Phase 5 focuses on delivering the AI‑powered customer service chatbot and the mobile‑app core features that enable role‑specific UI rendering and push‑notification delivery. The objectives are:
- Integrate an AI chatbot service that processes user queries, returns context‑aware answers, and escalates low‑confidence requests to human support.
- Provide a backend service that supplies role‑specific UI metadata to the mobile app, ensuring navigation and screen availability match the authenticated user’s role.
- Implement a push‑notification subsystem that queues, delivers, and logs notifications to mobile devices via Firebase Cloud Messaging (FCM) and APNs, and posts messages to designated Zalo groups.
- Enforce OWASP security controls, performance SLAs, logging, audit, and compliance with GDPR/CCPA throughout all new components.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Directory | Purpose | Key Files | REST/GraphQL/Event Endpoints |
| :--- | :--- | :--- | :--- |
| `./sources/backend/aichatbot` | AI chatbot service | `AIChatbotService.java`, `AIChatbotController.java` | `POST /api/chatbot/query` |
| `./sources/backend/mobileapp` | Mobile role‑specific UI service | `MobileRoleSpecificUIService.java`, `MobileRoleSpecificUIController.java` | `GET /api/mobile/ui/metadata` |
| `./sources/backend/notifications` | Push‑notification service | `PushNotificationService.java`, `PushNotificationController.java` | `POST /api/notifications/push` |
| `./sources/backend` | Docker build context | `Dockerfile` | N/A |
| `./sources/deployment/k8s` | Kubernetes manifests | `backend-deployment.yaml`, `backend-service.yaml` | N/A |
| Kafka Topics | `chatbot.responses`, `notifications.push` | N/A | Event‑driven routing |

All paths strictly begin with `./sources/` and adhere to the Java package `org.nlh4j.saas.membershiphub`.

## 3. Dedicated Sub-Agent Functional Directives
| Sub-Agent | Responsibilities |
| :--- | :--- |
| **coder** | Implement Java services, controllers, and integration logic; adhere to coding standards, OWASP guidelines, and performance targets. |
| **tester** | Write unit and integration tests; validate functional correctness, exception flows, and security constraints. |
| **reviewer** | Perform static code analysis, review OWASP compliance, and ensure adherence to architectural patterns. |
| **doc** | Produce README and API documentation for each module; maintain traceability of requirements. |
| **docker** | Create Dockerfile, build images, and push to registry; enforce image size limits. |
| **GCP** | Generate GKE deployment manifests, configure autoscaling, and ensure high‑availability settings. |

## 4. Phase Definition of Done (DoD)
- All tagged requirements `[REQ-019]`, `[REQ-020]`, `[REQ-021]` fully implemented with 100 % unit test coverage.
- OWASP Top 10 mitigations (SQLi, XSS, CSRF, etc.) verified via static analysis and runtime checks.
- Performance: API latency < 200 ms average; database queries indexed for sub‑second reads under 10 k concurrent users.
- Logging & audit: All critical actions logged with user ID, timestamp, and action details; logs retained for 1 year.
- Security: TLS 1.3 enforced; JWT tokens with 15 min expiry; refresh tokens 7 days; data at rest AES‑256.
- Compliance: GDPR/CCPA data deletion/export flows, consent management, and backup/DR policies in place.
- Docker image size < 500 MB; base image < 200 MB.
- Deployment: GKE HPA configured, 99.9 % uptime SLA, daily PostgreSQL backups, point‑in‑time recovery.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: AI CHATBOT INTEGRATION

#### SUB-TASK 1.1: Implement AIChatbotService
##### Assigned Sub-Agent: coder
##### Target Path: `./sources/backend/aichatbot/AIChatbotService.java`
* Traceability Tag Tokens: [REQ-019], [DAT-011], [EXC-004], [ARC-009], [ARC-006], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [NFR-009]
* Architectural Requirements:
  * Use Spring Boot with dependency injection; service annotated with `@Service`.
  * Leverage OpenAI API (or equivalent) via a secure HTTP client; credentials stored in `application.yml` encrypted.
  * Input validation: non‑empty query, length < 1024; reject malformed JSON.
  * Exception handling: map `ExternalServiceException` to HTTP 502; `InvalidInputException` to 400.
  * Logging: SLF4J with MDC for request ID; audit log entry on each response.

#### SUB-TASK 1.2: Implement AIChatbotController
##### Assigned Sub-Agent: coder
##### Target Path: `./sources/backend/aichatbot/AIChatbotController.java`
* Traceability Tag Tokens: [REQ-019], [DAT-011], [EXC-004], [ARC-009], [ARC-006], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [NFR-009]
* Architectural Requirements:
  * REST endpoint `POST /api/chatbot/query`; consumes `application/json`.
  * JWT authentication via `@PreAuthorize`; role check optional.
  * Request DTO validated with Hibernate Validator; errors returned as `400 Bad Request`.
  * Response DTO includes `answer`, `confidence`, `escalate` flag.
  * Publish response to Kafka topic `chatbot.responses` for downstream analytics.

#### SUB-TASK 1.3: Unit Tests for AIChatbotService
##### Assigned Sub-Agent: tester
##### Target Path: `./sources/backend/aichatbot/AIChatbotServiceTest.java`
* Traceability Tag Tokens: [REQ-019], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
* Architectural Requirements:
  * Mock external AI client with `Mockito`; test success, low confidence, and exception scenarios.
  * Verify input validation triggers `InvalidInputException`.
  * Assert audit log entries are created.

#### SUB-TASK 1.4: Review AIChatbotService
##### Assigned Sub-Agent: reviewer
##### Target Path: `./sources/backend/aichatbot/AIChatbotService.java`
* Traceability Tag Tokens: [REQ-019], [EXC-004], [NFR-001], [NFR-003], [NFR-006]
* Architectural Requirements:
  * Static analysis with SpotBugs and OWASP Dependency Check; no high‑severity findings.
  * Verify use of prepared statements for any DB interactions (none in this service).
  * Confirm exception handling aligns with API contract.

#### SUB-TASK 1.5: Documentation for AI Chatbot Module
##### Assigned Sub-Agent: doc
##### Target Path: `./sources/backend/aichatbot/README.md`
* Traceability Tag Tokens: [REQ-019], [DAT-011]
* Architectural Requirements:
  * Include endpoint spec, request/response examples, error codes, and deployment notes.
  * Reference GDPR data handling for user queries.

---

### DAY 2: MOBILE ROLE‑SPECIFIC UI SERVICE

#### SUB-TASK 2.1: Implement MobileRoleSpecificUIService
##### Assigned Sub-Agent: coder
##### Target Path: `./sources/backend/mobileapp/MobileRoleSpecificUIService.java`
* Traceability Tag Tokens: [REQ-020], [ARC-009], [ARC-006], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [NFR-009]
* Architectural Requirements:
  * Service returns a JSON map of role → list of available screens.
  * Data sourced from `roles` table and `role_screen_mapping` (pre‑populated).
  * Cache results in Redis with TTL 5 min to meet latency SLA.
  * Validate role ID against `Roles` table; throw `InvalidRoleException` if not found.

#### SUB-TASK 2.2: Implement MobileRoleSpecificUIController
##### Assigned Sub-Agent: coder
##### Target Path: `./sources/backend/mobileapp/MobileRoleSpecificUIController.java`
* Traceability Tag Tokens: [REQ-020], [ARC-009], [ARC-006], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [NFR-009]
* Architectural Requirements:
  * REST endpoint `GET /api/mobile/ui/metadata`; requires JWT auth.
  * Return HTTP 200 with JSON payload; 404 if role not found.
  * Log request and response with correlation ID.

#### SUB-TASK 2.3: Unit Tests for MobileRoleSpecificUIService
##### Assigned Sub-Agent: tester
##### Target Path: `./sources/backend/mobileapp/MobileRoleSpecificUIServiceTest.java`
* Traceability Tag Tokens: [REQ-020], [NFR-001], [NFR-003], [NFR-006]
* Architectural Requirements:
  * Mock repository to return sample role data; test cache hit/miss.
  * Verify exception thrown for invalid role.

#### SUB-TASK 2.4: Review MobileRoleSpecificUIService
##### Assigned Sub-Agent: reviewer
##### Target Path: `./sources/backend/mobileapp/MobileRoleSpecificUIService.java`
* Traceability Tag Tokens: [REQ-020], [NFR-001], [NFR-003], [NFR-006]
* Architectural Requirements:
  * Ensure no hard‑coded role names; use enum `UserRole`.
  * Verify thread‑safety of cache access.

#### SUB-TASK 2.5: Documentation for Mobile UI Module
##### Assigned Sub-Agent: doc
##### Target Path: `./sources/backend/mobileapp/README.md`
* Traceability Tag Tokens: [REQ-020]
* Architectural Requirements:
  * Detail API contract, role mapping schema, and caching strategy.

---

### DAY 3: PUSH‑NOTIFICATION SUBSYSTEM

#### SUB-TASK 3.1: Implement PushNotificationService
##### Assigned Sub-Agent: coder
##### Target Path: `./sources/backend/notifications/PushNotificationService.java`
* Traceability Tag Tokens: [REQ-021], [DAT-007], [ARC-008], [ARC-009], [ARC-006], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [NFR-009]
* Architectural Requirements:
  * Use Firebase Admin SDK for FCM; APNs via `pushy` library.
  * Persist notification record in `notifications` table; status flags `sent`, `failed`.
  * Retry logic: exponential back‑off up to 3 attempts; log each attempt.
  * Publish to Kafka topic `notifications.push` for analytics.

#### SUB-TASK 3.2: Implement PushNotificationController
##### Assigned Sub-Agent: coder
##### Target Path: `./sources/backend/notifications/PushNotificationController.java`
* Traceability Tag Tokens: [REQ-021], [DAT-007], [ARC-008], [ARC-009], [ARC-006], [NFR-001], [NFR-003], [NFR-004], [NFR-005], [NFR-006], [NFR-008], [NFR-009]
* Architectural Requirements:
  * REST endpoint `POST /api/notifications/push`; consumes JSON with `userId`, `message`, `platform`.
  * Validate `platform` enum; reject unsupported values.
  * Return 202 Accepted; actual delivery handled asynchronously.

#### SUB-TASK 3.3: Unit Tests for PushNotificationService
##### Assigned Sub-Agent: tester
##### Target Path: `./sources/backend/notifications/PushNotificationServiceTest.java`
* Traceability Tag Tokens: [REQ-021], [DAT-007], [ARC-008], [NFR-001], [NFR-003], [NFR-006]
* Architectural Requirements:
  * Mock FCM/APNs clients; test success, failure, retry path.
  * Verify database record creation and status updates.

#### SUB-TASK 3.4: Review PushNotificationService
##### Assigned Sub-Agent: reviewer
##### Target Path: `./sources/backend/notifications/PushNotificationService.java`
* Traceability Tag Tokens: [REQ-021], [DAT-007], [ARC-008], [NFR-001], [NFR-003], [NFR-006]
* Architectural Requirements:
  * Static analysis for null‑pointer safety; OWASP CSRF mitigated via `@CrossOrigin` restrictions.
  * Confirm retry schedule complies with NFR‑004 scaling.

#### SUB-TASK 3.5: Documentation for Notifications Module
##### Assigned Sub-Agent: doc
##### Target Path: `./sources/backend/notifications/README.md`
* Traceability Tag Tokens: [REQ-021], [DAT-007]
* Architectural Requirements:
  * Include API spec, retry policy, and failure handling guidelines.

#### SUB-TASK 3.6: Dockerfile for Backend Services
##### Assigned Sub-Agent: docker
##### Target Path: `./sources/backend/Dockerfile`
* Traceability Tag Tokens: [NFR-005], [ARC-009], [ARC-006]
* Architectural Requirements:
  * Multi‑stage build: base `openjdk:17-jdk-slim`; compile with Maven; copy JAR to `app.jar`.
  * Set `ENTRYPOINT ["java","-jar","/app.jar"]`.
  * Expose port 8080; health‑check `/actuator/health`.
  * Ensure final image < 500 MB.

#### SUB-TASK 3.7: GKE Deployment Manifest
##### Assigned Sub-Agent: GCP
##### Target Path: `./sources/deployment/k8s/backend-deployment.yaml`
* Traceability Tag Tokens: [ARC-009], [ARC-006], [NFR-004], [NFR-002]
* Architectural Requirements:
  * Deployment with 3 replicas; HPA based on CPU > 70 % or latency > 300 ms.
  * Service type `ClusterIP`; expose port 8080.
  * ConfigMap for `application.yml`; Secret for FCM credentials.
  * Enable `readinessProbe` and `livenessProbe` with 30 s intervals.

---