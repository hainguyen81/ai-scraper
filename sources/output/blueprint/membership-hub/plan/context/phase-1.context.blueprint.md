# PHASE 1 CONTEXT BLUEPRINT: membership-hub
## 1. Phase Operational Scope & Objectives
- Define the full project scope, stakeholder requirements, and high‑level architecture for the membership‑hub learning‑center platform.  
- Produce a detailed 5‑phase project plan (including duration, deliverables, and dependencies).  
- Initialize the source‑code repository with the core Java/Quarkus project skeleton, essential configuration files, and basic package structure.  
- Establish a local development environment (Docker‑based) that can spin up PostgreSQL, Kafka, and Quarkus services.  
- Create a CI/CD pipeline (GitHub Actions) that builds, tests, and pushes Docker images to a container registry.  
- Draft code‑review guidelines, contribution docs, and environment‑setup documentation to ensure consistent development practices.  
- Verify that the initial build passes, unit tests run, and the project is ready for Phase 2 (backend development).

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Directory / File | Purpose | Notes |
|-----------------|---------|-------|
| `./` | Project root | Contains `README.md`, `pom.xml`/`build.gradle`, `docker/`, `.github/`, `docs/` |
| `./src/main/java/com/membershiphub/` | Java source code (domain, service, controller) | Package name follows `com.membershiphub` |
| `./src/main/resources/` | Quarkus configuration (`application.yml`, `application-dev.yml`) | Must include datasource, kafka, security properties |
| `./src/main/resources/db/migration/` | Flyway/Liquibase scripts for Postgres schema | Optional but allowed |
| `./docker/` | Container definitions | `Dockerfile` (Quarkus app), `docker-compose.yml` (postgres, kafka, pgadmin) |
| `./.github/workflows/` | CI/CD pipelines | `ci.yml` (build, test, push), `deploy.yml` (optional) |
| `./docs/` | Project documentation | `PROJECT_PLAN.md`, `ARCHITECTURE.md`, `ENVIRONMENT_SETUP.md`, `CONTRIBUTING.md` |
| `./src/test/java/com/membershiphub/` | Unit & integration tests | Uses JUnit 5, Mockito, Quarkus Test extensions |
| `./src/test/resources/` | Test fixtures, Kafka mock topics | Optional |
| `./README.md` | End‑user & developer quick‑start | Must list prerequisites, how to run locally, CI status |

*No other directories or external repositories are permitted for Phase 1 work.*

## 3. Dedicated Sub-Agent Functional Directives (Specific tasks for Coder, Tester, Reviewer, DevOps, etc.)
| Agent | Core Responsibilities for Phase 1 |
|-------|-----------------------------------|
| **Manager** | Draft the high‑level project plan, define phase timelines, identify stakeholders, and create a lightweight risk register. |
| **Coder** | Produce the initial Java/Quarkus project skeleton, essential config files, Docker artifacts, and core documentation. |
| **DevOps** | Build the Docker stack (app + postgres + kafka), define a GitHub Actions CI pipeline, and configure environment variables for local & cloud deployment. |
| **Tester** | Scaffold the test project structure, add a smoke‑test for the main entry point, and configure test‑plugin in build tool. |
| **Reviewer** | Write contribution guidelines, CODEOWNERS, and branch‑protection rules; define a code‑review checklist aligned with enterprise standards. |

## 4. Phase Definition of Done (DoD)
- ✅ Git repository initialized with all required directories and placeholder files.  
- ✅ `pom.xml`/`build.gradle` includes Quarkus platform, PostgreSQL JDBC, Kafka client, Docker Maven plugin, and test dependencies.  
- ✅ `src/main/resources/application.yml` contains placeholders for datasource, Kafka bootstrap servers, and security defaults.  
- ✅ Docker images for the app, PostgreSQL, and Kafka are buildable via `docker-compose up --build`.  
- ✅ GitHub Actions workflow (`ci.yml`) runs on `push`/`pull_request`, executes `mvn clean package` (or `./gradlew clean build`), runs tests, and pushes the Docker image to a specified registry.  
- ✅ Basic test suite (`src/test/java/...`) compiles, runs, and passes a smoke test (e.g., health‑check endpoint).  
- ✅ Documentation (`README.md`, `PROJECT_PLAN.md`, `ARCHITECTURE.md`, `ENVIRONMENT_SETUP.md`, `CONTRIBUTING.md`) is present and references the CI/CD status badge.  
- ✅ Code‑review policies (CODEOWNERS, branch protection) are enforced in the repository.  
- ✅ All Phase 1 artifacts are committed, tagged, and the repository is ready for Phase 2 hand‑off.

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: PROJECT INITIALIZATION AND ENVIRONMENT SETUP

#### SUB‑TASK 1.1: Draft project plan and stakeholder matrix
##### Assigned Sub-Agent: Manager
##### Targeted Components & Technical Requirements:
* **Target Path 1:** `./docs/PROJECT_PLAN.md`
    * **Architectural Requirements:**
        * Document project overview, 5‑phase timeline (Days 1‑21), key milestones, and phase‑gate acceptance criteria.
        * Define roles & responsibilities (Manager, Coder, Tester, Reviewer, DevOps) and communication cadence.
        * Include risk register with high‑level mitigation strategies (e.g., security, compliance, scaling).
        * Reference external artifacts: Global Guardrails, enterprise coding standards, and the provided RAW requirements.

#### SUB‑TASK 1.2: Initialize Git repo and Java/Quarkus skeleton
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path 1:** `./` (repository root)
    * **Architectural Requirements:**
        * Create `.git` init, set default branch `main`, and add an initial `.gitignore` covering `target/`, `.idea/`, `*.log`, `docker/target/`.
* **Target Path 2:** `./pom.xml`
    * **Architectural Requirements:**
        * Declare Quarkus platform version (e.g., `quarkus-platform-bom:3.2.0`), Java 17 source/target compatibility, and essential dependencies: `quarkus-resteasy-reactive`, `quarkus-hibernate-orm`, `quarkus-jdbc-postgresql`, `quarkus-kafka-client`, `quarkus-smallrye-jwt`, `quarkus-oidc`, `quarkus-container-image-docker`.
        * Configure Maven plugin for Docker image building (`quarkus-container-image-docker`).
* **Target Path 3:** `./src/main/java/com/membershiphub/` (package root)
    * **Architectural Requirements:**
        * Create placeholder `Application.java` (main entry point) with `@QuarkusMain` and basic `main` method.
        * Add placeholder `HealthResource.java` exposing `/q/health` for liveness/probes (required by CI).
* **Target Path 4:** `./src/main/resources/application.yml`
    * **Architectural Requirements:**
        * Define `quarkus.datasource.url`, `quarkus.datasource.username`, `quarkus.datasource.password` placeholders.
        * Set `quarkus.kafka.bootstrap-servers` placeholder.
        * Enable security defaults (`quarkus.security.auth-protocols`, `quarkus.http.auth.basic`).

#### SUB‑TASK 1.3: Build Docker stack for local development
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:
* **Target Path 1:** `./docker/Dockerfile`
    * **Architectural Requirements:**
        * Base image `eclipse-temurin:17-jdk-alpine`.
        * Copy `pom.xml` and source code, run `mvn package` (or `./gradlew bootJar`).
        * Set `JAVA_OPTS` for Quarkus native/ JVM options.
        * Expose port `8080`.
        * Define entrypoint to run `java -jar /app/quarkus-run.jar`.
* **Target Path 2:** `./docker/docker-compose.yml`
    * **Architectural Requirements:**
        * Services: `app` (uses `Dockerfile`), `postgres` (image `postgres:15`), `kafka` (image `confluentinc/cp-kafka:7.4`).
        * Define environment variables for DB, Kafka, and Quarkus service discovery.
        * Define network `membership-hub-net`.
        * Add `pgadmin` optional for DB inspection (commented out).

#### SUB‑TASK 1.4: Scaffold test framework and smoke test
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path 1:** `./src/test/java/com/membershiphub/` (test package)
    * **Architectural Requirements:**
        * Create `HealthResourceTest.java` using `@QuarkusTest` to verify `/q/health` returns `200 OK`.
        * Add `Mockito` mocks for external services where needed.
* **Target Path 2:** `./pom.xml` (test plugin config)
    * **Architectural Requirements:**
        * Ensure `maven-surefire-plugin` and `quarkus-junit5` are configured to run tests in the `src/test` directory.

### DAY 2: CI/CD PIPELINE AND CONTAINERIZATION SETUP

#### SUB‑TASK 2.1: Define GitHub Actions CI pipeline
##### Assigned Sub-Agent: DevOps
##### Targeted Components & Technical Requirements:
* **Target Path 1:** `./.github/workflows/ci.yml`
    * **Architectural Requirements:**
        * Trigger on `push` and `pull_request` for `main` branch.
        * Jobs:
            * **Build**: runs on `ubuntu-latest`, checks out code, sets up JDK 17, builds with `mvn clean package` (or `./gradlew clean build`).
            * **Test**: depends on Build, runs unit/integration tests; fails if any test fails.
            * **Docker Build & Push**: runs only on `push` to `main`, builds image using `docker buildx`, tags with `${{ github.sha }}`, pushes to `ghcr.io/<org>/membership-hub`.
        * Include environment secrets for registry credentials (`GITHUB_TOKEN`).
        * Add a step to run `docker compose up -d` for local integration tests (optional).

#### SUB‑TASK 2.2: Establish code‑review guidelines and branch protection
##### Assigned Sub-Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path 1:** `./.github/CONTRIBUTING.md`
    * **Architectural Requirements:**
        * Outline commit message conventions (e.g., `feat:`, `fix:`, `docs:`, `test:`).
        * Define pull‑request template with checklist: code standards, unit test coverage, security review, documentation update.
        * Reference enterprise coding standards and security guardrails.
* **Target Path 2:** `./.github/CODEOWNERS`
    * **Architectural Requirements:**
        * Assign `@org/coders` to `src/main/java/**`, `@org/devops` to `docker/**`, `@org/testers` to `src/test/**`.
        * Enforce required reviewers before merge.
* **Target Path 3:** Repository branch protection settings (via GitHub UI – documented here)
    * **Architectural Requirements:**
        * Require linear history, status checks for CI, and approval from at least one CODEOWNER.

#### SUB‑TASK 2.3: Populate essential documentation
##### Assigned Sub-Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path 1:** `./README.md`
    * **Architectural Requirements:**
        * Provide project overview, tech stack, quick‑start commands (`docker compose up`), CI status badge (`https://img.shields.io/github/actions/...`).
        * Include local development steps, environment variables, and how to run tests.
* **Target Path 2:** `./docs/ARCHITECTURE.md`
    * **Architectural Requirements:**
        * Diagram high‑level layers: UI (Next.js), API Gateway (Quarkus), Services (Java), Data (PostgreSQL), Messaging (Kafka).
        * Note authentication flow (email/password, Firebase, Google, Facebook) and role‑based access control.
* **Target Path 3:** `./docs/ENVIRONMENT_SETUP.md`
    * **Architectural Requirements:**
        * Step‑by‑step for setting up local Docker stack, connecting to Postgres, configuring Kafka topics, and running the app.
        * Reference required ports, default credentials, and security considerations (data encryption, GDPR/CCPA compliance).

#### SUB‑TASK 2.4: Execute initial test suite to validate environment
##### Assigned Sub-Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path 1:** `./src/test/java/com/membershiphub/HealthResourceTest.java`
    * **Architectural Requirements:**
        * Use `@QuarkusTest` and `RestAssured` (or `WebTestClient`) to perform a GET to `/q/health` and assert response status `200` and JSON body containing `status=UP`.
        * Include a test for `/q/metrics` (optional) to confirm metrics endpoint is exposed.
* **Target Path 2:** `./pom.xml` (test execution)
    * **Architectural Requirements:**
        * Ensure `maven-surefire-plugin` runs with `-DskipITs=false` to include integration tests.
        * Configure `quarkus.test.integration-test-profile` to `dev` for local runs.

--- 

**End of Phase 1 Blueprint** – All Day‑1 and Day‑2 tasks are defined, assigned, and bounded. The repository now contains the minimal viable structure, CI pipeline, Docker stack, and documentation required to proceed confidently into Phase 2 (Backend Development).