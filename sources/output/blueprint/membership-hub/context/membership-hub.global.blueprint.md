# GLOBAL PROJECT CONTEXT: membership-hub

## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a multi-tenant, scalable application built using Java 17, Quarkus, Kafka, and Postgres. The tech stack includes:

* Backend: Java 17, Quarkus, Kafka, Postgres
* Frontend: Next.js, React
* Mobile App: Next.js, React Native
* Deployment: Docker, GCP, GKE
* Security: OWASP, Multi-tenancy, Encryption

The project architecture is a microservices-based system, with separate services for user management, course management, and notification management.

## 2. Global Guardrails & Enterprise Compliance Standards
The project must adhere to the following guardrails and standards:

* **Absolute Workspace Boundary Rule:** The repository workspace root is fixed at the project root `./`.
* **Mandatory Path Subdirectory Rule:** All files must be placed inside the `./sources/` directory.
* **Conditional Path Prefixing:** Backend services must be prefixed with `./sources/backend/`, while frontend services must be prefixed with `./sources/frontend/`.
* **Java Enterprise Package Standard:** Java source codes must reside within the corporate package foundation: `org.nlh4j.saas.membershiphub`.
* **Strict Package-to-Path Mapping:** Java files must follow the exact subdirectory layout matching the calculated lowercase token.
* **Strict Tester Target Path Syntax:** Tester sub-agents must use the literal placeholder token `INTEGRATION_SCOPE` for integration testing.

## 3. High-Level Multi-Phase Architectural Synopsis Grid
The project will be divided into exactly 5 phases, with each phase completed within a duration of 1-7 days. The phase breakdown is as follows:

| Phase | Duration (Days) | Sub-Agent | Tasks |
| --- | --- | --- | --- |
| 1 | 3 | Manager Agent, Coder Agent | Project setup, backend service implementation (user management, course management) |
| 2 | 2 | Coder Agent, Tester Agent | Frontend service implementation (Next.js, React), unit testing |
| 3 | 4 | Coder Agent, Reviewer Agent | Mobile app implementation (Next.js, React Native), integration testing |
| 4 | 3 | GCP Agent, GKE Agent | Deployment setup (Docker, GCP, GKE), security configuration |
| 5 | 5 | Manager Agent, Reviewer Agent | Cross-system integration, performance profiling, OWASP security verification, production deployment |

The tasks and sub-agents are assigned based on the detected project architecture and tech stack. The final phase is reserved for cross-system integration, security verification, and production deployment.

## 4. Phase 1: Project Setup and Backend Service Implementation
In this phase, the project setup will be completed, and the backend services for user management and course management will be implemented.

* Tasks:
	+ Project setup (Manager Agent)
	+ Backend service implementation (user management, course management) (Coder Agent)
* Sub-Agents: Manager Agent, Coder Agent
* Duration: 3 days

## 5. Phase 2: Frontend Service Implementation and Unit Testing
In this phase, the frontend services will be implemented using Next.js and React, and unit testing will be completed.

* Tasks:
	+ Frontend service implementation (Next.js, React) (Coder Agent)
	+ Unit testing (Tester Agent)
* Sub-Agents: Coder Agent, Tester Agent
* Duration: 2 days

## 6. Phase 3: Mobile App Implementation and Integration Testing
In this phase, the mobile app will be implemented using Next.js and React Native, and integration testing will be completed.

* Tasks:
	+ Mobile app implementation (Next.js, React Native) (Coder Agent)
	+ Integration testing (Tester Agent)
* Sub-Agents: Coder Agent, Tester Agent
* Duration: 4 days

## 7. Phase 4: Deployment Setup and Security Configuration
In this phase, the deployment setup will be completed, and security configuration will be implemented.

* Tasks:
	+ Deployment setup (Docker, GCP, GKE) (GCP Agent)
	+ Security configuration (GKE Agent)
* Sub-Agents: GCP Agent, GKE Agent
* Duration: 3 days

## 8. Phase 5: Cross-System Integration, Performance Profiling, and Production Deployment
In this phase, cross-system integration will be completed, performance profiling will be conducted, and the production deployment will be implemented.

* Tasks:
	+ Cross-system integration (Manager Agent)
	+ Performance profiling (Reviewer Agent)
	+ Production deployment (GKE Agent)
* Sub-Agents: Manager Agent, Reviewer Agent, GKE Agent
* Duration: 5 days

The project will be completed within the specified 5 phases, with each phase building on the previous one to ensure a comprehensive and secure implementation of the membership-hub system.