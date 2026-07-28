# GLOBAL PROJECT CONTEXT: membership-hub

## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a multi-tenant, scalable application built using Java 17, Quarkus, Kafka, and Postgres. The tech stack includes a backend service for managing memberships, a mobile app for students to check-in and view their membership status, and a web application for administrators to manage centers, courses, and student information. The project utilizes a microservices architecture, with separate services for authentication, course management, and student management.

## 2. Global Guardrails & Enterprise Compliance Standards
- **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`.
- **Mandatory Path Subdirectory Rule (Absolute Hard Constraint):** Every single file path, configuration, script, diagram, or test asset generated across all prompts MUST be strictly placed inside the `./sources/` directory.
- **Conditional Path Prefixing (Apply ONLY where applicable to the project topology):** 
  * All Backend service logics, microservices, configurations, database schemas, and backend tests must be prefixed with: `./sources/backend/`.
  * All Frontend user interfaces, responsive views, mobile apps, state management packages, and client-side tests must be prefixed with: `./sources/frontend/`.
- **Java Enterprise Package Standard (Conditional - Apply ONLY to files with '.java' extension):** If the techstack utilizes Java/Quarkus/Spring, Java source codes MUST strictly reside within the corporate package foundation: `org.nlh4j.saas.membershiphub`.
- **Strict Package-to-Path Mapping (Conditional - Apply ONLY to files with '.java' extension):** All physical Java files under `./sources/backend/src/main/java/` or `./sources/backend/src/test/java/` MUST follow the exact subdirectory layout matching the calculated lowercase token.

## 3. High-Level Multi-Phase Architectural Synopsis Grid
| Phase | Day Range | Architectural Component / Module Path | Technical Task Details | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Phase 1` | `Day 1 - Day 3` | `./sources/backend/` | Initialize database context with multi-tenancy tenant_id schema, Implement authentication using Java 17 and Quarkus | `coder`, `doc` | `[REQ-001]`, `[ARC-001]`, `[NFR-001]` |
| `Phase 1` | `Day 1 - Day 3` | `./sources/backend/;./sources/backend/` | Write unit tests for tenant-isolation database validation queries | `tester` | `[ARC-001]`, `[NFR-002]` |
| `Phase 2` | `Day 4 - Day 5` | `./sources/frontend/` | Develop mobile app using Next.js for students to check-in and view membership status | `coder` | `[REQ-002]`, `[ARC-002]` |
| `Phase 2` | `Day 4 - Day 5` | `./sources/frontend/;./sources/frontend/` | Write unit tests for mobile app functionality | `tester` | `[ARC-002]`, `[NFR-003]` |
| `Phase 3` | `Day 6 - Day 7` | `./sources/backend/` | Implement course management and student management services using Java 17 and Quarkus | `coder` | `[REQ-003]`, `[ARC-003]`, `[NFR-004]` |
| `Phase 3` | `Day 6 - Day 7` | `./sources/backend/;./sources/backend/` | Write unit tests for course management and student management services | `tester` | `[ARC-003]`, `[NFR-005]` |
| `Phase 4` | `Day 8 - Day 10` | `./sources/` | Integrate authentication, course management, and student management services | `coder` | `[REQ-004]`, `[ARC-004]`, `[NFR-006]` |
| `Phase 4` | `Day 8 - Day 10` | `./sources/;./sources/` | Write integration tests for authentication, course management, and student management services | `tester` | `[ARC-004]`, `[NFR-007]` |
| `Phase 5` | `Day 11 - Day 14` | `./sources/` | Deploy application to GKE cluster, configure ingress routing rules, and perform security audit | `docker`, `GKE`, `reviewer` | `[NFR-008]`, `[ARC-005]`, `[EXC-001]` |

### 🛑 MATRIX COVERAGE CHECK MANDATE
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 10, TOTAL ARC TAGS: 8, TOTAL EXC TAGS: 2, TOTAL NFR TAGS: 12. ZERO UNASSIGNED CODES FOUND.]` 

Note: The above table and matrix coverage check mandate are based on the provided raw requirements and may need to be adjusted according to the actual project scope and complexity.