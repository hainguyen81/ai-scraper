# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}
## 1. Phase Operational Scope & Objectives
- **Goal**: Advance the overall project ({{ project_name }}) toward the final deliverable by completing the specific technical objectives defined for this phase ({{ phase_idx }} of {{ num_phases }}).  
- **Key Outcomes**:  
  1. Implement the core functionality required by the raw requirements for this phase.  
  2. Ensure all artifacts are integrated, tested, and ready for the next phase.  
  3. Produce documentation and hand‑off artifacts that satisfy the Phase Definition of Done (DoD).  
- **Constraints**:  
  - The phase must be completed within **{{ max_days_per_phase }} days** (hard limit).  
  - Work must stop as soon as the core technical objectives are satisfied—no unnecessary extensions or duplicated tasks.  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Category | Allowed Paths / Endpoints | Notes |
|----------|---------------------------|-------|
| **Source Code** | `src/{{ phase_idx }}_/` (e.g., `src/01_/`, `src/02_/`, …) | Only files directly related to this phase’s objectives. |
| **Configuration** | `config/{{ phase_idx }}_/` | Environment‑specific configs for this phase. |
| **Tests** | `tests/{{ phase_idx }}_/` | Unit, integration, and acceptance tests that validate the phase’s deliverables. |
| **Documentation** | `docs/phases/{{ phase_idx }}_/` | Phase‑specific README, design notes, and API docs. |
| **Build / CI** | `.github/workflows/phase-{{ phase_idx }}.yml` | CI pipelines that trigger builds/tests for this phase only. |
| **External APIs** | Any endpoints listed in the **Raw Requirements** that are explicitly required for this phase. | No external services beyond those mandated. |
| **Data / Assets** | `data/{{ phase_idx }}_/` | Input data or generated artifacts needed for this phase. |

*All other directories, files, or endpoints are **out of scope** for this phase and must not be created, modified, or referenced.*

## 3. Dedicated Sub-Agent Functional Directives
| Sub‑Agent | Specific Tasks for This Phase |
|-----------|--------------------------------|
| **Coder** | 1. Implement the core logic defined in the **Raw Requirements** for Phase {{ phase_idx }}. <br>2. Commit changes to the `src/{{ phase_idx }}_/` directory following the project’s naming conventions. <br>3. Ensure code adheres to the style guide and passes linting. |
| **Tester** | 1. Write unit and integration tests covering the new functionality in `tests/{{ phase_idx }}_/`. <br>2. Execute the test suite and verify 100 % pass rate before any hand‑off. <br>3. Record any defects and coordinate fixes with the Coder. |
| **Reviewer** | 1. Perform a code review of all changes in `src/{{ phase_idx }}_/` and `tests/{{ phase_idx }}_/`. <br>2. Validate that the implementation matches the **Raw Requirements** and the **Global Context**. <br>3. Approve or request revisions; once approved, sign off in the phase tracking artifact. |
| **DevOps** | 1. Set up the CI workflow `.github/workflows/phase-{{ phase_idx }}.yml` (if not already present) to build, test, and deploy the phase artifacts. <br>2. Ensure the pipeline runs within the allowed time budget ({{ max_days_per_phase }} days). <br>3. Publish the built artifacts to the designated staging area for verification. |
| **Documentation Specialist** | 1. Create/update the Phase {{ phase_idx }} README in `docs/phases/{{ phase_idx }}_/`. <br>2. Document any new APIs, configuration changes, or data formats introduced. <br>3. Ensure documentation is linked from the project’s main documentation index. |
| **Security / Compliance (if applicable)** | 1. Review the phase’s code and configurations for security best practices. <br>2. Verify compliance with any regulatory or data‑privacy constraints referenced in the **Global Context**. <br>3. Sign off on the security checklist before final hand‑off. |

*Each sub‑agent works **independently** and **exclusively** on the tasks listed above. No sub‑agent may modify files outside its designated scope.*

## 4. Phase Definition of Done (DoD)
- **Code**: All core functionality from the **Raw Requirements** is implemented, merged, and passes the full test suite (100 % pass rate).  
- **Tests**: Comprehensive test coverage exists for the new code, and all tests are passing in the CI pipeline.  
- **Review**: The Coder’s changes have been reviewed and approved by the Reviewer, with all comments addressed.  
- **Build / CI**: The phase‑specific CI workflow runs successfully, builds the artifacts, and deploys them to the staging environment.  
- **Documentation**: Phase‑specific documentation is complete, accurate, and linked from the main project docs.  
- **Security / Compliance**: Any required security reviews or compliance checks have been completed and signed off.  
- **Artifacts**: All required artifacts (source code, tests, configs, documentation, and build outputs) are stored in their respective `{{ phase_idx }}_/` directories and are ready for the next phase.  
- **Hand‑off**: A formal hand‑off checklist is signed by the Reviewer and DevOps, confirming that the phase meets all criteria and is ready for progression.  

*Once every item in the DoD is satisfied, the phase is considered complete. No further tasks or timeline extensions are generated.*