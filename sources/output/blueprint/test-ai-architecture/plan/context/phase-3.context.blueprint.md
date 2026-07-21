# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}
## 1. Phase Operational Scope & Objectives
- **Goal**: Deliver the core functionality defined for Phase {{ phase_idx }} of {{ project_name }} as outlined in the Global Context and Raw Requirements.
- **Key Outcomes**: 
  - Implement the primary technical feature(s) required for this phase.
  - Ensure all implemented components meet the quality and security standards specified in the project requirements.
  - Produce a fully tested, documented, and ready‑to‑deploy artifact set.
- **Duration**: 1 day (hard limit: {{ max_days_per_phase }} days maximum).

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Source Code Directory**: `src/phase{{ phase_idx }}/`
  - All new or modified source files must reside here.
- **Configuration Files**: `config/phase{{ phase_idx }}/`
  - Environment‑specific configs (e.g., `dev.yaml`, `prod.yaml`) are permitted.
- **Test Directory**: `tests/phase{{ phase_idx }}/`
  - Unit, integration, and end‑to‑end tests must be placed here.
- **Documentation**: `docs/phase{{ phase_idx }}/`
  - Include README, API docs, and any user‑facing guides.
- **Endpoints**: 
  - Any new REST API endpoints must follow the pattern `/api/v1/phase{{ phase_idx }}/*`.
  - All endpoints must be defined in `src/phase{{ phase_idx }}/routes.js` (or equivalent).
- **Forbidden Areas**: 
  - No modifications outside the directories above.
  - No cross‑phase file sharing (e.g., importing from other phases) unless explicitly allowed in the Global Context.

## 3. Dedicated Sub-Agent Functional Directives
| Sub‑Agent | Specific Tasks | Deliverables |
|-----------|----------------|--------------|
| **Coder** | - Write clean, idiomatic code implementing the core feature.<br>- Follow the project’s coding standards and naming conventions.<br>- Commit changes with descriptive messages to `src/phase{{ phase_idx }}/`. | Completed source files, committed to version control. |
| **Tester** | - Design and execute unit tests covering all new functions.<br>- Perform integration tests for endpoint interactions.<br>- Validate against the acceptance criteria in the Raw Requirements. | Test suite passing, test coverage report. |
| **Reviewer** | - Conduct code review against standards and best practices.<br>- Verify that all requirements from the Global Context are satisfied.<br>- Approve or request revisions. | Review checklist, approval sign‑off. |
| **DevOps** | - Set up the CI/CD pipeline stage for Phase {{ phase_idx }}.<br>- Build and push container images to the artifact registry.<br>- Deploy the artifact to the designated environment (e.g., staging) for final validation. | Pipeline configuration, deployed artifact, health‑check confirmation. |
| **Documentation Specialist** | - Draft concise README and API documentation in `docs/phase{{ phase_idx }}/`.<br>- Ensure documentation aligns with the project’s style guide. | Completed documentation files. |

## 4. Phase Definition of Done (DoD)
- All core technical objectives for Phase {{ phase_idx }} are fully implemented and integrated.
- Every unit and integration test passes with ≥ 90 % coverage.
- Code review is complete and all reviewer comments are addressed.
- CI/CD pipeline for this phase builds, tests, and deploys successfully.
- Documentation is present, accurate, and accessible in `docs/phase{{ phase_idx }}/`.
- No open issues or blockers remain that prevent progression to the next phase.
- All artifacts are committed, tagged, and stored in the designated repositories.