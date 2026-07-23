# GLOBAL PROJECT CONTEXT: membership-hub

## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a comprehensive web and mobile application designed for managing memberships, courses, and student information. The tech stack consists of Java 17, Quarkus, Kafka, Postgres, and Docker, with a scalable architecture deployable on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE). The frontend will be built using Next.js, supporting multiple languages and responsive design for both iOS and Android.

## 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`.
- **Mandatory Path Prefixing:** 
  * Backend: `./sources/backend/`
  * Frontend: `./sources/frontend/`
- **Java Enterprise Package Standard:** `org.nlh4j.saas.membership-hub`
- **Strict Package-to-Path Mapping:** Java files under `./sources/backend/src/main/java/` or `./sources/backend/src/test/java/` must follow the exact subdirectory layout matching the package tokens.
- **Strict Tester Target Path Syntax:** `<source_component_or_token>;<test_suite_file_to_execute>`
- **Memory, Ingestion, & Loop Constraints:** Avoid runtime in-memory large dataset loops and delegate complex processing to native database operations.

## 3. Standardized Sub-Agent Persona Definitions
- **Manager Agent:** Oversees cross-phase orchestration and timeline validation.
- **Coder Agent:** Implements core features in `./sources/backend/src/main/` and `./sources/frontend/src/`.
- **Tester Agent:** Owns code verification and emits dual-path semi-colon formats for units or prefixes with `INTEGRATION_SCOPE` for system integration and automated UI/E2E test suites.
- **Reviewer Agent:** Performs static analysis, validates compliance, and acts as an automated compiler fixer.
- **Docker Agent:** Writes multi-stage, secure container configurations localized inside their workspace subdirectories.
- **GCP Agent:** Handles Google Cloud Platform identity access management, cloud storage, and automated cloud resource provisioning setups.
- **GKE Agent:** Responsible for Kubernetes orchestrations, writing deployment manifests, services, ingress configurations, and automated pipeline workflows.

## 4. Multi-Phase Segmentation Strategy Overview (Plan exactly 5 phases)
The project will be segmented into exactly 5 phases, each with a specific focus:
- **Phase 1 (Days 1-3):** Project setup, backend framework setup (Quarkus, Kafka, Postgres), and initial database schema design.
- **Phase 2 (Days 4-5):** Frontend setup (Next.js), responsive design, and initial feature implementation for user management and course management.
- **Phase 3 (Days 6-7):** Implementation of core features such as student registration, course enrollment, and payment processing.
- **Phase 4 (Days 8-10):** Integration of Kafka for event-driven architecture, implementation of notification systems, and initial deployment on GKE.
- **Phase 5 (Days 11-14):** Finalize frontend and backend integration, complete testing (unit, integration, E2E), and deploy the application on GCP.

## 5. Phase-Specific Deliverables and Timeline
Each phase will have specific deliverables and a strict timeline to ensure the project is completed within the required timeframe. The Manager Agent will oversee the progress and ensure that each phase is completed within the allocated time frame (maximum 7 days per phase).