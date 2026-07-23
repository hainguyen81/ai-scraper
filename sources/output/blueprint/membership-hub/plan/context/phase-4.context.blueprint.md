# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Integrate Apache Kafka as the core event bus for real‑time communication across services (attendance, notifications, enrollment, etc.).
- Implement a unified Notification Service that can dispatch emails, SMS/Zalo messages, and mobile push notifications based on Kafka events.
- Build and configure Docker images for both backend and frontend services with security‑hardening best practices.
- Provision a Google Kubernetes Engine (GKE) cluster on GCP and deploy the containerized services using Kubernetes manifests (Deployments, Services, ConfigMaps, Ingress).
- Validate end‑to‑end event flow, notification delivery, and cluster health through automated unit, integration, and E2E test suites.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Java Stack** – All source files must reside under `./sources/backend/` and follow the strict package layout `/org/nlh4j/saas/membership-hub/`.
- **Frontend Next.js Stack** – All UI, routing, and client‑side code must reside under `./sources/frontend/`.
- **Configuration & Infrastructure** – YAML/JSON configs, Dockerfiles, GCP/GKE scripts, and Kubernetes manifests are allowed only under `./sources/backend/` or `./sources/frontend/` (e.g., `./sources/backend/Dockerfile`, `./sources/frontend/gcp-provision.sh`).
- **Testing** – Unit tests under `./sources/backend/src/test/java/` and frontend tests under `./sources/frontend/tests/`.
- **REST/GraphQL/Event Endpoints** – New Kafka topic definitions, producer/consumer REST endpoints, and notification HTTP APIs may be introduced under the existing backend service layer.

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, Docker, GCP, GKE)
- **Coder Agent** – Implements Kafka producers/consumers, Event POJOs, Notification Service, and integrates them. Writes all Java service classes, configuration files, and frontend notification UI components.
- **Tester Agent** – Designs and executes unit tests for Kafka producers/consumers and Notification Service. Executes integration/E2E tests that verify event‑to‑notification pipelines and cross‑service workflows using `INTEGRATION_SCOPE`.
- **Reviewer Agent** – Performs static code analysis, validates Java package‑to‑path compliance, checks Docker security best practices, and ensures all generated files adhere to the enterprise standards.
- **Docker Agent** – Crafts multi‑stage, minimal‑footprint Dockerfiles for backend and frontend, includes health‑check probes, and ensures image layering follows security guidelines.
- **GCP Agent** – Automates GKE cluster provisioning, sets up network policies, IAM roles, and storage resources required for the application. All provisioning scripts must be placed under `./sources/backend/`.
- **GKE Agent** – Generates Kubernetes manifests (Deployment, Service, ConfigMap, Ingress) for both backend and frontend, prepares Helm charts if used, and orchestrates the deployment and verification of services on the GKE cluster.

## 4. Phase Definition of Done (DoD)
- Kafka topics `attendance.events`, `notification.events` are defined and functional.
- Producer service (`AttendanceEventProducer`) and consumer service (`EventProcessingService`) are implemented, unit‑tested, and integrated with Notification Service.
- Notification Service supports email, SMS/Zalo, and mobile push; all dependencies are mocked/configurable.
- Docker images for backend and frontend are built, scanned, and pushed to artifact registry.
- GKE cluster is provisioned, IAM and network policies are applied.
- Kubernetes manifests are applied; all pods reach `Ready` state and services are reachable.
- Automated test suite passes: unit tests >90% coverage, integration tests verify event‑to‑notification flow, and E2E tests confirm UI notification display.
- All code, configs, and manifests comply with Java package mapping, path prefix, and security guardrails.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Kafka Infrastructure Setup & Event Models
#### SUB‑TASK 1.1: Define Kafka configuration and topics
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/application.yml
    *   **Architectural Requirements:**
        *   Configure `spring.kafka.bootstrap-servers` to `kafka:9092`.
        *   Define `spring.kafka.producer.properties` and `spring.kafka.consumer.properties` for idempotence and serialization.
        *   Declare topic names `attendance.events` and `notification.events` with replication factor 1 and partition count 3.

#### SUB‑TASK 1.2: Create Event POJOs for domain events
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/model/AttendanceEvent.java
    *   **Architectural Requirements:**
        *   Annotate with `@KafkaSerializable` (custom marker) and include fields `studentId`, `timestamp`, `qrCodeData`, `centerId`.
        *   Implement `toString()` and `equals()` for logging and testing.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/model/NotificationEvent.java
    *   **Architectural Requirements:**
        *   Include fields `eventType` (enum: EMAIL, SMS, PUSH), `recipient`, `payload`, `priority`.
        *   Ensure serializable with Jackson annotations.

#### SUB‑TASK 1.3: Static code review and compliance check
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/model/AttendanceEvent.java
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/model/NotificationEvent.java
    *   **Architectural Requirements:**
        *   Verify package‑to‑path mapping matches `/org/nlh4j/saas/membership-hub/`.
        *   Ensure no unused imports, proper Lombok usage, and adherence to Java 17 coding standards.

### DAY 2: Kafka Producer & Consumer Services
#### SUB‑TASK 2.1: Implement Kafka producer for attendance events
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/AttendanceEventProducer.java
    *   **Architectural Requirements:**
        *   Autowire `KafkaTemplate<String, AttendanceEvent>`.
        *   Provide method `sendAttendanceEvent(AttendanceEvent event)` that logs and sends to `attendance.events`.
        *   Use `@Retryable` for transient failures.

#### SUB‑TASK 2.2: Implement Kafka consumer service to route events
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/EventProcessingService.java
    *   **Architectural Requirements:**
        *   Subscribe to `attendance.events` via `@KafkaListener`.
        *   Transform incoming `AttendanceEvent` into appropriate `NotificationEvent` based on event type.
        *   Emit `NotificationEvent` to `notification.events` using a `KafkaTemplate`.

#### SUB‑TASK 2.3: Unit tests for producer and consumer
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/AttendanceEventProducer.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/AttendanceEventProducerTest.java
    *   **Architectural Requirements:**
        *   Mock `KafkaTemplate` and verify `send` calls.
        *   Test retry logic with simulated exceptions.
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/EventProcessingService.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/EventProcessingServiceTest.java
    *   **Architectural Requirements:**
        *   Verify listener processes events and publishes correct `NotificationEvent`.
        *   Use `@EmbeddedKafka` for isolated testing.

### DAY 3: Notification Service Implementation
#### SUB‑TASK 3.1: Build Notification Service core
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/NotificationService.java
    *   **Architectural Requirements:**
        *   Define methods `sendEmail(NotificationEvent)`, `sendSms(NotificationEvent)`, `sendPush(NotificationEvent)`.
        *   Inject external clients (EmailClient, SmsClient, PushClient) via configuration.
        *   Implement circuit‑breaker pattern for each channel.

#### SUB‑TASK 3.2: Integrate Notification Service with Kafka consumer
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/EventProcessingService.java
    *   **Architectural Requirements:**
        *   After publishing `NotificationEvent`, call `notificationService.dispatch(event)`.
        *   Log successful dispatch and handle channel‑specific failures.

#### SUB‑TASK 3.3: Frontend notification UI component
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/components/NotificationCenter.tsx
    *   **Architectural Requirements:**
        *   Consume real‑time notifications via Server‑Sent Events or WebSocket.
        *   Display list of notifications with timestamps and actionable buttons.
        *   Support multi‑language i18n keys for notification messages.

### DAY 4: Containerization
#### SUB‑TASK 4.1: Create multi‑stage Dockerfile for backend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/Dockerfile
    *   **Architectural Requirements:**
        *   Use `eclipse-temurin:17-jdk-alpine` as base for build stage.
        *   Copy `pom.xml` and source, package with Maven.
        *   Use `distroless/java-debian` as runtime image.
        *   Include health‑check endpoint `/actuator/health`.

#### SUB‑TASK 4.2: Create multi‑stage Dockerfile for frontend
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/Dockerfile
    *   **Architectural Requirements:**
        *   Use `node:20-alpine` for build stage, install dependencies, build Next.js.
        *   Use `nginx:alpine` as runtime, copy built output.
        *   Expose port `3000` and define `nginx -g 'daemon off;'` as entrypoint.

#### SUB‑TASK 4.3: GCP provisioning script
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/gcp-provision.sh
    *   **Architectural Requirements:**
        *   Use `gcloud` SDK to create a GKE cluster named `membership-hub-cluster` with node pool `default-pool`.
        *   Enable necessary APIs (`container.googleapis.com`, `pubsub.googleapis.com`).
        *   Create a service account with `roles/container.admin` and `roles/pubsub.admin`.
        *   Output cluster credentials to `~/.kube/config`.

### DAY 5: Kubernetes Manifests & Integration Tests
#### SUB‑TASK 5.1: Generate Kubernetes Deployment for backend
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/k8s/backend-deployment.yaml
    *   **Architectural Requirements:**
        *   Deploy using image `membership-hub-backend:latest`.
        *   Mount ConfigMap for `application.yml`.
        *   Set resource limits (CPU 500m, memory 1Gi).
        *   Include liveness and readiness probes.

#### SUB‑TASK 5.2: Generate Kubernetes Service for backend
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/k8s/backend-service.yaml
    *   **Architectural Requirements:**
        *   ClusterIP service exposing port 8080.
        *   Selector matching backend deployment.

#### SUB‑TASK 5.3: Generate Kubernetes Ingress for frontend
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/k8s/frontend-ingress.yaml
    *   **Architectural Requirements:**
        *   Ingress with `nginx.ingress.kubernetes.io/rewrite-target: /$2` for SPA routing.
        *   TLS enabled via secret `membership-hub-tls`.
        *   Path prefixes `/api/*` routed to backend service, remaining to frontend.

#### SUB‑TASK 5.4: Integration/E2E test for notification flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/notification.e2e.spec.ts
    *   **Architectural Requirements:**
        *   Simulate QR attendance via API, verify Kafka event is produced.
        *   Validate NotificationEvent is consumed and notification appears in UI.
        *   Assert email/SMS/Push mock calls are triggered.

### DAY 6: Notification Service Unit Tests & Final Review
#### SUB‑TASK 6.1: Unit tests for NotificationService
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/NotificationService.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/NotificationServiceTest.java
    *   **Architectural Requirements:**
        *   Mock external clients and verify correct channel invocation.
        *   Test circuit‑breaker fallback behavior.

#### SUB‑TASK 6.2: Static analysis and compliance review
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/AttendanceEventProducer.java
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/EventProcessingService.java
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/NotificationService.java
*   **Target Path:** ./sources/backend/Dockerfile
*   **Target Path:** ./sources/frontend/Dockerfile
    *   **Architectural Requirements:**
        *   Validate Java package mapping.
        *   Ensure Dockerfile best practices (non‑root user, minimal layers).
        *   Confirm all file paths start with allowed prefixes.

### DAY 7: GKE Deployment & Phase Completion
#### SUB‑TASK 7.1: Apply Kubernetes manifests to GKE cluster
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/k8s/backend-deployment.yaml
*   **Target Path:** ./sources/backend/k8s/backend-service.yaml
*   **Target Path:** ./sources/frontend/k8s/frontend-ingress.yaml
    *   **Architectural Requirements:**
        *   Use `kubectl apply -f` with `--context=gke_membership-hub_us-central1_cluster`.
        *   Wait for pods to reach `Ready` status.
        *   Capture any rollout failures and rollback if needed.

#### SUB‑TASK 7.2: Verify service availability and notification delivery
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/service-health.spec.ts
    *   **Architectural Requirements:**
        *   Perform `curl` to backend `/actuator/health` and frontend `/`.
        *   Validate HTTP status 200 and expected JSON structure.
        *   Trigger a mock attendance event via API and confirm notification appears in UI.

#### SUB‑TASK 7.3: Phase final sign‑off
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/phase4-summary.md
    *   **Architectural Requirements:**
        *   Document completed Kafka topics, producer/consumer services, Notification Service, Docker images, GKE deployments.
        *   Include test results summary and compliance checklist.
        *   Provide artifact references (image tags, cluster endpoint) for downstream phases.