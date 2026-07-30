# PHASE 4 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
Phase 4 focuses on integrating Firebase Cloud Messaging (FCM) for push notifications and deploying the application to Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). This phase ensures that the system can reliably deliver real-time notifications to mobile users and is deployed in a scalable, production-ready environment. The integration must support multi-tenancy and adhere to security standards, including encrypted payloads and proper tenant isolation in notification routing. Deployment must include containerization, ingress configuration, and environment-specific variables for GKE.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Notification Service:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java`
- **Firebase Configuration:** `./sources/backend/src/main/resources/firebase-service-account.json`
- **GKE Deployment Manifests:** `./sources/infra/gke/deployment.yaml`, `./sources/infra/gke/service.yaml`, `./sources/infra/gke/ingress.yaml`
- **Docker Configuration:** `./sources/backend/Dockerfile`, `./sources/frontend/Dockerfile`
- **Environment Configuration:** `./sources/backend/src/main/resources/application-prod.properties`
- **API Endpoints:** `/api/notifications/send` (POST for sending notifications), `/api/notifications/register` (POST for device token registration)

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for coder, tester, reviewer, doc, docker, GCP, GKE)
- **docker:** Responsible for creating and optimizing Dockerfiles for backend and frontend, ensuring image size compliance (<500 MB) and multi-stage builds.
- **GKE:** Handles GKE-specific deployment manifests, including Kubernetes deployments, services, ingress rules, and environment variable injection for production.
- **coder:** Implements Firebase integration logic, including notification sending and device token registration, with multi-tenant support and error handling.
- **doc:** Creates deployment guides and notification flow documentation under `./sources/docs/`.
- **reviewer:** Performs static analysis on individual code files for security compliance, focusing on OWASP Top 10 issues like injection and data exposure.
- **tester:** Writes and executes integration tests for notification services and deployment configurations.

## 4. Phase Definition of Done (DoD)
- Firebase integration is complete, with push notifications successfully sent to registered devices via FCM.
- Backend and frontend are containerized with Docker images under 500 MB.
- Application is deployed to GKE with functional ingress, services, and environment-specific configurations.
- All notification-related code passes OWASP security checks and includes multi-tenancy validation.
- Documentation for deployment and notification flows is created and stored in `./sources/docs/`.
- Integration tests verify notification delivery and deployment stability.

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: FIREBASE INTEGRATION SETUP AND NOTIFICATION SERVICE IMPLEMENTATION
#### SUB-TASK 1.1: Implement Firebase notification service with multi-tenant support
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java`
    *   **Architectural Requirements:**
        *   Use Firebase Admin SDK to send push notifications with encrypted payloads.
        *   Implement tenant isolation by including `tenant_id` in notification metadata.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-009], [REQ-016], [REQ-021], [NFR-003]

#### SUB-TASK 1.2: Create Firebase service account configuration
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/resources/firebase-service-account.json`
    *   **Architectural Requirements:**
        *   Store service account JSON with restricted permissions and encrypt sensitive fields.
        *   Ensure the file is excluded from version control via `.gitignore`.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-009], [NFR-003]

### DAY 2: DOCKERIZATION AND IMAGE OPTIMIZATION
#### SUB-TASK 2.1: Create optimized Dockerfile for backend
##### Assigned Sub-Agent: docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/Dockerfile`
    *   **Architectural Requirements:**
        *   Use multi-stage build to reduce image size below 500 MB.
        *   Include only necessary dependencies and set non-root user for security.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [NFR-005]

#### SUB-TASK 2.2: Create optimized Dockerfile for frontend
##### Assigned Sub-Agent: docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/frontend/Dockerfile`
    *   **Architectural Requirements:**
        *   Use lightweight Node.js base image and optimize static asset delivery.
        *   Ensure environment variables for API endpoints are configurable at runtime.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [NFR-005]

### DAY 3: GKE DEPLOYMENT CONFIGURATION
#### SUB-TASK 3.1: Create Kubernetes deployment manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/infra/gke/deployment.yaml`
    *   **Architectural Requirements:**
        *   Define resource limits, liveness probes, and environment variables for backend and frontend.
        *   Include `tenant_id` as a configurable environment variable for multi-tenancy.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [ARC-005]

#### SUB-TASK 3.2: Create Kubernetes service and ingress manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/infra/gke/service.yaml`
    *   **Architectural Requirements:**
        *   Configure internal services for backend and frontend with proper port mappings.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [ARC-005]
*   **Target Path:** `./sources/infra/gke/ingress.yaml`
    *   **Architectural Requirements:**
        *   Set up HTTPS ingress with TLS termination and path-based routing for APIs and frontend.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [ARC-005]

### DAY 4: ENVIRONMENT CONFIGURATION AND SECURITY REVIEW
#### SUB-TASK 4.1: Create production environment configuration
##### Assigned Sub-Agent: coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/resources/application-prod.properties`
    *   **Architectural Requirements:**
        *   Define production database URLs, Firebase settings, and encryption keys.
        *   Ensure all sensitive values are placeholderized for Kubernetes secret injection.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [NFR-006]

#### SUB-TASK 4.2: Perform security review on notification service
##### Assigned Sub-Agent: reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/NotificationService.java`
    *   **Architectural Requirements:**
        *   Validate input sanitization to prevent injection attacks in notification payloads.
        *   Ensure JWT tokens are validated for tenant scope in notification requests.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [OWASP A01]

### DAY 5: INTEGRATION TESTING AND DOCUMENTATION
#### SUB-TASK 5.1: Write integration tests for notification service
##### Assigned Sub-Agent: tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;`./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/NotificationServiceIT.java`
    *   **Architectural Requirements:**
        *   Test notification delivery with mocked Firebase responses and verify tenant isolation.
        *   Cover edge cases like invalid device tokens and network failures.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [REQ-009], [EXC-003]

#### SUB-TASK 5.2: Create deployment and notification flow documentation
##### Assigned Sub-Agent: doc
##### Targeted Components & Technical Requirements:
*   **Target Path:** `./sources/docs/gke-deployment-guide.md`
    *   **Architectural Requirements:**
        *   Detail steps for building Docker images, deploying to GKE, and configuring ingress.
        *   Include diagrams for notification flow using PlantUML or similar.
    *   **DAILY LOGS TRACEABILITY RULES (ZERO TOLERANCE FOR BUNDLING):**
        *   **Targeted Tag IDs:** [NFR-003], [ARC-008]