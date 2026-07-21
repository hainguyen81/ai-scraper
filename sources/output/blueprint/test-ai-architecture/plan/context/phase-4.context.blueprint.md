# PHASE {{ phase_idx }} CONTEXT BLUEPRINT: {{ project_name }}
## 1. Phase Operational Scope & Objectives
- **Goal Alignment**: This phase delivers the core technical capabilities defined in the **Global Context** and the **Raw Requirements** for {{ project_name }}.  
- **Key Outcomes**:  
  1. Implement the primary feature set or infrastructure component required to advance the project toward the final deliverable.  
  2. Establish any necessary integration points or APIs that enable downstream phases.  
  3. Validate that the implemented solution meets the functional and non‑functional criteria outlined in the requirements.  
- **Success Metric**: All core objectives are demonstrably satisfied; no further work is required to meet the defined acceptance criteria.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
- **Source Code**:  
  - `/src/` – All application logic for this phase.  
  - `/src/{{ phase_idx }}_/` – Phase‑specific module (e.g., `auth`, `payment`, `reporting`).  
- **Configuration & Assets**:  
  - `/config/` – Environment‑specific settings (must not expose secrets).  
  - `/docs/` – Phase‑related documentation (API specs, design notes).  
- **Tests & Validation**:  
  - `/tests/` – Unit, integration, and end‑to‑end tests targeting the new functionality.  
- **Endpoints**:  
  - `POST /api/v1/{{ phase_idx }}_/action` – Primary entry point for the phase’s core operation.  
  - `GET /api/v1/{{ phase_idx }}_/status` – Health‑check or status endpoint (read‑only).  
- **Forbidden Areas** (must not be touched):  
  - `/src/previous_phases/` – Legacy code from earlier phases.  
  - `/infra/` – Infrastructure‑as‑code owned by DevOps (outside this phase’s scope).  

## 3. Dedicated Sub-Agent Functional Directives
### Coder
- **Task**: Implement the core business logic and API controllers under `/src/{{ phase_idx }}_/`.  
- **Deliverables**:  
  - Clean, idiomatic code following the project’s style guide.  
  - Comprehensive inline documentation for public methods and endpoints.  
- **Constraints**:  
  - Do **not** modify any files outside `/src/{{ phase_idx }}_/` or `/config/`.  
  - Ensure all new code compiles and passes static analysis.

### Tester
- **Task**: Design and execute test suites that validate the new functionality.  
- **Deliverables**:  
  - Unit tests covering all public methods in `/src/{{ phase_idx }}_/`.  
  - Integration tests that exercise the `POST /api/v1/{{ phase_idx }}_/action` endpoint.  
- **Constraints**:  
  - Tests must run in the CI pipeline without external dependencies.  
  - No test code may be placed outside `/tests/{{ phase_idx }}_/`.

### Reviewer
- **Task**: Conduct a formal code review of all changes introduced by Coder and Tester.  
- **Deliverables**:  
  - Signed-off review comments confirming adherence to coding standards and requirement traceability.  
  - Updated documentation where gaps are identified.  
- **Constraints**:  
  - Review only the files listed in the **Allowed Technical Scope** section.  
  - Provide feedback within the designated review window.

### DevOps
- **Task**: Prepare the deployment artifacts and CI/CD pipeline updates required for this phase.  
- **Deliverables**:  
  - Docker image or deployment manifest for the new service.  
  - Updated pipeline configuration (e.g., GitHub Actions, Jenkins) to build, test, and promote the phase’s artifacts.  
- **Constraints**:  
  - Do **not** modify production environment configurations.  
  - Ensure the pipeline respects the 1‑{{ max_days_per_phase }} day phase duration limit.

## 4. Phase Definition of Done (DoD)
- **Functional Completion**: All core objectives from Section 1 are implemented and verified.  
- **Code Quality**:  
  - All source files are linted, formatted, and pass static analysis.  
  - Unit and integration test coverage meets the project’s minimum threshold (≥ 80 %).  
- **Documentation**:  
  - API specifications and design notes are updated in `/docs/{{ phase_idx }}_/`.  
  - Inline comments are present for all public interfaces.  
- **Testing Validation**:  
  - All automated tests pass in the CI environment.  
  - Manual verification confirms the `POST /api/v1/{{ phase_idx }}_/action` endpoint behaves as expected.  
- **Deployment Readiness**:  
  - Build artifacts are packaged and the CI pipeline can promote them to the staging environment.  
  - No regressions introduced in previously completed phases.  
- **Sign‑off**:  
  - Coder, Tester, Reviewer, and DevOps each provide explicit sign‑off (e.g., via PR comments or ticket closure).  

**Phase {{ phase_idx }} is complete when every item in the DoD is satisfied.**