# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}
## 1. Phase Operational Scope & Objectives
- **Goal**: Execute the core technical objectives defined for this phase within the overall project ({{ project_name }}) as outlined in the Global Context and Raw Requirements.
- **Focus Areas**:
  1. Align deliverables with the high‑level project vision captured in the Global Context.
  2. Satisfy the specific functional and non‑functional requirements listed in the Raw Requirements.
  3. Ensure all work stays within the permitted technical boundaries (see Section 2).
- **Success Criteria**: The phase is complete when the deliverables explicitly listed under the Phase Definition of Done (DoD) are produced and verified.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Source Code**:
  - `src/` – All application source files.
  - `tests/` – Test suites for unit, integration, and end‑to‑end scenarios.
- **Configuration**:
  - `config/` – Project‑wide configuration files (e.g., `app.yml`, `database.yml`).
  - `.env.example` – Example environment variables.
- **Documentation**:
  - `docs/` – Architectural and user documentation.
- **Build / Deployment**:
  - `Dockerfile` / `docker-compose.yml` – Container definitions.
  - `CI/` – Continuous‑integration pipeline definitions.
- **Endpoints** (if applicable):
  - All HTTP(S) routes defined in the API specification (`api.yaml`).
- **Restricted Areas**:
  - No direct modifications to `node_modules/`, `.git/`, or any generated artifacts unless explicitly permitted in the Global Context.

## 3. Dedicated Sub-Agent Functional Directives
| Sub‑Agent | Primary Tasks | Hand‑off Criteria |
|-----------|---------------|-------------------|
| **Coder** | • Implement the core logic required by the phase.<br>• Write clean, idiomatic code following the project’s style guide.<br>• Commit changes with descriptive messages. | Code compiles/runs, passes basic linting, and includes unit tests. |
| **Tester** | • Design and execute test cases covering the new functionality.<br>• Record and report any failures or edge‑case issues.<br>• Update test coverage metrics. | All tests pass; test coverage meets the minimum threshold defined in the Global Context. |
| **Reviewer** | • Perform code review against the established standards.<br>• Verify that the implementation aligns with the Raw Requirements.<br>• Approve or request revisions. | Review checklist completed; no critical issues remain. |
| **DevOps** | • Ensure the build and deployment pipelines can incorporate the new artifacts.<br>• Validate container images and configuration changes.<br>• Update any required documentation for operations. | CI/CD pipeline runs successfully; artifacts are deployable to the staging environment. |
| **Documenter** *(if applicable)* | • Capture design decisions, API changes, and usage instructions.<br>• Update the `docs/` folder with phase‑specific notes. | Documentation is coherent, formatted correctly, and linked from the main README. |

## 4. Phase Definition of Done (DoD)
- [ ] All core technical objectives from the Raw Requirements are implemented and functional.
- [ ] Source code passes linting, formatting, and static analysis checks.
- [ ] Unit and integration tests covering the new functionality achieve the required coverage (≥ 80 % unless otherwise specified).
- [ ] All tests in the test suite pass without failures or errors.
- [ ] Code review checklist is signed off by the Reviewer.
- [ ] Build artifacts are successfully generated and can be deployed to the staging environment via the CI/CD pipeline.
- [ ] Updated documentation (if any) is committed and reviewed.
- [ ] No outstanding issues or blockers remain that prevent progression to the next phase.