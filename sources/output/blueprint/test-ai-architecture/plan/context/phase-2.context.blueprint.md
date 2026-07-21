# PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
- **Backend Service Foundation** – Build a production‑ready Quarkus application that exposes the core domain APIs for the membership‑hub platform.  
- **Event‑Driven Architecture** – Implement Kafka producers/consumers to capture attendance events, authentication events, and notification triggers, ensuring idempotent processing and replay safety.  
- **Data Layer** – Design and migrate a PostgreSQL schema that supports multi‑center isolation, member validity tracking, and audit logging.  
- **Authentication & Authorization** – Deliver internal email/password login, and external OAuth2/OpenID Connect integrations with Firebase, Google, and Facebook (using Quarkus Keycloak or Spring‑Security‑OAuth2).  
- **Attendance & Validity** – Create a QR‑scan endpoint that records daily attendance, enforces “one‑scan‑per‑day” semantics, and calculates remaining validity days for each member.  
- **Notification Hub** – Build a notification service capable of sending Zalo SMS, group‑chat messages, and mobile push notifications (via Firebase Cloud Messaging) based on attendance events.  
- **Containerization & Cloud Prep** – Produce a Docker image (native or JVM) and prepare Kubernetes manifests (Deployments, Services, ConfigMaps, Secrets) for deployment on GCP’s GKE cluster.  
- **Observability** – Add structured logging, health‑checks, and metrics endpoints to satisfy the monitoring guardrail.  

*Duration*: Days 4 – 7 (maximum 7 days total).  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Layer | Directory / File | Purpose |
|-------|------------------|---------|
| **Java Sources** | `src/main/java/com/membershiphub/backend/` | Core business services, repositories, security filters, Kafka producers/consumers. |
| **Configuration** | `src/main/resources/application.yml` | Quarkus config, datasource, Kafka bootstrap servers, JWT settings. |
| **Persistence** | `src/main/java/com/membershiphub/backend/repository/` | Spring Data JPA repositories for `Center`, `Member`, `Attendance`, `Validity`, `Notification`. |
| **Kafka** | `src/main/java/com/membershiphub/backend/kafka/` | Producers (`AttendanceEventProducer`, `NotificationEventProducer`) and consumers (`AttendanceEventConsumer`, `AuthEventConsumer`). |
| **Authentication** | `src/main/java/com/membershiphub/backend/security/` | JWT filter, OAuth2 configuration for Firebase/Google/Facebook providers, password hashing. |
| **REST Resources** | `src/main/java/com/membershiphub/backend/resource/` | OpenAPI‑annotated endpoints (see below). |
| **Docker** | `src/main/docker/Dockerfile.jvm` (or `Dockerfile.native`) | Multi‑stage build for container image. |
| **Tests** | `src/test/java/` (unit) <br> `src/it/java/` (integration) | JUnit/Mockito tests for services, contract tests for Kafka, security tests for auth. |
| **Kubernetes** | `k8s/` (e.g., `deployment.yaml`, `service.yaml`, `configmap.yaml`, `secret.yaml`) | Manifests for GKE deployment. |
| **CI/CD** | `.github/workflows/ci.yml` | Build, test, Docker push to Artifact Registry (optional but recommended). |

### Core REST Endpoints (must be implemented)
- `POST /api/auth/register` – internal user registration.  
- `POST /api/auth/login` – internal credential login, returns JWT.  
- `POST /api/auth/social/{provider}` – OAuth2 callback for Firebase/Google/Facebook, returns JWT.  
- `GET /api/centers` – list all centers (multi‑center support).  
- `POST /api/centers` – create a new center.  
- `GET /api/centers/{centerId}/members` – list members of a specific center.  
- `POST /api/attendance/qr` – QR scan attendance (expects `memberId` and `centerId`).  
- `GET /api/members/{memberId}/validity` – returns remaining validity days.  
- `POST /api/notifications` – trigger notification (Zalo SMS, group chat, push).  
- `GET /api/health` – liveness/readiness probes.  

### Kafka Topics (must be defined)
- `attendance.events` – payload: `{memberId, centerId, timestamp, scanned}`.  
- `auth.events` – payload: `{userId, action, timestamp}`.  
- `notification.events` – payload: `{memberId, type, payload}`.  

### Docker & GKE Boundaries
- Docker image tag: `gcr.io/<project-id>/membership-hub-backend:<version>`.  
- Kubernetes resources placed under `k8s/` with appropriate resource limits/requests.  

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
| Sub‑Agent | Concrete Tasks (Day‑wise focus) |
|-----------|--------------------------------|
| **Coder** | 1. Implement `MemberService` with CRUD + validity calculation logic.<br>2. Implement `AttendanceService` that writes to PostgreSQL **and** emits `attendance.events` to Kafka.<br>3. Add `NotificationService` that consumes `notification.events` and sends Zalo SMS, group chat, and FCM push.<br>4. Code OAuth2 configuration for each external provider (Firebase, Google, Facebook) using Quarkus OIDC.<br>5. Create REST resources (`AttendanceResource`, `MemberResource`, `AuthResource`) with OpenAPI annotations.<br>6. Add JWT authentication filter and role‑based access control (admin vs member).<br>7. Write a simple health‑check endpoint (`/api/health`). |
| **Tester** | 1. Unit‑test service methods (validity calculation, duplicate‑scan guard).<br>2. Integration‑test REST endpoints using `@QuarkusTest` (including security filters).<br>3. Contract‑test Kafka producers/consumers with embedded Kafka.<br>4. Write security tests for internal and social login flows.<br>5. Performance‑test attendance endpoint under load (optional). |
| **Reviewer** | 1. Verify OWASP Top‑10 compliance (SQL injection, XSS, insecure deserialization).<br>2. Check Kafka idempotency and exactly‑once semantics.<br>3. Validate Docker image size and use of multi‑stage builds.<br>4. Ensure GDPR/CCPA data‑handling (data retention, consent fields).<br>5. Review code style, naming conventions, and documentation (OpenAPI). |
| **DevOps** | 1. Create a multi‑stage Docker build (`Dockerfile.jvm` or `Dockerfile.native`).<br>2. Push image to GCP Artifact Registry.<br>3. Generate Kubernetes manifests (`deployment.yaml`, `service.yaml`, `configmap.yaml`, `secret.yaml`) with resource limits and HPA.<br>4. Set up a GKE cluster (if not existing) and apply manifests.<br>5. Configure Kafka and PostgreSQL as Kubernetes Services/Clusters (using GCP managed services).<br>6. Add monitoring stubs: Prometheus metrics endpoint, structured JSON logs, and a simple Grafana dashboard. |
| **Manager** (oversight) | 1. Track progress against Day 4‑7 milestones.<br>2. Ensure all sub‑agent deliverables are signed off before Phase 2 close.<br>3. Update Phase 2 status in the project board. |

*All sub‑agents must work in parallel but on **non‑overlapping** code areas to avoid conflicts (e.g., Coder writes business logic, Tester writes tests for that logic, Reviewer audits the combined code, DevOps builds and deploys the artifact).*

## 4. Phase Definition of Done (DoD)
- **Code & Build**  
  - All Quarkus services compile and run locally in dev mode.  
  - Docker image built, tagged, and pushed to GCP Artifact Registry.  
  - OpenAPI specification generated and accessible (`/openapi.yaml`).  

- **Data & Persistence**  
  - PostgreSQL schema migrated (centers, members, attendance, validity, notifications).  
  - Multi‑center data isolation verified (no cross‑center leakage).  

- **Event Streaming**  
  - Kafka topics (`attendance.events`, `auth.events`, `notification.events`) created in the GCP Kafka cluster.  
  - Producers emit events for attendance and notifications; consumers process them without duplication.  

- **Authentication**  
  - Internal email/password registration/login functional with secure password hashing.  
  - External OAuth2 flows for Firebase, Google, and Facebook fully functional and return valid JWTs.  

- **Attendance & Validity**  
  - QR scan endpoint (`POST /api/attendance/qr`) records attendance, enforces one‑scan‑per‑day per member, and updates validity days.  
  - Validity calculation logic correctly subtracts days based on attendance and expiration rules.  

- **Notifications**  
  - Notification service can send Zalo SMS, group‑chat messages, and mobile push (FCM) based on attendance events.  
  - All three channels tested with mock payloads.  

- **Security & Compliance**  
  - JWT tokens secured with RSA256, refresh mechanisms, and proper expiration.  
  - GDPR/CCPA considerations addressed (data‑deletion endpoints, consent flags).  

- **Testing**  
  - Unit test coverage ≥ 80 % for core service classes.  
  - Integration tests pass for all REST endpoints and Kafka contracts.  
  - Security tests confirm authentication/authorization rules.  

- **DevOps & Deployment**  
  - Kubernetes manifests ready and applied to GKE.  
  - Services expose correct ports, have proper HPA configurations.  
  - Health‑check endpoints (`/api/health`) respond with 200.  

- **Observability**  
  - Structured JSON logs emitted for all business events.  
  - Prometheus metrics endpoint (`/metrics`) includes request counts, error rates, and Kafka lag.  

- **Documentation & Sign‑off**  
  - Phase 2 deliverables documented in the project wiki.  
  - All sub‑agents have signed off on their respective work.  

When **all** the above criteria are satisfied, Phase 2 is complete and the project proceeds to Phase 3.