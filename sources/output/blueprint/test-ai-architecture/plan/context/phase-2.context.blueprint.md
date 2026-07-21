# PHASE 2 CONTEXT BLUEPRINT: test-ai-architecture
## 1. Phase Operational Scope & Objectives
| # | Objective | Description |
|---|-----------|-------------|
| **2.1** | **Core Backend Build** | Create a production‑ready Quarkus application that exposes RESTful APIs for user management, authentication (internal email/password + external Firebase/Google/Facebook), and attendance handling. |
| **2.2** | **Event‑Driven Attendance** | Implement Kafka producers/consumers to ingest QR‑scan events, persist attendance records in PostgreSQL, and trigger downstream notifications. |
| **2.3** | **Multi‑Tenancy Support** | Design schema and service layers to isolate data per training centre while sharing the same application runtime. |
| **2.4** | **Security & Compliance** | Apply JWT‑based auth, role‑based access control, GDPR/CCPA‑aligned data handling, and audit logging. |
| **2.5** | **Containerization & Deployment Prep** | Build a Docker image, push to GCP Artifact Registry, and generate Kustomize/Helm manifests for GKE rollout. |
| **2.6** | **Observability** | Add OpenTelemetry metrics, structured logging (Logback), and health‑check endpoints. |

*All work must be completed within the 4‑day window (Days 4‑7). No extra days may be introduced.*

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)

```
src/
  main/
    java/
      com/membership/
        backend/               ← Core Quarkus services
          model/
            User.java
            Center.java
            Attendance.java
          repository/
            UserRepository.java
            CenterRepository.java
            AttendanceRepository.java
          service/
            UserService.java
            AuthService.java
            AttendanceService.java
            NotificationService.java
          resource/
            UserResource.java          ← /api/users/{id}
            AuthResource.java          ← /api/auth/login, /api/auth/register
            CenterResource.java        ← /api/centers
            AttendanceResource.java    ← /api/attendance/scan, /api/attendance/{id}
            HealthResource.java        ← /q/health
          security/
            JwtAuthFilter.java
            KeyGenerator.java
          kafka/
            AttendanceProducer.java
            AttendanceConsumer.java
        config/
          application.properties
    resources/
      META-INF/
        services/
          org.apache.kafka.clients.KafkaProducer
      static/
      public/
  test/
    java/
      com/membership/
        backend/
          ... unit & integration tests
```

**Key REST Endpoints (must be implemented):**
- `POST /api/auth/login` – internal email/password & external OAuth2 token validation.  
- `POST /api/auth/register` – create internal user.  
- `GET /api/users/{id}` – retrieve user profile (center‑scoped).  
- `POST /api/attendance/scan` – accept QR payload, produce Kafka event.  
- `GET /api/attendance/{date}` – list attendance for a centre on a given day.  
- `GET /q/health` – liveness/readiness probes.  

**Kafka Topics (must exist):**
- `attendance-scan` – raw QR events.  
- `attendance-processed` – processed attendance records for downstream notifications.  

**Docker & GKE artefacts (must be generated):**
- `Dockerfile.jvm` / `Dockerfile.native` under `src/main/docker`.  
- `docker-compose.yml` (optional, for local dev).  
- `k8s/` folder with `deployment.yaml`, `service.yaml`, `hpa.yaml`, `configmap.yaml`.  

## 3. Dedicated Sub-Agent Functional Directives

| Sub‑Agent | Specific Tasks (Day‑wise focus) | Deliverables |
|-----------|--------------------------------|--------------|
| **Coder** | **Day 4** – Set up Quarkus project, define JPA entities, create repositories, and write basic `Application.java`. <br>**Day 5** – Implement `AuthService` with JWT generation, integrate Firebase/Google/Facebook OAuth2 clients, and secure endpoints via `JwtAuthFilter`. <br>**Day 6** – Build `AttendanceResource` (QR validation), `AttendanceProducer` (send to `attendance-scan`), and `AttendanceConsumer` (write to PostgreSQL, emit `attendance-processed`). <br>**Day 7** – Add multi‑tenant schema switching (e.g., using `centerId` in repository methods), implement `NotificationService` stub, and write OpenTelemetry metrics. | Fully functional Quarkus services, compiled JAR, Dockerfiles, and a README with build commands. |
| **Tester** | **Day 4** – Write unit tests for JPA entities and repository CRUD. <br>**Day 5** – Create integration tests for `/api/auth/login` (internal & external) using mock OAuth2 providers. <br>**Day 6** – Simulate Kafka flow with embedded Kafka broker; test `AttendanceResource` → producer → consumer → DB. <br>**Day 7** – Execute health‑check endpoint tests, verify security headers, and generate a test coverage report. | Test suite passing ≥ 90 % coverage, JUnit reports, and a test‑summary artifact. |
| **Reviewer** | **Day 4‑5** – Perform code walk‑throughs, enforce Java/Quarkus coding standards, check security best‑practices (e.g., password hashing, token expiration). <br>**Day 6‑7** – Review Kafka message schema, ensure idempotency, and validate multi‑tenant isolation logic. | Signed-off code review checklist, comments resolved, and a compliance badge. |
| **DevOps** | **Day 4** – Build Docker image (`docker build -f src/main/docker/Dockerfile.jvm -t gcr.io/<project>/membership-hub-backend:latest .`). <br>**Day 5** – Push image to GCP Artifact Registry (`gcloud artifacts repositories`). <br>**Day 6** – Generate Kustomize/Helm charts, create `configmap.yaml` with DB credentials (secret manager reference) and Kafka bootstrap servers. <br>**Day 7** – Deploy to GKE using `kubectl apply -k k8s/`, verify pods, and enable Cloud Monitoring/Logging for the service. | Deployed backend pod(s) in GKE, accessible endpoints, and monitoring dashboards linked. |
| **Manager** | Daily stand‑ups, risk log updates, and approval gates for each sub‑agent’s deliverable before moving to the next day. | Phase‑gate sign‑off documentation. |

*All sub‑agents must work in parallel but **must not overlap** on the same file or endpoint. The Coder owns the source code, the Tester owns test artefacts, the Reviewer owns only review comments, and DevOps owns container & deployment artefacts.*

## 4. Phase Definition of Done (DoD)

- **[Backend]** All Quarkus services compile, start, and expose the required REST endpoints with correct HTTP status codes.
- **[Auth]** Internal email/password login, registration, and external OAuth2 flows (Firebase/Google/Facebook) produce valid JWTs and enforce role‑based access.
- **[Kafka]** `attendance-scan` topic receives QR events; `AttendanceConsumer` reliably writes to PostgreSQL; duplicate scans on the same day are idempotent.
- **[Multi‑Tenancy]** Each centre’s data is isolated via `centerId` column; cross‑centre queries return only owned records.
- **[Security]** Passwords hashed with bcrypt, JWT signed/encrypted, audit logs stored, GDPR/CCPA fields (consent flags) persisted.
- **[Observability]** `/q/health` returns UP, OpenTelemetry metrics emitted, structured Logback logs with correlation IDs.
- **[Testing]** All unit & integration tests pass, coverage ≥ 90 %, test reports attached.
- **[Code Review]** Reviewer checklist signed, all comments addressed.
- **[Containerization]** Docker image built, scanned for vulnerabilities, pushed to GCP Artifact Registry.
- **[Deployment]** GKE deployment creates running pods, service exposes backend, HPA configured, monitoring dashboards active.
- **[Documentation]** README with build, run, and deploy instructions, plus API spec (OpenAPI YAML) committed.

When **all** DoD items are satisfied, the Phase 2 work is complete and the hand‑off to Phase 3 can commence. No further timeline extensions are permitted.