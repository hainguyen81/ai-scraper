# GLOBAL PROJECT CONTEXT: autosellhub-automation

## 1. Executive Summary & Tech Stack Blueprint
The autosellhub-automation project is a multi-tenant e-commerce platform that utilizes a microservices architecture. The tech stack consists of Node.js, Express.js, and MongoDB. The project requires a dynamic pricing engine, real-time inventory synchronization, and a drag-and-drop campaign builder for advertising. The system must ensure strict access control, data encryption, and compliance with OWASP security standards.

## 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The repository workspace root is fixed at the project root `./`.
- **Mandatory Path Subdirectory Rule:** All files must be placed inside the `./sources/` directory.
- **Conditional Path Prefixing:** 
  * Backend services will be prefixed with `./sources/backend/`.
  * Frontend interfaces will be prefixed with `./sources/frontend/`.
- **Java Enterprise Package Standard:** Not applicable, as the project uses Node.js.
- **Strict Package-to-Path Mapping:** Not applicable, as the project uses Node.js.
- **Strict Tester Target Path Syntax:** Tester target paths will follow the semi-colon separated pair syntax.
- **Memory, Ingestion, & Loop Constraints:** The system will avoid runtime in-memory large dataset loops and utilize native database relational operations.

## 3. High-Level Multi-Phase Architectural Synopsis Grid
The project will be divided into exactly 5 phases, with each phase strictly bounded between 1 to 7 days.

| Phase | Duration (Days) | Description | Sub-Agents |
| --- | --- | --- | --- |
| 1 | 3 | Implement dynamic pricing engine, database schema, and access control | coder, reviewer |
| 2 | 4 | Develop real-time inventory synchronization, campaign builder, and advertising scheduler | coder, tester |
| 3 | 2 | Implement user management, OAuth2 + MFA, and analytics dashboard | coder, reviewer |
| 4 | 3 | Integrate all components, perform cross-system testing, and validate performance | tester, reviewer |
| 5 | 5 | Deploy to production, configure containerized infrastructure, and perform security verification | docker, GCP, GKE |

The following requirements will be implemented in each phase:

* Phase 1:
	+ Epic Module: Autonomous Pricing Engine
	+ Epic Module: Inventory Sync (database schema)
	+ Role-Based Access Control (RBAC) Matrix
* Phase 2:
	+ Epic Module: Inventory Sync (real-time synchronization)
	+ Epic Module: Advertising Scheduler
	+ Epic Module: Campaign Builder
* Phase 3:
	+ Epic Module: User Management
	+ Epic Module: Analytics Dashboard
	+ OAuth2 + MFA
* Phase 4:
	+ Integrate all components
	+ Perform cross-system testing
	+ Validate performance
* Phase 5:
	+ Deploy to production
	+ Configure containerized infrastructure
	+ Perform security verification

The sub-agents will work together to ensure that all requirements are implemented and that the system is secure, scalable, and compliant with OWASP security standards.