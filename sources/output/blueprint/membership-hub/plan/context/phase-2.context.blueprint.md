# PHASE 2 CONTEXT BLUEPRINT: membership-hub
## 1. Phase Operational Scope & Objectives
- **Core Technical Objectives**  
  1. Build a fully‑functional Java 17 Quarkus backend with Kafka integration, Postgres persistence, and JWT‑based authentication (email/password, Firebase, Google, Facebook).  
  2. Define the essential domain entities (`User`, `Center`, `Course`, `Attendance`, `Enrollment`) and expose REST resources for CRUD and attendance marking.  
  3. Implement a minimal Next.js frontend that supports login, language detection, and a placeholder dashboard.  
  4. Deliver Docker images, CI/CD pipeline definitions, and basic integration tests.  
  5. Ensure compliance with global guardrails: package‑to‑path mapping, absolute workspace boundary, and no in‑memory large‑dataset loops.

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
| Layer | Path Prefix | Example Files | Notes |
|-------|-------------|---------------|-------|
| **Backend** | `./sources/backend/` | `pom.xml`, `src/main/java/...`, `src/test/java/...` | All Java source, tests, and build descriptors. |
| **Frontend** | `./sources/frontend/` | `package.json`, `src/pages/...`, `src/components/...` | All TypeScript/React/Next.js files. |
| **Docker** | `./sources/backend/` | `Dockerfile`, `docker-compose.yml` | Build context for backend. |
| **CI/CD** | `./sources/backend/` | `.github/workflows/...` | GitHub Actions for build, test, deploy. |

**Endpoints (Backend)**  
- `GET /api/v1/health` – health check.  
- `POST /api/v1/auth/login` – email/password login.  
- `POST /api/v1/auth/register` – user registration.  
- `GET /api/v1/centers` – list centers.  
- `GET /api/v1/courses` – list courses.  
- `POST /api/v1/attendance/scan` – QR scan attendance.  

**Frontend Pages**  
- `/login` – login form.  
- `/dashboard` – placeholder dashboard.  

## 3. Dedicated Sub-Agent Functional Directives
| Agent | Responsibility | Key Deliverables |
|-------|----------------|------------------|
| **Coder** | Implement all Java and TypeScript source files, Dockerfiles, and CI configs. | Source files, Dockerfile, `package.json`, Next.js pages. |
| **Tester** | Write unit tests for services and resources; integration tests for multi‑component flows. | JUnit test classes, integration test suites. |
| **Reviewer** | Perform static analysis, enforce no nested loops over large tables, validate package‑to‑path mapping. | Review reports, code comments. |
| **DevOps** | Create Docker images, compose files, and CI/CD pipelines. | `Dockerfile`, `docker-compose.yml`, GitHub Actions workflow. |

## 4. Phase Definition of Done (DoD)
- All core entities, services, and resources compile and pass unit tests.  
- Authentication flow works end‑to‑end (frontend → backend → Postgres).  
- Attendance marking endpoint publishes a Kafka event.  
- Docker image builds successfully and passes integration tests.  
- CI pipeline runs tests, builds image, and deploys to a GKE staging cluster.  
- Reviewer approves code with no violations of guardrails.  

## 5. DAY‑BY‑DAY ARCHITECTURAL EXECUTION LOGS

### DAY 1: BACKEND BOILERPLATE & HEALTH ENDPOINT
#### SUB‑TASK 1.1: Configure Enterprise Multi‑Module Backend
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/pom.xml`  
  * **Architectural Requirements:**  
    * Define parent POM, Quarkus BOM, Postgres driver, Kafka client, and JWT dependencies.  
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/HealthResource.java`  
  * **Architectural Requirements:**  
    * Expose `/api/v1/health` returning JSON `{status: "UP"}`.  

#### SUB‑TASK 1.2: Initialize Frontend Boilerplate
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/package.json`  
  * **Architectural Requirements:**  
    * Scripts for `dev`, `build`, `lint`, Tailwind CSS integration.  
* **Target Path:** `./sources/frontend/src/pages/_app.tsx`  
  * **Architectural Requirements:**  
    * Wrap application with Tailwind provider and language context.  

#### SUB‑TASK 1.3: Unit Test Health Endpoint
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/HealthResource.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/HealthResourceTest.java`  
  * **Architectural Requirements:**  
    * Assert HTTP 200 and JSON body contains `status=UP`.  

---

### DAY 2: AUTHENTICATION – EMAIL/ PASSWORD
#### SUB‑TASK 2.1: Implement User Entity & Repository
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/User.java`  
  * **Architectural Requirements:**  
    * JPA entity with fields: `id`, `email`, `passwordHash`, `roles`, `centerId`.  
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/UserRepository.java`  
  * **Architectural Requirements:**  
    * CRUD repository, findByEmail.  

#### SUB‑TASK 2.2: Create Auth Service & Resource
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java`  
  * **Architectural Requirements:**  
    * Password hashing (BCrypt), JWT generation, login logic.  
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AuthResource.java`  
  * **Architectural Requirements:**  
    * Endpoints: `/api/v1/auth/login`, `/api/v1/auth/register`.  

#### SUB‑TASK 2.3: Frontend Login Page
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/pages/login.tsx`  
  * **Architectural Requirements:**  
    * Form with email/password, submit to `/api/v1/auth/login`, store JWT in localStorage.  

#### SUB‑TASK 2.4: Unit Tests for Auth Service
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AuthService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AuthServiceTest.java`  
  * **Architectural Requirements:**  
    * Test password hashing, JWT claims, login success/failure.  

---

### DAY 3: DOMAIN ENTITIES – CENTER & COURSE
#### SUB‑TASK 3.1: Center Entity & Repository
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/Center.java`  
  * **Architectural Requirements:**  
    * Fields: `id`, `name`, `address`, `taxCode`, `adminUserId`.  
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/CenterRepository.java`  
  * **Architectural Requirements:**  
    * CRUD repository.  

#### SUB‑TASK 3.2: Course Entity & Repository
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/Course.java`  
  * **Architectural Requirements:**  
    * Fields: `id`, `centerId`, `title`, `description`, `startDate`, `endDate`, `teacherId`.  
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/CourseRepository.java`  
  * **Architectural Requirements:**  
    * CRUD repository, findByCenterId.  

#### SUB‑TASK 3.3: Center & Course Resources
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/CenterResource.java`  
  * **Architectural Requirements:**  
    * Endpoints: `GET /api/v1/centers`, `POST /api/v1/centers`.  
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/CourseResource.java`  
  * **Architectural Requirements:**  
    * Endpoints: `GET /api/v1/courses`, `POST /api/v1/courses`.  

#### SUB‑TASK 3.4: Frontend Center & Course Pages
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/pages/centers.tsx`  
  * **Architectural Requirements:**  
    * Fetch and display list of centers.  
* **Target Path:** `./sources/frontend/src/pages/courses.tsx`  
  * **Architectural Requirements:**  
    * Fetch and display list of courses.  

#### SUB‑TASK 3.5: Integration Test for Center CRUD
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/integration/CenterIntegrationTest.java`  
  * **Architectural Requirements:**  
    * Create a center, retrieve it, update, delete, and assert database state.  

---

### DAY 4: ATTENDANCE & QR SCAN
#### SUB‑TASK 4.1: Attendance Entity & Repository
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/model/Attendance.java`  
  * **Architectural Requirements:**  
    * Fields: `id`, `userId`, `courseId`, `scanTimestamp`.  
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/repository/AttendanceRepository.java`  
  * **Architectural Requirements:**  
    * CRUD repository, findByUserIdAndDate.  

#### SUB‑TASK 4.2: Attendance Service & Resource
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java`  
  * **Architectural Requirements:**  
    * `scanAttendance(userId, courseId)` – idempotent per day.  
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/resource/AttendanceResource.java`  
  * **Architectural Requirements:**  
    * `POST /api/v1/attendance/scan` – accepts JSON `{userId, courseId}`.  

#### SUB‑TASK 4.3: Frontend Attendance Scan Component
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/frontend/src/components/AttendanceScan.tsx`  
  * **Architectural Requirements:**  
    * QR code scanner (using `react-qr-reader`), submit to backend, display success message.  

#### SUB‑TASK 4.4: Unit Test for Attendance Service
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/service/AttendanceServiceTest.java`  
  * **Architectural Requirements:**  
    * Test idempotency, date filtering, and event publishing stub.  

---

### DAY 5: KAFKA INTEGRATION
#### SUB‑TASK 5.1: Kafka Producer Configuration
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/config/KafkaProducerConfig.java`  
  * **Architectural Requirements:**  
    * Configure `io.smallrye.reactive.messaging` producer for topic `attendance-events`.  

#### SUB‑TASK 5.2: Publish Attendance Event
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java`  
  * **Architectural Requirements:**  
    * After successful scan, emit JSON `{userId, courseId, timestamp}` to Kafka.  

#### SUB‑TASK 5.3: Integration Test for Kafka Event
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/integration/AttendanceKafkaTest.java`  
  * **Architectural Requirements:**  
    * Use embedded Kafka, trigger scan, assert message received on `attendance-events`.  

#### SUB‑TASK 5.4: Reviewer Static Analysis
##### Assigned Sub‑Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/service/AttendanceService.java`  
  * **Architectural Requirements:**  
    * Verify no nested loops over large tables; confirm use of indexed queries.  

---

### DAY 6: DEVOPS – DOCKER & CI
#### SUB‑TASK 6.1: Dockerfile for Backend
##### Assigned Sub‑Agent: DevOps
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/Dockerfile`  
  * **Architectural Requirements:**  
    * Multi‑stage build: Maven compile → Quarkus native image → minimal Alpine runtime.  

#### SUB‑TASK 6.2: Docker Compose for Local Development
##### Assigned Sub‑Agent: DevOps
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/docker-compose.yml`  
  * **Architectural Requirements:**  
    * Services: `backend`, `postgres`, `kafka`.  

#### SUB‑TASK 6.3: GitHub Actions Workflow
##### Assigned Sub‑Agent: DevOps
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/.github/workflows/ci.yml`  
  * **Architectural Requirements:**  
    * Steps: checkout, setup JDK 17, build, test, docker build, push to GCP Artifact Registry.  

#### SUB‑TASK 6.4: Integration Test for Docker Build
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/integration/DockerBuildTest.java`  
  * **Architectural Requirements:**  
    * Spin up container, run health check, assert status 200.  

---

### DAY 7: FINAL REVIEW & DO NOTIFY
#### SUB‑TASK 7.1: Reviewer Final Pass
##### Assigned Sub‑Agent: Reviewer
##### Targeted Components & Technical Requirements:
* **Target Path:**  
  * `./sources/backend/src/main/java/org/nlh4j/saas/membershiphub/**`  
  * `./sources/frontend/src/**`  
  * `./sources/backend/Dockerfile`  
  * `./sources/backend/docker-compose.yml`  
  * **Architectural Requirements:**  
    * Confirm package‑to‑path mapping, no forbidden loops, all tests passing, and code coverage ≥ 80%.  

#### SUB‑TASK 7.2: Release Notes & Documentation
##### Assigned Sub‑Agent: Coder
##### Targeted Components & Technical Requirements:
* **Target Path:** `./sources/backend/README.md`  
  * **Architectural Requirements:**  
    * Document API endpoints, Docker usage, environment variables, and deployment steps.  

#### SUB‑TASK 7.3: Final Integration Test – End‑to‑End Flow
##### Assigned Sub‑Agent: Tester
##### Targeted Components & Technical Requirements:
* **Target Path:** `INTEGRATION_SCOPE;./sources/backend/src/test/java/org/nlh4j/saas/membershiphub/integration/FullE2ETest.java`  
  * **Architectural Requirements:**  
    * Register user → login → create center/course → scan attendance → verify Kafka event → health check.  

---

**Phase 2 Complete** – All core objectives met, DoD satisfied, and ready for Phase 3 (Frontend Expansion).