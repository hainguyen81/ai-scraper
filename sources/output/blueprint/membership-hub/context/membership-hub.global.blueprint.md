# GLOBAL PROJECT CONTEXT: membership-hub

## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a multi-tenant, scalable application with both web and mobile components. The tech stack consists of Java 17, Quarkus, Kafka, Postgres, and Docker, with deployment on Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE). The project requires a robust authentication system, with support for internal authentication via email and password, as well as external authentication via Firebase, Google, and Facebook. The application will have various roles, including System Admin, Admin, Manager, Teacher, and Student, each with distinct permissions and access levels.

## 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`.
- **Conditional Path Prefixing:** 
  * All Backend service logics, microservices, configurations, database schemas, and backend tests must be prefixed with: `./sources/backend/`.
  * All Frontend user interfaces, responsive views, mobile apps, state management packages, and client-side tests must be prefixed with: `./sources/frontend/`.
- **Java Enterprise Package Standard:** All source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.membership-hub`.
- **Strict Package-to-Path Mapping:** This package structure dictates that all physical Java files under `./sources/backend/src/main/java/` or `./sources/backend/src/test/java/` MUST follow the exact subdirectory layout matching the package tokens.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`.
- **Memory, Ingestion, & Loop Constraints:** All generated code structures must strictly avoid runtime in-memory large dataset loops.

## 3. High-Level Multi-Phase Architectural Synopsis Grid
| Phase | Duration (Days) | Sub-Agent | Tasks |
| --- | --- | --- | --- |
| 1 | 3 | Coder Agent, Reviewer Agent | Implement authentication system, setup database schema, create backend services for user management |
| 2 | 4 | Coder Agent, Tester Agent | Develop frontend components, implement responsive views, create mobile app, setup state management packages |
| 3 | 2 | Coder Agent, Reviewer Agent | Implement business logic for course management, setup payment gateway, integrate with Kafka for event-driven architecture |
| 4 | 3 | Tester Agent, Reviewer Agent | Perform unit testing, integration testing, and end-to-end testing, validate OWASP compliance |
| 5 | 2 | GCP Agent, GKE Agent, Docker Agent | Setup GCP infrastructure, deploy application on GKE, create Docker containers, configure CI/CD pipeline |

Note: The tasks and sub-agents assigned to each phase are based on the raw requirements and the detected project architecture layout. The duration of each phase is estimated and may vary depending on the complexity of the tasks.