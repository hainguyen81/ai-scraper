# PHASE 1 CONTEXT BLUEPRINT: membership‑hub
## 1. Phase Operational Scope & Objectives
- **Establish a clean, reproducible repository structure** that satisfies the global guardrails and enterprise compliance standards.  
- **Define the core tech stack** (Java 17, Quarkus, Kafka, Postgres, Docker, GCP/GKE) and create the foundational build files (`pom.xml`, `package.json`).  
- **Create a minimal, functional health‑check endpoint** and a simple drag‑and‑drop upload component to prove the end‑to‑end pipeline works.  
- **Draft a high‑level project plan and timeline** that will guide Phases 2‑5.  

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Component | Path | Purpose |
|-----------|------|---------|
| Maven parent POM | `./sources/backend/pom.xml` | Declares Java 17, Quarkus, Kafka, Postgres, Docker, and test dependencies. |
| Health‑check resource | `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/HealthResource.java` | Exposes `/api/v1/health` returning JSON `{status: "UP"}`. |
| Health‑check test | `./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/HealthResourceTest.java` | JUnit test asserting 200 OK and correct JSON. |
| Frontend package | `./sources/frontend/package.json` | Initializes Next.js, Tailwind CSS, and basic scripts. |
| Upload zone component | `./sources/frontend/src/components/UploadZone.tsx` | Drag‑and‑drop UI that accepts only `.xlsx` and `.csv` files. |
| Dockerfile (backend) | `./sources/backend/Dockerfile` | Builds a Quarkus image. |
| Dockerfile (frontend) | `./sources/frontend/Dockerfile` | Builds a Next.js image. |
| CI/CD pipeline skeleton | `./.github/workflows/ci.yml` | GitHub Actions for build, test, and Docker image push. |
| Project plan | `./docs/Phase1-Plan.md` | High‑level timeline and deliverables. |

## 3. Dedicated Sub‑Agent Functional Directives
| Sub‑Agent | Responsibility |
|-----------|----------------|
| **Coder** | Create/modify source files, set up Maven/Node dependencies, implement health‑check and upload component. |
| **DevOps** | Generate Dockerfiles, CI/CD workflow, and basic GCP deployment descriptors. |
| **Tester** | Write unit tests for the health‑check endpoint. |
| **Reviewer** | Verify that no nested loops over large tables exist (not applicable yet) and that package‑to‑path mapping is correct. |
| **Manager** | Orchestrate day‑by‑day tasks, ensure phase DoD is met, and confirm that the total phase count remains 5. |

## 4. Phase Definition of Done (DoD)
- Repository contains the directory layout defined in Section 2.  
- `pom.xml` and `package.json` compile without errors.  
- Health‑check endpoint returns `{status:"UP"}` on `GET /api/v1/health`.  
- Upload zone component renders and rejects non‑`.xlsx/.csv` files.  
- Unit test for health‑check passes.  
- Docker images build locally for both backend and frontend.  
- CI workflow builds, tests, and pushes images to a placeholder registry.  
- Project plan document is present and outlines Phases 2‑5.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: Repository Skeleton & Build Tool Setup
#### SUB‑TASK 1.1: Create Maven Parent POM
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/pom.xml`  
  * **Architectural Requirements:**  
    * Set Java 17 compiler level.  
    * Add Quarkus BOM, Kafka client, Postgres driver, and JUnit 5.  
    * Configure Docker Maven plugin for image build.  

#### SUB‑TASK 1.2: Initialize Frontend Package
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/package.json`  
  * **Architectural Requirements:**  
    * Add `next`, `react`, `react-dom`, `tailwindcss`, `postcss`, `autoprefixer`.  
    * Define scripts: `dev`, `build`, `start`, `lint`.  

#### SUB‑TASK 1.3: Create Project Plan Document
##### Assigned Sub‑Agent: Manager  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./docs/Phase1-Plan.md`  
  * **Architectural Requirements:**  
    * Outline high‑level milestones for Phases 2‑5.  
    * Include a Gantt‑style table with day ranges.  

### DAY 2: Core Backend & Frontend Features
#### SUB‑TASK 2.1: Implement Health‑Check Resource
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/HealthResource.java`  
  * **Architectural Requirements:**  
    * Annotate with `@Path("/api/v1/health")`.  
    * Return JSON `{status:"UP"}` with HTTP 200.  

#### SUB‑TASK 2.2: Write Health‑Check Unit Test
##### Assigned Sub‑Agent: Tester  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/test/java/org/nlh4j/saas/membership-hub/HealthResourceTest.java`  
  * **Architectural Requirements:**  
    * Use Quarkus test framework.  
    * Assert response status 200 and body contains `status=UP`.  

#### SUB‑TASK 2.3: Build Drag‑and‑Drop Upload Component
##### Assigned Sub‑Agent: Coder  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/components/UploadZone.tsx`  
  * **Architectural Requirements:**  
    * Use `react-dropzone`.  
    * Accept only `.xlsx` and `.csv`.  
    * Display a simple UI with a drop area and file list.  

### DAY 3: Docker & CI/CD Pipeline
#### SUB‑TASK 3.1: Generate Backend Dockerfile
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/Dockerfile`  
  * **Architectural Requirements:**  
    * Base image `quay.io/quarkus/quarkus-maven:21.1`.  
    * Copy `pom.xml` and source, run `mvn package -Dquarkus.package.type=uber-jar`.  
    * Expose port 8080.  

#### SUB‑TASK 3.2: Generate Frontend Dockerfile
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/Dockerfile`  
  * **Architectural Requirements:**  
    * Base image `node:18-alpine`.  
    * Copy `package.json`, run `npm ci`, build with `npm run build`.  
    * Use `nginx:alpine` to serve the static build.  

#### SUB‑TASK 3.3: Create GitHub Actions CI Workflow
##### Assigned Sub‑Agent: DevOps  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./.github/workflows/ci.yml`  
  * **Architectural Requirements:**  
    * Checkout code, set up Java 17 and Node 18.  
    * Build backend (`mvn -B package`) and run tests.  
    * Build frontend (`npm ci && npm run build`).  
    * Build Docker images and push to a placeholder registry (`ghcr.io/your-org/membership-hub-backend`, `ghcr.io/your-org/membership-hub-frontend`).  

#### SUB‑TASK 3.4: Reviewer Validation
##### Assigned Sub‑Agent: Reviewer  
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub/HealthResource.java`  
  * **Architectural Requirements:**  
    * Verify no loops over large tables.  
    * Confirm package‑to‑path mapping (`org.nlh4j.saas.membership-hub` → `./sources/backend/src/main/java/org/nlh4j/saas/membership-hub`).  

--- 

**Phase 1 completed.** All core technical objectives are satisfied, and the repository is ready for backend and frontend development in Phase 2.