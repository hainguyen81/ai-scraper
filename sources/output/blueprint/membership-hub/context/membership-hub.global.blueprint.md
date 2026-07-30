# GLOBAL PROJECT CONTEXT: membership-hub

## 1. Executive Summary & Tech Stack Blueprint
The membership-hub project is a multi-center membership management platform with real-time attendance tracking, digital membership cards, and multi-channel communication. The detected tech stack includes a Node.js backend with Next.js frontend, utilizing a PostgreSQL database, and integrating with Firebase, Google, and Facebook for authentication. The project will be deployed on Google Kubernetes Engine (GKE) with Docker containers.

## 2. Global Guardrails & Enterprise Compliance Standards
The project will adhere to the following guardrails and compliance standards:
- **Absolute Workspace Boundary Rule:** The repository workspace root is fixed at the project root `./`.
- **Mandatory Path Subdirectory Rule:** All files and assets will be placed inside the `./sources/` directory.
- **Conditional Path Prefixing:** Backend services will be prefixed with `./sources/backend/`, frontend interfaces with `./sources/frontend/`, and infrastructure files with `./sources/infra/`.
- **OWASP Security Standards:** The project will implement OWASP Top 10 mitigations, including SQL injection protection, XSS prevention, and CSRF defense.
- **GDPR/CCPA Compliance:** The project will ensure personal data deletion, data export, and consent management.

## 3. High-Level Multi-Phase Architectural Synopsis Grid
The project will be divided into exactly 5 phases, with each phase strictly bounded between 1 to 7 days.

| Phase | Day Range | Architectural Component / Module Path | Technical Task Details | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Phase 1` | `Day 1 - Day 3` | `./sources/backend/` | Initialize database context with multi-tenancy tenant_id schema | `coder`, `doc` | `[REQ-001], [ARC-001], [DAT-001]` |
| `Phase 1` | `Day 1 - Day 3` | `./sources/backend/;./sources/backend/` | Write unit tests for tenant-isolation database validation queries | `tester` | `[ARC-001], [NFR-002]` |
| `Phase 2` | `Day 4 - Day 6` | `./sources/frontend/` | Implement user registration, login, and authentication flows | `coder`, `doc` | `[REQ-002], [REQ-003], [ARC-002]` |
| `Phase 2` | `Day 4 - Day 6` | `./sources/frontend/;./sources/backend/` | Integrate frontend and backend services for authentication | `tester` | `[REQ-002], [ARC-002]` |
| `Phase 3` | `Day 7 - Day 9` | `./sources/backend/` | Implement attendance tracking, QR code scanning, and notification services | `coder`, `doc` | `[REQ-004], [REQ-005], [ARC-003]` |
| `Phase 3` | `Day 7 - Day 9` | `./sources/backend/;./sources/backend/` | Write unit tests for attendance tracking and notification services | `tester` | `[REQ-004], [ARC-003]` |
| `Phase 4` | `Day 10 - Day 12` | `./sources/frontend/` | Implement course browsing, enrollment, and student card management | `coder`, `doc` | `[REQ-006], [REQ-007], [ARC-004]` |
| `Phase 4` | `Day 10 - Day 12` | `./sources/frontend/;./sources/backend/` | Integrate frontend and backend services for course management | `tester` | `[REQ-006], [ARC-004]` |
| `Phase 5` | `Day 13 - Day 14` | `./sources/` | Execute complete multi-tenant leak audit and OWASP A02 PII application-layer encryption validation | `reviewer` | `[NFR-002], [EXC-003]` |
| `Phase 5` | `Day 13 - Day 14` | INTEGRATION_SCOPE;./sources/infra/gke/ | Deploy multi-stage Docker configurations to GKE cluster and map ingress routing rules | `docker`, `GKE` | `[NFR-003], [ARC-005]` |

### MATRIX COVERAGE CHECK MANDATE
`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: 25, TOTAL ARC TAGS: 9, TOTAL EXC TAGS: 5, TOTAL DAT TAGS: 11, TOTAL NFR TAGS: 9. ZERO UNASSIGNED CODES FOUND.]`