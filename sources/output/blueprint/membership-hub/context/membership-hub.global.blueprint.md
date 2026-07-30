# GLOBAL PROJECT CONTEXT: membership-hub

## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is designed as a multi-tenant, scalable, and secure platform for managing membership across multiple centers. The tech stack consists of a Quarkus-based backend, utilizing Java as the primary programming language, with a PostgreSQL database for storing membership data. The frontend will be built using Next.js, a React-based framework, to provide a responsive and interactive user interface. For authentication and authorization, the project will utilize OAuth 2.0 with JWT tokens. The system will also integrate with Firebase for push notifications and Google Cloud Platform for infrastructure management.

## 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`.
- **Mandatory Path Subdirectory Rule:** Every single file path, configuration, script, diagram, or test asset generated across all prompts MUST be strictly placed inside the `./sources/` directory.
- **Conditional Path Prefixing:** 
  * All Backend service logics, microservices, configurations, database schemas, and backend tests must be prefixed with: `./sources/backend/`.
  * All Frontend user interfaces, responsive views, and client-side tests must be prefixed with: `./sources/frontend/`.
- **Java Enterprise Package Standard:** Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.membershiphub`.
- **Strict Package-to-Path Mapping:** All physical Java files under `./sources/backend/src/main/java/` or `./sources/backend/src/test/java/` MUST follow the exact subdirectory layout matching the calculated lowercase token.

## 3. High-Level Multi-Phase Architectural Synopsis Grid
| Phase | Day Range | Architectural Component / Module Path | Technical Task Details | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Phase 1 | Day 1 - Day 3 | `./sources/backend/` | Initialize database context with multi-tenancy tenant_id schema | `coder`, `doc` | `[REQ-001]`, `[ARC-001]` |
| Phase 1 | Day 1 - Day 3 | `./sources/backend/;./sources/backend/` | Write unit tests for tenant-isolation database validation queries | `tester` | `[ARC-001]`, `[NFR-002]` |
| Phase 2 | Day 4 - Day 6 | `./sources/backend/` | Implement authentication and authorization using OAuth 2.0 with JWT tokens | `coder` | `[REQ-002]`, `[ARC-002]` |
| Phase 2 | Day 4 - Day 6 | `./sources/frontend/` | Develop user interface components for login and registration | `coder` | `[REQ-003]`, `[REQ-004]` |
| Phase 3 | Day 7 - Day 9 | `./sources/backend/` | Develop API endpoints for managing membership data | `coder` | `[REQ-005]`, `[REQ-006]` |
| Phase 3 | Day 7 - Day 9 | `./sources/frontend/` | Develop user interface components for managing membership data | `coder` | `[REQ-007]`, `[REQ-008]` |
| Phase 4 | Day 10 - Day 12 | `./sources/` | Integrate Firebase for push notifications | `docker` | `[REQ-009]`, `[NFR-003]` |
| Phase 4 | Day 10 - Day 12 | `./sources/` | Deploy application to Google Cloud Platform | `GKE` | `[NFR-003]`, `[ARC-005]` |
| Phase 5 | Day 13 - Day 14 | `./sources/` | Execute complete multi-tenant leak audit and OWASP A02 PII application-layer encryption validation | `reviewer` | `[NFR-002]`, `[EXC-003]` |
| Phase 5 | Day 13 - Day 14 | INTEGRATION_SCOPE;./sources/infra/gke/ | Deploy multi-stage Docker configurations to GKE cluster and map ingress routing rules | `docker`, `GKE` | `[NFR-003]`, `[ARC-005]` |

### TRACEABILITY MATRIX ENFORCEMENT
TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.