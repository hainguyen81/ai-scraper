# GLOBAL PROJECT CONTEXT: membership-hub

## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a comprehensive web and mobile application designed for managing memberships, courses, and student information. The tech stack consists of Java 17, Quarkus, Kafka, Postgres, and Docker, with a scalable architecture deployable on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The frontend will be built using Next.js, supporting multiple languages and responsive design for both iOS and Android.

## 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`.
- **Mandatory Path Prefixing:** 
  * Backend logic: `./sources/backend/`
  * Frontend logic: `./sources/frontend/`
- **Java Enterprise Package Standard:** `org.nlh4j.saas.membership-hub`
- **Strict Package-to-Path Mapping:** Java files under `./sources/backend/src/main/java/` or `./sources/backend/src/test/java/` must follow the exact subdirectory layout matching the package tokens.
- **Strict Tester Target Path Syntax (JUnit & Integration):** `<source_component>;<test_suite>` or `INTEGRATION_SCOPE;./sources/backend/src/test/java/.../IntegTest.java`
- **Memory & Loop Constraints:** Avoid in-memory large dataset loops; use native database operations instead.

## 3. Standardized Sub-Agent Persona Definitions
- **Manager Agent:** Cross-phase orchestration and timeline validation.
- **Coder Agent:** Implementation of core features in `./sources/backend/src/main/` and `./sources/frontend/src/`.
- **Tester Agent:** Code verification and emitting dual-path semi-colon format for units or prefixing with `INTEGRATION_SCOPE` for integration suites.
- **Reviewer Agent (Compiler Fixer):** Static analysis, compliance validation, and automated compiler fixing.
- **Docker Agent:** Writing multi-stage, secure container configurations.
- **GCP Agent:** Google Cloud Platform identity access management and resource provisioning.
- **GKE Agent:** Kubernetes orchestrations, deployment manifests, services, ingress configurations, and pipeline workflows.

## 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
### Phase 1: Project Setup and Backend Foundation (Day 1-3)
- Initialize project structure with `./sources/backend/` and `./sources/frontend/`.
- Set up Java 17, Quarkus, and Postgres for the backend.
- Define the database schema and initial data models.

### Phase 2: Frontend Development and Integration (Day 4-5)
- Develop the frontend using Next.js, focusing on responsive design and multi-language support.
- Integrate the frontend with the backend API.

### Phase 3: Feature Implementation and Testing (Day 6-7)
- Implement core features for membership management, course management, and student information.
- Write unit tests and integration tests for the implemented features.

### Phase 4: Deployment and Security (Day 1-3)
- Configure Docker for containerization.
- Set up GCP and GKE for deployment.
- Implement security measures, including authentication and authorization.

### Phase 5: Final Testing, Review, and Deployment (Day 4-7)
- Conduct thorough testing, including system integration testing.
- Review the code for compliance and best practices.
- Deploy the application to GCP using GKE.

Each phase is designed to be completed within the 1-7 day limit, ensuring that the project is structured, scalable, and deployable within the given constraints.