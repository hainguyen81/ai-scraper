# PHASE 1 CONTEXT BLUEPRINT: membership-hub

## 1. Phase Operational Scope & Objectives
- Establish the foundational project structure for the membership-hub application.
- Initialize a Quarkus backend with Java 17, configure PostgreSQL datasource, Kafka event streaming, and basic security (email/password, OAuth via Firebase/Google/Facebook).
- Design and create the initial relational schema covering core entities: Center, User (with Role enum), Course, Teacher, Student, Enrollment, Attendance (QR-based), Notification, Promotion, and related audit fields.
- Scaffold a minimal Next.js frontend with multi‑language support, responsive layout, and basic authentication UI.
- Produce Docker containerization artifacts and GCP/GKE infrastructure manifests for future deployment.
- Implement unit tests for core domain services and a health‑check endpoint.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Backend Java sources:** `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/`
- **Backend test sources:** `./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/`
- **Backend resources (config, migrations):** `./sources/backend/src/main/resources/`
- **Backend Docker file:** `./sources/backend/src/main/docker/`
- **Frontend sources:** `./sources/frontend/src/`
- **Frontend tests:** `./sources/frontend/tests/`
- **Project root configuration:** `./sources/backend/pom.xml` (Maven) or `./sources/backend/gradle.xml` (Gradle)
- **Environment placeholders:** `./sources/backend/src/main/resources/application.properties`
- **Database migration scripts (Flyway/Liquibase):** `./sources/backend/src/main/resources/db/migration/`
- **Kafka topic definitions:** `./sources/backend/src/main/resources/kafka-topics.txt`
- **GCP provisioning scripts:** `./sources/backend/src/main/docker/gcp-provision.sh`
- **GKE deployment manifests:** `./sources/backend/src/main/docker/k8s/`

## 3. Dedicated Sub-Agent Functional Directives
- **Coder Agent:** Implement all Java domain models, repositories, services, and REST resources; create Next.js project scaffolding, language detection middleware, and basic UI components.
- **Tester Agent:** Write JUnit unit tests for domain services and integration tests for Kafka/REST flows; use Playwright/E2E tests for critical user journeys.
- **Reviewer Agent:** Perform static code analysis, enforce package‑to‑path mapping, and validate compliance with SonarQube/SpotBugs rules.
- **Docker Agent:** Produce a multi‑stage Dockerfile for the Quarkus JVM image and a sidecar container for Kafka UI.
- **GCP Agent:** Generate Terraform/Deployment Manager snippets for Cloud SQL, Secret Manager, and IAM roles; create a service account JSON placeholder.
- **GKE Agent:** Draft Kubernetes Deployment, Service, Ingress, and ConfigMap manifests for Quarkus, Kafka, and PostgreSQL; define a basic Helm chart structure.

## 4. Phase Definition of Done (DoD)
- Project root contains a functional Quarkus Maven/Gradle build with all required plugins (Hibernate ORM, Kafka, OpenTelemetry).
- Initial Flyway migration scripts create tables for Center, User, Role, Course, Teacher, Student, Enrollment, Attendance, Notification, Promotion with proper constraints and indexes.
- Core REST resources (e.g., `/api/centers`, `/api/courses`, `/api/attendance/qr`) are implemented with OpenAPI specs.
- Basic Next.js project with i18n routing, locale detection, and placeholder pages for login, dashboard, and course list.
- Dockerfile and GCP/GKE manifest files are syntactically correct and placed under the designated directories.
- Unit test coverage ≥ 80 % for domain services; all tests pass locally.
- Health‑check endpoint (`/q/health`) returns UP status.
- All Java source files strictly follow `/org/nlh4j/saas/membership-hub/` package layout.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: PROJECT ROOT INITIALIZATION & CORE BACKEND SKELETON
#### SUB‑TASK 1.1: Create Quarkus project skeleton and Maven configuration
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/pom.xml
    *   **Architectural Requirements:**
        *   Define Maven coordinates matching `org.nlh4j.saas.membership-hub`.
        *   Include Quarkus platform version 3.10+, Hibernate ORM, Kafka, JDBC PostgreSQL extensions.
        *   Configure Java compiler source/target as 17.
        *   Add plugins for Quarkus dev mode, Docker build, and Maven shade.

#### SUB‑TASK 1.2: Establish application properties and package layout
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/application.properties
    *   **Architectural Requirements:**
        *   Define datasource URL, username, password placeholders for PostgreSQL.
        *   Configure Kafka bootstrap servers and default topics.
        *   Set Quarkus profile to `dev` for local testing.
        *   Enable OpenAPI generation (`quarkus.swagger-ui`).

#### SUB‑TASK 1.3: Define JPA entity base package and core model interfaces
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/domain/model/
    *   **Architectural Requirements:**
        *   Create abstract `BaseEntity` with `id`, `createdAt`, `updatedAt`.
        *   Define `Center`, `Role`, `User`, `Course`, `Teacher`, `Student`, `Enrollment`, `Attendance`, `Notification`, `Promotion` entities.
        *   Use appropriate JPA annotations (`@Entity`, `@Table`, `@ManyToOne`, `@OneToMany`, `@Enumerated(EnumType.STRING)`).
        *   Ensure all classes reside under the exact package path `/org/nlh4j/saas/membership-hub/domain/model/`.

#### SUB‑TASK 1.4: Create repository interfaces extending Panache
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/repository/
    *   **Architectural Requirements:**
        *   Implement `CenterRepository extends PanacheRepository<Center>`.
        *   Add custom queries for common operations (e.g., find by taxId).
        *   Ensure repository names map to the domain model package.

#### SUB‑TASK 1.5: Write unit tests for the base entity and repository
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/domain/model/BaseEntity.java;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/domain/model/BaseEntityTest.java
    *   **Architectural Requirements:**
        *   Verify JPA persistence using an in‑memory H2 datasource for unit testing.
        *   Assert CRUD operations and audit field population.

#### SUB‑TASK 1.6: Perform static code review and compliance check
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/
    *   **Architectural Requirements:**
        *   Validate that every `.java` file follows the strict package‑to‑path mapping.
        *   Run SpotBugs and SonarQube rules; flag any violations.

#### SUB‑TASK 1.7: Generate Dockerfile for Quarkus JVM image
##### Assigned Sub-Agent: Docker
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/docker/Dockerfile.jvm
    *   **Architectural Requirements:**
        *   Use multi‑stage build with `maven:3.9.6-eclipse-temurin-17` for compile stage.
        *   Copy target application JAR into a slim `openjdk:17-jdk-slim` runtime stage.
        *   Set JVM options for optimal memory usage (`-Xms256m -Xmx512m`).
        *   Expose port 8080 and define entrypoint.

### DAY 2: DATABASE SCHEMA & KAFKA EVENT STREAMING SETUP
#### SUB‑TASK 2.1: Create Flyway migration scripts for initial schema
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/db/migration/V1__initial_schema.sql
    *   **Architectural Requirements:**
        *   Create tables: `centers`, `roles`, `users`, `courses`, `teachers`, `students`, `enrollments`, `attendance`, `notifications`, `promotions`.
        *   Define primary keys, foreign key constraints, indexes, and NOT NULL constraints.
        *   Insert seed data for `roles` (SystemAdmin, Admin, Manager, Teacher, Student).

#### SUB‑TASK 2.2: Configure Kafka topics and producer/consumer configuration
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/resources/kafka-topics.txt
    *   **Architectural Requirements:**
        *   List topics: `center-events`, `course-events`, `enrollment-events`, `attendance-events`, `notification-events`.
        *   Define replication factor and partition count (e.g., 3 partitions, replication 1).

#### SUB‑TASK 2.3: Implement Kafka connector in Quarkus (smallrye-reactive-messaging)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/service/kafka/AttendanceEventProducer.java
    *   **Architectural Requirements:**
        *   Use `@Outgoing` channel named `attendance-out` to serialize `Attendance` events as JSON.
        *   Configure connector to `smallrye-kafka` with topic `attendance-events`.

#### SUB‑TASK 2.4: Write integration test for Kafka event flow
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/service/kafka/AttendanceEventProducerIT.java
    *   **Architectural Requirements:**
        *   Start a mock Kafka broker (e.g., `KafkaEmbedded`).
        *   Verify that publishing an `Attendance` event results in a message on the `attendance-events` topic.
        *   Assert message payload matches expected JSON structure.

#### SUB‑TASK 2.5: Review code style and package compliance for Day 2 changes
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/
    *   **Architectural Requirements:**
        *   Ensure all new Java files adhere to the `/org/nlh4j/saas/membership-hub/` path mapping.
        *   Validate imports and line length rules.

#### SUB‑TASK 2.6: Create GCP provisioning script placeholder
##### Assigned Sub-Agent: GCP
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/docker/gcp-provision.sh
    *   **Architectural Requirements:**
        *   Include commands to create a Google Cloud SQL instance (PostgreSQL), enable Cloud KMS, and generate a service account JSON key.
        *   Use `gcloud` CLI commands with placeholders for project ID and region.
        *   Script should be executable (`chmod +x`).

### DAY 3: FRONTEND SCAFFOLDING & KUBERNETES MANIFESTS
#### SUB‑TASK 3.1: Initialize Next.js project with i18n and basic routing
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/next.config.js
    *   **Architectural Requirements:**
        *   Configure `i18n` with supported locales (`en`, `vi`, `zh`).
        *   Set `reactStrictMode` true.
        *   Define `experimental.appDir` for App Router.

#### SUB‑TASK 3.2: Create core page components for admin dashboard
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/pages/dashboard.tsx
    *   **Architectural Requirements:**
        *   Implement a responsive layout using Material‑UI or Tailwind.
        *   Include widgets for “Active Courses Today”, “Teachers on Duty”, “Student Attendance Cards”.
        *   Integrate locale detection via `next-i18next`.

#### SUB‑TASK 3.3: Implement authentication UI (email/password + OAuth)
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/frontend/src/pages/auth/login.tsx
    *   **Architectural Requirements:**
        *   Provide form fields for email/password with validation.
        *   Include sign‑in buttons for Google, Facebook, and Firebase.
        *   Use Next.js API routes (`/api/auth`) for credential verification.

#### SUB‑TASK 3.4: Write Playwright E2E tests for critical user flows
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/frontend/tests/auth.spec.ts
    *   **Architectural Requirements:**
        *   Test login with valid credentials.
        *   Test OAuth redirect to Google/Facebook (mocked).
        *   Verify protected dashboard access after login.

#### SUB‑TASK 3.5: Draft Kubernetes Deployment and Service manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/docker/k8s/deployment.yaml
    *   **Architectural Requirements:**
        *   Define Deployment for Quarkus app (`image: membership-hub-backend:latest`).
        *   Set resource limits (`cpu: 500m`, `memory: 1Gi`).
        *   Configure environment variables for datasource and Kafka bootstrap.
        *   Include liveness and readiness probes (`/q/health`).

#### SUB‑TASK 3.6: Create Service and Ingress manifests
##### Assigned Sub-Agent: GKE
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/docker/k8s/service.yaml
    *   **Architectural Requirements:**
        *   Expose Quarkus app on port 8080 with NodePort.
        *   Label selectors matching the Deployment.
    *   **Target Path:** ./sources/backend/src/main/docker/k8s/ingress.yaml
        *   **Architectural Requirements:**
            *   Define Ingress for both backend (`/api/*`) and frontend (via separate Ingress or same cluster).
            *   Use `nginx-ingress` controller with TLS placeholder.

#### SUB‑TASK 3.7: Final static review and compliance audit
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
*   **Target Path:** ./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/
    *   **Architectural Requirements:**
        *   Verify all Java files are placed under the exact package path.
        *   Ensure no stray files exist outside allowed directories.
        *   Run final SonarQube scan; address any high‑severity issues.

#### SUB‑TASK 3.8: Execute full test suite and health check verification
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
*   **Target Path:** INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/HealthCheckIT.java
    *   **Architectural Requirements:**
        *   Start Quarkus in test mode.
        *   Perform GET `/q/health` and assert status `UP`.
        *   Validate that all required datasources and Kafka connectors are reachable.