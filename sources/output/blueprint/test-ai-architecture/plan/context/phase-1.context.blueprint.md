# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}
## 1. Phase Operational Scope & Objectives
- **Goal Alignment**: Leverage the insights from the **Global Context** and the **Raw Requirements** to define and deliver the specific technical outcomes required for this phase of {{ project_name }}.
- **Key Objectives**:
  1. Translate high‑level business or system requirements into concrete implementation plans.
  2. Establish clear boundaries for development, testing, review, and deployment activities.
  3. Produce a shippable artifact (e.g., code module, configuration, documentation) that satisfies the phase‑specific functional criteria.
- **Success Indicators**:
  - All defined objectives are met or exceeded.
  - Deliverables are ready for hand‑off to the next phase without ambiguity.
  - No open technical debt that would block subsequent phases.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Source Code**:
  - `src/` – all application source files.
  - `src/{{ project_name }}/` – project‑specific modules.
- **Configuration**:
  - `config/` – environment and deployment configuration files.
- **Tests**:
  - `tests/` – unit, integration, and acceptance test suites.
- **Documentation**:
  - `docs/` – user guides, API docs, and architecture diagrams.
- **Build / CI**:
  - `ci/` – pipeline definitions, scripts, and Dockerfiles.
- **Endpoints** (if applicable):
  - All HTTP(S) endpoints defined in the requirements (e.g., `/api/v1/{{ project_name }}/*`).
- **Restricted Areas**:
  - No access to production databases, external third‑party services, or any files outside the listed directories unless explicitly granted.

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
| Sub‑Agent | Core Tasks | Deliverables |
|-----------|------------|--------------|
| **Coder** | 1. Implement the required features/modules based on the phase objectives.<br>2. Follow the coding standards and naming conventions defined in the global context.<br>3. Commit code with descriptive messages and appropriate tags. | • Source code files in `src/{{ project_name }}/`<br>• Unit test stubs (if applicable) |
| **Tester** | 1. Design and execute test cases covering the new functionality.<br>2. Validate that the implemented code meets the acceptance criteria.<br>3. Log any defects and verify fixes. | • Test reports and coverage metrics |
| **Reviewer** | 1. Perform code review against the established standards.<br>2. Ensure alignment with project requirements and global context.<br>3. Approve or request revisions. | • Review comments and approval sign‑off |
| **DevOps** | 1. Set up the build pipeline for the new artifacts.<br>2. Deploy artifacts to the designated non‑production environment for validation.<br>3. Update any necessary infrastructure as per the phase scope. | • CI/CD pipeline configuration<br>• Deployment manifests |
| **Documentation Specialist** *(if part of the team)* | 1. Draft or update relevant documentation (API docs, README, architecture diagrams).<br>2. Ensure documentation is synchronized with code changes. | • Updated documentation files in `docs/` |

## 4. Phase Definition of Done (DoD)
- **Code**: All required functionality implemented, unit tests passing, and code reviewed & approved.
- **Testing**: Comprehensive test suite executed with ≥ 80 % coverage (or as defined) and no open critical defects.
- **Documentation**: All necessary documentation updated and reviewed.
- **Build/CI**: Pipeline built, artifacts packaged, and successfully deployed to the staging environment.
- **Sign‑off**: All sub‑agents have confirmed completion and the phase is ready for hand‑off.
- **Constraints Met**: The phase does not exceed the maximum allowed duration of **{{ max_days_per_phase }} days** and stops as soon as the core objectives are satisfied.