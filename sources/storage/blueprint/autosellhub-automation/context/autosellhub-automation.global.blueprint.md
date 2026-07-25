# GLOBAL PROJECT CONTEXT: autosellhub-automation

## 1. Executive Summary & Tech Stack Blueprint
The autosellhub-automation project is a multi-tenant e-commerce automation platform that utilizes a microservices architecture. The tech stack consists of Node.js, Express.js, MongoDB, and Docker. The project will be built using a modular approach, with each module representing a separate microservice. The platform will provide features such as AI-powered pricing suggestions, real-time inventory synchronization, and multi-channel advertising.

## 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`.
- **Mandatory Path Subdirectory Rule:** Every single file path, configuration, script, diagram, or test asset generated across all prompts MUST be strictly placed inside the `./sources/` directory.
- **Conditional Path Prefixing:** 
  * All Backend service logics, microservices, configurations, database schemas, and backend tests must be prefixed with: `./sources/backend/`.
  * All Frontend user interfaces, responsive views, mobile apps, state management packages, and client-side tests must be prefixed with: `./sources/frontend/`.
- **Java Enterprise Package Standard:** Not applicable, as the project uses Node.js.
- **Strict Package-to-Path Mapping:** Not applicable, as the project uses Node.js.
- **Strict Tester Target Path Syntax:** Any component targeted by a Tester Sub-Agent must be structured as a strict semi-colon separated pair `<source_component_or_token>;<test_suite_file_to_execute>`.
- **Memory, Ingestion, & Loop Constraints:** All generated code structures must strictly avoid runtime in-memory large dataset loops.

## 3. High-Level Multi-Phase Architectural Synopsis Grid
The project will be divided into exactly 5 phases, with each phase strictly bounded between 1 to 7 days max. The phase breakdown strategy will follow an incremental feature distribution approach, with the final phase reserved for cross-system integration, performance profiling, and production deployment.

| Phase | Duration (Days) | Description | Sub-Agents |
| --- | --- | --- | --- |
| 1 | 3 | Implement User Management, Authentication, and Authorization | coder, tester, reviewer |
| 2 | 4 | Develop Autonomous Pricing Engine, Inventory Sync, and Advertising Scheduler | coder, tester, reviewer |
| 3 | 3 | Build Analytics Dashboard, KPI Reporting, and Data Visualization | coder, tester, reviewer |
| 4 | 4 | Implement Multi-Tenancy, Data Isolation, and Security Features | coder, tester, reviewer |
| 5 | 5 | Cross-System Integration, Performance Profiling, and Production Deployment | coder, tester, reviewer, docker, GCP, GKE |

The following table maps the exact distribution of components and requirements across the 5 phases:

| Component | Requirement | Phase |
| --- | --- | --- |
| User Management | Implement User Management, Authentication, and Authorization | 1 |
| Autonomous Pricing Engine | Develop AI-powered pricing suggestions | 2 |
| Inventory Sync | Develop real-time inventory synchronization | 2 |
| Advertising Scheduler | Develop multi-channel advertising scheduler | 2 |
| Analytics Dashboard | Build analytics dashboard and KPI reporting | 3 |
| Multi-Tenancy | Implement multi-tenancy and data isolation | 4 |
| Security Features | Implement security features and OWASP compliance | 4 |
| Production Deployment | Deploy application to production environment | 5 |

## 4. Phase 1: User Management, Authentication, and Authorization
In this phase, the coder sub-agent will implement user management, authentication, and authorization features. The tester sub-agent will write unit tests and integration tests for these features. The reviewer sub-agent will perform static code analysis and review the code for security compliance.

## 5. Phase 2: Autonomous Pricing Engine, Inventory Sync, and Advertising Scheduler
In this phase, the coder sub-agent will develop the autonomous pricing engine, inventory sync, and advertising scheduler features. The tester sub-agent will write unit tests and integration tests for these features. The reviewer sub-agent will perform static code analysis and review the code for security compliance.

## 6. Phase 3: Analytics Dashboard, KPI Reporting, and Data Visualization
In this phase, the coder sub-agent will build the analytics dashboard, KPI reporting, and data visualization features. The tester sub-agent will write unit tests and integration tests for these features. The reviewer sub-agent will perform static code analysis and review the code for security compliance.

## 7. Phase 4: Multi-Tenancy, Data Isolation, and Security Features
In this phase, the coder sub-agent will implement multi-tenancy, data isolation, and security features. The tester sub-agent will write unit tests and integration tests for these features. The reviewer sub-agent will perform static code analysis and review the code for security compliance.

## 8. Phase 5: Cross-System Integration, Performance Profiling, and Production Deployment
In this phase, the coder sub-agent will perform cross-system integration and ensure that all components work together seamlessly. The tester sub-agent will write integration tests and perform performance profiling. The reviewer sub-agent will review the code for security compliance and ensure that all requirements are met. The docker sub-agent will create Docker containers for the application. The GCP sub-agent will configure Google Cloud Platform resources. The GKE sub-agent will configure Kubernetes clusters and deploy the application to production.